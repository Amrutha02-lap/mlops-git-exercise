class HelloWorld:
    def __init__(self):
        pass  # No initialization needed for now

    def greet(self):
 
        print("Hello, VScode World!")


        print("Hello, GitHub World!")
        print("This is my local change")  # NEW line you add locally
 

def main():
    hw = HelloWorld()
    hw.greet()


if __name__ == "__main__":
    main()
