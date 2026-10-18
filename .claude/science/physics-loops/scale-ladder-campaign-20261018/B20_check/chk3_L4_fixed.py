#!/usr/bin/env python3
"""B20 check 3: L4.  The affine momentum action k -> R k + c_R is read off the PSG operators themselves
(Op Bloch(k) = Bloch(k') U on all 64 L=4 momenta), not from spectra.  Then T-fixed points are found by exact
integer arithmetic on (pi/16)Z^3 (finer than B20's (pi/8)Z^3) for the four translation groups; the
translation groups themselves (periodicity / taste shifts) are re-verified on sample words."""
import time
from chklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
# affine action, in units of pi/2 (integers mod 4)
ACT = []
for (P, s), R in zip(rots, ROTS):
    R = np.array(R, int); cs = set()
    for k in GRIDK:
        kk, U = op_bloch(P, s, k)
        n = np.round(k / (np.pi / 2)).astype(int); n2 = np.round(kk / (np.pi / 2)).astype(int)
        cs.add(tuple((n2 - R @ n) % 4))
    ACT.append((R, cs))
check("each PSG rotation acts on the 64 L=4 momenta as k -> R k + c_R with ONE constant c_R in pi Z^3 (affine, shift class mod 2pi)",
      all(len(c) == 1 and all(x % 2 == 0 for x in list(c)[0]) for _, c in ACT), f"{len({tuple(list(c)[0]) for _, c in ACT})} distinct shift classes")
