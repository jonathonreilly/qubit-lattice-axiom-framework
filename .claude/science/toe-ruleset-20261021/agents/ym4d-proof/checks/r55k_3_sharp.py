#!/usr/bin/env python3
# checks/r55k_3_sharp.py -- POST-HOC. Criteria: checks/r55k_3_criteria.md (written first).
# Library = r55k_1_const.py's library section (exec'd verbatim).
import os, time
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, "r55k_1_const.py")).read().split('P("r55k_1_const.py')[0])
T0 = time.time()
P("r55k_3_sharp.py (POST-HOC): sharp telescope accounting, sup_R B_i(8) F(R) Chat^(1-2^-i)")
KB = 150
terms = [LOG(2 ** k - 1) / (2 ** k) for k in range(1, KB + 1)]   # log(p_j - 1)/p_j, p_j = 2^(j+1), j = k-1
acc = I.c(0)
for t in terms: acc = acc + t
LOGB1 = I(acc.lo, acc.hi + (LN2 * (KB + 2) / (2 ** KB)).hi)
def logBpart(i, m=8):          # log of prod_{j<i} (p_j-1)^{m/p_j}
    s = I.c(0)
    for t in terms[:i]: s = s + t
    return s * m
B8 = EXP(LOGB1 * 8); SQ6 = SQRT(6)
CS = I.c(Fr("411.9229708842423061")); CG = I.c(Fr("5699.632830341894211"))
def c_quarter(q):
    th = Fr(4, 1) / q
    return (1 - th) * POW(4 * th, th / (1 - th))
def CS1sq(q, m, s1):
    if q is None: cth, a = I.c(1), Fr(1)
    else:
        q = Fr(q); a = q / (q - 4); cth = c_quarter(q)
    return (1 / (Fr(3, 4) - Fr(1, 4) / m)) * (cth * POW(27 * CS, a) + s1 * CG)
