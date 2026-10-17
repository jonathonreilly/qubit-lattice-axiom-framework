#!/usr/bin/env python3
"""Independent group-theory checks for the C8 note (statements 1-4 + the nondegeneracy argument).

Everything is computed from explicit matrices:
  * 2O is generated as a set of 2x2 SU(2) matrices from lifts of C4z and C3(111) and closed under
    multiplication (no quaternion table is typed in).
  * Subgroups are identified through their SO(3) images (adjoint action).
  * 1-dimensional representations are found by brute force (all assignments of roots of unity to a
    generating set, extended and checked against the full multiplication table), not from theory.
  * Characters of 2O come from SU(2) spin-j restrictions; orthonormality and completeness are checked.
Run: python3 check_grouptheory.py
"""
import itertools
import numpy as np
np.set_printoptions(legacy="1.25")

TOL = 1e-9
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SX, SY, SZ]


def su2(axis, angle):
    n = np.array(axis, dtype=float)
    n = n / np.linalg.norm(n)
    return np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * (n[0] * SX + n[1] * SY + n[2] * SZ)


def key(M):
    return tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 7) + 0.0)


def so3(U):
    return np.array([[0.5 * np.trace(PAULI[a] @ U @ PAULI[b] @ U.conj().T).real for b in range(3)]
                     for a in range(3)])


def rkey(R):
    return tuple(np.round(R.ravel(), 7) + 0.0)


class Group:
    """Finite group given by elements and a multiplication table."""

    def __init__(self, elems, mul, ident, labels=None):
        self.elems = elems
        self.n = len(elems)
        self.mul = mul  # mul[i][j] = index of e_i e_j
        self.e = ident
        self.inv = [next(j for j in range(self.n) if mul[i][j] == ident) for i in range(self.n)]

    def order(self, i):
        k, x = 1, i
        while x != self.e:
            x = self.mul[x][i]
            k += 1
        return k

    def generated(self, gens):
        S = {self.e}
        frontier = [self.e]
        while frontier:
            new = []
            for x in frontier:
                for g in gens:
                    y = self.mul[x][g]
                    if y not in S:
                        S.add(y)
                        new.append(y)
            frontier = new
        return S

    def commutator_subgroup(self, sub=None):
        sub = list(range(self.n)) if sub is None else list(sub)
        comms = {self.mul[self.mul[self.inv[a]][self.inv[b]]][self.mul[a][b]] for a in sub for b in sub}
        return self.generated(list(comms))

    def classes(self, sub=None):
        sub = list(range(self.n)) if sub is None else sorted(sub)
        seen, out = set(), []
        for x in sub:
            if x in seen:
                continue
            c = {self.mul[self.mul[g][x]][self.inv[g]] for g in sub}
            seen |= c
            out.append(sorted(c))
        return out


def matrix_group(gens):
    elems = [I2]
    idx = {key(I2): 0}
    frontier = [I2]
    while frontier:
        new = []
        for X in frontier:
            for G in gens:
                Y = X @ G
                k = key(Y)
                if k not in idx:
                    idx[k] = len(elems)
                    elems.append(Y)
                    new.append(Y)
        frontier = new
    mul = [[idx[key(A @ B)] for B in elems] for A in elems]
    return Group(elems, mul, 0), idx


def one_dim_reps(G, sub, N):
    """All homomorphisms sub -> mu_N (N-th roots of unity), by brute force on a generating set.
    Returns list of dicts element->complex."""
    sub = sorted(sub)
    # pick a small generating set greedily
    gens, span = [], {G.e}
    for x in sub:
        if x not in span:
            gens.append(x)
            span = G.generated(gens)
    roots = [np.exp(2j * np.pi * k / N) for k in range(N)]
    reps = []
    for imgs in itertools.product(range(N), repeat=len(gens)):
        val = {G.e: 0}
        frontier = [G.e]
        ok = True
        while frontier and ok:
            new = []
            for x in frontier:
                for g, kg in zip(gens, imgs):
                    y = G.mul[x][g]
                    v = (val[x] + kg) % N
                    if y in val:
                        if val[y] != v:
                            ok = False
                            break
                    else:
                        val[y] = v
                        new.append(y)
                if not ok:
                    break
            frontier = new
        if ok:
            # full check of the homomorphism property
            ok = all(val[G.mul[a][b]] == (val[a] + val[b]) % N for a in sub for b in sub)
        if ok:
            reps.append({x: roots[val[x]] for x in sub})
    return reps


out_lines = []


def out(s=""):
    print(s)
    out_lines.append(s)


