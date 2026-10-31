#!/usr/bin/env python3
# checks/r55k_2_posthoc.py -- POST-HOC (designed after reading checks/r55k_1_out.txt). Criteria: checks/r55k_2_criteria.md
# (written first). Reuses r55k_1's interval library verbatim (exec of the library section of r55k_1_const.py).
import os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "r55k_1_const.py")).read()
lib = src.split('P("r55k_1_const.py')[0]
exec(lib)
T0 = time.time()
P("r55k_2_posthoc.py (POST-HOC) -- library = r55k_1_const.py lines before its first P(...) call")
KB = 150
acc = I.c(0)
for k in range(1, KB + 1): acc = acc + LOG(2 ** k - 1) / (2 ** k)
LOGB1 = I(acc.lo, acc.hi + (LN2 * (KB + 2) / (2 ** KB)).hi)
B8 = EXP(LOGB1 * 8); SQ6 = SQRT(6)
CS = I.c(Fr("411.9229708842423061")); CG = I.c(Fr("5699.632830341894211"))
def c_quarter(q):
    th = Fr(4, 1) / q
    return (1 - th) * POW(4 * th, th / (1 - th))
def CS1sq(q, m, cs=CS, cg=CG, s1=4096):
    if q is None: cth, a = I.c(1), Fr(1)
    else:
        q = Fr(q); a = q / (q - 4); cth = c_quarter(q)
    return (1 / (Fr(3, 4) - Fr(1, 4) / m)) * (cth * POW(27 * cs, a) + s1 * cg)
