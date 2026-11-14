# r55h_arith.py — exact/rigorous arithmetic for REVIEW55_HWPLD.
# Criteria: checks/r55h_arith_criteria.md and checks/r55h_ring_criteria.md (both written before this file).
# Fractions only for verdicts; logs as rigorous rational enclosures. Floats only in printed summaries.
from fractions import Fraction as F
import sys

def atanh_encl(z, n=70):
    # z rational, 0 <= z <= 1/3 ; returns (lo, hi) with lo <= atanh(z) <= hi
    s = F(0); p = z; z2 = z * z
    for k in range(n + 1):
        s += p / (2 * k + 1)
        p *= z2
    tail = p / ((2 * n + 3) * (1 - z2))   # p = z^{2n+3}
    return (s, s + tail)

L2 = tuple(2 * v for v in atanh_encl(F(1, 3)))           # ln 2
def ln_encl(x):
    x = F(x)
    assert x > 0
    # x = 2^e * y, y in [1,2)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    y = x / (F(2) ** e) if e >= 0 else x * (F(2) ** (-e))
    while y >= 2: y /= 2; e += 1
    while y < 1: y *= 2; e -= 1
    z = (y - 1) / (y + 1)
    lo, hi = atanh_encl(z)
    lo, hi = 2 * lo, 2 * hi
    if e >= 0:
        return (e * L2[0] + lo, e * L2[1] + hi)
    else:
        return (e * L2[1] + lo, e * L2[0] + hi)

LN10 = ln_encl(10)
def log10_encl(x):
    lo, hi = ln_encl(x)
    a = lo / LN10[1] if lo >= 0 else lo / LN10[0]
    b = hi / LN10[0] if hi >= 0 else hi / LN10[1]
    return (a, b)

def pow10(k):
    return F(10) ** k

def sigfig(x, s):
    x = F(x); assert x > 0
    e = len(str(x.numerator)) - len(str(x.denominator))
    while pow10(e) > x: e -= 1
    while pow10(e + 1) <= x: e += 1
    m = x / pow10(e - s + 1)
    q, r = divmod(m.numerator, m.denominator)
    if 2 * r >= m.denominator: q += 1
    if q == 10 ** s:            # carry
        q //= 10; e += 1
    return (q, e)

def parse(v):
    # '4.89789e-97' -> (489789, -97, 6 sig figs); '204.17' -> (20417, 2, 5)
    v = v.strip()
    if 'e' in v:
        mant, ex = v.split('e'); ex = int(ex)
    else:
        mant, ex = v, 0
    if '.' in mant:
        ip, fp = mant.split('.')
    else:
        ip, fp = mant, ''
    digits = (ip + fp).lstrip('0') or '0'
    s = len(digits)
    e = ex + len(ip.lstrip('0')) - 1 if ip.lstrip('0') else ex - (len(fp) - len(fp.lstrip('0'))) - 1
    return int(digits), e, s

def rounds_to(encl, printed):
    q, e, s = parse(printed)
    a = sigfig(encl[0], s); b = sigfig(encl[1], s)
    return a == (q, e) and b == (q, e), a, b

def fl(x):
    return float(x)

out = []
def rec(s):
    out.append(s); print(s); sys.stdout.flush()

V = {}
def check(tag, encl, printed):
    ok, a, b = rounds_to(encl, printed)
    rec("  %-58s printed %-12s enclosure [%.9e, %.9e] -> %s" % (tag, printed, fl(encl[0]), fl(encl[1]), 'OK' if ok else 'MISMATCH'))
    V[tag] = ok
    return ok

a = F(1, 10 ** 86); beta = F(186, 1000); LN3 = ln_encl(3); LN12800 = ln_encl(12800)
Dr = 17 ** 4 - 1; LN2D2 = ln_encl(2 * Dr * Dr)

