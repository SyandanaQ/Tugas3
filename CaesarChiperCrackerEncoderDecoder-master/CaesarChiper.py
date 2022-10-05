uppercase_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number = ["1","2","3","4","5","6","7","8","9","0"]

def main():
    cc_text = input("""
CAESAR CHIPER 

Menu :
2)Decode Text 
1)Encode Text 
3)Break Caesar Chiper Encrypted Text

Silahkan pilih menu yang tersedia : """)
    if cc_text == "1":
        encode_with_cc()
    elif cc_text == "2":
        decode_with_cc()
    elif cc_text == "3":
        cc_breaker()
    else:
        print("Nomere salah lurr\n")
        main()

def go_to_menu():
    cc_text = input("Kembali ke main menu 1)Yes 2)No ?  ")
    cc_text.lower()
    if cc_text == "1" or cc_text == "yes":
        main()
    elif cc_text == "2" or cc_text == "no":
        print("Sampai jumpa lagi!!")
    else:
        print("Nomere salah lurr")

def encode_with_cc():
    cc_text = input("\nWhat text do you want to encode? ")
    shift = int(input("How many shift do you want to have? "))
    shiftcount = 0
    counter = 0
    cc_text = list(cc_text)
    for word in cc_text:
        if word in uppercase_alphabets:
            shiftcount = uppercase_alphabets.index(cc_text[counter]) + shift
            if shiftcount >= 26:
                shiftcount %= 26
            cc_text[counter] = uppercase_alphabets[shiftcount]
            counter += 1
        elif word in lowercase_alphabets:
            shiftcount = lowercase_alphabets.index(cc_text[counter]) + shift
            if shiftcount >= 26:
                shiftcount %= 26
            cc_text[counter] = lowercase_alphabets[shiftcount]
            counter += 1
        elif word in number:
            shiftcount = number.index(cc_text[counter]) + shift
            if shiftcount >= 10:
                shiftcount %= 10
            cc_text[counter] = number[shiftcount]
            counter += 1
        else:
            counter += 1
    cc_text = "".join(cc_text)
    print(f"Hasil encoded : {cc_text}")
    go_to_menu()

def decode_with_cc():
    cc_text = input("\nWhat text do you want to decode? ")
    shift = int(input("How many shift did that text have? "))
    shiftcount = 0
    counter = 0
    cc_text = list(cc_text)
    for word in cc_text:
        if word in uppercase_alphabets:
            shiftcount = uppercase_alphabets.index(cc_text[counter]) - shift
            if shiftcount >= 26:
                shiftcount %= 26
            cc_text[counter] = uppercase_alphabets[shiftcount]
            counter += 1
        elif word in lowercase_alphabets:
            shiftcount = lowercase_alphabets.index(cc_text[counter]) - shift
            if shiftcount >= 26:
                shiftcount %= 26
            cc_text[counter] = lowercase_alphabets[shiftcount]
            counter += 1
        elif word in number:
            shiftcount = number.index(cc_text[counter]) - shift
            if shiftcount >= 10:
                shiftcount %= 10
            cc_text[counter] = number[shiftcount]
            counter += 1
        else:
            counter += 1
    cc_text = "".join(cc_text)
    print(f"Hasil encrypted  : {cc_text}")
    go_to_menu()

def cc_breaker():
    cc_text = input("\nWhat text do you want to crack? ")
    shiftcount = 0
    counter = 0
    shift = 1
    i = 1
    while i != 26:
        cc_text = list(cc_text)
        for word in cc_text:
            if word in uppercase_alphabets:
                shiftcount = uppercase_alphabets.index(cc_text[counter]) + shift
                if shiftcount >= 26:
                    shiftcount %= 26
                cc_text[counter] = uppercase_alphabets[shiftcount]
                counter += 1
            elif word in lowercase_alphabets:
                shiftcount = lowercase_alphabets.index(cc_text[counter]) + shift
                if shiftcount >= 26:
                    shiftcount %= 26
                cc_text[counter] = lowercase_alphabets[shiftcount]
                counter += 1
            elif word in number:
                shiftcount = number.index(cc_text[counter]) + shift
                if shiftcount >= 10:
                    shiftcount %= 10
                cc_text[counter] = number[shiftcount]
                counter += 1
            else:
                counter += 1
        cc_text = "".join(cc_text)
        print(f"Attempt {i} : {cc_text}")
        counter = 0
        i += 1
    go_to_menu()

main()