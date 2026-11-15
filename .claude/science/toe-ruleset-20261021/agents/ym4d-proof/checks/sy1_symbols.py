#!/usr/bin/env python3
# sy1_symbols.py  --  T55-C symbol audit: the arithmetic the rename needs.
# Criteria: checks/sy1_criteria.md  (written BEFORE this file).
# Exact rational arithmetic only (fractions). No BLAS, no numeric lock needed.

from fractions import Fraction as F

OUT = []
def P(s=""):
    OUT.append(s)

# ---------------------------------------------------------------- inputs
d, L, N = 4, 3, 2
A_d = F((d - 1) * L * (L - 1), 2)            # = 9
L2 = F(L * L)                                 # = 9
c_1 = F(1, 2) / (L2 + F(11, 2) * A_d)         # = 1/117   EXISTENCE l.1771
EPS_LIVE = F(67, 10 ** 41)                    # 6.7e-40   RLARGE l.72
EPS_ILL = F(2)                                # 2         RLARGE l.73

def eta_RS(eps, n=N):
    "RLARGE l.64 / l.976: min{eps/(2L^2), eps^2/(512 N A_d)}"
    return min(eps / (2 * L2), eps * eps / (512 * n * A_d))

def eta_KN(eps):
    "EXISTENCE l.1771 / l.1774: c_1 * eps"
    return c_1 * eps

def eta_q(eps, n=N):
    "RLARGE l.64, delta_0/A_d entry omitted (unevaluated)"
    return min(eps / (2 * L2), eps / (256 * n * A_d))

def m_tau(eta, eps, C_I):
    "PLD l.1097: least m with (L^2/(2 C_I))^m * eta >= 2 C_I eps / L^2"
    base = L2 / (2 * C_I)
    target = 2 * C_I * eps / L2
    m, cur = 0, F(eta)
    while cur < target:
        cur *= base
        m += 1
        if m > 100000:
            raise RuntimeError("no convergence")
    return m

CIs = [F(1), F(3, 2), F(2)]

P("=" * 78)
P("sy1_symbols.py  --  T55-C symbol audit arithmetic (exact rationals)")
P("criteria: checks/sy1_criteria.md")
P("=" * 78)
P("inputs: d=%d L=%d N=%d  A_d=%s  c_1=%s  eps_live=6.7e-40  eps_ill=2"
  % (d, L, N, A_d, c_1))
P("        eta_RS(eps_live) = %.6e   eta_KN(eps_live) = %.6e"
  % (float(eta_RS(EPS_LIVE)), float(eta_KN(EPS_LIVE))))
P("        active entry of eta_RS at eps_live: %s"
  % ("quadratic" if eta_RS(EPS_LIVE) == EPS_LIVE ** 2 / (512 * N * A_d) else "linear"))
P()

# ---------------------------------------------------------------- SY1-1
t_kn = tuple(m_tau(eta_KN(EPS_LIVE), EPS_LIVE, c) for c in CIs)
# eps-independence of the KN form: c_1 is a pure ratio, so m_tau must not move
t_kn_ill = tuple(m_tau(eta_KN(EPS_ILL), EPS_ILL, c) for c in CIs)
v1 = "MTAU-KN-REPRODUCES" if t_kn == (3, 4, 5) else "SOURCE-DISAGREES"
P("[SY1-1] m_tau at eta_1^KN (C_I = 1, 1.5, 2), eps_1 = 6.7e-40 : %s" % (t_kn,))
P("        same at eps_1 = 2 (KN form is eps-independent)        : %s" % (t_kn_ill,))
P("        PLD l.1098/l.1244 record 3 / 3,4,5   ->  %s" % v1)
P()

# ---------------------------------------------------------------- SY1-2
t_rs = tuple(m_tau(eta_RS(EPS_LIVE), EPS_LIVE, c) for c in CIs)
if all(m >= 40 for m in t_rs):
    v2 = "MTAU-RS-DIFFERS (live defect confirmed)"
elif any(m <= 10 for m in t_rs):
    v2 = "NO-DEFECT"
else:
    v2 = "INCONCLUSIVE"
P("[SY1-2] m_tau at eta_1^RS (C_I = 1, 1.5, 2), eps_1 = 6.7e-40 : %s" % (t_rs,))
P("        criterion 'every entry >= 40'  ->  %s" % v2)
P("        ratio to PLD's quoted 3/4/5    : %s"
  % tuple(F(a, b) for a, b in zip(t_rs, (3, 4, 5))).__str__())
P()

# ---------------------------------------------------------------- SY1-3 control
t_rs_ill = tuple(m_tau(eta_RS(EPS_ILL), EPS_ILL, c) for c in CIs)
ctrl_passes = all(m >= 40 for m in t_rs_ill)
P("[SY1-3] DESIGNED-FAIL CONTROL: same code path, same criterion, eps_1 = 2")
P("        m_tau at eta_1^RS, eps_1 = 2                          : %s" % (t_rs_ill,))
P("        criterion 'every entry >= 40'  ->  %s"
  % ("PASSED  *** SY1-2 IS EVIDENCE-VOID ***" if ctrl_passes
     else "FAILED as designed (criterion is eps_1-sensitive)"))
