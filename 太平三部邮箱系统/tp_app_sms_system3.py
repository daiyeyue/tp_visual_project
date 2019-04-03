import random
import datetime

#day = input("请输入日期，日期格式如：" + '2019-04-04 00:00:00')
day = '2019-04-05 00:00:00'


sen_first = "insert into tp_app3_sms_system_3 (sample_time, failed_reason, failed_reason_count) values('"
for i in range(1,97):
    failed_reason_list = ['MK001','MK002','MK003','MK004','MK005']
    markTime = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
    for failed_reason in failed_reason_list:
        failed_reason_count = str(random.randint(0, 50))
        #markTime = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
        print(sen_first + str(markTime) + "'" + ",'" + failed_reason + "'," + failed_reason_count + ');')
    markTime = markTime - datetime.timedelta(minutes=15)
    day = datetime.datetime.strftime(markTime,'%Y-%m-%d %H:%M:%S')



