def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile content:\n")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_file_with_error_handling()
