#!/usr/bin/env python3
"""r55a_2 -- decade arithmetic of the a_RS / KN-step complex. Criteria: checks/r55a_2_criteria.md (written first).
Fractions only; log10 by rigorous rational enclosures; sqrt by isqrt enclosures. No floats. Reviewer claude-opus-5-5."""
from fractions import Fraction as F
from math import isqrt

# ---------- rigorous rational enclosures ----------
def ln_r(r, n=60):
    """enclosure of ln r for rational r in [1, 2]: 2 atanh z, z=(r-1)/(r+1) in [0,1/3]."""
    assert 1 <= r <= 2
    z = (r - 1) / (r + 1)
    s, zp = F(0), z
    for i in range(n):
        s += zp / (2 * i + 1)
        zp *= z * z
    lo = 2 * s
    rem = 2 * zp / ((2 * n + 1) * (1 - z * z))   # zp = z^(2n+1)
    return lo, lo + rem

LN2 = ln_r(F(2))
LN54 = ln_r(F(5, 4))
LN10 = (3 * LN2[0] + LN54[0], 3 * LN2[1] + LN54[1])

def ln_enc(q):
    """enclosure of ln q, q > 0 rational."""
    q = F(q); assert q > 0
    j = 0
    while q >= 2: q /= 2; j += 1
    while q < 1: q *= 2; j -= 1
    lo, hi = ln_r(q)
    if j >= 0:
        return lo + j * LN2[0], hi + j * LN2[1]
    return lo + j * LN2[1], hi + j * LN2[0]

def log10_enc(q):
    q = F(q); assert q > 0
    # split off powers of ten exactly so the series argument stays moderate
    k = len(str(q.numerator)) - len(str(q.denominator))
    m = q / F(10) ** k
    while m >= 10: m /= 10; k += 1
    while m < 1: m *= 10; k -= 1
    lo, hi = ln_enc(m)                     # 0 <= ln m < ln 10
    return k + lo / LN10[1], k + hi / LN10[0]

def sqrt_enc(n, D=10**30):
    s = isqrt(n * D * D)
    return F(s, D), F(s + 1, D)

def fmt(x, dig=6):
    x = F(x); sgn = '-' if x < 0 else '+'
    x = abs(x); sc = 10 ** dig
    v = (x.numerator * sc * 2 + x.denominator) // (2 * x.denominator)
    return f"{sgn}{v // sc}.{str(v % sc).zfill(dig)}"
def fenc(e, dig=6):
    return f"[{fmt(e[0], dig)}, {fmt(e[1], dig)}]"
def sci(x, dig=6):
    x = F(x); lo, hi = log10_enc(x); k = int(lo) if lo >= 0 else -int(-lo) - (0 if lo == int(lo) else 1)
    m = x / F(10) ** k
    while m >= 10: m /= 10; k += 1
    while m < 1: m *= 10; k -= 1
    return f"{fmt(m, dig)[1:]}e{k}"
def within(enc, target, tol):
    return max(abs(enc[0] - target), abs(enc[1] - target)) <= tol
def ver(b, yes="REPRODUCES", no="DISAGREES"): return yes if b else no

out = []; P = out.append
P("r55a_2  decade arithmetic (criteria: r55a_2_criteria.md).  enclosures are rigorous rational intervals.")
P(f"ln2 enclosure width {fmt(LN2[1]-LN2[0], 3)} ; ln10 width {fmt(LN10[1]-LN10[0], 3)}")

# ---------- definitions ----------
Ad, L2 = F(9), F(9)
def eta_RS(e, N): return min(e / 18, e * e / (512 * N * Ad))
def delta0(N): return min(F(1, 640 * N), F(2, N ** 3))
def eta_q(e, N): return min(e / 18, e / (256 * N * Ad), delta0(N) / Ad)
def eta_KN(e): return e / 117
def a_eta(eta, N): return eta * eta / (2 * N)
def kern(e, N, kap): return kap * e * e / (256 * N)
def a_RS(eta, e, N, kap=F(1)): return min(a_eta(eta, N), kern(e, N, kap))

E_TODAY = F(67, 10) * F(10) ** -40
E_PROP = F(938495112638, 10**11) * F(10) ** -45
E_LIVE = {"6.7e-40 (RLARGE l.72)": E_TODAY, "9.52e-40 (RLARGE l.71)": F(952, 100) * F(10) ** -40,
          "8.95e-40 (RLARGE l.611)": F(895, 100) * F(10) ** -40, "1.27e-39 (RLARGE l.611)": F(127, 100) * F(10) ** -39}
DX_A = F(2456, 1000) * F(10) ** -152      # REVIEW_SF_S7 l.203
DX_B = F(25, 10) * F(10) ** -152          # RLARGE l.618
CEIL = F(100)

