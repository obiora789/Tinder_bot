import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import dotenv
import os
import time
import random

new_file = dotenv.find_dotenv()
dotenv.load_dotenv(new_file)

MY_NAME = os.environ.get("NAME")
TINDER_URL = "https://tinder.com/"
CHROME_DRIVER = os.environ.get("CHROME_PATH")
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.getenv("PASSWORD")
MOBILE_NUMBER = os.environ.get("MOBILE")
SERVICE = Service(executable_path=CHROME_DRIVER)
LONG = 2
SHORT = 3
DELAY = 5
END = 9
max_distance = 50
number_of_swipes = 100
capabilities = DesiredCapabilities().CHROME


def email_address():
    """Inputs the email and clicks 'Next'"""
    time.sleep(DELAY*2 - generate_random_time(LONG))
    email_add = driver.find_element(By.NAME, 'identifier')
    email_add.click()   # Clicks the email field
    time.sleep(DELAY - generate_random_time(LONG))
    email_add.clear()    # Clears the email field
    email_add.send_keys(EMAIL)    # Types in email
    time.sleep(DELAY - generate_random_time(LONG))
    next_ = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
    actions = ActionChains(driver)
    actions.move_to_element(next_).perform()
    time.sleep(DELAY - generate_random_time(LONG))
    actions.click(on_element=next_).perform()
    # next_.click()
    # driver.execute_script("arguments[0].click();", next_)


def generate_random_time(number_of_secs):
    """Generates a random time between 1 and 5 seconds once it receives the number of seconds"""
    return round(random.randint(DELAY, END) / 10, 1) * number_of_secs


def login_button(word: str):
    """Clicks the login button"""
    log_in = driver.find_element(By.LINK_TEXT, word)
    driver.execute_script("arguments[0].click();", log_in)
    time.sleep(DELAY - generate_random_time(LONG))


def get_distance(indexes):
    """Gets the distance between you and the current lady."""
    time.sleep(generate_random_time(LONG))
    dist_from_me = driver.find_elements(By.CLASS_NAME, "Row")   # gets the pictures that contain distance information
    distances = []
    for dist in dist_from_me:
        if "kilometres away" in dist.text and indexes <= 2:
            distances.append(dist)
            print(f"Dist from me: {dist.text}")
    try:
        distance_from_me = distances[-1].text       # gets the particular distance between you and the current lady
    except IndexError:
        distance_from_me = None  # distance_from_me = f"{max_distance * 2} kilometres away"
    return distance_from_me


