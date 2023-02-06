class Intern:
    def __init__(self, name = "My name? I'm nobody, an intern, I have no name.") -> None:
        self.name = name
    
    def __str__(self):
        return self.name
    
    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return self.Coffee()

def call_intern():
    intern = Intern()
    mark = Intern("Mark")

    print("Manager: What's your name?")
    print(intern)
    print("Manager: What's your name?")
    print(mark)
    print("Manager: Mark, go make coffee")
    print(mark.make_coffee())

    try:
        print("Manager: Intern, do the work")
        intern.work()
    except Exception as answer:
        print(answer)
        print("Manager: Intern did not work.")

if __name__ == '__main__':
    call_intern()