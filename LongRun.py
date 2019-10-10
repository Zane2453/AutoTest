from selenium import webdriver
# from pyvirtualdisplay import Display
import time, random

'''display = Display(visible=0, size=(800, 600))
display.start()'''
driver = webdriver.Chrome()

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

if __name__ == "__main__":
    count = 1
    driver.maximize_window()
    driver.get("https://aipoll.nctu.me/pollstart/2")
    driver.get("https://aipoll.nctu.me/vote/4")
    main_window = driver.current_window_handle
    time.sleep(2)

    driver.execute_script('''window.open("https://aipoll.nctu.me/pollstart/4","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

    driver.switch_to.window(main_window)
    time.sleep(3)
    driver.find_element_by_css_selector('#startBtn').click()
    print(count)

    while True:
        while driver.find_element_by_css_selector('#end').value_of_css_property('visibility') != 'visible':
            time.sleep(3)
            voteAns()
            time.sleep(3)

            driver.switch_to.window(driver.window_handles[1])
            driver.get("https://aipoll.nctu.me/pollnext")
            driver.switch_to.window(main_window)
            count = count + 1
            print(count)
        time.sleep(3)
        count = 1
        driver.delete_all_cookies()
        driver.get("https://aipoll.nctu.me/pollstart/2")
        driver.get("https://aipoll.nctu.me/vote/4")
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://aipoll.nctu.me/pollstart/4")

        driver.switch_to.window(main_window)
        time.sleep(3)
        driver.find_element_by_css_selector('#startBtn').click()
        print(count)

    time.sleep(5)
    driver.quit()