def verdict(name, cond):
    out(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    return cond


# ---------------------------------------------------------------- build 2O
gC4 = su2([0, 0, 1], np.pi / 2)
gC3 = su2([1, 1, 1], 2 * np.pi / 3)
G, idx = matrix_group([gC4, gC3])
E = G.e
M1 = idx[key(-I2)]
out("=== Construction ===")
verdict("2O generated by SU(2) lifts of C4z and C3(111) has 48 elements", G.n == 48)
verdict("all 48 matrices are in SU(2)",
        all(np.allclose(U @ U.conj().T, I2) and abs(np.linalg.det(U) - 1) < TOL for U in G.elems))
R_of = [so3(U) for U in G.elems]
img = {}
for i, R in enumerate(R_of):
    img.setdefault(rkey(R), []).append(i)
verdict("SO(3) image has 24 rotations, each with exactly 2 lifts (+-U)",
        len(img) == 24 and all(len(v) == 2 for v in img.values()))
verdict("every SO(3) image is a signed permutation matrix (rotation group O of the cube)",
        all(np.allclose(np.abs(R).sum(0), 1) and np.allclose(np.round(R), R) for R in R_of))


def lifts_of_rotation(axis, angle):
    R = so3(su2(axis, angle))
    return img[rkey(R)]


def preimage(rot_list):
    S = set()
    for ax, ang in rot_list:
        S |= set(lifts_of_rotation(ax, ang))
    return S


def check_is_subgroup(S):
    return all(G.mul[a][b] in S for a in S for b in S)


# ---------------------------------------------------------------- (1)
out("\n=== Statement (1): -1 in commutator subgroups ===")
C2 = G.commutator_subgroup()
out(f"  |[2O,2O]| = {len(C2)}; -1 in it: {M1 in C2}")
verdict("[2O,2O] = 2T (order 24) and contains -1", len(C2) == 24 and M1 in C2)
r2O = one_dim_reps(G, range(48), 8)
out(f"  1-dim reps of 2O (brute force over 8th roots of unity): {len(r2O)}; values on -1: "
    f"{sorted(set(np.round(r[M1].real, 6) for r in r2O))}")
verdict("2O has exactly 2 one-dim reps, both send -1 -> +1", len(r2O) == 2 and all(abs(r[M1] - 1) < TOL for r in r2O))

for name, rots in [
    ("D2 = {E, C2x, C2y, C2z}", [([1, 0, 0], 0), ([1, 0, 0], np.pi), ([0, 1, 0], np.pi), ([0, 0, 1], np.pi)]),
    ("D2' = {E, C2z, C2(110), C2(1-10)}", [([1, 0, 0], 0), ([0, 0, 1], np.pi), ([1, 1, 0], np.pi), ([1, -1, 0], np.pi)]),
]:
    S = preimage(rots)
    sq = []
    for ax, ang in rots[1:]:
        for l in lifts_of_rotation(ax, ang):
            sq.append(G.mul[l][l] == M1)
    comm = G.commutator_subgroup(S)
    orders = sorted(G.order(x) for x in S)
    r = one_dim_reps(G, S, 4)
    out(f"  {name}: preimage order {len(S)}, subgroup {check_is_subgroup(S)}, element orders {orders}")
    out(f"     all six C2 lifts square to -1: {all(sq)}; commutator subgroup = "
        f"{sorted(np.round(np.trace(G.elems[c]).real, 6) for c in comm)} (traces), -1 in it: {M1 in comm}")
    out(f"     1-dim reps: {len(r)}, values on -1: {sorted(set(np.round(x[M1].real, 6) for x in r))}")
    verdict(f"{name}: preimage is Q8 (1 elt order 1, 1 order 2, 6 order 4) and [Q8,Q8] = {{+-1}} contains -1",
            orders == [1, 2] + [4] * 6 and M1 in comm and len(comm) == 2)
    verdict(f"{name}: no 1-dim rep sends -1 -> -1", all(abs(x[M1] - 1) < TOL for x in r))

# lifts of perpendicular pi rotations anticommute (structural reason)
a, b = su2([0, 0, 1], np.pi), su2([1, 1, 0], np.pi)
verdict("lifts of C2z and C2(110) anticommute (=> commutator is -1)", np.allclose(a @ b, -b @ a))

# the other nontrivial-in-U(1) extension class of O: w2 + beta(sgn) (GL(2,3)-type), as {i^{s(g)} g}
T2 = C2  # 2T
gl23 = [(1j if i not in T2 else 1) * G.elems[i] for i in range(48)]
H23, _ = matrix_group([gl23[i] for i in range(48)])
odd_c2_sq = [np.allclose((1j * G.elems[l]) @ (1j * G.elems[l]), I2) for l in lifts_of_rotation([1, 1, 0], np.pi)]
m1 = [i for i, U in enumerate(H23.elems) if np.allclose(U, -I2)][0]
verdict("w2+beta(sgn) extension (GL(2,3)-type, order 48): edge-C2 lifts square to +1, -1 still in commutator",
        H23.n == 48 and all(odd_c2_sq) and m1 in H23.commutator_subgroup())

# ---------------------------------------------------------------- (2)
out("\n=== Statement (2): central Z2 extensions of Z2 x Z2 ===")
K = [(0, 0), (1, 0), (0, 1), (1, 1)]
kadd = lambda g, h: ((g[0] + h[0]) % 2, (g[1] + h[1]) % 2)
pairs = [(g, h) for g in K[1:] for h in K[1:]]
cocycles = []
for vals in itertools.product([0, 1], repeat=len(pairs)):
    w = {(g, h): 0 for g in K for h in K}
    w.update(dict(zip(pairs, vals)))
    if all((w[(g, h)] + w[(kadd(g, h), k)] - w[(h, k)] - w[(g, kadd(h, k))]) % 2 == 0
           for g in K for h in K for k in K):
        cocycles.append(w)
out(f"  normalized Z2-valued 2-cocycles on Z2xZ2: {len(cocycles)}")
all_ok = True
seen_types = {}
for w in cocycles:
    els = [(g, s) for g in K for s in (0, 1)]
    eidx = {x: i for i, x in enumerate(els)}
    mul = [[eidx[(kadd(x[0], y[0]), (x[1] + y[1] + w[(x[0], y[0])]) % 2)] for y in els] for x in els]
    Ext = Group(els, mul, eidx[((0, 0), 0)])
    z = eidx[((0, 0), 1)]
    # squares of both lifts of each involution
    n_sq = 0
    for g in K[1:]:
        sqs = {Ext.mul[eidx[(g, s)]][eidx[(g, s)]] for s in (0, 1)}
        assert len(sqs) == 1  # both lifts square to the same element
        n_sq += (sqs.pop() == z)
    reps = one_dim_reps(Ext, range(8), 4)
    exists = any(abs(r[z] + 1) < TOL for r in reps)
    abelian = all(Ext.mul[a][b] == Ext.mul[b][a] for a in range(8) for b in range(8))
    ords = tuple(sorted(Ext.order(x) for x in range(8)))
    typ = {(1, 2, 2, 2, 2, 2, 2, 2): "Z2^3", (1, 2, 2, 2, 4, 4, 4, 4): "Z4xZ2" if abelian else "?",
           (1, 2, 2, 2, 2, 2, 4, 4): "D4", (1, 2, 4, 4, 4, 4, 4, 4): "Q8"}[ords]
    seen_types.setdefault((n_sq, typ, abelian, exists), 0)
    seen_types[(n_sq, typ, abelian, exists)] += 1
    all_ok &= (exists == (n_sq % 2 == 0))
for (n_sq, typ, ab, ex), c in sorted(seen_types.items()):
    out(f"  #involutions with lift^2 = z: {n_sq} -> extension {typ:6s} abelian={ab!s:5s} "
        f"1-dim rep with z->-1: {ex!s:5s} ({c} cocycles)")
verdict("1-dim rep with z -> -1 exists  <=>  number of 'odd-square' involutions is even (0 or 2), all 16 cocycles",
        all_ok)
out("  (asserted in the loop: both lifts of an involution have the same square, so the count is well defined)")

# ---------------------------------------------------------------- (3)
out("\n=== Statement (3): binary dihedral group of order 12 over D3 = <C3(111), edge C2> ===")
d3_rots = [([1, 0, 0], 0), ([1, 1, 1], 2 * np.pi / 3), ([1, 1, 1], 4 * np.pi / 3),
           ([1, -1, 0], np.pi), ([0, 1, -1], np.pi), ([-1, 0, 1], np.pi)]
H = preimage(d3_rots)
verdict("preimage of D3 has order 12 and is a subgroup", len(H) == 12 and check_is_subgroup(H))
Hn = sorted(H)
abelian_H = all(G.mul[a][b] == G.mul[b][a] for a in Hn for b in Hn)
c3_lifts = lifts_of_rotation([1, 1, 1], 2 * np.pi / 3) + lifts_of_rotation([1, 1, 1], 4 * np.pi / 3)
c3_order6 = [x for x in c3_lifts if G.order(x) == 6]
c2_lifts = {ax: lifts_of_rotation(ax, np.pi) for ax in ((1, -1, 0), (0, 1, -1), (-1, 0, 1))}
verdict("nonabelian; order-6 C3 lifts cube to -1; all C2 lifts have order 4 (square to -1)",
        (not abelian_H) and all(G.mul[G.mul[x][x]][x] == M1 for x in c3_order6)
        and all(G.mul[l][l] == M1 for v in c2_lifts.values() for l in v))
rH = one_dim_reps(G, H, 12)
out(f"  1-dim reps of the order-12 group: {len(rH)}")
spin_chars = [r for r in rH if abs(r[M1] + 1) < TOL]
for k, r in enumerate(rH):
    c2v = {ax: [np.round(r[l], 6) for l in ls] for ax, ls in c2_lifts.items()}
    c3v = sorted(set(np.round(r[x], 6) for x in c3_order6))
    c3v3 = sorted(set(np.round(r[x], 6) for x in c3_lifts if G.order(x) == 3))
    out(f"   rep {k}: -1 -> {np.round(r[M1], 6)}; C2 lifts (+-U per axis) -> {c2v}; "
        f"order-6 C3 lifts -> {c3v}; order-3 C3 lifts -> {c3v3}")
verdict("exactly 2 characters with -1 -> -1 (complex conjugates)",
        len(spin_chars) == 2 and all(abs(spin_chars[0][x] - np.conj(spin_chars[1][x])) < TOL for x in H))
verdict("in them every C2 lift -> +-i and every order-6 C3 lift -> -1 (order-3 C3 lift -> +1)",
        all(abs(abs(r[l]) - 1) < TOL and abs(r[l].real) < TOL for r in spin_chars for v in c2_lifts.values() for l in v)
        and all(abs(r[x] + 1) < TOL for r in spin_chars for x in c3_order6))
# sign bookkeeping: fixed lift convention U = -i n.sigma (n unit) for the three C2 axes
for k, r in enumerate(spin_chars):
    vals = []
    for ax in c2_lifts:
        n = np.array(ax) / np.sqrt(2)
        vals.append(np.round(r[idx[key(-1j * (n[0] * SX + n[1] * SY + n[2] * SZ))]], 6))
    out(f"   spinorial char {k}: lifts -i n.sigma, n = (1,-1,0),(0,1,-1),(-1,0,1) (normalized) -> {vals}")

# ---------------------------------------------------------------- characters of 2O
out("\n=== Character table of 2O (from SU(2) spin-j restrictions) ===")
cls = G.classes()
csize = np.array([len(c) for c in cls])
rep_el = [c[0] for c in cls]


def spin_char(j2, U):  # j2 = 2j
    lam = np.linalg.eigvals(U)[0]
    return sum(lam ** (j2 - 2 * k) for k in range(j2 + 1))


def cf(f):  # class function vector from per-element function
    return np.array([f(G.elems[c]) for c in rep_el])


def inner(a, b):
    return np.sum(csize * a * np.conj(b)) / 48


sgn = np.array([1.0 if c[0] in T2 else -1.0 for c in cls])
chi = {}
chi["A1"] = np.ones(len(cls))
chi["A2"] = sgn
chi["T1"] = cf(lambda U: spin_char(2, U))
chi["T2"] = chi["T1"] * sgn
chi["E"] = cf(lambda U: spin_char(4, U)) - chi["T2"]
chi["E1/2"] = cf(lambda U: spin_char(1, U))
chi["E5/2"] = chi["E1/2"] * sgn
chi["G3/2"] = cf(lambda U: spin_char(3, U))
names = list(chi)
gram = np.array([[inner(chi[a], chi[b]) for b in names] for a in names])
verdict(f"8 classes; the 8 class functions are orthonormal (Gram = identity); sum dim^2 = "
        f"{int(sum(chi[n][0].real ** 2 for n in names))}",
        len(cls) == 8 and np.allclose(gram, np.eye(8)) and abs(sum(chi[n][0].real ** 2 for n in names) - 48) < TOL)
out("  class reps (trace, order, size): " + ", ".join(
    f"({np.trace(G.elems[c]).real:+.3f},{G.order(c)},{len(cls[k])})" for k, c in enumerate(rep_el)))
for n in names:
    out(f"  {n:5s}: " + " ".join(f"{v.real:+.3f}" if abs(v.imag) < TOL else f"{v:.3f}" for v in chi[n]))
verdict("G3/2 = restriction of SU(2) spin 3/2 is irreducible, 4-dim, -1 -> -1",
        abs(inner(chi["G3/2"], chi["G3/2"]) - 1) < TOL and abs(chi["G3/2"][0] - 4) < TOL
        and abs(chi["G3/2"][[k for k, c in enumerate(cls) if M1 in c][0]] + 4) < TOL)


def induce(sub, f):
    """Frobenius formula: Ind f (g) = (1/|H|) sum_{s in G} f(s g s^-1) [f = 0 off H]."""
    vals = []
    for c in rep_el:
        tot = 0
        for s in range(48):
            y = G.mul[G.mul[s][c]][G.inv[s]]
            if y in sub:
                tot += f[y]
        vals.append(tot / len(sub))
    return np.array(vals)


def decompose(v):
    return {n: int(round(inner(v, chi[n]).real)) for n in names if abs(inner(v, chi[n])) > 1e-6}


# ---------------------------------------------------------------- (4)
out("\n=== Statement (4): induction from the order-12 binary dihedral subgroup ===")
for k, r in enumerate(rH):
    ind = induce(H, r)
    out(f"  rep {k} (-1 -> {np.round(r[M1].real, 3)}, a C2 lift -> {np.round(r[c2_lifts[(1, -1, 0)][0]], 3)}): "
        f"dim {ind[0].real:.0f}, Ind = {decompose(ind)}")
for k, r in enumerate(spin_chars):
    ind = induce(H, r)
    verdict(f"spinorial character #{k} (C2 lift {np.round(r[c2_lifts[(1, -1, 0)][0]], 3)}): Ind is 4-dim and = G3/2",
            abs(ind[0] - 4) < TOL and decompose(ind) == {"G3/2": 1})
# Frobenius cross check: restriction of G3/2 to H
Hcls = G.classes(H)
resG = {x: spin_char(3, G.elems[x]) for x in H}
mult = [sum(resG[x] * np.conj(r[x]) for x in H) / 12 for r in spin_chars]
verdict(f"Frobenius cross-check: <Res G3/2, chi> = {[round(m.real, 6) for m in mult]} (each 1); "
        f"<Res E1/2, chi> = <Res E5/2, chi> = 0",
        all(abs(m - 1) < TOL for m in mult)
        and all(abs(sum(spin_char(1, G.elems[x]) * (1 if (s == 0 or x in T2) else -1) * np.conj(r[x]) for x in H)) < TOL
                for r in spin_chars for s in (0, 1)))

# ---------------------------------------------------------------- all subgroups of O as site groups
out("\n=== Extra: every subgroup K of O as a site-symmetry group ===")
out("  (does the preimage of K admit a 1-dim rep with -1 -> -1, i.e. can a ONE-state fermion sit at a site")
out("   with site group K and carry w2|K?  If yes: which 2O-rep does the orbit multiplet carry?)")
subs = set()
for a_ in range(48):
    for b_ in range(a_, 48):
        S = frozenset(G.generated([a_, b_, M1]))
        subs.add(S)
# conjugacy classes of preimage subgroups
reps_sub = []
for S in sorted(subs, key=len):
    if any(frozenset(G.mul[G.mul[g][x]][G.inv[g]] for x in T) == S for T in reps_sub for g in range(48)):
        continue
    reps_sub.append(S)
for S in reps_sub:
    # describe the SO(3) image
    rots = {}
    for x in S:
        U = G.elems[x]
        ang = 2 * np.arccos(np.clip(np.trace(U).real / 2, -1, 1))
        rots[rkey(R_of[x])] = round(np.degrees(ang))
    angs = sorted(set(min(a, 360 - a) for a in rots.values()))
    r = one_dim_reps(G, S, 24 if len(S) <= 24 else 8)
    sp = [x for x in r if abs(x[M1] + 1) < TOL]
    ab = all(G.mul[p][q] == G.mul[q][p] for p in S for q in S)
    decs = sorted({str(decompose(induce(S, x))) for x in sp})
    out(f"  |K| = {len(S)//2:2d}  rotation angles {angs}  preimage abelian={ab!s:5s}  "
        f"#1-dim reps with -1->-1: {len(sp):2d}  orbit size {48//len(S):2d}  Ind -> {decs if decs else '-'}")

with open(__file__.replace("check_grouptheory.py", "out_grouptheory.txt"), "w") as fh:
    fh.write("\n".join(out_lines) + "\n")
