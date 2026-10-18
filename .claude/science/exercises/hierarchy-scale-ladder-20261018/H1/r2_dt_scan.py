"""R2: dimensional transmutation with b0 fixed by content (HIER-1 mechanism (b)).

Convention: mu dg/dmu = -b0 g^3/(16 pi^2) - b1 g^5/(16 pi^2)^2,
b0 = (11/3) C_A - (4/3) T_F N_f,  b1 = (34/3) C_A^2 - 4 C_F T_F N_f - (20/3) C_A T_F N_f,
fundamental Dirac flavours, T_F = 1/2.  One-loop: Lambda/mu = exp(-8 pi^2/(b0 g^2)).
Two-loop: Lambda/mu = (b0 g^2/(16 pi^2))^(-b1/(2 b0^2)) exp(-8 pi^2/(b0 g^2)) (b1 > 0 only).
Banks-Zaks two-loop fixed point: g*^2 = -16 pi^2 b0/b1 when b0 > 0 > b1.
Supplied: the gauge group SU(N) and N_f (NOT built on the one-qubit ladder chain),
g_bare^2 = 1 (the repo's convention/open gate), u0 = 0.5934^(1/4) for scheme spread.
"""
from fractions import Fraction as Fr
import math

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok)
    FAIL += (not ok)
    print(("PASS" if ok else "FAIL"), name, detail)


def coeffs(N, Nf):
    CA = Fr(N)
    CF = Fr(N * N - 1, 2 * N)
    TF = Fr(1, 2)
    b0 = Fr(11, 3) * CA - Fr(4, 3) * TF * Nf
    b1 = Fr(34, 3) * CA ** 2 - 4 * CF * TF * Nf - Fr(20, 3) * CA * TF * Nf
    return b0, b1


def decades_1loop(b0, g2):
    return 8 * math.pi ** 2 / (float(b0) * g2 * math.log(10))


def decades_2loop(b0, b1, g2):
    b0f, b1f = float(b0), float(b1)
    pref = (b0f * g2 / (16 * math.pi ** 2)) ** (-b1f / (2 * b0f ** 2))
    return decades_1loop(b0, g2) - math.log10(pref)


u0 = 0.5934 ** 0.25
schemes = {"g2=1 (alpha_bare)": 1.0, "g2=1/u0 (alpha_LM)": 1 / u0, "g2=1/u0^2 (alpha_s)": 1 / u0 ** 2}

print("== SU(3), N_f fundamental Dirac, g^2 = 1 ==")
print(" Nf   b0      b1        dec1L   dec2L(b1>0)  g*^2(BZ)")
for Nf in range(0, 17):
    b0, b1 = coeffs(3, Nf)
    d1 = decades_1loop(b0, 1.0)
    d2 = decades_2loop(b0, b1, 1.0) if b1 > 0 else float("nan")
    gs = -16 * math.pi ** 2 * float(b0) / float(b1) if b1 < 0 else float("nan")
    print(f" {Nf:2d}  {str(b0):6s}  {str(b1):8s}  {d1:7.2f}  {d2:9.2f}   {gs:7.3f}")

b0_16, b1_16 = coeffs(3, 16)
check("SU(3) N_f=16: b0 = 1/3 (main: YT P2 / BBS O2 surface)", b0_16 == Fr(1, 3), f"b1 = {b1_16}")

# max decades among SU(3) contents with b1 > 0 (perturbative two-loop flow has no IR fixed point)
best = max((decades_2loop(*coeffs(3, Nf), 1.0), Nf) for Nf in range(0, 17) if coeffs(3, Nf)[1] > 0)
check("SU(3), b1 > 0 contents at g^2=1 reach at most ~6 decades", best[0] < 15, f"max {best[0]:.2f} decades at N_f={best[1]}")

need = [Nf for Nf in range(0, 17) if decades_1loop(coeffs(3, Nf)[0], 1.0) >= 15]
check("SU(3): every N_f with >= 15 one-loop decades has b1 < 0", all(coeffs(3, Nf)[1] < 0 for Nf in need),
      f"N_f reaching 15 decades: {need}")

print("== lemma: for SU(N), N=2..100, (one-loop decades >= 15 at g^2=1) => b1 < 0 ==")
ok = True
worst = None
for N in range(2, 101):
    nf_max = int(Fr(11 * N, 2))
    for Nf in range(0, nf_max + 1):
        b0, b1 = coeffs(N, Nf)
        if b0 <= 0:
            continue
        if decades_1loop(b0, 1.0) >= 15 and not b1 < 0:
            ok = False
            worst = (N, Nf)
check("lemma holds for N=2..100", ok, f"counterexample {worst}")
# analytic margin: b0 <= b0_crit := 8 pi^2/(15 ln10) needs N_f >= (11N - 3 b0_crit)/2;
# b1 < 0 iff N_f > 34 N^3/(13 N^2 - 3).  Margin at each N:
b0c = 8 * math.pi ** 2 / (15 * math.log(10))
margins = [((11 * N - 3 * b0c) / 2) - 34 * N ** 3 / (13 * N ** 2 - 3) for N in range(2, 101)]
check("analytic margin positive for N=2..100", min(margins) > 0,
      f"b0_crit = {b0c:.4f}; min margin {min(margins):.3f} flavours (N=2)")

print("== scheme spread (g^2 at the grid rung) for SU(3) ==")
for name, g2 in schemes.items():
    row = []
    for Nf in (0, 6, 12, 13, 16):
        row.append(f"Nf={Nf}:{decades_1loop(coeffs(3, Nf)[0], g2):.2f}")
    print(" ", name, f"g2={g2:.4f}", " ".join(row))

# required b0 for the hierarchy number of the formula, K = 2.017e-17 (16.70 decades)
b0_req = 8 * math.pi ** 2 / (16.695 * math.log(10))
print(f"b0 needed for 16.70 decades at g^2=1: {b0_req:.4f} (SU(3) N_f would be {(33 - 3 * b0_req) / 2:.2f})")

print("== U(1) with charged Dirac content ==")
# QED: mu de/dmu = + (sum q^2) e^3/(12 pi^2): b0 = -(4/3) sum q^2 < 0 for any charged content
for charges in ([1], [1, 1, 1], [1] * 16, [Fr(1, 3)] * 3):
    b0 = -Fr(4, 3) * sum(Fr(q) ** 2 for q in charges)
    check(f"U(1) charges {charges[:3]}{'...' if len(charges) > 3 else ''}: b0 < 0 (not asymptotically free)", b0 < 0, f"b0 = {b0}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
