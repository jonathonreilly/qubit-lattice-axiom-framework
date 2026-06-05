#!/usr/bin/env python3
"""
BETA=6 SU(3) PLAQUETTE -- CERTIFIED CONVERGENT BACKBONE ENCLOSURE
================================================================

Rigorous (ball/interval-arithmetic) enclosure at beta=6 of the convergent
"backbone" of the Wilson plaquette expectation:

    <P>(6)  =  P_1plaq(6)  +  Delta_cube(6)  +  Delta_2cube^(w10)(6)  +  [non-cube remainder]
              \________________________ backbone ________________________/    \__ open wall __/

The three backbone sectors are CONVERGENT at beta=6 (nearest J-zero at |b|~8.205 > 6),
so each has a well-defined value; this runner certifies them to ~45 digits.

KEY RIGOROUS LEMMA (the certification rests on this):
    J(b) = int_{SU(3)} exp((b/3) Re Tr U) dU = sum_n a_n b^n,   a_n = (1/n!) E[((1/3)Re Tr U)^n].
    For SU(3), Re Tr U in [-3/2, 3], hence |(1/3) Re Tr U| <= 1, hence
        |a_n| <= 1/n!                                              (*)
    This is a RIGOROUS, closed-form bound on every Taylor coefficient. It gives a
    rigorous exponential tail bound  |sum_{n>N} a_n b^n| <= sum_{n>N} b^n/n!  (a tail of e^b),
    and likewise for J', J''. J is entire (order 1), so the series converges everywhere.

METHOD:
  - a_n computed EXACTLY (rationals) from the reproven order-3 Picard-Fuchs recurrence
        6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2},  a0=1,a1=0,a2=1/36.
  - partial sums S, S', S'' are EXACT; tails bounded rigorously by (*).
  - J(6), J'(6), J''(6) as rigorous intervals (mpmath.iv); J(6) certified > 0.
  - K'=J'/J, K''=J''/J-(J'/J)^2 by interval division (safe, J(6)>0).
  - Delta_cube   = 72   * K'' * (K')^5   (cube-sector closed form; reproduces d5..d8)
    Delta_2cube  = 1080 * K'' * (K')^9   (leading two-cube weight-10 closed form, #2598)
  - backbone = P_1plaq + Delta_cube + Delta_2cube, certified enclosure.

This is a certified rigorous VALUE (not a Monte-Carlo number) for 86.9% of the
0.5934 MC comparator. It does NOT close <P>(6): the non-cube remainder (~+0.078)
is the open rho_{p,q}(6) wall. See companion notes.

Status authority: independent audit lane only; cite effective_status from
docs/audit/data/audit_ledger.json. Forbidden-import clean: every number is
reproven from the SU(3) Haar single-link integral + the J recurrence; 0.5934 is
an after-the-fact comparator, never a derivation input.

Reprove-and-cite: the certified-holonomic-evaluation methodology is the standard
of Mezzarobba, "Rigorous Multiple-Precision Evaluation of D-Finite Functions in
SageMath" (arXiv:1607.01967); here it is realized directly via the closed-form
coefficient bound (*) + interval arithmetic, cited as method/comparator only.

Run:  python3 scripts/frontier_beta6_certified_backbone_2026_06_04.py
"""
import math
import sympy as sp
import mpmath as mp
from mpmath import iv

PASS = 0
FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1; print(f"  [PASS] {name}")
    else:
        FAIL += 1; print(f"  [FAIL] {name}  {detail}")

def a_coeffs(N):
    """Exact Picard-Fuchs coefficients a_0..a_{N+1} (sympy Rationals)."""
    a = {0: sp.Integer(1), 1: sp.Integer(0), 2: sp.Rational(1, 36)}
    for n in range(2, N + 1):
        a[n + 1] = (n * (n + 1) * a[n] + 2 * (2 * n + 3) * a[n - 1] + a[n - 2]) \
                   / (6 * (n + 1) * (n + 4) * (n + 5))
    return a

def Ttail(M):
    """Rigorous upper bound on sum_{m>M} 6^m/m!  =  tail of e^6."""
    num = mp.mpf(6) ** (M + 1) / mp.factorial(M + 1)
    return num * (1 / (1 - mp.mpf(6) / (M + 2)))   # valid since M+2 > 6

