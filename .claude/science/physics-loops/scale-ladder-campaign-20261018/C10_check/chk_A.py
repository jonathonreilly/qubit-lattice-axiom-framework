#!/usr/bin/env python3
"""C10 check, Model A.  Independent encoding: every constraint is a quadratic form 1/2 z^T Q z on
z = (phi, X, pi, P); brackets via B = Q Om R - R Om Q (matrix algebra, no differentiation of expressions).
Linear functions are coefficient vectors v (f = v.z) with {v.z, w.z} = v^T Om w."""
import sympy as sp, itertools, random
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

def setup(L, dfun):
    N = 4 * L
    Om = sp.zeros(N, N)
    for i in range(2 * L):
        Om[i, 2 * L + i] = 1; Om[2 * L + i, i] = -1
    Dl = sp.Matrix(L, L, lambda x, y: dfun((y - x) % L))
    def vec(phi=None, X=None, pi=None, P=None):
        v = sp.zeros(N, 1)
        for blk, w in enumerate([phi, X, pi, P]):
            if w is not None:
                for i in range(L): v[blk * L + i] += w[i]
        return v
    e = lambda x: [1 if i == x else 0 for i in range(L)]
    row = lambda x: [Dl[x, y] for y in range(L)]
    neg = lambda r: [-t for t in r]
    a = [vec(pi=e(x), phi=row(x)) for x in range(L)]
    b = [vec(pi=e(x), phi=neg(row(x))) for x in range(L)]
    be = [vec(P=e(x), X=neg(row(x))) for x in range(L)]
    ga = [vec(P=e(x), X=row(x)) for x in range(L)]
    l = [a[x] - be[x] for x in range(L)]; m = [a[x] + be[x] for x in range(L)]
    n = [b[x] - ga[x] for x in range(L)]; k = [b[x] + ga[x] for x in range(L)]
    prod = lambda v, w: (v * w.T + w * v.T)          # quadratic form matrix Q with 1/2 z^T Q z = (v.z)(w.z)
    Cp = [prod(l[x], m[x]) / 4 for x in range(L)]
    Cm = [prod(n[x], k[x]) / 4 for x in range(L)]
    # H and D directly from their definitions
    pi_ = [vec(pi=e(x)) for x in range(L)]; P_ = [vec(P=e(x)) for x in range(L)]
    Dphi = [vec(phi=row(x)) for x in range(L)]; DX = [vec(X=row(x)) for x in range(L)]
    H = [(prod(pi_[x], pi_[x]) + prod(Dphi[x], Dphi[x]) - prod(P_[x], P_[x]) - prod(DX[x], DX[x])) / 2 for x in range(L)]
    Dd = [prod(pi_[x], Dphi[x]) + prod(P_[x], DX[x]) for x in range(L)]
    return dict(Om=Om, Dl=Dl, l=l, m=m, n=n, k=k, Cp=Cp, Cm=Cm, H=H, D=Dd, prod=prod, N=N)

def br(Q, R, Om): return (Q * Om * R - R * Om * Q).applyfunc(sp.expand)
def iszero(M): return all(sp.expand(t) == 0 for t in M)

# ---- (a1) bracket formulas, fully generic circulant, L = 4, 5
for L in (4, 5):
    ds = sp.symbols(f"d0:{L}")
    S_ = setup(L, lambda r: ds[r]); Om, Dl, pr = S_["Om"], S_["Dl"], S_["prod"]
    A = Dl - Dl.T; S = Dl + Dl.T
    okHD = all(iszero(S_["H"][x] - S_["Cp"][x] - S_["Cm"][x]) and iszero(S_["D"][x] - S_["Cp"][x] + S_["Cm"][x]) for x in range(L))
    check(f"A-HD L={L} generic circulant: H = C+ + C-, D = C+ - C-", okHD)
    ok1 = ok2 = ok3 = True
    l, m, n, k = S_["l"], S_["m"], S_["n"], S_["k"]
    for x in range(L):
        for y in range(L):
            ok1 &= iszero(br(S_["Cp"][x], S_["Cp"][y], Om) - A[x, y] * (pr(l[x], m[y]) + pr(m[x], l[y])) / 8)
            ok2 &= iszero(br(S_["Cm"][x], S_["Cm"][y], Om) + A[x, y] * (pr(n[x], k[y]) + pr(k[x], n[y])) / 8)
            ok3 &= iszero(br(S_["Cp"][x], S_["Cm"][y], Om) - S[x, y] * (pr(l[x], k[y]) + pr(m[x], n[y])) / 8)
    check(f"A-br L={L} generic circulant: {{C+,C+}} = A(l m'+m l')/8", ok1)
    check(f"A-br L={L} generic circulant: {{C-,C-}} = -A(n k'+k n')/8", ok2)
    check(f"A-br L={L} generic circulant: {{C+x,C-y}} = S_xy (l_x k_y + m_x n_y)/8", ok3)

