# COP3502C - LAB 6
# LEO JO
# OCT.25.2023

def encode(password):
    # PASSWORD IS ASSUMED TO BE A STRING
    list_convert = []
    output = ""
    # CONVERT STRING TO LIST
    for i in range(len(password)):
        list_convert.append(int(password[i]))
    # SHIFT DIGITS UP BY 3
    for j in range(len(list_convert)):
        calculate = list_convert[j] + 3
        # REDUCE TO SINGLE DIGIT
        if calculate > 9:
            calculate -= 10
        # ADD TO FINAL OUTPUT
        output += str(calculate)
    return output

def decode(password):
    de_pass = []
    for digit in password:
        digit = int(digit)
        digit -= 3
        digit = str(digit)
        de_pass.append(digit)
    return ''.join(de_pass)


if __name__ == "__main__":
    # SETUP
    en_pass = ""
    de_pass = ""

    # MENU
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            en_pass = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            de_pass = decode(en_pass)
            print(f"The encoded password is {en_pass}, and the original password is {de_pass}.\n")
        elif option == "3":
            break
