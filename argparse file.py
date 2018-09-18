import argparse
parser = argparse.ArgumentParser()
args= parser.parse_args()
parser.add_argument('square', help= 'display a square of given number',\
                    default = n, type = int)
print args.square**2