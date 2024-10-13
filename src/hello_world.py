class helloWorld:
    def say_hello(self):
        return "Hello World!"
    
def main():
    hw = helloWorld()
    print(hw.say_hello)

if __name__ == "__main__":
    main()