from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import keyboard  # To detect key press

# Set up the Chrome driver (ensure you have the correct driver for your browser)
service = Service('C:\\Users\\Max\\Downloads\\chromedriver-win64\\chromedriver.exe')  # Update 'path_to_chromedriver' to the actual path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the YouTube channel
driver.get('https://www.youtube.com/@Gordonua/videos')

# Scroll down multiple times
scroll_pause_time = 1  # Adjust the sleep time as needed
is_scrolling = True  # Flag to control scrolling state

try:
    while True:
        if is_scrolling:
            # Scroll down to the bottom
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            print("Scrolling...")
            time.sleep(scroll_pause_time)
        
        # Check if a specific key (e.g., 'p') is pressed to toggle scrolling/pause
        if keyboard.is_pressed('p'):
            is_scrolling = not is_scrolling
            if is_scrolling:
                print("Resuming scrolling.")
            else:
                print("Pausing scrolling.")
            time.sleep(1)  # Add a short delay to avoid rapid toggling
        
        # Check if we've reached the bottom of the page
        # You can add logic here to break the loop if you have reached the desired video or the bottom of the page
        # if driver.find_element(By.XPATH, "your_xpath_to_specific_video"):
        #     break

finally:
    # Close the driver
    driver.quit()
