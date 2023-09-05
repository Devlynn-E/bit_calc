def statement_gen(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


def user_choice():

    text_ok = ["text", "t", "txt"]
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]
    int_ok = ["integer", "int", "#", "num", "number"]

    valid = False
    while not valid:

        response = input("file type (integer / text / image): ").lower()

        if response in text_ok:
            return "text"

        elif response in image_ok:
            return "image"

        elif response in int_ok:
            return "integer"

        elif response == "i":
            want_integer = input("press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            print("please choose a valid response")
            print()


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


def int_bits():

    var_int = num_check("please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_int)

    num_bits = len(var_binary)

    print("\n{} in binary is {}".format(var_int, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""


def text_bits():

    print()

    var_text = input("enter some text: ")

    var_length = len(var_text)
    num_bits = 8 * var_length

    print("\n\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits {} x 8...".format(var_length))
    print("we need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""


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


statement_gen("bit calc for int, txt, img", "-")

print("\n")

keep_going = ""
while keep_going == "":

    data_type = user_choice()
    print("You chose", data_type)

    if data_type == "integer":
        int_bits()

    elif data_type == "image":
        image_bits()

    else:
        text_bits()

    keep_going = input("\nPress <enter> to continue or <any> to quit ")
    print()
    