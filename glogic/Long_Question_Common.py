import pyodbc


def Get_DB_conn():
    for retry in range(3):
        try:
            conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                  'Server=localhost;'
                                  'Database=test;'
                                  # 'Trusted_Connection=yes;'
                                  ';UID=sa;'
                                  'PWD=saPwd123')
            cursor = conn.cursor()
            return conn,cursor
        except Exception as e:
            print('failed')
            continue
    raise  # throw if the retry fails too often

def Send_Survey_Question(User,Type):
    try:

        conn, cursor = Get_DB_conn()

        pending_list = []
        new_questions = []
        responses_list = []

        if Type == 'Pending':
            query = f"select *,datediff(hour,sent_on,getdate()) as HourDiff from User_Question_Logs where User_Number = '{User}' and Response_Status = 0;"
            cursor.execute(query)
            for i in cursor:

                if i[5]>48 or i[5]>168:
                    message = f"Sending message to {i[1]} after {i[5]} hours. Since, there isn't any response received against last question."
                    print(message)
                    query = f"SELECT * FROM Questions_List where status = 1 and number = '{i[2]}';"
                    cursor.execute(query)
                    question = cursor.fetchone()
                    question = question[2]
                    user_question_list = {
                                            "User"      :   i[1],
                                            "Question"  :   question[2]
                                         }
                    pending_list.append(user_question_list)
                else:
                    print("No pending Responses")
        elif Type == "New":
            query = f"select max(cast(Q_number as int)) as Last_question_id from User_Question_Logs where User_Number = '{User}';"
            cursor.execute(query)
            question = cursor.fetchone()

            message = f"Sending message to {User} for new question after Question ID {question[0]}."
            print(message)

            if question[0] is None:
                query = f"SELECT * FROM Questions_List where status = 1 and number in ('-3','-2','-1');"
            else:

                query = f"SELECT  top 1 * FROM Questions_List where status = 1 and cast(number as integer) > cast('{question[0]}' as integer) and number not in ('Thanks Continue','Invalid');"
                print(query)
            cursor.execute(query)
            question = cursor.fetchall()
            for i in question:
                question_ = i[2]
                Options = i[3]
                id = i[1]
                json_list = {
                                "Q_Number": id,
                                "Question": question_.replace('$','\n'),
                                'Options': Options.replace('$',"\n")
                }
                new_questions.append(json_list)
        elif Type == "Response":
            query = f"select max(Q_number) as Last_question_id ,(select count(1) from User_Question_Logs where user_number = '{User}') as q_count from User_Question_Logs where User_Number = '{User}' and Response_Status = 0 and datediff(hour,sent_on,getdate())<48;"
            cursor.execute(query)
            question = cursor.fetchone()

            question_options = f"select Options_list from Questions_List where number = '{question[0]}';"
            cursor.execute(question_options)
            Options_question = cursor.fetchone()
            if Options_question:
                print(Options_question[0])

                output = Options_question[0].split(',')
                print(output)

                message = f"Message received from {User} agianst Question ID {question[0]} and current question count is {question[1]}."
                print(message)

                response = {
                    "Question": question[0].replace('$',"\n"),
                    "Options": output,
                    "count": question[1]
                }

                responses_list.append(response)

        return new_questions,pending_list,responses_list
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def add_User_response(User, Response):
    try:
        conn, cursor = Get_DB_conn()
        new, pending, responses_list = Send_Survey_Question(User, 'Response')

        if responses_list:

            query = f"insert into User_Response_Logs select * from ( select '{User}' as user_,'{responses_list[0]['Question']}' as response_q,'{Response}' as response_,getdate() as received_on) as e where not exists (select 1 from User_Response_Logs l where l.user_number = e.user_ and l.response = e.response_ and l.q_number = e.response_q);"

            cursor.execute(query)

            cursor.commit()

            update_status = f"Update User_Question_Logs set response_status = 1 where user_number = '{User}' and Q_Number = '{responses_list[0]['Question']}' and response_status = 0;"

            cursor.execute(update_status)

            cursor.commit()

            print("Response saved successfully!!")
        else:
            print("No pending questions!!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def add_Question_Sent_Log(Q_List,User):
    try:
        conn, cursor = Get_DB_conn()

        for i in Q_List:
        # Q_List
            print(i['Q_Number'])
        if i['Q_Number']=='21':
            query = f"insert into User_Question_Logs select * from (select '{User}' as user_,'{i['Q_Number']}' as q_number,1 as status_,getdate() as date_ ) as r where not exists (select 1 from User_Question_Logs L where L.User_Number = R.user_ and L.Q_Number = R.Q_Number and L.Response_Status = 0 );"
        else:
            query = f"insert into User_Question_Logs select * from (select '{User}' as user_,'{i['Q_Number']}' as q_number,0 as status_,getdate() as date_ ) as r where not exists (select 1 from User_Question_Logs L where L.User_Number = R.user_ and L.Q_Number = R.Q_Number and L.Response_Status = 0 );"
        cursor.execute(query)
        cursor.commit()
        print("Question has been logged succeddfully!!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def Validate_Options(Options, Response):
    try:
        if Response in Options:
            return "valid"
        else:
            return "invalid"
    except Exception as e:
        print(e)
    # finally:

def Vipe_clean_user_question_logs(User):
    try:
        conn, cursor = Get_DB_conn()

        query = f"delete from User_Question_Logs where User_Number = '{User}';"
        cursor.execute(query)
        cursor.commit()
        print("Question history has been Removed successfully!!")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# new, pending, responses_list = Send_Survey_Question('+923214075902','New')
#
# print(new)
# print("--------------------")
# print(pending)
# print("--------------------")
# print(responses_list)
# #
# Validate_Options(responses_list[0]['Options'],'a')
#
# add_User_response("+923214075902",'a')
#
# new, pending, responses_list = Send_Survey_Question('+9232140759021','New')
# #
# print(new)
# print("--------------------")
# print(pending)
# print("--------------------")
# print(responses_list)
#
# add_Question_Sent_Log(new,"+923214075902")
#
# Validate_Options(responses_list[0]['Options'],'a')
#
# add_User_response("+923214075902",'a')