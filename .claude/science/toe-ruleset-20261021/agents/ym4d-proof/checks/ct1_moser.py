#!/usr/bin/env python3
"""ct1_moser.py -- arithmetic of EPS-T's Moser telescope (SQ.md s15.1 step (6)).

Pre-registered criteria: checks/ct1_criteria.md.  Pure python, single thread, no BLAS, no lock.

Blocks:
  A  telescope identities and the beta-products  prod_{i<i*} beta_i^{m/p_i}
  B  radius schedules: F := R^2 * prod_{i<i*} d_i^{-2/p_i}   (written vs optimised)
  C  assembly  C_T = sqrt(6) * F * prod(beta^m/p) * Chat, on a table of SUPPLIED factor values

p_i := 2*2^i,  beta_i := p_i - 1.
"""
from fractions import Fraction as Fr
import math
import random

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


# ---------------------------------------------------------------- Block A
def block_A():
    say("=" * 78)
    say("BLOCK A -- telescope identities and beta-products")
    say("=" * 78)

    # A1: series sums, truncated at i = 200, exact rationals
    N = 200
    s1 = sum(Fr(1, 2 * 2 ** i) for i in range(N + 1))          # sum 1/p_i
    s2 = sum(Fr(i, 2 * 2 ** i) for i in range(N + 1))          # sum i/p_i
    s3 = sum(Fr(i + 1, 2 ** (i + 1)) for i in range(N + 1))    # sum (i+1)2^-(i+1)
    say("  sum_{i<=200} 1/p_i            = %.18f   (target 1)" % float(s1))
    say("  sum_{i<=200} i/p_i            = %.18f   (target 1)" % float(s2))
    say("  sum_{i<=200} (i+1)2^-(i+1)    = %.18f   (target 2)" % float(s3))
    a1 = abs(float(s1) - 1.0) < 1e-12 and abs(float(s3) - 2.0) < 1e-12
    say("  A1 verdict: %s" % ("PASS" if a1 else "FAIL"))
    say()

    # A2: beta-products
    say("  A2  prod_{i<i*} beta_i^{m/p_i},  beta_i = p_i - 1 = 2^{i+1} - 1")
    a2 = True
    for m in (2, 4, 8):
        prev = 0.0
        vals = []
        for istar in range(1, 61):
            lg = sum((m / (2.0 * 2 ** i)) * math.log(2.0 * 2 ** i - 1.0) for i in range(istar))
            v = math.exp(lg)
            vals.append(v)
            if v >= 2.0 ** (2 * m):
                a2 = False
            if v < prev - 1e-15:
                a2 = False
            prev = v
        say("    m=%d: i*=1 -> %.6g ; i*=4 -> %.6g ; i*=60 -> %.10g ; bound 2^%d = %d"
            % (m, vals[0], vals[3], vals[-1], 2 * m, 2 ** (2 * m)))
        say("          limit/bound ratio = %.6f" % (vals[-1] / 2.0 ** (2 * m)))
    say("  A2 verdict: %s" % ("PASS" if a2 else "FAIL"))
    say()
    return a1, a2


# ---------------------------------------------------------------- Block B
def F_of_schedule(R, gaps):
    """F = R^2 * prod_i d_i^{-2/p_i}  for the given gap list."""
    lg = 2.0 * math.log(R)
    for i, d in enumerate(gaps):
        lg -= (2.0 / (2.0 * 2 ** i)) * math.log(d)
    return math.exp(lg)


def written_schedule(R):
    """SQ.md l.1498-1503: r_i = R/2 + R 2^{-i-3}, d_i = R 2^{-i-4}, i* = floor(log2 R) - 6,
    gaps required >= 4."""
    istar = int(math.floor(math.log2(R))) - 6
    if istar < 0:
        istar = 0
    gaps = [R * 2.0 ** (-i - 4) for i in range(istar)]
    return istar, gaps


def optimised_schedule(R, budget_frac=0.5, inset=4.0, dmin=12.0):
    """gaps proportional to lambda_i = 2^{-i}, total budget = R*budget_frac - inset,
    i* = largest number of steps whose smallest gap is still >= dmin."""
    S = R * budget_frac - inset
    if S < dmin:
        return 0, []
    best = (0, [])
    istar = 1
    while istar <= 60:
        Lam = sum(2.0 ** (-i) for i in range(istar))
        gaps = [S * (2.0 ** (-i)) / Lam for i in range(istar)]
        if gaps[-1] < dmin:
            break
        best = (istar, gaps)
        istar += 1
    return best


