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


text_bits()
