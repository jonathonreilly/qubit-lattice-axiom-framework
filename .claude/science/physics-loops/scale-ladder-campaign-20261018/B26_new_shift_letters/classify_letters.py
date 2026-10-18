#!/usr/bin/env python3
"""B26 part 1: exhaustive classification of PSG-symmetric signed/phased permutation ('shift') letters of the
12 corner modes with displacement range <= 2 (sup norm), in the INDEPENDENT build B7_check/chk_core.py
(own GF(2) gauge, brute-force PSG; imported read-only, not modified).

Class (declared):  X = sum_d |v+d><v| (x) X_d  (translation invariant, 12x12 blocks, |d|_inf <= 2),
  X a phased permutation: exactly one nonzero entry per row and per column, entries in {+-1, +-i};
  G_g X G_g^-1 = chi(g) X for all 24 proper rotations g (gauge-dressed:  G_g|v,c> = (-1)^{lam.v+tau(c)}|Rv,Rc>),
  chi = trivial (symmetric letters)   or chi = A2 (pseudoscalar 'half-letters'; even products are symmetric).
  Also report commutation with the 24 improper (inversion-dressed) PSG elements.
Covariance condition (derived from the action):  X_{Rd}[Rc',Rc] = chi(g) (-1)^{lam.d + tau(c) + tau(c')} X_d[c',c].
Method: for every source/target pair (c0 -> c'@d), c0 fixed (rotations are transitive on corners), |d|<=2:
  group-average the elementary block (with and without the A2 twist) and test whether the result is a nonzero
  phased permutation. Because one row (c0@0) of a phased permutation has exactly one entry, every letter in the
  class is z * (one such average) -- the enumeration is exhaustive.
Spectrum type: eigenvalues of X(k) at random k (constant vs k-dependent)."""
import sys, os, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B7_check'))
t0 = time.time()
from chk_core import *     # noqa  (independent model build)
import numpy as np
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

def chiA2(M):
    """A2 character of O: sign of the axis permutation of the signed-permutation matrix M (proper)."""
    perm = [int(np.nonzero(M[i])[0][0]) for i in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j]); return (-1) ** inv
RNG2 = [d for d in itertools.product(range(-2, 3), repeat=3)]
def act(g, X):
    """g . X for block dict X (d -> 12x12)."""
    M = OH[g]; lam = LAM[g]; tau = TAU[g]; Y = {}
    for d, B in X.items():
        Rd = rdir(M, d); s = (-1.0) ** int(lam @ np.array(d) % 2)
        Bn = np.zeros((12, 12), complex)
        for (i, j) in zip(*np.nonzero(np.abs(B) > 1e-12)):
            ci, cj = CORN[i], CORN[j]
            Bn[CI[rcorn(M, ci)], CI[rcorn(M, cj)]] += s * (-1.0) ** (int(tau[i]) + int(tau[j])) * B[i, j]
        Y[Rd] = Y.get(Rd, 0) + Bn
    return Y
def addd(X, Y, w=1.0):
    Z = {d: B.copy() for d, B in X.items()}
    for d, B in Y.items(): Z[d] = Z.get(d, 0) + w * B
    return {d: B for d, B in Z.items() if np.abs(B).max() > 1e-12}
def avg(E, gs, twist):
    X = {}
    for g in gs: X = addd(X, act(g, E), (chiA2(OH[g]) if twist else 1.0))
    return X
def is_phased_perm(X):
    if not X: return False
    tot = np.zeros((12, 12)); cnt_r = np.zeros(12); cnt_c = np.zeros(12)
    for d, B in X.items():
        nz = np.abs(B) > 1e-9; cnt_r += nz.sum(1); cnt_c += nz.sum(0)
    return bool((cnt_r == 1).all() and (cnt_c == 1).all())
def normalise(X):
    m = max(np.abs(B).max() for B in X.values()); return {d: B / m for d, B in X.items()}