def block_B():
    say("=" * 78)
    say("BLOCK B -- radius schedules, F = R^2 prod d_i^{-2/p_i}")
    say("=" * 78)

    # B2 first (cheap, structural)
    istar64 = [written_schedule(R)[0] for R in range(64, 128)]
    istar_small = [int(math.floor(math.log2(R))) - 6 for R in range(32, 64)]
    b2 = all(s == 1 for s in istar64) and all(s <= 0 for s in istar_small)
    say("  B2  written i* on R in [64,127]: set = %s ; on R in [32,63]: set = %s"
        % (sorted(set(istar64)), sorted(set(istar_small))))
    say("  B2 verdict: %s  (R_0 = 64 performs one step at most; S4-6 reproduced)"
        % ("PASS" if b2 else "FAIL"))
    say()

    # B1 written schedule scan
    Rs = list(range(64, 4097)) + [2 ** k for k in range(13, 19)]
    best = None
    for R in Rs:
        istar, gaps = written_schedule(R)
        if istar == 0:
            F = R * R  # no step: the trivial branch, sup <= ||w||_2 = R^2 * R^-2 ||w||_2
        else:
            F = F_of_schedule(R, gaps)
        if best is None or F > best[1]:
            best = (R, F)
    say("  B1  written schedule (budget R/8, dmin 4): max F over R in [64, 2^18]")
    say("        argmax R = %d, F = %.10f  (target: R=128, F=2048)" % best)
    for R in (64, 128, 129, 256, 1024, 65536):
        istar, gaps = written_schedule(R)
        F = R * R if istar == 0 else F_of_schedule(R, gaps)
        say("        R=%-7d i*=%-3d F=%.6f" % (R, istar, F))
    b1 = (best[0] == 128) and abs(best[1] - 2048.0) / 2048.0 < 1e-9
    say("  B1 verdict: %s" % ("PASS" if b1 else "FAIL"))
    say()

    # B3 optimised schedule scan
    say("  B3  optimised schedule (budget R/2 - 4, gaps prop to 2^-i, dmin 12)")
    best_o = None
    rows = []
    for R in list(range(32, 4097)) + [2 ** k for k in range(13, 19)]:
        istar, gaps = optimised_schedule(R)
        if istar == 0:
            continue
        F = F_of_schedule(R, gaps)
        p_last = 2.0 * 2 ** istar
        rows.append((R, istar, p_last, F))
        if best_o is None or F > best_o[3]:
            best_o = (R, istar, p_last, F)
    say("        max F = %.6f at R = %d (i* = %d, p_{i*} = %g)"
        % (best_o[3], best_o[0], best_o[1], best_o[2]))
    for R in (32, 48, 64, 128, 256, 1024, 65536):
        for r in rows:
            if r[0] == R:
                say("        R=%-7d i*=%-3d p_{i*}=%-8g F=%.6f" % r)
                break
    b3 = best_o[3] < 128.0
    say("  B3 verdict: %s" % ("PASS" if b3 else "FAIL"))
    say()

    # smallest R at which the optimised schedule runs at all
    Rmin = min(r[0] for r in rows)
    say("        smallest R with >=1 optimised step: %d  (trivial branch then gives C_T >= %d)"
        % (Rmin, Rmin * Rmin))
    # smallest R with at least 3 steps
    R3 = min([r[0] for r in rows if r[1] >= 3], default=None)
    say("        smallest R with >=3 optimised steps: %s" % R3)
    say()

    # B4 optimality of the proportional allocation
    random.seed(20261028)
    b4 = True
    say("  B4  is d_i proportional to 2^-i optimal for fixed i* and budget?")
    for istar in (2, 3, 4, 5):
        Lam = sum(2.0 ** (-i) for i in range(istar))
        base = [(2.0 ** (-i)) / Lam for i in range(istar)]
        pbase = 1.0
        for i, d in enumerate(base):
            pbase *= d ** (-2.0 / (2.0 * 2 ** i))
        worst = pbase
        for _ in range(2000):
            w = [random.random() + 1e-6 for _ in range(istar)]
            tot = sum(w)
            cand = [x / tot for x in w]
            p = 1.0
            for i, d in enumerate(cand):
                p *= d ** (-2.0 / (2.0 * 2 ** i))
            if p < worst:
                worst = p
            if p < pbase * (1 - 1e-12):
                b4 = False
        say("        i*=%d: proportional gives %.10f, best of 2000 random gives %.10f"
            % (istar, pbase, worst))
    say("  B4 verdict: %s" % ("PASS" if b4 else "FAIL"))
    say()
    return b1, b2, b3, b4, best, best_o, Rmin


