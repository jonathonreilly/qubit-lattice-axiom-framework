"""A38 t1: (a) which period-2 textures are kept by all 24 glued turns up to a translation (strict
state-level condition)?  Exhaustive over bijections cell -> 8 body diagonals (the orbit argument says the
values must be body diagonals, one each), plus a random-texture control.
(b) calm pair laws (J,K,D) for each survivor; (c) covariant star-local terms (NNN pairs inside a star,
three-spin star terms) that keep it calm."""
import os, sys, signal, itertools, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from lib38 import *

t0 = time.time()
cellidx = {c: i for i, c in enumerate(CELL)}


def act(R, tex):
    """(g.m)(r) = R m(R^{-1} r), rotation about the origin site"""
    out = {}
    for r in CELL:
        rp = tuple(int(v) % 2 for v in R.T @ np.array(r))
        out[r] = R @ tex[rp]
    return out


def translate(tex, t):
    return {r: tex[tuple((r[i] + t[i]) % 2 for i in range(3))] for r in CELL}


def same(a, b, tol=1e-9):
    return all(np.linalg.norm(a[r] - b[r]) < tol for r in CELL)


def strict_ok(tex):
    for R in TURNS:
        g = act(R, tex)
        if not any(same(g, translate(tex, t)) for t in CELL):
            return False
    return True


octs = [np.array(s, float) / np.sqrt(3) for s in itertools.product((1, -1), repeat=3)]
octi = {tuple(np.round(o * np.sqrt(3)).astype(int)): i for i, o in enumerate(octs)}
# integer tables: site permutation r -> R^T r mod 2, octant permutation o -> R o, translations
sp = [[cellidx[tuple(int(v) % 2 for v in R.T @ np.array(r))] for r in CELL] for R in TURNS]
op = [[octi[tuple(int(v) for v in R @ np.round(o * np.sqrt(3)).astype(int))] for o in octs] for R in TURNS]
tr = [[cellidx[tuple((r[i] + t[i]) % 2 for i in range(3))] for r in CELL] for t in CELL]
good = []
for perm in itertools.permutations(range(8)):
    transl = set(tuple(perm[tr[t][r]] for r in range(8)) for t in range(8))
    ok = True
    for g in range(24):
        img = tuple(op[g][perm[sp[g][r]]] for r in range(8))
        if img not in transl:
            ok = False; break
    if ok:
        good.append(perm)
print(f"(a) bijections cell -> 8 body diagonals kept by all 24 turns up to translation: {len(good)} of 40320")
H8 = {r: np.array([(-1) ** r[0], (-1) ** r[1], (-1) ** r[2]], float) / np.sqrt(3) for r in CELL}
h8set = []
for t in CELL:
    T = translate(H8, t)
    h8set.append(tuple(int(np.argmin([np.linalg.norm(T[r] - o) for o in octs])) for r in CELL))
print("    they are exactly the 8 translates of H8 (m^a(r) = (-1)^{r_a}/sqrt3):", sorted(good) == sorted(h8set))
# controls: random textures, uniform textures, Neel along (111), Klein 4-sublattice texture
rng = np.random.default_rng(1)
ctrl = {"uniform (1,1,1)": {r: np.ones(3) / np.sqrt(3) for r in CELL},
        "Neel along (1,1,1)": {r: (-1) ** sum(r) * np.ones(3) / np.sqrt(3) for r in CELL},
        "random": {r: (lambda v: v / np.linalg.norm(v))(rng.normal(size=3)) for r in CELL}}
for n, t in ctrl.items():
    print(f"    control {n:20s}: strict condition holds? {strict_ok(t)}")
# site stabiliser of H8 at the origin: turns with t = 0
stab = [R for R in TURNS if same(act(R, H8), H8)]
print(f"    exact site stabiliser of H8 about a site: order {len(stab)} (C3 about the local body diagonal)")
# do the face-diagonal half-turns fix any site of H8 exactly? (needed by the A33 parity formula)
fd = [R for R in TURNS if round(np.trace(R)) == -1 and np.sum(np.abs(np.diag(R))) == 1]
fdfix = 0
for R in fd:
    for c in CELL:
        # rotation about site c: r -> R(r - c) + c
        out = {}
        for r in CELL:
            rp = tuple(int(v) % 2 for v in (R.T @ (np.array(r) - np.array(c)) + np.array(c)))
            out[r] = R @ H8[rp]
        if same(out, H8):
            fdfix += 1
