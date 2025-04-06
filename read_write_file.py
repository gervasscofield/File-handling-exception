def modify_line(line):
    return line.upper()  # Example modification: convert text to uppercase

def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [modify_line(line) for line in lines]

        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content written to {output_file} successfully!")

    except FileNotFoundError:
        print("Input file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
read_and_write_file("sample_input.txt", "modified_output.txt")
