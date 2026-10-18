#!/usr/bin/env python3
"""C10: lattice Hamiltonian constraints with field-dependent structure functions (1D, periodic).

Supplied models only (free scalar phi,pi; clock/embedding pairs).  No physical identification.
All checks exact (sympy over QQ, QQ(symbols), cyclotomic reduction).  New code; imports nothing
from earlier campaign runners.

Parts
  F  framework lemmas: momentum-linear constraints (frame / Frobenius), Kuchar form, recombination
  A  Model A: one clock pair (X,P), 4L-dim, string-type H,D  (zero local dof)
  P  Model P: lattice parametrised field theory, two embedding pairs (X+-,Pi+-), 6L-dim
     P1-P3 naive anomaly; P4-P5 Groebner certificates over finite-range ansatze; P6 X-independent clocks
Usage:  python3 c10_runner.py [--slow]
"""
import sys, itertools, time
import sympy as sp

SLOW = "--slow" in sys.argv
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    sys.stdout.flush()

T0 = time.time()

# ------------------------------------------------------------------ difference operators
def circ(L, d):
    """circulant Delta_xy = d(y-x)"""
    D = sp.zeros(L, L)
    for x in range(L):
        for r, v in d.items():
            D[x, (x + r) % L] += v
    return D
FWD = {1: 1, 0: -1}
CEN = {1: sp.Rational(1, 2), -1: -sp.Rational(1, 2)}

def pb_canon(f, g, Q, P):
    return sp.expand(sum(sp.diff(f, q) * sp.diff(g, p) - sp.diff(f, p) * sp.diff(g, q) for q, p in zip(Q, P)))

def cyclo_eq(e1, e2, w, L):
    return sp.rem(sp.expand(e1 - e2), sp.cyclotomic_poly(L, w), w) == 0

# ================================================================== Part F
print("=== Part F: framework lemmas")
# F1 Frobenius: constraints <p,V_a> are first class iff the distribution span V is involutive.
x, y, z, px, py, pz = sp.symbols("x y z px py pz")
Q3, P3 = [x, y, z], [px, py, pz]
C1, C2 = px, py + x * pz              # V1 = d_x, V2 = d_y + x d_z ; [V1,V2] = d_z not in span
br = pb_canon(C1, C2, Q3, P3)
on = br.subs({px: 0, py: -x * pz})
check("F1a non-involutive momentum-linear pair is NOT first class", sp.simplify(on - pz) == 0 and on != 0, f"{{C1,C2}}|_Sigma = {on}")
C2b = py + x * px                     # V2 = d_y + x d_x, [V1,V2] = d_x in span
br = pb_canon(C1, C2b, Q3, P3)
check("F1b involutive pair is first class (bracket = structure fn * constraint)", sp.expand(br - C1) == 0, f"{{C1,C2}} = {br}")
# F2 frame: n momentum-linear constraints with V a frame on R^n => Sigma = zero section => automatically first class
q = sp.symbols("q0:3"); p = sp.symbols("k0:3")
V = [[1, q[2], q[0]**2], [0, 1, q[1]], [0, 0, 1]]           # unit upper-triangular: a frame everywhere
Cs = [sum(V[a][i] * p[i] for i in range(3)) for a in range(3)]
ok = all(sp.expand(pb_canon(Cs[a], Cs[b], q, p).subs({pi_: 0 for pi_ in p})) == 0 for a in range(3) for b in range(3))
check("F2 frame (n momentum-linear constraints, n-dim base) is first class automatically", ok)
# F3 Kuchar form: K_x = P_x + h_x(X, z): {K_x,K_y} is P-independent  => weak = strong vanishing
Xs = sp.symbols("X0:3"); Ps = sp.symbols("P0:3"); fz, pz_ = sp.symbols("fz pz_")
hs = [Xs[0] * fz**2 + pz_ * Xs[1], Xs[1]**2 * pz_ + fz * Xs[2], fz * pz_ * Xs[0] * Xs[2]]
Ks = [Ps[i] + hs[i] for i in range(3)]
Qa, Pa = list(Xs) + [fz], list(Ps) + [pz_]
ok = all(not any(pb_canon(Ks[i], Ks[j], Qa, Pa).has(pp) for pp in Ps) for i in range(3) for j in range(3))
check("F3 Kuchar-form brackets are independent of the clock momenta (first class <=> strongly abelian)", ok)
# F4 recombination with a ruler: C_x = g_x K_x, g = 1 + Delta u, K abelian (and Pi-free h)
#     {C_x,C_y} = Delta_xy (g_y/g_x) C_x - Delta_yx (g_x/g_y) C_y   strongly on {g != 0}
for L, dname, d in [(5, "cen", CEN), (5, "fwd", FWD), (6, "cen", CEN)]:
    D = circ(L, d)
    u = sp.symbols(f"u0:{L}"); Pi = sp.symbols(f"Pi0:{L}"); f = sp.symbols(f"f0:{L}"); pf = sp.symbols(f"pf0:{L}")
    g = [1 + sum(D[i, j] * u[j] for j in range(L)) for i in range(L)]
    K = [Pi[i] + pf[i]**2 / 2 for i in range(L)]           # abelian K (h_x = pi_x^2/2 commute)
    C = [sp.expand(g[i] * K[i]) for i in range(L)]
    QQ_, PP_ = list(u) + list(f), list(Pi) + list(pf)
    ok = True
    for i in range(L):
        for j in range(L):
            lhs = pb_canon(C[i], C[j], QQ_, PP_)
            rhs = D[i, j] * g[j] * K[i] - D[j, i] * g[i] * K[j]
            ok &= sp.expand(lhs - rhs) == 0
    check(f"F4a recombination identity C=gK, L={L} {dname}", ok)
