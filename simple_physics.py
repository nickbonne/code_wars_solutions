
# https://www.codewars.com/kata/simple-physics-problem/train/python

def solveit(vi,vf,t):
	answer = []
	a = (vf - vi)/t
	d = (vi * t) + (0.5)*(a)*(t**2)
	if vi > vf:
		return answer
	else:
		answer = [round(a,2),round(d,2)]
		return answer
