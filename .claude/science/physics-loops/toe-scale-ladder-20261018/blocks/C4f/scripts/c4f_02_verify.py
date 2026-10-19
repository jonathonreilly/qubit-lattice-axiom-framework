#!/usr/bin/env python3
"""C4f verification of the construction U = L2 o L1 (see c4f_core docstring).

usage: c4f_02_verify.py SECTION   with SECTION in
  inv_sparse  exhaustive involution checks on Z^3 (sparse code): all k<=3 configurations in the
              4^3 box, all k=4 in the 3^3 box; U^-1 U = id on the same sets
  inv_dense   torus L=10,12 (dense code): random densities, stress (packed candidate units of all
              kinds, empty/full/half-space/slab backgrounds); L1^2 = L2^2 = id, U^-1 U = id;
              agreement sparse(wrapped) vs dense on every stress configuration
  sym         TI; N conservation; covariance under all 24 R in O with the axis action
              (T: P_R; odd: P_R o C), with the explicit SU(2) phases; witnesses that U P_R != P_R U
              for odd R and U C != C U (so the C4e mechanism is not what makes it work)
  sectors     single magnon / single hole frozen; all magnon pairs |rho|<=6 on Z^3 (glider
              prediction v = rho_b rho_c e_a for face pairs, static otherwise); all hole pairs
              |rho|<=4 in the full background on the L=12 torus (prediction v = -rho_b rho_c e_a)
  radius      exact per-layer dependency radius from the definition; empirical flip influence
Each section prints PASS/FAIL lines and 'TOTAL: PASS=<n> FAIL=<n>'.
"""
import sys, os, time, itertools, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4f_core as C
import c4f_dense as Dn

P = F = 0
def check(name, ok, info=''):
    global P, F
    if ok: P += 1; print('PASS', name, info, flush=True)
    else: F += 1; print('FAIL', name, info, flush=True)

O = C.build_O()
ODD = [i for i, M in enumerate(O) if C.perm_sign(M) == -1]

def face_v(rho):
    """C4e prediction: face pair with zero coordinate a, nonzero b, c moves by rho_b rho_c e_a."""
    z = [i for i in range(3) if rho[i] == 0]
    if len(z) != 1 or any(abs(v) != 1 for v in rho if v): return None
    a = z[0]; b, c = [i for i in range(3) if i != a]
    v = [0, 0, 0]; v[a] = rho[b] * rho[c]; return tuple(v)

# ---------------------------------------------------------------- helpers for dense configs
def stress_config(DU, rng, bg, nplace):
    T = DU.T; L = T.L
    if bg == 'empty': c = np.zeros(T.V, bool)
    elif bg == 'full': c = np.ones(T.V, bool)
    elif bg == 'half': c = T.coords[:, 2] >= L // 2
    elif bg == 'slab': c = (T.coords[:, 0] % 5) < 2
    else: c = rng.random(T.V) < 0.5
    c = c.copy()
    lays = [DU.L1, DU.L2]
    for _ in range(nplace):
        lay = lays[rng.integers(2)]; u = rng.integers(lay['n'])
        st = rng.integers(2)
        D = lay['D'][u]; Dp = lay['Dp'][u]
        c[D] = bool(st == 0); c[Dp] = bool(st == 1)
        ctl = lay['ctl'][u]
        if ctl == 1: c[lay['G'][u]] = False
        if ctl == 2: c[lay['G'][u]] = True
    return c

def nplace_draw(rng, V):
    """log-uniform number of unit placements in [3, V/8]"""
    return int(np.exp(rng.uniform(np.log(3), np.log(V / 8))))

def to_set(T, c):
    return frozenset(tuple(int(v) for v in T.coords[i]) for i in np.nonzero(c)[0])

def perm_R(T, M):
    """site permutation index array: (P_R c)[R x] = c[x]  ->  new = c[inv]"""
    img = T.idx((T.coords @ np.array(M).T))
    inv = np.empty(T.V, int); inv[img] = np.arange(T.V)
    return inv

