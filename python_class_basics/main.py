from user import User
from post import Post

user1 = User("john", "john@example.com", "Tech Support", "p4ss")
user2 = User("miltos", "miltos@example.com", "DevOps guy", "123")

#user1.getUserInfo()
#user1.changeJobDesc("Health Inspector")
user1.getUserInfo()

#post1 = Post(1,"First post!", "Good day everyone", user1.name)
post2 = Post(2, "Second post!", "Hi everyone", user1)

post2.showPost()
