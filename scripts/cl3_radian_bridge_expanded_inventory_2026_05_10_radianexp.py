#!/usr/bin/env python3
"""Supplied finite arithmetic/search, not a framework exclusion or phase prediction.
P_VEV_NUM remains the original binary float promoted to mpmath at 50 dps.
APBC fourth-power factor is a historical catalogue label; Fraction(7, 8) is supplied.
All old literal-True assertions are reported as unscored history.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md',)

def historical(label, condition, detail=''):
    print(f'HISTORICAL_UNSCORED (not a current assertion): {label!r}; old predicate={bool(condition)}; old detail={detail!r}')
import math
from fractions import Fraction
from itertools import product
try:
    import mpmath as mp
    mp.mp.dps = 50
    HAVE_MPMATH = True
except Exception:
    HAVE_MPMATH = False

def heading(s: str) -> None:
    print()
    print('=' * 72)
    print(s)
    print('=' * 72)

def check(label: str, condition: bool, detail: str='') -> bool:
    if condition:
        print(f'  PASS  {label}')
        if detail:
            print(f'        {detail}')
        return True
    print(f'  FAIL  {label}')
    if detail:
        print(f'        {detail}')
    return False
RETAINED_RATIONALS = {'1/3': Fraction(1, 3), '2/3': Fraction(2, 3), '2/9': Fraction(2, 9), '8/9': Fraction(8, 9), '1/9': Fraction(1, 9), '1/2': Fraction(1, 2), '1/4': Fraction(1, 4), '1/5': Fraction(1, 5), '7/8': Fraction(7, 8), '7/9': Fraction(7, 9), '7/18': Fraction(7, 18), '4/3': Fraction(4, 3), '13/3': Fraction(13, 3), '37/2': Fraction(37, 2), '3071/36': Fraction(3071, 36), '20873/48': Fraction(20873, 48), '5/9': Fraction(5, 9), '47/486': Fraction(47, 486), '16891/43740': Fraction(16891, 43740), '41/10': Fraction(41, 10), '-19/6': Fraction(-19, 6), '-7': Fraction(-7, 1), '16': Fraction(16, 1), '18': Fraction(18, 1), '2': Fraction(2, 1), '3': Fraction(3, 1), '7': Fraction(7, 1), '26': Fraction(26, 1)}
P_VEV_NUM = 0.5934

def list_retained_inventory_pi_status() -> list[tuple[str, str, bool]]:
    return [('1/3, 2/3, 2/9, 8/9, 1/9, 1/2, 1/4, 1/5', 'Cl(3)/Z^3 group-theory', False), ('7/8', 'APBC fourth-power factor', False), ('7/9', 'SU(3) NLO C-iso', False), ('7/18', 'taste_weight = (7/8)(T_F)(R_conn)', False), ('4/3', 'Casimir C_2 of SU(3) fundamental', False), ('13/3, 37/2, 3071/36, 20873/48', 'Wilson NNLO/NNNLO/N4LO/N5LO', False), ('5/9, 47/486, 16891/43740', 'C-iso NLO+ discrepancy', False), ('41/10, -19/6, -7', 'SM one-loop beta b_1, b_2, b_3', False), ('16, 18', 'Wilson chain exponents (4D taste)', False), ('7, 26', 'QCD N_f=6 beta_0, beta_1', False), ('<P> = 0.5934', 'single computed input (lattice MC)', False), ('u_0 = <P>^{1/4} = 0.8776', 'tadpole improvement', False), ('alpha_bare = 1/(4*pi)', 'QED canonical normalization (CONTAINS pi)', True), ('alpha_LM = alpha_bare/u_0', 'inherits 1/(4*pi) (CONTAINS pi)', True), ('alpha_s(v) = alpha_bare/u_0^2', 'inherits 1/(4*pi) (CONTAINS pi)', True)]

def main() -> int:
    for rel in AUDIT_INPUT_PATHS:
        if not (ROOT / rel).is_file():
            print(f'Missing declared input: {rel}')
            return 1
    pass_count = 0
    fail_count = 0

    def tally(ok: bool) -> None:
        nonlocal pass_count, fail_count
        if ok:
            pass_count += 1
        else:
            fail_count += 1
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    items = list_retained_inventory_pi_status()
    print()
    rat_count = 0
    pi_count = 0
    for label, role, has_pi in items:
        marker = '[contains pi]' if has_pi else '[no explicit pi]'
        if has_pi:
            pi_count += 1
        else:
            rat_count += 1
        print(f'UNSCORED LEGACY DATA (historical labels):     {marker:<18} {label:<45} -- {role}')
    print()
    print(f'UNSCORED LEGACY DATA (historical labels):   Inventory size: {len(items)} groups.')
    print(f'UNSCORED LEGACY DATA (historical labels):   Groups without explicit pi (not rationality): {rat_count}')
    print(f'UNSCORED LEGACY DATA (historical labels):   pi-containing groups: {pi_count}')
    tally(check('1.1 Catalogue has at least fourteen groups', len(items) >= 14, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    tally(check('1.2 At least eleven catalogue groups have no explicit pi in their supplied expression (not rationality)', rat_count >= 11, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    tally(check('1.3 Exactly three catalogue groups explicitly use pi', pi_count == 3, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    new_rationals_since_probe30 = [('c_3 (NNLO Wilson)', Fraction(-13, 3), 'PR #857 SU(3) NNLO note'), ('c_4 (NNNLO)', Fraction(-37, 2), 'PR #857'), ('c_5 (N4LO)', Fraction(-3071, 36), 'PR #857'), ('c_6 (N5LO)', Fraction(-20873, 48), 'PR #857'), ('beta_0 at N_f=6', Fraction(7, 1), 'QCD beta retained'), ('beta_1 at N_f=6', Fraction(26, 1), 'PR #917 closed-form'), ('Wilson chain exp 18', Fraction(18, 1), 'PR #799 Probe 19'), ('phi_dimensionless 2/9', Fraction(2, 9), 'PR #814 Probe 24 Step 1'), ('4/3 Casimir', Fraction(4, 3), 'SU(3) fundamental'), ('7/9 NLO C-iso', Fraction(7, 9), 'PR #685 / PR #857'), ('5/9 NNLO C-iso disc.', Fraction(5, 9), 'PR #857')]
    print()
    print(f'UNSCORED LEGACY DATA (historical labels):   Supplementary supplied Fraction rows: {len(new_rationals_since_probe30)}')
    for label, frac, src in new_rationals_since_probe30:
        print(f'UNSCORED LEGACY DATA (historical labels):     {label:<25} = {str(frac):<15} ({src})')
    tally(check('2.1 Supplementary supplied Fraction list has at least eleven rows', len(new_rationals_since_probe30) >= 11, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    tally(check('2.2 All supplementary values are Fraction instances', all((isinstance(f, Fraction) for _, f, _ in new_rationals_since_probe30)), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('2.3 Lindemann-Weierstrass forbids transcendental output from rational input', True, 'pi is transcendental over Q; (Q-finite combinations of rationals) is a subset of Q; pi NOT in Q')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    if not HAVE_MPMATH:
        tally(check('3.0 Required mpmath availability', False, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    else:
        historical('3.0 mpmath available', True, f'using {mp.mp.dps} decimal places')
        targets = {'2*pi': mp.mpf(2) * mp.pi, 'pi': mp.pi, 'pi/2': mp.pi / 2, 'pi/3': mp.pi / 3, 'pi/9': mp.pi / 9, '4*pi': mp.mpf(4) * mp.pi, '1/(2*pi)': mp.mpf(1) / (mp.mpf(2) * mp.pi), '(2/9)*2*pi': mp.mpf(2) / 9 * mp.mpf(2) * mp.pi}
        print()
        print(f'UNSCORED LEGACY DATA (historical labels):   pi (50 dps) = {mp.nstr(mp.pi, 50)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   2*pi (50 dps) = {mp.nstr(mp.mpf(2) * mp.pi, 50)}')
        candidates = []
        for name, q in RETAINED_RATIONALS.items():
            v = mp.mpf(q.numerator) / mp.mpf(q.denominator)
            if v != 0:
                candidates.append((name, v))
        candidates.append(('<P>', mp.mpf(P_VEV_NUM)))
        candidates.append(('u_0', mp.mpf(P_VEV_NUM) ** mp.mpf('0.25')))
        alpha_bare = mp.mpf(1) / (mp.mpf(4) * mp.pi)
        candidates.append(('alpha_bare', alpha_bare))
        u_0 = mp.mpf(P_VEV_NUM) ** mp.mpf('0.25')
        alpha_LM = alpha_bare / u_0
        alpha_s_v = alpha_bare / u_0 ** 2
        candidates.append(('alpha_LM', alpha_LM))
        candidates.append(('alpha_s(v)', alpha_s_v))
        print(f'UNSCORED LEGACY DATA (historical labels): \n  {len(candidates)} candidate atoms.')
        near_misses = []
        TOL_STRICT_NUMERIC = mp.mpf('1e-30')
        TOL_SOFT = mp.mpf('1e-3')
        for name, v in candidates:
            for tname, tval in targets.items():
                if v == 0 or tval == 0:
                    continue
                err = abs(v - tval) / abs(tval)
                if err < TOL_SOFT:
                    near_misses.append((tname, name, mp.nstr(v, 15), float(err)))
        for (n1, v1), (n2, v2) in product(candidates, repeat=2):
            if v1 == 0 or v2 == 0:
                continue
            for op, val in [(f'{n1} * {n2}', v1 * v2), (f'{n1} / {n2}', v1 / v2)]:
                for tname, tval in targets.items():
                    err = abs(val - tval) / abs(tval)
                    if err < TOL_SOFT:
                        near_misses.append((tname, op, mp.nstr(val, 15), float(err)))
        small_coeffs = [-3, -2, -1, 1, 2, 3, 4, 6, 8, 9]
        for (n1, v1), (n2, v2) in product(candidates, repeat=2):
            if v1 == 0 and v2 == 0:
                continue
            for c1 in small_coeffs:
                for c2 in small_coeffs:
                    val = c1 * v1 + c2 * v2
                    for tname, tval in targets.items():
                        err = abs(val - tval) / abs(tval)
                        if err < TOL_SOFT and abs(val) > 0.001:
                            near_misses.append((tname, f'{c1}*{n1} + {c2}*{n2}', mp.nstr(val, 15), float(err)))
        print()
        print(f'UNSCORED LEGACY DATA (historical labels):   Near-misses (error < 1e-3):')
        near_misses.sort(key=lambda r: r[3])
        for r in near_misses[:30]:
            tname, expr, val, err = r
            print(f'UNSCORED LEGACY DATA (historical labels):     target {tname:<10} : {expr:<55} = {val} (rel.err {err:.3e})')
        exact_matches = [r for r in near_misses if r[3] < float(TOL_STRICT_NUMERIC)]
        historical('3.1 Numerical search completed across pair-products and small-coeff sums', True, f'{len(near_misses)} near-misses (err<1e-3); {len(exact_matches)} strict numerical matches (err<1e-30)')
        exact_matches_pure = [r for r in exact_matches if 'alpha_bare' not in r[1] and 'alpha_LM' not in r[1] and ('alpha_s(v)' not in r[1]) and ('<P>' not in r[1]) and ('u_0' not in r[1])]
        tally(check('3.2 No filtered rational-atom search result meets numerical threshold 1e-30', len(exact_matches_pure) == 0, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
        heading('Supplied finite diagnostic block; historical conclusions withdrawn')
        print()
        print()
        print(f'UNSCORED LEGACY DATA (historical labels):   1/(4 * alpha_bare) = {mp.nstr(1 / (4 * alpha_bare), 50)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   pi                 = {mp.nstr(mp.pi, 50)}')
        ratio_check = 1 / (4 * alpha_bare)
        agrees = abs(ratio_check - mp.pi) < mp.mpf('1e-40')
        print(f'UNSCORED LEGACY DATA (historical labels):   agree?             = {agrees}')
        tally(check('4.1 Supplied reciprocal identity meets tolerance 1e-40', bool(agrees), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
        print()
        print()
        print()
        print()
        print()
        historical('4.2 alpha_bare = 1/(4*pi) inherits pi via continuum-matching convention', True, 'The 4*pi factor is the (2*pi)^d momentum-integration normalization, i.e. the period convention')
        historical('4.3 Therefore: pi in alpha_bare is NOT a derivation, it is the same primitive P', True, 'Cannot use alpha_bare to derive pi without circularity')
        heading('Supplied finite diagnostic block; historical conclusions withdrawn')
        print()
        print()
        s_t_canonical = mp.mpf(1) / 8
        P_HK_SU3 = 1 - mp.exp(-(mp.mpf(4) / 3) * s_t_canonical)
        print(f'UNSCORED LEGACY DATA (historical labels):   s_t = 1/8           = {mp.nstr(s_t_canonical, 15)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   -(4/3)*s_t          = {mp.nstr(-(mp.mpf(4) / 3) * s_t_canonical, 15)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   P_HK_SU(3)(s_t=1/8) = {mp.nstr(P_HK_SU3, 30)}')
        for tname, tval in targets.items():
            err = abs(P_HK_SU3 - tval) / abs(tval)
            print(f'UNSCORED LEGACY DATA (historical labels):     vs {tname:<10} : err = {mp.nstr(err, 6)}')
        print()
        historical('5.1 Heat-kernel evaluation 1 - exp(-(4/3)*s_t) is transcendental in e, not pi', True, 'e and pi algebraically independent (Nesterenko); finite combos avoid pi')
        heading('Supplied finite diagnostic block; historical conclusions withdrawn')
        print()
        print()
        print()
        print()
        s_t = mp.mpf(1) / 8
        wilson_partial = mp.mpf('4/3') * s_t - mp.mpf('1/9') * s_t ** 2 - mp.mpf('13/81') * s_t ** 3 - mp.mpf('37/162') * s_t ** 4 - mp.mpf('3071/8748') * s_t ** 5 - mp.mpf('20873/34992') * s_t ** 6
        print(f'UNSCORED LEGACY DATA (historical labels):   Wilson partial (n<=6) = {mp.nstr(wilson_partial, 30)}')
        for tname, tval in targets.items():
            err = abs(wilson_partial - tval) / abs(tval)
            print(f'UNSCORED LEGACY DATA (historical labels):     vs {tname:<10} : err = {mp.nstr(err, 6)}')
        historical('5.2 Wilson partial sum at s_t=1/8 is a rational (no pi dependence)', True, 'All retained Wilson coefficients rational; finite-sum is rational')
        wilson_full_at_inf = mp.mpf(1)
        historical('5.3 Wilson series asymptote at s_t -> inf is 1 (free limit)', True, 'Free SU(3): <P> -> 1 = trivial holonomy; not 2*pi')
        heading('Supplied finite diagnostic block; historical conclusions withdrawn')
        print()
        print()
        print()
        for s_tv in [mp.mpf(1) / 8, mp.mpf(1) / 2]:
            disc_partial = mp.mpf('7/9') * s_tv ** 2 - mp.mpf('5/9') * s_tv ** 3 - mp.mpf('47/486') * s_tv ** 4 - mp.mpf('16891/43740') * s_tv ** 5 - mp.mpf('308999/524880') * s_tv ** 6
            print(f'UNSCORED LEGACY DATA (historical labels):   s_t = {mp.nstr(s_tv, 5)}: disc partial = {mp.nstr(disc_partial, 20)}')
            for tname, tval in targets.items():
                err = abs(disc_partial - tval) / abs(tval)
                if err < 0.5:
                    print(f'UNSCORED LEGACY DATA (historical labels):     vs {tname:<10} : err = {mp.nstr(err, 6)}  (CLOSE)')
        historical('5.4 C-iso discrepancy series at retained s_t is rational; no pi-target match', True, 'Rational coefficients; finite sum rational; no 2*pi or related target match')
        heading('Supplied finite diagnostic block; historical conclusions withdrawn')
        print()
        print()
        for k in [1, 2, 4, 8, 16, 18, 32, 36]:
            v = alpha_LM ** k
            print(f'UNSCORED LEGACY DATA (historical labels):   alpha_LM^{k:<3} = {mp.nstr(v, 10):<25} ', end='')
            best_match = None
            best_err = mp.inf
            for tname, tval in targets.items():
                err = abs(v - tval) / abs(tval)
                if err < best_err:
                    best_err = err
                    best_match = tname
            print(f'UNSCORED LEGACY DATA (historical labels): closest: {best_match} (rel.err {mp.nstr(best_err, 4)})')
        historical('5.5 alpha_LM^k for k in {1,2,...,36} does NOT produce pi-related target', True, 'alpha_LM = (1/(4*pi))/u_0 carries one factor of 1/pi per power; no 2*pi')
        inv_alpha_bare = mp.mpf(1) / alpha_bare
        inv_alpha_LM_u0 = mp.mpf(1) / (alpha_LM * u_0)
        four_pi = mp.mpf(4) * mp.pi
        print()
        print(f'UNSCORED LEGACY DATA (historical labels):   1/alpha_bare         = {mp.nstr(inv_alpha_bare, 30)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   1/(alpha_LM * u_0)   = {mp.nstr(inv_alpha_LM_u0, 30)}')
        print(f'UNSCORED LEGACY DATA (historical labels):   4*pi                 = {mp.nstr(four_pi, 30)}')
        print(f"UNSCORED LEGACY DATA (historical labels):   agree (1/alpha_bare = 4*pi) = {abs(inv_alpha_bare - four_pi) < mp.mpf('1e-30')}")
        print(f"UNSCORED LEGACY DATA (historical labels):   agree (1/(alpha_LM*u_0) = 4*pi) = {abs(inv_alpha_LM_u0 - four_pi) < mp.mpf('1e-30')}")
        tally(check('5.6 Two supplied reciprocal identities meet tolerance 1e-30', abs(inv_alpha_bare - four_pi) < mp.mpf('1e-30') and abs(inv_alpha_LM_u0 - four_pi) < mp.mpf('1e-30'), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    pdg_brannen = [-0.67857, -0.29683, 0.9754]
    if HAVE_MPMATH:
        cands = [('1 (literal P)', mp.mpf(1)), ('2*pi', mp.mpf(2) * mp.pi), ('4*pi', mp.mpf(4) * mp.pi), ('pi', mp.pi), ('u_0/alpha_LM = 4*pi*u_0^2 (supplied fixture)', u_0 / alpha_LM), ('4/3 (Casimir)', mp.mpf('4/3')), ('7/8 (APBC)', mp.mpf('7/8')), ('7/9 (NLO C-iso)', mp.mpf('7/9')), ('16 (taste exp)', mp.mpf(16)), ('18 (m_tau exp)', mp.mpf(18)), ('26 (beta_1)', mp.mpf(26)), ('alpha_LM', alpha_LM), ('alpha_LM^2', alpha_LM ** 2), ('<P>', mp.mpf(P_VEV_NUM))]
        best_match = None
        best_max_dev = mp.inf
        for name, alpha in cands:
            phi_eff = mp.mpf(2) / 9 * alpha
            cos_vals = [mp.cos(phi_eff + mp.mpf(2) * mp.pi * k / 3) for k in range(3)]
            sorted_pdg = sorted(pdg_brannen)
            sorted_cv = sorted([float(c) for c in cos_vals])
            max_dev = max((abs(c - p) for c, p in zip(sorted_cv, sorted_pdg)))
            print(f"UNSCORED LEGACY DATA (historical labels):   alpha = {name:<35}: cos = ({', '.join((mp.nstr(c, 5) for c in cos_vals))}), max-dev vs PDG = {mp.nstr(max_dev, 5)}")
            if max_dev < best_max_dev:
                best_max_dev = max_dev
                best_match = name
        historical('6.1 Best match found across expanded candidates', True, f"alpha = '{best_match}' (max-dev = {mp.nstr(best_max_dev, 5)})")
        historical("6.2 'alpha = 1' (literal P) matches PDG to ~1e-4 (RECOVERED FROM PROBE 30)", True, 'Reconfirms P primitive; no NEW dimensional candidate beats it')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('7.1 No closure of P from expanded retained inventory', True, 'Lindemann-Weierstrass still rules out rational -> transcendental')
    historical('7.2 alpha_bare-inheritance route is convention re-entry, not derivation', True, '4*pi in alpha_bare is the same period-2*pi-convention identified as P')
    historical('7.3 No NEW PDG-passing alpha candidate beats alpha = 1 (literal P)', True, "Recovers Probe 30's PDG-match exhaustion result on expanded basis")
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('8.1 Inventory expanded from 7 (Probe 30) to >=25 retained items', True, '11+ new rationals named with explicit retained provenance')
    historical('8.2 P status unchanged: bounded admission', True, 'Expanded inventory does not close the obstruction')
    historical("8.3 NEW DIAGNOSTIC: alpha_bare's pi is convention re-entry of P", True, 'alpha_bare = 1/(4*pi) inherits the period convention, not a derivation')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('9.1 No PDG values used in Sections 1-8 (derivation)', True, 'PDG only as Section 9 falsifiability comparator')
    historical('9.2 No new axioms', True, 'Uses only retained content as of 2026-05-10')
    historical('9.3 No new admissions', True, 'P remains the same admission Probe 30 named')
    historical('9.4 No fitted selectors', True, 'Pure dimensional/numerical analysis on retained constants')
    historical('9.5 Lindemann-Weierstrass / Nesterenko admitted as theorem-grade math', True, 'Standard mathematical theorems, not new framework axioms')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    print('=' * 72)
    print('=' * 72)
    if HAVE_MPMATH:
        tally(check('Supplied u is positive and denominators nonzero', u_0 > 0 and alpha_bare != 0 and (alpha_LM != 0)))
        tally(check('Corrected u/l = 4pi*u^2 identity', abs(u_0 / alpha_LM - 4 * mp.pi * u_0 ** 2) < mp.mpf('1e-30')))
        tally(check('Periodicity counterexample alpha=1+9pi', max((abs(mp.cos(mp.mpf(2) / 9 * (1 + 9 * mp.pi) + 2 * mp.pi * k / 3) - mp.cos(mp.mpf(2) / 9 + 2 * mp.pi * k / 3)) for k in range(3))) < mp.mpf('1e-30')))
        tally(check('Rational floor approximants obey finite error bound', all((0 <= 2 * mp.pi - mp.floor(10 ** n * 2 * mp.pi) / 10 ** n < mp.mpf(1) / 10 ** n for n in (1, 2, 3, 4, 5, 6)))))
    print(f'=== TOTAL: PASS={pass_count}, FAIL={fail_count} ===')
    return 0 if fail_count == 0 else 1
if __name__ == '__main__':
    raise SystemExit(main())
