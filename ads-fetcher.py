
# read every line of ads_ids.txt into a list of ids



from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver 
import uuid
import time
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("window-size=1920,1080")


driver=webdriver.Chrome(options=options)

for id in ids:
    url="https://www.facebook.com/ads/archive/render_ad/?id={id}&access_token=EAAVgpvtpZBTcBAM8YCEuDzRZAFJ3NhQkgyaPjm0c5QB3TtY7hnyZAZBLzDme4mULrZC8DdiZBbXOzM6eK4oyqWqdXlGZAFC1FXdDMDJemz84S8lwr0zdJzcGUoK5Dza9uZBsTiIoHNTI1G4FTn9XvlNXrLv05KQZBlvpZCmwJ8qHR4YUdNZBLzWOkUNFIM1f5i7YNQZD".format(id=id)
    driver.get(url)

    time.sleep(5)

    print(url)

    ad=driver.find_element(By.CLASS_NAME, "_8n-d")
    driver.execute_script('arguments[0].scrollIntoView({block: "center"});', ad)
    ad.screenshot("ads/{id}.png".format(id=id))

driver.quit()





    





