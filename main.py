import time

import pandas as pd

from src.defines import *
from src.driver import quit_driver, setup_driver
from src.log_config import logger
from src.login import login


def main():
    df = pd.read_excel(INPUT_FILE, dtype={'NIF': str, 'PASSWORD': str})
    driver = setup_driver()
    i = 0
    df['STATUS'] = ''

    for index, row in df.iterrows():

        nif = row['NIF']
        password = row['PASSWORD']

        logger.info(f'Trying loggin {nif} | {i}')
        driver.delete_all_cookies()
        status = login(driver, nif, password)
        df.at[index, 'STATUS'] = status
        logger.info(f'{nif} | {status}')
        i += 1
        if i % 10 == 0:
            df.to_excel(OUTPUT_FILE, index=False)
        time.sleep(2)
        if i % 50 == 0:
            quit_driver(driver)
            driver = setup_driver()

    df.to_excel(OUTPUT_FILE, index=False)
    logger.info('PROCESS FINISHED. CHECK OUTPUT FILE')
    quit_driver(driver)


if __name__ == '__main__':
    main()
