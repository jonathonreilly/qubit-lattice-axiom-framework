import sympy as sp, itertools, pickle, sys
from exact_setup import *
G=[R for R in rotations() if R[2,2]==1 or R[2,2]==-1]  # stabilizer of z-axis line: D4
print(len(G))
alg=Alg(1,lambda R: sp.eye(1))
r=int(sys.argv[1])
offs=[(a,b,0) for a in range(-r,r+1) for b in range(-r,r+1)]
eb=equivariant_basis(alg,G,offs)
print('dim',len(eb)); pickle.dump(eb,open('plane_basis_r%d.pkl'%r,'wb'))