ACT = [(R, np.array(list(c)[0]) // 2) for R, c in ACT]        # c_R = pi * s_R, s_R in {0,1}^3
isT = [abs(np.trace(R) - 3) < .5 or (abs(np.trace(R) + 1) < .5 and np.allclose(np.abs(np.diag(R)), 1)) or (abs(np.trace(R)) < .5 and np.allclose(np.diag(R), 0)) for R, _ in ACT]
check("T = 12 rotations (identity, 3 axis C2, 8 C3)", sum(isT) == 12)
# lattices in units of pi/16: membership tests for integer vectors v (k = v pi/16)
def in_a(v): return all(x % 32 == 0 for x in v)
def in_b(v): return in_a(v) or in_a([x - 16 for x in v])
def in_c(v): return all(x % 8 == 0 for x in v)
def in_d(v): return all(x % 16 == 0 for x in v)
LAT = dict(a=(in_a, 32), b=(in_b, 32), c=(in_c, 8), d=(in_d, 16))
def fixed_set(lat, grp):
    test, per = LAT[lat]; out = set()
    for v in itertools.product(range(32), repeat=3):
        v = np.array(v)
        if all(test(list(R @ v + 16 * s - v)) for (R, s), t in zip(ACT, isT) if (t or grp == 'O')):
            out.add(tuple(v % per) if lat != 'b' else min(tuple(v % 32), tuple((v + 16) % 32)))
    return sorted(out)
res = {}
for lat in 'abcd':
    for g in 'TO':
        res[(lat, g)] = fixed_set(lat, g)
    print(f"  ({lat}) T-fixed (k in pi/16 units):", res[(lat, 'T')], " O-fixed:", res[(lat, 'O')])
ks16 = tuple(np.round(kst / (np.pi / 16)).astype(int) % 32); mks16 = tuple(np.round(-kst / (np.pi / 16)).astype(int) % 32)
check("(a) mod 2pi Z^3: T-fixed = O-fixed = {+-k*}", set(res[('a', 'T')]) == {ks16, mks16} and res[('a', 'T')] == res[('a', 'O')])
check("(b) mod 2pi Z^3 + pi(1,1,1): one class {k* ~ -k*}", len(res[('b', 'T')]) == 1 and res[('b', 'T')] == res[('b', 'O')])
check("(c) mod (pi/2)Z^3: T-fixed = {0, (pi/4)(1,1,1)}", set(res[('c', 'T')]) == {(0, 0, 0), (4, 4, 4)} and res[('c', 'T')] == res[('c', 'O')])
check("(d) mod pi Z^3: T-fixed = {0, (pi/2)(1,1,1)}", set(res[('d', 'T')]) == {(0, 0, 0), (8, 8, 8)} and res[('d', 'T')] == res[('d', 'O')])
# little groups (rotation parts) at the uniaxial points
def lg(v, lat):
    test, _ = LAT[lat]; v = np.array(v)
    return [R for (R, s) in ACT if test(list(R @ v + 16 * s - v))]
pts = {('a', 'k*+pi e_x'): np.array(ks16) + np.array([16, 0, 0]), ('a', 'k*+pi(1,1,0)'): np.array(ks16) + np.array([16, 16, 0]),
       ('d', 'X_r=(pi/2)e_x'): [8, 0, 0], ('d', 'M_r=(pi/2)(1,1,0)'): [8, 8, 0], ('c', 'X_r=(pi/4)e_x'): [4, 0, 0], ('c', 'M_r=(pi/4)(1,1,0)'): [4, 4, 0]}
info = {}
for key, v in pts.items():
    G = lg(v, key[0]); axes = [R for R in G if abs(np.trace(R) + 1) < .5]
    hasC4 = any(abs(np.trace(R) - 1) < .5 for R in G); hasC3 = any(abs(np.trace(R)) < .5 for R in G)
    # common invariant axis
    inv = [e for e in np.eye(3) if all(np.allclose(np.abs(R @ e), e) for R in G)]
    info[key] = (len(G), hasC4, hasC3, len(inv))
print("  little groups (order, has C4, has C3, # invariant coordinate axes):", info)
check("cube doublers, X_r, M_r: rotation little groups of order 8 with a C4 and no C3 (D4), one invariant axis (uniaxial allowed)",
      all(v[0] == 8 and v[1] and not v[2] and v[3] >= 1 for v in info.values()))
# verify the translation groups on sample words
rng = np.random.default_rng(4); kk = rng.uniform(-np.pi, np.pi, (4, 3))
noR = ['S', rand_onsite_unitary(rng), 'S2', rand_onsite_unitary(rng), 'Si', rand_onsite_unitary(rng)]
check("(b) words without R_L: W(k + pi(1,1,1)) = W(k)", all(np.allclose(Wword(noR, k + np.pi * np.ones(3)), Wword(noR, k)) for k in kk))
withR = ['S', 'R', rand_onsite_unitary(rng)]
check("(b) control: with R_L, W(k + pi(1,1,1)) != W(k) in spectrum", not np.allclose(np.sort(eigph(Wword(withR, kk[0] + np.pi))), np.sort(eigph(Wword(withR, kk[0])))))
# corner-plane signs Z_i and the S^2 taste
fc = np.array([FACE[c] for c in CORN]); PL = np.array([0 if f[2] == 0 else (1 if f[1] == 0 else 2) for f in fc])
L202 = ULc(2, 0, 2)
Zs = [np.diag(np.where(fc[:, i] != 0, -1.0, 1.0)) for i in range(3)]
# S^2(k + pi/2 e_i) = S^2(k) Z_i ?
okZ = all(np.allclose(Sk(k + np.pi / 2 * np.eye(3)[i], 2), Sk(k, 2) @ Zs[i]) for k in kk for i in range(3))
check("S^2(k + (pi/2) e_i) = S^2(k) Z_i, Z_i = diag(-1 on corners with a component along i)", okZ)
w = ['S2', UHc(2, 0), 'S2', L202]
check("(c) Z_i W(k) Z_i = W(k + (pi/2)e_i) for S2.H20.S2.L202 (exact taste)", all(np.allclose(Zs[i] @ Wword(w, k) @ Zs[i], Wword(w, k + np.pi / 2 * np.eye(3)[i])) for k in kk for i in range(3)))
w2 = ['S', UHc(1, 3), 'S', L202]
check("(d) Z_i W(k) Z_i = W(k + pi e_i) for S.H13.S.L202", all(np.allclose(Zs[i] @ Wword(w2, k) @ Zs[i], Wword(w2, k + np.pi * np.eye(3)[i])) for k in kk for i in range(3)))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
