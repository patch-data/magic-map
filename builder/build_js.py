#!/usr/bin/env python

# Reads a CSV file and outputs a JavaScript object

# Pass it a CSV file

import sys
import csv
import json
from decimal import Decimal

# Override the dumb JSON encoder
# Thanks to http://stackoverflow.com/questions/8652497/caught-typeerror-while-rendering-decimal51-8-is-not-json-serializable
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

filename =  sys.argv[1]

full_dict = csv.DictReader(open(filename, 'rU'))

trimmed_dict = {}

for row in full_dict:
	trimmed_dict[row['Subdomain']] = [Decimal(row['Lat']),Decimal(row['Lng'])]
	
with open('patches.js', 'w') as outfile:
	outfile.write('var lookup = ')
	json.dump(trimmed_dict,outfile,cls=DecimalEncoder)