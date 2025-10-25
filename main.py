import subprocess
import requests
import os













with open("a.txt", "w", encoding='utf-8') as file:
    pass
UA = os.environ.get('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36')
BOTTOKEN = os.environ.get('BOTTOKEN')
USERID = os.environ.get('USERID')
SOUTHPLUS = os.environ.get('eb9e6_ck_info=%2F%09; eb9e6_cknum=BlYHXwJQAgZTVDk8XQVQBldRBQcDU1EGAlFSUlUGCwNWUlxRDwVUBA1bAQ4%3D; eb9e6_winduser=BVUHVQdaAj5TWgEMCFFcBgZUAllUA1AEAFRcVAcNXw9WA1QAUwNRUzw%3D; eb9e6_threadlog=%2C219%2C208%2C5%2C128%2C73%2C223%2C224%2C13%2C221%2C14%2C; peacemaker=1; eb9e6_ol_offset=291582; cf_clearance=T1fGKcrk0E7QG2rTvSOQY_K1j9KZGu2kMEyytWJ9CTQ-1761392745-1.2.1.1-OkvZ6i_XC5uoQ9gsiTQK2xJmeFehcDswly5.30W3dxCzTGgqEXRxVDWEIip5SJtiHsigPatw1UqCrlT5JiycLtZWamNpFpEWdCDDkLtKrocPyeeno1t7yXartVdKE9EWdeT6qOAObOOwcl6vEjtghMatV2qyEvP8Dzuq5lqS27C_FF55gNDvrOnJLBj2dcZU2BWJ5I7CYxO9hcxz3qV5TamTgYh6gFveXlDeycZv6no; eb9e6_readlog=%2C2116867%2C2685544%2C2691040%2C2688782%2C2673409%2C1711478%2C2674974%2C2642181%2C; eb9e6_lastpos=other; eb9e6_lastvisit=91%091761392835%09%2Fplugin.php%3FH_name-tasks.html.html')
ACGFUN = os.environ.get('ctL4_2132_saltkey=p034T60e; ctL4_2132_lastvisit=1761390008; ctL4_2132_mobile=no; ctL4_2132_sendmail=1; ftacgfunpro=1; ctL4_2132_seccodecS=1315293.c6eb46a145066fa549; ctL4_2132_ulastactivity=1761393738%7C0; ctL4_2132_auth=f50fgp4Y08eLjRZL%2BTiYUEYfyqFvTBzeC2UBryV501cEpJE36I%2FFk%2BTv2kVWNO8Kf68VRixL85xkAWhcjbgH8Qn7hck; ctL4_2132_sid=0; ctL4_2132_nofavfid=1; ctL4_2132_checkpm=1; ctL4_2132_noticeTitle=1; ctL4_2132_lastact=1761393762%09plugin.php%09; ctL4_2132_creditnotice=0D0D2D0D0D0D0D0D0D408116; ctL4_2132_creditbase=0D5D0D0D0D0D0D0D0; ctL4_2132_misigntime=1761393762')
VIKACG = os.environ['VIKACG']

# 检查 UA 是否存在，并打印
if UA:

    if SOUTHPLUS:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nSouthplus签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            result = subprocess.run(['python', 'SouthPlus.py'], check=True, capture_output=True, text=True)
            print(result.stdout)  # 如果成功，打印标准输出
        except Exception as e:
            print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅SouthPlus签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行Southplus签到")




    if ACGFUN:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nAcgFun签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            result = subprocess.run(['python', 'AcgFun.py'], check=True, capture_output=False, text=True)
            print(result.stdout)  # 如果成功，打印标准输出
        except Exception as e:
            print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅AcgFun签到出错：\n{str(e)}")

    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行AcgFun签到")



    if VIKACG:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\nVikACG签到结果：")
        try:
            # 运行 SouthPlus.py 脚本
            result = subprocess.run(['python', 'VikACG.py'], check=True, capture_output=True, text=True)
            print(result.stdout)  # 如果成功，打印标准输出
        except Exception as e:
            print(e)
            with open("a.txt", "a", encoding='utf-8') as file:
                file.write(f"\n  😅VikACG签到出错：\n{str(e)}")
    else:
        with open("a.txt", "a", encoding='utf-8') as file:
            file.write("\n  😢不进行VikACG签到")























else:
    with open("a.txt", "a", encoding='utf-8') as file:
        file.write("❗未设置UA，脚本拒绝执行")








if USERID:
    with open('a.txt', 'r', encoding='utf-8') as file:
        content = file.read()  # 读取文件内容

    # 发送消息到 Telegram
    url = f'https://api.telegram.org/bot{BOTTOKEN}/sendMessage'
    payload = {
        'chat_id': USERID,
        'text': content,
    }

    response = requests.post(url, data=payload)

else:
    exit(0)
