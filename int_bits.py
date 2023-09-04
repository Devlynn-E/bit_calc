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
