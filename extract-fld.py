#!/usr/bin/python

import io
import tldextract

infile = "text.txt"

def extract(infile):
    with io.open(infile) as f:
        for line in f:
            domain = line.strip('\n')
            extracted = tldextract.extract(domain)
            if extracted.registered_domain:
                print("{}".format(extracted.registered_domain))
                sv = open('extracted.txt', 'a')
                sv.write(domain + '\n')
                
if __name__ == '__main__':
    extract(infile)
