from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

Email_ID = "ap_email"
Pass_ID = "ap_password"
Continue_ID = "continue"
sign_ID = "signInSubmit"
Search_ID = "twotabsearchtextbox"
Search_Button = "nav-search-submit-button"

############################################
user = "username"         ##################
password = "password"     ##################
############################################


driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

driver.find_element(By.ID,Email_ID).send_keys(user)

driver.find_element(By.ID,Continue_ID).click()

driver.find_element(By.ID,Pass_ID).send_keys(password)

driver.find_element(By.ID,sign_ID).click()

driver.find_element(By.ID,Search_ID).send_keys("redmi note 10")

driver.find_element(By.ID,Search_Button).click()

driver.close()





