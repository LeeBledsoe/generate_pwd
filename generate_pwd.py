import random as r

def int_to_char(list_to_convert):
    return_list = []

    for item in list_to_convert:
        return_list.append(chr(item))
    
    return return_list

def char_to_int(list_to_convert):
    return_list = []

    for item in list_to_convert:
        return_list.append(ord(item))
    
    return return_list


def generate_pwd(available_dictionary, pwd_length):
    return_pwd = ""
    temp_pwd = []
    x = 0
    
    while x < pwd_length:
        temp_pwd.append(r.choice(available_dictionary))
        x += 1

    temp_pwd = int_to_char(temp_pwd)
    
    for char in temp_pwd:
        return_pwd += char

    return return_pwd

def generate_dictionary(items_to_remove):
    return_dict = []
    default_dict = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                    53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                    73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
                    93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112,
                    113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
    if items_to_remove:
        new_list = char_to_int(items_to_remove)
        set1 = set(default_dict)
        set2 = set(new_list)
        return_dict = list(set1 - set2)
    else:
        return default_dict
        
    return return_dict


def write_to_file(file_path, password):
    with open(file_path, "a") as file:
        file.write(password)
        file.write("\n")


if __name__ == "__main__":
    running = True
    file_path = input("to write to a file enter in the path here or press enter to continue: ")
    char_to_remove = input("Enter in any characters to exclude, press enter to continue: ")
    pwd_length = int(input("Enter the desired password length: "))
    user_choice = ""


    
    while running:

        list_for_removal = []
        dictionary = []
        password = ""

        if char_to_remove:
            for char in char_to_remove:
                list_for_removal.append(char)
        
        dictionary = generate_dictionary(list_for_removal)
        password = generate_pwd(dictionary, pwd_length)

        if file_path:
            write_to_file(file_path, password)
            print("Sucessfully wrote new to password" + file_path + "\n")
        else:
            print(password + "\n")
        
        user_choice = input("generate another password?: y/n" + "\n")
        if(user_choice == "n"):
            running = False
        else:
            print("\n")





        


    