# ======================================================================== sections
def inv_sparse():
    U = C.Dyn()
    t0 = time.time()
    box4 = list(itertools.product(range(4), repeat=3))
    box3 = list(itertools.product(range(3), repeat=3))
    confs = [frozenset(s) for k in range(4) for s in itertools.combinations(box4, k)]
    confs += [frozenset(s) for s in itertools.combinations(box3, 4)]
    bad1 = bad2 = badU = 0; moved = 0
    for c in confs:
        a = U.L1.apply(c); b = U.L2.apply(c)
        bad1 += U.L1.apply(a) != c; bad2 += U.L2.apply(b) != c
        u = U(c); badU += U.inv(u) != c; moved += u != c
        if len(u) != len(c): badU += 1
    check(f'Z^3: L1^2 = L2^2 = id and U^-1 U = id, N conserved, on {len(confs)} configs '
          f'(all k<=3 in 4^3 box + all k=4 in 3^3 box)', bad1 == bad2 == badU == 0,
          f'[bad {bad1},{bad2},{badU}; {moved} configs moved by U; {time.time()-t0:.0f}s]')

def inv_dense():
    rng = np.random.default_rng(20261019)
    for L in (10, 12):
        DU = Dn.DenseU(L); T = DU.T
        wrap = (lambda L: (lambda z: (z[0] % L, z[1] % L, z[2] % L)))(L)
        SU = C.Dyn(wrap)
        t0 = time.time()
        nb = 0; ncfg = 0; ncross = 0; nA = nB = 0; nagree_bad = 0; nsp = 0
        for p in (0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.98):
            for _ in range(6 if L == 10 else 3):
                c = rng.random(T.V) < p
                a, x1 = Dn.apply(DU.L1, c, True); b, x2 = Dn.apply(DU.L2, a, True)
                nb += not np.array_equal(Dn.apply(DU.L1, a), c)
                nb += not np.array_equal(Dn.apply(DU.L2, b), a)
                ncfg += 1; ncross += len(x1) + len(x2)
        bgs = ['empty', 'full', 'half', 'slab', 'rand']
        nst = 60 if L == 10 else 25
        for bg in bgs:
            for i in range(nst):
                c = stress_config(DU, rng, bg, nplace_draw(rng, T.V))
                a, x1 = Dn.apply(DU.L1, c, True); b, x2 = Dn.apply(DU.L2, a, True)
                c1 = Dn.apply(DU.L2, c)
                nb += not np.array_equal(Dn.apply(DU.L1, a), c)
                nb += not np.array_equal(Dn.apply(DU.L2, b), a)
                nb += not np.array_equal(Dn.apply(DU.L2, c1), c)
                ncfg += 1; ncross += len(x1) + len(x2)
                kinds = DU.L2['ctl'][x2]; nB += int((kinds == 1).sum()); nA += int((kinds == 2).sum())
                if i < (8 if L == 10 else 3):      # sparse cross-implementation agreement
                    nsp += 1
                    nagree_bad += SU(to_set(T, c)) != to_set(T, b)
        check(f'torus L={L}: L1^2 = L2^2 = id on {ncfg} configs (random p in [0.02,0.98] + stress on '
              f'empty/full/half/slab/rand backgrounds)', nb == 0,
              f'[{ncross} active-unit crossings, of which L2: {nB} B-type, {nA} A-type; {time.time()-t0:.0f}s]')
        check(f'torus L={L}: stress exercises both L2 kinds (>=100 crossings each)', nA >= 100 and nB >= 100)
        check(f'torus L={L}: sparse (c4f_core) == dense (c4f_dense) on {nsp} stress configs', nagree_bad == 0)

