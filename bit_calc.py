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


statement_gen("bit calc for int, txt, img", "-")

print("\n")

keep_going = ""
while keep_going == "":

    data_type = user_choice()
    print("You chose", data_type)