def bloch(X, k): return sum(B * np.exp(-1j * np.dot(k, d)) for d, B in X.items())
def covariant(X, g, chi):
    Y = act(g, X); keys = set(X) | set(Y)
    return all(np.allclose(Y.get(d, 0), chi * X.get(d, 0)) for d in keys)

# --- sanity: the model Hamiltonian satisfies the covariance condition (validates the derived action formula)
h = {}
for (i1, i2, s) in ELIST:
    sg = -(-1.0) ** int(u[ETYPES[(i1, i2, s)]])
    h.setdefault(tuple(s), np.zeros((12, 12), complex))[i2, i1] += sg
    h.setdefault(neg(tuple(s)), np.zeros((12, 12), complex))[i1, i2] += sg
check("model H (all 36 edge types, own gauge) is invariant under all 48 dressed O_h elements (validates action formula)",
      all(covariant(h, g, 1.0) for g in ALL))
check("PSG gauge solve consistent with all flux constraints", FLUX_OK)

c0 = CORN[0]; i0 = CI[c0]
print("source corner c0 =", sorted(c0), flush=True)
letters = []
for twist in (False, True):
    for d in RNG2:
        for j in range(12):
            E = {d: np.zeros((12, 12), complex)}; E[d][j, i0] = 1.0
            X = avg(E, PROPER, twist)
            if not X: continue
            X = normalise(X)
            if is_phased_perm(X): letters.append((twist, d, CORN[j], X))
print(f"enumerated {2 * len(RNG2) * 12} (twist, target) pairs; phased-permutation letters found: {len(letters)}", flush=True)

rng = np.random.default_rng(3)
KS = rng.uniform(-np.pi, np.pi, size=(6, 3))
ks_ = np.array([1, -1, 1]) * np.pi / 2
rows = []
f0 = np.array([sum(np.array(x) for x in c0)])[0]
for twist, d, cj, X in letters:
    # symmetry under all proper rotations with character
    cov = all(covariant(X, g, chiA2(OH[g]) if twist else 1.0) for g in PROPER)
    inv_sym = all(covariant(X, g, 1.0) for g in ALL[24:]); inv_anti = all(covariant(X, g, -1.0) for g in ALL[24:])
    inv_A2 = all(covariant(X, g, chiA2(OH[g] @ -np.eye(3, dtype=int))) for g in ALL[24:])
    specs = [np.sort(np.angle(np.linalg.eigvals(bloch(X, k)))) for k in KS]
    const = all(np.allclose(s_, specs[0], atol=1e-9) for s_ in specs)
    U = all(np.allclose(bloch(X, k) @ bloch(X, k).conj().T, np.eye(12)) for k in KS)
    sq = bloch(X, KS[0]) @ bloch(X, KS[0])
    a_par = None
    dv = np.array(d)
    # displacement in units of the face diagonal f_c0
    a_par = float(dv @ f0 / 2) if np.allclose(dv, (dv @ f0 / 2) * f0) else None
    kind = 'same corner' if cj == c0 else ('antipodal corner' if cj == frozenset(neg(x) for x in c0) else 'other corner')
    rows.append((twist, d, kind, a_par, cov, inv_sym, inv_anti, inv_A2, const, U, specs[0]))
    print(f"  {'A2 ' if twist else 'sym'} target {sorted(cj)}@{d}: {kind}, d = {a_par} f_c; covariant={cov}; "
          f"O_h-inv: comm={inv_sym} anti={inv_anti} A2xinv={inv_A2}; unitary={U}; spectrum {'CONSTANT' if const else 'k-dependent'} "
          f"{np.round(specs[0] / np.pi, 4) if const else ''}; X(k)^2 ~ {'scalar' if np.allclose(sq, sq[0,0]*np.eye(12)) else 'non-scalar'}", flush=True)

