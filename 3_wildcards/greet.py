import argparse

_a_dictionary = {
    'en': {
        'hello': 'Hello',
        'goodbye': 'Goodbye',
        'world' : 'world',
    },
    'fr': {
        'hello': 'Bonjour',
        'goodbye': 'Au revoir',
        'world' : 'monde',
    },
    'es': {
        'hello': 'Hola',
        'goodbye': 'Adios',
        'world' : 'mundo'
    }
}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', required=True)
    parser.add_argument('--greeting', required=True)
    parser.add_argument('--output', required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    words = _a_dictionary[args.language]
    msg = '{} {}\n'.format(words[args.greeting], words['world'])
    
    with open(args.output, 'w') as out:
        out.write(msg)

if __name__ == "__main__":
    main()