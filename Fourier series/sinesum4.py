# Exercise 4.20
from math import pi
from sinesum1 import table
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--T', type =float, default = 2*pi, \
                    help = 'Domain of function')
parser.add_argument('--n', 'n values', type = list ,\
                    default ='[1,3,5,10,30,100]', help = 'list of n values' )
parser.add_argument('--a', 'alpha_values', type =list ,\
                    default = '[.01,.25,.49]' , help= 'list of alpha values')
args = parser.parse_args()

table(args.n,args.a,args.T)