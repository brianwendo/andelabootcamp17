def word_count(string):
    """This function splits the words in a string and prints out the word and its count in a dictionary"""
    string_list = string.split()
 
    string_dict= {}
    for word in string_list:
        if word in string_dict:
            string_dict[word] += 1
        else:
        	string_dict[word] = 1
    return string_dict
