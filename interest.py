def loan_calculator(A,T,R):
	A = int(input("please add loan amount: "))
	#A is the loan amount
	T = int(input("please add time limit: "))
	#T is the time limit for the loan amount
	R = int(input("please add rate: "))
	#R is the interest rate
	if T <=  0:
		print("0 is not valid time")
		#tests for zero and negative numbers
	elif T > 12:
		print("Invalid time limit")
		#tests for maximum months 12
	else:
		return T


	L = (A*((R/100)*(T/12))) + A
	#L is the total loan amount repayable after time T
	return L

#print (loan_calculator(1000,36,12))

