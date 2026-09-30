import numpy as np, itertools
from k1_function_space import *
np.set_printoptions(precision=4,suppress=True,linewidth=150)
names=['1','cx','sx','cy','sy','cz','sz']
def show(kind):
    null,fs,nb=family(kind,nn_vectors())
    # row-reduce nullspace to a canonical readable basis
    import sympy
    A=sympy.Matrix(np.round(null,10).tolist())
    R,piv=A.rref(iszerofunc=lambda x: abs(x)<1e-8)
    print('== ',kind)
    lab=[f'e:{n}' for n in names]+[f'd{c}:{n}' for c in 'xyz' for n in names]
    for i in range(R.rows):
        terms=[f'{float(R[i,j]):+.3f}*{lab[j]}' for j in range(R.cols) if abs(R[i,j])>1e-8]
        print('   ',' '.join(terms))
for k in ['trivial','sign','axis','full']:
    show(k)