def sym():
    rng = np.random.default_rng(7)
    L = 10; DU = Dn.DenseU(L); T = DU.T
    cfgs = [stress_config(DU, rng, bg, nplace_draw(rng, T.V))
            for bg in ('empty', 'full', 'half', 'slab', 'rand') for _ in range(40)]
    acts = 0
    imgs = []
    for c in cfgs:
        a, x1 = Dn.apply(DU.L1, c, True); b, x2 = Dn.apply(DU.L2, a, True); acts += len(x1) + len(x2)
        imgs.append(b)
    # N conservation and TI
    check('N conserved on all stress configs', all(c.sum() == b.sum() for c, b in zip(cfgs, imgs)))
    okT = True
    for s in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (3, -2, 5)):
        sh = T.idx(T.coords - np.array(s))       # (S c)[x] = c[x - s]
        for c, b in zip(cfgs[:12], imgs[:12]):
            okT &= np.array_equal(DU(c[sh]), b[sh])
    check('translation invariance (4 shifts x 12 configs)', okT)
    # point group with axis action
    from c4f_su2 import su2_lift, Bn
    okR = []; okph = True
    for i, M in enumerate(O):
        inv = perm_R(T, M); odd = i in ODD
        ok = True
        for c, b in zip(cfgs, imgs):
            Mc = c[inv]; Mb = b[inv]
            if odd: Mc = ~Mc; Mb = ~Mb
            ok &= np.array_equal(DU(Mc), Mb)
        okR.append(ok)
        # explicit phases: beta_R|c> = prod_x D_n[c'(Rx), c(x)] |c'>;  amplitude depends on c via N only
        Qm = C.perm_sign(M) * np.abs(M); Dm = Bn.conj().T @ su2_lift(Qm) @ Bn   # index 0 magnon
        def amp(c):
            n1 = int(c.sum()); n0 = T.V - n1
            if odd: return Dm[1, 0] ** n1 * Dm[0, 1] ** n0
            return Dm[0, 0] ** n1 * Dm[1, 1] ** n0
        for c, b in zip(cfgs, imgs):
            okph &= abs(amp(c) - amp(b)) < 1e-9
    check(f'U M_R = M_R U for all 12 R in T (M_R = P_R) on 200 stress configs [{acts} crossings]',
          all(okR[i] for i in range(24) if i not in ODD))
    check('U M_R = M_R U for all 12 odd R (M_R = P_R o C) on 200 stress configs', all(okR[i] for i in ODD))
    check('explicit SU(2) amplitudes of beta_R agree on c and Uc (all 24 R): beta_R U = U beta_R exactly', okph)
    # witnesses: C4e-style symmetry fails here
    pair = np.zeros(T.V, bool); pair[T.idx([(0, 0, 0), (1, 1, 0)])] = True
    nfail = 0
    for i in ODD:
        inv = perm_R(T, O[i])
        nfail += not np.array_equal(DU(pair[inv]), DU(pair)[inv])
    check('witness: U P_R != P_R U for all 12 odd R (pure permutation is NOT a symmetry)', nfail == 12)
    check('witness: U C != C U (U is not particle-hole symmetric, unlike C4e)',
          not np.array_equal(DU(~pair), ~DU(pair)))

