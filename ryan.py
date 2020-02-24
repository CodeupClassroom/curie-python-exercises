
def hello():
    return "Hello, World!"

def goodbye():
    return "Ciao"

# Add this condition to run procedural code on import.
if __name__ == '__main__':
    print("The Ryan library 📚 is successfully imported. 💯")
    assert hello() == "Hello, World!"
    assert goodbye() == "Ciao"
    print("Tests ran successfully")

