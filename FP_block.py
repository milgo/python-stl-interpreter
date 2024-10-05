def pre_FP(RLO_obj, BLOCK_obj):
	RLO_obj["STACK"].append(2)
	print("-->FP push rlo")
	return RLO_obj
	
def post_FP(RLO_obj, BLOCK_obj):
	print("-->FP pop rlo")
	RLO_obj["RLO"] = RLO_obj["STACK"].pop()
	return RLO_obj
	
def FP(RLO_obj, BLOCK_obj):
	RLO_obj["RLO"] = RLO_obj["RLO"] + 1
	print("-->FP execute " + str(RLO_obj["RLO"]))
	return RLO_obj