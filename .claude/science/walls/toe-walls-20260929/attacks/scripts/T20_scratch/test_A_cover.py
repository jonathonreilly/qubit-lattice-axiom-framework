"""Test A: is the spinor double cover forced by the soldering choice on the FINITE group O?
Question per action rho: does a linear unitary 2-dim rep U of O exist with U (b.sigma) U^dag = (rho(g) b).sigma ?"""
import itertools
import numpy as np
from common import O, KINDS, rho, su2_of_rotation, I2, check_homs

check_homs()
key = lambda M: tuple(np.round(M.flatten(), 6))
idx = {tuple(g.flatten()): i for i, g in enumerate(O)}


def order(M):
    P = M.copy(); n = 1
    while not np.array_equal(P, np.eye(3, dtype=int)):
        P = P @ M; n += 1
    return n


def gen_closure(gens):
    S = {tuple(np.eye(3, dtype=int).flatten())}
    frontier = [np.eye(3, dtype=int)]
    while frontier:
        nf = []
        for a in frontier:
            for g in gens:
                b = a @ g
                k = tuple(b.flatten())
                if k not in S:
                    S.add(k); nf.append(b)
        frontier = nf
    return S


# find Coxeter generators s, t with s^2 = t^3 = (st)^4 = 1 generating O (S4 = <s,t | s^2,t^3,(st)^4>)
pair = None
for s in O:
    if order(s) != 2:
        continue
    for t in O:
        if order(t) != 3:
            continue
        if order(s @ t) != 4:
            continue
        if len(gen_closure([s, t])) == 24:
            pair = (s, t); break
    if pair:
        break
s, t = pair
print("Coxeter generators found: s (order 2), t (order 3), st (order 4), generate all 24 elements")

results = {}
for kind in KINDS:
    Us0 = su2_of_rotation(rho(kind, s))
    Ut0 = su2_of_rotation(rho(kind, t))
    ok = []
    for a in [1, -1, 1j, -1j]:
        Us = a * Us0
        if not np.allclose(Us @ Us, I2, atol=1e-9):
            continue
        for k in range(6):
            b = np.exp(2j * np.pi * k / 6)
            Ut = b * Ut0
            if not np.allclose(np.linalg.matrix_power(Ut, 3), I2, atol=1e-9):
                continue
            W = Us @ Ut
            if np.allclose(np.linalg.matrix_power(W, 4), I2, atol=1e-9):
                ok.append((a, k))
    results[kind] = len(ok) > 0
    print(f"[method 1] action={kind:8s}: linear 2-dim lift of the presentation exists? {results[kind]}  (#phase choices: {len(ok)})")

# Method 2: lifted group G^ in SU(2); is -1 in its commutator subgroup?
def su2_key(U):
    return tuple(np.round(np.concatenate([U.real.flatten(), U.imag.flatten()]), 6))


def su2_closure(gens):
    S = {su2_key(I2): I2}
    frontier = [I2]
    while frontier:
        nf = []
        for a in frontier:
            for g in gens:
                b = a @ g
                k = su2_key(b)
                if k not in S:
                    S[k] = b; nf.append(b)
        frontier = nf
    return S


for kind in KINDS:
    gens = []
    for g in O:
        U = su2_of_rotation(rho(kind, g))
        gens += [U, -U]
    G = su2_closure(gens)
    els = list(G.values())
    comms = []
    for a, b in itertools.product(els, repeat=2):
        comms.append(a @ b @ np.linalg.inv(a) @ np.linalg.inv(b))
    D = su2_closure(comms)
    minus1 = su2_key(-I2) in D
    print(f"[method 2] action={kind:8s}: |G^|={len(G):3d}  |[G^,G^]|={len(D):3d}  -1 in commutator subgroup? {minus1}")

print()
print("Reading: 'trivial','sign','axis' -> True (a linear rep exists: cover NOT forced); 'full' -> False (no linear 2-dim rep of O has Bloch action g; the 2-dim projective rep is the binary octahedral 2O, class nonzero in H^2(S4,U(1))=Z_2).")
# Sanity: enumerate all linear 2-dim reps of S4 (irreps 1, sgn, E, T1, T2 of dims 1,1,2,3,3): 2-dim reps = 1+1, 1+sgn, sgn+sgn, E.
# Their Bloch actions have image of order <= 6 (through S3), never the order-24 octahedral group.
