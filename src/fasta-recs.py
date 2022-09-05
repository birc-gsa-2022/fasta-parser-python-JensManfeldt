import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()


    with open(args.fasta.name, "r") as file:
        text = file.read()
        chrom = text.split(">")
    

    for i in range(1,len(chrom)):
        name, seq = chrom[i].split("\n", 1)
        name = name.strip()
        seq = seq.replace("\n", "")
        print(name + "\t" + seq)




if __name__ == '__main__':
    main()