def sectors():
    U = C.Dyn()
    one = frozenset({(0, 0, 0)})
    check('single magnon fixed by U and U^-1 (Z^3; TI gives all sites)', U(one) == one and U.inv(one) == one)
    L = 12; DU = Dn.DenseU(L); T = DU.T
    full = np.ones(T.V, bool)
    okh = True
    for x in T.coords[::97]:
        c = full.copy(); c[T.idx(x)] = False
        okh &= np.array_equal(DU(c), c) and np.array_equal(DU.inv(c), c)
    check('single hole in the full background fixed by U and U^-1 (torus L=12, 18 sites)', okh)
    check('vacuum and antivacuum fixed', np.array_equal(DU(full), full) and not DU(~full).any())
    # magnon pairs on Z^3
    r = 6; nmov = nstat = bad = 0
    for rho in itertools.product(range(-r, r + 1), repeat=3):
        if rho <= (0, 0, 0): continue
        c = frozenset({(0, 0, 0), rho}); v = face_v(rho)
        x = c; ok = True
        for t in range(3):
            x = U(x)
            exp = c if v is None else frozenset(C.add(z, tuple((t + 1) * vi for vi in v)) for z in c)
            ok &= x == exp
        bad += not ok
        if v is None: nstat += 1
        else: nmov += 1
    check(f'all {nmov + nstat} magnon pairs |rho|<=6: face pairs glide by v = rho_b rho_c e_a for 3 ticks, '
          f'all others static (prediction = C4e glider)', bad == 0 and nmov == 6, f'[{nmov} moving, {nstat} static]')
    # hole pairs on the torus, full background
    r = 4; hmov = hstat = hbad = 0
    for rho in itertools.product(range(-r, r + 1), repeat=3):
        if rho <= (0, 0, 0): continue
        v = face_v(rho)
        c = full.copy(); c[T.idx([(0, 0, 0), rho])] = False
        x = c; ok = True
        for t in range(3):
            x = DU(x)
            sh = (0, 0, 0) if v is None else tuple(-(t + 1) * vi for vi in v)
            e = full.copy(); e[T.idx([sh, C.add(rho, sh)])] = False
            ok &= np.array_equal(x, e)
        hbad += not ok
        if v is None: hstat += 1
        else: hmov += 1
    check(f'all {hmov + hstat} hole pairs |rho|<=4 (torus L=12, full background): face hole pairs glide by '
          f'-rho_b rho_c e_a (declared prediction from Theta-covariance), others static',
          hbad == 0 and hmov == 6, f'[{hmov} moving, {hstat} static]')

def radius():
    for name, lay in (('L1', C.Layer(('sq',))), ('L2', C.Layer(('B', 'A')))):
        rmax = 0
        x = (0, 0, 0)
        for u in C._units_S_at(lay.kinds, x):
            dep = set()
            for w in [u] + list(lay._N1_raw(u)) + list(lay._N2_raw(u)):
                D, Dp, G, _ = C.unit_geom(w); dep |= set(D) | set(Dp) | set(G)
            rmax = max(rmax, max(max(abs(v) for v in z) for z in dep))
        print(f'{name}: exact dependency radius (sites read to decide site 0) = {rmax}')
        globals()['R_' + name] = rmax
    check('per-layer dependency radius computed (L1 = 3 as in C4e)', R_L1 == 3, f'[L1 {R_L1}, L2 {R_L2}]')
    # empirical single-flip influence on stress configs (torus L=12)
    rng = np.random.default_rng(3)
    DU = Dn.DenseU(12); T = DU.T
    emp = {'L1': 0, 'L2': 0, 'U': 0}
    for it in range(60):
        c = stress_config(DU, rng, ('empty', 'full', 'half', 'slab')[it % 4], int(rng.integers(30, 200)))
        outs = {'L1': Dn.apply(DU.L1, c), 'L2': Dn.apply(DU.L2, c), 'U': DU(c)}
        for j in rng.choice(T.V, 25, replace=False):
            c2 = c.copy(); c2[j] = ~c2[j]
            o2 = {'L1': Dn.apply(DU.L1, c2), 'L2': Dn.apply(DU.L2, c2), 'U': DU(c2)}
            for k in emp:
                diff = np.nonzero(outs[k] != o2[k])[0]
                for d in diff:
                    if d == j: continue
                    dz = (T.coords[d] - T.coords[j] + 6) % 12 - 6
                    emp[k] = max(emp[k], int(np.abs(dz).max()))
    print('empirical single-flip influence radius:', emp)
    check('empirical influence within proved bounds (L_i <= exact radius, U <= R_L1 + R_L2)',
          emp['L1'] <= R_L1 and emp['L2'] <= R_L2 and emp['U'] <= R_L1 + R_L2)

if __name__ == '__main__':
    sec = sys.argv[1]
    {'inv_sparse': inv_sparse, 'inv_dense': inv_dense, 'sym': sym, 'sectors': sectors, 'radius': radius}[sec]()
    print(f'TOTAL: PASS={P} FAIL={F}')
