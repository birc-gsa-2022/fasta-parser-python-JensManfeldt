import argparse
import sys


def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    # Get things from cords file
    text = ""
    with open(args.fasta.name + "-coordinates", "r") as file:
        text = file.read()
    
    coords = text.split("\n")
    # extract from fasta file

    with open(args.fasta.name, "r") as file:
        text = file.read()
        chrom = text.split(">")
    
    genomeDict = dict()
    for i in range(1,len(chrom)):
        name, seq = chrom[i].split("\n", 1)
        name = name.strip()
        seq = seq.replace("\n", "")
        genomeDict.update({name : seq})

    for i in range(len(coords)):
        coord = coords[i].split("\t")
        if len(coord) == 1:
            pass
        if len(coord) == 3:
            genome = genomeDict.get(coord[0])
            print(genome[int(coord[1])-1: int(coord[2])-1])

             
    #print(f"Now I need to process the records in {args.fasta}")
    #print(f"and the coordinates in {args.coords}")


if __name__ == '__main__':
    main()
