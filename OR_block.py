def pre_OR(RLO_obj, BLOCK_obj):
	RLO_obj["STACK"].append(2)
	print("-->OR push rlo")
	return RLO_obj
	
def post_OR(RLO_obj, BLOCK_obj):
	print("-->OR pop rlo")
	RLO_obj["RLO"] = RLO_obj["STACK"].pop()
	return RLO_obj
	
def OR(RLO_obj, BLOCK_obj):
	RLO_obj["RLO"] = RLO_obj["RLO"] + 1
	print("-->OR execute " + str(RLO_obj["RLO"]))
	return RLO_obj