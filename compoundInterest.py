"""Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by:
A = P(1 + R/100) t
Compound Interest = A – P
Where,
A is amount
P is the principal amount
R is the rate and
T is the time span
"""
P = float(input("Enter the principle amount:"))
R = float(input("Enter the rate% :"))
T = int(input("Enter the time span:"))
A = P*(1+R/100)**T
Ci = A-P
print("Compound Interest: ", Ci)
