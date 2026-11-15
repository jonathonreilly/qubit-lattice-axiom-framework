# dag55_3: (TC) ε_loc/2 ≥ (16N + 3)A_dη_q against RLARGE's own ε_loc (frozen Proposition CL) and RS-lin's η_q.
# Criteria: checks/dag55_3_criteria.md (written first). Exact integers/Fractions only; floats only in labelled display.
from fractions import Fraction as F
from math import isqrt

d, L = 4, 3
SCALE = 10 ** 30


def sqrt_bounds(x):
    """rigorous [lo, hi] for sqrt(x), x a nonnegative Fraction, at resolution 1/SCALE"""
    num = x.numerator * SCALE * SCALE
    den = x.denominator
    # sqrt(num/den) = sqrt(num*den)/den
    r = isqrt(num * den)
    lo = F(r, den * SCALE)
    hi = F(r + 1, den * SCALE)
    assert lo * lo <= x <= hi * hi
    return lo, hi


def point(N, kappa):
    n_l = 4 * L ** 3 * (L - 1)
    n_P = 6 * n_l
    A_d = F((d - 1) * L * (L - 1), 2)
    b_1 = n_P + 12 * kappa * (1 + A_d) ** 2
    delta_0 = min(F(1, 640 * N), F(2, N ** 3))
    eps1 = F(1, 10 ** 30)  # any eps1 on the small branch; R is eps1-free there
    eta_entries = (eps1 / (2 * L ** 2), eps1 / (256 * N * A_d), delta_0 / A_d)
    eta_q = min(eta_entries)
    B1 = (eta_q == eps1 / (256 * N * A_d)) and (eps1 / (256 * N * A_d) <= delta_0 / A_d) and (eps1 / (256 * N * A_d) <= eps1 / (2 * L ** 2))
    s_lo, s_hi = sqrt_bounds(N * b_1)
    B2 = s_lo > 2  # 1/(2 sqrt(N b_1)) < 1/4
    # eps_loc = eps1 / (2 sqrt(N b_1)) on this branch
    rhs = (16 * N + 3) * A_d * eta_q
    # R = rhs / (eps_loc/2) = rhs * 4 sqrt(N b_1) / eps1
    R_lo = rhs * 4 * s_lo / eps1
    R_hi = rhs * 4 * s_hi / eps1
    verdict = "FAILS" if R_lo > 1 else ("HOLDS" if R_hi <= 1 else "UNDECIDED")
    # controls
    eps_loc_hand = (16 * N + 3) * eps1 / (128 * N)
    C1 = rhs / (eps_loc_hand / 2)
    C2 = rhs / ((eps1 / 4) / 2)
    return dict(N=N, kappa=kappa, b_1=b_1, A_d=A_d, n_P=n_P, eta_over_eps=eta_q / eps1, B1=B1, B2=B2,
                R_lo=R_lo, R_hi=R_hi, verdict=verdict, C1=C1, C2=C2)


def disp(x):
    return f"{float(x):.6g}"  # display only


def main():
    allC = True
    for N in (2, 3):
        for kappa in (F(1), F(1, 4)):
            r = point(N, kappa)
            print(f"N={N} κ={r['kappa']}: n_P={r['n_P']} A_d={r['A_d']} b_1={r['b_1']} η_q/ε_1={r['eta_over_eps']} "
                  f"gates B1={'PASS' if r['B1'] else 'FAIL'} B2={'PASS' if r['B2'] else 'FAIL'}")
            print(f"   R ∈ [{r['R_lo']}, {r['R_hi']}]  (display {disp(r['R_lo'])})  -> (TC) {r['verdict']}; "
                  f"η would have to be ≤ η_q/R, i.e. ×{disp(1 / r['R_hi'])} of η_q")
            c1ok = (r['C1'] == 1)
            c2ok = (r['C2'] <= 1)
            allC = allC and c1ok and c2ok and r['B1'] and r['B2']
            print(f"   C1 (RLARGE's hand ε_loc = (16N+3)ε_1/(128N)): R = {r['C1']} -> {'= 1 exactly (as designed)' if c1ok else 'NOT 1'}")
            print(f"   C2 (ε_loc := ε_1/4): R = {r['C2']} -> {'HOLDS (as designed)' if c2ok else 'does not hold'}")
    print(f"CONTROLS and gates: {'all as designed' if allC else 'NOT all as designed -> unable to decide'}")


if __name__ == "__main__":
    main()
