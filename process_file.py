# Read and Process a Text File
def process_text_file(filename):
    line_count = 0
    word_count = 0
    character_count = 0
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                character_count += len(line)
        print("\n===== TEXT FILE STATISTICS =====")
        print("File:", filename)
        print("Number of lines:", line_count)
        print("Number of words:", word_count)
        print("Number of characters:", character_count)
        print("================================")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except PermissionError:
        print("Error: Permission denied while opening the file.")
    except UnicodeDecodeError:
        print("Error: The file could not be read using UTF-8 encoding.")
    except OSError as error:
        print("Error while reading the file:", error)
print("===== TEXT FILE PROCESSOR =====")
filename = input("Enter the text file name (example: sample.txt): ")
process_text_file(filename)