import random
import datetime

day = '2019-04-03'
#date_time = datetime.datetime.strptime(str, '%Y-%m-%d')
#markTime = date_time - datetime.timedelta(minutes=15)
#print(markTime)


sen_first = "insert into tp_app3_sms_system_1 (sample_time, sms_received_volume, sms_sent_volume, sms_underwrite_volume, wechat_verification_code, 95589_unicom, 95589_mobile, success_rate, sms_avg_response_time) values('"
for i in range(1,97):
    sms_received_volume = str(random.randint(1500, 2500))
    sms_sent_volume = str(random.randint(1500, 2500))
    sms_underwrite_volume = str(random.randint(0, 200))
    wechat_verification_code = str(random.randint(0, 200))
    unicom = str(random.randint(0, 200))
    mobile = str(random.randint(0, 200))
    success_rate = str(random.randint(90, 99) + random.random())
    sms_avg_response_time = str(random.uniform(0.02, 0.05))
    date_time = datetime.datetime.strptime(day, '%Y-%m-%d')
    markTime = str(date_time - datetime.timedelta(minutes=15))


    print(sen_first + markTime + "'" + ',' + sms_received_volume + ',' + sms_sent_volume  + ',' + sms_underwrite_volume + ',' + wechat_verification_code  + ',' + unicom + ',' + mobile + ',' + success_rate + ',' + sms_avg_response_time + ')')

    #print("insert into tp_app3_sms_system_1 (sample_time, sms_received_volume, sms_sent_volume, sms_underwrite_volume, wechat_verification_code, 95589_unicom, 95589_mobile, success_rate, sms_avg_response_time) values('2019-04-03 00:00:00',1236,1458,30,548,1476,1475,80,0.034);")
