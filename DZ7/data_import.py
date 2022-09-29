import json

def line_to_dict(split_Line):

    line_dict = {}
    for part in split_Line:
        key, value = part.split(":", maxsplit=1)
        line_dict[key] = value

    return line_dict


def convert() :
    f = open("Q:\Python\DZ\DZ_Python\DZ7\data\my_txt.txt", "r")
    content = f.read()
    splitcontent = content.splitlines()

    lines = [line.split(' | ') for line in splitcontent]

    lines = [line_to_dict(l) for l in lines]

    with open("Q:\Python\DZ\DZ_Python\DZ7\data\json_txt.json", 'w') as fout:
        json.dump(lines, fout, indent=4)