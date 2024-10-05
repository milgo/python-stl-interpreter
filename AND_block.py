def pre_AND(RLO_obj, BLOCK_obj):
	RLO_obj["STACK"].append(2)
	print("-->AND push rlo")
	return RLO_obj
	
def post_AND(RLO_obj, BLOCK_obj):
	print("-->AND pop rlo")
	RLO_obj["RLO"] = RLO_obj["STACK"].pop()
	return RLO_obj
	
def AND(RLO_obj, BLOCK_obj):
	RLO_obj["RLO"] = RLO_obj["RLO"] + 1
	print("-->AND execute " + str(RLO_obj["RLO"]))
	return RLO_obj