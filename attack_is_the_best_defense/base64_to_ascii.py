#!/usr/bin/env python

import sys
import base64

# Check if the correct number of arguments has been provided
if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

# Read the contents of the file
with open(sys.argv[1], "r") as f:
    base64_data = f.read()
    print(base64_data)

# Decode the base64 data to binary
binary_data = base64.b64decode(base64_data)

# Convert the binary data to ASCII
ascii_data = binary_data.decode("ascii")

# Print the ASCII data to stdout
print(ascii_data)

