from selenium import webdriver
import pytest
from time import sleep

@pytest.mark.usefixtures('setupBrowser')
class Test_Blog:

    
    def test_demo(self):

        mainTitle = self.driver.find_element_by_tag_name('h3').text

        assert 'Welcome to my final project at college' in mainTitle
        print(mainTitle)

        self.driver.find_element_by_link_text('Read More →').click()

        successTitle = self.driver.find_element_by_tag_name('h1').text

        assert 'ooooooooba' in successTitle
        print(successTitle)

        self.driver.find_element_by_name('name').send_keys('Gomes')
        self.driver.find_element_by_name('email').send_keys("test@selenium.com")
        self.driver.find_element_by_name('body').send_keys('Testanto selenium')
        self.driver.find_element_by_name('submitComment').click()

        successComment = self.driver.find_element_by_class_name('alert').text

        assert 'Your comment is awaiting moderation' in successComment
        print(successComment)

        self.driver.find_element_by_name('Title').click()

        self.driver.find_element_by_link_text('About').click()

        aboutTitle = self.driver.find_element_by_tag_name('h1').text

        assert 'Sobre nós' in aboutTitle
        print(aboutTitle)

        self.driver.find_element_by_name('Title').click()

        self.driver.find_element_by_link_text('Contact').click()

        self.driver.find_element_by_name('contact_name').send_keys('Yago')

        self.driver.find_element_by_name('email_contact').send_keys('test@selenium.com')

        self.driver.find_element_by_name('content').send_keys('testando selenium')

        self.driver.find_element_by_name('sendContact').click()

        submitContact = self.driver.find_element_by_class_name('alert').text

        assert 'E-mail sent with success' in submitContact
        print(submitContact)

        self.driver.find_element_by_name('Title').click()

        self.driver.find_element_by_link_text('Login').click()

        self.driver.find_element_by_name('username').send_keys('admin')

        self.driver.find_element_by_name('password').send_keys('admin')

        self.driver.find_element_by_name('LoginButton').click()

        loged = self.driver.find_element_by_name('loged').text

        assert 'Hello, admin!' in loged
        print(loged)

        if 'Hello, admin' in loged:
            self.driver.find_element_by_link_text('Logout').click()

        nonLoged = self.driver.find_element_by_name('nonLoged').text

        assert 'Hello' in nonLoged
        print(nonLoged)

        self.driver.find_element_by_link_text('Login').click()

        self.driver.find_element_by_link_text('Are you new? Register here').click()

        self.driver.find_element_by_id('id_username').send_keys('Yago')

        self.driver.find_element_by_id('id_email').send_keys('selenium@test.com')

        password1 = self.driver.find_element_by_id('id_password1').send_keys('admin123456@')

        password2 = self.driver.find_element_by_id('id_password2').send_keys('admin123456@')

        self.driver.find_element_by_name('submitPassword').click()

        self.driver.close()

        