#!/usr/bin/env python3
"""T16 test 2: the blank state as the unique symmetric configuration; stabiliser order as a
Lyapunov function along permanent births; deterministic covariant laws cannot leave the blank.

Model: ring of L=6 sites; possibility menu = 6 octahedron vertices (+-x,+-y,+-z), internal group
O (24 proper rotations of the octahedron acting on the menu); lattice group = translations (6) x
reflection (2).  Configuration: each site empty (0) or one possibility (1..6).
Variant B adds an invariant 7th possibility ("centre", the I/2-like point)."""
import itertools
import numpy as np

L = 6
# octahedron vertices as vectors, and the 24 rotations as signed permutation matrices det +1
verts = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i, p in enumerate(perm):
            M[i, p] = signs[i]
        if round(np.linalg.det(M)) == 1:
            rots.append(M)
assert len(rots) == 24
vidx = {tuple(v): i for i, v in enumerate(verts)}
menu_maps = []
for M in rots:
    menu_maps.append(np.array([vidx[tuple(M @ v)] for v in verts]))
menu_maps = np.array(menu_maps)  # (24, 6)

site_perms = []
for r in range(L):
    for refl in (False, True):
        site_perms.append(np.array([((-i if refl else i) + r) % L for i in range(L)]))
site_perms = np.array(site_perms)  # (12, L)


def build(centre: bool):
    q = 6 + (1 if centre else 0)  # menu symbols 0..q-1, empty = q
    base = q + 1
    maps = []
    for m in menu_maps:
        full = np.concatenate([m, [6]] if centre else [m]) if centre else m
        full = np.concatenate([full, [q]])  # empty maps to empty
        maps.append(full)
    maps = np.array(maps)
    return q, base, maps


def all_configs(base):
    n = base ** L
    idx = np.arange(n)
    digs = np.zeros((n, L), int)
    t = idx.copy()
    for i in range(L):
        digs[:, i] = t % base
        t //= base
    return digs


def encode(digs, base):
    w = base ** np.arange(L)
    return digs @ w


def stab_orders(centre):
    q, base, maps = build(centre)
    digs = all_configs(base)
    n = digs.shape[0]
    stab = np.zeros(n, int)
    for sp in site_perms:
        for mm in maps:
            # g acts: new config c'[sp[i]] = mm[c[i]]
            img = np.empty_like(digs)
            img[:, sp] = mm[digs]
            stab += (encode(img, base) == np.arange(n))
    return q, base, digs, stab


def analyse(centre):
    q, base, digs, stab = stab_orders(centre)
    n = digs.shape[0]
    G = len(site_perms) * len(menu_maps)
    fixed = np.where(stab == G)[0]
    print(f"[{'pure menu + centre' if centre else 'pure menu'}] |G| = {G}, configs = {n}, "
          f"configs fixed by all of G: {len(fixed)}")
    for f in fixed:
        d = digs[f]
        print("   fixed config digits:", d.tolist(), "(empty = %d)" % q)
    # Lyapunov check along every single birth (empty site -> symbol in menu)
    viol = strict = tot = 0
    for i in range(L):
        emp = np.where(digs[:, i] == q)[0]
        for a in range(q):
            c2 = digs[emp].copy()
            c2[:, i] = a
            j = encode(c2, base)
            tot += len(emp)
            viol += int(np.sum(stab[j] > stab[emp]))
            strict += int(np.sum(stab[j] < stab[emp]))
    print(f"   single-birth edges: {tot}, stabiliser order increased on {viol}, strictly dropped on {strict}")
    return len(fixed), viol


nf_pure, viol_pure = analyse(False)
nf_c, viol_c = analyse(True)

# 2d: deterministic covariant closure from empty, count-threshold rules on a ring of 6
print("\n[2d] deterministic count-threshold rules from the empty ring (k = recorded neighbours 0..2)")
def sync(A):
    occ = np.zeros(L, bool)
    while True:
        k = np.roll(occ, 1).astype(int) + np.roll(occ, -1).astype(int)
        elig = (~occ) & np.isin(k, list(A))
        if not elig.any():
            return occ
        occ = occ | elig
        # (crowding rules would never stop growing under synchronous update only if eligible remains)
        if occ.all():
            return occ

def seq_scan(A):
    occ = np.zeros(L, bool)
    changed = True
    while changed:
        changed = False
        for i in range(L):
            k = int(occ[(i - 1) % L]) + int(occ[(i + 1) % L])
            if (not occ[i]) and k in A:
                occ[i] = True
                changed = True
    return occ

partial_sync = 0
noncov_seq = 0
for r in range(1, 4):
    for A in itertools.combinations(range(3), r):
        a = sync(A)
        s = seq_scan(A)
        kind = "empty" if not a.any() else ("full" if a.all() else "PARTIAL")
        partial_sync += kind == "PARTIAL"
        # translation covariance of the sequential scan: is the result invariant under all rotations?
        inv = all(np.array_equal(np.roll(s, t), s) for t in range(L))
        noncov_seq += not inv
        print(f"   A={A}: synchronous -> {kind:7s}; site-order scan -> {s.astype(int).tolist()} "
              f"{'(translation-invariant)' if inv else '(NOT translation-invariant)'}")


# 2c' (added after 2c FAILED as pre-registered): what does survive?  Internal pointwise stabiliser
# (rotations fixing every recorded possibility, sites untouched) is monotone by inclusion.
def internal_pointwise(centre):
    q, base, maps = build(centre)
    digs = all_configs(base)
    n = digs.shape[0]
    st = np.zeros(n, int)
    for mm in maps:
        ok = np.ones(n, bool)
        for i in range(L):
            d = digs[:, i]
            ok &= (d == q) | (mm[d] == d)
        st += ok
    viol = 0
    for i in range(L):
        emp = np.where(digs[:, i] == q)[0]
        for a in range(q):
            c2 = digs[emp].copy(); c2[:, i] = a
            viol += int(np.sum(st[encode(c2, base)] > st[emp]))
    return viol, st

v_int, st_int = internal_pointwise(False)
print("\n[2c'] internal pointwise stabiliser: violations along births =", v_int,
      "; order 24 at empty, values seen:", sorted(set(st_int.tolist()), reverse=True))
# explicit counterexample to the set-stabiliser Lyapunov claim
q, base, maps = build(False)
c1 = np.full(L, q); c1[0] = 0
c2 = c1.copy(); c2[3] = 0
def lattice_stab(c):
    n = 0
    for sp in site_perms:
        img = np.empty_like(c); img[sp] = c
        n += np.array_equal(img, c)
    return n
print("   counterexample: one record at site 0 -> lattice set-stabiliser", lattice_stab(c1),
      "; add the same possibility at site 3 -> lattice set-stabiliser", lattice_stab(c2),
      "(a second record can RAISE the set symmetry)")

ok2a = nf_pure == 1
ok2b = nf_c == 2
ok2c = viol_pure == 0 and viol_c == 0
ok2d = partial_sync == 0 and noncov_seq > 0
print("\nRESULT 2a unique fixed config (pure menu):", ok2a)
print("RESULT 2b two fixed configs with an invariant possibility:", ok2b)
print("RESULT 2c (pre-registered) set-stabiliser order never rises along births:", ok2c, "  <- FAILED; see 2c'")
print("RESULT 2c' internal pointwise stabiliser monotone:", v_int == 0)
print("RESULT 2d no synchronous rule gives a partial config; site-order scans break covariance:", ok2d)
