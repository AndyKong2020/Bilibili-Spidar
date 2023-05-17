import json
import os
import re
import sys


# This function loads the json file and returns the data
def loadJsonFile(filename):
    if os.path.exists(filename):
        with open(filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
    else:
        print("File does not exist: " + filename)
        sys.exit()


# This function saves the data to the json file
def saveJsonFile(filename, data):
    with open(filename, 'w', encoding='UTF-8') as outfile:
        json.dump(data, outfile, indent=4, separators=(',', ': '), ensure_ascii=False)
        outfile.close()


# This function returns the value of the key in the json file
def getJsonData(jsonData, key):
    value = []
    for video in jsonData:
        value.append(video[key])
    return value


def get_bv(urllist):
    # findall() 查找匹配正则表达式的字符串
    bvlist = []
    for url in urllist:
        bv = re.findall('BV[0-9A-Za-z]{10}', url)
        bvlist.append(bv[0] if bv else None)
    return bvlist