# F4b zeroth-order constants at g = 1:  c(m,n) = lam_n - lam_m,  Lambda_n = lam_n ; (S) holds; central: Lam2/Lam1 = 2cos(2pi/L)
w = sp.Symbol("w")
for L in range(4, 10):
    lam = lambda n, d: sp.expand(sum(v * w**((n * r) % L) for r, v in d.items()))
    okS = True
    for d, dn in [(CEN, "cen"), (FWD, "fwd")]:
        # Fourier of C_xy^x = Delta_xy, C_xy^y = -Delta_yx at g=1:  {C_m,C_n} = (lam_n - lam_m) C_{m+n}
        D = circ(L, d)
        for m_ in range(L):
            for n_ in range(L):
                # coefficient of C_x in sum_{x,y} w^{m x + n y} (Delta_xy C_x - Delta_yx C_y), at x = 0 (translation covariance)
                c0 = sum(w**((n_ * yy) % L) * D[0, yy] for yy in range(L)) - sum(w**((m_ * xx) % L) * D[xx, 0] for xx in range(L))
                okS &= cyclo_eq(c0, lam(n_, d) - lam(m_, d), w, L)
        l1, lm1 = lam(1, d), lam(L - 1, d)
        okS &= not cyclo_eq(l1, 0, w, L) and not cyclo_eq(l1, lm1, w, L)
    # central: Lam2 = (w + w^-1) Lam1
    okS &= cyclo_eq(lam(2, CEN), sp.expand((w + w**(L - 1)) * lam(1, CEN)), w, L)
    check(f"F4b L={L}: c(m,n)=lam_n-lam_m, (S) holds (cen, fwd), cen Lam2/Lam1 = w+1/w = 2cos(2pi/L)", okS)

