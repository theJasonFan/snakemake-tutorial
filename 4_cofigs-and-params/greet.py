import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--greeting', required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--repeats', type=int, required=True)
    parser.add_argument('--output', required=True)
    return parser.parse_args()

def main():
    args = parse_args()

    msg = '{} {}\n'.format(args.greeting, args.name)
    msg = msg * args.repeats
    
    with open(args.output, 'w') as out:
        out.write(msg)

if __name__ == "__main__":
    main()