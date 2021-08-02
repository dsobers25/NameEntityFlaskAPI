from selenium import webdriver

chromedriver = "C:/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.google.com")