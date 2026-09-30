"""Test D: mixing patterns fixed entirely by residual symmetries inside the finite groups acting on the hw=1 triplet."""
import itertools, math, numpy as np
from common import BOX61
def perm_matrices():
    return [np.array([[1.0 if j == p[i] else 0.0 for j in range(3)] for i in range(3)]) for p in itertools.permutations(range(3))]
def signed_perm_matrices():
    out = []
    for P in perm_matrices():
        for s in itertools.product((1, -1), repeat=3):
            out.append(np.diag(s) @ P)
    return out
def key(M): return tuple(np.round(M, 6).flatten())
def closure(gens):
    els = {key(np.eye(3)): np.eye(3)}
    frontier = [np.eye(3)]
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = g @ a
                k = key(b)
                if k not in els:
                    els[k] = b; new.append(b)
        frontier = new
    return list(els.values())
def subgroups(G):
    subs = {}
    for r in (1, 2, 3):
        for gens in itertools.combinations(G, r):
            H = closure(list(gens))
            k = frozenset(key(h) for h in H)
            subs[k] = H
    return list(subs.values())
def is_abelian(H): return all(np.allclose(a @ b, b @ a) for a in H for b in H)
rng = np.random.default_rng(1)
def joint_basis(H):
    """orthonormal joint eigenbasis if all joint eigenspaces are 1-dim, else None."""
    c = rng.normal(size=len(H)) + 1j * rng.normal(size=len(H))
    N = sum(ci * h for ci, h in zip(c, H))
    w, V = np.linalg.eig(N)
    if np.min([abs(w[i] - w[j]) for i in range(3) for j in range(i + 1, 3)]) < 1e-6: return None
    # eigenvectors of a normal matrix with distinct eigenvalues are orthogonal
    V = V / np.linalg.norm(V, axis=0)
    if not np.allclose(V.conj().T @ V, np.eye(3), atol=1e-8): return None
    return V
def patterns(G, label):
    subs = [H for H in subgroups(G) if is_abelian(H)]
    bases = []
    for H in subs:
        V = joint_basis(H)
        if V is not None: bases.append(V)
    # distinct bases up to column permutation/phase: use |V|^2 up to permutations of columns as key
    def canon(V):
        a = np.abs(V) ** 2
        cols = sorted(map(tuple, np.round(a.T, 6)))
        return tuple(cols)
    uniq = {}
    for V in bases: uniq.setdefault(canon(V), V)
    B = list(uniq.values())
    pats = {}
    for Ve in B:
        for Vn in B:
            U = Ve.conj().T @ Vn
            a = np.abs(U) ** 2
            # any row = electron, any column arrangement with rows/cols permuted
            for r in range(3):
                row = a[r]
                pats.setdefault(tuple(sorted(np.round(row, 6))), []).append(np.round(a, 4))
    print(f"\n{label}: order {len(G)}, abelian subgroups with nondegenerate joint basis: {len(bases)} (distinct bases {len(B)})")
    print("  distinct electron-row multisets |U_e j|^2 over all pairs (Ve,Vn) and all rows:")
    smallest_nonzero = 9
    for rowset in sorted(pats):
        print("   ", rowset)
        smallest_nonzero = min([smallest_nonzero] + [x for x in rowset if x > 1e-6])
    print(f"  smallest nonzero |U_e j|^2 anywhere: {smallest_nonzero:.6f}  (data needs |U_e3|^2 ~ 0.0222)")
    # closest to data (s13^2 = min entry of the row, s12^2 from ordered remaining), report best
    best = None
    for rowset in pats:
        r = sorted(rowset)          # ascending: candidate (nu3, nu2, nu1)
        s13 = r[0]; s12 = r[1] / (1 - s13)
        d = math.hypot((s13 - 0.02245) / 0.0009, (s12 - 0.309) / 0.0134)
        if best is None or d < best[0]: best = (d, rowset, s12, s13)
    print(f"  pattern closest to (s13^2, s12^2) = (0.0225, 0.309) [proxy centre]: row {best[1]}: s13^2={best[3]:.4f}, s12^2={best[2]:.4f}")
    return smallest_nonzero
s1 = patterns(perm_matrices(), "S3 = <C3, P23> (lane's static generation group)")
s2 = patterns(signed_perm_matrices(), "O_h = signed permutations (adds translation phases diag(+-1)); order 48")