# ---------- G1 ----------
P("\n== G1 gain (linear vs quadratic a_RS), kappa = 1")
for (lab, e) in (("6.7e-40", E_TODAY), ("prop 9.38495112638e-45", E_PROP)):
    for N in (2, 3):
        direct = a_RS(eta_KN(e), e, N) / a_RS(eta_RS(e, N), e, N)
        closed = (F(4608 * N) / (117 * e)) ** 2
        g = log10_enc(direct)
        P(f"  eps={lab:24s} N={N}: gain {fenc(g)}   direct==closed form: {direct == closed}")
        tgt = {("6.7e-40", 2): [(F(821406, 10**4), F(5, 10**5)), (F(82141, 10**3), F(5, 10**4))],
               ("6.7e-40", 3): [(F(824927, 10**4), F(5, 10**5))],
               ("prop 9.38495112638e-45", 2): [(F(918478, 10**4), F(5, 10**5)), (F(91848, 10**3), F(5, 10**4))],
               ("prop 9.38495112638e-45", 3): [(F(922000, 10**4), F(5, 10**5))]}[(lab, N)]
        for t, tol in tgt:
            P(f"      vs {fmt(t, 4)}: {ver(within(g, t, tol))}")

# ---------- G2 ----------
P("\n== G2 margins log10((a/100)/DX'), eps = 6.7e-40, N = 2, kappa = 1")
aq = a_RS(eta_RS(E_TODAY, 2), E_TODAY, 2); al = a_RS(eta_KN(E_TODAY), E_TODAY, 2)
P(f"  a_RS quadratic = {sci(aq)} ; a_RS linear = {sci(al)}")
mqA = log10_enc(aq / CEIL / DX_A); mqB = log10_enc(aq / CEIL / DX_B)
mqA625 = log10_enc(aq / 625 / CEIL / DX_A); mlA = log10_enc(al / CEIL / DX_A); mlA625 = log10_enc(al / 625 / CEIL / DX_A)
P(f"  quad /100, DX'=2.456e-152: {fenc(mqA)}  vs -15.617: {ver(within(mqA, F(-15617, 1000), F(5, 10**4)))}")
P(f"  quad /100, DX'=2.5e-152  : {fenc(mqB)}  vs -15.62479 (ARS_BIND A6): {ver(within(mqB, F(-1562479, 10**5), F(5, 10**6)))}")
P(f"  quad /(625*100), DX'=2.456e-152: {fenc(mqA625)}  vs -18.413: {ver(within(mqA625, F(-18413, 1000), F(5, 10**4)))}")
P(f"  lin /100, DX'=2.456e-152: {fenc(mlA)}  vs +66.523: {ver(within(mlA, F(66523, 1000), F(5, 10**4)))}")
P(f"  lin /(625*100), DX'=2.456e-152: {fenc(mlA625)}  vs +63.728: {ver(within(mlA625, F(63728, 1000), F(5, 10**4)))}")
sepAB = log10_enc(DX_B / DX_A)
P(f"  power: the two DX' inputs differ by {fenc(sepAB)} decades (>= 0.005 required): {sepAB[0] >= F(5, 1000)}")

# ---------- G3 ----------
P("\n== G3 live a = theta*c_pr*eps^2 at the supremum theta = 1/24, c_pr = 1/(640*53^2)")
c_pr = F(1, 640 * 53 * 53)
a_live = F(1, 24) * c_pr * E_TODAY ** 2
P(f"  c_pr = {c_pr} = {sci(c_pr)} ; a_bad = {sci(c_pr*E_TODAY**2)} ; a = {sci(a_live, 7)}")
rel = abs(a_live / (F(1040415, 10**6) * F(10) ** -86) - 1)
P(f"  vs 1.040415e-86 (ARS_BIND A7): relative diff {sci(rel, 3)} -> {ver(rel <= F(5, 10**7))}")
m7B = log10_enc(a_live / CEIL / DX_B); m7A = log10_enc(a_live / CEIL / DX_A)
P(f"  margin a/100 vs DX'=2.5e-152  : {fenc(m7B)}  vs +63.61927: {ver(within(m7B, F(6361927, 10**5), F(5, 10**6)))}")
P(f"  margin a/100 vs DX'=2.456e-152: {fenc(m7A)}")
diff = (mqA[0] - mqB[1], mqA[1] - mqB[0])
P(f"  ATTRIBUTION: (-15.6171...) - (-15.6248...) = {fenc(diff, 7)} ; log10(2.5/2.456) = {fenc(sepAB, 7)}")
att = abs(diff[0] - sepAB[0]) < F(1, 10**6) and abs(diff[1] - sepAB[1]) < F(1, 10**6)
P(f"  -> {'DIFFERENT-DX-INPUT' if att else 'OTHER'}")
# theta at the HW [HW-2] value 1/96 and the collar value 1/(96*82), for the record (reported, not pre-registered as verdicts)
for th, lab in ((F(1, 96), "theta=1/96 ([HW-2])"), (F(1, 96 * 82), "theta=1/(96*82) (W-cb collar)")):
    P(f"  [report] {lab}: margin vs DX'=2.456e-152 = {fenc(log10_enc(th*c_pr*E_TODAY**2/CEIL/DX_A), 3)}")

