from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import instaloader

from dotenv import find_dotenv, load_dotenv
import os


class Insta:
    def __init__(self):
        try:
            load_dotenv(find_dotenv(".env"))
        except Exception:
            raise FileNotFoundError("No .env file found! try again...")

        else:
            self.email = os.getenv("EMAIL")
            self.password = os.getenv("PASSWORD")
            self.uname = os.getenv("UNAME")

            if self.email is None or self.password is None or self.uname is None:
                raise Warning("Plese set email password and username in .env file")

            browser = input(
                "What is the browser you are using....\ninput, \n'c' for chrome,\n'f' for firefox,\n'e' for Edge,\n's' for Safari,\n").lower()

            site = f"https://www.instagram.com/"

            if browser == "c":
                profile_path = "/data/chrome"
                options = webdriver.ChromeOptions()
                options.add_argument(f"user-data-dir={profile_path}")
                self.driver = webdriver.Chrome(options=options)
            elif browser == "f":
                profile_path = "/data/Frirefox"
                options = webdriver.FirefoxOptions()
                options.set_preference("profile", profile_path)
                self.driver = webdriver.Firefox(options=options)
            elif browser == "e":
                profile_path = "/data/edge"
                options = webdriver.EdgeOptions()
                options.add_argument(f"user-data-dir={profile_path}")
                self.driver = webdriver.Edge(options=options)
            elif browser == "s":
                self.driver = webdriver.Safari()
            else:
                profile_path = "/data/chrome"
                options = webdriver.ChromeOptions()
                options.add_argument(f"user-data-dir={profile_path}")
                self.driver = webdriver.Chrome(options=options)

            self.driver.get(site)

            self.wait = WebDriverWait(self.driver, 20)

    def login(self):

        try:
            print("Preparing for login...")
            mail = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            mail.send_keys(self.email)

            ps = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            ps.send_keys(self.password)

            button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._acap")))
            button.click()

            not_now = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl")))
            not_now.click()

            notifications = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
            notifications.click()
            print("Logged in")

        except Exception:
            raise NameError("Wrong username or password! try again...")

    def make_following_list(self):
        try:
            print("Making your following profiles list")
            l = instaloader.Instaloader()
            l.login(user=self.uname, passwd=self.password)

            profile = instaloader.Profile.from_username(l.context, "thamod_the_oxytann")
            following_list = [f.username for f in profile.get_followees()]
            print("following profiles list has been created")
            return following_list
        except Exception:
            raise NameError("Wrong username! try again...")

    def unfollowing(self, following_list):
        unfollowing = []
        for index, value in enumerate(following_list):
            print(f"checking user {index + 1}) {value}.....")
            site = f"https://www.instagram.com/{value}"
            self.driver.get(site)

            try:
                following = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "li.xl565be")))[2].find_elements(
                    By.CSS_SELECTOR, "div a span")[0]
                following.click()

                user_following_list = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "div.x1dm5mii")))

                users = user_following_list[0]
                user = users.find_elements(By.CSS_SELECTOR, "div div div div")[1].find_elements(By.CSS_SELECTOR,
                                                                                                "div div div div div a div div span")[
                    0].text
                if not self.uname == user:
                    unfollowing.append(value)
            except IndexError:
                unfollowing.append(value)
        self.driver.close()
        return unfollowing

    def unfollow(self, user_lis):

        for index, value in enumerate(user_lis):
            try:
                print(f"unfollowing user {index + 1}) {value}.....")
                site = f"https://www.instagram.com/{value}"
                self.driver.get(site)
                foll = self.wait.until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "._acan")))
                foll.click()

                unfoll = self.wait.until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, "div.x1i10hfl:nth-child(8)")))[0]
                unfoll.click()

            except Exception:
                pass

        self.driver.close()
