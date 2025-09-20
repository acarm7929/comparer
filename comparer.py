import os 

def compare_files(file1, file2):
    file1_size = set(os.listdir(file1))
    file2_size = set(os.listdir(file2))

    only_in_file1 = file1_size - file2_size
    only_in_file2 = file2_size - file1_size

    in_both = file1_size & file2_size

    print(f"Files only in {file1}: {only_in_file1}")
    print(f"Files only in {file2}: {only_in_file2}")
    print(f"Files in both: {in_both}")


if __name__ == "__main__":

    file1 = input("Enter the path for the first directory: ").strip('"')
    file2 = input("Enter the path for the second directory: ").strip('"')

    compare_files(file1, file2)

    print("Comparison complete.")

  

