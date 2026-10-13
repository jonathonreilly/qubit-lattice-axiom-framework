#!/usr/bin/env python3
"""R19-6 [A]: set A's record-noise mean source written in weight-1 form, both readout gauges.

Law (E1 + N_c, insertion weight a = 4 - 2w; R18-7/R18-11):  T^{mu nu} = J^{mu nu} / (-g)^{w/2}, J the flat-conserved
record mode.  Written in weight-1 form, sqrt(-g) G^{mu nu} = 8 pi sqrt(-g) T^{mu nu} = 8 pi (-g)^{(a-2)/4} J^{mu nu}, so the
coarse-grained O(G noise^2) mean source per frame mode is
    tau^{mu nu}_a = ((a-2)/4) < tr(eta h) J^{mu nu} >  -  < [sqrt(-g) G^{mu nu}]^(2)[h,h] > / 8 pi          (*)
(the Pi completion acts on the homogeneous mode only; Lemma P / F0 -- not part of the per-mode table).
Claim U (stated before the run): at a = 2 the record term drops and the mean source is the weight-1 Einstein-density
functional A'[h] := -<[sqrt(-g)G^{mu nu}]^(2)[h,h]>/8 pi of the record-noise metric -- the same functional that R19-3
evaluates on the graviton vacuum.  Its readout-gauge independence is then Lemma D (field side), and every
gauge dependence for a != 2 sits in the record term (a-2)/4 <tr h J>.
Checks: (A1) Poisson-gauge linear solve, harmonic closed form, both satisfy G^(1) = 8 pi J; (A2) per-monomial
coefficients of (*) in units pi/k^2 vs R19-2's table (TESTS-registered R18-11/R19-2 law, lower-index form);
(A3) Poisson - harmonic per monomial, symbolic a; (A4) A'[h_n] at R19-2's complete least-decoherence split.
G = c = 1.  Subtraction: none.
Run: OMP_NUM_THREADS=2 python3 r196_setA.py
"""
import sympy as sp, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r196_lib import C, S, eps, eta, N, make_D, avg, einstein_lower, einstein_upper_density, order

t0 = time.time()
om, k = sp.symbols('omega k', positive=True)
a = sp.Symbol('a')
x = sp.Symbol('x', positive=True)
X = om / k
D = make_D(om, k)

rho, Tp, jx, jy, tp, tc = sp.symbols('rho T_perp j_x j_y t_p t_c', real=True)
J = sp.zeros(4, 4)                      # contravariant record mode (R15-2 channel variables), on cos(theta)
J[0, 0] = rho; J[0, 3] = J[3, 0] = X * rho; J[3, 3] = X**2 * rho
J[0, 1] = J[1, 0] = jx; J[1, 3] = J[3, 1] = X * jx
J[0, 2] = J[2, 0] = jy; J[2, 3] = J[3, 2] = X * jy
J[1, 1] = Tp / 2 + tp; J[2, 2] = Tp / 2 - tp; J[1, 2] = J[2, 1] = tc
J = J * C
Jl = eta * J * eta
print("[A0] flat conservation of J:", [sp.simplify(sum(D(m, J[m, n]) for m in range(N))) for n in range(N)])

# --- Poisson gauge: h00 = -2 Phi, h0i = S_i (transverse), hij = -2 Psi delta + hTT ; solve G^(1) = 8 pi J_lower
syms = sp.symbols('Phc Phs Psc Pss Sxc Sxs Syc Sys hpc hps hcc hcs', real=True)
Phi = syms[0] * C + syms[1] * S; Psi = syms[2] * C + syms[3] * S
Sx = syms[4] * C + syms[5] * S; Sy = syms[6] * C + syms[7] * S
hp = syms[8] * C + syms[9] * S; hc = syms[10] * C + syms[11] * S
hP = sp.zeros(4, 4)
hP[0, 0] = -2 * Phi; hP[0, 1] = hP[1, 0] = Sx; hP[0, 2] = hP[2, 0] = Sy
for i in (1, 2, 3):
    hP[i, i] = -2 * Psi
