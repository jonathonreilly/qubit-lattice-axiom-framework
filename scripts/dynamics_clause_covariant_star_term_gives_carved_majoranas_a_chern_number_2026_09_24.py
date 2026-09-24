#!/usr/bin/env python3
"""A covariant time-reversal-odd star term gives a record-carved Majorana network a Chern number.

Open PR 9097 showed that record fields keep the carved Majoranas of open PR
9054 sublattice-symmetric, that a gapless start plus Kitaev's non-covariant
pattern gives a weak Chern number, that zero dangling fields are realizable
on some networks, and that no covariant time-reversal-odd star term of
weight at most three gives a free same-class bilinear there. This runner
extends the star terms to every odd weight (1, 3, 5, 7) and finds a covariant
one that makes a realizable carving chiral (supplied models, finite
diagnostics, no physical reading):

1. The carving: a 19-site relaxed three-direction network on the 4x4x4 cell
   (from open PR 9097's zero-field search). No record touches unrecorded
   sites along all three axes. Each record points along the last axis that
   avoids its unrecorded neighbours, with sign (-1)^(x+y+z), so every field
   on an unrecorded site vanishes.
2. Covariant odd star terms by signed orbits of the 24 proper rotations
   under full soldering: weights 1 and 3 give 37 dimensions, matching open
   PR 9088; weights 1 to 7 give 325.
3. Exact Majorana images: every Pauli string on the carving, with records
   replaced by their values, is mapped to Kitaev's Majoranas with the
   physical constraint inserted where needed. The map reproduces the
   network's bond matrix exactly, and on three-site clusters with bonds,
   Kitaev's pattern and dangling fields the spin spectrum equals one parity
   sector of the Majorana spectrum.
4. The free covariant subspace: covariant terms whose every reduced string
   is a free (gauge-invariant, bilinear) Majorana term. It is 41-dimensional
   here. The projection onto it of the weight-5 orbit
   s^x_{+x} s^y_{-x} s^y_{+y} s^z_{-y} s^z_{+z} is a covariant term of
   weights 5 and 7 whose non-free strings cancel exactly and whose free
   strings include same-class bilinears.
5. The chiral phase: with the compass-point bonds plus lambda times that term,
   at lambda = 1, 2 and 4 the lowest flux sectors (8 of 16, degenerate) each
   have 12 exact zero modes per cell, a gap above them, and weak Chern
   numbers (-1, 0, 0) on four k_x planes.
6. Chiral surface modes: on a slab 12 cells thick with open boundaries along
   z (lambda = 2, k_x = 1), the in-gap states sit on the two surfaces, and as
   k_y winds once they cross energies -0.01 and 0.01 once upward on one
   surface and once downward on the other.
7. The phase needs zero dangling fields: its 12 zero modes sit entirely on
   dangling b Majoranas. Tilting the records to give dangling fields of
   size 0.1 couples them in, leaves 2 exact zero modes per cell, and the
   negative bands' Chern number on the k_x planes becomes 0. With open PR
   9054's generic record contents no covariant odd star term stays free at
   all on this carving.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 900

import numpy as np
from scipy.optimize import minimize

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


# ------------------------------------------------ the carving machinery of open PR 9054 (compass point)
L3 = (4, 4, 4)
# generic record contents: the fixed direction (1, sqrt 2, sqrt 3) projected
# orthogonal to each record's constrained axes; its components are positive,
# so the two records on a dangling axis never cancel
V_GENERIC = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)]) / np.sqrt(6.0)
N20 = [(0, 0, 0), (0, 0, 3), (0, 1, 0), (0, 2, 1), (0, 2, 2), (0, 3, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
       (1, 1, 1), (1, 2, 1), (2, 0, 1), (2, 0, 2), (2, 1, 1), (2, 1, 2), (3, 0, 0), (3, 1, 2), (3, 2, 2),
       (3, 3, 0), (3, 3, 1)]
N16 = [(0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 1, 2), (1, 1, 3), (2, 0, 3), (2, 1, 0),
       (2, 1, 3), (2, 2, 0), (3, 0, 2), (3, 0, 3), (3, 2, 0), (3, 2, 1), (3, 3, 1), (3, 3, 2)]


def nbr(s, ax, d, Ls=L3):
    t = list(s)
    t[ax] = (t[ax] + d) % Ls[ax]
    return tuple(t)


def winding_rank(comp, Ls=L3):
    comp = set(comp)
    s0 = min(comp)
    pos = {s0: (0, 0, 0)}
    stack = [s0]
    wind = set()
    while stack:
        v = stack.pop()
        for ax in range(3):
            for d in (1, -1):
                t = list(v)
                t[ax] += d
                off = [0, 0, 0]
                if t[ax] == Ls[ax]:
                    t[ax], off[ax] = 0, 1
                if t[ax] == -1:
                    t[ax], off[ax] = Ls[ax] - 1, -1
                w = tuple(t)
                if w not in comp:
                    continue
                pw = tuple(pos[v][i] + off[i] for i in range(3))
                if w in pos:
                    if pos[w] != pw:
                        wind.add(tuple(pw[i] - pos[w][i] for i in range(3)))
                else:
                    pos[w] = pw
                    stack.append(w)
    rank = int(np.linalg.matrix_rank(np.array(sorted(wind)))) if wind else 0
    return len(pos) == len(comp), rank


def build(comp, Ls=L3):
    comp = sorted(comp)
    ix = {s: i for i, s in enumerate(comp)}
    cs = set(comp)
    bonds = []
    for s in comp:
        for ax in range(3):
            t = list(s)
            t[ax] += 1
            off = [0, 0, 0]
            if t[ax] == Ls[ax]:
                t[ax], off[ax] = 0, 1
            t = tuple(t)
            if t in cs:
                bonds.append((ix[s], ix[t], ax, tuple(off)))
    contents, cons_ok = {}, True
    for r in itertools.product(*[range(l) for l in Ls]):
        if r in cs:
            continue
        cons = set()
        for ax in range(3):
            for d in (1, -1):
                u = nbr(r, ax, d, Ls)
                if u in cs and nbr(u, ax, d, Ls) in cs:
                    cons.add(ax)
        if len(cons) > 2:
            cons_ok = False
            continue
        q = V_GENERIC.copy()
        for a in cons:
            q[a] = 0.0
        contents[r] = q / np.linalg.norm(q)
    kept_field, dfield = 0.0, {}
    for s in comp:
        for ax in range(3):
            for d in (1, -1):
                r = nbr(s, ax, d, Ls)
                if r in cs:
                    continue
                f = contents[r][ax] if r in contents else 0.0
                if nbr(s, ax, -d, Ls) in cs:
                    kept_field = max(kept_field, abs(f))
                else:
                    dfield[(ix[s], ax)] = dfield.get((ix[s], ax), 0.0) + f
    live = [key for key, v in dfield.items() if abs(v) > 0]
    uf = list(range(len(comp)))

    def fnd(a):
        while uf[a] != a:
            uf[a] = uf[uf[a]]
            a = uf[a]
        return a

    tree, non = [], []
    for b in bonds:
        ra, rb = fnd(b[0]), fnd(b[1])
        if ra != rb:
            uf[ra] = rb
            tree.append(b)
        else:
            non.append(b)
    per_axis = all(sum(nbr(s, ax, d, Ls) in cs for d in (1, -1)) <= 1 for s in comp for ax in range(3))
    return dict(comp=comp, ix=ix, n=len(comp), bonds=bonds, dfield=dfield, live=live, tree=tree, non=non,
                cons_ok=cons_ok, kept_field=kept_field, per_axis=per_axis,
                ndangling=sum(1 for s in comp for ax in range(3)
                              if nbr(s, ax, 1, Ls) not in cs and nbr(s, ax, -1, Ls) not in cs))


def majorana_matrix(G, u_all, k=None):
    n = G["n"]
    N = n + len(G["live"])
    A = np.zeros((N, N), dtype=complex)
    for (j, kk, ax, off), ub in zip(G["bonds"], u_all):
        t = -2 * ub * (np.exp(1j * np.dot(k, off)) if k is not None else 1.0)
        A[j, kk] += t
        A[kk, j] -= np.conj(t)
    for pos, (j, ax) in enumerate(G["live"]):
        h = G["dfield"][(j, ax)]
        A[n + pos, j] += 2 * h
        A[j, n + pos] -= 2 * h
    return A


def u_from_non(G, u_non):
    uu = {b: 1 for b in G["tree"]}
    uu.update({b: v for b, v in zip(G["non"], u_non)})
    return [uu[b] for b in G["bonds"]]



# ------------------------------------------------ exact Majorana images of Pauli strings on a carving
E3 = np.eye(3, dtype=int)


def cell_of(x):
    return tuple(int(v) // 4 for v in x)


def fold(x):
    return tuple(int(v) % 4 for v in x)


class Carving:
    """A periodic relaxed carving on the 4x4x4 cell: kept bonds with gauge values, dangling axes, Majorana labels."""

    def __init__(self, comp, bonds_u):
        self.comp = sorted(comp)
        self.kept = {s: {} for s in self.comp}
        for (j, k, ax, off, u) in bonds_u:
            sj, sk = self.comp[j], self.comp[k]
            self.kept[sj][ax] = (sk, np.array(off), u)          # bond j -> k across cell offset off, u_jk = u
            self.kept[sk][ax] = (sj, -np.array(off), -u)
        self.dangling = {s: [a for a in range(3) if a not in self.kept[s]] for s in self.comp}
        self.majs = [("c", s) for s in self.comp] + [("b", s, a) for s in self.comp for a in self.dangling[s]]
        self.mid = {m: i for i, m in enumerate(self.majs)}

    def image(self, P):
        """Pauli string P (unwrapped site -> label) as coef * g1 g2 on the physical space, (coef, None, None) if it is
        a pure gauge product, or None if it is not a free bilinear. sigma^a = i b^a c, and sigma^a D = -i b^{a+1} b^{a+2}
        where D = b^x b^y b^z c = 1; b's on a kept bond pair into b_j b_k = -i u_jk."""
        sites = sorted(P)
        best = None
        for d in itertools.product((0, 1), repeat=len(sites)):
            coef, L = 1 + 0j, []
            for x, dx in zip(sites, d):
                a = P[x]
                if dx == 0:
                    coef *= 1j
                    L += [("b", x, a), ("c", x)]
                else:
                    coef *= -1j
                    L += [("b", x, (a + 1) % 3), ("b", x, (a + 2) % 3)]
            ok = True
            while True:
                p1 = next((q for q, it in enumerate(L) if it[0] == "b" and it[2] in self.kept[fold(it[1])]), None)
                if p1 is None:
                    break
                x, a = L[p1][1], L[p1][2]
                sk, off, u = self.kept[fold(x)][a]
                target = ("b", tuple(np.array(x) - np.array(fold(x)) + np.array(sk) + 4 * off), a)
                if target not in L:
                    ok = False
                    break
                p2 = L.index(target)
                assert p2 > p1                                  # p1 is the first kept-axis b, so its partner comes later
                coef *= (-1) ** (p2 - p1 - 1)
                del L[p2]
                del L[p1]
                coef *= -1j * u
            if not ok or len(L) > 2:
                continue
            if best is None or len(L) < len(best[1]):
                best = (coef, L)
        if best is None:
            return None
        coef, L = best
        if not L:
            return (coef, None, None)

        def key(g):
            return (("c", fold(g[1])) if g[0] == "c" else ("b", fold(g[1]), g[2])), cell_of(g[1])
        return (coef, key(L[0]), key(L[1]))

