from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import socket, threading, random

driver = webdriver.Chrome()
count = 1
connection = None

def Start():
    msg = "s"
    connection.send(msg.encode('utf-8'))

def voteAns():
    global driver
    num = random.randint(1,101)

    if num%4 == 0:
        driver.find_element_by_css_selector('#options>button:first-child').click()
    elif num%4 == 1:
        driver.find_element_by_css_selector('#options>button:nth-child(2)').click()
    elif num%4 == 2:
        driver.find_element_by_css_selector('#options>button:nth-child(3)').click()
    else:
        driver.find_element_by_css_selector('#options>button:nth-child(4)').click()

def toProcessing():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost', 8888))
    server.listen(1)

    global count
    global driver
    global connection

    while True:
        print('Waiting for Client (Processing)')
        (connection, client_address) = server.accept()
        print('Connection successed! Client (Processing) info: ', connection, client_address)
        msg = "s"
        connection.send(msg.encode('utf-8'))

        while True:
            try:
                raw_data = connection.recv(1024)
                buf = raw_data.decode('utf-8')
                if buf == 's':
                    time.sleep(3)
                    driver.find_element_by_css_selector('#startBtn').click()
                    time.sleep(3)
                    print(count)
                    voteAns()
                    count = count + 1
                    msg = 'v'
                    connection.send(msg.encode('utf-8'))
                    time.sleep(3)
                    msg = 'n'
                    connection.send(msg.encode('utf-8'))
                elif buf == 'n' and driver.find_element_by_css_selector('#end').value_of_css_property('visibility') != 'visible':
                    time.sleep(3)
                    print(count)
                    voteAns()
                    count = count + 1
                    msg = 'v'
                    connection.send(msg.encode('utf-8'))
                    time.sleep(3)
                    msg = 'n'
                    connection.send(msg.encode('utf-8'))
            except ConnectionResetError as e:
                print("Break")
                break

        connection.close()
        print('Client (Processing) disconnection')

if __name__ == "__main__":
    driver.maximize_window()
    driver.get("https://aipoll.nctu.me/pollstart/2")
    driver.get("https://aipoll.nctu.me/vote/4")
    main_window = driver.current_window_handle

    t = threading.Thread(target=toProcessing, daemon=True)
    t.start()

    while True:
        if driver.find_element_by_css_selector('#end').value_of_css_property('visibility') == 'visible':
            time.sleep(5)
            count = 1
            driver.delete_all_cookies()
            driver.get("https://aipoll.nctu.me/pollstart/2")
            driver.get("https://aipoll.nctu.me/vote/4")
            time.sleep(3)
            Start()

    # website reloading
    #driver.refresh()

    time.sleep(5)
    driver.quit()