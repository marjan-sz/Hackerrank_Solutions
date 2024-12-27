# # opening file and truncate the size to 100 bytes
# f = open("sample.txt", "a")
# f.truncate(100)
# f.close()



# opening the file in read mode
my_file = open("sample.txt", "r")

# # read line by line and return a list of strings
# data_lines = my_file.readlines()
# new_List = [read_string.replace("\n", "") for read_string in data_lines]
# data_into_list_filtered = list(filter(None, new_List))
# print("data_lines: ", data_into_list_filtered)
# my_file.close()

# reading the file as one string
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when ' ' is seen.
data_into_list = data.replace('\n', " ").split(" ")
# remove empty strs
data_into_list_filtered = list(filter(None, data_into_list))
# printing the number of words
print("Number of words: ", len(data_into_list_filtered))
my_file.close()