# ---------------------------------------------------------------- Block C
def assemble(F, m, C1, gammaV, nbr_exp34, extra=1.0, a_exp=2):
    """C_T = sqrt(6) * F * 2^{2m} * Chat,  Chat = (9*4*nbr^{3/4}*C1*gammaV)^a / 4^{a-1}.

    a_exp = 2 reproduces the delta = 1/(2P) Young absorption actually used in the written route
    (cost P^2/2); a_exp = 1 is the sharp Trudinger/Serrin exponent sigma/(2 sigma - d) = 1 at
    (d, sigma) = (4, 4).
    """
    P_hat = 9.0 * 4.0 * nbr_exp34 * C1 * gammaV      # P = P_hat * beta^4 / R
    if a_exp == 2:
        Chat = P_hat ** 2 / 4.0
    else:
        Chat = P_hat
    Chat *= extra
    beta_fac = 2.0 ** (2 * m)
    return math.sqrt(6.0) * F * beta_fac * Chat, P_hat, Chat, beta_fac


def block_C(F_written, F_opt):
    say("=" * 78)
    say("BLOCK C -- assembly (REPORTED; inputs are SUPPLIED constants, see CONST_T.md)")
    say("=" * 78)
    N3 = 7 ** 4 * 6
    N1 = 3 ** 4 * 6
    say("  local multiplicities: |N_3| = 7^4*6 = %d, |N_3|^{3/4} = %.1f" % (N3, N3 ** 0.75))
    say("                        |N_1| = 3^4*6 = %d,  |N_1|^{3/4} = %.1f" % (N1, N1 ** 0.75))
    say()
    rows = [
        # label                               F          m  C1   gammaV nbr^{3/4}        a
        ("as written, N_3 maxima",            F_written, 8, 10.0, 230.0, N3 ** 0.75, 2),
        ("as written, N_1 maxima for V_s",    F_written, 8, 10.0, 230.0, N1 ** 0.75, 2),
        ("+ optimised schedule",              F_opt,     8, 10.0, 230.0, N1 ** 0.75, 2),
        ("+ beta^2 Caccioppoli (m=4)",        F_opt,     4, 10.0, 230.0, N1 ** 0.75, 2),
        ("+ sharp a = 1",                     F_opt,     4, 10.0, 230.0, N1 ** 0.75, 1),
        ("all three, C1=3 gammaV=50",         F_opt,     4, 3.0,   50.0, N1 ** 0.75, 1),
    ]
    say("  %-34s %8s %3s %6s %7s %9s %2s  %12s" %
        ("row", "F", "m", "C1", "gammaV", "nbr^3/4", "a", "C_T"))
    res = []
    for lab, F, m, C1, gV, nb, a in rows:
        CT, Ph, Ch, bf = assemble(F, m, C1, gV, nb, a_exp=a)
        res.append((lab, CT))
        say("  %-34s %8.1f %3d %6.1f %7.1f %9.1f %2d  %12.4g" %
            (lab, F, m, C1, gV, nb, a, CT))
    say()
    say("  threshold from REVIEW_SQ_S4 S4-16: C_T <~ 1e13")
    for lab, CT in res:
        say("    %-34s C_T = %-12.4g  %s" % (lab, CT, "UNDER 1e13" if CT < 1e13 else "OVER 1e13"))
    say()

    # one-factor-at-a-time sensitivity around the "as written, N_1" row
    say("  sensitivity (row 2 as the base point; each factor varied alone)")
    base = (F_written, 8, 10.0, 230.0, N1 ** 0.75, 2)
    CT0 = assemble(*base[:1], base[1], base[2], base[3], base[4], a_exp=base[5])[0]
    say("    base C_T = %.4g" % CT0)
    for name, idx, vals in (
        ("F", 0, [F_opt, F_written, 2048.0, 16384.0]),
        ("m", 1, [2, 4, 8]),
        ("C1", 2, [1.0, 3.0, 10.0, 100.0]),
        ("gammaV", 3, [10.0, 50.0, 230.0, 1000.0]),
        ("nbr^{3/4}", 4, [6.0 ** 0.75, N1 ** 0.75, N3 ** 0.75]),
        ("a", 5, [1, 2]),
    ):
        outs = []
        for v in vals:
            args = list(base)
            args[idx] = v
            CT = assemble(args[0], args[1], args[2], args[3], args[4], a_exp=args[5])[0]
            outs.append("%g->%.3g" % (v, CT))
        say("    %-12s %s" % (name, "   ".join(outs)))
    say()


def main():
    a1, a2 = block_A()
    b1, b2, b3, b4, best_w, best_o, Rmin = block_B()
    block_C(best_w[1], best_o[3])
    say("=" * 78)
    say("VERDICT SUMMARY (pre-registered A1 A2 B1 B2 B3 B4)")
    say("=" * 78)
    v = {"A1": a1, "A2": a2, "B1": b1, "B2": b2, "B3": b3, "B4": b4}
    for kk in ("A1", "A2", "B1", "B2", "B3", "B4"):
        say("  %s : %s" % (kk, "PASS" if v[kk] else "FAIL"))
    say("  OVERALL : %s" % ("PASS" if all(v.values()) else "FAIL"))
    say("  C1 block is REPORTED, no pre-registered verdict.")


if __name__ == "__main__":
    main()
