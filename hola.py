import argparse
def say_hello(name="World"):
        print("Hello ", name, "!")
parser = argparse.ArgumentParser(description='Say hello.')
parser.add_argument('--name', type=str, required=False,
        metavar='name', help='Nicolas', default='World')
args = parser.parse_args()
say_hello(args.name)