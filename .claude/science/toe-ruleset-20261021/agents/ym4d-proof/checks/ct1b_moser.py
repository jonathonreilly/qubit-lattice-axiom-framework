#!/usr/bin/env python3
"""ct1b_moser.py -- POST-HOC corrections to ct1_moser.py, written after seeing ct1_out.txt.

Everything in this file is labelled post-hoc in CONST_T.md.  Three pre-registered verdicts of
ct1_criteria.md failed (B1, B2, B3); this script recomputes the same quantities with the three
errors of my own criteria fixed:

  (i)  i* = floor(log2 R) - 6 is ZERO on [64,128), not 1 -- so my B2 target was wrong and
       REVIEW_SQ_S4 S4-6 is exactly right;
  (ii) F is maximised at the RIGHT edge of each dyadic block, not the left, so the written
       schedule's max over R >= 128 is at R = 255, not R = 128;
  (iii) the optimised schedule's max over R >= 32 is 175.8 (> my 128 target), attained at R = 79.

It then does what ct1 did not: scan the Moser absorption exponent a = q/(q-4) over q, which is
the factor that decides the verdict.

Pure python, single thread, no BLAS, no lock.
"""
import math

OUT = []


def say(s=""):
    OUT.append(str(s))
    print(s)


def p_of(i):
    return 2.0 * 2 ** i


def B(m, istar=200):
    """prod_{i<istar} beta_i^{m/p_i}, beta_i = p_i - 1."""
    lg = sum((m / p_of(i)) * math.log(p_of(i) - 1.0) for i in range(istar))
    return math.exp(lg)


def F_of(R, gaps):
    lg = 2.0 * math.log(R)
    for i, d in enumerate(gaps):
        lg -= (2.0 / p_of(i)) * math.log(d)
    return math.exp(lg)


def written(R):
    istar = max(0, int(math.floor(math.log2(R))) - 6)
    return istar, [R * 2.0 ** (-i - 4) for i in range(istar)]


def optimised(R, dmin=12.0, budget_frac=0.5, inset=4.0):
    S = R * budget_frac - inset
    best = (0, [])
    istar = 1
    while istar <= 60:
        Lam = sum(2.0 ** (-i) for i in range(istar))
        gaps = [S * 2.0 ** (-i) / Lam for i in range(istar)]
        if gaps[-1] < dmin:
            break
        best = (istar, gaps)
        istar += 1
    return best


def scan(sched, R0, Rmax=2 ** 18, **kw):
    best = None
    Rs = list(range(R0, min(Rmax, 8193))) + [2 ** k for k in range(13, 19)]
    for R in Rs:
        if R < R0:
            continue
        istar, gaps = sched(R, **kw) if kw else sched(R)
        if istar == 0:
            continue
        F = F_of(R, gaps)
        if best is None or F > best[1]:
            best = (R, F, istar)
    return best


