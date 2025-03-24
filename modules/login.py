from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login(driver, nif, password):
    driver.get(
        'https://www.acesso.gov.pt/v2/loginForm?partID=PFAP&path=/geral/dashboard'
    )
    aut_nif = driver.find_element(
        By.XPATH, '/html/body/div[1]/section/div[1]/div/div/label[2]'
    )
    aut_nif.click()
    field_nif = driver.find_element(By.ID, 'username')
    field_nif.send_keys(nif)
    field_password = driver.find_element(By.NAME, 'password')
    field_password.send_keys(password)
    bt_login = driver.find_element(By.ID, 'sbmtLogin')
    bt_login.click()

    if wrong_password(driver):
        return 'Senha Incorreta'
    elif expired_password(driver):
        return 'Senha Expirada'
    else:
        disconnect(driver)
        return 'Senha OK'


def wrong_password(driver):
    try:
        error_message = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'error-message'))
        )
        return True
    except TimeoutException:
        return False


def expired_password(driver):
    try:
        renew_password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '/html/body/div/main/div/div/div/section/div/form/div[1]',
                )
            )
        )

        return True
    except TimeoutException:
        return False


def disconnect(driver):
    driver.get(
        'https://www.acesso.gov.pt//jsp/logout.jsp?partID=PFAP&path=/geral/atauth/logout'
    )
