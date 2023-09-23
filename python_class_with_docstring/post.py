"""Module for class definition of a post"""


class Post:
    """Represents a post

    Args:
        post_id (int): The number of the post_id
        title (str): The title of the post
        message (str): The text message of the post
        original_poster (obj): The original poster object
    """

    def __init__(self, post_id, title, message, original_poster) -> None:
        self.post_id = post_id
        self.title = title
        self.message = message
        self.original_poster = original_poster

    def edit_post(self, new_title, new_message):
        """Edit a post

        Args:
            new_title (_type_): _description_
            new_message (_type_): _description_
        """
        self.title = new_title
        self.message = new_message

    def show_post(self):
        """Show a post"""
        print(
            f"Title: {self.title} \nMessage: {self.message} \n written by: {self.original_poster.name}. Tell them what you think at: {self.original_poster.email}\n"  # noqa: E501
        )
