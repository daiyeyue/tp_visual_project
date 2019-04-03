import random
import datetime

#day = input("请输入日期，日期格式如：" + '2019-04-04 00:00:00')
day = '2019-04-05 00:00:00'


sen_first = "insert into tp_app3_sms_system_2 (sample_time, sms_rs_middledb_received_volume, sms_rs_rmi_received_volume, sms_rs_total_received_volume, sms_rs_sucess_sent_volume, sms_rs_failed_sent_volume, sms_cx_middledb_received_volume, sms_cx_rmi_received_volume, sms_cx_total_received_volume, sms_cx_sucess_sent_volume, sms_cx_failed_sent_volume, sms_yl_middledb_received_volume, sms_yl_rmi_received_volume, sms_yl_total_received_volume, sms_yl_sucess_sent_volume, sms_yl_failed_sent_volume, max_response_time, avg_response_time, sms_underwrite_volume, sms_rs_underwrite_volume, sms_cx_underwrite_volume, sms_yl_underwrite_volume, wechat_verification_code, wechat_rs_verification_code, wechat_cx_verification_code, wechat_yl_verification_code) values('"
for i in range(1,97):
    sms_rs_middledb_received_volume = str(random.randint(1500, 2500))
    sms_rs_rmi_received_volume = str(random.randint(1500, 2500))
    sms_rs_total_received_volume = str(random.randint(1500, 2500))
    sms_rs_sucess_sent_volume = str(random.randint(1500, 2500))
    sms_rs_failed_sent_volume = str(random.randint(1500, 2500))
    sms_cx_middledb_received_volume = str(random.randint(1500, 2500))
    sms_cx_rmi_received_volume = str(random.randint(1500, 2500))
    sms_cx_total_received_volume = str(random.randint(1500, 2500))
    sms_cx_sucess_sent_volume = str(random.randint(1500, 2500))
    sms_cx_failed_sent_volume = str(random.randint(1500, 2500))
    sms_yl_middledb_received_volume = str(random.randint(1500, 2500))
    sms_yl_rmi_received_volume = str(random.randint(1500, 2500))
    sms_yl_total_received_volume = str(random.randint(1500, 2500))
    sms_yl_sucess_sent_volume = str(random.randint(1500, 2500))
    sms_yl_failed_sent_volume = str(random.randint(1500, 2500))
    max_response_time = str(random.uniform(0.02, 0.05))
    avg_response_time = str(random.uniform(0.02, 0.05))
    sms_underwrite_volume = str(random.randint(1500, 2500))
    sms_rs_underwrite_volume = str(random.randint(1500, 2500))
    sms_cx_underwrite_volume = str(random.randint(1500, 2500))
    sms_yl_underwrite_volume = str(random.randint(1500, 2500))
    wechat_verification_code = str(random.randint(1500, 2500))
    wechat_rs_verification_code = str(random.randint(1500, 2500))
    wechat_cx_verification_code = str(random.randint(1500, 2500))
    wechat_yl_verification_code = str(random.randint(1500, 2500))
    markTime = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
    print(sen_first + str(markTime) + "'" + ',' + sms_rs_middledb_received_volume + ',' + sms_rs_rmi_received_volume + ',' + sms_rs_total_received_volume + ',' + sms_rs_sucess_sent_volume + ',' + sms_rs_failed_sent_volume + ',' + sms_cx_middledb_received_volume + ',' + sms_cx_rmi_received_volume + ',' + sms_cx_total_received_volume + ',' + sms_cx_sucess_sent_volume + ',' + sms_cx_failed_sent_volume + ',' + sms_yl_middledb_received_volume + ',' + sms_yl_rmi_received_volume + ',' + sms_yl_total_received_volume + ',' + sms_yl_sucess_sent_volume + ',' + sms_yl_failed_sent_volume + ',' + max_response_time + ',' + avg_response_time + ',' + sms_underwrite_volume + ',' + sms_rs_underwrite_volume + ',' + sms_cx_underwrite_volume + ',' + sms_yl_underwrite_volume + ',' + wechat_verification_code + ',' + wechat_rs_verification_code + ',' + wechat_cx_verification_code + ',' + wechat_yl_verification_code +');')
    markTime = markTime - datetime.timedelta(minutes=15)
    day = datetime.datetime.strftime(markTime,'%Y-%m-%d %H:%M:%S')



