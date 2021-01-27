from seleniumwire import webdriver
import time

start = time.time()
url = 'https://www.chegg.com/homework-help/A-Laboratory-Guide-to-Human-Physiology-14th-edition-chapter-C5-problem-5C4-solution-9780077296179'
#url = 'https://whatismyipaddress.com/'
"""#options = {
'proxy': {
    'http': 'http://yeqtqqbi-dest:u2facbl1w5zu@45.94.47.108:8152',
    'https': 'http://yeqtqqbi-dest:u2facbl1w5zu@45.94.47.108:8152',
    }
}"""
#options.add_argument('--proxy-server=%s' % PROXY)
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
browser = webdriver.Chrome('chromedriver', options=chrome_options) #seleniumwire_options=options)
time.sleep(10)
browser.get(url)
"""time.sleep(3)
S = lambda X: browser.execute_script('return document.body.parentNode.scroll'+X)
browser.set_window_size(S('Width'),S('Height')) # May need manual adjustment
browser.find_element_by_tag_name('body').screenshot('web_screenshot.png')
end = time.time()
tot_time = (end - start)
print(tot_time)"""