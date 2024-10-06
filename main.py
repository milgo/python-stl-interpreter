import json
from AND_block import *
from OR_block import *
from ASSIGN_block import *
#from FP_block import *

mem = { "%m1.0" : 1, "%m2.0": 0, "%m3.0": 1}
RLO_obj = { "RLO" : 0, "STACK" : []}

with open('programdata.json', 'r') as file:
    programdata = json.load(file)

#print(globals())
print(RLO_obj)
for item in programdata:
	value = item["function"]
	if value in globals():
		print(value + " " + str(item["target"]))
		f_name = globals()[value]
		RLO_obj = f_name(RLO_obj, item, mem)
		#print(RLO_obj)
print(RLO_obj)