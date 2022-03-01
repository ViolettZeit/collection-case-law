import time


def do_collect():
    from bs4 import BeautifulSoup
    from selenium import webdriver

    driverpath = '/Users/dasol/ChromeDriver/chromedriver'  # Local path
    target_uri = 'https://nate.com'

    # set options
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
    #options.add_argument('headless')

    driver = webdriver.Chrome(driverpath, options=options)
    driver.implicitly_wait(3)  # 웹 자원 로드를 위해 3초 인터벌
    driver.get(target_uri)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    for i in soup:
        print(soup.contents)

    time.sleep(10)
    driver.close()  # 현재 탭 닫기
    driver.quit()

    return
