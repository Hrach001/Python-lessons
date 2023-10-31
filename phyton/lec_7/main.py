while True:
    file_name = input("Enter the name of the text file you want to open: ")

    try:
        file = open(file_name, 'r')
        file_contents = file.read()
        print(f"File '{file_name}' contents:")
        print(file_contents)
        file.close()
        break
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please enter a valid file name.")
    # except ValueError:
    #     print("Invalid input. Please enter a valid file name.")
    continue

    while True:
        choice = input("Do you want to write to the same file (same) or a new file (new)? ")
        if choice == 'same':
            try:
                file = open(file_name, 'a')
                new_content = input("Enter content you want to append: ")
                file.write(new_content + "\n")
            except FileNotFoundError:
                print(f"File '{file_name}' not found. Please enter a valid file name.")
            else:
                print("Content successfully appended to the file.")
            finally:
                file.close()
                print("File has been closed.")
            break
        elif choice == 'new':
            new_file_name = input("Enter the new file's name: ")
            try:
                new_file = open(new_file_name, "w")
                new_content = input("Enter the content you want to write to the new file: ")
                new_file.write(new_content)
            except FileNotFoundError:
                print(f"File '{new_file_name}' not found. Please enter a valid file name.")
            else:
                print(f"Content successfully written to the new file '{new_file_name}'.")
            finally:
                new_file.close()
                print("File has been closed.")
            break
        else:
            print("Invalid choice. Please enter 'same' for the same file or 'new' for a new file.")
