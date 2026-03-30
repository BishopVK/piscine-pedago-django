class Intern:
    def __init__(self, Name ="My name? I’m nobody, an intern, I have no name."):
        self.Name = Name  # Guardamos el dato en la instancia

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return ("This is the worst coffee you ever tasted.")

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

if __name__ == "__main__":
    unnamed = Intern()
    print(unnamed)

    named = Intern("Mark")
    print(named)

    coffee = named.make_coffee()
    print(f"{named}: {coffee}")

    try:
        unnamed.work()
    except Exception as e:
        if str(e):
            print(f"{unnamed}: {e}")
