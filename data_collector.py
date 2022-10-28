

'''
Source:

'''

import client

OUTPUT_FOLDER = "output/"

def startpy():

    filename = "urls.txt"

    with open(filename) as filehandle:
        lines = filehandle.readlines()

    # print(lines)

    for line in lines:
        line = str(line).strip()
        filename = str(line.split("/")[-1]).strip() +".html"

        print(line, filename)
        client.get_single_url(line, OUTPUT_FOLDER+filename)


if __name__ == '__main__':

    startpy()