from sys import argv
from os.path import exists

from_file = "test2.txt"
to_file = "new_test2.txt"

print(f"copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()