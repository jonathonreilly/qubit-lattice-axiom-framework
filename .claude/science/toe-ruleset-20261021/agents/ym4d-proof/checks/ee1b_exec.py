#!/usr/bin/env python3 -I
"""ee1b_exec.py -- RE-RUN of ee1-1 only, under a new id, criteria UNTOUCHED.

Why: ee1_exec.py returned DOES-NOT-FACTORISE on ee1-1 because of a transcription
error IN MY OWN SCRIPT -- E_OLD_PRE was written F(12687,10)*1e-39 = 1.2687e-36,
a factor 1e3 too large. The three failing ratios were 1000.2, 999.5, 1002.1,
which is the signature. ee1_out.txt is kept unaltered and the FAIL stands as
reported; this file re-runs the SAME pre-registered gate with the transcription
corrected and nothing else changed.

Note on the first run's power claim: the designed-FAIL control also returned
DOES-NOT-FACTORISE, but for the SAME common cause, so the first run's
"HAS-POWER" line was not supported by its own evidence. The power verdict is
established here instead, where main and control separate.

ee1-2, ee1-3 and ee1-4 are NOT re-run: their arithmetic did not touch
E_OLD_PRE, their controls separated cleanly, and their verdicts stand as in
ee1_out.txt.

Also adds the (C4) false-precision probe, which is POST-HOC (written after
reading ee1-2(a)'s NO-DISCRIMINATION) and labelled as such in the output.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 50


def D(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def log10(x):
    return D(x).log10()


# ------------------------------------------------ transcriptions (corrected)
E_OLD_PRE = F(12687, 10 ** 4) * F(10) ** -39   # 1.2687e-39  REVIEW_SF_S7 l.196; SF l.2837; NORMS l.746
E_RERUN_PRE = F(952, 100) * F(10) ** -40       # 9.52e-40    RLARGE l.71; REVIEW_SF_S7 l.53,247
E_OLD_TB = F(895, 100) * F(10) ** -40          # 8.95e-40    REVIEW_SF_S7 l.47,200,297; RLARGE l.611
E_RERUN_TB = F(67, 10) * F(10) ** -40          # 6.7e-40     RLARGE l.72,612

TB1 = F(7056, 10000)                           # 0.7056      REVIEW_SF_S7 l.199-200
CLASS = F(75, 100)                             # x0.75       REVIEW_SF_S7 l.251

out = []


def say(s=""):
    out.append(s)


say("=" * 78)
say("ee1b-1  RE-RUN of ee1-1 (C6), criteria file untouched")
say("=" * 78)


def factorise(tb1_factor, label):
    cells = [
        ("old", "pre", E_OLD_PRE, F(1)),
        ("old", "TB1", E_OLD_TB, tb1_factor),
        ("rerun", "pre", E_RERUN_PRE, CLASS),
        ("rerun", "TB1", E_RERUN_TB, CLASS * tb1_factor),
    ]
    worst = F(1)
    say("")
    say(f"-- {label}: TB-1 factor = {D(tb1_factor)}")
    say(f"{'class':8s} {'corr':5s} {'recorded':>16s} {'predicted':>16s} {'ratio':>12s}")
    for cls, corr, recorded, fac in cells:
        pred = E_OLD_PRE * fac
        ratio = pred / recorded
        say(f"{cls:8s} {corr:5s} {D(recorded):16.6E} {D(pred):16.6E} {D(ratio):12.6f}")
        worst = max(worst, ratio if ratio >= 1 else 1 / ratio)
    verdict = "FACTORISES" if worst <= F(101, 100) else "DOES-NOT-FACTORISE"
    say(f"worst deviation = x{D(worst):.6f}   ->  {verdict}")
    return verdict


v_main = factorise(TB1, "MAIN")
v_ctrl = factorise(F(1, 2), "DESIGNED-FAIL CONTROL (TB-1 replaced by 1/2)")

say("")
say(f"ee1b-1 MAIN    : {v_main}")
say(f"ee1b-1 CONTROL : {v_ctrl}   (criteria require DOES-NOT-FACTORISE)")
say("ee1b-1 POWER   : " + ("HAS-POWER (main and control separate)"
                           if v_main == "FACTORISES" and v_ctrl == "DOES-NOT-FACTORISE"
                           else "NO POWER"))

say("")
say("Which cell is predicted by which factor, i.e. where the independence lies:")
say("  base 1.2687e-39            REVIEW_SF_S7 l.196  ((TH-ch') at tau^A, a_p entry only, old class)")
say("  x 0.7056 (TB-1)            REVIEW_SF_S7 l.199  (full (TH-bg) min{a_p,a_c}, n_K term)")
say("  x 0.75   (class)           REVIEW_SF_S7 l.251  ('slightly worse (x0.75) otherwise')")
say("  -> 6.7e-40                 RLARGE l.72, l.612; REVIEW_SF_S7 l.53, l.247, l.297")
say("  Neither factor was read from the cell it predicts.")

# ------------------------------------------------ POST-HOC: (C4) false precision
say("")
say("=" * 78)
say("[POST-HOC, EE1-P1]  (C4): at what precision in eta_flat does the verdict live?")
say("Written AFTER seeing ee1-2(a) return NO-DISCRIMINATION. Not pre-registered.")
say("=" * 78)

E_PROP = F(938495112638, 10 ** 11) * F(10) ** -45
E_TAUFLAT = F(938496, 10 ** 5) * F(10) ** -45

say("")
say("eta_flat as published, and as EPS1_SWEEP 4.5 carries it:")
cands = [
    ("TAUFLAT l.196, l.213   (6 s.f.)", F(352310, 10 ** 5) * F(10) ** -88),
    ("TAUFLAT l.561          (3 s.f.)", F(352, 100) * F(10) ** -88),
    ("EPS1_SWEEP 4.5        (12 s.f.)", F(352309230578, 10 ** 11) * F(10) ** -88),
]
say(f"{'eta_flat source':34s} {'value':>22s} {'prop HOLDS':>11s} {'TAUFLAT HOLDS':>14s}")
for nm, eb in cands:
    say(f"{nm:34s} {D(eb):22.12E} {str(4 * E_PROP ** 2 <= eb):>11s} "
        f"{str(4 * E_TAUFLAT ** 2 <= eb):>14s}")

say("")
say("So the (C4) discrimination exists only at >= 7 significant figures of eta_flat.")
say("Relative gap between the two candidate cuts:")
say(f"  (TAUFLAT / proposed) - 1 = {D(E_TAUFLAT / E_PROP - 1):.4E}")
say("Relative width of eta_flat's own input band, from C_D ~ (0.5-0.9)e3*C_T (S4-16):")
band = (F(9, 10) / F(5, 10)) ** 4          # eta_flat ~ C_D^-4
say(f"  eta_flat varies by x{D(band):.4f} across the C_D band alone "
    f"= {log10(band):.4f} decades")
cut_band = (F(9, 10) / F(5, 10)) ** 2      # cut ~ C_D^-2
say(f"  the CUT itself varies by x{D(cut_band):.4f} across that band "
    f"= {log10(cut_band):.4f} decades")
say("")
say(f"  ratio of (input band width) to (the gap (C4) adjudicates) = "
    f"x{D((cut_band - 1) / (E_TAUFLAT / E_PROP - 1)):.3E}")
say("  i.e. (C4) adjudicates a gap ~10^-6 relative inside an input band of ~x3.24.")

print("\n".join(out))
