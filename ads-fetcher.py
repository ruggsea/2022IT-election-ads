import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import uuid
import time
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(options=options)


def get_ads_from_file(file):

    # get token from environmental variable

    token = os.environ.get("fb_api_key")

    # read every line of ads_ids.txt into a list of ids

    with open(file=file) as f:
        ids = f.readlines()

    print("The script will try to screenshot {len} ads".format(len=len(ids)))

    # for each id in the list of ids, fetch the ad and save it as a png file

    counter = 0
    for id in ids:
        url = "https://www.facebook.com/ads/archive/render_ad/?id={id}&access_token={token}".format(
            id=id,
            token=token.strip()
        )
        driver.get(url)
        time.sleep(0.3)
        print(id)
        ad = driver.find_element(By.CLASS_NAME, "_8n-d")
        driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', ad)
        ad.screenshot("ads/{id}.png".format(id=id.strip()))
        ids.remove(id)
        if counter == 999:
            with open('ads_ids.txt', 'w') as f:
                f.writelines(ids)
            counter = 0
        else:
            counter += 1

    driver.quit()


if __name__ == "__main__":
    get_ads_from_file("ads_ids.txt")
