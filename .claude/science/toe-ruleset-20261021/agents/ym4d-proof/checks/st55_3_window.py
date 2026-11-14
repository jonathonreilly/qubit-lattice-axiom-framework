# st55_3 -- bracket the one-step positivity threshold tau_c(kappa_0) at the stripe on H_red(0).
# Criteria: st55_3_criteria.md (sha256 ef8f1d5e..., written 2026-10-29T06:07:47Z before this script).
# Uses st55_2_stripe.py's definitions unchanged (executed up to its main loop). Exact arithmetic only.
import os, time
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "st55_2_stripe.py")).read()
exec(SRC[:SRC.index("RES = {}")])          # definitions only (no main loop)

T1 = time.time()
grid = [F(1, n) for n in (80, 60, 50, 40, 35, 30, 25, 22, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4)]
kappas = [F(1, 4), F(1), F(4)]
sp = Space((0,))
table = {}
for tau in [F(0)] + grid:
    U, cb, sb = stripe(tau)
    kd = kernel_data(sp, U)
    for mu in range(d):
        Mbar = kd[mu][0]
        assert Mbar[1] == 0 and Mbar[2] == 0 and Mbar[3] == 0 and Mbar[0] > 0, "zero-mismatch premise fails"
    Hb = bare_hessian(sp, U)
    Hk = kernel_hessian(sp, kd)
    G = gauge_matrix(sp, U)
    B = nullspace(transpose(G), sp.dim)
    HbB = restrict(Hb, B); HkB = restrict(Hk, B)
    row = []
    for kap in kappas:
        M = [[HbB[p][q] + kap * HkB[p][q] for q in range(len(B))] for p in range(len(B))]
        pd = ldl_pd(M)
        table[(tau, kap)] = pd
        row.append(pd)
    log("tau = %-5s  PD(kappa=1/4, 1, 4) = %s   t=%.1fs" % (tau, row, time.time() - T1))

def bracket(kap):
    vals = [table[(t, kap)] for t in grid]
    mono = all(not (vals[i] is False and vals[i + 1] is True) for i in range(len(vals) - 1))
    plus = None; minus = None
    for t, v in zip(grid, vals):
        if v and minus is None:
            plus = t
        if (not v) and minus is None:
            minus = t
    return mono, plus, minus

res = {}
for kap in kappas:
    mono, plus, minus = bracket(kap)
    res[kap] = (mono, plus, minus)
    log("kappa_0 = %s: monotone %s ; last PD tau_+ = %s ; first non-PD tau_- = %s" % (kap, mono, plus, minus))

def mid(kap):
    _, p, m = res[kap]
    return (p + m) / 2 if (p is not None and m is not None) else None

m1, m4, mq = mid(F(1)), mid(F(4)), mid(F(1, 4))
w1 = res[F(1)][0] and res[F(1)][1] is not None and res[F(1)][2] is not None and F(1, 18) <= res[F(1)][1] and res[F(1)][2] <= F(1, 14)
w2 = res[F(4)][0] and m4 is not None and m1 is not None and F(14, 10) <= m4 / m1 <= F(26, 10)
w3 = res[F(1, 4)][0] and mq is not None and m1 is not None and F(35, 100) <= mq / m1 <= F(65, 100)
c1 = all(table[(F(0), k)] for k in kappas)
c2 = (not table[(F(1, 4), F(1, 4))]) and (not table[(F(1, 4), F(1))])
log("W1 (kappa=1 bracket inside [1/18, 1/14], monotone):", w1)
log("W2 (tau_c(4)/tau_c(1) in [1.4, 2.6]):", w2, " ratio of midpoints =", (m4 / m1) if (m4 and m1) else None)
log("W3 (tau_c(1/4)/tau_c(1) in [0.35, 0.65]):", w3, " ratio of midpoints =", (mq / m1) if (mq and m1) else None)
log("C1 (tau = 0 PD for all kappa):", c1, "; C2 (tau = 1/4 not PD for kappa = 1/4, 1):", c2)
log("OVERALL:", "PASS" if (w1 and w2 and w3 and c1 and c2) else "FAIL (see the predictions above)", " total %.1fs" % (time.time() - T1))