hP[1, 1] += hp; hP[2, 2] += -hp; hP[1, 2] = hP[2, 1] = hc
G1, _ = einstein_lower(hP, D)
eqs = []
for m in range(4):
    for q in range(m, 4):
        e = sp.expand(order(G1[m, q], 1) - 8 * sp.pi * Jl[m, q])
        eqs += [e.coeff(C, 1).coeff(S, 0), e.coeff(S, 1).coeff(C, 0)]
eqs = [e for e in (sp.simplify(e) for e in eqs) if e != 0]
sol = sp.solve(eqs, syms, dict=True)
assert len(sol) == 1
sol = {kk: sp.factor(v) for kk, v in sol[0].items()}
hP = hP.subs(sol)
print("[A1] Poisson-gauge solution: Phi = %s, Psi = %s, S_x = %s, h_+ = %s" %
      (sol[syms[0]], sol[syms[2]], sol[syms[4]], sol[syms[8]]))
# --- harmonic gauge closed form: hbar = 16 pi J_lower/(k^2 - w^2), h = hbar - eta tr(hbar)/2
hb = (16 * sp.pi / (k**2 - om**2)) * Jl
trb = sum(eta[i, i] * hb[i, i] for i in range(4))
hH = (hb - eta * trb / 2).applyfunc(sp.expand)
for lab, hh in (("Poisson", hP), ("harmonic", hH)):
    Gx, _ = einstein_lower(hh, D)
    res = sum(1 for m in range(4) for q in range(4) if sp.simplify(order(Gx[m, q], 1) - 8 * sp.pi * Jl[m, q]) != 0)
    print("     %-8s: G^(1)[h] = 8 pi J_lower violated in %d of 16 components" % (lab, res))
print("     [%.1fs]" % (time.time() - t0))

mons = [rho**2, rho*Tp, Tp**2, jx**2, jy**2, tp**2, tc**2]


def per_mode(hh):
    G, gi = einstein_lower(hh, D)
    Y1 = einstein_upper_density(G, gi, hh, 1)
    trh = sp.expand(sum(eta[i, i] * hh[i, i] for i in range(4)))
    rec = ((a - 2) / 4) * (J * trh).applyfunc(avg)                    # record term, upper indices
    fld = Y1.applyfunc(lambda e: -avg(order(e, 2)) / (8 * sp.pi))      # A'[h], upper indices
    out = {}
    for lab, M in (("rec", rec), ("fld", fld)):
        t00 = sp.expand(M[0, 0]); tkk = sp.expand(M[1, 1] + M[2, 2] + M[3, 3])
        t0i = [sp.simplify(M[0, i]) for i in (1, 2, 3)]
        for nm, ex in (("tau_00", t00), ("tau_kk", tkk)):
            P = sp.Poly(sp.expand(ex * k**2 / sp.pi), *[rho, Tp, jx, jy, tp, tc])
            for mon in mons:
                out[(lab, nm, mon)] = sp.factor(sp.simplify(sp.sympify(P.coeff_monomial(mon)).subs(om, x * k)))
            cross = [m_ for m_ in P.monoms() if sum(m_) == 2 and max(m_) == 1 and not (m_[0] == 1 and m_[1] == 1)]
            out[(lab, nm, 'cross')] = [sp.simplify(P.coeff_monomial(rho**m_[0]*Tp**m_[1]*jx**m_[2]*jy**m_[3]*tp**m_[4]*tc**m_[5]))
                                       for m_ in cross]
        out[(lab, 'tau_0i')] = t0i
    return out


res = {}
for lab, hh in (("Poisson", hP), ("harmonic", hH)):
    res[lab] = per_mode(hh)
    print("[A2:%s] done [%.1fs]" % (lab, time.time() - t0))

# R19-2's table (r192_modes.out [A2]; = R18-11's rR18-11:166-171), lower-index law with insertion weight a
c00 = {rho**2: 2*a*x**2 + 2*a - 3*x**2 - 7, rho*Tp: -a, Tp**2: 0, jx**2: 4, jy**2: 4,
       tp**2: 4*(x**2 + 1)/(x**2 - 1)**2, tc**2: 4*(x**2 + 1)/(x**2 - 1)**2}