# ------------------------------------------------ 1. the carving and its zero-field records
N19 = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 3), (0, 2, 3), (1, 0, 1), (1, 0, 2), (1, 1, 2), (1, 1, 3), (1, 3, 1),
       (2, 1, 2), (2, 2, 1), (2, 2, 2), (2, 3, 0), (2, 3, 1), (3, 0, 0), (3, 2, 3), (3, 3, 0), (3, 3, 3)]
CS = set(N19)
G19 = dict(build(N19), live=[], dfield={})
content, touch = {}, []
for r in itertools.product(range(4), repeat=3):
    if r in CS:
        continue
    avoid = {ax for ax in range(3) for d in (1, -1) if nbr(r, ax, d) in CS}
    touch.append(len(avoid))
    opts = [a for a in range(3) if a not in avoid]
    content[r] = (opts[-1], (-1) ** (sum(r) % 2))          # the last free axis, sign staggered by parity
field_max = max(abs(content[r][1]) * (content[r][0] == ax) for s in N19 for ax in range(3) for d in (1, -1)
                for r in [nbr(s, ax, d)] if r not in CS)
conn, rank = winding_rank(N19)
check("the carving: a 19-site relaxed three-direction network whose zero-field records are realizable",
      conn and rank == 3 and G19["per_axis"] and max(touch) <= 2 and field_max == 0,
      f"connected {conn}, winding rank {rank}, bonds {len(G19['bonds'])}; every record touches at most {max(touch)} axes; "
      f"largest field on an unrecorded site {field_max}")

