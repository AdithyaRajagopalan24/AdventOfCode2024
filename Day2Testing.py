def is_valid_row(row):
    """Check if a row is valid based on the given conditions."""
    # Convert the row to a list of integers
    try:
        numbers = list(map(int, row.strip().split()))
    except ValueError:
        return False

    # Check for gradual increase or decrease with differences of 1, 2, or 3
    increasing = all(
        numbers[i] < numbers[i + 1] and 1 <= numbers[i + 1] - numbers[i] <= 3
        for i in range(len(numbers) - 1)
    )
    decreasing = all(
        numbers[i] > numbers[i + 1] and 1 <= numbers[i] - numbers[i + 1] <= 3
        for i in range(len(numbers) - 1)
    )

    return increasing or decreasing

def is_valid_with_one_removal(row):
    """Check if a row becomes valid upon removing one element."""
    try:
        numbers = list(map(int, row.strip().split()))
    except ValueError:
        return False

    for i in range(len(numbers)):
        # Create a new list with one element removed
        modified_row = numbers[:i] + numbers[i+1:]
        # Check if the modified row is valid
        if is_valid_row(" ".join(map(str, modified_row))):
            return True

    return False

def count_valid_rows(file_path):
    """Count the number of valid rows in the file."""
    valid_row_count = 0

    with open("day2_SampleInput.txt", 'r') as file:
        for row in file:
            if is_valid_row(row) or is_valid_with_one_removal(row):
                valid_row_count += 1

    return valid_row_count

# Example usage
if __name__ == "__main__":
    # file_path = input("Enter the path to the text file: ")
    file_path = "day2_SampleInput.txt"
    try:
        result = count_valid_rows(file_path)
        print(f"Number of valid rows: {result}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
