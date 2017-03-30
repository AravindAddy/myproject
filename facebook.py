from selenium import webdriver
from selenium.webdriver.common.by import By #1
from selenium.webdriver.support.ui import WebDriverWait #2
from selenium.webdriver.support import expected_conditions as EC #3

from lxml import html

def get_driver():
    '''
        We need to create driver like this.
        Driver is kind of browser, using this
        driver we will open all the urls
    '''

    driver = webdriver.PhantomJS("/home/niranjan/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
    return driver

def open_home_page(driver):
    # Opening urls in selenium
    driver.get("https://www.facebook.com/careers/locations/")

    # As selenium stimulates browser. we need to take few things
    # into considerations. And we need to write program with
    # context of browser.
    # Whenever we open url or click or submit form via selenium,
    # We need to give some "Wait"
    # More information here
    # http://selenium-python.readthedocs.io/waits.html

    # One way of applying wait
    element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="fb_content clearfix "]'))
                ) # This needs import stmt no.1, 2, 3

    #Another way of applying waits, ( First one is preferrable )
    driver.implicitly_wait(10)

    #Creating doc
    hdoc = driver.page_source.encode("utf-8")
    hdoc = html.fromstring(hdoc)

    list_of_locations = hdoc.xpath('//table[@class="uiGrid _51mz _3e0p _5f0n"]//tr/td')
    for loc in list_of_locations:
        link = "".join(loc.xpath('.//a[contains(@href, "careers")]/@href'))
        if link:
            link = "https://www.facebook.com%s" %link 

def main():

    driver = get_driver()
    open_home_page(driver)


if __name__ == "__main__":
    main()
