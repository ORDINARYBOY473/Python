import os 

def write_to_file():
    text = input("Enter text to write: ")
    with open("data.txt", "w") as file:
        file.write(text)
        print("Text written to file successfully")

def read_file():
    """Read and display file contents"""
    try:
        with open("data.txt", "r") as file:
            content = file.read()
        if content:
            print("\n--- File Contents ---")
            print(content)
            print("--- End of File ---\n")
        else:
            print("File is empty.")
    except FileNotFoundError:
        print("File not found.")

def append_to_file():
    """Append text to file"""
    text = input("Enter text to append: ")
    with open("data.txt", "a") as file:
        file.write(text + "\n")
    print("✓ Text appended to file successfully!")

def delete_file():
    """Delete the file"""
    try:
        os.remove("data.txt")
        print("File deleted successfully")
    except FileNotFoundError:
        print("File not found") 

def main():
    """Main function with menu loop"""
    while True:
        print("\n----File Handling Menu----")
        print("1.Write to File")
        print("2.Read File")
        print("3.Append to File")
        print("4.Delete File")
        print("5.Exit")

        choice = input("\n Enter your choice (1-5): ")

        if choice == "1":
            write_to_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_to_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("\nExiting program. GoodBye!")
            break 
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
    