# ---- (a2) Theorem A1 strong closure, antisymmetric Delta: general antisymmetric at L=5 (d1,d2) and L=4 (d1);
#      then specialise to SLAC L=5 and central.  Polynomial identity m_x m_y {C+x,C+y} = D_xy (m_y^2 C+x + m_x^2 C+y).
def polyform(Q, zs): return sp.expand((sp.Matrix(zs).T * Q * sp.Matrix(zs))[0] / 2)
def lin(v, zs): return sp.expand((v.T * sp.Matrix(zs))[0])
for L, dfun, lab in [(5, None, "general antisym (d1,d2)"), (4, None, "general antisym (d1)")]:
    d1, d2 = sp.symbols("d1 d2")
    if L == 5: dd = {1: d1, 4: -d1, 2: d2, 3: -d2}
    else: dd = {1: d1, 3: -d1}
    S_ = setup(L, lambda r: dd.get(r, 0)); Om, Dl = S_["Om"], S_["Dl"]
    zs = sp.symbols(f"z0:{4 * L}")
    ok = True
    for x in range(L):
        for y in range(L):
            ok &= iszero(br(S_["Cp"][x], S_["Cm"][y], Om))
            mx, my = lin(S_["m"][x], zs), lin(S_["m"][y], zs); nx, ny = lin(S_["n"][x], zs), lin(S_["n"][y], zs)
            lhs = polyform(br(S_["Cp"][x], S_["Cp"][y], Om), zs) * mx * my
            rhs = Dl[x, y] * (my**2 * polyform(S_["Cp"][x], zs) + mx**2 * polyform(S_["Cp"][y], zs))
            ok &= sp.expand(lhs - rhs) == 0
            lhs = polyform(br(S_["Cm"][x], S_["Cm"][y], Om), zs) * nx * ny
            rhs = -Dl[x, y] * (ny**2 * polyform(S_["Cm"][x], zs) + nx**2 * polyform(S_["Cm"][y], zs))
            ok &= sp.expand(lhs - rhs) == 0
    check(f"A1 L={L} {lab}: {{C+,C-}}=0 and strong closure with m_y/m_x, n_y/n_x structure functions", ok)
# SLAC L=5 explicitly (exact trig numbers); d(r) = (1/L) sum_n lam_n w^{-n r}, lam_n = i 2 pi nbar / L
L = 5
w = sp.exp(2 * sp.pi * sp.I / L)
nbar = lambda n: n if n <= L // 2 else n - L
lamS = [sp.I * 2 * sp.pi * nbar(n) / L for n in range(L)]
dS = [sp.nsimplify(sp.simplify(sp.expand_complex(sum(lamS[n] * w**(-n * r) for n in range(L)) / L))) for r in range(L)]
dSn = [sp.N(t, 30) for t in dS]
check("SLAC L=5 real-space kernel is real antisymmetric with d(0)=0", abs(dSn[0]) < 1e-25 and abs(sp.im(dSn[1])) < 1e-25 and abs(dSn[1] + dSn[4]) < 1e-25 and abs(dSn[2] + dSn[3]) < 1e-25,
      f"d1={sp.re(dSn[1]):.12f} d2={sp.re(dSn[2]):.12f}")
