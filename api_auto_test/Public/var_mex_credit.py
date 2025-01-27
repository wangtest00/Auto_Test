__all__=['host_api','host_action','host_mgt','host_pay','head_api','head_mgt','head_pay','CONFIGS','which_db']

which_db='mex_credit'
host_api="https://test-api.lanadigital.mx"
host_action="https://test-action.lanadigital.mx"
host_mgt="https://test-mgt.lanadigital.mx/"
host_pay="https://test-pay.lanadigital.mx"
head_api={"user-agent": "Dart/2.12 (dart:io)","x-user-language": "es","x-auth-token": "Bearer" ,"accept-encoding": "gzip","content-length": "63","host": "test-api.lanadigital.mx","x-app-name": "LanaDigital","content-type": "application/json",
        "x-app-type": "10090001","x-app-version": "116","x-app-no": "208" }

head_mgt={"Host": "test-mgt.lanadigital.mx","Connection": "keep-alive","Content-Length": "55",
"sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',"Accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
"Content-Type": "application/json;charset=UTF-8","Origin": "https://test-mgt.lanadigital.mx","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty","Referer": "https://test-mgt.lanadigital.mx/","Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9","Cookie": "language=zh"}

head_pay={"Host": "test-pay.lanadigital.mx","Connection": "keep-alive","Content-Length": "55",
"sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',"Accept": "application/json, text/plain, */*","sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
"Content-Type": "application/json;charset=UTF-8","Origin": "https://test-pay.lanadigital.mx","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty","Referer": "https://test-pay.lanadigital.mx/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-CN,zh;q=0.9","Cookie": "language=zh"}
CONFIGS = {
    'mex_credit': {'host':'192.168.0.60','port':3306, 'user': 'cs_liull','password': 'cs_liull!qw####','database': 'mex_credit'}
}
host_api=host_api
host_action=host_action
host_mgt=host_mgt
host_pay=host_pay
head_api=head_api
head_mgt=head_mgt
head_pay=head_pay
CONFIGS=CONFIGS
which_db=which_db