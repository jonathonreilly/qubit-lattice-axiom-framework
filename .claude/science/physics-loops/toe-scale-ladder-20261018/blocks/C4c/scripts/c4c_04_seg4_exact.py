"""C4c-04: EXACT (sympy) classification of U(1)-conserving Hermitian h on the 4-site segment
S = {0,1,2,3}e (the smallest support with two non-vertex sites), with commuting translates
(t = 1, 2, 3).  By Lemma V the vertices 0 and 3 act diagonally, so the most general h is
    h = D(n0,n1,n2,n3) + sum_{k0,k3} [ a_{k0k3} P_k0 s+_1 s-_2 P_k3 + b_{k0k3} P_k0 s-_1 s+_2 P_k3 ],
with 16 diagonal unknowns D and 4+4 hop unknowns (Hermiticity: b = conj(a)).  We solve the
commutator equations exactly and test whether any solution has a != 0 with b = conj(a).
Also run for the 5-site segment's inner part?  No: only the 4-site case is claimed.
"""
import itertools
import sympy as sp
from c4c_common import check, total

n = 4
D = {c: sp.Symbol('D' + ''.join(map(str, c))) for c in itertools.product((0, 1), repeat=n)}
A = {k: sp.Symbol(f'a{k[0]}{k[1]}') for k in itertools.product((0, 1), repeat=2)}
B = {k: sp.Symbol(f'b{k[0]}{k[1]}') for k in itertools.product((0, 1), repeat=2)}


def h_terms(c):
    """local action of h on local config c (tuple of 4 bits): list of (coef, c')"""
    out = [(D[c], c)]
    k = (c[0], c[3])
    if c[1] == 0 and c[2] == 1:    # s+_1 s-_2 : magnon 2 -> 1
        out.append((A[k], (c[0], 1, 0, c[3])))
    if c[1] == 1 and c[2] == 0:
        out.append((B[k], (c[0], 0, 1, c[3])))
    return out


def apply(t, N, vec):
    """apply h translated by t (sites t..t+3) on region of N sites to vec: dict config->coef"""
    out = {}
    for conf, co in vec.items():
        loc = conf[t:t + n]
        for cf, l2 in h_terms(loc):
            new = conf[:t] + l2 + conf[t + n:]
            out[new] = out.get(new, 0) + co * cf
    return out


eqs = set()
for t in (1, 2, 3):
    N = n + t
    for conf in itertools.product((0, 1), repeat=N):
        v = {conf: 1}
        r1 = apply(0, N, apply(t, N, v))
        r2 = apply(t, N, apply(0, N, v))
        for key in set(r1) | set(r2):
            e = sp.expand(r1.get(key, 0) - r2.get(key, 0))
            if e != 0:
                eqs.add(e)
print("number of distinct nonzero commutator polynomials:", len(eqs))
unk = list(A.values()) + list(B.values()) + list(D.values())
sols = sp.solve(list(eqs), unk, dict=True)
print("solution branches:", len(sols))
bad = []
for sl in sols:
    av = [sp.simplify(A[k].subs(sl)) for k in A]
    bv = [sp.simplify(B[k].subs(sl)) for k in B]
    # Hermitian requires b_k = conj(a_k); a branch is non-diagonal-Hermitian iff some a_k and the
    # matching b_k can both be nonzero
    for ak, bk in zip(av, bv):
        if ak != 0 and bk != 0:
            bad.append((sl, ak, bk))
    print("  branch: a =", av, " b =", bv)
check("seg4: every exact solution has a_k * b_k = 0 for all k, i.e. Hermitian h is diagonal",
      len(bad) == 0, f"{len(bad)} offending branch entries")
# independent certificate: Groebner basis of (commutator ideal + <a_k b_k - 1>) is {1} for each k
# (the commutator equations are homogeneous of degree 2, so a nonzero Hermitian hop |a_k|^2 > 0 can
# be normalised to a_k b_k = 1 with b_k = conj(a_k)).
for k in A:
    G = sp.groebner(list(eqs) + [A[k] * B[k] - 1], *unk, order='grevlex')
    check(f"seg4: Groebner basis with a_{k[0]}{k[1]} b_{k[0]}{k[1]} = 1 is [1] (no Hermitian hop on control {k})",
          list(G.exprs) == [1])
total()
