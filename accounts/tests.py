from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
import chromedriver_binary

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='/usr/local/bin/chromedriver')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://localhost:8000'+ str(reverse_lazy('account_login')))

        username_input = self.selenium.find_element_by_name('login')
        username_input.send_keys('take')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('Take3434')
        self.selenium.find_element_by_class_name('btn').click()

        self.assertEqual('日記一覧 | My Diary',self.selenium.title)