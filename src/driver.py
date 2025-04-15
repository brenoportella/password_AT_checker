import os

from selenium import webdriver

download_dir = os.path.dirname(os.path.abspath(__file__))


def setup_driver():
    """
    Sets up and returns a configured Edge WebDriver instance.

    This function configures the Edge WebDriver with specific preferences and options,
    such as the default download directory and disabling popup blocking and safe browsing
    features. It also runs the browser in headless mode.

    Returns:
        webdriver.Edge: A configured Edge WebDriver instance.
    """
    edge_prefs = {
        'download.neverAsk.saveToDisk': 'application/xml, text/anytext, text/plaintext',
        'download.default_directory': str(download_dir),
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'disable-popup-blocking': True,
        'safebrowsing.enabled': False,
        'download_restrictions': 0,
    }

    options = webdriver.EdgeOptions()
    options.add_argument('--safebrowsing-disable-download-protection')
    options.add_argument('--headless')
    options.add_experimental_option('prefs', edge_prefs)

    driver = webdriver.Edge(options=options)
    return driver


def quit_driver(driver):
    """
    Quits the given WebDriver instance.

    This function properly closes the WebDriver instance, shutting down the browser
    and releasing any associated resources.

    Args:
        driver (webdriver.Edge): The WebDriver instance to quit.

    Returns:
        None
    """
    driver.quit()