# A1 at SLAC: identity is polynomial in (d1,d2), so it specialises; check numerically too at a random point
S_ = setup(L, lambda r: sp.re(dSn[r]) if r else 0); Om, Dl = S_["Om"], S_["Dl"]
random.seed(3)
zv = [sp.Float(random.uniform(-1, 1), 30) for _ in range(4 * L)]
mx = [lin(S_["m"][x], zv) for x in range(L)]
err = 0
for x in range(L):
    for y in range(L):
        lhs = polyform(br(S_["Cp"][x], S_["Cp"][y], Om), zv)
        rhs = Dl[x, y] * (mx[y] / mx[x] * polyform(S_["Cp"][x], zv) + mx[x] / mx[y] * polyform(S_["Cp"][y], zv))
        err = max(err, abs(lhs - rhs))
        err = max(err, max(abs(t) for t in br(S_["Cp"][x], S_["Cm"][y], Om)))
check("A1 SLAC L=5 numerical spot check (30 digits)", err < 1e-20, f"max err {float(err):.1e}")

# ---- (a3) Sigma cap U = {l=0,k=0}: regular (rank 2L) and Lagrangian for antisymmetric; forward not Lagrangian
for L, dd, lab, expectLag in [(5, {1: sp.Rational(1, 2), 4: -sp.Rational(1, 2)}, "central", True),
                              (5, {1: sp.Symbol("d1"), 4: -sp.Symbol("d1"), 2: sp.Symbol("d2"), 3: -sp.Symbol("d2")}, "general antisym", True),
                              (5, {1: 1, 0: -1}, "forward", False), (4, {1: sp.Rational(1, 2), 3: -sp.Rational(1, 2)}, "central", True)]:
    S_ = setup(L, lambda r: dd.get(r, 0)); Om = S_["Om"]
    V = sp.Matrix.hstack(*(S_["l"] + S_["k"])).T
    rk = V.rank(); Pm = (V * Om * V.T).applyfunc(sp.expand)
    lag = iszero(Pm)
    check(f"SigmaU L={L} {lab}: rank(l,k) = 2L = {2*L} and Lagrangian = {expectLag}", rk == 2 * L and lag == expectLag, f"rank={rk}")
    # on {l=k=0}: sum_x m_x = 0 and sum_x n_x = 0 (so a uniform nonzero m needs a winding sector)
    ns = V.nullspace()
    msum = sum((S_["m"][x] for x in range(L)), sp.zeros(4*L,1)); nsum = sum((S_["n"][x] for x in range(L)), sp.zeros(4*L,1))
    okw = all(sp.expand((msum.T * v)[0]) == 0 and sp.expand((nsum.T * v)[0]) == 0 for v in ns)
    check(f"SigmaU L={L} {lab}: periodic sector, sum_x m_x = sum_x n_x = 0 on {{l=k=0}} (uniform m needs winding)", okw)
    if L == 5 and lab == "central":
        # U nonempty: a point with l=k=0, all m_x, n_x != 0
        c = sp.Matrix(sp.symbols(f"c0:{len(ns)}"))
        pt = sum((ci * v for ci, v in zip([3, -1, 2, 5, -4, 1, 7, -2, 3, 11][:len(ns)], ns)), sp.zeros(4 * L, 1))
        vals = [(S_["m"][x].T * pt)[0] for x in range(L)] + [(S_["n"][x].T * pt)[0] for x in range(L)]
        check("SigmaU L=5 central: U cap Sigma nonempty (explicit point with all m,n != 0)", all(v != 0 for v in vals), str(vals))

