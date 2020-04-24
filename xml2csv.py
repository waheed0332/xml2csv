#!/usr/bin/env python

__author__ = 'Waheed Abbas (@waheed0332)'
__date__ = '20200424'
__version__ = '1.0'
__description__ = """This script is able to parse any xml file.
                     You can also parse nested xml files as well.
                  """

import xmltodict
import collections
import pandas as pd
import argparse
import multiprocessing as mp
import glob


def converter(data, output = {}, name = ""):
    if type(data) is collections.OrderedDict:
        for key in data.keys():
            d_ = data[key]
            if type(d_) is collections.OrderedDict:
                output = converter(d_, output, name+key+".")
            else:
                if type(d_) is list:
                    for item in d_:
                        output = converter(item, output, name+key+".")
                else:
                    if name+key in output.keys():
                        count = 0
                        while(1):
                            if name+key+'.'+str(count) not in output.keys():
                                output[name+key+'.'+str(count)] = d_
                                break
                            else:
                                count+=1
                    else:
                        output[name+key] = d_
    return output


def parse(path):
    with open(path,'r') as file:
        xml = file.read()
        xmlDict = xmltodict.parse(xml)
    
    response = converter(xmlDict)
    return response

def main():
    try:
        if(args.xml!=None):
            file_list = args.xml
        else:
            file_list = glob.glob(args.bulk+'/*')
        
        pool = mp.Pool(mp.cpu_count())
        result = pool.map(parse, file_list)
        df = pd.DataFrame(result)
        df.to_csv(args.csv, index=False)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--xml",
                        nargs='*',
                        help="Specify a xml file.")
    
    parser.add_argument("-b", "--bulk",
                        nargs='?',
                        help="Specify path to xml files folder.")
    
    parser.add_argument("-csv", "--csv",
                        nargs='?', const='converted.csv',
                        help="Specify the name of a csv file to write to.")
    args = parser.parse_args()

    if not args.xml and not args.bulk:
        print("\n[-] Please specify an input file to parse."
              "\nUse -f <file.xml> to specify the file."
              "\nOr use -b <folder path> to specify the path to xml files")
        exit()
    
    if not args.csv:
        print("\n[-] Please specify an output file name to put data. "
              "Use -csv <file.csv> to specify the file\n")
        exit()

    main()