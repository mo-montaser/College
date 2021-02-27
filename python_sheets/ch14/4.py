"""
4.  Write a class called Time whose only field is a time in seconds. It should have a method called
    convert_to_minutes that returns a string of minutes and seconds formatted as in the fol-
    lowing example: if seconds is 230, the method should return '5:50'. It should also have
    a method called convert_to_hours that returns a string of hours, minutes, and seconds
    formatted analogously to the previous method.

"""


class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return f'{minutes:02}:{seconds:02}'

    def convert_to_hours(self):

        hour = self.seconds // 3600
        seconds = self.seconds % 3600
        minutes = seconds // 60
        seconds %= 60
        return f'{hour:02}:{minutes:02}:{seconds:02}'


# t = Time(90)
# print(t.convert_to_minutes())
# print(t.convert_to_hours())
