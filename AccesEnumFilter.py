import argparse
from ast import main

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file', type=str, metavar='', required=True, help="File to be filtered")
parser.add_argument('-o', dest='output', type=str, metavar='', required=True, help="Output file")
parser.add_argument('-w', dest='word', type=str, metavar='', required=True, help="Word to be filtered")
args = parser.parse_args()




filename = args.file
filedest = args.output
filterword = args.word


def main():
    
    linecounter_found = 0
    linecounter = 0
    
    with open(filename, 'r', encoding='utf-16') as f:
        read = f.readlines()
        
        
        
        
        for line in read:
            
            linecounter += 1
            
            if filterword in line:
                linecounter_found += 1
                with open(filedest, 'a', encoding='utf-16') as out:
                    out.write(line)
    print(f"Found {linecounter_found} lines out of {linecounter} lines containing '{filterword}' in '{filename}' and wrote \nthem to '{filedest}'")

                

main()




