from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOpitons
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import datetime

FF_SEND_URL = 'https://send.firefox.com/'
FILE_BROWSE_BTN_ID = 'file-upload'
UPLOAD_BTN_ID = 'upload-btn'
DOWNLOAD_URL_TXT_ID = 'share-url'

class FireFoxSend:
    def upload(self, file_to_upload, wait_in_secs = 1200):
        if not os.path.exists(file_to_upload):
            raise FileNotFoundError()

        start_time = datetime.datetime.now()
        try:
            options = FFOpitons()
            #options.add_argument("--headless")

            print('Initializing FF')
            driver = webdriver.Firefox(executable_path='C:\\geckodriver-v0.22.0-win64\\geckodriver.exe',
                                       firefox_options=options)
            print(f'Loading {FF_SEND_URL}')
            driver.get(FF_SEND_URL)

            # Wait for file browser  button to be located
            print('Waiting for file browser button..')
            WebDriverWait(driver, wait_in_secs).until(EC.presence_of_element_located((By.ID, FILE_BROWSE_BTN_ID)))

            file_upload_btn = driver.find_element_by_id(FILE_BROWSE_BTN_ID)
            file_upload_btn.send_keys(file_to_upload)

            # Wait for upload button to be located
            print(f'Uploading the file {file_to_upload}')
            WebDriverWait(driver, wait_in_secs).until(EC.presence_of_element_located((By.ID, UPLOAD_BTN_ID)))
            upload_btn = driver.find_element_by_id(UPLOAD_BTN_ID)
            upload_btn.click()

            # Wait for download link url to be located
            print('Waiting for download link to appear..')
            WebDriverWait(driver, wait_in_secs).until(EC.presence_of_element_located((By.ID, DOWNLOAD_URL_TXT_ID)))
            share_url_input = driver.find_element_by_id(DOWNLOAD_URL_TXT_ID)
            download_link = share_url_input.get_property('value')
        finally:
            driver.quit()

        print(f'Time taken to upload the file: {(datetime.datetime.now() - start_time).total_seconds()} seconds.')

        return download_link
