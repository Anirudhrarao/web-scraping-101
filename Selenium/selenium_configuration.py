from selenium import webdriver



def initialize_webdriver() -> None:
    """
    Basic setup to initialize webdriver for chrome
    Args:
        None
    Returns:
        None
    """
    driver_path: str = './chromedriver'

    driver = webdriver.Chrome() # Setup for web driver 

    driver.get("https://www.amazon.com/") # Will open specified url

    print(driver.title) # Print title of web

    driver.quit() # Quit the driver to close the browser

# initialize_webdriver()


def headless_mode() -> None:
    """
    Headless  driver setup for chrome
    Desc:
        Headless mode refers to running a web browser without its graphical user interface (GUI)
    Args:
        None
    Returns:
        None
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.amazon.com/")
    print(driver.title)
    
    driver.quit()

# headless_mode()