# ------------------------------------------------ 2. covariant odd star terms by signed orbits (full soldering)
ROTS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3), dtype=int)
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if round(np.linalg.det(R)) == 1:
            ROTS.append(R)
POS = [np.zeros(3, dtype=int)] + [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def sidx(v):
    return [k for k, u in enumerate(POS) if np.array_equal(u, v)][0]


def star_strings(weights):
    out = []
    for w in weights:
        for sup in ([(0,)] if w == 1 else list(itertools.combinations(range(7), w))):
            for labs in itertools.product(range(3), repeat=len(sup)):
                out.append((sup, labs))
    return out


def signed_orbits(strings):
    """Covariant (full soldering) combinations: orbit sums with consistent signs; orbits with a sign clash vanish."""
    sid = {s: i for i, s in enumerate(strings)}
    maps = []
    for R in ROTS:
        img, sg = np.zeros(len(strings), dtype=np.int64), np.zeros(len(strings), dtype=np.int64)
        for i, (sup, labs) in enumerate(strings):
            new = [sidx(R @ POS[x]) for x in sup]
            sign, labs2 = 1, []
            for a in labs:
                b = int(np.flatnonzero(R[:, a])[0])
                sign *= int(R[b, a])
                labs2.append(b)
            order = sorted(range(len(sup)), key=lambda t: new[t])
            img[i] = sid[(tuple(new[t] for t in order), tuple(labs2[t] for t in order))]
            sg[i] = sign
        maps.append((img, sg))
    seen, vecs = np.zeros(len(strings), dtype=bool), []
    for i in range(len(strings)):
        if seen[i]:
            continue
        orb, frontier, ok = {i: 1}, [i], True
        while frontier:
            x = frontier.pop()
            for img, sg in maps:
                y, s_ = int(img[x]), orb[x] * int(sg[x])
                if y in orb:
                    ok &= orb[y] == s_
                else:
                    orb[y] = s_
                    frontier.append(y)
        for y in orb:
            seen[y] = True
        if ok:
            vecs.append(orb)
    return vecs


dim3 = len(signed_orbits(star_strings([1, 3])))
STR = star_strings([1, 3, 5, 7])
VECS = signed_orbits(STR)
check("covariant odd star terms under full soldering, as signed rotation orbits",
      dim3 == 37 and len(VECS) == 325,
      f"weights 1 and 3: {dim3} (open PR 9088's full-soldering count); weights 1, 3, 5, 7: {len(VECS)}")

# ------------------------------------------------ 3. exact Majorana images
ks4 = [np.array(q) * 2 * np.pi / 4 for q in itertools.product(range(4), repeat=3)]


def zero_field_sector():
    best = None
    for u in itertools.product((1, -1), repeat=len(G19["non"])):
        E = sum(-0.5 * ev[ev > 0].sum() for ev in
                (np.linalg.eigvalsh(1j * majorana_matrix(G19, u_from_non(G19, u), k)) for k in ks4)) / len(ks4)
        if best is None or E < best[0]:
            best = (E, u)
    return u_from_non(G19, best[1])


u0 = zero_field_sector()
car = Carving(G19["comp"], [(j, k, ax, off, ub) for (j, k, ax, off), ub in zip(G19["bonds"], u0)])


def add_terms(A, terms, k, lam, carv):
    for cf, g1, g2 in terms:
        tau = (cf / 1j).real
        (m1, c1), (m2, c2) = g1, g2
        i1, i2 = carv.mid[m1], carv.mid[m2]
        ph = np.exp(1j * np.dot(k, np.array(c2) - np.array(c1)))
        A[i1, i2] += 2 * lam * tau * ph
        A[i2, i1] -= 2 * lam * tau * np.conj(ph)


bond_terms = [car.image({tuple(np.array(G19["comp"][j])): ax, tuple(np.array(G19["comp"][kk]) + 4 * np.array(off)): ax})
              for (j, kk, ax, off) in G19["bonds"]]
bond_dev = 0.0
for _ in range(4):
    k = np.random.default_rng(100 + _).uniform(0, 2 * np.pi, 3)
    A = np.zeros((len(car.majs), len(car.majs)), dtype=complex)
    add_terms(A, bond_terms, k, 1.0, car)
    bond_dev = max(bond_dev, np.linalg.norm(A[:G19["n"], :G19["n"]] - majorana_matrix(G19, u0, k)))
PAU = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
rngc = np.random.default_rng(3)
ed_dev = 0.0
for trial in range(12):
    a, cax = rngc.choice(3, size=2, replace=False)
    m = (1, 1, 1)
    i_, k_ = tuple(np.array(m) + E3[a]), tuple(np.array(m) + E3[cax])
    comp = sorted([m, i_, k_])
    ix = {s: t for t, s in enumerate(comp)}
    cl = Carving(comp, [(ix[m], ix[i_], a, (0, 0, 0), int(rngc.choice([1, -1]))),
                        (ix[m], ix[k_], cax, (0, 0, 0), int(rngc.choice([1, -1])))])
    terms = [(1.0, {m: a, i_: a}), (1.0, {m: cax, k_: cax}), (rngc.normal(), {i_: a, m: 3 - a - cax, k_: cax})]
    terms += [(rngc.normal(), {s: ax}) for s in comp for ax in cl.dangling[s]]
    A = np.zeros((len(cl.majs), len(cl.majs)))
    H = np.zeros((8, 8), dtype=complex)
    for lam, Pm in terms:
        cf, g1, g2 = cl.image(Pm)
        tau = (lam * cf / 1j).real
        A[cl.mid[g1[0]], cl.mid[g2[0]]] += 2 * tau
        A[cl.mid[g2[0]], cl.mid[g1[0]]] -= 2 * tau
        ops = [np.eye(2, dtype=complex)] * 3
        for sx, lb in Pm.items():
            ops[ix[sx]] = PAU[lb]
        H += lam * np.kron(np.kron(ops[0], ops[1]), ops[2])
    eps = np.sort(np.linalg.eigvalsh(1j * A))[len(cl.majs) // 2:]
    lev = {0: [], 1: []}
    for occ in itertools.product((0, 1), repeat=len(eps)):
        lev[sum(occ) % 2].append(-0.5 * eps.sum() + np.dot(occ, eps))
    spin = np.sort(np.linalg.eigvalsh(H))
    ed_dev = max(ed_dev, min(np.max(np.abs(np.sort(lev[p]) - spin)) for p in (0, 1)))
corner = next(s_ for s_ in car.comp if len(car.kept[s_]) >= 2)
ca, cc = sorted(car.kept[corner])[:2]
xa = tuple(np.array(car.kept[corner][ca][0]) + 4 * car.kept[corner][ca][1])
xc = tuple(np.array(car.kept[corner][cc][0]) + 4 * car.kept[corner][cc][1])
kit_img = car.image({xa: ca, corner: 3 - ca - cc, xc: cc})
kit_same = kit_img is not None and kit_img[1][0][0] == "c" and kit_img[2][0][0] == "c" and \
    (sum(kit_img[1][0][1]) - sum(kit_img[2][0][1])) % 2 == 0
kept_field_free = car.image({corner: ca}) is not None
check("exact Majorana images: the bond matrix is reproduced, and three-site clusters match the spin spectrum",
      bond_dev < 1e-12 and ed_dev < 1e-12 and kit_same and not kept_field_free,
      f"bond matrix deviation {bond_dev:.0e}; 12 clusters with bonds, Kitaev's pattern and dangling fields: largest spectral deviation {ed_dev:.0e}; "
      f"on the carving Kitaev's pattern is a free same-class c-c bilinear and a kept-axis field is not free")

# ------------------------------------------------ 4. the free covariant subspace on this carving
reduced = {}                       # (string index, centre) -> (unwrapped reduced string, record factor)
for si, (sup, labs) in enumerate(STR):
    for m in itertools.product(range(4), repeat=3):
        Pm, coef = {}, 1
        for s_, lab in zip(sup, labs):
            x = tuple(np.array(m) + POS[s_])
            if fold(x) in CS:
                Pm[x] = lab
            elif content[fold(x)][0] != lab:
                coef = 0
                break
            else:
                coef *= content[fold(x)][1]
        if coef:
            reduced[(si, m)] = (Pm, coef)
fkey = {}
by_string = {}
for (si, m), (Pm, coef) in reduced.items():
    fk = tuple(sorted((fold(x), l) for x, l in Pm.items()))
    fkey.setdefault(fk, Pm)
    by_string.setdefault(si, []).append((fk, coef, m))
klist = sorted(fkey)
kid = {k_: i for i, k_ in enumerate(klist)}
Amat = np.zeros((len(klist), len(VECS)))
for vi, orb in enumerate(VECS):
    for si, sg in orb.items():
        for fk, coef, m in by_string.get(si, []):
            Amat[kid[fk], vi] += sg * coef
img_fold = [car.image(fkey[k_]) if fkey[k_] else (1.0, None, None) for k_ in klist]
bad = np.array([im is None for im in img_fold])
nzr = np.linalg.norm(Amat, axis=1) > 1e-12
_, sv, vt = np.linalg.svd(Amat[bad & nzr])
Nf = vt[int(np.sum(sv > 1e-9)):].T
Pfree = Nf @ Nf.T
target = ((1, 2, 3, 4, 5), (0, 1, 1, 2, 2))      # s^x_{+x} s^y_{-x} s^y_{+y} s^z_{-y} s^z_{+z}
oi = next(i for i, orb in enumerate(VECS) if STR.index(target) in orb)
v = Pfree[:, oi] / np.max(np.abs(Pfree[:, oi]))
weights_used = sorted({len(STR[min(VECS[j])][0]) for j in range(len(VECS)) if abs(v[j]) > 1e-9})
cancel = np.max(np.abs(Amat[bad] @ v)) if bad.any() else 0.0


def class_of(g):
    return sum(g[0][1]) % 2 if g[0][0] == "c" else 1 - sum(g[0][1]) % 2


def is_kitaev_pattern(fk):
    """A three-site string i - m - k at a corner m with labels (axis of i, third axis, axis of k)."""
    if len(fk) != 3:
        return False
    sites = dict(fk)
    for m_, lab_m in sites.items():
        others = [(t, l) for t, l in sites.items() if t != m_]
        axes = []
        for t, l in others:
            ax = [a_ for a_ in range(3) if a_ in car.kept[m_] and car.kept[m_][a_][0] == t]
            if len(ax) != 1 or l != ax[0]:
                break
            axes.append(ax[0])
        else:
            if len(set(axes)) == 2 and lab_m == 3 - sum(axes):
                return True
    return False


same_idx = [i for i, im in enumerate(img_fold) if im is not None and im[1] is not None and abs(Amat[i] @ v) > 1e-9
            and class_of(im[1]) == class_of(im[2])]
same_free = len(same_idx)
same_kitaev = sum(1 for i in same_idx if is_kitaev_pattern(klist[i]))
check("the free covariant subspace, and the projection of the weight-5 orbit onto it",
      Nf.shape[1] == 41 and cancel < 1e-9 and weights_used == [5, 7] and same_free > 0 and same_kitaev == same_free,
      f"free subspace dimension {Nf.shape[1]} of {len(VECS)}; projected term uses {int(np.sum(np.abs(v) > 1e-9))} orbits of weights "
      f"{weights_used}; non-free strings cancel to {cancel:.0e}; same-class free bilinears {same_free}, all Kitaev's pattern at corners")


# ------------------------------------------------ 5. the chiral phase
def term_entries(carv):
    ent, const = [], 0.0
    for vi, orb in enumerate(VECS):
        if abs(v[vi]) < 1e-14:
            continue
        for si, sg in orb.items():
            for fk, coef, m in by_string.get(si, []):
                im = carv.image(reduced[(si, m)][0])
                if im is None:
                    continue                              # non-free strings cancel in total (check 4)
                cf, g1, g2 = im
                if g1 is None:
                    const += (v[vi] * sg * coef * cf).real
                else:
                    ent.append((v[vi] * sg * coef * cf, g1, g2))
    return ent, const


def H_of(uvals, ent, carv, k, lam):
    A = np.zeros((len(carv.majs), len(carv.majs)), dtype=complex)
    A[:G19["n"], :G19["n"]] = majorana_matrix(G19, uvals, k)
    add_terms(A, ent, k, lam, carv)
    return 1j * A


def chern(uvals, ent, carv, lam, p, kf, N=24):
    a1, a2 = [a for a in range(3) if a != p]
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    vec = {}
    for i1, k1 in enumerate(ks):
        for i2, k2 in enumerate(ks):
            k = np.zeros(3)
            k[a1], k[a2], k[p] = k1, k2, kf
            w, V = np.linalg.eigh(H_of(uvals, ent, carv, k, lam))
            vec[(i1, i2)] = V[:, w < -1e-7]
    if len({x.shape[1] for x in vec.values()}) != 1:
        return None
    tot = 0.0
    for i1 in range(N):
        for i2 in range(N):
            q = [vec[(i1, i2)], vec[((i1 + 1) % N, i2)], vec[((i1 + 1) % N, (i2 + 1) % N)], vec[(i1, (i2 + 1) % N)]]
            tot += np.angle(np.prod([np.linalg.det(q[j].conj().T @ q[(j + 1) % 4]) for j in range(4)]))
    return tot / (2 * np.pi)


def gap_above_zero(uvals, ent, carv, lam):
    grid = [np.array(q) * 2 * np.pi / 6 for q in itertools.product(range(6), repeat=3)]
    nz = min(int(np.sum(np.abs(np.linalg.eigvalsh(H_of(uvals, ent, carv, k, lam))) < 1e-9)) for k in grid)
    f = lambda k: np.sort(np.abs(np.linalg.eigvalsh(H_of(uvals, ent, carv, np.array(k), lam))))[nz]
    seeds = sorted((f(k), tuple(k)) for k in grid)[:6]
    return nz, min(minimize(f, np.array(k0), method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-12,
                                                                               "maxiter": 3000}).fun for _, k0 in seeds)


ks6 = [np.array(q) * 2 * np.pi / 6 for q in itertools.product(range(6), repeat=3)]
rows5, ok5 = [], True
for lam in (1.0, 2.0, 4.0):
    sectors = []
    for u in itertools.product((1, -1), repeat=len(G19["non"])):
        uvals = u_from_non(G19, u)
        carv = Carving(G19["comp"], [(j, k, ax, off, ub) for (j, k, ax, off), ub in zip(G19["bonds"], uvals)])
        ent, const = term_entries(carv)
        E = sum(-0.5 * ev[ev > 0].sum() for ev in (np.linalg.eigvalsh(H_of(uvals, ent, carv, k, lam)) for k in ks6)) / len(ks6)
        sectors.append((E + lam * const, u, uvals, carv, ent))
    sectors.sort(key=lambda t: t[0])
    lowest = [t for t in sectors if t[0] < sectors[0][0] + 1e-6]
    next_gap = min(t[0] for t in sectors if t[0] >= sectors[0][0] + 1e-6) - sectors[0][0]
    cx_all, gaps = set(), []
    for E, u, uvals, carv, ent in lowest:
        nz, gp = gap_above_zero(uvals, ent, carv, lam)
        gaps.append((nz, gp))
        cx_all.add(round(chern(uvals, ent, carv, lam, 0, 1.0), 6))
    E, u, uvals, carv, ent = lowest[0]
    if lam == 2.0:
        slab_setup = (uvals, carv, ent, min(g for _, g in gaps))
    planes = {p: sorted({round(chern(uvals, ent, carv, lam, p, kf), 6) for kf in (0.5, 2.0, 3.5, 5.0)}) for p in range(3)}
    ok5 &= (len(lowest) == 8 and all(nz == 12 and gp > 0.01 for nz, gp in gaps) and cx_all == {-1.0}
            and planes == {0: [-1.0], 1: [0.0], 2: [0.0]})
    rows5.append(f"lambda {lam}: {len(lowest)} lowest sectors (next {next_gap:.4f} up), 12 zero modes, gap "
                 f"{min(g for _, g in gaps):.4f}, weak Chern numbers ({int(planes[0][0])}, {int(planes[1][0])}, {int(planes[2][0])})")
check("the chiral phase: in every lowest flux sector, a gapped band structure with weak Chern numbers (-1, 0, 0)",
      ok5, "; ".join(rows5))

# ------------------------------------------------ 6. chiral surface modes on a slab
uvals, carv, ent, bulk_gap = slab_setup
bonds_img = [carv.image({tuple(np.array(G19["comp"][j])): ax, tuple(np.array(G19["comp"][kk]) + 4 * np.array(off)): ax})
             for (j, kk, ax, off) in G19["bonds"]]
all_terms = [(cf, g1, g2, 1.0) for cf, g1, g2 in bonds_img] + [(cf, g1, g2, 2.0) for cf, g1, g2 in ent]
nm = len(carv.majs)
Nl = 12                                                   # cells along z, open boundary; k_x and k_y stay good


def slab(kx, ky):
    A = np.zeros((Nl * nm, Nl * nm), dtype=complex)
    for cf, (m1, c1), (m2, c2), w in all_terms:
        tau = (w * cf / 1j).real
        d = np.array(c2) - np.array(c1)
        ph = np.exp(1j * (kx * d[0] + ky * d[1]))
        for n in range(Nl):
            if 0 <= n + d[2] < Nl:
                i1, i2 = n * nm + carv.mid[m1], (n + d[2]) * nm + carv.mid[m2]
                A[i1, i2] += 2 * tau * ph
                A[i2, i1] -= 2 * tau * np.conj(ph)
    return 1j * A


surf = {"bottom": {}, "top": {}}
n_bulklike = 0
kys = np.linspace(0, 2 * np.pi, 121, endpoint=False)
for ky in kys:
    w, V = np.linalg.eigh(slab(1.0, ky))
    sel = (np.abs(w) > 1e-6) & (np.abs(w) < 0.8 * bulk_gap)
    for e, vec in zip(w[sel], V[:, sel].T):
        wts = np.array([np.sum(np.abs(vec[n * nm:(n + 1) * nm]) ** 2) for n in range(Nl)])
        side = "bottom" if wts[:2].sum() > 0.7 else ("top" if wts[-2:].sum() > 0.7 else None)
        if side:
            surf[side].setdefault(ky, []).append(e)
        else:
            n_bulklike += 1


def signed_crossings(branch, E0):
    tot = 0
    for i in range(len(kys)):
        a, b = kys[i], kys[(i + 1) % len(kys)]
        if len(branch.get(a, [])) == 1 and len(branch.get(b, [])) == 1:
            ea, eb = branch[a][0] - E0, branch[b][0] - E0
            if np.sign(ea) != np.sign(eb):
                tot += int(np.sign(eb - ea))
    return tot


flow = {side: [signed_crossings(surf[side], E0) for E0 in (-0.01, 0.01)] for side in surf}
check("chiral surface modes: on a slab open along z the in-gap states sit on the surfaces and cross the gap with opposite chirality",
      flow["top"] in ([1, 1], [-1, -1]) and flow["bottom"] == [-flow["top"][0]] * 2 and n_bulklike <= 8,
      f"12-cell slab at k_x = 1, lambda = 2, 121 values of k_y: surface-localized in-gap states top {sum(len(x) for x in surf['top'].values())}, "
      f"bottom {sum(len(x) for x in surf['bottom'].values())}, other {n_bulklike}; signed crossings of E = -0.01 and 0.01: "
      f"top {flow['top']}, bottom {flow['bottom']}")

# ------------------------------------------------ 7. the phase needs zero dangling fields
zero_modes = None
w0, V0 = np.linalg.eigh(H_of(uvals, ent, carv, np.array([0.3, 0.7, 1.1]), 2.0))
zm = V0[:, np.abs(w0) < 1e-9]
b_weight = sum(float(np.sum(np.abs(zm[carv.mid[m], :]) ** 2)) for m in carv.majs if m[0] == "b")
rng7 = np.random.default_rng(4)
dangling_terms = [carv.image({s_: a}) for s_ in carv.comp for a in carv.dangling[s_]]
tilt = rng7.choice([1, -1], size=len(dangling_terms)) * rng7.uniform(0.5, 1.5, size=len(dangling_terms))


def H_tilted(k, eps):
    A = np.zeros((nm, nm), dtype=complex)
    add_terms(A, [(eps * t * cf, g1, g2) for (cf, g1, g2), t in zip(dangling_terms, tilt)], k, 1.0, carv)
    return H_of(uvals, ent, carv, k, 2.0) + 1j * A


grid7 = [np.array(q) * 2 * np.pi / 6 for q in itertools.product(range(6), repeat=3)]
nz7 = min(int(np.sum(np.abs(np.linalg.eigvalsh(H_tilted(k, 0.1))) < 1e-9)) for k in grid7)


def chern_tilted(eps, p, kf, N=24):
    a1, a2 = [a for a in range(3) if a != p]
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    vec = {}
    for i1, k1 in enumerate(ks):
        for i2, k2 in enumerate(ks):
            k = np.zeros(3)
            k[a1], k[a2], k[p] = k1, k2, kf
            w, V = np.linalg.eigh(H_tilted(k, eps))
            vec[(i1, i2)] = V[:, w < -1e-7]
    if len({x.shape[1] for x in vec.values()}) != 1:
        return None
    tot = 0.0
    for i1 in range(N):
        for i2 in range(N):
            q = [vec[(i1, i2)], vec[((i1 + 1) % N, i2)], vec[((i1 + 1) % N, (i2 + 1) % N)], vec[(i1, (i2 + 1) % N)]]
            tot += np.angle(np.prod([np.linalg.det(q[j].conj().T @ q[(j + 1) % 4]) for j in range(4)]))
    return tot / (2 * np.pi)


cx7 = [chern_tilted(0.1, 0, kf) for kf in (0.5, 2.5)]
# generic contents (open PR 9054's rule: a fixed direction projected orthogonal to the kept axes of unrecorded
# neighbours), which leave fields on the dangling axes: how many covariant terms stay free?
gcontent = {}
for r in itertools.product(range(4), repeat=3):
    if r in CS:
        continue
    cons = {ax for ax in range(3) for d in (1, -1) if nbr(r, ax, d) in CS and nbr(nbr(r, ax, d), ax, d) in CS}
    qv = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)])
    for a_ in cons:
        qv[a_] = 0.0
    gcontent[r] = qv / np.linalg.norm(qv)