def m_for(q, s1):
    v = ((1 + SQ6) * SQRT(CS1sq(q, 1, s1))).hi
    return int(-((-v.numerator) // v.denominator))
def Chat(q, R0, s1):
    m = m_for(q, s1)
    if q is None: a, Vinf = Fr(1), POW(R0, -2)
    else:
        q = Fr(q); a = q / (q - 4); Vinf = POW(R0, -2 + 8 / q)
    ac = (1 + SQ6) * SQRT(CS1sq(q, m, s1)) / m
    return Fr(1, 2) * POW(108 * CS, a) + Fr(1, 2) * ac * ac + 288 * (CG + 18 * (3 * CS * Vinf + Fr(1, 36 * m)))
def Lam_i(i): return 2 - Fr(2) ** (1 - i)
def sig_i(i): return sum(Fr(j, 2 ** j) for j in range(i))
def istar(Sb, dmin=12):
    i = 0
    while Sb * Fr(2) ** (-i) / Lam_i(i + 1) >= dmin: i += 1
    return i
def blocks(alpha, beta, R0, dmin=12, imax=60):
    out = []
    for i in range(1, imax + 1):
        x = (dmin * Lam_i(i) * Fr(2) ** (i - 1) + beta) / alpha; Rlo = -((-x.numerator) // x.denominator)
        x = (dmin * Lam_i(i + 1) * Fr(2) ** i + beta) / alpha; Rhi = -((-x.numerator) // x.denominator) - 1
        a_, b_ = max(Rlo, R0), Rhi
        if b_ < a_: continue
        for RR in sorted(set([a_, b_])):
            Sb = alpha * RR - beta; assert istar(Sb, dmin) == i
            Lm = Lam_i(i); lf = 2 * LOG(RR) - Lm * LOG(Sb / Lm) + LN2 * sig_i(i)
            out.append((RR, i, lf))
    return out
BLK = {}
def Csharp(q, alpha, beta, R0, s1):
    key = (alpha, beta, R0)
    if key not in BLK: BLK[key] = blocks(Fr(alpha), Fr(beta), R0)
    lc = LOG(Chat(q, R0, s1)); best = None
    for RR, i, lf in BLK[key]:
        v = lf + logBpart(i) + lc * (1 - Fr(1, 2 ** i))
        if best is None or v.lo > best[0].lo: best = (v, RR, i)
    lim = LOG(Fr(16) / Fr(alpha) ** 2) + LOGB1 * 8 + lc            # i_* -> infinity
    if lim.lo > best[0].lo: best = (lim, "inf", "inf")
    loose_F = max((EXP(lf) for RR, i, lf in BLK[key]), key=lambda z: z.lo)
    return SQ6 * EXP(best[0]), best[1], best[2], SQ6 * loose_F * B8 * EXP(lc)
Lam_inf = Fr(16) * (Fr("4.94") + Fr("3.34"))
def Lam(q):
    if q is None: return I.c(Lam_inf)
    q = Fr(q); return 4 * POW(2, 2 + 4 / q) * (Fr("4.94") + Fr("3.34") * POW(32, 1 / q))
H = Fr("5.05e9"); DX = Fr("2.456e-152")
alloc = [("printed (R/2-4, R0=64)", Fr(1, 2), 4, 64, 4096),
         ("(a) EPSSTAR radii (R/4-3, R0=64)", Fr(1, 4), 3, 64, 4096),
         ("(b) S1 gap R/16-4 (7R/16-3, R0=256)", Fr(7, 16), 3, 256, 65536)]
RES = {}
for name, al, be, R0, s1 in alloc:
    P(); P("-- %s" % name)
    rows = {}
    for q in (8, 11, 12, 16, 100, 1000, None):
        cs_, RR, ii, cl = Csharp(q, al, be, R0, s1)
        cd = 2 * (Fr("1.011") * 2 * Lam(q) * cs_ + Fr("46.8"))
        cut = 1 / (Fr("3.31e7") * cd * cd) / (2 * SQRT(H))
        ob = LOG10(cut * cut * cut * cut / (4 * 9216 ** 2) / 100 / DX)
        rows[q] = (cs_, cd, cut, ob, cl)
        P("   q=%-5s C_T#=%s at R=%s (i*=%s) | loose sqrt6*Fmax*B8*Chat=%s ratio %s | C_D=%s eps_cut=%s obj=%s" %
          (q, S(cs_, 5), RR, ii, S(cl, 5), S(cl / cs_, 4), S(cd, 5), S(cut, 5), SF(ob, 3)))
    lev = rows[None][3] - rows[8][3]
    P("   lever obj(inf)-obj(8) = %s ; obj(inf)-obj(12) = %s" % (SF(lev, 4), SF(rows[None][3] - rows[12][3], 4)))
    def CDq(qq):
        cs_, _, _, _ = Csharp(qq, al, be, R0, s1)
        return 2 * (Fr("1.011") * 2 * Lam(qq) * cs_ + Fr("46.8"))
    lo_q, hi_q = Fr(8), Fr(64)
    if CDq(lo_q).hi <= Fr("6.7e15"): P("   C_D <= 6.7e15 already at q = 8")
    else:
        for _ in range(22):
            mq = (lo_q + hi_q) / 2; v = CDq(mq)
            if v.lo > Fr("6.7e15"): lo_q = mq
            elif v.hi <= Fr("6.7e15"): hi_q = mq
            else: break
        P("   real q at which C_D = 6.7e15 (c_N = 2): [%s, %s]" % (fx(lo_q, 4), fx(hi_q, 4, True)))
    RES[name] = (rows, lev)
names = [a[0] for a in alloc]
r12 = RES[names[0]][0][12]
verdict("S1-i (loose formula within x1.1 of sharp sup, q=12, printed)", le(r12[4] / r12[0], Fr(11, 10)))
verdict("S1-ii (q=12 meets C_D <= 6.7e15 under EPSSTAR's own radii, sharp)", le(RES[names[1]][0][12][1], Fr("6.7e15")))
dl = RES[names[2]][1] - Fr("24.0891")
verdict("S1-iii (lever survives sharp accounting to 0.05, alloc b)", True if (dl.hi <= Fr(1, 20) and dl.lo >= -Fr(1, 20)) else (False if (dl.lo > Fr(1, 20) or dl.hi < -Fr(1, 20)) else None))
P(); P("SUMMARY")
for t, v, n in VERD: P("  %-80s %s" % (t, v))
P("runtime %.1f s" % (time.time() - T0))
