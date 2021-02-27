"""
6.  Write a class called Converter. The user will pass a length and a unit when declaring an
    object from the class—for example, c = Converter(9,'inches'). The possible units are
    inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these
    units there should be a method that returns the length converted into those units. For exam-
    ple, using the Converter object created above, the user could call c.feet() and should get
    0.75 as the result.

"""


class Converter:
    def __init__(self, length, unit):
        self.unit = unit
        self.length = length

    ''' Convert the unit to inches, then convert the inches to the desired unit'''

    def convert_inches(self, unit):

        if (self.unit == 'inches'):
            self.length = self.length
        else:
            '''Convert the unit to'''
            switcher_1 = {
                'feet': self.length * 12,
                'yards': self.length * 36,
                'miles': self.length * 63360,
                'kilometers': self.length * 39370,
                'meters': self.length * 39.37,
                'centimeters': self.length / 2.54,
                'millimeters': self.length / 25.4
            }
            self.length = switcher_1.get(self.unit)

        '''Convert the inches to every unit'''

        switcher_2 = {
            'inches': self.length,
            'feet': self.length / 12,
            'yards': self.length / 36,
            'miles': self.length / 63360,
            'kilometers': self.length / 39370,
            'meters': self.length / 39.37,
            'centimeters': self.length * 2.54,
            'millimeters': self.length * 25.4
        }
        return switcher_2.get(unit)

    def inches(self):
        return self.convert_inches('inches')

    def feet(self):
        return self.convert_inches('feet')

    def yards(self):
        return self.convert_inches('yards')

    def miles(self):
        return self.convert_inches('miles')

    def kilometers(self):
        return self.convert_inches('kilometers')

    def meters(self):
        return self.convert_inches('meters')

    def centimeters(self):
        return self.convert_inches('centimeters')

    def millimeters(self):
        return self.convert_inches('millimeters')


c = Converter(10, 'miles')
print(c.feet())