g_reduced = {}
for si, (sup, labs) in enumerate(STR):
    for m in itertools.product(range(4), repeat=3):
        Pm, coef = {}, 1.0
        for s_, lab in zip(sup, labs):
            x = tuple(np.array(m) + POS[s_])
            if fold(x) in CS:
                Pm[x] = lab
            else:
                coef *= gcontent[fold(x)][lab]
                if abs(coef) < 1e-15:
                    break
        if abs(coef) > 1e-15:
            g_reduced[(si, m)] = (tuple(sorted((fold(x), l) for x, l in Pm.items())), coef, Pm)
g_keys = sorted({v_[0] for v_ in g_reduced.values()})
g_kid = {k_: i for i, k_ in enumerate(g_keys)}
g_pm = {v_[0]: v_[2] for v_ in g_reduced.values()}
g_A = np.zeros((len(g_keys), len(VECS)))
for vi, orb in enumerate(VECS):
    for si, sg in orb.items():
        for m in itertools.product(range(4), repeat=3):
            if (si, m) in g_reduced:
                fk, coef, _ = g_reduced[(si, m)]
                g_A[g_kid[fk], vi] += sg * coef
g_bad = np.array([(car.image(g_pm[k_]) is None) if g_pm[k_] else False for k_ in g_keys])
_, g_sv, _ = np.linalg.svd(g_A[g_bad])
g_free = len(VECS) - int(np.sum(g_sv > 1e-9))
check("the phase needs zero dangling fields: its zero modes sit on dangling b's, and tilted records of size 0.1 remove the Chern number",
      zm.shape[1] == 12 and abs(b_weight - 12) < 1e-9 and nz7 < 12 and all(c is not None and abs(c) < 1e-6 for c in cx7)
      and g_free == 0,
      f"zero modes {zm.shape[1]}, weight on dangling b's {b_weight:.3f}; with dangling fields of size 0.1 (random signs): "
      f"exact zero modes {nz7}, Chern numbers on two k_x planes {[float(round(c, 6)) + 0.0 for c in cx7]}; "
      f"with open PR 9054's generic contents no covariant term stays free (free dimension {g_free})")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
