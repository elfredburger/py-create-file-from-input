def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:

        while True:
            message = input("Enter new line of content: ")
            if message == "stop":
                break
            f.write(message + "\n")


if __name__ == "__main__":
    main()