def main():
    print(__doc__.split("Run:")[0].strip()[:0] or "")  # keep stdout tidy
    print("BETA=6 CERTIFIED CONVERGENT BACKBONE\n" + "=" * 40)
    mp.mp.dps = 60
    N = 70
    a = a_coeffs(N + 1)

    # --- LEMMA CHECK: |a_n| <= 1/n!  (the rigorous coefficient bound) ---
    viol = [n for n in range(N) if abs(a[n]) > sp.Rational(1, math.factorial(n))]
    check("rigorous coefficient bound |a_n| <= 1/n! holds for all n<%d" % N,
          not viol, f"violations at {viol}")

    # --- seed sanity (a_n match the SU(3) Haar moments) ---
    check("seed a_0=1, a_1=0, a_2=1/36 (J(0)=1; E[ReTrU]=0; a_2=1/36)",
          a[0] == 1 and a[1] == 0 and a[2] == sp.Rational(1, 36))

    iv.dps = 50
    six = iv.mpf(6)
    def IVrat(r): return iv.mpf(int(r.p)) / iv.mpf(int(r.q))

    S   = sum(IVrat(a[n]) * six ** n                  for n in range(N + 1))
    Sp  = sum(n * IVrat(a[n]) * six ** (n - 1)        for n in range(1, N + 1))
    Spp = sum(n * (n - 1) * IVrat(a[n]) * six ** (n - 2) for n in range(2, N + 1))
    TJ, TJp, TJpp = Ttail(N), Ttail(N - 1), Ttail(N - 2)
    J   = S   + iv.mpf([-float(TJ),   float(TJ)])
    Jp  = Sp  + iv.mpf([-float(TJp),  float(TJp)])
    Jpp = Spp + iv.mpf([-float(TJpp), float(TJpp)])

    check("rigorous tails negligible (J tail < 1e-40)", float(TJ) < 1e-40,
          f"TJ={mp.nstr(TJ,3)}")
    check("J(6) certified strictly > 0 (so K=log J safe; nearest J-zero |b|~8.205>6)",
          J.a > 0, f"J in {J}")

    Kp = Jp / J
    Kpp = Jpp / J - (Jp / J) ** 2
    P1   = Kp
    Dcube = iv.mpf(72) * Kpp * Kp ** 5
    D2c   = iv.mpf(1080) * Kpp * Kp ** 9
    back  = P1 + Dcube + D2c

    def lohi(x):
        s = mp.nstr(x, 50).strip()
        if s.startswith('['):
            a, b = s.lstrip('[').rstrip(']').split(',')
            return mp.mpf(a), mp.mpf(b)
        return mp.mpf(s), mp.mpf(s)
    def half(x):
        lo, hi = lohi(x); return (hi - lo) / 2
    def encloses(x, val, tol=mp.mpf('1e-9')):
        lo, hi = lohi(x); return (lo - tol) <= mp.mpf(val) <= (hi + tol)
    print("\nCERTIFIED ENCLOSURES [lower, upper]:")
    for name, x in [("P_1plaq(6)", P1), ("Delta_cube(6)", Dcube),
                    ("Delta_2cube_w10(6)", D2c), ("BACKBONE(6)", back)]:
        lo, hi = lohi(x)
        print(f"  {name:20s} in [{mp.nstr(lo, 28)}, {mp.nstr(hi, 28)}]  (half-width {mp.nstr(half(x), 3)})")

    # --- cross-checks against the (non-certified) closed-form values on main ---
    check("P_1plaq(6) encloses 0.42253173965 (matches d9 runner)",  encloses(P1, '0.42253173965'))
    check("Delta_cube(6) encloses 0.06291341533 (cube closed form)",encloses(Dcube, '0.06291341533'))
    check("Delta_2cube_w10(6) encloses 0.03007958721 (#2598)",      encloses(D2c, '0.03007958721'))
    check("BACKBONE(6) encloses 0.51552474219 (certified)",         encloses(back, '0.51552474219'))
    check("backbone half-width < 1e-40 (certified to ~45 digits)",  half(back) < mp.mpf('1e-40'))

    frac = back.a / mp.mpf("0.5934") * 100
    print(f"\nCERTIFIED: backbone(6) >= {mp.nstr(back.a, 16)}")
    print(f"  accounts for >= {mp.nstr(frac, 6)}% of the 0.5934 Monte-Carlo comparator.")
    print(f"  Remaining {mp.nstr(100 - frac, 4)}% = the non-cube rho_{{p,q}}(6) wall (open).")

    print(f"\nSCORECARD: PASS={PASS} FAIL={FAIL}")
    return FAIL == 0

if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
