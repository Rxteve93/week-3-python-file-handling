def read_user_file():
    """
    Asks the user for a filename and attempts to read and print its content,
    handling potential FileNotFoundError and permission errors.
    """
    filename = input("Enter the name of the file you want to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_user_file()
