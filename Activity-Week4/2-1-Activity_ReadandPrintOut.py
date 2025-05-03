# Activity W4-2-1: txt file
# Read the txt file and printout the first and last line of the file. See below

# def read_first_last_lines("Activity-Week4\sample_text.txt"):
with open('Activity-Week4\sample_text.txt', 'r') as file:
    lines = file.readlines()
    if lines:
        print("First line:", lines[0].strip())
        print("Last line:", lines[-1].strip())
