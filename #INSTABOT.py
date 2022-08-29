#INSTABOT
from instabot import Bot

bot = Bot()
bot.login(username="your_username",
          password="your_password")
# Follow
#To folllow a single person
bot.follow("persons username")

# To follow more person.
list_of_user = ["user_id1", "user_id2", "user_id3", "...."]
bot.follow_users(list_of_user)

# To unfollow a single person.
bot.unfollow("user_id")

# To unfollow more person.
unfollow_list = ["user_id1", "user_id2", "user_id3", "..."]
bot.unfollow_users(unfollow_list)

# Count number of followers
followers = bot.get_user_followers("user_id")
print("Total number of followers:")
print(len(followers))

# To send message to a single person.
message = "I like instagram"
bot.send_message(message, "instagram")

# To send same message to many follower.
message = "I like instagram"
list_of_userid = ["user_id1", "user_id2", "user_id3", "..."]
bot.send_messages(message, list_of_userid)

