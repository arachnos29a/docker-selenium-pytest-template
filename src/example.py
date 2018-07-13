from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSomething():
    def test_title(self):
        browser = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        browser.get('https://google.com')
        assert 'google' in browser.title

