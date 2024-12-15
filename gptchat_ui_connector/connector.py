import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def chat(prompt: str) -> str:
    driver = uc.Chrome(headless=False, use_subprocess=False)

    driver.get("https://chatgpt.com/")
    time.sleep(3)
    input_box = driver.find_element(By.ID, "prompt-textarea")
    input_box.send_keys(prompt)
    time.sleep(2)
    input_box.send_keys(Keys.RETURN)

    time.sleep(20)
    response = driver.find_element(By.XPATH, "//div[@data-message-author-role='assistant']")
    return response.text


if __name__ == "__main__":
    print(chat("Hey, How are you doing?"))
