#!/usr/bin/env python3
# ab1 — T55-M. Exact rational arithmetic, no BLAS, no lock.
# Criteria: checks/ab1_criteria.md (written BEFORE this file).
from fractions import Fraction as F
from decimal import Decimal, getcontext
getcontext().prec = 60


def dec(x):
    """log10 of a positive Fraction, exactly enough (60-digit decimal)."""
    return (Decimal(x.numerator).ln() - Decimal(x.denominator).ln()) / Decimal(10).ln()


def fsci(x):
    return f"{Decimal(x.numerator)/Decimal(x.denominator):.6E}"


# ---- inputs, all quoted (see criteria table) -------------------------------
N = 2
L = 3
A_d = F(9)                       # RLARGE l.1009
kappa = F(1)                     # RLARGE l.1248 (illustrative)
delta_0 = F(4, 10) / (256 * N)   # HIST l.152: 256*N*delta_0 = 0.4 at N=2
c_pr = F(1, 640) / (53 ** 2)     # RLARGE l.90
theta = F(1, 24)                 # RLARGE l.612 / l.88
DXp = F(25, 10) * F(10) ** -152  # RLARGE l.618, at C_Omega = 1
CEIL = F(100)                    # RLARGE l.616-617: g^2 <~ a/10^2
LEDGER_aRS = F(593136, 100000) * F(10) ** -166   # SYMBOLS l.356

EPS = [("6.7e-40  (RLARGE l.72, headline)", F(67, 10) * F(10) ** -40),
       ("8.95e-40 (RLARGE l.611)", F(895, 100) * F(10) ** -40),
       ("9.52e-40 (RLARGE l.71)", F(952, 100) * F(10) ** -40),
       ("1.27e-39 (RLARGE l.611)", F(127, 100) * F(10) ** -39)]

C_RS_GREEDY = F(625)   # RLARGE l.1021
C_RS_JOINT = F(81)     # RLARGE l.435, HIST l.185-186


def eta1(e):            # RLARGE l.1009
    return min(e / 18, e * e / (4608 * N))


def etaq(e):            # HIST l.180
    return min(e / 18, e / (2304 * N), delta_0 / 9)


def a_RS(e):            # RLARGE l.1020
    return min(eta1(e) ** 2 / (2 * N), kappa * e * e / (256 * N))


def a_RSlin(e):         # HIST l.174/l.182 kernel, l.180 plaquette; same min structure
    return min(etaq(e) ** 2 / (2 * N), kappa * e * e / (1024 * N))


def a_live(e):          # RLARGE l.87-89, l.414: a = theta * a_bad, a_bad = c_pr*eps^2
    return theta * c_pr * e * e


def verdict(ok):
    return "PASS" if ok else "FAIL"


TOL = Decimal("0.01")
res = {}
print("=" * 78)
print("ab1 — T55-M margins. Exact rationals. Criteria: checks/ab1_criteria.md")
print("=" * 78)

e0 = EPS[0][1]

# ---- (A1) ------------------------------------------------------------------
v = a_RS(e0)
d = abs(dec(v) - dec(LEDGER_aRS))
res["A1"] = d <= TOL
print(f"\n(A1) a_RS at eps_1=6.7e-40 : {fsci(v)}")
print(f"     SYMBOLS l.356 ledger    : {fsci(LEDGER_aRS)}")
print(f"     |delta| = {d:.6f} decades  -> {verdict(res['A1'])}")

# ---- (A2) ------------------------------------------------------------------
ok = True
print("\n(A2) which branch attains the min in a_RS?")
for lab, e in EPS:
    pl, ke = eta1(e) ** 2 / (2 * N), kappa * e * e / (256 * N)
    who = "plaquette" if pl < ke else "kernel"
    ok &= (pl < ke)
    print(f"     {lab:34s} plaq={fsci(pl)} kern={fsci(ke)}  -> {who}")
res["A2"] = ok
print(f"     -> {verdict(res['A2'])}")