options = uc.ChromeOptions()
prefs = {
    "profile.default_content_setting_values":
        {
            "geolocation": 1,       # enables location settings
            'notifications': 1,     # enables notifications
        },
    'profile.managed_default_content_settings':
        {
            'geolocation': 1        # sets your current location
        }
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-popup-blocking")    # allows pop-ups to input your gmail login details
capabilities.update(options.to_capabilities())
with uc.Chrome(service=SERVICE, options=options, use_subprocess=True) as driver:
    driver.get(url=TINDER_URL)
    time.sleep(DELAY)
    try:
        div = driver.find_element(By.CSS_SELECTOR, "body div")      # Accept
        div_id = div.get_attribute("id")
        accept_cookies = driver.find_element(       # gets the "Accept Cookies button"
            By.XPATH, f'//*[@id="{div_id}"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
        driver.execute_script("arguments[0].click();", accept_cookies)   # Clicks Accept cookies
    except NoSuchElementException:
        pass
    time.sleep(DELAY - generate_random_time(SHORT))
    login_button("Log in")  # clicks the login button at the top right of Tinder webpage
    time.sleep(DELAY+2 - generate_random_time(LONG))
    # The "Continue with Google" button is in an iframe, so you need to switch to that iframe
    WebDriverWait(driver, DELAY * 3).until(ec.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))
    google_log_in = WebDriverWait(driver, DELAY*SHORT).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/span[1]')))
    driver.execute_script("arguments[0].click();", google_log_in)   # Clicks the "Continue with Google" button
    # driver.switch_to.default_content()
    time.sleep(DELAY - generate_random_time(LONG))
    driver.switch_to.window(driver.window_handles[1])   # Switches to the new window to input Google login details
    email_address()    # inputs the email and clicks next
    password = WebDriverWait(driver, DELAY * 3).until(ec.presence_of_element_located((By.NAME, "Passwd")))
    # try:
    #     password = WebDriverWait(driver, DELAY*3).until(ec.presence_of_element_located((By.NAME, "Passwd")))
    # except TimeoutException:
    #     try_again = driver.find_element(By.CLASS_NAME, "VfPpkd-mRLv6")
    #     driver.execute_script("arguments[0].click();", try_again)
    #     email_address()
    #     password = WebDriverWait(driver, DELAY * 3).until(ec.presence_of_element_located((By.NAME, "Passwd")))
    driver.execute_script("arguments[0].click();", password)   # Clicks the password field
    time.sleep(DELAY - generate_random_time(LONG))   # delay
    password.clear()  # Clears the password field
    password.send_keys(PASSWORD)   # Types the password
    time.sleep(DELAY - generate_random_time(LONG))
    password.send_keys(Keys.ENTER)    # presses the "Enter" key
    time.sleep(DELAY * 2 - generate_random_time(LONG))  # waits for Google authentication
    driver.switch_to.window(driver.window_handles[0])    # returns to the main window

    time.sleep(DELAY * 2 - generate_random_time(LONG))
    div_two = driver.find_element(By.XPATH, '/html/body/div[2]')
    div_two_id = div_two.get_attribute("id")  # gets the div id (This changes)
    try:
        allow_location = driver.find_element(By.XPATH,  # locates the "Allow location" button if displayed
                                             f'//*[@id="{div_two_id}"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
        print(allow_location.text)    # prints the "Allow location" button if displayed
        time.sleep(DELAY - generate_random_time(LONG))
        WebDriverWait(driver, DELAY * DELAY).until(ec.element_to_be_clickable(allow_location))  # Wait until clickable
        driver.execute_script("arguments[0].click();", allow_location)    # then click it
        time.sleep(DELAY - generate_random_time(LONG))
    except NoSuchElementException:
        pass
    count = 0
    driver.implicitly_wait(DELAY * (LONG + DELAY))
    mouse_pointer = ActionChains(driver)     # activates the mouse pointer
    for index in range(1, number_of_swipes):
        matched = None
        count += 1
        driver.implicitly_wait(DELAY * 2)
        WebDriverWait(driver, DELAY ** SHORT).until(ec.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR,
                                                                                                   ".Bd button path")))
        slide_container = driver.find_elements(By.CSS_SELECTOR, ".recsCardboard__cards .StretchedBox")
        for slide in slide_container:   # looping through the slide container
            display_slide = slide.get_attribute("aria-hidden")   # this gets the current slide
            if display_slide == "false":   # This indicates the slide/lady currently being displayed
                next_previous = slide.find_elements(By.CSS_SELECTOR, ".tappable-view svg")  # next and previous buttons
                print(f"Previous or Next: {next_previous}", len(next_previous))
                pics = slide.find_elements(By.CLASS_NAME, "keen-slider__slide")   # locating the pictures of each lady
                print(f"Number of pics: {len(pics)}")
                number_of_pics = len(pics)
                name = slide.find_element(By.CSS_SELECTOR, ".Ell span")    # gets the lady's name
                print(name.text)
                break
        print(f"Slide Container: {len(slide_container)}")
        proximity_from_me = None     # variable to store distance value
        if number_of_pics > 1:    # Determines if lady has more than one picture so that it can scroll through them.
            for ind in range(1, number_of_pics):  # Scrolls through the lady's pictures and gets her proximity from you.
                print(f"Initial distance: {get_distance(ind)}")
                if ind < 2 and proximity_from_me is None:
                    try:
                        proximity_from_me = int(get_distance(ind).split(" ")[0])  # actual distance value
                        print(f"Proximity is: {proximity_from_me}")
                    except ValueError:
                        pass
                elif ind == 2 and proximity_from_me is None:
                    try:
                        proximity_from_me = int(get_distance(ind).split(" ")[0])    # actual distance value
                        print(f"Proximity is: {proximity_from_me}")
                    except ValueError:
                        proximity_from_me = max_distance * 2  # arbitrary value set when no distance value was retrieved
                elif proximity_from_me is None:
                    proximity_from_me = max_distance * 2   # arbitrary value set when no distance value was retrieved
                mouse_pointer.move_to_element(next_previous[-1]).click().perform()
                time.sleep(generate_random_time(LONG))
        elif number_of_pics == 1:
            proximity_from_me = max_distance * 2    # arbitrary value set when no distance value was retrieved
        buttons = driver.find_elements(By.CSS_SELECTOR, ".Bd button path")
        print(f"Total Buttons: {len(buttons)}")
        print(f"Distance from me: {proximity_from_me}", f"Max distance: {max_distance}")
        if proximity_from_me < max_distance and number_of_pics >= SHORT:   # this determines which button is clicked
            mouse_pointer.move_to_element(buttons[3]).click().perform()    # Click Like button
        else:
            mouse_pointer.move_to_element(buttons[1]).click().perform()  # Click Dislike button
        try:
            new_buttons = driver.find_elements(By.CSS_SELECTOR, ".c1p6lbu0 .w1u9t036 .l17p5q9z")
            # for button in new_buttons:
            #     if button.text == "Not interested":
            #         print(button.text)
            #         mouse_pointer.move_to_element(button).click().perform()
            not_interested = [mouse_pointer.move_to_element(button).click().perform()
                              for button in new_buttons if button.text == "Not interested"]
        except NoSuchElementException:
            pass
        # try:
        #     matched = driver.find_element(By.CLASS_NAME, "StretchedBox")
        #     print(matched)
        #     driver.implicitly_wait(DELAY*2)
        # except NoSuchElementException:
        #     pass
        # else:
        #     if matched:
        #         print(f"Her name is: {name.text}")
        #         chat_with_her = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[3]/div[3]/form/textarea')
        #         driver.execute_script("arguments[0].click();", chat_with_her)
        #         chat_with_her.send_keys(f"Hi {name.text}, I'm {MY_NAME}.")
        #         chat_with_her.send_keys(Keys.RETURN)
        #         time.sleep(DELAY - generate_random_time(LONG))
        #         chat_with_her.send_keys(f"{name.text} with the beautiful smile.")
        #         chat_with_her.send_keys(Keys.ENTER)
        #         time.sleep(DELAY*2 - generate_random_time(SHORT))
        #         try:
        #             do_not_subscribe = driver.find_element(By.CLASS_NAME, "close")
        #             driver.execute_script("arguments[0].click();", do_not_subscribe)
        #         except NoSuchElementException:
        #             pass





















# options.add_argument("window-size=1200x600")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument = {"args": ['--disable-web-security', '--user-data-dir', '--allow-running-insecure-content']}
# options.add_experimental_option("debuggerAddress", "localhost: 8797")
# options.headless = True
# options.add_argument("--profile-directory=Default")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("--incognito")
# options.add_argument("user_agent=DN")
