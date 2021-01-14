lengths = []

usr_input = float(input("Enter the length in feet:"))

lengths.append(usr_input)

lengths.append(lengths[0] * 12)
lengths.append(lengths[0] * 0.3333)
lengths.append(lengths[0] * 0.000189394)
lengths.append(lengths[0] * 304.8)
lengths.append(lengths[0] * 30.48)
lengths.append(lengths[0] * 0.3048)
lengths.append(lengths[0] * 0.0003048)

while(True):

    selector = int(input('''For inches enter 1
                             For yards enter 2
                             For miles enter 3
                             For millimeters enter 4
                             For centimeters enter 5
                             For meters enter 6
                             For kilometers enter 7
                            '''))

    print(lengths[selector])
