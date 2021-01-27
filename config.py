from selenium import webdriver
import time

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
start = time.time()
url = 'https://www.chegg.com/homework-help/A-Laboratory-Guide-to-Human-Physiology-14th-edition-chapter-C5-problem-5C4-solution-9780077296179'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH
browser = webdriver.Chrome('chromedriver', options=chrome_options) #seleniumwire_options=options)
time.sleep(10)
browser.get(url)
time.sleep(3)
S = lambda X: browser.execute_script('return document.body.parentNode.scroll'+X)
browser.set_window_size(S('Width'),S('Height')) # May need manual adjustment
browser.find_element_by_tag_name('body').screenshot('web_screenshot.png')
end = time.time()
tot_time = (end - start)
print(tot_time)

#wew
