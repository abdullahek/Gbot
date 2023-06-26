from . import app, db#, WebScrapea
from .gresponses import Dictionary
from .models import User
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from . import Long_Question_Common as lrq


@app.route('/message', methods=['GET', 'POST'])
def bot():
    print("request")
    num = request.form.get('From')
    num = num.replace('whatsapp:', '')
    incoming_msg = request.form.get('Body').lower()



    # db.save(User(number=num,
    #              response=incoming_msg))

    resp = MessagingResponse()
    msg = resp.message()

    new, pending, responses_list = lrq.Send_Survey_Question(num,'New')
    # print(new)
    Message=''
    if new is None:
        Message = "Thank you! You have completed the survey and you’ve earned R100 airtime which is on its way to you now. As part of your participation in the study, someone from Genesis Analytics will contact you to hear about how WageWise has helped you to manage your money so far. If you want to stop receiving the surveys, please send STOP."

        msg.body(Message)
    elif incoming_msg in ['End','end']:
        lrq.Vipe_clean_user_question_logs(num)

        Message = "Please type Hi to re-start the process."

        msg.body(Message)
    elif incoming_msg is not None and incoming_msg not in ['Hi','hi','HI'] and new is not None:
        new, pending, responses_list = lrq.Send_Survey_Question(num, 'Response')
        print("Printing responses_list")
        print(responses_list)
        response = lrq.Validate_Options(responses_list[0]['Options'], incoming_msg)
        if response == 'valid':
            lrq.add_User_response(num,incoming_msg)
            new, pending, responses_list = lrq.Send_Survey_Question(num, 'New')
            # print(new)
            lrq.add_Question_Sent_Log(new, num)
            for r in new:
                Message = Message + '\n\n' + r['Question'] + "\n\n" + r['Options']


        else:
            Message = "Sorry, please try answering again. Remember to send only the number that matches the answer you want to choose."

        msg.body(Message)

    elif new is not None and incoming_msg is not None:
        for r in new:
            Message = Message + '\n\n' + r['Question']
            # lrq.add_Question_Sent_Log(new, num)
        lrq.add_Question_Sent_Log(new, num)
        msg.body(Message)



    return str(resp)