def consts(ses, cp, cU=1):
    if ses == 5: Csh, hn, hn1, hD = 6561, 38418, 38417, 38416
    else: Csh, hn, hn1, hD = 81, 10002, 10001, 10000
    bn = Csh * 81 * hn * cp + hn1 * cU
    bD = hD * (Csh * 81 * cp + cU)
    cf = Csh * 81 * cp
    return bn, bD, cf

def g2(den_int, extra=LN12800, num=a):
    return (num / (den_int + extra[1]), num / (den_int + extra[0]))

def nT(bD):
    return (F(bD) / (a * beta * LN3[1]), F(bD) / (a * beta * LN3[0]))

def nH(B0, hD=38416):
    lo = (4 + F(hD * B0) / LN3[1]) / (a * beta)
    hi = (4 + F(hD * B0) / LN3[0]) / (a * beta)
    return (F(lo.numerator // lo.denominator), F(hi.numerator // hi.denominator))

def relboot(cf, h=38417):
    return g2(h * (cf + 1))

def histsum(cf, h=38417):
    return g2(h * (cf + 2))

def ratio(x, y):  # enclosures x / y
    return (x[0] / y[1], x[1] / y[0])

def const_encl(c):
    return (F(c), F(c))

# ============ A1 ============
rec("A1 HW §35.7 table")
rows = [(5, 1, '20416938755', '20415875872', '531441', '4.89789e-97', '9.99104e96'),
        (5, 82, '1674185866133', '1674098709808', '43578162', '5.97305e-99', '8.19264e98'),
        (6, 1, '65633123', '65620000', '6561', '1.52362e-94', '3.21128e94'),
        (6, 17, '1115603075', '1115380000', '111537', '8.96376e-96', '5.45840e95'),
        (6, 82, '5381106005', '5380030000', '538002', '1.85835e-96', '2.63286e96')]
G2 = {}; NT = {}
a1 = True
for ses, cp, pbn, pbD, pcf, pg, pn in rows:
    bn, bD, cf = consts(ses, cp)
    ints_ok = (str(bn) == pbn and str(bD) == pbD and str(cf) == pcf)
    rec("  s%d c+=%d: b_n=%d b_D=%d c_f=%d integers match: %s" % (ses, cp, bn, bD, cf, ints_ok))
    a1 &= ints_ok
    G2[(ses, cp)] = g2(bn); NT[(ses, cp)] = nT(bD)
    a1 &= check("g2CRC s%d c+=%d" % (ses, cp), G2[(ses, cp)], pg)
    a1 &= check("n_T s%d c+=%d" % (ses, cp), NT[(ses, cp)], pn)
rec("A1 VERDICT: " + ("PASS" if a1 else "FAIL"))

# ============ A2 ============
rec("A2 S5-12 four-way coincidence at s5 c+=1")
bn, bD, cf = consts(5, 1)
a2 = True
for p in ('4.89789e-97', '4.897894e-97'): a2 &= check("(S2) s5", G2[(5, 1)], p)
RB = relboot(cf); HS = histsum(cf)
for p in ('4.89802e-97', '4.898021e-97'): a2 &= check("REL-boot s5 (B*=c_f+1, 38417)", RB, p)
for p in ('4.898e-97', '4.898012e-97'): a2 &= check("HIST-sum s5 (B0=c_f+2, 38417)", HS, p)
for p in ('9.99104e96', '9.991038e96'): a2 &= check("n_T s5", NT[(5, 1)], p)
for B0lab, B0 in (('c_f', cf), ('c_f+2', cf + 2)):
    enc = nH(B0)
    for p in ('9.99102e96', '9.991019e96'):
        ok, _, _ = rounds_to(enc, p)
        rec("  n_H(B0=%s) = [%.9e, %.9e] vs printed %s -> %s" % (B0lab, fl(enc[0]), fl(enc[1]), p, 'OK' if ok else 'mismatch'))
rec("A2 VERDICT (S2/REL/HIST/n_T): " + ("PASS" if a2 else "FAIL") + " (n_H rows are records of which B0 reproduces)")

# ============ A3 ============
rec("A3 decision ratios")
a3 = True
DX = const_encl(F(25, 10) / pow10(152))
E94 = const_encl(1 / pow10(94))
a3 &= check("s5 slack vs 2.5e-152 (3 s.f.)", ratio(G2[(5, 1)], DX), '1.96e55')
a3 &= check("s5 slack vs 2.5e-152 (5 s.f.)", ratio(G2[(5, 1)], DX), '1.9592e55')
a3 &= check("s6 x17 slack vs 2.5e-152", ratio(G2[(6, 17)], DX), '3.5855e56')
# break-even c_+: a/(65623122 c + 10001 + ln12800) = 2.5e-152
K = F(81 * 81 * 10002)
be = ((a / DX[0] - 10001 - LN12800[1]) / K, (a / DX[0] - 10001 - LN12800[0]) / K)
a3 &= check("break-even c_+ (s6)", be, '6.0954e57')
a3 &= check("1e-94 / g2 s5", ratio(E94, G2[(5, 1)]), '204.17')
a3 &= check("1e-94 / g2 s6 x17", ratio(E94, G2[(6, 17)]), '11.16')
a3 &= check("1e-94 / g2 s6 x82", ratio(E94, G2[(6, 82)]), '53.81')
a3 &= check("g2 s6 no ring / 1e-94", ratio(G2[(6, 1)], E94), '1.52')
G2[(5, 17)] = g2(consts(5, 17)[0])
a3 &= check("g2 s5 x17 (w6 A3)", G2[(5, 17)], '2.88112e-98')
for cp in (1, 17, 82):
    r = ratio(g2(consts(6, cp)[0]), g2(consts(5, cp)[0]))
    rn = ratio(nT(consts(5, cp)[1]), nT(consts(6, cp)[1]))
    a3 &= check("g2 gain s5->s6 at c+=%d" % cp, r, '311.1')
    a3 &= check("n_T gain s5->s6 at c+=%d" % cp, rn, '311.2')
S1_17 = g2(17 * 320001, extra=LN2D2)
a3 &= check("(S1) ceiling s6 x17", S1_17, '1.83822e-93')
a3 &= check("g2_ret s6 x17 (a_ret=2.0e-91)", g2(17 * 320001, extra=LN2D2, num=F(2, 10 ** 91)), '3.67644e-98')
cf17 = consts(6, 17)[2]
RB17 = relboot(cf17); HS17 = histsum(cf17)
a3 &= check("REL-boot s6 x17 (38417)", RB17, '2.33375e-96')
a3 &= check("1e-94 / REL-boot s6 x17", ratio(E94, RB17), '42.85')
NH17 = nH(cf17 + 2)
a3 &= check("n_H s6 x17 (38416, B0=c_f+2)", NH17, '2.09688e96')
a3 &= check("n_H / n_T s6 x17", ratio(NH17, NT[(6, 17)]), '3.84')
sp_ceil = ratio(G2[(6, 17)], HS17)
rec("  spread candidates at x17, HIST as written: (S2)/HIST-sum = [%.6f, %.6f]; (S2)/REL = [%.6f, %.6f]; n_H/n_T = [%.6f, %.6f]"
    % (fl(sp_ceil[0]), fl(sp_ceil[1]), fl(ratio(G2[(6,17)], RB17)[0]), fl(ratio(G2[(6,17)], RB17)[1]),
       fl(ratio(NH17, NT[(6,17)])[0]), fl(ratio(NH17, NT[(6,17)])[1])))
RB17s = relboot(cf17, h=10001); HS17s = histsum(cf17, h=10001); NH17s = nH(cf17 + 2, hD=10000)
rec("  spread candidates at x17, H-geo': (S2)/HIST-sum = [%.6f, %.6f]; (S2)/REL = [%.6f, %.6f]; n_H/n_T = [%.6f, %.6f]"
    % (fl(ratio(G2[(6,17)], HS17s)[0]), fl(ratio(G2[(6,17)], HS17s)[1]), fl(ratio(G2[(6,17)], RB17s)[0]),
       fl(ratio(G2[(6,17)], RB17s)[1]), fl(ratio(NH17s, NT[(6,17)])[0]), fl(ratio(NH17s, NT[(6,17)])[1])))
rec("A3 VERDICT: " + ("PASS" if a3 else "FAIL (see MISMATCH lines)"))

# ============ A4 (records) ============
rec("A4 RECORD: HW-route binding ceiling min{(S2), REL-boot, HIST-sum}")
for cp in (1, 17, 82):
    bn, bD, cf = consts(6, cp)
    for lab, h in (('HIST as written', 38417), ("H-geo'", 10001)):
        vals = {'(S2)': g2(bn), 'REL': relboot(cf, h), 'HIST': histsum(cf, h)}
        mn = min(vals.items(), key=lambda kv: kv[1][0])
        dec = log10_encl(mn[1][0] / DX[0])
        rec("  c+=%-3d %-16s binding=%s %.6e   decades above 2.5e-152: [%.4f, %.4f]" %
            (cp, lab, mn[0], fl(mn[1][0]), fl(dec[0]), fl(dec[1])))

# ============ A5 m_tau ============
rec("A5 PLD l.1097 m_tau")
def mtau(eta, eps, CI, Lv=3):
    b = F(Lv * Lv) / (2 * CI); target = 2 * CI * eps / (Lv * Lv)
    m, v = 0, eta
    while v < target:
        v *= b; m += 1
    return m
CIs = (F(1), F(3, 2), F(2))
eps0 = F(67, 10 ** 41)
kn = tuple(mtau(eps0 / 117, eps0, c) for c in CIs)
def eta_rs(eps, N=2, Ad=9, Lv=3):
    return min(eps / (2 * Lv * Lv), eps * eps / (512 * N * Ad))
rs = tuple(mtau(eta_rs(eps0), eps0, c) for c in CIs)
rs2 = tuple(mtau(eta_rs(F(2)), F(2), c) for c in CIs)
rec("  (i) eta=c_1 eps (c_1=1/117): %s  -> PLD (3,4,5) %s" % (kn, 'CONFIRMED' if kn == (3, 4, 5) else 'REFUTED'))
rec("  (ii) eta=RLARGE l.64 at eps=6.7e-40, N=2: %s -> SYMBOLS (66,90,122) %s" % (rs, 'CONFIRMED' if rs == (66, 90, 122) else 'REFUTED'))
rec("  (iii) control eta=RLARGE l.64 at eps=2: %s -> REVIEW_PLD_S3 (5,7,10) %s" % (rs2, 'CONFIRMED' if rs2 == (5, 7, 10) else 'REFUTED'))
rec("  (i') c_1-route depth is eps-independent: at eps=2 %s" % (tuple(mtau(F(2) / 117, F(2), c) for c in CIs),))

# ============ A6 HW l.604 ============
rec("A6 HW l.604 coefficient B(theta) = (1/640)(theta/53)^2")
Bold = F(1, 640) * (F(1, 10 ** 8) / 53) ** 2
Bnew = F(1, 640) * (F(3, 10 ** 8) / 53) ** 2
ok6 = sigfig(Bnew, 6) == (500623, -22)
rec("  B(1e-8) = %.9e ; B(3e-8) = %.9e (exact %s) -> SYMBOLS 5.00623e-22 %s" % (fl(Bold), fl(Bnew), Bnew, 'CONFIRMED' if ok6 else 'REFUTED'))
rec("  ratios: B(3e-8)/B(1e-8) = %s ; B(3e-8)/5e-23 = %s = %.6f ; SQ l.216 'approx 3e-23 at C_D=2': B(3e-8)/16 = %.4e"
    % (Bnew / Bold, Bnew / F(5, 10 ** 23), fl(Bnew / F(5, 10 ** 23)), fl(Bnew / 16)))

# ============ A7 ============
rec("A7 c_lcr shift factors")
def shift(den_int, extra):
    return ((den_int + extra[0] + 10 ** 9) / (den_int + extra[1]), (den_int + extra[1] + 10 ** 9) / (den_int + extra[0]))
check("PLD p6 B3 factor at s5 b_n", shift(consts(5, 1)[0], LN12800), '1.0490')
for cp in (1, 17, 82):
    f = shift(consts(6, cp)[0], LN12800)
    f1 = shift(cp * 320001, LN2D2)
    rec("  RECORD s6 c+=%d: (S2) factor [%.6f, %.6f]; (S1) factor [%.3f, %.3f]" % (cp, fl(f[0]), fl(f[1]), fl(f1[0]), fl(f1[1])))
f1s5 = shift(1229313, LN2D2)
rec("  RECORD s5 c+=1 (S1) factor (c_att=1229313): [%.3f, %.3f]" % (fl(f1s5[0]), fl(f1s5[1])))

# ============ A8 ============
rec("A8 u*eps_1^2")
e1 = F(67, 10 ** 41)
check("u eps^2 at g2=1e-94", const_encl(e1 * e1 * pow10(94)), '4.489e15')
rec("  RECORD at g2=2.5e-152: %.4e" % fl(e1 * e1 / (F(25, 10) / pow10(152))))
bn82, bD82, cf82 = consts(6, 82)
g82 = min(g2(bn82)[0], relboot(cf82)[0], histsum(cf82)[0])
rec("  RECORD at the x82 HW-route binding value %.5e: %.4e" % (fl(g82), fl(e1 * e1 / g82)))

# ============ R1-R4 ring (records) ============
rec("R1-R4 RECORDS (reviewer's sharpened ring accounting; no pass/fail)")
bn1, bD1, cf1 = consts(6, 1)
R1g = g2(bn1)
rec("  R1 open ring merged: c_+=1: g2CRC [%.6e, %.6e]  n_T %.6e  c_f %d" % (fl(R1g[0]), fl(R1g[1]), fl(NT[(6, 1)][0]), cf1))
for lab, h in (('HIST as written', 38417), ("H-geo'", 10001)):
    rb, hs = relboot(cf1, h), histsum(cf1, h)
    rec("     REL-boot(%s) %.6e  HIST-sum %.6e" % (lab, fl(rb[0]), fl(hs[0])))
R2g = g2(bn1 + 6480)
R2s1 = g2(320001 + 80, extra=LN2D2)
rec("  R2 closed ring merged: g2CRC [%.6e, %.6e]  n_T %.6e (b_D unchanged)  (S1) %.6e" % (fl(R2g[0]), fl(R2g[1]), fl(NT[(6, 1)][0]), fl(R2s1[0])))
rec("     ratio R2 / x82 row = %.4f ; R2 / x17 row = %.4f" % (fl(R2g[0] / G2[(6, 82)][1]), fl(R2g[0] / G2[(6, 17)][1])))
bn82, bD82, cf82 = consts(6, 82)
r3 = {'(S2)': g2(bn82), 'REL(38417)': relboot(cf82), 'HIST(38417)': histsum(cf82)}
rec("  R3 x82 as tabulated: " + ", ".join("%s %.6e" % (k, fl(v[0])) for k, v in r3.items()))
for lab, val in (('R1 (S2)', R1g), ('R1 REL HIST-as-written', relboot(cf1)), ('R2 (S2)', R2g), ('x82 (S2)', g2(bn82)), ('x82 HIST-sum as written', histsum(cf82))):
    d1 = log10_encl(val[0] / DX[0]); d2 = log10_encl(val[0] / E94[0])
    rec("  R4 %-24s decades vs 2.5e-152 [%.4f, %.4f]; vs 1e-94 [%.4f, %.4f]" % (lab, fl(d1[0]), fl(d1[1]), fl(d2[0]), fl(d2[1])))

rec("SUMMARY: A1 %s | A2 %s | A3 %s | mismatches: %s" % ('PASS' if a1 else 'FAIL', 'PASS' if a2 else 'FAIL', 'PASS' if a3 else 'FAIL',
    [k for k, v in V.items() if not v]))