# ---- (A3) ------------------------------------------------------------------
rslin_cube = a_RSlin(e0) / C_RS_JOINT
claim_A3 = F(6525, 1000) * F(10) ** -89
d = abs(dec(rslin_cube) - dec(claim_A3))
res["A3"] = d <= TOL
print(f"\n(A3) RS-lin per-cube = min(eta_q^2/2N, k*eps^2/1024N)/81 = {fsci(rslin_cube)}")
print(f"     [S25-CLAIM] 6.525e-89 ; |delta| = {d:.6f} decades -> {verdict(res['A3'])}")
print(f"     (RS-lin min attained by: "
      f"{'plaquette' if etaq(e0)**2/(2*N) < kappa*e0*e0/(1024*N) else 'kernel'})")

# ---- (A4) ------------------------------------------------------------------
gain = dec(rslin_cube) - dec(a_RS(e0) / C_RS_GREEDY)
d = abs(gain - Decimal("79.84"))
res["A4"] = d <= TOL
print(f"\n(A4) gain over a_RS/625 = {gain:.5f} decades ; [S25-CLAIM] 79.84 ;"
      f" |delta| = {d:.5f} -> {verdict(res['A4'])}")

# ---- (A5) ------------------------------------------------------------------
m5 = dec(rslin_cube / CEIL) - dec(DXp)
d = abs(m5 - Decimal("61.42"))
res["A5"] = d <= TOL
print(f"\n(A5) RS-lin ceiling vs DX' (C_Omega=1) = {m5:+.5f} ; [S25-CLAIM] +61.42 ;"
      f" |delta| = {d:.5f} -> {verdict(res['A5'])}")

# ---- (A6) ------------------------------------------------------------------
m6 = dec(a_RS(e0) / CEIL) - dec(DXp)
d = abs(m6 - Decimal("-15.62"))
res["A6"] = d <= TOL
print(f"\n(A6) a_RS ceiling vs DX' (C_Omega=1) = {m6:+.5f} ; PROOF l.71-73 -15.62 ;"
      f" |delta| = {d:.5f} -> {verdict(res['A6'])}")
m6c = dec(a_RS(e0) / C_RS_GREEDY / CEIL) - dec(DXp)
print(f"     with c_RS=625: {m6c:+.5f}  (ARS_FIX's -18.41 pair)")

# ---- (A7) ------------------------------------------------------------------
al = a_live(e0)
m7 = dec(al / CEIL) - dec(DXp)
res["A7"] = m7 > 0
print(f"\n(A7) LIVE exponent a = theta*c_pr*eps^2 = {fsci(al)}  (RLARGE l.612 says ~1.0e-86)")
print(f"     a/10^2 vs DX' = {m7:+.5f} decades -> l.618 is "
      f"{'TRUE' if m7 > 0 else 'FALSE'} at a  -> {verdict(res['A7'])}")

# ---- (A8) ------------------------------------------------------------------
# breach reverses when DX' = 2.5e-152/C_Omega drops to a_RS/10^2
C_rev = (a_RS(e0) / CEIL) / DXp
C_rev = 1 / C_rev
d = abs(dec(C_rev) - dec(F(414, 100) * F(10) ** 15))
res["A8"] = d <= TOL
print(f"\n(A8) C_Omega at which the a_RS breach reverses = {fsci(C_rev)}")
print(f"     [S25-CLAIM] 4.14e15 ; |delta| = {d:.5f} decades -> {verdict(res['A8'])}")

# ---- (A9) ------------------------------------------------------------------
part_eta = 2 * (dec(etaq(e0)) - dec(eta1(e0)))
part_c = dec(C_RS_GREEDY / C_RS_JOINT)
tot = part_eta + part_c
d1 = abs(tot - gain)
pred = dec(F(4) / (e0 * e0))
d2 = abs(part_eta - pred)
res["A9"] = (d1 <= Decimal("0.001")) and (d2 <= Decimal("0.001"))
print(f"\n(A9) decomposition of (A4):")
print(f"     log10(eta_q/eta_1)^2 = {part_eta:.5f}   [HIST l.181 predicts log10(4/eps^2)"
      f" = {pred:.5f}, |delta|={d2:.6f}]")
print(f"     log10(625/81)        = {part_c:.5f}")
print(f"     sum                  = {tot:.5f} vs (A4) {gain:.5f}, |delta|={d1:.6f}"
      f" -> {verdict(res['A9'])}")

# ---- (A10) -----------------------------------------------------------------
print("\n(A10) spread over the four live eps_1 (defect 2):")
print(f"     {'eps_1':34s} {'(A4) gain':>11s} {'(A5) RSlin-DX':>14s}"
      f" {'(A6) aRS-DX':>12s} {'(A7) a-DX':>11s}")
