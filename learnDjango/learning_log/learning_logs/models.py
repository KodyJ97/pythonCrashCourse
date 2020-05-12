from django.db import models


class Topic(models.Model):
    """A topic the user is learning about"""

    # The text attribute is a CharField—a piece of data that’s made up of characters,
    # or text. You use CharField when you want to store a small amount of text,
    # such as a name, a title, or a city. When we define a CharField attribute,
    # we have to tell Django how much space it should reserve in the database.
    # Here we give it a max_length of 200 characters, which should be enough to
    # hold most topic names.
    text = models.CharField(max_length=200)

    #The date_added attribute is a DateTimeField—a piece of data that will record
    # a date and time ➋. We pass the argument auto_add_now=True, which tells
    # Django to automatically set this attribute to the current date and time
    # whenever the user creates a new topic.
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specified learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
