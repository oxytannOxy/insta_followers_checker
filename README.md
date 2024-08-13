# Oxy_insta_followers_checker
---
![Oxy_insta_followers_checker](https://i.ibb.co/9gCnqVQ/1e874aeb-bc55-4db7-a6ad-ba4d4b213f36.png)

<div align="center">

![Static Badge](https://img.shields.io/badge/oxytann-blue?style=for-the-badge)

---

![Static Badge](https://img.shields.io/badge/python-blue?style=flat&label=v%203.12.4&labelColor=green)
![Static Badge](https://img.shields.io/badge/selenium-blue?style=flat&label=v%204.23.1&labelColor=green)
![Static Badge](https://img.shields.io/badge/Apache-blue?style=flat&label=license&labelColor=green)

---
</div>

## Instructions 😌

This Python program is used to find the Instagram profiles that you are following but that have not followed you back. To find those accounts, you need to run ***"finder.py"***. Once it finishes, you will get a ".txt" file containing the profiles that have not followed you back. Then you can run ***"unfollower.py"*** to unfollow those profiles. If you want to keep following some of those profiles, simply remove their usernames from the ".txt" file before running ***"unfollower.py"***.

---

## How to install ?

1. Download repo.

    ```sh
    git clone https://github.com/oxytannOxy/insta_followers_checker.git
    ```

2. Go to the folder.

    ```sh
    cd insta_followers_checker
    ```

3. Create the .env file.

    Inside the ***"insta_followers_checker"*** folder, create a ***".env"*** file using a text editor app or terminal. In that file, write your ***"email", "password", and "Instagram username"*** that you need to log in to your Instagram account. Like this...

    ***Ex :-***

    ```sh
    EMAIL=YourEmail
    PASSWORD=YourPassword
    UNAME=YourUsername
    ```

    ***Remember do not put spaces arround the "=" sign and do not skip any of this.***

4. Then Install requirements.

    ```sh
    pip install -r requirements.txt
    ```

5. Find out who unfollowed you run...

    ```bash
    python finder.py
    ```

6. To unfollow them run...

    ***Please read the instructions before use***

    ```bash
    python unfollower.py
    ```
---

<div align="center">

## Credits

![Static Badge](https://img.shields.io/badge/oxytann-blue?style=flat)

[Oxytann](https://t.me/oxytann) 😌

</div>
