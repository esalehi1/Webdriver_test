# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:14:51 2024

@author: Erfan
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# راه‌اندازی مرورگر کروم با WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# باز کردن صفحه گوگل
driver.get("https://www.google.com")

# بستن مرورگر
driver.quit()
