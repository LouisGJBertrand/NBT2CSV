# NBT 2 CSV Tool for Create Schematics and structure blocks

This tool exports in csv format every blocks required for structure blocks, create schematics etc.

/!\ some blocks like grass are placed in the schematicanon via dirt blocks, this tool will not register grassblocks as dirt but as grass blocks

This tool uses the NBT standard file format. it is compatible with every GZIPed nbt files (structures, create schematics etc.)

# Usage

put all your .nbt files you wish to convert to csv in the input folder, then run the script with

```bash
py .\nbt_util.py
```

the script will output every csv to the output folder as well as a global one with cumulated block count.

The python file has a `__main__` test hence you can import it in your project as a standard python module.


Getting the CSV of the block count for the structure

```py
# exportCSV :
#   True    = will return the total block dictionary and export the file to CSV
#   False   = will return the total block dictionary
Block_needed = NBT2CSV(filename = "GlobalPathTo\\YourFile.nbt", exportCSV = True)
```

Combining two block dictionaries

```py
# Combine two block count dicts into one.
CombinedDict = CombineElements(PaletteA = {"block_name":1}, PaletteB = {"block_name":5})
```


# Requirements

```
Python 3.+
pip
NBT Module (https://pypi.org/project/NBT/)
```

# Installation

click on code then download the zip of the git. Unzip in a folder.

alternatively you can clone the git with

```
git clone https://github.com/LouisGJBertrand/NBT2CSV.git
```

to install the nbt module execute the following command:

```batch
pip install NBT
```

# License

```
Tool:
MIT License Standard - (C) Louis BERTRAND

Initial method for reading NBT Data (answer by hc_dev)
https://stackoverflow.com/questions/74857267/how-do-i-convert-a-string-nbt-into-json-with-python
```