# ---------- G4 ----------
P("\n== G4 route ratios at eps = 6.7e-40")
for N, tb, tp, tlog in ((2, F(1551148, 1000), F(201029, 1000), F(23033, 10**4)), (3, F(3490083, 1000), F(452315, 1000), F(26554, 10**4))):
    r = eta_KN(E_TODAY) / eta_q(E_TODAY, N)
    bare = r * r; per = F(81, 625) * bare
    P(f"  N={N}: eta_KN/eta_q = {r} ; bare = {bare} = {fmt(bare, 4)} ; per-cube (81/625) = {per} = {fmt(per, 4)}")
    P(f"     bare vs {fmt(tb,3)}: {ver(abs(bare - tb) <= F(5, 10**4))} ; per-cube vs {fmt(tp,3)}: {ver(abs(per - tp) <= F(5, 10**4))}"
      f" ; log10 per-cube {fenc(log10_enc(per))} vs {fmt(tlog,4)}: {ver(within(log10_enc(per), tlog, F(5, 10**5)))}")

# ---------- G5 ----------
P("\n== G5(a) eta_KN/eta_q across eps in (0,2]")
test_eps = [E_TODAY, F(1, 1000), F(39, 100), F(2, 5), F(41, 100), F(1), F(2)]
universal = True; reversal = True
for N in (2, 3):
    for e in test_eps:
        r = eta_KN(e) / eta_q(e, N)
        exact = (r == F(256 * N, 13))
        universal &= exact; reversal &= (r > 1)
        P(f"  N={N} eps={fmt(e,2) if e > F(1,10**6) else sci(e,2):>10s}: ratio = {fmt(r,4)}  {'EXACT-256N/13' if exact else 'NOT 256N/13'}")
P(f"  claim 'by 512/13 (768/13) at every eps_1': {'CONFIRMED' if universal else 'REFUTED-AS-UNIVERSAL'} ; "
  f"{'REVERSAL-HOLDS' if reversal else 'REVERSAL-FAILS'}")
P("\n== G5(b) RLARGE l.65 as written today (current eta_RS)")
ok_all = True; ctrl_violation = False
for N in (2, 3):
    for e in test_eps:
        eq = eta_q(e, N); cap_active = (eq == delta0(N) / Ad) and (delta0(N) / Ad < e / (256 * N * Ad))
        holds = (eta_RS(e, N) <= eq) or cap_active
        ok_all &= holds
        if eta_RS(e, N) > eq: ctrl_violation = True
        P(f"  N={N} eps={fmt(e,2) if e > F(1,10**6) else sci(e,2):>10s}: eta_RS/eta_q = {fmt(eta_RS(e,N)/eq,6) if e > F(1,10**6) else sci(eta_RS(e,N)/eq,4)}"
          f"  cap(delta_0/9) active: {cap_active}  -> clause holds: {holds}")
P(f"  -> {'L65-TRUE-AS-WRITTEN' if ok_all else 'L65-FALSE'} ; control (drop the 'unless' clause) finds a violation: "
  f"{'FIRES' if ctrl_violation else 'NO POWER'}")

# ---------- G6 ----------
P("\n== G6(a) post-adoption branch of a_RS")
kstar = F(128, 13689)
P(f"  kappa* = 256/27378 = {kstar} = {fmt(kstar, 8)} ; 117^2*2 = {117*117*2}")
kap_only = True
for N in (2, 3):
    for e in (F(1, 10**40), F(1, 1000), F(1, 2), F(2), F(814), F(815), F(1000)):
        for kap in (kstar * F(999, 1000), kstar * F(1001, 1000), F(1, 4), F(1)):
            plaq = a_eta(eta_KN(e), N) <= kern(e, N, kap)
            kap_only &= (plaq == (kap >= kstar))