def main():
    say("=" * 80)
    say("POST-HOC 1 -- schedule factors F, with my criteria's three errors corrected")
    say("=" * 80)
    say("  written schedule, scanned over R >= 128 (REVIEW_SQ_S4 S4-6's fixed R_0):")
    bw = scan(written, 128)
    say("    max F = %.4f at R = %d (i* = %d)" % (bw[1], bw[0], bw[2]))
    for R in (128, 200, 255, 256, 511, 512, 1023, 4096, 65536):
        istar, gaps = written(R)
        say("      R=%-6d i*=%-3d F=%.4f" % (R, istar, F_of(R, gaps) if istar else R * R))
    say("    trivial branch for R < 128 forces C_T >= 127^2 = %d" % (127 ** 2))
    say()
    say("  optimised schedule (budget R/2 - 4, gaps prop 2^-i, dmin 12), R >= 32:")
    bo = scan(optimised, 32)
    say("    max F = %.4f at R = %d (i* = %d)" % (bo[1], bo[0], bo[2]))
    say("    asymptote F(R -> inf) = %.4f" % F_of(2 ** 18, optimised(2 ** 18)[1]))
    say("    trivial branch for R < 32 forces C_T >= 31^2 = %d" % (31 ** 2))
    say()
    say("  dmin sensitivity of the optimised max F and of the trivial floor:")
    for dmin in (4.0, 8.0, 12.0, 16.0, 24.0):
        R0 = int(math.ceil(2 * (dmin + 4.0)))
        b = scan(optimised, R0, dmin=dmin)
        say("    dmin=%-4g  R_0=%-4d  max F=%.3f at R=%-5d  trivial floor=(R_0-1)^2=%d"
            % (dmin, R0, b[1], b[0], (R0 - 1) ** 2))
    say()

    say("=" * 80)
    say("POST-HOC 2 -- beta-products B(m) = prod_{i>=0} beta_i^{m/p_i}")
    say("=" * 80)
    for m in (4.0, 4.1, 4.25, 4.5, 5.0, 6.0, 8.0):
        say("    m=%-5g B(m)=%12.4f   (crude bound 2^{2m} = %.4g)" % (m, B(m), 2.0 ** (2 * m)))
    say()

    say("=" * 80)
    say("POST-HOC 3 -- C_T(q):  a = q/(q-4) is the exponent on the potential norm")
    say("=" * 80)
    say("  C_T = sqrt(6) * F * B(4a) * Chat")
    say("  Chat = 0.5*(A_s gamma_s)^a + 0.5*(A_c gamma_c)^2 + 288*C_1*Q")
    say("  A_s gamma_s = 36 * C_1 * C_V * |N_1^plaq|     (the nbr exponents cancel exactly)")
    say("  A_c gamma_c = 36 * C_1 * |N_3^plaq|^{3/4} * c_c * eps_star   (V_c: sigma=4 always, a_c=2)")
    N1 = 3 ** 4 * 6
    N3 = 7 ** 4 * 6
    F = bo[1]
    say("  |N_1^plaq| = %d, |N_3^plaq|^{3/4} = %.1f, F = %.2f (optimised)" % (N1, N3 ** 0.75, F))
    say()

    def CT(q, C1, CV, cc=50.0, eps=1e-4, R0=32.0, verbose=False):
        a = q / (q - 4.0)
        Ag_s = 36.0 * C1 * CV * N1
        Ag_c = 36.0 * C1 * (N3 ** 0.75) * cc * eps
        # sup-norm of V, used only by the extra cutoff-type terms
        Vinf = CV * R0 ** (-2.0 + 8.0 / q)
        Q = 1.0 + 18.0 * Vinf * N1
        Chat = 0.5 * Ag_s ** a + 0.5 * Ag_c ** 2 + 288.0 * C1 * Q
        if verbose:
            say("        a=%.4f  (A g)_s=%.4g  term_s=%.4g  term_c=%.4g  288C1Q=%.4g  B=%.4g"
                % (a, Ag_s, 0.5 * Ag_s ** a, 0.5 * Ag_c ** 2, 288 * C1 * Q, B(4 * a)))
        return math.sqrt(6.0) * F * B(4.0 * a) * Chat

    say("  reference point C_1 = 20, C_V = 100, c_c = 50, eps_* = 1e-4:")
    say("    %-6s %-8s %-12s %s" % ("q", "a", "C_T", "verdict vs 1e13"))
    for q in (5, 6, 8, 12, 16, 24, 32, 50, 64, 100, 200, 400):
        v = CT(q, 20.0, 100.0)
        say("    %-6d %-8.4f %-12.4g %s" % (q, q / (q - 4.0), v, "UNDER" if v < 1e13 else "OVER"))
    say()
    say("  breakdown at q = 8 and q = 100 (reference point):")
    for q in (8, 100):
        say("      q=%d:" % q)
        CT(q, 20.0, 100.0, verbose=True)
    say()
    say("  sensitivity: C_T at q = 8 and q = 100 over the SUPPLIED constants")
    say("    %-10s %-10s %-14s %-14s" % ("C_1", "C_V", "C_T(q=8)", "C_T(q=100)"))
    for C1 in (5.0, 20.0, 100.0):
        for CV in (20.0, 100.0, 500.0):
            say("    %-10g %-10g %-14.4g %-14.4g" % (C1, CV, CT(8, C1, CV), CT(100, C1, CV)))
    say()
    say("  the q needed to bring C_T under 1e13, as a function of (C_1, C_V):")
    for C1 in (5.0, 20.0, 100.0):
        for CV in (20.0, 100.0, 500.0):
            qq = None
            for q in range(5, 4001):
                if CT(float(q), C1, CV) < 1e13:
                    qq = q
                    break
            say("    C_1=%-6g C_V=%-6g  q_min = %s" % (C1, CV, qq))
    say()
    say("  eps_* sensitivity of the V_c term at q = 100 (C_1=20, C_V=100):")
    for eps in (1e-2, 1e-4, 1e-6, 1e-8):
        say("    eps_*=%-8.0e  C_T = %.4g" % (eps, CT(100, 20.0, 100.0, eps=eps)))
    say()
    say("  the written schedule instead of the optimised one, at q=100 (factor F only):")
    say("    F_written(max, R>=128) = %.2f -> C_T scales by %.2f" % (bw[1], bw[1] / F))
    say("=" * 80)


if __name__ == "__main__":
    main()
