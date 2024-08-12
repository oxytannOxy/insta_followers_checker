from insta import Insta


instagram = Insta()
instagram.login()

with open(file="you_need_to_unfollow.txt", mode="r") as file:
    user_lis = file.readlines()

instagram.unfollow(user_lis)
print("Successfully unfollowed all users in 'you_need_to_unfollow.txt' 😌")
