#!/usr/bin/env python3
import numpy as np, itertools, time
from cyc3d import *

t0 = time.time()
rng = np.random.default_rng(5)
shifts = lambda s: [s[k:] + s[:k] for k in range(len(s))]
fmt = lambda v: "(" + ",".join("%+.3g" % (c + 0.0) for c in v) + ")"

# 1. bulk identity + loop-area density M --------------------------------------------------
L = 12
none = np.zeros(L ** 3, bool)
for name, sch in [("layer-z", LAYER_Z), ("C3-cycle", C3CYC)]:
    pi, path = run3(L, none, sch)
    M, spread = loop_area_density(L, path)
    print(f"[1] {name}: bulk identity {np.array_equal(pi, np.arange(L**3))}; "
          f"loop area vector per site M = {fmt(M)} (max deviation over items {spread:.1e})")

# 2. covariance up to cyclic relabelling (exact permutation equalities) -------------------
L = 8
x, y, z = coords3(L)
def site_map(f):
    X_, Y_, Z_ = f(x, y, z); return idx(L, X_, Y_, Z_)
R4z = lambda a, b, c: (-b, a, c)
R4x = lambda a, b, c: (a, -c, b)
R3 = lambda a, b, c: (c, a, b)
C2z = lambda a, b, c: (-a, -b, c)
T1 = lambda a, b, c: (a + 1, b, c)
def matches(sch, f, J):
    """which cyclic phases k satisfy  f pi_J f^-1 == pi^{(k)}_{fJ}"""
    g = site_map(f)
    p0 = run3(L, J, sch)[0]
    J2 = np.zeros_like(J); J2[g] = J
    return [k for k, s in enumerate(shifts(sch)) if np.array_equal(run3(L, J2, s)[0][g], g[p0])]
for name, sch, ops in [("layer-z", LAYER_Z, [("C4z", R4z), ("T_x", T1), ("C4x", R4x)]),
                       ("C3-cycle", C3CYC, [("C3(111)", R3), ("T_x", T1), ("C2z", C2z), ("C4z", R4z)])]:
    out = {}
    for opn, f in ops:
        ks = set()
        good = True
        for trial in range(6):
            J = rng.random(L ** 3) < 0.12
            m = matches(sch, f, J)
            good &= len(m) > 0
            ks |= set(m)
        out[opn] = sorted(ks) if good else "NO phase works"
    print(f"[2] {name}: phases k with  R pi_J R^-1 = pi^(k)_RJ  on 6 random lock patterns: {out}")

# 3. cubic island: circulation half-plane fluxes and per-face currents -------------------
L, s, lo = 16, 6, 5
hi = lo + s - 1; cc = lo + (s - 1) / 2.0
J = cube(L, lo, s)
for name, sch in [("layer-z", LAYER_Z), ("C3-cycle", C3CYC)]:
    pi, path = run3(L, J, sch)
    mv = np.nonzero(pi != np.arange(L ** 3))[0]
    xx, yy, zz = coords3(L)
    dist = np.maximum.reduce([np.maximum(lo - xx[mv], xx[mv] - hi), np.maximum(lo - yy[mv], yy[mv] - hi),
                              np.maximum(lo - zz[mv], zz[mv] - hi)])
    # half-plane circulation fluxes through the island centre line
    Hz = plane_flux(L, pi, 1, cc + 0.3, lambda p: cc + 0.25 < p[0] < cc + L / 2)
    Hx = plane_flux(L, pi, 2, cc + 0.3, lambda p: cc + 0.25 < p[1] < cc + L / 2)
    Hy = plane_flux(L, pi, 0, cc + 0.3, lambda p: cc + 0.25 < p[2] < cc + L / 2)
    print(f"[3] {name}, cube s={s}: moved={len(mv)}, all within distance {int(dist.max())} of the cube; "
          f"half-plane fluxes (Hx,Hy,Hz) = ({Hx},{Hy},{Hz})")
    # per-face mean current: face normal axis a, sign sg; tangents t; middle range of the other tangent
    rows = []
    for a in range(3):
        for sg in (+1, -1):
            face = hi + 0.5 if sg > 0 else lo - 0.5
            K = [0.0, 0.0, 0.0]
            for t in range(3):
                if t == a: continue
                u = 3 - a - t                                   # the other tangent axis
                cond = (lambda p, a=a, sg=sg, face=face, u=u:
                        sg * (p[a] - face) > 0 and sg * (p[a] - face) < 3 and lo + 0.5 < p[u] < hi - 0.5)
                K[t] = plane_flux(L, pi, t, cc + 0.3, cond) / (s - 2)
            rows.append(("+-"[sg < 0] + "xyz"[a], fmt(K)))
    print("     per-face current (items per cycle per unit length):", ", ".join(f"{f}:{k}" for f, k in rows))

# 4. group facts behind the 3D no-go -------------------------------------------------------
O = []
for p in itertools.permutations(range(3)):
    for sgn in itertools.product((1, -1), repeat=3):
        Mx = np.zeros((3, 3), int)
        for i in range(3): Mx[p[i], i] = sgn[i]
        if round(np.linalg.det(Mx)) == 1: O.append(Mx)
key = lambda m: tuple(m.flatten())
comm = {key(np.eye(3, dtype=int))}
frontier = [a @ b @ a.T @ b.T for a in O for b in O]
grp = set()
for c in frontier: grp.add(key(c))
changed = True
while changed:
    changed = False
    for g1 in list(grp):
        for g2 in list(grp):
            k = key(np.array(g1).reshape(3, 3) @ np.array(g2).reshape(3, 3))
            if k not in grp: grp.add(k); changed = True
tr = sorted(int(np.trace(np.array(g).reshape(3, 3))) for g in grp)
print(f"[4] |O| = {len(O)}; commutator subgroup [O,O] has {len(grp)} elements, traces {tr} "
      f"(trace -1 = face C2, 0 = C3, 3 = identity)")
E = [np.array(v) for v in [X, Y, Z]]
killed = all(any((np.array(g).reshape(3, 3) @ e == -e).all() for g in grp) for e in E)
print(f"    every axis vector e is reversed by some element of [O,O]: {killed}")
print(f"time {time.time()-t0:.1f}s")
