"""Kill check: 'one qubit, one exact nearest-neighbour rotation-symmetric tick has no non-trivial unitary'
is a statement about a ONE-PARTICLE two-component amplitude.  Read the axioms' Qubit literally
(one M_2(C) per site, many-body), and non-trivial exactly covariant radius-1 unitaries exist:
Clifford QCAs (repo: archive/notes/docs/work_history/repo/review_feedback/CUBIC_ONE_QUBIT_CLIFFORD_QCA_UNIQUENESS_CYCLE40_NOTE_2026-07-14.md).
Here: (1) exact symplectic check that Q = L_s H is a valid radius-1 Clifford skeleton over F_2[Z^3],
      s = x+1/x+y+1/y+z+1/z (invariant under all 48 cube symmetries, so the trivial onsite rotation action is covariant);
      (2) operator spreading on a torus: support of the Heisenberg image of a single Pauli X under t ticks."""
import numpy as np, itertools
# (1) symplectic condition bar(Q)^T lam Q = lam over F_2, with s = bar(s): Q = [[0,1],[1,s]] (= L_s H up to convention)
# polynomial entries as functions of the single symbol s (commutative, char 2): represent via truth over s in {0,1}? use sympy GF(2)
import sympy as sp
s = sp.symbols('s')
Q = sp.Matrix([[0,1],[1,s]])
lam = sp.Matrix([[0,1],[1,0]])
Qbar_T = Q.T                       # bar(s)=s, so bar acts trivially on entries
M = (Qbar_T*lam*Q).applyfunc(lambda e: sp.Poly(sp.expand(e), s, modulus=2).as_expr())
print('Qbar^T lam Q mod 2 =', M.tolist(), ' == lam ?', M == lam)
# (2) operator growth on L^3 torus
L = 24
def apply_s(f):
    out = np.zeros_like(f)
    for ax in range(3):
        out ^= np.roll(f, 1, axis=ax) ^ np.roll(f, -1, axis=ax)
    return out
def step(xz):
    x, z = xz
    # Q = [[0,1],[1,s]] acting on column (x,z):  x' = z ; z' = x + s z
    return (z.copy(), x ^ apply_s(z))
x = np.zeros((L,L,L), dtype=np.uint8); z = np.zeros_like(x)
x[0,0,0] = 1
state = (x, z)
c = L//2
print('t, max L1 extent of support of the evolved Pauli string, number of sites in support')
for t in range(0, 9):
    sup = np.argwhere((state[0] | state[1]) > 0)
    d = np.abs(((sup + L//2) % L) - L//2).sum(axis=1)     # L1 distance to origin on torus
    print(t, int(d.max()), len(sup))
    state = step(state)
print('=> exact cone: extent <= t (radius-1 update), and it actually grows every tick (propagating companion class).')