ckk = {rho**2: (x**2 + 1)*(2*a*x**2 - 4*x**2 - 1), rho*Tp: a*x**2 + 2*a - 2*x**2 - 2, Tp**2: -(a - 2), jx**2: -4,
       jy**2: -4, tp**2: -4*(x**2 - 3)/(x**2 - 1)**2, tc**2: -4*(x**2 - 3)/(x**2 - 1)**2}
print("\n[A2] per-monomial mean source (units pi/k^2), weight-1 form (*) = record term + A'[h]:")
for g in ("Poisson", "harmonic"):
    r = res[g]
    ok = 0
    for mon in mons:
        for nm, ref in (("tau_00", c00), ("tau_kk", ckk)):
            tot = sp.simplify(r[("rec", nm, mon)] + r[("fld", nm, mon)])
            if g == "Poisson":
                ok += int(sp.simplify(tot - ref[mon]) == 0)
    if g == "Poisson":
        print("     Poisson gauge: (*) equals R19-2's lower-index table in %d of %d entries (form independence)" % (ok, 2 * len(mons)))
    print("     %s: cross monomials (should be 0): %s ; tau_0i: %s" % (
        g, set(sum([r[(l, nm, 'cross')] for l in ("rec", "fld") for nm in ("tau_00", "tau_kk")], [])),
        [sp.simplify(u + v) for u, v in zip(r[("rec", "tau_0i")], r[("fld", "tau_0i")])]))
print("\n     A'[h_n] = field part alone (= the whole source at a = 2), Poisson gauge, per monomial (units pi/k^2):")
for mon in mons:
    print("       %-8s tau_00 = %-34s tau_kk = %s" % (mon, res["Poisson"][("fld", "tau_00", mon)], res["Poisson"][("fld", "tau_kk", mon)]))
print("     record term (a-2)/4 <tr h J>, Poisson gauge:")
for mon in mons:
    print("       %-8s tau_00 = %-34s tau_kk = %s" % (mon, res["Poisson"][("rec", "tau_00", mon)], res["Poisson"][("rec", "tau_kk", mon)]))

print("\n[A3] readout-gauge dependence, Poisson minus harmonic, per monomial:")
allfld0 = True
for mon in mons:
    for nm in ("tau_00", "tau_kk"):
        dF = sp.simplify(res["Poisson"][("fld", nm, mon)] - res["harmonic"][("fld", nm, mon)])
        dR = sp.factor(sp.simplify(res["Poisson"][("rec", nm, mon)] - res["harmonic"][("rec", nm, mon)]))
        allfld0 &= (dF == 0)
        if dR != 0:
            print("       %-8s %s: field part diff = %s ; record part diff = %s" % (mon, nm, dF, dR))
print("     field part A'[h] gauge-independent for every monomial: %s  (Lemma D on the classical noise metric)" % allfld0)
print("     => total source gauge-independent iff a = 2 (record-term difference carries the factor (a-2)); matches Theorem G")

print("\n[A4] Theorem I0 restated: A'[h_n] at R19-2's complete least-decoherence split (r192_split.out [B2] powers)")
for region, sgn in (("x < 1", 1), ("x > 1", -1)):
    one_m = sgn * (1 - x**2)
    p1 = 2 / one_m; q = -sgn; p2 = one_m; Pj = sp.Rational(1, 4); Pt = one_m / 4
    pw = {rho**2: p1, rho*Tp: q, Tp**2: p2, jx**2: Pj, jy**2: Pj, tp**2: Pt, tc**2: Pt}
    for g in ("Poisson", "harmonic"):
        f00 = sp.simplify(sum(res[g][("fld", "tau_00", m)] * pw[m] for m in mons))
        fkk = sp.simplify(sum(res[g][("fld", "tau_kk", m)] * pw[m] for m in mons))
        r00 = sp.factor(sp.simplify(sum(res[g][("rec", "tau_00", m)] * pw[m] for m in mons)))
        rkk = sp.factor(sp.simplify(sum(res[g][("rec", "tau_kk", m)] * pw[m] for m in mons)))
        print("     %s, %-8s: A'[h_n] (tau_00, tau_kk)/u0 = (%s, %s) ; record term = (%s, %s)" % (region, g, f00, fkk, r00, rkk))
print("total time %.1fs" % (time.time() - t0))
