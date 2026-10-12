"""1D control: the integrable XXZ ring (a qubit law) has an exactly conserved local odd charge
Q3 = sum_j [h_{j,j+1}, h_{j+1,j+2}] (the energy current), range 3, whose one-magnon symbol is odd with
nonzero slope at k=0: an IR-normalised exactly conserved 'momentum' with a local continuity identity.
A next-nearest-neighbour ZZ term (non-integrable) destroys it.  Dense ED on L=10."""
import numpy as np
from functools import reduce
L = 10
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
def op(ops):  # ops: dict site->matrix
    return reduce(np.kron, [ops.get(j, I2) for j in range(L)])
def h(j, D):
    a, b = j % L, (j+1) % L
    return op({a: X, b: X}) + op({a: Y, b: Y}) + D*op({a: Z, b: Z})
for D, J2 in [(0.5, 0.0), (0.5, 0.3), (1.7, 0.0)]:
    hs = [h(j, D) for j in range(L)]
    H = sum(hs) + J2*sum(op({j % L: Z, (j+2) % L: Z}) for j in range(L))
    Q3 = sum(hs[j] @ hs[(j+1) % L] - hs[(j+1) % L] @ hs[j] for j in range(L))
    c = H @ Q3 - Q3 @ H
    print(f"Delta={D}, J2(nnn ZZ)={J2}: ||[H,Q3]||_F/||Q3||_F = {np.linalg.norm(c)/np.linalg.norm(Q3):.2e}")
    if J2 == 0:
        # one-magnon sector: states with one down spin at site r; Q3 diagonal in k
        idx = [int(''.join('1' if s == r else '0' for s in range(L)), 2) for r in range(L)]
        Q1 = Q3[np.ix_(idx, idx)]; H1 = H[np.ix_(idx, idx)]
        ks = 2*np.pi*np.arange(L)/L
        U = np.exp(1j*np.outer(np.arange(L), ks))/np.sqrt(L)
        q = np.real_if_close(np.diag(U.conj().T @ Q1 @ U)); e = np.real(np.diag(U.conj().T @ H1 @ U))
        # fit q(k) = a sin k + b sin 2k
        A = np.vstack([np.sin(ks), np.sin(2*ks)]).T; coef = np.linalg.lstsq(A, (q/1j).real if np.iscomplexobj(q) else q, rcond=None)[0]
        print(f"   one-magnon Q3 symbol /i = {coef[0]:+.4f} sin k {coef[1]:+.4f} sin 2k ; slope at 0 = {coef[0]+2*coef[1]:+.4f}")
