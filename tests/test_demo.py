from selenium import webdriver
import pytest
from time import sleep


class TestBlog:

    driver = webdriver.Chrome(executable_path='C://Users//Yago//Desktop//chromedriver.exe')
    driver.get('http://localhost:5000')

    mainTitle = driver.find_element_by_tag_name('h3').text

    assert 'Welcome to my final project at college' in mainTitle
    print(mainTitle)

    driver.find_element_by_link_text('Read More →').click()

    successTitle = driver.find_element_by_tag_name('h1').text

    assert 'ooooooooba' in successTitle
    print(successTitle)

    driver.find_element_by_name('name').send_keys('Yago')
    driver.find_element_by_name('email').send_keys("test@selenium.com")
    driver.find_element_by_name('body').send_keys('Testanto selenium')
    driver.find_element_by_name('submitComment').click()

    successComment = driver.find_element_by_class_name('alert').text

    assert 'Your comment is awaiting moderation' in successComment
    print(successComment)

    driver.find_element_by_name('Title').click()

    driver.find_element_by_link_text('About').click()

    aboutTitle = driver.find_element_by_tag_name('h1').text

    assert 'Sobre nós' in aboutTitle
    print(aboutTitle)

    driver.find_element_by_name('Title').click()

    driver.find_element_by_link_text('Contact').click()

    driver.find_element_by_name('contact_name').send_keys('Yago')

    driver.find_element_by_name('email_contact').send_keys('test@selenium.com')

    driver.find_element_by_name('content').send_keys('testando selenium')

    driver.find_element_by_name('sendContact').click()

    submitContact = driver.find_element_by_class_name('alert').text

    assert 'E-mail sent with success' in submitContact
    print(submitContact)

    driver.find_element_by_name('Title').click()

    driver.find_element_by_link_text('Login').click()

    driver.find_element_by_name('username').send_keys('admin')

    driver.find_element_by_name('password').send_keys('admin')

    driver.find_element_by_name('LoginButton').click()

    loged = driver.find_element_by_name('loged').text

    assert 'Hello, admin!' in loged
    print(loged)

    if 'Hello, admin' in loged:
        driver.find_element_by_link_text('Logout').click()

    nonLoged = driver.find_element_by_name('nonLoged').text

    assert 'Hello' in nonLoged
    print(nonLoged)

    driver.find_element_by_link_text('Login').click()

    driver.find_element_by_link_text('Are you new? Register here').click()

    driver.find_element_by_id('id_username').send_keys('Yago')

    driver.find_element_by_id('id_email').send_keys('selenium@test.com')

    password1 = driver.find_element_by_id('id_password1').send_keys('admin123456@')

    password2 = driver.find_element_by_id('id_password2').send_keys('admin123456@')

    driver.find_element_by_name('submitPassword').click()

    