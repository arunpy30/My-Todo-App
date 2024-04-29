FILEPATH = "todos.txt"  #assiging a str to variable tp use late without typing


def get_todos(filepath=FILEPATH):    #making todos.txt as default argument to avoid typing many time
    with open(filepath, 'r') as file_local:    #this is context manager, use files without closing
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):   #can't provide default parametet followed by non default parameter
    with open(filepath, 'w') as file:       #todos_arg non default, filpath default paramt.
        file.writelines(todos_arg)

if __name__ == "__main__":  # prevent from protecting these print fun while running todocli.py
    print("Hello")
    print(get_todos())