# ---- (a4) uniform-background Dirac algebra, from the A1 structure functions, at m = mb, n = nb
L = 5
d1, d2 = sp.symbols("d1 d2")
dd = {1: d1, 4: -d1, 2: d2, 3: -d2}
Dl = sp.Matrix(L, L, lambda x, y: dd.get((y - x) % L, 0))
cp = sp.symbols(f"cp0:{L}"); cm = sp.symbols(f"cm0:{L}"); mb, nb = sp.symbols("mb nb")
Hs = [cp[x] + cm[x] for x in range(L)]; Ds = [cp[x] - cm[x] for x in range(L)]
PP = lambda x, y: Dl[x, y] * (mb / mb * cp[x] + mb / mb * cp[y])      # {C+x,C+y} at uniform m
MM = lambda x, y: -Dl[x, y] * (nb / nb * cm[x] + nb / nb * cm[y])
ok = True
for x in range(L):
    for y in range(L):
        HH = PP(x, y) + MM(x, y)          # {C+ + C-, C+ + C-}, {C+,C-}=0
        DH = PP(x, y) - MM(x, y)          # {C+ - C-, C+ + C-}
        DD = PP(x, y) + MM(x, y)
        ok &= sp.expand(HH - Dl[x, y] * (Ds[x] + Ds[y])) == 0 and sp.expand(DH - Dl[x, y] * (Hs[x] + Hs[y])) == 0 \
              and sp.expand(DD - Dl[x, y] * (Ds[x] + Ds[y])) == 0
check("A5 uniform background: {H,H} = Del(D+D), {D,H} = Del(H+H), {D,D} = Del(D+D)", ok)
# Fourier: {D_0, H_n} = lam_n H_n and {H_1,H_-1} = (lam_-1 - lam_1) D_0, with lam_n = sum_r d(r) w^{n r}
wv = sp.Symbol("w")
def four(coef_fun, L, wv):
    return coef_fun
for lab, ddn in [("central", {1: sp.Rational(1, 2), L - 1: -sp.Rational(1, 2)}), ("SLAC", {r: dS[r] for r in range(1, L)})]:
    Dn = sp.Matrix(L, L, lambda x, y: ddn.get((y - x) % L, 0))
    ww = sp.exp(2 * sp.pi * sp.I / L)
    lam = [sum(ddn.get(r, 0) * ww**(n * r) for r in range(L)) for n in range(L)]
    # coefficient of H_y (as w^{n y}) in {D_0,H_n} = sum_{x,y} w^{n y} Dn[x,y] (H_x + H_y) -> project on H_0 component
    Lam = []
    for nn in range(L):
        c0 = sum(ww**(nn * y) * Dn[0, y] for y in range(L)) + sum(Dn[x, 0] for x in range(L))   # coefficient of H_0
        Lam.append(sp.N(c0, 30))
    okL = all(abs(Lam[nn] - sp.N(lam[nn], 30)) < 1e-25 for nn in range(L))
    c11 = sp.N(sum(ww**(1 * 0) * ww**(-1 * y) * Dn[0, y] for y in range(L)) + sum(ww**(1 * x) * Dn[x, 0] for x in range(L)), 30)  # coeff of D_0 in {H_1,H_-1}
    r21 = Lam[2] / Lam[1]
    target = 2 * sp.cos(2 * sp.pi / L) if lab == "central" else 2
    check(f"A5 Fourier {lab} L=5: Lambda_n = lam_n, {{H_1,H_-1}} coefficient of D_0 = {sp.N(c11,8)} != 0, Lam2/Lam1 = {sp.N(r21,10)}",
          okL and abs(c11) > 1e-6 and abs(r21 - sp.N(target, 30)) < 1e-20)

# ---- (a5) A3 kink-rule spot checks
def component(S_, L, cp_choice, cm_choice):
    eqs = [(S_["l"][x] if cp_choice[x] == 0 else S_["m"][x]) for x in range(L)] + [(S_["n"][x] if cm_choice[x] == 0 else S_["k"][x]) for x in range(L)]
    V = sp.Matrix.hstack(*eqs).T
    ns = V.nullspace()
    t = sp.symbols(f"t0:{len(ns)}")
    pt = sum((ti * v for ti, v in zip(t, ns)), sp.zeros(4 * L, 1))
    return pt, t