# ================================================================== Part A
print("=== Part A: one clock pair (X,P): H = (pi^2+(Dphi)^2)/2 - (P^2+(DX)^2)/2, D = pi Dphi + P DX")
def modelA(L, D):
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}"); X = sp.symbols(f"X0:{L}"); P = sp.symbols(f"P0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    DX = [sum(D[i, j] * X[j] for j in range(L)) for i in range(L)]
    a = [p_[i] + Df[i] for i in range(L)]; b = [p_[i] - Df[i] for i in range(L)]
    be = [P[i] - DX[i] for i in range(L)]; ga = [P[i] + DX[i] for i in range(L)]
    l = [sp.expand(a[i] - be[i]) for i in range(L)]; m = [sp.expand(a[i] + be[i]) for i in range(L)]
    n = [sp.expand(b[i] - ga[i]) for i in range(L)]; k = [sp.expand(b[i] + ga[i]) for i in range(L)]
    Cp = [sp.expand(l[i] * m[i] / 4) for i in range(L)]; Cm = [sp.expand(n[i] * k[i] / 4) for i in range(L)]
    H = [sp.expand((p_[i]**2 + Df[i]**2 - P[i]**2 - DX[i]**2) / 2) for i in range(L)]
    Dd = [sp.expand(p_[i] * Df[i] + P[i] * DX[i]) for i in range(L)]
    return dict(f=f, p=p_, X=X, P=P, l=l, m=m, n=n, k=k, Cp=Cp, Cm=Cm, H=H, D=Dd, Q=list(f) + list(X), Pm=list(p_) + list(P))

for L in [4, 5]:
    dsym = sp.symbols(f"d0:{L}")
    Dg = circ(L, {r: dsym[r] for r in range(L)})       # fully general circulant
    M = modelA(L, Dg)
    pb = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
    okHD = all(sp.expand(M["H"][i] - M["Cp"][i] - M["Cm"][i]) == 0 and sp.expand(M["D"][i] - M["Cp"][i] + M["Cm"][i]) == 0 for i in range(L))
    check(f"A1 L={L}: H = C+ + C-, D = C+ - C-, C+ = l m/4, C- = n k/4 (general circulant)", okHD)
    A = Dg - Dg.T; S = Dg + Dg.T
    ok = True
    for i in range(L):
        for j in range(L):
            ok &= sp.expand(pb(M["Cp"][i], M["Cp"][j]) - A[i, j] * (M["l"][i] * M["m"][j] + M["m"][i] * M["l"][j]) / 8) == 0
            ok &= sp.expand(pb(M["Cm"][i], M["Cm"][j]) + A[i, j] * (M["n"][i] * M["k"][j] + M["k"][i] * M["n"][j]) / 8) == 0
            ok &= sp.expand(pb(M["Cp"][i], M["Cm"][j]) - S[i, j] * (M["l"][i] * M["k"][j] + M["m"][i] * M["n"][j]) / 8) == 0
    check(f"A2 L={L}: exact brackets {{C+,C+}}=A(lm'+ml')/8, {{C-,C-}}=-A(nk'+kn')/8, {{C+,C-}}=S(lk'+mn')/8, A=D-D^T, S=D+D^T", ok)

def branch_scan(L, D, label):
    """Sigma = union over per-site choices; each component is a linear subspace. Test first-classness on each."""
    M = modelA(L, D)
    pb = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
    allC = M["Cp"] + M["Cm"]
    BR = [[pb(allC[i], allC[j]) for j in range(2 * L)] for i in range(2 * L)]
    A = D - D.T; S = D + D.T
    allv = M["Q"] + M["Pm"]
    res = {}
    agree = True
    for sp_ in itertools.product([0, 1], repeat=L):          # 0: l_x = 0, 1: m_x = 0
        for sm in itertools.product([0, 1], repeat=L):       # 0: n_x = 0, 1: k_x = 0
            eqs = [(M["l"][i] if sp_[i] == 0 else M["m"][i]) for i in range(L)] + [(M["n"][i] if sm[i] == 0 else M["k"][i]) for i in range(L)]
            Jrank = sp.Matrix([[sp.diff(e, v) for v in allv] for e in eqs]).rank()
            sol = sp.solve(eqs, allv, dict=True)[0]
            fc = all(sp.expand(BR[i][j].subs(sol)) == 0 for i in range(2 * L) for j in range(i + 1, 2 * L))
            # predicted rule
            pred = True
            for i in range(L):
                for j in range(L):
                    if A[i, j] != 0 and (sp_[i] != sp_[j] or sm[i] != sm[j]): pred = False
                    if S[i, j] != 0 and sp_[i] != sm[j]: pred = False
            agree &= (pred == fc)
            res[(sp_, sm)] = (fc, Jrank)
    fcs = [(k_, v) for k_, v in res.items() if v[0]]
    return fcs, agree, len(res)

