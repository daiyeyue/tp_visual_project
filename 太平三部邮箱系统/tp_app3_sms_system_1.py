import random
import datetime

#day = input("请输入日期，日期格式如：" + '2019-04-04 00:00:00')
day = '2019-04-05 00:00:00'


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
    markTime = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
    print(sen_first + str(markTime) + "'" + ',' + sms_received_volume + ',' + sms_sent_volume + ',' + sms_underwrite_volume + ',' + wechat_verification_code + ',' + unicom + ',' + mobile + ',' + success_rate + ',' + sms_avg_response_time + ');')
    markTime = markTime - datetime.timedelta(minutes=15)
    day = datetime.datetime.strftime(markTime,'%Y-%m-%d %H:%M:%S')



