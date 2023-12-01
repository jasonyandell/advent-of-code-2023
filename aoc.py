def read_data(file):
    txt_file = open(f"{file}", "r")
    file_content = txt_file.read()
    txt_file.close()
    return file_content

def read_lines(file_name):
    with open(file_name) as file:
        inputs = [ line.strip() for line in file ]
    return inputs

def read_lines_raw(file):
    txt_file = open(f"{file}", "r")
    file_content = txt_file.read()
    txt_file.close()
    return file_content.splitlines()