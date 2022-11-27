import sys
import getopt
import re
import string

# Command to execute:
# dinucleotide_repeat_finder.py -i <genome_samples>

chromosome_pattern = 'TGTGTGTGTGTGTGTGTG'

# get filename from the input argument "-i <inputfile>"
def get_filename(argv):
    arg_input = ""
    arg_help = "{0} -i <input>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hi:", ["help", "input="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg

    return arg_input


# read the file to build one string without newline
def build_string(filename):
    # Using readline()
    file1 = open(filename, 'r')
    count = 0
    lines = ''

    while True:
        count += 1

        # Get next line from file
        line = file1.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break
        lines = lines + line.strip()
    file1.close()
    return lines.upper()

def find_repeat(chromosomes):
# Find all indices of 'the'
    indices_object = re.finditer(pattern=chromosome_pattern, string=chromosomes)
    indices = [index.start() for index in indices_object]
    number = 1
    for index in indices:
        print('{} {}, {} {}'.format('number:', number, 'offset:', index))
        print('{} {}'.format('repeat:', chromosomes[index-5:index+len(chromosome_pattern)+5]))
        number = number + 1


def main():
    filename = get_filename(sys.argv)
    chromosomes = build_string(filename)
    find_repeat(chromosomes)

if __name__ == "__main__":
    main()
