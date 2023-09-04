def num_check(question, low):

    valid = False
    while not valid:

        error = "please input an integer that is more than ""(or equal to) {}".format(low)

        try:

            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

    valid = False
    while not valid:

        error = "please input a number above zero"

        try:

            length = float(input("enter the length: "))

            if length > 0:
                valid = True

            else:
                print(error)
                print()

        except ValueError:
            print(error)


def image_bits():

    image_width = num_check("image width? ", 1)
    image_height = num_check("image height? ", 1)

    num_pixels = image_width * image_height

    num_bits = num_pixels * 24

    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""


image_bits()