signs = []
for lab, e in EPS:
    g = dec(a_RSlin(e) / C_RS_JOINT) - dec(a_RS(e) / C_RS_GREEDY)
    s5 = dec(a_RSlin(e) / C_RS_JOINT / CEIL) - dec(DXp)
    s6 = dec(a_RS(e) / CEIL) - dec(DXp)
    s7 = dec(a_live(e) / CEIL) - dec(DXp)
    signs.append((g > 0, s5 > 0, s6 > 0, s7 > 0))
    print(f"     {lab:34s} {g:>+11.4f} {s5:>+14.4f} {s6:>+12.4f} {s7:>+11.4f}")
res["A10"] = all(s == signs[0] for s in signs)
print(f"     signs constant across spread -> {verdict(res['A10'])}")

# ---- designed-FAIL controls ------------------------------------------------
print("\n" + "-" * 78)
print("DESIGNED-FAIL CONTROLS (each MUST fail)")
print("-" * 78)

# (C-F1) mechanism removed: eta_q -> eta_1 in RS-lin's plaquette branch
ctrl = min(eta1(e0) ** 2 / (2 * N), kappa * e0 * e0 / (1024 * N)) / C_RS_JOINT
g_ctrl = dec(ctrl) - dec(a_RS(e0) / C_RS_GREEDY)
cf1_passes_A4 = abs(g_ctrl - Decimal("79.84")) <= TOL
print(f"\n(C-F1) eta_q -> eta_1 : gain = {g_ctrl:.5f} decades (pre-registered: 0.888, NOT 79.84)")
print(f"       does it pass (A4)'s threshold? {cf1_passes_A4}  -> control "
      f"{'FAILED as designed' if not cf1_passes_A4 else 'PASSED — (A4) IS VOID'}")

# (C-F2) assert kernel branch attains the min
cf2 = kappa * e0 * e0 / (256 * N) < eta1(e0) ** 2 / (2 * N)
print(f"\n(C-F2) 'a_RS's min is the kernel branch' : {cf2}  -> control "
      f"{'FAILED as designed' if not cf2 else 'PASSED — (A2) IS VOID'}")

# (C-F3) (A7)'s test run with a_RS instead of a
cf3 = (dec(a_RS(e0) / CEIL) - dec(DXp)) > 0
print(f"\n(C-F3) (A7) run with a_RS in place of a : clears DX'? {cf3}  -> control "
      f"{'FAILED as designed' if not cf3 else 'PASSED — (A7) IS VOID'}")

# (C-F4) (A1) at the illustrative eps_1 = 0.5
e_ill = F(1, 2)
cf4 = abs(dec(a_RS(e_ill)) - dec(LEDGER_aRS)) <= TOL
print(f"\n(C-F4) (A1) at eps_1 = 0.5 : a_RS = {fsci(a_RS(e_ill))}, matches ledger? {cf4}")
print(f"       -> control {'FAILED as designed' if not cf4 else 'PASSED — ab1 IS eps_1-BLIND'}")

controls_ok = (not cf1_passes_A4) and (not cf2) and (not cf3) and (not cf4)

# ---- extra, labelled POST-HOC (not pre-registered) -------------------------
print("\n" + "-" * 78)
print("POST-HOC (not pre-registered; reported as post-hoc)")
print("-" * 78)
print(f"  live a vs RS-lin per-cube : log10(a / RS-lin) = "
      f"{dec(a_live(e0)) - dec(rslin_cube):+.5f} decades")
print(f"  i.e. the LIVE route's exponent is "
      f"{'BETTER' if a_live(e0) > rslin_cube else 'WORSE'} than RS-lin's joint-route per-cube value")
print(f"  eta_1 = {fsci(eta1(e0))}  eta_q = {fsci(etaq(e0))}  "
      f"(delta_0/9 cap binds? {etaq(e0) == delta_0/9})")
print(f"  a_bad = c_pr*eps^2 = {fsci(c_pr*e0*e0)}  (RLARGE l.93 says ~2.5e-85)")

print("\n" + "=" * 78)
for k in ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]:
    print(f"  {k:4s} {verdict(res[k])}")
print(f"  CONTROLS all failed as designed: {controls_ok}")
print("=" * 78)
