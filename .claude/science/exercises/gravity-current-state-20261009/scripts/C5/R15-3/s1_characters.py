"""R15-3 s1: character bookkeeping for Theorem C (auxiliary-irrep counting).
Checks: (1) explicit O irreps; (2) eigenvalue multisets of C4 (z), C3 (111), C2' (110) in each irrep;
(3) the stabilizer characters on TT(k) for the three symmetric directions; (4) minimal generalized-kernel
content G (even multiplicities, as required for a symplectic O-rep) under each set of TT-character conditions."""
import itertools, numpy as np
from common import *

G = proper_cubic_group()
irr = irreps(G)
print("irrep checks (homomorphism, <chi,chi>):", check_irreps(G, irr))
idx = lambda R: [i for i, S in enumerate(G) if np.allclose(S, R)][0]
C4 = stabilizer_element(G, [0, 0, 1], 4)
C3 = stabilizer_element(G, [1, 1, 1], 3)
C2p = stabilizer_element(G, [1, 1, 0], 2)
w = np.exp(2j * np.pi / 3)
def label(z):
    for name, v in [("+1", 1), ("-1", -1), ("+i", 1j), ("-i", -1j), ("w", w), ("wbar", w.conjugate())]:
        if abs(z - v) < 1e-9: return name
    return str(np.round(z, 6))
def eigs(M):
    return sorted(label(z) for z in np.linalg.eigvals(M))
print("\nstabilizer eigenvalues in each irrep:")
for name in ["A1", "A2", "E", "T1", "T2"]:
    print(f"  {name}: C4_z {eigs(irr[name][idx(C4)])}  C3_111 {eigs(irr[name][idx(C3)])}  C2'_110 {eigs(irr[name][idx(C2p)])}")

print("\nstabilizer eigenvalues on TT(k), helicity-1 and helicity-0 subspaces of Sym^2:")
for (nm, R, k) in [("C4_z", C4, [0, 0, 1]), ("C3_111", C3, [1, 1, 1]), ("C2'_110", C2p, [1, 1, 0])]:
    PT = tt_projector(k); S = sym2_rep(R)
    # basis of TT
    vals, vecs = np.linalg.eigh(PT); BT = vecs[:, vals > 0.5]
    kk = np.asarray(k, float) / np.linalg.norm(k)
    # helicity-0 subspace: span{delta, k k}; helicity-1: rest
    h0 = []
    for M in [np.eye(3), np.outer(kk, kk)]:
        h0.append(np.array([np.sum(E * M) for E in SYM2]))
    H0 = np.linalg.qr(np.array(h0).T)[0]
    rest = np.eye(6) - BT @ BT.T - H0 @ H0.T
    vals1, vecs1 = np.linalg.eigh(rest); B1 = vecs1[:, vals1 > 0.5]
    print(f"  {nm}: TT {eigs(BT.T @ S @ BT)}  hel-1 {eigs(B1.T @ S @ B1)}  hel-0 {eigs(H0.T @ S @ H0)}")

# multiplicity data per irrep
data = {}
for name in ["A1", "A2", "E", "T1", "T2"]:
    e4 = eigs(irr[name][idx(C4)]); e3 = eigs(irr[name][idx(C3)]); e2 = eigs(irr[name][idx(C2p)])
    data[name] = dict(dim=irr[name][0].shape[0], m4=e4.count("-1"), mw=e3.count("w"), mwb=e3.count("wbar"), m2=e2.count("+1"))
print("\nper-irrep (dim, mult of -1 under C4, w under C3, +1 under C2'):", {k: (v['dim'], v['m4'], v['mw'], v['m2']) for k, v in data.items()})
print("per-irrep check m4 + m2 <= dim:", {k: v['m4'] + v['m2'] <= v['dim'] for k, v in data.items()})

names = ["A1", "A2", "E", "T1", "T2"]
def search(conds, need_res=False, maxmult=8):
    best = None; sols = []
    for n in itertools.product(range(0, maxmult + 1, 2), repeat=5):
        n = dict(zip(names, n))
        dim = sum(n[r] * data[r]['dim'] for r in names)
        if dim == 0: continue
        m4 = sum(n[r] * data[r]['m4'] for r in names)
        mw = sum(n[r] * data[r]['mw'] for r in names)
        m2 = sum(n[r] * data[r]['m2'] for r in names)
        ok = True
        if 'C4' in conds and m4 < 4: ok = False
        if 'C3' in conds and mw < 2: ok = False
        if 'C2p' in conds and m2 < 4: ok = False
        if need_res and (n['E'] == 0 or n['T2'] == 0): ok = False
        if not ok: continue
        if best is None or dim < best:
            best = dim; sols = [n]
        elif dim == best:
            sols.append(n)
    return best, sols
print("\nminimal generalized kernel G at k=0 (even multiplicities; branches = dim/2):")
for conds, res in [(('C4',), False), (('C4', 'C3'), False), (('C4', 'C2p'), False), (('C4', 'C3', 'C2p'), False),
                   (('C4',), True), (('C4', 'C3', 'C2p'), True)]:
    best, sols = search(conds, res)
    fmt = [" + ".join(f"{v}{k}" for k, v in s.items() if v) for s in sols]
    print(f"  TT characters on {conds}{' + nonvanishing h-TT residue on z' if res else ''}: dim G = {best} -> {best//2} gapless branches ({best//2 - 2} partners); minimal G: {fmt}")
