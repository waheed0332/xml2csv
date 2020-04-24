# xml2csv
Converts XML files into csv file, this script is capable of converting extremely nested xml files.

This script utilize power of multiprocessing to convert huge data in less time.

## Requirements
Install required libraries using following command before running script.
`pip install -r requirements.txt`

## Usage

### Convert single xml to csv file
`python xml2csv.py -f ./xml-samples/1.xml -csv out.csv`

### Convert multiple xmls to csv file
`python xml2csv.py -f ./xml-samples/2.xml  ./xml-samples/1.xml -csv out.csv`

### Convert bulk xmls to csv
`python xml2csv.py -b ./xml-samples/ -csv out.csv`

###### Arguments
```
-f Input XML document's filename.
-b Path to the folder containing xml files.
-csv Name of output csv file.
```