print(f"    face-diagonal half-turns that keep H8 exactly about some site: {fdfix} of {len(fd)}x8")

# (b) calm pair laws
basisP = [pair_law(1, 0, 0), pair_law(0, 1, 0), pair_law(0, 0, 1)]
M, keys = calm_matrix(H8, basisP)
N, S = null_space(M)
print(f"(b) H8 under J s.s + K s^a s^a + D DM: singular values {np.round(S, 6).tolist()}; calm laws (J,K,D) ="
      f" {np.round(N.T / N.T[:, :1], 9).tolist() if N.size else 'none'}")
for n, t in ctrl.items():
    if n == "random":
        continue
    M2, _ = calm_matrix(t, basisP)
    N2, S2 = null_space(M2)
    print(f"    control {n:20s}: calm (J,K,D) null space = {np.round(N2.T, 6).tolist()}")
# Klein-dual check: U = prod_r C2 about axis a(r); H8 <-> Neel(111)
Ok = {r: np.diag([(-1) ** (r[1] + r[2]), (-1) ** (r[0] + r[2]), (-1) ** (r[0] + r[1])]) for r in CELL}
neel = {r: Ok[r] @ H8[r] for r in CELL}
print("    Klein four-sublattice rotation maps H8 to a Neel state along a body diagonal:",
      all(np.allclose(neel[r], (-1) ** sum(r) * neel[(0, 0, 0)]) for r in CELL), "; neel(0) =", np.round(neel[(0, 0, 0)] * np.sqrt(3), 6))

# (c) covariant star-local terms
shapes = {"NN pair": [(0, 0, 0), (1, 0, 0)],
          "NNN pair (face diagonal, inside a star)": [(1, 0, 0), (0, 1, 0)],
          "pair at distance 2 (inside a star)": [(-1, 0, 0), (1, 0, 0)],
          "3-spin L (x, x+a, x+b)": [(0, 0, 0), (1, 0, 0), (0, 1, 0)],
          "3-spin straight (x-a, x, x+a)": [(-1, 0, 0), (0, 0, 0), (1, 0, 0)],
          "3-spin octant (x+a, x+b, x+c)": [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
          "3-spin (x-a, x+b, x+a)": [(-1, 0, 0), (0, 1, 0), (1, 0, 0)]}
allb, names = [], []
for nm, sh in shapes.items():
    b = covariant_basis(sh)
    print(f"(c) {nm:42s}: {len(b)} independent glued covariant terms")
    allb += b; names += [nm] * len(b)
M3, keys3 = calm_matrix(H8, allb)
N3, S3 = null_space(M3, tol=1e-9)
print(f"    H8 with all {len(allb)} star-local terms: calm subspace dimension {N3.shape[1]}; flip patterns {len(keys3)}")
# which classes enter the calm subspace
for j in range(N3.shape[1]):
    v = N3[:, j]
    used = sorted(set(names[i] for i in range(len(v)) if abs(v[i]) > 1e-8))
    print(f"    calm direction {j}: uses {used}")
np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "t1_calm_star_basis.npy"), N3)
# T (chiral octant term, A34 C56): does it keep H8 calm on its own?
T = {}
for s in itertools.product((1, -1), repeat=3):
    C = np.zeros((3, 3, 3))
    for a, b, c in itertools.permutations(range(3)):
        C[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])
    add_term(T, [(s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])], s[0] * s[1] * s[2] * C)
aT = flip_amplitudes(H8, T)
print(f"    A34's chiral term T alone on H8: largest flip amplitude {max(abs(v) for v in aT.values()):.4f}"
      f" (patterns of size {sorted(set(len(k) for k, v in aT.items() if abs(v) > 1e-12))})")
print(f"time {time.time() - t0:.1f} s")
