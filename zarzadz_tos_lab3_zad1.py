import base64

text = input("Input text: ")

def szyfr(text):

    choice = input("choose '1' to decode, choose '2' to encode: ")

    if choice == '1':

        data_bytes = text.encode('ascii')

        base64_bytes = base64.b64encode(data_bytes)
        base64_string = base64_bytes.decode('ascii')
        print("Encoded Data: ", base64_string)

    elif choice == '2':

        base64_bytes = text.encode('ascii')

        data_bytes = base64.b64decode(base64_bytes)
        text = data_bytes.decode('ascii')

        print("encoded text : ", text)

    else:
        print("valid command")
        quit()

szyfr(text)

