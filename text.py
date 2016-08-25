def ParellSenar(v):
	"""
	Aquesta funció comprova si un valor es parell o senar
	Input: valor enter
	Output: 0 si parell, 1 si senar, -1 altrament
	>>> ParellSenar(4)
	0
	>>> ParellSenar(5)
	1
	>>> ParellSenar('a')
	-1
	"""
	if type(v) == int:
		return(v%2)
	else:
		return -1 
