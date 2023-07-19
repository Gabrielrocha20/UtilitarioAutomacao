from collections.abc import Callable, Iterable, Mapping
from subprocess import CREATE_NO_WINDOW
from threading import Thread
from time import sleep
from typing import Any

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PegarLiberacao:
    def __init__(self):
        pass
    def liberar(self, cnpj):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        chrome_service = ChromeService("./chromedriver.exe")
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(service=chrome_service,options=options)
        driver.get("https://www.datahex.com.br/liberacao/#/")
        
        elem = driver.find_element(By.ID, "input_0")
        elem.clear()
        elem.send_keys(cnpj)
        try:
            send = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[2]/button[2]')
        except:
            send = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[3]/button[2]')
        send.click()

        sleep(2)

        try:
            divArara1 = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[2]/md-content/md-card[1]/md-card-content/p[1]').text
            divArara2 = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[2]/md-content/md-card[1]/md-card-content/p[2]').text

            divPdv1 = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[2]/md-content/md-card[2]/md-card-content/p[1]').text
            divPdv2 = driver.find_element(By.XPATH, '/html/body/div/div/md-content/form/div[2]/md-content/md-card[2]/md-card-content/p[2]').text
        except:
            divArara1 = "Vazio"
            divArara2 = "Vazio"
            divPdv1 = "Vazio"
            divPdv2 = "Vazio"

        driver.close()
        driver.quit()
        liberacao = f"""
            Arara
        {divArara1}

        {divArara2}
        //
            PDV
        {divPdv1}

        {divPdv2}
        """
        return liberacao