P("        REVIEW_PLD_S3 l.435 records 5 / 7 / 10 at eps_1 = 2   ->  %s"
  % ("REPRODUCES" if t_rs_ill == (5, 7, 10) else "DISAGREES"))
P()

# ---------------------------------------------------------------- SY1-4
r_rs = eta_RS(EPS_LIVE) / eta_q(EPS_LIVE)
r_kn = eta_KN(EPS_LIVE) / eta_q(EPS_LIVE)
half_a, half_b = r_rs < 1, r_kn > 1
v4 = ("ORDER-REVERSED (both halves)" if (half_a and half_b)
      else "HALF" if (half_a or half_b) else "NO-REVERSAL")
P("[SY1-4] eta_q(eps_live) = %.6e" % float(eta_q(EPS_LIVE)))
P("        eta_1^RS / eta_q = %.6e   (< 1 ? %s)" % (float(r_rs), half_a))
P("        eta_1^KN / eta_q = %.6f      (> 1 ? %s)" % (float(r_kn), half_b))
P("        exact eta_1^KN/eta_q = %s = %s" % (r_kn, 4608 * F(1, 117)))
P("        RLARGE l.65 records 'eta_1 <= eta_q'  ->  %s" % v4)
P("        N = 3 ratio: %.6f" % float(eta_KN(EPS_LIVE) / eta_q(EPS_LIVE, 3)))
P()

# ---------------------------------------------------------------- SY1-5
Cp = F(53)
c_flat = F(1, 640)
def window(tau_R, k=F(331, 10) * 10 ** 6):
    "largest C_D with tau_R <= theta_0^SUP / C' , theta_0^SUP = 1/(k C_D^2)"
    # tau_R <= 1/(k C_D^2 C')  <=>  C_D^2 <= 1/(k C' tau_R)
    return (1 / (k * Cp * tau_R))
tauR = F(275, 10 ** 17)                       # 2.75e-15
w2 = window(tauR)
import math
w = math.sqrt(float(w2))
ok5 = abs(w - 455.283301) <= 1e-4
w2c = window(tauR * 10)
wc = math.sqrt(float(w2c))
ctrl5_fails = not (abs(wc - 455.283301) <= 1e-4) and wc <= 150
P("[SY1-5] C_D window (tau_R <= theta_0^SUP/C'), tau_R = 2.75e-15 : C_D <= %.6f" % w)
P("        exact C_D^2 = %s" % w2)
P("        TAUFLAT [TF1-C] records 455.283301  ->  %s"
  % ("WINDOW-REPRODUCES" if ok5 else "DISAGREES"))
P("        CONTROL at tau_R = 2.75e-14: C_D <= %.6f  ->  %s"
  % (wc, "FAILED as designed" if ctrl5_fails else "CONTROL DID NOT FAIL"))
P()

# ---------------------------------------------------------------- SY1-6
# a_bad = c_flat * (theta_0^SUP / C')^2 ; coefficient of 1/C_D^4
th_stale = F(1, 10 ** 8)                      # SQ l.212  "1e-8 / C_D^2"
th_corr = F(3, 10 ** 8)                       # SQ l.216  "3e-8 / C_D^2"  (l.212 is 3x low)
a_stale = c_flat * (th_stale / Cp) ** 2
a_corr = c_flat * (th_corr / Cp) ** 2
hw_quoted = F(5, 10 ** 23)                    # HW l.604
ratio = a_corr / hw_quoted
v6 = ("STALE-CONFIRMED" if ratio >= 5 else "NO-DEFECT" if F(1, 2) <= ratio <= 2
      else "REPORTED-AS-COMPUTED")
P("[SY1-6] a_bad coefficient of 1/C_D^4 :")
P("        at SQ l.212's stale theta_0 = 1e-8/C_D^2  : %.6e" % float(a_stale))
P("        at SQ l.216's corrected      3e-8/C_D^2   : %.6e" % float(a_corr))
P("        HW l.604 quotes                           : %.6e" % float(hw_quoted))
P("        corrected / HW-quoted = %.4f   ->  %s" % (float(ratio), v6))
P("        exact theta_0 ratio corrected/stale = %s (square -> %s)"
  % (th_corr / th_stale, (th_corr / th_stale) ** 2))
P()
P("=" * 78)
P("VERDICTS: SY1-1 %s | SY1-2 %s | SY1-3 %s | SY1-4 %s | SY1-5 %s | SY1-6 %s"
  % (v1, v2.split()[0], "CONTROL-FAILED-AS-DESIGNED" if not ctrl_passes else "EVIDENCE-VOID",
     v4.split()[0], "WINDOW-REPRODUCES" if ok5 else "DISAGREES", v6))
P("=" * 78)

print("\n".join(OUT))
