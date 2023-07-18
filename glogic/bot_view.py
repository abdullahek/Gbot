from . import app, db#, WebScrapea
from .gresponses import Dictionary
from .models import User
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from . import Long_Question_Common as lrq
from . import send_airtime as sa

@app.route('/message', methods=['GET', 'POST'])
def bot():
    print("request")
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()

    status = lrq.check_survey_status(num)
    new, pending, responses_list = lrq.Send_Survey_Question(num, 'New')

    print(new)
    print(pending)
    print(responses_list)
    print(status)

    if status > 0:
        resp = MessagingResponse()
        msg = resp.message()
        message = 'Survey has already been taken'
        msg.body(message)
    else:

        # db.save(User(number=num,
        #              response=incoming_msg))

        resp = MessagingResponse()
        msg = resp.message()

        new, pending, responses_list = lrq.Send_Survey_Question(num,'New')
        # print(new)
        Message=''
        if new is None:
            print("Here it is")
            Message = "Thank you! You have completed the survey and you’ve earned R100 airtime which is on its way to you now. As part of your participation in the study, someone from Genesis Analytics will contact you to hear about how WageWise has helped you to manage your money so far. If you want to stop receiving the surveys, please send STOP."
            lrq.Vipe_clean_user_question_logs(num)
            msg.body(Message)
        elif incoming_msg in ['End','end']:
            lrq.Vipe_clean_user_question_logs(num)

            Message = "Please type Hi to re-start the process."

            msg.body(Message)
        elif incoming_msg is not None and incoming_msg not in ['Hi','hi','HI'] and new is not None:
            new, pending, responses_list = lrq.Send_Survey_Question(num, 'Response')
            print("Printing responses_list")
            print(responses_list)
            Options = responses_list[0]['Options']
            response = ''
            if responses_list[0]['Multi'] == True:
                split_char = ''
                data =[]
                if ' ' in incoming_msg:
                    split_char = ' '
                    data = incoming_msg.split(split_char)
                elif ',' in incoming_msg:
                    split_char = ','
                    data = incoming_msg.split(split_char)
                else:
                    split_char = ''
                    data = [char for char in incoming_msg]

                # data = incoming_msg.split(split_char)
                for r in data:
                    print(r)
                    print(responses_list)
                    count = responses_list[0]['count']
                    response = lrq.Validate_Options(Options, r)
                    if response == 'valid':
                        continue
                    else:
                        # Message = "Sorry, please try answering again. Remember to send only the number that matches the answer you want to choose."
                        break
                if response == 'valid':
                    lrq.add_User_response(num, incoming_msg)
                    new, pending, responses_list = lrq.Send_Survey_Question(num, 'New')
                    # print(new)
                    lrq.add_Question_Sent_Log(new, num)
                    for r_ in new:
                        if (count >= 21):
                            print('At 21 count')
                            lrq.Vipe_clean_user_question_logs(num)
                            sa.send_airtime_after_survey(num, 100)

                        Message = Message + '\n\n' + r_['Question'] + "\n\n" + r_['Options']
                else:
                    Message = "Sorry, please try answering again. Remember to send only the letter that matches the answer you want to choose."
            else:
                response = lrq.Validate_Options(responses_list[0]['Options'], incoming_msg)
                if response == 'valid':
                    lrq.add_User_response(num,incoming_msg)
                    new, pending, responses_list = lrq.Send_Survey_Question(num, 'New')
                    # print(new)
                    lrq.add_Question_Sent_Log(new, num)
                    for r in new:
                        print("Here it is2")
                        Message = Message + '\n\n' + r['Question'] + "\n\n" + r['Options']


                else:
                    Message = "Sorry, please try answering again. Remember to send only the letter that matches the answer you want to choose."

            print(Message)
            msg.body(Message)

        elif new is not None and incoming_msg is not None:
            for r in new:
                Message = Message + '\n\n' + r['Question']
                # lrq.add_Question_Sent_Log(new, num)
            lrq.add_Question_Sent_Log(new, num)
            msg.body(Message)



    return str(resp)

