FILEPATH = "Todo.txt"  # static variable in module


def get_data(filepath=FILEPATH):  # default Parameter
    with open(filepath, "r") as local_file:
        local_list = local_file.readlines()
        return local_list


def put_data(par_list, filepath=FILEPATH):
    with open("Todo.txt", "w") as local_file:
        local_file.writelines(par_list)


if __name__ == "__main__":  # Checks if the root file is executing or not
    print("Only executed if executed by main")