def val(Q, pt): return sp.expand((pt.T * Q * pt)[0] / 2)
def lv(v, pt): return sp.expand((v.T * pt)[0])
# central L=4, C+ kink at sites 0|1 (l0=0, m1=0, l2=0, l3=0), C- uniform k=0
L = 4
S_ = setup(L, lambda r: {1: sp.Rational(1, 2), 3: -sp.Rational(1, 2)}.get(r, 0)); Om, Dl = S_["Om"], S_["Dl"]; A = Dl - Dl.T
pt, t = component(S_, L, [0, 1, 0, 0], [1, 1, 1, 1])
b01 = val(br(S_["Cp"][0], S_["Cp"][1], Om), pt)
pred = A[0, 1] * lv(S_["m"][0], pt) * lv(S_["l"][1], pt) / 8
cons_ok = all(val(Q, pt) == 0 for Q in S_["Cp"] + S_["Cm"])
check("A3 central L=4 kink component (l,m,l,l | k,k,k,k): on it {C+_0,C+_1} = A_01 m_0 l_1 / 8, not identically 0",
      cons_ok and sp.expand(b01 - pred) == 0 and b01 != 0, f"= {sp.factor(b01)}")
# all anomalous pairs on that component: only the kink pairs (0,1),(1,2) ... list them
bad = [(i, j) for i in range(2 * L) for j in range(i + 1, 2 * L) if val(br((S_["Cp"] + S_["Cm"])[i], (S_["Cp"] + S_["Cm"])[j], Om), pt) != 0]
check("A3 central L=4 same component: non-vanishing brackets only between C+ at the kink sites", set(bad) == {(0, 1), (1, 2)}, str(bad))
# a C- kink at L=5 central: anomaly -A n_x k_y/8 form, i.e. -1/8 A_xy (n_x k_y + k_x n_y)
L = 5
S_ = setup(L, lambda r: {1: sp.Rational(1, 2), 4: -sp.Rational(1, 2)}.get(r, 0)); Om, Dl = S_["Om"], S_["Dl"]; A = Dl - Dl.T
pt, t = component(S_, L, [0] * 5, [1, 1, 0, 1, 1])     # l everywhere; C- : k,k,n,k,k
b = val(br(S_["Cm"][1], S_["Cm"][2], Om), pt); pred = -A[1, 2] * lv(S_["n"][1], pt) * lv(S_["k"][2], pt) / 8
check("A3 central L=5 C- kink (k,k,n,k,k): {C-_1,C-_2} = -A_12 n_1 k_2/8 != 0 (C- kinks carry the mirrored form, not A m l/8)",
      sp.expand(b - pred) == 0 and b != 0)
# forward L=5: regular branches (l,k) and (m,n) anomalous via S; reducible (l,n) first class
S_ = setup(L, lambda r: {1: 1, 0: -1}.get(r, 0)); Om, Dl = S_["Om"], S_["Dl"]; S = Dl + Dl.T
pt, t = component(S_, L, [0] * 5, [1] * 5)
b = val(br(S_["Cp"][0], S_["Cm"][1], Om), pt); pred = S[0, 1] * lv(S_["m"][0], pt) * lv(S_["n"][1], pt) / 8
check("A3 forward L=5 regular (l,k) branch: {C+_0,C-_1} = S_01 m_0 n_1/8 != 0", sp.expand(b - pred) == 0 and b != 0)
pt, t = component(S_, L, [1] * 5, [0] * 5)
b = val(br(S_["Cp"][0], S_["Cm"][1], Om), pt); pred = S[0, 1] * lv(S_["l"][0], pt) * lv(S_["k"][1], pt) / 8
check("A3 forward L=5 regular (m,n) branch: {C+_0,C-_1} = S_01 l_0 k_1/8 != 0", sp.expand(b - pred) == 0 and b != 0)
pt, t = component(S_, L, [0] * 5, [0] * 5)
allC = S_["Cp"] + S_["Cm"]
okfc = all(val(br(allC[i], allC[j], Om), pt) == 0 for i in range(2 * L) for j in range(i + 1, 2 * L))
V = sp.Matrix.hstack(*(S_["l"] + S_["n"])).T
check("A3 forward L=5 (l,n) branch first class, reducible (rank < 2L)", okfc and V.rank() < 2 * L, f"rank={V.rank()}")
print(f"TOTAL chk_A: PASS={PASS} FAIL={FAIL}")
