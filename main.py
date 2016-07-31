import argparse
import sys

parser = argparse.ArgumentParser(description='Translates text.')
parser.add_argument('source', metavar='SOURCE', type=str,
                    help='the name of the source language')
parser.add_argument('target', metavar='TARGET', type=str,
                    help='the name of the target language')


args = parser.parse_args()
print(args)

if args.source == args.target:
    print("Translating from {} to {} (press ctrl+c to exit)"
          .format(args.source, args.target))
    while True:
        try:
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if line:
            print("Translation (language = {}): {}"
                  .format(args.target, line.strip()))
        else:
            break
else:
    print("translation between different languages is currently not supported!")
