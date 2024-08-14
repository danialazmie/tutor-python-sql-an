import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path',)
parser.add_argument('--dpi', default='300')

args = parser.parse_args()

print(args.path)
print(args.dpi)