P(f"  active branch decided by kappa >= kappa* alone at every tested (eps, N, kappa): {'BOUNDARY-KAPPA-ONLY' if kap_only else 'NO'}")
stale = all(a_eta(eta_KN(e), 2) <= kern(e, 2, F(1)) for e in (F(814), F(815), F(1000), F(10**6)))
P(f"  at kappa = 1, N = 2, plaquette branch active at eps = 814, 815, 1000, 1e6: {stale} -> '814.587' {'STALE' if stale else 'NOT-STALE'}")
P("== G6(b) pre-adoption branch (current eta_RS), N = 2")
pre = {}
for kap in (F(1), F(1, 100)):
    pre[kap] = [a_eta(eta_RS(e, 2), 2) <= kern(e, 2, kap) for e in (F(1), F(511), F(513), F(700), F(814), F(815), F(1000), F(10**4))]
P(f"  kappa=1   : plaquette active at eps = 1,511,513,700,814,815,1000,1e4: {pre[F(1)]}")
P(f"  kappa=1/100 (control): {pre[F(1,100)]}")
P(f"  -> {'ALWAYS-PLAQUETTE' if all(pre[F(1)]) else 'BRANCH-CHANGES'} at kappa=1 ; control "
  f"{'FIRES' if not all(pre[F(1,100)]) else 'NO POWER'} ; ARS_FIX 'active iff eps_1 < 814.587': "
  f"{'REFUTED-AS-IFF' if all(pre[F(1)]) else 'CONSISTENT'}")
eps_cross = 1   # crossover of the quadratic formula alone, eps^2 = 4608^2 N^2/128 at N=2
P(f"  quadratic-formula crossover eps^2 = 4608^2*4/128 = {F(4608**2*4,128)} (eps = 814.587...), while the quadratic entry of eta_RS"
  f" is active only for eps <= 4608N/18 = {F(4608*2,18)}")

# ---------- G7 ----------
P("\n== G7 Codex F4's re-centring-free linear threshold eta_F4 = min{eps/18, eps/(32 sqrt(N) A_d)}")
for N in (2, 3):
    s = sqrt_enc(N)
    ratio = (F(288) * s[0] / 117, F(288) * s[1] / 117)          # eta_KN/eta_F4 (eps-free while eps/(288 sqrt N) < eps/18)
    D = (2 * log10_enc(ratio[0])[0], 2 * log10_enc(ratio[1])[1])
    # gain of eta_F4 over the quadratic eta_RS at eps = 6.7e-40
    gF4_lo = 2 * log10_enc(E_TODAY / (288 * s[1]) / eta_RS(E_TODAY, N))[0]
    gF4_hi = 2 * log10_enc(E_TODAY / (288 * s[0]) / eta_RS(E_TODAY, N))[1]
    P(f"  N={N}: eta_KN/eta_F4 = 288 sqrt(N)/117 in [{fmt(ratio[0],6)}, {fmt(ratio[1],6)}] ;"
      f" RECENTRING-SHARE D = {fenc(D, 5)} decades ; gain of eta_F4 over eta_RS at 6.7e-40 = [{fmt(gF4_lo,5)}, {fmt(gF4_hi,5)}]")
    P(f"     eta_F4 vs RS-lin's eta_q: eta_F4/eta_q = 8 sqrt(N) in [{fmt(8*s[0],4)}, {fmt(8*s[1],4)}]")

# ---------- G8 ----------
P("\n== G8 RS-lin joint per-cube exponent vs live a, eps = 6.7e-40, N = 2")
jt = a_eta(eta_q(E_TODAY, 2), 2) / 81
P(f"  a_eta(eta_q)/81 = {sci(jt, 6)}  vs 6.52499e-89: {ver(abs(jt / (F(652499, 10**5) * F(10)**-89) - 1) <= F(1, 10**5))}")
la = log10_enc(a_live / jt)
P(f"  log10(a_live/joint) = {fenc(la, 5)}  vs 2.20263: {ver(within(la, F(220263, 10**5), F(5, 10**6)))}")
P(f"  joint per-cube margin vs DX'=2.456e-152: {fenc(log10_enc(jt / CEIL / DX_A), 4)} (RA-17 quotes +61.424)")

# ---------- G9 ----------
P("\n== G9 C_Omega at which the a_RS 'breach' reverses (= 10^{-margin})")
cA = DX_A / (aq / CEIL); cB = DX_B / (aq / CEIL)
P(f"  DX'=2.456e-152: C_Omega* = {sci(cA, 5)}  vs 4.14e15: {ver(abs(cA / (F(414, 100) * F(10)**15) - 1) <= F(5, 10**3))}")
P(f"  DX'=2.5e-152  : C_Omega* = {sci(cB, 5)}  vs 4.2149e15: {ver(abs(cB / (F(42149, 10**4) * F(10)**15) - 1) <= F(5, 10**4))}")
print("\n".join(out))
