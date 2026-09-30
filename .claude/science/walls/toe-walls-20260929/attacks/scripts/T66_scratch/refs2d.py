import pickle, sympy as sp
from cont2d import *
from match2d import sympy_terms2
pieces = pickle.load(open('cont2d_pieces.pkl', 'rb'))
V2, T3 = pieces['V2'], pieces['T3']
fmap = {hxx: ('h', 0), hyy: ('h', 1), hzz: ('h', 2), hxy: ('h', 3), Pxx: ('P', 0), Pyy: ('P', 1), Pzz: ('P', 2), Pxy: ('P', 3),
        N: ('N', 0), M: ('M', 0), XIx: ('Xx', 0), XIy: ('Xy', 0)}
xi0, xi1 = structure_function()
G_gen = degpart(sp.expand(lie_G((XIx, XIy))), 2)
G1xi1 = degpart(sp.expand(lie_G(xi1)), 2)
REF2 = {
    'T3': sympy_terms2(N * T3, fmap, x, y),
    'V2': sympy_terms2(N * V2, fmap, x, y),
    'G2': sympy_terms2(G_gen, fmap, x, y),
    'xi1': sympy_terms2(G1xi1, fmap, x, y),
    'chi': [],
}
if __name__ == '__main__':
    for k, v in REF2.items():
        print(k, len(v))
