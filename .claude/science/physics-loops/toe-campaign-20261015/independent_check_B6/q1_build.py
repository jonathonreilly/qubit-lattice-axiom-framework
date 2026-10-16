import sympy as sp, itertools, pickle, time
from exact_setup import *
t=time.time()
G=rotations()
alg=Alg(1,lambda R: sp.eye(1))
r=int(__import__('sys').argv[1])
offs=[tuple(n) for n in itertools.product(range(-r,r+1),repeat=3)]
eb=equivariant_basis(alg,G,offs)
print('dim',len(eb),time.time()-t)
pickle.dump(eb,open('q1_basis_r%d.pkl'%r,'wb'))
