import math
from colorama import init
init()
from colorama import Fore, Style
from prettytable import PrettyTable

def parseAddressDA(address, blocks, block_size, word_size = 4):
    """ Helper function that will parse the address, for direct Associative method. \n
        Paramenters: \n
        \t address \n
        \t blocks \n
        \t block_size \n
        \t word_size: default is 4\n
        Return dictionary with tag, address_result, index,word_offset, byte_offset
    """
    binary_address = bin(address)[2:].zfill(32)
    byte_offset_size = int(math.log2(word_size))
    word_offset_size = int(math.log2(block_size))
    index_size = int(math.log2(blocks))
    byte_offset = int(binary_address[-byte_offset_size:],2)
    if word_offset_size == 0:
        word_offset = 0
    elif word_offset_size == 1:
        word_offset = int(binary_address[len(binary_address)-byte_offset_size-1],2)
    else:
        word_offset = int(binary_address[-byte_offset_size-byte_offset_size:-byte_offset_size],2)
    index = int(binary_address[-byte_offset_size-word_offset_size-index_size:-byte_offset_size-word_offset_size],2)
    tag = int(binary_address[:-(byte_offset_size+byte_offset_size)-1],2)
    address_result = int(binary_address[:-byte_offset_size],2)
    return {"tag" : tag, "address_result" : address_result , "index" : index , "word_offset" : word_offset, "byte_offset" : byte_offset}

def directAssociative(addresses,blocks,block_size,extended=True,pretty_print=True):
    """ Creates the full table for direct Associative mode . \n
        Paramenters: \n
        \t address \n
        \t blocks \n
        \t block_size \n
        \t pretty_print which defaults to one \n
        Return full table as a list of lists with the data and also will print it, unless specified to false
    """
    table = eval(str([[" "] * block_size] * blocks))
    full_table = []
    for address in addresses:
        parseResult = parseAddressDA(address, blocks, block_size)
        index, word, address_result = parseResult["index"], parseResult["word_offset"], parseResult["address_result"]
        if address_result in table[index]:
            result = [address,Fore.GREEN + "HIT" + Style.RESET_ALL]
        elif table[index][1:] == table[index][:-1] and len(table[index])>1 or table[index]==[" "]:
            result = [address,Fore.RED + "MISSED" + Style.RESET_ALL]
        else:
            result = [address, Fore.YELLOW + "COLLISION" + Style.RESET_ALL]
        table[index][word] = address_result
        if len(table[index])>1:
            for i in range(0,word):
                try:
                    table[index][word-i-1] = address_result - i - 1
                except:
                    pass
            for x in range(word-1,len(table[index])):
                try:
                    table[index][word+x] = address_result + x
                except:
                    pass
        if(extended):
            full_table.append(flat_list(eval(str([result[0],parseResult["tag"],parseResult["address_result"],index,word,parseResult["byte_offset"],table,result[1]]))))
        else:
            full_table.append(flat_list(eval(str([result[0],table,result[1]]))))
    if pretty_print:
        t = PrettyTable(header(blocks,block_size,extended))
        for row in full_table:
            t.add_row(row)
        print(t)
    return full_table

def header(blocks,block_size,extended):
    """ Creates the header list . \n
        Paramenters: \n
        \t blocks \n
        \t block_size \n
        Return dictionary list with the header
    """
    if(extended):
        header =["Address","Tag","Real Address","Index","WordOffset","ByteOffset"]
    else:
        header =["Address"]
    for i in range(0,blocks):
        for x in range(0,block_size):
            header.append("B%i W%i"%(i,x))
    header.append("Result")
    return header

def flat_list(old_list):
    """Function for creating one big array from array of arrays, this is recursive so be careful"""
    new_list = []
    for element in old_list:
        if "list" in str(type(element)):
            recursive_list = flat_list(element)
            for sub_element in recursive_list:
                new_list.append(sub_element) 
        else:
            new_list.append(element)
    return new_list

def demo():
    """ Demo function, as its name describes it is for testing the usage of the script. Can also be seen as an example \n
        No parameters and no return
    """
    addresses = [3,180,43,2,191,88,190,14,181,44,186,253]
    print ("example 1")
    directAssociative(addresses,8,1)
    print ("example 2")
    directAssociative(addresses,4,2)
    print ("example 3")
    directAssociative(addresses,2,4)

#TODO Implement Full asociative