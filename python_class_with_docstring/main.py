"""Main app for basic class definitions and usage"""

from user import User
from post import Post

user1 = User("john", "john@example.com", "Tech Support", "p4ss")
user2 = User("miltos", "miltos@example.com", "DevOps guy", "123")

user1.get_user_info()
user1.change_job_description("Pizza tasting specialist")
user1.get_user_info()

# post1 = Post(1,"First post!", "Good day everyone", user1.name)
post2 = Post(2, "Another post!", "Hello everyone. Pizza anyone?", user1)

post2.show_post()
