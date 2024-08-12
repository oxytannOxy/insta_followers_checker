from insta import Insta


instagram = Insta()
instagram.login()
following_list = instagram.make_following_list()
unfollowing = instagram.unfollowing(following_list)

print(f"All done!")
for f in unfollowing:
    try:
        with open('you_need_to_unfollow.txt', 'w') as file:
            file.write("")
        with open(file="you_need_to_unfollow.txt", mode="a") as file:
            file.write(f"{f}\n")
    except Exception:
        with open(file="you_need_to_unfollow.txt", mode="w") as file:
            file.write(f"{f}\n")

print("check 'you_need_to_unfollow.txt' 😌")