def ACGC(q, m, **kw): return (1 + SQ6) * SQRT(CS1sq(q, m, **kw)) / m
def m_for(q, s1, cs=CS, cg=CG):
    v = ACGC(q, 1, s1=s1, cs=cs, cg=cg).hi
    return int(-((-v.numerator) // v.denominator))
def CT_eps(q, F, R0, m, s1, cs=CS, cg=CG, Ns=3):
    if q is None: a, Vinf = Fr(1), POW(R0, -2)
    else:
        q = Fr(q); a = q / (q - 4); Vinf = POW(R0, -2 + 8 / q)
    src_ = Fr(1, 2) * POW(36 * cs * Ns, a)
    ac = ACGC(q, m, cs=cs, cg=cg, s1=s1)
    cut = 288 * (cg + 18 * (Ns * cs * Vinf + Fr(1, 36 * m)))
    return SQ6 * F * B8 * (src_ + Fr(1, 2) * ac * ac + cut), ac
def Lam_i(i): return 2 - Fr(2) ** (1 - i)
def sig_i(i): return sum(Fr(j, 2 ** j) for j in range(i))
def istar(Sb, dmin=12):
    i = 0
    while Sb * Fr(2) ** (-i) / Lam_i(i + 1) >= dmin: i += 1
    return i
def Fmax(alpha, beta, R0, dmin=12, imax=45):
    alpha, beta = Fr(alpha), Fr(beta); best = None
    for i in range(1, imax + 1):
        x = (dmin * Lam_i(i) * Fr(2) ** (i - 1) + beta) / alpha; Rlo = -((-x.numerator) // x.denominator)
        x = (dmin * Lam_i(i + 1) * Fr(2) ** i + beta) / alpha; Rhi = -((-x.numerator) // x.denominator) - 1
        a_, b_ = max(Rlo, R0), Rhi
        if b_ < a_: continue
        for RR in sorted(set([a_, b_])):
            Sb = alpha * RR - beta; assert istar(Sb, dmin) == i
            Lm = Lam_i(i); lf = 2 * LOG(RR) - Lm * LOG(Sb / Lm) + LN2 * sig_i(i)
            if best is None or lf.lo > best[2].lo: best = (RR, i, lf)
    return best[0], EXP(best[2])
Lam_inf = Fr(16) * (Fr("4.94") + Fr("3.34"))
def Lam(q):
    if q is None: return I.c(Lam_inf)
    q = Fr(q); return 4 * POW(2, 2 + 4 / q) * (Fr("4.94") + Fr("3.34") * POW(32, 1 / q))
H = Fr("5.05e9"); DX = Fr("2.456e-152"); eps1 = Fr("6.7e-40")

P(); P("P2  c'_theta at theta = 1/2: (1-1/2)*(4*1/2)^((1/2)/(1-1/2)) = (1/2)*2^1 = %s  [run-2 display fix]" % (Fr(1, 2) * 2 ** 1))
verdict("P2 (c'_theta(1/2) == 1 exactly)", Fr(1, 2) * 2 ** 1 == 1)

P(); P("P1  QFIX chain under radius allocations CONSISTENT with Stage 1 (P-max, |N_S|=3, c_N=2, C_3=1, m(q) => A_c g_c <= 1)")
allocs = {}
Ra, Fa = Fmax(Fr(1, 4), 3, 64);   allocs["a: EPSSTAR radii (S1 gap R/4-4, S2 budget R/4-3, R0=64)"] = (Fa, 64, 4096)
Rb, Fb = Fmax(Fr(7, 16), 3, 256); allocs["b: S1 gap R/16-4, S2 budget 7R/16-3, R0=256"] = (Fb, 256, 65536)
allocs["ref: EPSSTAR/QFIX as printed (F=175.8, R0=64, S2 budget R/2-4 -- inconsistent)"] = (I.c(Fr("175.8")), 64, 4096)
P("    F_a = %s (R=%d) ; F_b = %s (R=%d)" % (S(Fa, 8), Ra, S(Fb, 8), Rb))
res = {}
for name, (F, R0, s1) in allocs.items():
    P("  -- %s" % name)
    rows = {}
    for q in (8, 11, 12, 16, 32, 100, 1000, None):
        m = m_for(q, s1)
        ct, ac = CT_eps(q, F.hi, R0, m, s1)
        cd = 2 * (Fr("1.011") * 2 * Lam(q) * ct + Fr("46.8"))
        cut = 1 / (Fr("3.31e7") * cd * cd) / (2 * SQRT(H))
        ob = LOG10(cut * cut * cut * cut / (4 * 9216 ** 2) / 100 / DX)
        rows[q] = (ct, cd, cut, ob)
        P("     q=%-5s m=%-7d A_cg_c<=%s C_T=%s C_D=%s eps_cut=%s obj=%s" %
          (q, m, sci(ac.hi, 3, True), S(ct, 5), S(cd, 5), S(cut, 5), SF(ob, 3)))
    lev = rows[None][3] - rows[8][3]
    P("     lever obj(inf)-obj(8) = %s ; obj(inf)-obj(12) = %s" % (SF(lev, 4), SF(rows[None][3] - rows[12][3], 4)))
    lo_q, hi_q = Fr(8), Fr(200)
    m_ = lambda qq: m_for(qq, s1)
    def CDq(qq):
        ct, _ = CT_eps(qq, F.hi, R0, m_(qq), s1)
        return 2 * (Fr("1.011") * 2 * Lam(qq) * ct + Fr("46.8"))
    if CDq(lo_q).hi <= Fr("6.7e15"): P("     C_D <= 6.7e15 already at q = 8")
    else:
        for _ in range(26):
            mq = (lo_q + hi_q) / 2; v = CDq(mq)
            if v.lo > Fr("6.7e15"): lo_q = mq
            elif v.hi <= Fr("6.7e15"): hi_q = mq
            else: break
        P("     real q at which C_D = 6.7e15 (c_N = 2): [%s, %s]" % (fx(lo_q, 4), fx(hi_q, 4, True)))
    res[name] = (rows, lev)
ka = list(allocs)[0]; kb = list(allocs)[1]
verdict("P1-i (q=12 meets C_D <= 6.7e15 under EPSSTAR's own radii)", le(res[ka][0][12][1], Fr("6.7e15")))
dl = LOG10(res[kb][0][12][2] / Fr("1.2948e-44"))
P("    log10(eps_cut(12; b)/1.2948e-44) = %s" % SF(dl, 4))
verdict("P1-ii (eps_cut(12) survives a consistent allocation to 0.1 decade)", True if (dl.hi <= Fr(1, 10) and dl.lo >= -Fr(1, 10)) else (False if (dl.lo > Fr(1, 10) or dl.hi < -Fr(1, 10)) else None))
dlev = res[kb][1] - Fr("24.0891")
verdict("P1-iii (lever allocation-independent to 0.01 decade)", True if (dlev.hi <= Fr(1, 100) and dlev.lo >= -Fr(1, 100)) else (False if (dlev.lo > Fr(1, 100) or dlev.hi < -Fr(1, 100)) else None))

P(); P("P3  fixed F=175.8, R0=64, q=12: smallest C_T over the delta-budget grid (achievable values; STAR_CONST's C_B^tot = 16/d2 + 54)")
cq = c_quarter(Fr(12)); a32 = Fr(3, 2)
def CT12(cs, cg, rho_note=""):
    x = 108 * cs; srcv = Fr(1, 2) * x * SQRT(x)
    y = 27 * cs
    m = None
    def cs1sq(mm): return (1 / (Fr(3, 4) - Fr(1, 4) / mm)) * (cq * y * SQRT(y) + 4096 * cg)
    v = ((1 + SQ6) * SQRT(cs1sq(1))).hi; m = int(-((-v.numerator) // v.denominator))
    ac = (1 + SQ6) * SQRT(cs1sq(m)) / m
    cut = 288 * (cg + 18 * (3 * cs * Fr(1, 256) + Fr(1, 36 * m)))
    return SQ6 * Fr("175.8") * B8 * (srcv + Fr(1, 2) * ac * ac + cut)
best = None
for rho in (Fr(1, 16), Fr(1, 1000)):
    for jd in range(4, 81, 2):          # delta_2 = jd/400 in [0.01, 0.2]
        d2 = Fr(jd, 400)
        for jt in range(300, 501, 5):   # T = jt/1000 in [0.3, 0.5]
            T = Fr(jt, 1000); kap = 1 - d2 - rho - T
            if kap <= 0: continue
            cs = I.c(8 * (9 / T + 2) / kap); cg = I.c(8 * (16 / d2 + 54) / kap + 272)
            v = CT12(cs, cg)
            if best is None or v.hi < best[0].hi: best = (v, rho, d2, T)
P("    coarse best: C_T = %s at rho=%s delta_2=%s T=%s" % (S(best[0], 5), best[1], best[2], best[3]))
v0, rho0, d0, t0 = best
for jd in range(-6, 7):
    for jt in range(-6, 7):
        d2 = d0 + Fr(jd, 2000); T = t0 + Fr(jt, 2000); kap = 1 - d2 - rho0 - T
        if d2 <= 0 or kap <= 0: continue
        v = CT12(I.c(8 * (9 / T + 2) / kap), I.c(8 * (16 / d2 + 54) / kap + 272))
        if v.hi < best[0].hi: best = (v, rho0, d2, T)
P("    refined best: C_T(12) = %s at rho=%s delta_2=%s T=%s  (EPSSTAR l.608 says the floor is 4.4e12)" % (S(best[0], 5), best[1], best[2], best[3]))
P("    at the chosen allocation (delta_2 = rho = 1/16): C_T(12) = %s" % S(CT12(CS, CG), 7))
P(); P("SUMMARY")
for t, v, n in VERD: P("  %-80s %s" % (t, v))
P("runtime %.1f s" % (time.time() - T0))
