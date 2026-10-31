# ru55_1: U3 / (TC) / Lemma W-cb# arithmetic. Criteria: checks/ru55_1_criteria.md (written first).
# Exact Fractions only; square roots never enter a verdict (squares compared); floats only in labelled displays.
from fractions import Fraction as F
from math import isqrt

d, L = 4, 3
A_d = F((d - 1) * L * (L - 1), 2)
n_l = 4 * L ** 3 * (L - 1)
n_P = 6 * n_l
c_pr = F(1, 640 * 53 ** 2)
C_flat = L ** 2 + 1 + (12 + 3 * L) * A_d
EPS = F(1, 10 ** 30)  # a live-branch eps_1 for the branch gates only


def b1(kappa):
    return n_P + 12 * kappa * (1 + A_d) ** 2


def sqrt_disp(q):
    """display-only enclosure of sqrt(q) for a positive Fraction q (6 decimals)"""
    S = 10 ** 6
    r = isqrt(q.numerator * S * S // q.denominator)
    return f"[{r / S:.6f}, {(r + 1) / S:.6f}]"


def point(N, kappa, eps_loc_sq_override=None):
    out = {}
    B = b1(kappa)
    delta0 = min(F(1, 640 * N), F(2, N ** 3))
    # (eps_loc/eps_1)^2 on the square-root branch, and the branch gate B1
    el_sq_sqrtbranch = F(1, 4 * N * B)
    out['B1'] = el_sq_sqrtbranch <= F(1, 16)
    el_sq = el_sq_sqrtbranch if eps_loc_sq_override is None else eps_loc_sq_override
    # eta_q/eps_1 on the middle branch, and gate B2
    eq = F(1, 256 * N) / A_d
    out['B2'] = (eq <= F(1, 2 * L ** 2)) and (EPS * eq <= delta0 / A_d)
    # G1
    R2 = ((16 * N + 3) * A_d * eq) ** 2 / (el_sq / 4)
    out['R2'] = R2
    out['G1'] = 'FAILS' if R2 > 1 else 'HOLDS'
    out['G1_closed'] = (R2 == F((16 * N + 3) ** 2) * B / (4096 * N)) if eps_loc_sq_override is None else None
    # eta*/eps_1 squared: min{eta_q, eps_loc/(2(16N+3)A_d)} via squares
    cand_sq = el_sq / (4 * (16 * N + 3) ** 2 * A_d ** 2)
    estar_sq = min(eq ** 2, cand_sq)
    out['estar_is_etaq'] = (estar_sq == eq ** 2)
    # G4 entries (units eps_1^2)
    e1 = c_pr * el_sq / 4
    e2 = kappa * el_sq / (64 * N)
    e3 = c_pr * estar_sq
    out['e'] = (e1, e2, e3)
    out['G4_min'] = e3 < min(e1, e2)
    out['acb_over_abad'] = e3 / c_pr
    old3 = c_pr * eq ** 2
    out['shrink'] = old3 / e3
    out['G4_shrink_eq_R2'] = (old3 / e3 == R2)
    out['G5'] = e3 < c_pr
    # G2: U3's own fix vs CL (c)
    u3 = F(16 * N + 3, 128 * N) ** 2
    out['G2'] = u3 > F(1, 4 * N * B)
    out['G2a'] = u3 >= F(1, 2 * N * B)
    out['G2b'] = u3 >= F(1, 2 * N * n_P)
    # G6: eta' := eta_q / R ; (eta'/2)^2 = eq^2/(4 R^2) vs (eps^J_loc/C_flat)^2 = 1/(157^2 (1+A_d)^2 N C_flat^2)
    etap_half_sq = eq ** 2 / (4 * R2)
    etaq_half_sq = eq ** 2 / 4
    J_sq = F(1, 157 ** 2 * (1 + A_d) ** 2 * N * C_flat ** 2)
    out['G6_before'] = 'eps^J_loc/C_flat binds' if J_sq <= etaq_half_sq else 'eta_q/2 binds'
    out['G6_after'] = 'eps^J_loc/C_flat binds' if J_sq <= etap_half_sq else "eta'/2 binds"
    out['G6'] = 'UNCHANGED' if (J_sq <= etap_half_sq and J_sq <= etaq_half_sq) else 'CHANGED'
    out['G6_ratio'] = etap_half_sq / J_sq
    # G7: joint collar with eps^J_loc/2
    out['RJ2'] = ((16 * N + 3) * A_d * eq) ** 2 / (F(1, 157 ** 2 * (1 + A_d) ** 2 * N) / 4)
    return out


def g3(N, factor=F(1)):
    t = F(1)
    delta = factor * t / (16 * N + 3)
    x = t - 3 * delta
    a = (t - 3 * delta) >= 16 * N * delta
    b = (t - 3 * delta) >= t / 2
    c = (x / (2 * N) - 4 * delta) >= x / (4 * N)
    dd = x ** 2 / (4 * N) >= t ** 2 / (16 * N)
    return a, b, c, dd


def main():
    allpass = True
    controls_ok = True
    print("ru55_1: (TC), W-cb#, a_cb#, eps^J_nat, joint factor  [exact Fractions; displays labelled]")
    print(f"constants: A_d={A_d} n_P={n_P} c_pr={c_pr} C_flat={C_flat}")
    for N in (2, 3):
        a, b, c, dd = g3(N)
        ok = a and b and c and dd
        allpass &= ok
        print(f"G3 N={N}: (a) {a} (b) {b} (c) {c} (d) {dd} -> {'PASS' if ok else 'FAIL'}")
        a2, _, _, _ = g3(N, F(2))
        print(f"C2 N={N}: delta = 2t/(16N+3): (a) {a2} -> {'FAILS (as designed)' if not a2 else 'did not fail: CONTROL DOES NOT FIRE'}")
        controls_ok &= (not a2)
    for N in (2, 3):
        for kappa in (F(1), F(1, 4)):
            o = point(N, kappa)
            gates = o['B1'] and o['B2']
            print(f"\nN={N} kappa={kappa} b_1={b1(kappa)}: branch gates B1={o['B1']} B2={o['B2']}")
            if not gates:
                allpass = False
                print("  branch gate FAILED: point not reported")
                continue
            print(f"  G1: R^2 = {o['R2']} (display R in {sqrt_disp(o['R2'])}); closed form (16N+3)^2 b_1/(4096N) equal: {o['G1_closed']} -> (TC) {o['G1']}")
            allpass &= (o['G1_closed'] is True)
            print(f"  G2: U3 fix vs CL(c) INCOMPATIBLE: {o['G2']}; G2a (sqrt2-relaxed CL): {o['G2a']}; G2b (relaxed, b_1 -> n_P): {o['G2b']}")
            e1, e2, e3 = o['e']
            print(f"  G4: e1={e1} e2={e2} e3={e3}; e3 < min(e1,e2): {o['G4_min']}; a_cb#/a_bad = {o['acb_over_abad']} (display {float(o['acb_over_abad']):.6e})")
            print(f"      old third entry / e3 = {o['shrink']} == R^2: {o['G4_shrink_eq_R2']}")
            print(f"  C3: old/e3 == R (not R^2)? compare squares: (old/e3)^2 == R^2 -> {o['shrink'] ** 2 == o['R2']} (must be False)")
            controls_ok &= not (o['shrink'] ** 2 == o['R2'])
            print(f"  G5: a_D# = a_cb# (e3 < c_pr): {o['G5']}")
            print(f"  G6: before: {o['G6_before']}; after eta' = eta_q/R: {o['G6_after']} -> eps^J_nat {o['G6']}; (eta'/2)^2/(eps^J_loc/C_flat)^2 = {o['G6_ratio']} (display {float(o['G6_ratio']):.4f})")
            print(f"  G7: R_J^2 = {o['RJ2']} (display R_J in {sqrt_disp(o['RJ2'])})")
            allpass &= o['G4_min'] and o['G4_shrink_eq_R2'] and o['G5']
            # C1: eps_loc := eps_1/4
            oc = point(N, kappa, eps_loc_sq_override=F(1, 16))
            c1 = (oc['G1'] == 'HOLDS') and oc['estar_is_etaq']
            print(f"  C1: eps_loc := eps_1/4: R^2 = {oc['R2']} -> (TC) {oc['G1']}; eta* == eta_q: {oc['estar_is_etaq']} -> {'as designed' if c1 else 'CONTROL DOES NOT FIRE'}")
            controls_ok &= c1
    print(f"\nGATES: {'all PASS' if allpass else 'NOT all PASS'}; CONTROLS: {'all as designed' if controls_ok else 'NOT all as designed -> UNABLE TO DECIDE'}")


if __name__ == "__main__":
    main()
