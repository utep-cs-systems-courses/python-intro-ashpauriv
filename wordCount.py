#! /usr/bin/env python3                                                                                                                                                                      
import os
import sys
import string


# Open input file for reading                                                                                                                                                                             
count = {}
with open(sys.argv[1], 'r') as f:
        words = f.read().split()
        for word in words:
            # Remove punctuation and convert to lowercase                                
            word = word.strip(string.punctuation).lower()
            count[word] = count.get(word, 0) + 1
            
sorted_count = sorted(count.items())

# Open output file for writing                                                                                                                                                                            
outp = os.open(sys.argv[2], os.O_WRONLY | os.O_TRUNC)

for key, value in sorted_count:
        os.write(outp, f"{value} {key}\n".encode())
        
os.close(outp)
