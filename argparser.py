import argparse
import sys

class MyArgParser(argparse.ArgumentParser):
    def __init__(self):
        super(MyArgParser, self).__init__()
        self.add_argument(
            '--batch_size',
            type=int,
            default=100,
            help='Number of examples to process in a batch (ie. 400)')

def main(unused_argv):
	print ("batch size = {}".format(FLAGS.batch_size))
	print ("unused argv = {}".format(unused_argv))

if __name__ == '__main__':
    parser = MyArgParser()
    FLAGS, unparsed = parser.parse_known_args()
    argv=[sys.argv[0]] + unparsed
    main(argv)
