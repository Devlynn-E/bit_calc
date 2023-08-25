def statement_gen(text, decoration):

    ends = decoration * 5

    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


statement_gen("bit calc for int, txt, img", "-")

print("\n")

keep_going = ""
while keep_going == "":
