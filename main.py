import json
from AND_block import *
from OR_block import *
#from S_block import *
#from FP_block import *

mem = { "%m3.0" : 1, "%m4.0": 0}
RLO_obj = { "RLO" : 0, "STACK" : [], "POP_RLO" : 0}

with open('programdata.json', 'r') as file:
    programdata = json.load(file)

#print(globals())

for item in programdata:
	value = item["function"]
	if value in globals():
		print(value)
		f_name = globals()[value]
		f_name(RLO_obj, item)