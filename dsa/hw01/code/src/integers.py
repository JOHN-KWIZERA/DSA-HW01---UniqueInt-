# Function that takes in txt file of integers and out puts them without repeating any.


# Step 1 import txt file that has numbers into the function

# Step 2 extract file contentent into python list

# Step 3 iterate list checking for integers

# Step 4 create new list from interated list

# Step 5 check for repeatition register one instance of each integer in the new list

# Step 6: Write the unique integers to a new output txt file


def extract_unique_integers(file_path, output_file):
    # Step 1: Import txt file
    with open(file_path, 'r') as file:
        # Step 2: Extract file content into a list (split by spaces or newlines)
        content = file.read().split()

    # Step 3: Iterate over the list, checking for valid integers
    integer_list = []
    for item in content:
        try:
            # Step 4: Convert to integer and add to the list if it’s a valid integer
            integer_list.append(int(item))
        except ValueError:
            # Ignore non-integer values
            pass

    # Step 5: Remove duplicates by converting to a set and then back to a list
    unique_integers = list(set(integer_list))

    # Step 6: Write the unique integers to a new output txt file
    with open(output_file, 'w') as output:
        for num in sorted(unique_integers):
            output.write(f"{num}\n")

    print(f"Unique integers have been written to {output_file}")


# Example usage
file_path = 'small_sample_input_01.txt'  # Provide the path to your input txt file
output_file = 'output_unique_numbers.txt'  # Specify the output file name
extract_unique_integers(file_path, output_file)