for L, dn, d in [(4, "cen", CEN), (4, "fwd", FWD), (5, "cen", CEN), (5, "fwd", FWD)]:
    fcs, agree, ntot = branch_scan(L, circ(L, d), dn)
    desc = sorted({("l" if all(s == 0 for s in k_[0]) else "m" if all(s == 1 for s in k_[0]) else "mix") + ("n" if all(s == 0 for s in k_[1]) else "k" if all(s == 1 for s in k_[1]) else "mix") + f"(rank {v[1]})" for k_, v in fcs})
    check(f"A3 L={L} {dn}: first-class components of Sigma (of {ntot}) match the kink rule", agree, f"first class: {desc}")
    if dn == "cen":
        check(f"A3c L={L} cen: exactly the 4 uniform branches; regular (rank 2L) ones are (l,k),(m,n)",
              set(desc) == {f"ln(rank {L + L - (2 if L % 2 == 0 else 1)})", f"mk(rank {L + L - (2 if L % 2 == 0 else 1)})", f"lk(rank {2 * L})", f"mn(rank {2 * L})"}, str(desc))
    else:
        check(f"A3f L={L} fwd: only the reducible branches (l,n),(m,k) are first class; regular branches anomalous",
              set(desc) == {f"ln(rank {2 * L - 1})", f"mk(rank {2 * L - 1})"}, str(desc))
# symbolic antisymmetric range-2 circulant (covers central, 4th-order central; SLAC is antisymmetric too)
L = 5
d1, d2 = sp.symbols("d1 d2")
Das = circ(L, {1: d1, -1: -d1, 2: d2, -2: -d2})
M = modelA(L, Das)
pb = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
ok = True
for i in range(L):
    for j in range(L):
        ok &= sp.expand(pb(M["Cp"][i], M["Cm"][j])) == 0
        lhs = pb(M["Cp"][i], M["Cp"][j]) * M["m"][i] * M["m"][j]
        rhs = Das[i, j] * (M["m"][j]**2 * M["Cp"][i] + M["m"][i]**2 * M["Cp"][j])
        ok &= sp.expand(lhs - rhs) == 0
        lhs = pb(M["Cm"][i], M["Cm"][j]) * M["n"][i] * M["n"][j]
        rhs = -Das[i, j] * (M["n"][j]**2 * M["Cm"][i] + M["n"][i]**2 * M["Cm"][j])
        ok &= sp.expand(lhs - rhs) == 0
check("A4 L=5 any antisymmetric range-2 Delta: {C+,C-}=0 and strong closure "
      "{C+x,C+y} = D_xy (m_y/m_x C+x + m_x/m_y C+y) on {m!=0}; {C-x,C-y} = -D_xy (n_y/n_x C-x + n_x/n_y C-y) on {n!=0}", ok)
