j=10
while(j>0):
    apt=input("Select a mode: (e)encrypt or (d)decrypt  ")
    if(apt=='e' or apt=='d'):
        txt=input("Enter the text: ")
        s=int(input("Enter the shift number: "))
        def encrypt(txt,s):
            result=""
            for i in range(len(txt)):
                char=txt[i]
                if(char.isupper()):
                    result+=chr((ord(char)+s-65)%26+65)
                elif(char.islower()):
                    result+=chr((ord(char)+s-97)%26+97)
                else:
                    result+=' '
            return result   
        def decrypt(txt,s):
            dResult=""
            for i in range(len(txt)):
                char=txt[i]
                if(char.isupper()):
                    dResult+=chr((ord(char)-s-65)%26+65)
                elif(char.islower()):
                    dResult+=chr((ord(char)-s-97)%26+97)
                else:
                    dResult+=' '
            return dResult
        if(apt=='e'):
            print("The encrypted text is: "+encrypt(txt,s).upper())
        elif(apt=='d'):
            print("cipher-decrypt: "+decrypt(txt,s).upper())
        abc=input("Do you wish to exit:- yes or no  ")
        if(abc=='yes'):
            print("Thank you")
            break
    else:
        print("invalid input")    