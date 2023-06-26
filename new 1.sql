SELECT TOP (1000) [id]
      ,[number]
      ,[response]
      ,[date_added]
  FROM [test].[dbo].[Data_for_G:Bot]


  select '{User}' as user_,'{Q_Number}' as q_
  
  
  number,0 as status_,getdate() as date_ 
	
	
	
	--CREATE TABLE [dbo].[User_Question_Logs](
--	[id] [int] IDENTITY(1,1) NOT NULL,
--	[User_Number] [varchar](40) NOT NULL,
--	[Q_number] [varchar](20) NOT NULL,
--	[Response_Status] bit NOT NULL,
--	[Sent_On] datetime NOT NULL,
--PRIMARY KEY CLUSTERED 
--(
--	[id] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
--) ON [PRIMARY]
--GO


select * from User_Question_Logs

update User_Question_Logs
set		Response_Status = 0, Sent_On = getdate()


delete from user_question_logs where id = 3

select *,datediff(hour,sent_on,getdate()) as HourDiff from User_Question_Logs where User_Number = '+923214075902' and Response_Status = 1;

--insert into User_Question_Logs
--values
--('+923214075902','1',0,dateadd(hour, -48, getdate()))


--CREATE TABLE [dbo].[User_Response_Logs](
--	[id] [int] IDENTITY(1,1) NOT NULL,
--	[User_Number] [varchar](40) NOT NULL,
--	[Q_number] [varchar](20) NOT NULL,
--	[Response] [varchar](10) NOT NULL,
--	[Received_On] datetime NOT NULL,
--PRIMARY KEY CLUSTERED 
--(
--	[id] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
--) ON [PRIMARY]
--GO

select * from User_Response_Logs


insert into Questions_List
values
('2','How has your income changed in the past 11 months?','1. I am earning more money\n2. I am earning less money\n3. I no longer have an income\n4. My income has not changed',1,getdate()),
('3','If you have additional income, how do you spend that money?','a. To pay for day-to-day expenses\nb. To pay off debt\nc. To save for financial goals\nd. To save for retirement\ne. I don’t have additional sources of income',1,getdate()),
('4','How often have you prepared a budget in the past 11 months?','a. Every month\nb. Some months\nc. Hardly ever\nd. Never',1,getdate()),
('5','How are you budgeting differently in the past 11 months?','a. I started budgeting straight after I attended the WageWise training\nb. I started budgeting a few weeks after attending the WageWise training\nc. My budgeting behaviour has not changed\nd. I budget less regularly\ne. I budget more regularly',1,getdate()),
('6','Are you happy with the way you have been budgeting over the past 11 months?','a. Yes, I have made good progress towards achieving my budgeting goals\nb. No, I am not happy with the progress I have made towards achieving my budgeting goals\nc. I did not want to change my budgeting behaviour',1,getdate()),
('7','How often have you reached your savings goal in the past 11 months?','a. Every month\nb. Some months\nc. Hardly ever\nd. Never',1,getdate()),
('8','How often have you had to use your savings to cover your day-to-day expenses in the past 11 months?','a. Every month\nb. Some months\nc. Hardly ever\nd. Never',1,getdate()),
('9','How are you saving differently in the past 11 months?','a. I started saving straight after I attended the WageWise training\nb. I started saving a few months after attending the WageWise training\nc. I do not save at all\nd. I save less often\ne. I save more often',1,getdate()),
('10','Are you happy with the way you have been saving over the past 11 months?','a. Yes, I have made good progress towards achieving my saving goals\nb. No, I am not happy with the progress I have made towards achieving my saving goals\nc. I did not want to change my saving behaviour',1,getdate()),
('11','In the past 11 months, how often have you struggled to pay your debts on time?','a. I always struggled to pay my debts on time\nb. I sometimes struggled to pay my debts in time\nc. I hardly ever struggled to pay my debts on time\nd. I never struggled to pay my debts on time\ne. I do not have any debt',1,getdate()),
('12','If you have struggled to pay your debt on time over the past 11 months, what have you done to help manage your debt? Select all the options that apply to you.','a. I have negotiated my interest rate\nb. I have asked family and friends for money\nc. I have approached a debt counsellor for advice\nd. I have referred to the WageWise financial education content for tips\ne. I have used my savings to pay my debts\nf. I have missed my debt repayment\ng. I have not struggled to pay my debt on time',1,getdate()),
('13','If you had a financial emergency in the past 11 months, do you think that the information you learned from the WageWise programme helped you?','a. Helped you to cope\nb. Helped you to speak to someone you trust about your financial situation\nc. Helped you to speak to your employer about your financial concerns\nd. Did not help you cope\ne. I did not experience a financial emergency in the past 11 months',1,getdate()),
('14','If you have negotiated an interest rate when taking up new credit, or when signing new credit contracts in the past 11 months, did you use any information learned from the WageWise resources?','a. Yes, I have\nb. No, I have not negotiated an interest rate when taking up new credit or signing new credit contracts',1,getdate()),
('15','What has been your main financial goal over the past 11 months?','a. To budget more regularly\nb. To save more for emergencies\nc. To reduce my debt\nd. To borrow less\ne. To plan for retirement\nf. All of the above\ng. I do not have a financial goal',1,getdate()),
('16','Has the information you have learned from WageWise encouraged you to make changes to your retirement plan?','a. Yes\nb. No\nc. I did not want to make changes to my retirement plan',1,getdate()),
('17','How do you feel about your progress in achieving your financial goal over the past 11 months?','a. I have achieved my financial goal\nb. I am happy with the progress I have made\nc. I am not happy with the progress I have made\nd. I have not made any progress\ne. I do not have a financial goal',1,getdate()),
('18','Over the past 11 months, has the information you received during the WageWise training changed the way you manage your money?','a. Yes\nb. No\nc. I did not want to change the way I manage my money',1,getdate()),
('19','Over the past 11 months, how often have you worried about financially supporting yourself and/or your family?','a. I have always worried about supporting myself and/or my family\nb. I have sometimes worried supporting myself and/or my family\nc. I have hardly ever worried about supporting myself and/or my family\nd. I have never worried supporting myself and/or my family',1,getdate()),
('20','Over the past 11 months, has the information you received from WageWise affected your level of stress regarding money?','a. I have become less stressed about managing my money\nb. I have become more stressed about managing my money\nc. My stress levels regarding money have not changed',1,getdate())


--CREATE TABLE [dbo].[Questions_List](
--	[id] [int] IDENTITY(1,1) NOT NULL,
--	[number] [varchar](20) NOT NULL,
--	[Question] [varchar](1000) NOT NULL,
--	[Options] [varchar](4096) NOT NULL,
--	[Status] bit NOT NULL,
--	[Added_On] datetime NOT NULL,
--PRIMARY KEY CLUSTERED 
--(
--	[id] ASC
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
--) ON [PRIMARY]
--GO

--insert into Questions_List
--Values
--('-3','Hello😀Genesis Analytics invites you to participate in the ASISA Foundation’s WageWise financial education midline survey where you answer questions and earn R100 worth of airtime.','',1,Getdate()),
--('-2','Your personal information and responses will not be shared and are only used for research purposes. Your participation will not impact your ability to participate in WageWise or affect your ability to receive future financial or training support.','',1,getdate()),
--('-1','This will not take up much of your time but is longer than the surveys you receive each month. You can stop at any time by sending STOP. STOP will remove you from our system and you will not receive any more messages from us. To participate in the survey and earn R100 airtime, please send Yes to continue.','',1,getdate()),
--('0','Thank you for agreeing to participate! We have 20 questions for you to answer. When you’ve answered all 20	questions, R100 airtime will be on its way to you. Please select your response by responding with the number that matches your answer.','',1,getdate()),
--('Thanks Continue','Thank you for your answers so far! Keep going - you’re nearly finished!','',1,getdate()),
--('Invalid','Sorry, please try answering again. Remember to send only the number that matches the answer you want to choose.','',1,getdate())

--('1','Who makes the decisions about money in your household?','1. I make the decisions about money\n2. Myself and my partner\n3. My partner/ Spouse\n4. Another family member\n5. Someone outside of my family\n6. Prefer not to say',1,getdate())


select * from Questions_List

