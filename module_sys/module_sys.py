# system input,output
import sys

#sys.stderr.write('This is stderr text\n') # prints in red
#sys.stderr.flush()
#sys.stdout.write('This is stdout text\n')   # prints in black

#print(sys.argv) # file path to the current editing file

#if len(sys.argv) > 1:
#    print(sys.argv[1])

#if len(sys.argv) > 1:
#    print(float(sys.argv[1]) + 5)

def main(arg):
    print(arg)

main(sys.argv[1])
