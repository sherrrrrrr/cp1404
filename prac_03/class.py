FILENAME = "file_w3.txt"
# in_file=open(FILENAME)
# for line in in_file:
# text = line.strip().split(",")
# print(text[0])
# in_file.close

name = input("Enter the name of the guitar: ")
year = input("Enter the year of the guitar: ")

in_file = open(FILENAME)
for line in in_file:
    text = line.strip().split(",")
    if text[0] == name and text[1] == year:
        print(f"The price for {name} in {year} is {text[2]}")
        break

in_file.close()
