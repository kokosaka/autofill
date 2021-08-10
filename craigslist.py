from selenium import webdriver
import data

# tells program were using chrome
web = webdriver.Chrome()
# traverse through initial form
web.get("https://losangeles.craigslist.org/")
web.find_element_by_xpath('//*[@id="post"]').click()
web.find_element_by_xpath(
    '/html/body/article/section/form/ul/li[1]/label/input').click()
web.find_element_by_xpath(
    '/html/body/article/section/form/ul/li[6]/label/span[1]/input').click()
web.find_element_by_xpath(
    '//*[@id="new-edit"]/div/label/label[37]/input').click()

title_element = web.find_element_by_xpath('//*[@id="PostingTitle"]')
title_element.send_keys(data.title)

price_element = web.find_element_by_xpath(
    '//*[@id="new-edit"]/div/div[1]/label[2]/label/input')
price_element.send_keys(data.price)

zip_element = web.find_element_by_xpath('//*[@id="postal_code"]')
zip_element.send_keys(data.zip)

desc_element = web.find_element_by_xpath('//*[@id="PostingBody"]')
desc_element.send_keys(data.desc)

email_element = web.find_element_by_xpath(
    '//*[@id="new-edit"]/div/fieldset[2]/div/div/div[1]/label/label/input')
email_element.send_keys(data.email)

web.find_element_by_xpath('//*[@id="new-edit"]/div/div[3]/div/button').click()
web.find_element_by_xpath('//*[@id="leafletForm"]/button').click()
