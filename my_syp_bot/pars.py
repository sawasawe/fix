from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://agroserver.ru/apelsiny/'

# Инициализация веб-драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен и указан путь к драйверу Chrome

# Открываем страницу
driver.get(url)

# Ищем элементы с ценами
price_elements = driver.find_elements(By.price, 'your-class-for-prices')

# Выводим цены
for price_element in price_elements:
    price = price_element.text.strip()
    print(f"Цена на апельсины: {price}")

# Закрываем веб-драйвер
driver.quit()