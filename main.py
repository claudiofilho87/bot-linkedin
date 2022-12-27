# import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# ======================================================================================================================
# # First way with google login
# ======================================================================================================================

# driver = uc.Chrome(use_subprocess=True)
# driver.get(URL)
#
# main_page = driver.current_window_handle
#
# sleep(2)
# button_login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
# button_login.click()
# sleep(2)
# google_login = driver.find_element(By.XPATH, "//*[@id='sign-in-with-google-button']")
# google_login.click()
# sleep(2)
# driver.switch_to.window(driver.window_handles[-1])
# email_login = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
# email_login.send_keys("claudiofilho1525@gmail.com")
# button_next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
# button_next.click()
# sleep(2)
# password_login = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
# password_login.send_keys("C2468101214c")
# sleep(2)
# button_finish = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
# button_finish.click()
# sleep(100)
# ======================================================================================================================


# ======================================================================================================================
# # Second way with directly login
# ======================================================================================================================

chrome_driver_path = "C:\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

sleep(2)
button_login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
button_login.click()
sleep(1)
email_login = driver.find_element(By.XPATH, '//*[@id="username"]')
email_login.send_keys("claudiofilho1525@gmail.com")
sleep(1)
password_login = driver.find_element(By.XPATH, '//*[@id="password"]')
password_login.send_keys("C2468101214")
button_finish = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
button_finish.click()
# sleep(15)
find_jobs = True
max_number_id = 1000
number_id = 50
jobs = 0
while find_jobs:
    try:
        box_job = driver.find_element(By.CSS_SELECTOR, f'#ember{number_id} .job-card-list__title')
        box_job.click()
        sleep(2)
        driver.execute_script("arguments[0].scrollIntoView(true);", box_job)
        sleep(2)
        text_candidates = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/ul/li[3]/span')
        number_candidates = int(text_candidates.text.split()[6])
        if number_candidates <= 100:
            save_button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
            save_button.click()
            sleep(2)
            jobs += 1
            print(jobs)
            if jobs == 15:
                find_jobs = False
        number_id += 12
    except:
        pass
        number_id += 1
    if number_id >= max_number_id:
        max_number_id += 1000
        bar_search = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list__pagination')
        buttons = bar_search.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            # print(button.get_attribute("outerHTML"))
            if int(button.text) == int(max_number_id / 1000):
                button.click()
                sleep(1)
                number_id = 0
                break

sleep(1000)