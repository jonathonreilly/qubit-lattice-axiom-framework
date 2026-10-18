#!/usr/bin/env python3
"""(d): odd-L torus with U(1) twist theta. Quasi-periodic convention psi(w + L n) = e^{i theta.n} psi(w).
Operators defined on the infinite lattice and restricted to the quasi-periodic subspace (function language):
  (G psi)(R v, R c) = (-1)^(lam.v + tau(c)) psi(v, c);  (H psi)(w, a) = sum_d h_d[a, b] psi(w - d, b).
A rotation preserves twist theta iff R theta + pi L R lam = theta (mod 2 pi)."""
import itertools, sys
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__file__))
from chk_core import *

def qp_ops(L, theta):
    sites = list(itertools.product(range(L), repeat=3)); si = {v: i for i, v in enumerate(sites)}
    n = 12 * len(sites)
    def red(w):
        w = np.array(w); w0 = w % L; return tuple(int(x) for x in w0), (w - w0) // L
    def G(g):
        A = np.zeros((n, n), complex); Rinv = OH[g].T
        for w0 in sites:
            v = Rinv @ np.array(w0)                     # full preimage (integer vector)
            v0, nn = red(v)
            ph = (-1.0) ** int(LAM[g] @ v) * np.exp(1j * np.dot(theta, nn))
            A[12*si[w0]:12*si[w0]+12, 12*si[v0]:12*si[v0]+12] += ph * UF[g]
        return A
    def H(h):
        A = np.zeros((n, n), complex)
        for w in sites:
            for d, B in h.items():
                v0, nn = red(np.array(w) - np.array(d))
                A[12*si[w]:12*si[w]+12, 12*si[v0]:12*si[v0]+12] += B * np.exp(1j * np.dot(theta, nn))
        return A
    return G, H

T4 = torus_ops(4)
rr = np.random.default_rng(2)
hr = {d: rr.normal(size=(12, 12)) + 1j*rr.normal(size=(12, 12)) for d in itertools.product(range(-1, 2), repeat=3)}
A = T4['from_blocks'](hr); A = (A + A.conj().T)/2
S = sum(T4['G'](g) @ A @ T4['G'](g).T for g in PROPER) / 24
h = T4['to_blocks'](S)

kst = np.array([.5, -.5, .5]) * np.pi
c2x, c2y = find(np.diag([1, -1, -1])), find(np.diag([-1, 1, -1]))
for L, theta, lab in ((3, kst, 'k*'), (3, -kst, '-k*'), (3, np.zeros(3), '0'), (1, kst, 'k*'), (5, kst, 'k*')):
    G, H = qp_ops(L, theta)
    HL = H(h)
    herm = np.allclose(HL, HL.conj().T)
    sym = [g for g in PROPER if np.allclose(G(g) @ HL, HL @ G(g), atol=1e-9)]
    uni = all(np.allclose(G(g).conj().T @ G(g), np.eye(len(HL))) for g in PROPER)
    # compatibility predicted by the affine condition
    pred = [g for g in PROPER if same_k(OH[g] @ theta + np.pi * L * (OH[g] @ LAM[g]), theta)]
    ac = np.allclose(G(c2x) @ G(c2y), -G(c2y) @ G(c2x))
    out = f"L={L} theta={lab}: H hermitian {herm}, unitary {uni}, symmetric rotations {len(sym)}/24 (predicted {len(pred)}, same set {sorted(sym)==sorted(pred)})"
    if L <= 3 and len(sym) == 24:
        ev = np.linalg.eigvalsh(HL); out += f", C2x/C2y anticommute {ac}, all 1p levels even {all(x % 2 == 0 for x in mults(ev, 1e-8))}"
    print(out)

# Fock-level identity Gamma(A)Gamma(B) = (-1)^N Gamma(B)Gamma(A) on the L=1 twisted torus (12 modes), monomial unitaries
def fock(Um):
    nm = Um.shape[0]; dim = 1 << nm
    pi = [int(np.argmax(np.abs(Um[:, c]))) for c in range(nm)]; uc = [Um[pi[c], c] for c in range(nm)]
    F = np.zeros((dim, dim), complex)
    for s in range(dim):
        occ = [c for c in range(nm) if s >> c & 1]
        # apply c^dag_{pi(o)} in order occ[0], occ[1], ... (state = c^dag_{o_1} c^dag_{o_2}... |0>, o increasing)
        amp = 1.0 + 0j; state = 0; sign = 1
        for o in reversed(occ):                        # rightmost operator acts first
            t = pi[o]
            sign *= (-1) ** bin(state & ((1 << t) - 1)).count('1')
            state |= 1 << t; amp *= uc[o]
        F[state, s] = sign * amp
    return F
G1, H1 = qp_ops(1, kst)
Fa, Fb = fock(G1(c2x)), fock(G1(c2y))
Nn = np.array([bin(s).count('1') for s in range(1 << 12)])
print("L=1 Fock: Gamma(C2x)Gamma(C2y) = (-1)^N Gamma(C2y)Gamma(C2x):", np.allclose(Fa @ Fb, np.diag((-1.0) ** Nn) @ Fb @ Fa))
