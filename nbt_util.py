from asyncio.windows_events import NULL
import os
import re
from nbt import nbt # type: ignore


SCRIPT_AUTH = "Louis 'Loé' BERTRAND <github@louisgjbertrand>"
SCRIPT_NAME = "NBT TO CSV UTIL"
SCRIPT_DESCRIPTION = "Made For GoodSoup <3"
SCRIPT_VERSION = "v1.1"


def CombineElements(PaletteA: dict, PaletteB: dict):

    for key in PaletteB:
        block_name = key
        if PaletteA.__contains__(block_name):
            PaletteA[block_name] += PaletteB[block_name]
            continue
        PaletteA[block_name] = PaletteB[block_name]

    return PaletteA

def CreateModNBT(nbtfile, exportCSV = True, filename = NULL):
    palette_data = nbtfile["palette"]
    blocks = nbtfile["blocks"]


    palette = []
    i = 0
    for palette_el in palette_data:
        el_name = str(palette_el["Name"])

        palette.append(el_name)
        i+=1
        continue

    block_dict = {}
    for blocks_list_element in blocks:
        
        # the id has to be converted to integer
        palette_element_id = int(str(blocks_list_element["state"]))
        palette_block_name = palette[palette_element_id]

        if(block_dict.__contains__(palette_block_name)):
            block_dict[palette_block_name] += 1
            continue
        block_dict[palette_block_name] = 1


    if exportCSV:
        csv = "block_name,count\n"

        for key in block_dict:
            block_name = key
            csv += "\""+block_name+"\","+str(block_dict[block_name])+"\n"

        f = open(filename.replace("input", "output").replace(".nbt", ".csv"), "w")
        f.write(csv)
        f.close()
    return block_dict

    
def WorldEditNBT(nbtfile, exportCSV = True, filename = NULL):
    palette_data = nbtfile["Palette"]
    blocks = nbtfile["Data"]

    palette = []
    i = 0
    for palette_el in palette_data:

        el_name = str(palette_el)

        palette.append(re.sub("[\(\[].*?[\)\]]", "",el_name).replace("[]",""))
        i+=1
        continue

    block_dict = {}
    for blocks_list_element in blocks:
        # the id has to be converted to integer
        palette_block_name = palette[blocks_list_element]

        if(block_dict.__contains__(palette_block_name)):
            block_dict[palette_block_name] += 1
            continue
        block_dict[palette_block_name] = 1


    if exportCSV:
        csv = "block_name,count\n"

        for key in block_dict:
            block_name = key
            csv += "\""+block_name+"\","+str(block_dict[block_name])+"\n"

        f = open(filename.replace("input", "output").replace(".nbt", ".csv"), "w")
        f.write(csv)
        f.close()
    return block_dict

def NBT2CSV(filename, exportCSV = True):

    nbtfile = nbt.NBTFile(filename,'rb')


    if("palette" in nbtfile.keys()):
        block_dict = CreateModNBT(nbtfile, exportCSV, filename)
        return block_dict

    if("Schematic" in nbtfile.keys()):
        block_dict = WorldEditNBT(nbtfile["Schematic"]["Blocks"], exportCSV, filename)
        return block_dict


def main():
    
    print(SCRIPT_NAME)
    print("Author "+SCRIPT_AUTH)
    print(SCRIPT_DESCRIPTION)
    print("version "+SCRIPT_VERSION+"\n\n")

    input_directory = os.listdir("./input")
    GlobalBlockCount = {}

    file_counter = 0
    for file_name in input_directory:
        if not file_name.__contains__(".nbt"):
           continue
        print ("found ./input/" + file_name)
        file_counter+=1

    print("\ntotal files to convert: "+ str(file_counter)+"\n")

    file_counter = 0
    while file_counter < len(input_directory):

        file_name = str(input_directory[file_counter])

        if not file_name.__contains__(".nbt"):
            file_counter+=1
            continue

        print ("converting ./input/" + file_name)
        filename = "./input/" + file_name

        block_dict = NBT2CSV(filename, True)
        GlobalBlockCount = CombineElements( GlobalBlockCount , block_dict )

        print ("saved at ./output/" + file_name.replace(".nbt", ".csv"))
        file_counter+=1

    print("\nConvertion finished ("+ str(file_counter)+")")

    csv = "block_name,count\n"

    for key in GlobalBlockCount:
        csv += "\""+key+"\","+str(GlobalBlockCount[key])+"\n"


    f = open("./output/global.csv", "a")
    f.write(csv)
    f.close()

    return 0


if __name__ == '__main__':
    exit(main())
