import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера (Chrome)
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# URL сайта
url = "https://piter-online.net"

# 1) Ввод URL https://piter-online.net в Chrome
driver.get(url)

# 2) Найти поле ввода улицы и нажать на него
street_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
)
street_input.click()

# 3) Ввести текст "Тестовая линия" и нажать Enter
street_input.send_keys("Тестовая линия")
street_input.send_keys(Keys.RETURN)

# 4) Найти поле для ввода дома и нажать на него
house_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"))
)
house_input.click()

# 5) Ввести "1" и нажать Enter
house_input.send_keys("1")
house_input.send_keys(Keys.RETURN)

# 6) Нажать на элемент дропдауна
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"))
)
dropdown.click()

# 7) Выбрать элемент из списка
dropdown_item = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]"))
)
dropdown_item.click()

# 8) Нажать кнопку "Показать тарифы"
show_tariffs_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]"))
)
show_tariffs_button.click()

# 9) Закрыть popup
exit_popup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='root']/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]"))
)
exit_popup.click()

# 10) Нажать кнопку "Подключить услугу"

service_button_1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[1]/div[1]/div[2]/div[2]/div[1]/a[1]/span[1]"))
)

service_button_2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[2]/div[2]/div[7]/div[1]/div[1]/div[2]/div[2]"))
)

service_button_3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[3]/div[6]/div[1]/div[1]/div[2]/div[2]/div[1]"))
)

service_button_4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[1]/div[2]/div[4]/div[6]/div[1]/div[1]/div[2]/div[2]"))
)

service_button_5 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[1]/div[2]/div[5]/div[6]/div[1]/div[1]/div[2]/div[2]"))
)

phone_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[2]/input[1]")))
apply_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[contains(text(),'Оставить заявку')]")))
press_exit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//div[4]/div[1]/div[1]/div[1]/div[2]/span[1]")))
buttons_list = [service_button_1, service_button_2, service_button_3, service_button_4, service_button_5]
for service in buttons_list:

        service.click()
        phone_input.click()
        phone_input.send_keys("1111111111")
        apply_button.click()
        press_exit.click()
# Подождать некоторое время, чтобы форма была отправлена (возможно, потребуется настройка времени ожидания)
time.sleep(5)

# 11) Проверка статуса (из Network)
status = None
for entry in driver.get_log('network'):
    if 'POST' in entry['message']:
        request = entry['message']
        if 'status=201' in request:
            status = 201
            break

assert status == 201, "Заявка не отправлена со статусом 201"

driver.quit()
