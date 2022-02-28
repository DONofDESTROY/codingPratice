import sys
def main():
    message = '''
        Welcome to shopping site
        I am your assistant
        tell me what to do
        1. Checkout cart
        2. empty my cart
        3. look for items
        4. add items

    '''
    print(message)
    while True:
        try: 
            n = int(input())
            if(n==1):
                print("Check out cart")
            if(n==2):
                print("empty my cart")
            if(n==3):
                print("look for items")
            if(n==4):
                print("add items")
            if(n>5):
                raise Exception("unkown number")
        except:
            print("Entered number/word is not supported")
            print("exiting system")
            sys.exit(0)
        
    


main()
