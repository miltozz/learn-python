class Post:
    def __init__(self, id, title, message, op) -> None:
        '''int id, str title, str message, obj op'''
        self.id = id
        self.title = title
        self.message = message
        self.op = op

    def editPost(self, new_title, new_message):
        self.title = new_title
        self.message = new_message

    def showPost(self):
        print(f"Title: {self.title} \nMessage: {self.message} \n written by: {self.op.name}. Tell them what you think at: {self.op.email}\n")