# A5: at a uniform background m = mb, n = nb (needs winding of phi -/+ X) the H,D structure functions are
#     {H_x,H_y} ~ D_xy (D_x + D_y), {D_x,H_y} ~ D_xy (H_x + H_y), {D_x,D_y} ~ D_xy (D_x + D_y)  (continuum with delta' -> Delta)
mb, nb = sp.symbols("mb nb")
cp = sp.symbols(f"cp0:{L}"); cm = sp.symbols(f"cm0:{L}")
sfp = lambda i, j, mm: Das[i, j] * (mm[j] / mm[i] * cp[i] + mm[i] / mm[j] * cp[j])
sfm = lambda i, j, nn: -Das[i, j] * (nn[j] / nn[i] * cm[i] + nn[i] / nn[j] * cm[j])
mu = [mb] * L; nu = [nb] * L
Hs = [cp[i] + cm[i] for i in range(L)]; Ds = [cp[i] - cm[i] for i in range(L)]
ok = True
for i in range(L):
    for j in range(L):
        HH = sfp(i, j, mu) + sfm(i, j, nu)
        DH = sfp(i, j, mu) - sfm(i, j, nu)   # {C+ - C-, C+ + C-} = {C+,C+} - {C-,C-}
        ok &= sp.expand(HH - Das[i, j] * (Ds[i] + Ds[j])) == 0 and sp.expand(DH - Das[i, j] * (Hs[i] + Hs[j])) == 0
check("A5 uniform background: {H_x,H_y} = D_xy(D_x+D_y), {D_x,H_y} = D_xy(H_x+H_y) on shell (Dirac algebra, delta'->Delta)", ok)

# ================================================================== Part P
print("=== Part P: lattice PFT  C+ = Pi+ g+ + a^2/4,  C- = Pi- g- - b^2/4,  g+- = 1 + Delta u+-,  H = C+ - C-, D = C+ + C-")
def modelP(L, D):
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}")
    up = sp.symbols(f"up0:{L}"); Pp = sp.symbols(f"Pp0:{L}"); um = sp.symbols(f"um0:{L}"); Pm = sp.symbols(f"Pm0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    gp = [1 + sum(D[i, j] * up[j] for j in range(L)) for i in range(L)]
    gm = [1 + sum(D[i, j] * um[j] for j in range(L)) for i in range(L)]
    a = [p_[i] + Df[i] for i in range(L)]; b = [p_[i] - Df[i] for i in range(L)]
    Cp = [sp.expand(Pp[i] * gp[i] + a[i]**2 / 4) for i in range(L)]
    Cm = [sp.expand(Pm[i] * gm[i] - b[i]**2 / 4) for i in range(L)]
    return dict(f=f, p=p_, up=up, Pp=Pp, um=um, Pm=Pm, a=a, b=b, gp=gp, gm=gm, Cp=Cp, Cm=Cm,
                Q=list(f) + list(up) + list(um), P=list(p_) + list(Pp) + list(Pm))
for L, dn, d in [(5, "cen", CEN), (5, "fwd", FWD), (5, "as2", {1: d1, -1: -d1, 2: d2, -2: -d2})]:
    D = circ(L, d)
    M = modelP(L, D)
    pb = lambda F, G: pb_canon(F, G, M["Q"], M["P"])
    A = D - D.T; S = D + D.T
    ok = True
    for i in range(L):
        for j in range(L):
            e = pb(M["Cp"][i], M["Cp"][j]) - (M["Pp"][i] * M["gp"][j] * D[i, j] - M["gp"][i] * M["Pp"][j] * D[j, i] + A[i, j] * M["a"][i] * M["a"][j] / 4)
            ok &= sp.expand(e) == 0
            ok &= sp.expand(pb(M["Cp"][i], M["Cm"][j]) + S[i, j] * M["a"][i] * M["b"][j] / 4) == 0
    check(f"P1 L={L} {dn}: exact {{C+,C+}} and {{C+,C-}} = -S a_x b_y/4", ok)
    # on shell: Pi+ = -a^2/(4 g+), Pi- = b^2/(4 g-)
    onsh = {M["Pp"][i]: -M["a"][i]**2 / (4 * M["gp"][i]) for i in range(L)}
    onsh.update({M["Pm"][i]: M["b"][i]**2 / (4 * M["gm"][i]) for i in range(L)})
    if dn != "fwd":
        ok = True
        for i in range(L):
            for j in range(L):
                wk = pb(M["Cp"][i], M["Cp"][j]).subs(onsh)
                pred = -D[i, j] * (M["a"][i] * M["gp"][j] - M["a"][j] * M["gp"][i])**2 / (4 * M["gp"][i] * M["gp"][j])
                ok &= sp.simplify(wk - pred) == 0
        check(f"P2 L={L} {dn}: on shell {{C+x,C+y}} = -D_xy (a_x g_y - a_y g_x)^2 / (4 g_x g_y)  (anomaly)", ok)
    # explicit rational point of Sigma where {H_0,H_1} != 0  (H = C+ - C-)
    vals = {v: sp.Rational(r, 7) for v, r in zip(M["f"] + M["p"] + M["up"] + M["um"], itertools.cycle([1, -2, 3, 5, -1, 4, 2]))}
    if dn == "as2": vals.update({d1: sp.Rational(2, 3), d2: -sp.Rational(1, 12)})
    H = [M["Cp"][i] - M["Cm"][i] for i in range(L)]
    hb = sp.simplify(pb(H[0], H[1]).subs(onsh).subs(vals))
    cons = [sp.simplify(c.subs(onsh).subs(vals)) for c in M["Cp"] + M["Cm"]]
    check(f"P3 L={L} {dn}: naive lattice PFT is NOT first class: point on Sigma with {{H_0,H_1}} = {hb}", all(c == 0 for c in cons) and hb != 0)

# Kuchar form of the chiral sector and flatness  F_xy = d_{u_y} h_x - d_{u_x} h_y + {h_x,h_y}
def flat_naive(L, d):
    D = circ(L, d)
    a = sp.symbols(f"a0:{L}"); u = sp.symbols(f"u0:{L}")
    g = [1 + sum(D[i, j] * u[j] for j in range(L)) for i in range(L)]
    h = [a[i]**2 / (4 * g[i]) for i in range(L)]
    pa = lambda F, G: sum(2 * (D[i, j] - D[j, i]) / 2 * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L))
    ok = True
    for i in range(L):
        for j in range(L):
            F = sp.diff(h[i], u[j]) - sp.diff(h[j], u[i]) + pa(h[i], h[j])
            ok &= sp.simplify(F + D[i, j] * (a[i] / g[i] - a[j] / g[j])**2 / 4) == 0
    return ok