sym = [r for r in rows if not r[0]]; ps = [r for r in rows if r[0]]
check("every found letter is unitary and covariant under all 24 dressed rotations", all(r[4] and r[9] for r in rows))
check("every letter's displacement is a multiple a*f_c of the corner's face diagonal, target corner = c or -c (C2' stabiliser argument)",
      all(r[3] is not None and r[2] in ('same corner', 'antipodal corner') for r in rows))
geo = sorted(set((r[2], r[3]) for r in rows))
print("geometric types found:", geo)
print("symmetric letters (chi trivial):", sorted((r[2], r[3]) for r in sym))
print("pseudoscalar A2 letters:", sorted((r[2], r[3]) for r in ps))
check("each of the 10 C2'-fixed targets {c,-c} x a in {-2..2} gives exactly one letter (either chi=1 or chi=A2, never both, never neither)",
      len(rows) == 10 and len(set((r[2], r[3]) for r in rows)) == 10)
check("same-corner letters are exactly the symmetric S^a, a=-2..2 (a=0 identity); k-dependent iff a != 0",
      sorted(r[3] for r in sym if r[2] == 'same corner') == [-2, -1, 0, 1, 2] and all((not r[8]) == (r[3] != 0) for r in sym if r[2] == 'same corner'))
check("antipodal letters A_a (c@v -> -c@v + a f_c) all have a CONSTANT Bloch spectrum (2x2 blocks c<->-c)",
      all(r[8] for r in rows if r[2] == 'antipodal corner'))

# --- algebra of the classified letters in this independent build (block-dict products on the infinite lattice)
def mul(X, Y):
    Z = {}
    for d1, B1 in X.items():
        for d2, B2 in Y.items():
            d = tuple(a + b for a, b in zip(d1, d2)); Z[d] = Z.get(d, 0) + B1 @ B2
    return {d: B for d, B in Z.items() if np.abs(B).max() > 1e-12}
def eq(X, Y, z=1.0):
    keys = set(X) | set(Y); return all(np.allclose(X.get(d, 0), z * Y.get(d, 0)) for d in keys)
def inv(X): return {neg(d): B.conj().T for d, B in X.items()}
Lt = {(r[2], r[3]): X for r, (tw, d, cj, X) in zip(rows, letters)}
S1, A0c = Lt[('same corner', 1.0)], Lt[('antipodal corner', 0.0)]
def Spow(a):
    X = {(0, 0, 0): np.eye(12, dtype=complex)}
    for _ in range(abs(a)): X = mul(X, S1 if a > 0 else inv(S1))
    return X
hl = {d: B for d, B in h.items() if d != (0, 0, 0)}; RL = {d: -B / np.sqrt(2) for d, B in hl.items()}
check("independent R_L := H_link/sqrt2 is an involution (R_L^2 = 1)", eq(mul(RL, RL), {(0, 0, 0): np.eye(12)}))
check("A0^2 = -1", eq(mul(A0c, A0c), {(0, 0, 0): np.eye(12)}, -1.0))
check("A_a = z_a A0 S^a (|z_a| = 1) for a = -2..2", all(any(eq(Lt[("antipodal corner", float(a))], mul(A0c, Spow(a)), z) for z in (1, -1, 1j, -1j)) for a in (-2, -1, 0, 1, 2)))
check("S^2 letter = S1*S1 and S^-1 letter = S1^-1 (up to sign)", any(eq(Lt[('same corner', 2.0)], mul(S1, S1), z) for z in (1, -1)) and any(eq(Lt[('same corner', -1.0)], inv(S1), z) for z in (1, -1)))
check("A0 S A0^-1 = S^-1", eq(mul(A0c, mul(S1, inv(A0c))), inv(S1)))
check("A0 R_L A0^-1 = -S R_L S^-1  (so the A2 half-letters generate no new symmetric letter)", eq(mul(A0c, mul(RL, inv(A0c))), mul(S1, mul(RL, inv(S1))), -1.0))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
