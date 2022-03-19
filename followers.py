# Code written by YASHWANT JODHA
# for internship assignment

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_followers(username):
    """
    Finds followers of the public twitter account.

    Input:
        username - username of the twitter profile
    
    Output:
        Followers of the account.
    """
    
    # driver initialization and opening twitter link
    driver = selenium.webdriver.Chrome()
    twitter_url = f'https://twitter.com/{username}'
    driver.get(twitter_url)

    # followers element on the page; wait for "wait_time" to load
    # as content is async loaded
    wait_time = 5
    followers_xpath = r"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div[2]/a/span[1]/span"
    followers_element = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, followers_xpath)))
    
    followers = followers_element.text
    driver.quit()
    return followers


# Examples
print(find_followers("elonmusk")) # 78.4M
print(find_followers("yashwantjodha01")) # 2 :)