check("P4a naive Kuchar density h=a^2/(4g): curvature F_xy = -D_xy (v_x - v_y)^2/4, v = a/g (cen, L=5)", flat_naive(5, CEN))

# ---------------------------------------------------------------- finite-range ansatz certificates
def jet_cert(Ra, Rw, N, mode, d=CEN, normk=0, verbose=True):
    """h_x = sum_{r<=s, |r|,|s|<=Ra} c_rs(w) a_{x+r} a_{x+s},  {a_x,a_y} = 2 Delta_xy (Delta antisymmetric here)
    mode 'g'    : c_rs Taylor polynomial (order N) in e_t = g_{x+t} - 1, |t|<=Rw, g = 1 + Delta u
    mode 'shift': c_rs Taylor polynomial in u_{x+t}, |t|<=Rw, with shift invariance sum_y d/du_y h_x = 0
    mode 'u'    : as 'shift' without shift invariance (control)
    Flatness imposed through order N-1 (complete for C^N germs at the ruler background), uniform value tt*sum c_rs(0) = 1."""
    rd = max(abs(k) for k in d)
    span = 2 * Ra + (Rw + rd if mode == "g" else Rw) + 2 * rd + 2
    L = 2 * span + 3
    def Dl(i, j):
        r = (j - i) % L
        if r > L // 2: r -= L
        return d.get(r, 0)
    a = sp.symbols(f"a0:{L}"); e = sp.symbols(f"e0:{L}")
    pairs = [(r, s) for r in range(-Ra, Ra + 1) for s in range(r, Ra + 1)]
    ts = list(range(-Rw, Rw + 1))
    mons = [c for k in range(N + 1) for c in itertools.combinations_with_replacement(ts, k)]
    kap = {(r, s, c): sp.Symbol("k_%d_%d_" % (r, s) + "_".join(map(str, c)) + "_%d" % len(c)) for (r, s) in pairs for c in mons}
    unk = list(kap.values()); tt = sp.Symbol("tt")
    def h(xx):
        return sp.expand(sum(v * sp.prod([e[(xx + t) % L] for t in c]) * a[(xx + r) % L] * a[(xx + s) % L] for (r, s, c), v in kap.items()))
    def pba(F, G):
        return sp.expand(sum(2 * Dl(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0))
    def du(F, yy):
        if mode == "g":
            return sp.expand(sum(Dl(zz, yy) * sp.diff(F, e[zz]) for zz in range(L) if Dl(zz, yy) != 0))
        return sp.expand(sp.diff(F, e[yy]))
    def trunc(F, nmax):
        if F == 0: return F
        pP = sp.Poly(F, *e)
        return sp.expand(sum(cf * sp.prod([v**kk for v, kk in zip(e, mon)]) for mon, cf in pP.terms() if sum(mon) <= nmax))
    eqs = set()
    h0 = h(0)
    for yy in range(1, span + 1):
        F = trunc(du(h0, yy) - du(h(yy), 0) + pba(h0, h(yy)), N - 1)
        if F == 0: continue
        gens = [v for v in list(a) + list(e) if F.has(v)]
        eqs.update(sp.expand(cf) for cf in sp.Poly(F, *gens).coeffs())
    if mode == "shift":
        sh = sp.expand(sum(sp.diff(h0, e[yy % L]) for yy in ts))
        if sh != 0:
            eqs.update(sp.Poly(sh, *[v for v in list(a) + list(e) if sh.has(v)]).coeffs())
    norms = [tt * sum(v for (r, s, c), v in kap.items() if len(c) == 0) - 1]
    for kk in range(1, normk + 1):   # continuum 1/g along uniform background (mode g only)
        norms.append(sum(v for (r, s, c), v in kap.items() if len(c) == kk) - (-1)**kk * sum(v for (r, s, c), v in kap.items() if len(c) == 0))
    G = sp.groebner(list(eqs) + norms, *(unk + [tt]), order="grevlex")
    return list(G) == [1], len(unk), len(eqs), L

def run_jet(Ra, Rw, N, mode, expect_empty, label, **kw):
    t = time.time()
    empty, nu, ne, L = jet_cert(Ra, Rw, N, mode, **kw)
    check(f"{label} mode={mode} Ra={Ra} Rw={Rw} N={N}: flat jets with nonzero uniform value {'do not exist' if expect_empty else 'exist'}",
          empty == expect_empty, f"(L={L}, {nu} unknowns, {ne} eqs, Groebner {'[1]' if empty else 'nontrivial'}, {time.time() - t:.0f}s)")

# P4b class-1 rational ansatz h_x = sum k_rst a_{x+r} a_{x+s} / g_{x+t}: only h = 0 is flat
def class1(Ra, Rg, d=CEN):
    rd = max(abs(k) for k in d)
    span = 2 * Ra + Rg + 2 * rd + 2
    L = 2 * span + 3
    def Dl(i, j):
        r = (j - i) % L
        if r > L // 2: r -= L
        return d.get(r, 0)
    a = sp.symbols(f"a0:{L}"); g = sp.symbols(f"g0:{L}")
    pairs = [(r, s) for r in range(-Ra, Ra + 1) for s in range(r, Ra + 1)]
    kap = {(r, s, t): sp.Symbol(f"k{r}_{s}_{t}".replace("-", "m")) for (r, s) in pairs for t in range(-Rg, Rg + 1)}
    h = lambda xx: sum(v * a[(xx + r) % L] * a[(xx + s) % L] / g[(xx + t) % L] for (r, s, t), v in kap.items())
    pba = lambda F, G: sum(2 * Dl(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0)
    du = lambda F, yy: sum(Dl(zz, yy) * sp.diff(F, g[zz]) for zz in range(L) if Dl(zz, yy) != 0)
    eqs = set(); h0 = h(0)
    for yy in range(1, span + 1):
        num = sp.expand(sp.fraction(sp.together(du(h0, yy) - du(h(yy), 0) + pba(h0, h(yy))))[0])
        if num == 0: continue
        eqs.update(sp.expand(c) for c in sp.Poly(num, *[v for v in list(a) + list(g) if num.has(v)]).coeffs())
    sol = sp.solve(list(eqs), list(kap.values()), dict=True)
    return all(all(v == 0 for v in s.values()) for s in sol) and len(sol) >= 1, len(kap), L
for Ra, Rg in [(1, 0), (1, 1)] + ([(2, 1)] if SLOW else []):
    t = time.time()
    ok, nk, L = class1(Ra, Rg)
    check(f"P4b class h = sum k a a / g_(x+t), Ra={Ra} Rg={Rg} (cen): the only flat member is h = 0", ok, f"(L={L}, {nk} unknowns, {time.time() - t:.0f}s)")

print("--- P5 jet certificates (germs at the ruler background X+ = x)")
run_jet(0, 0, 2, "g", True, "P5a")
run_jet(1, 0, 2, "g", True, "P5b")
run_jet(1, 1, 1, "g", False, "P5c(order-0 only, control)")
run_jet(1, 1, 2, "g", True, "P5d")
run_jet(1, 1, 1, "shift", False, "P5e(order-0 only, control)")
run_jet(1, 1, 2, "shift", True, "P5f")
run_jet(1, 1, 2, "u", False, "P5g(no shift invariance, control)")
if SLOW:
    run_jet(1, 2, 2, "g", True, "P5h")
    run_jet(2, 0, 2, "g", True, "P5i")
    run_jet(1, 2, 2, "shift", True, "P5j")

# P6 X-independent clocks: K_x = P_x + h_x(phi,pi) abelian  => {h_x, sum_y h_y} = 0 (energy density frozen).
#    No finite-range quadratic h with sum_x h_x = H0 = (1/2) sum (pi^2 + (Delta phi)^2) has {h_0, H0} = 0.
print("--- P6 X-independent (deparametrised) clocks")
def lemD(L, R, d):
    D = circ(L, d)
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    H0 = sp.expand(sum(p_[i]**2 + Df[i]**2 for i in range(L)) / 2)
    win = list(range(-R, R + 1))
    zz = lambda xx: [f[(xx + i) % L] for i in win] + [p_[(xx + i) % L] for i in win]
    n = 2 * len(win)
    c = {(i, j): sp.Symbol(f"c{i}_{j}") for i in range(n) for j in range(i, n)}
    h = lambda xx: sum(v * zz(xx)[i] * zz(xx)[j] for (i, j), v in c.items())
    allv = list(f) + list(p_)
    eqs = sp.Poly(sp.expand(sum(h(xx) for xx in range(L)) - H0), *allv).coeffs()
    eqs += sp.Poly(pb_canon(h(0), H0, f, p_), *allv).coeffs()
    return sp.linsolve(eqs, list(c.values())) == sp.EmptySet
for L, R, dn, d in [(7, 1, "cen", CEN), (7, 1, "fwd", FWD), (8, 1, "cen", CEN), (9, 2, "cen", CEN), (9, 2, "fwd", FWD)] + ([(11, 3, "cen", CEN)] if SLOW else []):
    check(f"P6 L={L} R={R} {dn}: no range-R quadratic density with sum = H0 and {{h_0,H0}} = 0", lemD(L, R, d))

print(f"TOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - T0:.0f}s, {'slow' if SLOW else 'fast'} mode)")
