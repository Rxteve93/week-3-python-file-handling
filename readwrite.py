def modify_file(input_filename, output_filename="modified_file.txt"):
    """
    Reads each line from an input file, adds a line number,
    and writes the modified lines to a new output file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str, optional): The name of the output file.
                                         Defaults to "modified_file.txt".
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line_number, line in enumerate(infile, 1):
                modified_line = f"{line_number}: {line}"
                outfile.write(modified_line)
        print(f"Successfully read '{input_filename}' and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "original.txt"  # You can change this to your input filename
    modify_file(input_file)
