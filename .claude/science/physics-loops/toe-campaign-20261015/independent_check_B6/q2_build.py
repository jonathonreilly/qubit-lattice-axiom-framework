import sympy as sp, itertools, sys, pickle
from exact_setup import *
G=rotations()
alg=Alg(2,perm_rep2)
offs=[tuple(n) for n in itertools.product([-1,0,1],repeat=3)]
eb=equivariant_basis(alg,G,offs)
print('dim',len(eb))
pickle.dump(eb,open('q2_basis.pkl','wb'))
