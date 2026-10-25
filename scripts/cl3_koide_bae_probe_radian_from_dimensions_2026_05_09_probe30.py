#!/usr/bin/env python3
"""Supplied dimensional-kernel and finite fixture diagnostics; no physical exclusion."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/KOIDE_BAE_PROBE_RADIAN_FROM_DIMENSIONS_BOUNDED_NOTE_2026-05-09_probe30.md',)

def historical(label, condition, detail=''):
    print(f'HISTORICAL_UNSCORED (not a current assertion): {label!r}; old predicate={bool(condition)}; old detail={detail!r}')
import math

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
    a_s_dim = ('L',)
    historical('1.1 a_s (spatial lattice spacing) retained on A2 (Z^3 substrate)', a_s_dim == ('L',), 'MINIMAL_AXIOMS_2026-05-03.md, PHYSICAL_LATTICE_NECESSITY_NOTE.md')
    a_tau_dim = ('T',)
    historical('1.2 a_tau (temporal lattice spacing) retained via RP transfer matrix T = e^{-a_tau H}', a_tau_dim == ('T',), 'AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md')
    v_LR_dim = ('L', 'T^-1')
    historical('1.3 v_LR (Lieb-Robinson velocity) retained as 2erJ from A1+A2+A3+A4', v_LR_dim == ('L', 'T^-1'), 'AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md (M2)')
    M_Pl_dim = ('M',)
    historical('1.4 M_Pl (framework UV cutoff) retained as anchor', M_Pl_dim == ('M',), 'COMPLETE_PREDICTION_CHAIN_2026_04_15.md §8.1, PHYSICAL_LATTICE_NECESSITY_NOTE.md')
    P_avg = 0.5934
    historical('1.5 <P> = 0.5934 (plaquette VEV) retained as single computed input', abs(P_avg - 0.5934) < 1e-09, 'COMPLETE_PREDICTION_CHAIN_2026_04_15.md §2 (SU(3) lattice MC at beta=6)')
    g_bare = 1.0
    historical('1.6 g_bare = 1 (bare gauge coupling) retained by Cl(3) canonical normalization', g_bare == 1.0, 'G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07.md')
    hbar_dim = ('M', 'L^2', 'T^-1')
    historical('1.7 hbar (Planck constant) retained implicitly through QM structure on Cl(3) algebra', hbar_dim == ('M', 'L^2', 'T^-1'), 'Cl(3) per-site state space + standard QM')
    historical('1.8 Inventory closure: seven named dimensional/named constants exhaust the retained surface', True, 'Any dimensionless ratio on retained surface is a function of these seven')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    constants = {'a_s': (1, 0, 0), 'a_tau': (0, 1, 0), 'v_LR': (1, -1, 0), 'M_Pl': (0, 0, 1), 'P_avg': (0, 0, 0), 'g_bare': (0, 0, 0), 'hbar': (2, -1, 1)}
    xi_1_exp = (constants['v_LR'][0] + constants['a_tau'][0] - constants['a_s'][0], constants['v_LR'][1] + constants['a_tau'][1] - constants['a_s'][1], constants['v_LR'][2] + constants['a_tau'][2] - constants['a_s'][2])
    tally(check('2.1 Supplied x1 exponent vector vanishes', xi_1_exp == (0, 0, 0), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    xi_2_exp = (constants['M_Pl'][0] + constants['a_s'][0] + constants['v_LR'][0] - constants['hbar'][0], constants['M_Pl'][1] + constants['a_s'][1] + constants['v_LR'][1] - constants['hbar'][1], constants['M_Pl'][2] + constants['a_s'][2] + constants['v_LR'][2] - constants['hbar'][2])
    tally(check('2.2 Supplied x2 exponent vector vanishes', xi_2_exp == (0, 0, 0), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    inv_xi_1_exp = (constants['a_s'][0] - constants['v_LR'][0] - constants['a_tau'][0], constants['a_s'][1] - constants['v_LR'][1] - constants['a_tau'][1], constants['a_s'][2] - constants['v_LR'][2] - constants['a_tau'][2])
    tally(check('2.3 Inverse x1 exponent vector vanishes', inv_xi_1_exp == (0, 0, 0), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('2.4 Dimensionless-ratio space: 2-dim from (a_s, a_tau, v_LR, M_Pl, hbar) plus <P>, g_bare', 7 - 3 == 4, "Buckingham-Pi: 5 dim'l constants - 3 dimensions = 2 indep ratios")
    xi_1_natural = 1.0
    print()
    print(f'UNSCORED LEGACY DATA (historical labels):   Convention-fixed natural-unit values:')
    print(f'UNSCORED LEGACY DATA (historical labels):     xi_1 = v_LR * a_tau / a_s = c_natural = {xi_1_natural}')
    print(f'UNSCORED LEGACY DATA (historical labels):     xi_2 = M_Pl * a_s * v_LR / hbar = M_Pl * a_s / hbar (substrate parameter, not a fixed scalar)')
    print(f'UNSCORED LEGACY DATA (historical labels):     <P>  = {P_avg}')
    print(f'UNSCORED LEGACY DATA (historical labels):     g_bare = {g_bare}')
    historical('2.5 Convention xi_1 = 1 fixes c = 1 in natural units (no information beyond the convention)', xi_1_natural == 1.0, 'xi_1 = 1 is a convention, not a derivation')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    two_pi = 2 * math.pi
    print(f'UNSCORED LEGACY DATA (historical labels): \n  2*pi = {two_pi:.10f}')
    tally(check('3.1 Fixture x1=1 differs from 2pi by more than 1', abs(xi_1_natural - two_pi) > 1.0, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    tally(check('3.2 Fixture g=1 differs from 2pi by more than 1', abs(g_bare - two_pi) > 1.0, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    tally(check('3.3 Fixture P=.5934 differs from 2pi by more than 1', abs(P_avg - two_pi) > 1.0, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    print()
    found_match = False
    closest_q = None
    closest_diff = float('inf')
    for p in range(1, 101):
        for r in range(1, 101):
            q = p / r
            if abs(q * P_avg - two_pi) < 1e-06:
                found_match = True
                break
            if abs(q * P_avg - two_pi) < closest_diff:
                closest_diff = abs(q * P_avg - two_pi)
                closest_q = (p, r)
        if found_match:
            break
    tally(check('3.4 Finite p,r in 1..100 scan has no match at absolute tolerance 1e-6', not found_match, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('3.5 No small-rational multiple of xi_1 (= 1) equals 2*pi (pi transcendental)', True, 'Lindemann-Weierstrass: pi is transcendental, hence 2*pi ≠ p/r for any p, r ∈ Z')
    e_const = math.e
    tally(check('3.6 math.e agrees with decimal 2.71828 at tolerance .001', abs(e_const - 2.71828) < 0.001, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('3.7 e and pi are algebraically independent for cases of interest (Nesterenko on (e^pi, pi))', True, 'No nontrivial algebraic relation between e and pi is known; Nesterenko proved transcendence of e^pi')
    historical('3.8 No finite arithmetic combination of {e, rationals, <P>} produces 2*pi', True, 'Corollary of (3.5)-(3.7); no algebraic combination of (e, q ∈ Q) gives 2*pi')
    historical('3.9 2*pi is structurally outside the retained dimensional inventory', True, 'Step 2 closure: dimensional-analysis route to P is closed negatively')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    spin_half_period = 4 * math.pi
    so3_period = 2 * math.pi
    historical('4.1 Spin-1/2 SU(2) natural period = 4*pi', abs(spin_half_period - 4 * math.pi) < 1e-09, f'SU(2) period = {spin_half_period:.6f}, SO(3) period = {so3_period:.6f}')
    historical('4.2 4*pi is transcendental (twice 2*pi, derived from transcendental pi)', True, 'By Lindemann-Weierstrass on q*pi for nonzero algebraic q')
    phi_dimensionless = 2.0 / 9.0
    phi_in_4pi_units = phi_dimensionless * 4 * math.pi
    cos_at_4pi_unit = [math.cos(phi_in_4pi_units + 2 * math.pi * k / 3) for k in range(3)]
    print(f'UNSCORED LEGACY DATA (historical labels): \n  Test: cos((2/9)*4*pi + 2*pi*k/3) for k = 0, 1, 2')
    print(f'UNSCORED LEGACY DATA (historical labels):         cos values = {cos_at_4pi_unit}')
    pdg_cos = [0.9754, -0.67857, -0.29683]
    print(f'UNSCORED LEGACY DATA (historical labels):   PDG observed       = {pdg_cos}')
    rel_dev_at_4pi = [abs(c - p) / max(abs(p), 1e-09) for c, p in zip(cos_at_4pi_unit, pdg_cos)]
    print(f"UNSCORED LEGACY DATA (historical labels):   Relative deviation = {[f'{d:.4f}' for d in rel_dev_at_4pi]}")
    pdg_match_at_4pi = all((d < 0.001 for d in rel_dev_at_4pi))
    tally(check('4.3 Supplied 4pi cosine fixture fails rounded-vector relative tolerance .001', not pdg_match_at_4pi, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    phi_in_2pi_units = phi_dimensionless * 2 * math.pi
    cos_at_2pi_unit = [math.cos(phi_in_2pi_units + 2 * math.pi * k / 3) for k in range(3)]
    rel_dev_at_2pi = [abs(c - p) / max(abs(p), 1e-09) for c, p in zip(cos_at_2pi_unit, pdg_cos)]
    pdg_match_at_2pi = all((d < 0.001 for d in rel_dev_at_2pi))
    print(f'UNSCORED LEGACY DATA (historical labels): \n  Test: cos((2/9)*2*pi + 2*pi*k/3) for k = 0, 1, 2')
    print(f'UNSCORED LEGACY DATA (historical labels):         cos values = {cos_at_2pi_unit}')
    print(f"UNSCORED LEGACY DATA (historical labels):   Relative deviation = {[f'{d:.4f}' for d in rel_dev_at_2pi]}")
    tally(check('4.4 Supplied 2pi cosine fixture fails rounded-vector relative tolerance .001', not pdg_match_at_2pi, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    candidates = [('Literal-rational-as-radian (the primitive P)', 1.0), ('Cycle period 2*pi', 2 * math.pi), ('Spin-1/2 period 4*pi', 4 * math.pi), ('Bargmann triangle pi', math.pi), ('Z_3-step 2*pi/3', 2 * math.pi / 3), ('Plancherel-step 2*pi/9', 2 * math.pi / 9), ('xi_1 (= 1, c-slope)', xi_1_natural), ('g_bare (= 1)', g_bare), ('<P> (= 0.5934)', P_avg), ('e (from v_LR = 2erJ)', math.e)]
    print()
    print(f"UNSCORED LEGACY DATA (historical labels):   {'Candidate':<48} {'alpha':>10}  {'PDG match?':>12}")
    print('  ' + '-' * 76)
    pdg_match_results = []
    for label, alpha in candidates:
        cos_vals = [math.cos(phi_dimensionless * alpha + 2 * math.pi * k / 3) for k in range(3)]
        rel_devs = [abs(c - p) / max(abs(p), 1e-09) for c, p in zip(cos_vals, pdg_cos)]
        match = all((d < 0.001 for d in rel_devs))
        pdg_match_results.append((label, alpha, match, max(rel_devs)))
        match_str = 'YES' if match else f'NO ({max(rel_devs):.3f})'
        print(f'UNSCORED LEGACY DATA (historical labels):   {label:<48} {alpha:>10.4f}  {match_str:>12}')
    matches = [(label, alpha) for label, alpha, m, _ in pdg_match_results if m]
    print()
    print(f'UNSCORED LEGACY DATA (historical labels):   Total candidates that PDG-match: {len(matches)}')
    for label, alpha in matches:
        print(f'UNSCORED LEGACY DATA (historical labels):     -> {label} (alpha = {alpha})')
    all_matches_are_alpha_one = all((abs(alpha - 1.0) < 1e-09 for _, alpha in matches))
    tally(check('5.1 Among exactly ten fixtures, matching alpha values equal 1', all_matches_are_alpha_one and len(matches) >= 1, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    nontrivial_alphas = [(label, alpha, m, dev) for label, alpha, m, dev in pdg_match_results if abs(alpha - 1.0) > 1e-09]
    nontrivial_matches = [x for x in nontrivial_alphas if x[2]]
    nontrivial_fails = [x for x in nontrivial_alphas if not x[2]]
    tally(check('5.2 Among exactly ten fixtures, no tested alpha differing from 1 matches', len(nontrivial_matches) == 0, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('5.3 The unique passing candidate alpha = 1 IS the literal-rational-as-radian convention = primitive P', True, "Per KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT 'period-1-rad vs period-2pi-rad' formulation")
    cos_at_radian = [math.cos(phi_dimensionless + 2 * math.pi * k / 3) for k in range(3)]
    rel_dev_at_radian = [abs(c - p) / max(abs(p), 1e-09) for c, p in zip(cos_at_radian, pdg_cos)]
    pdg_match_at_radian = all((d < 0.001 for d in rel_dev_at_radian))
    print(f'UNSCORED LEGACY DATA (historical labels): \n  Verification: cos(2/9 + 2*pi*k/3) vs PDG')
    print(f"UNSCORED LEGACY DATA (historical labels):     Computed = {[f'{c:.5f}' for c in cos_at_radian]}")
    print(f'UNSCORED LEGACY DATA (historical labels):     PDG      = {pdg_cos}')
    print(f'UNSCORED LEGACY DATA (historical labels):     Max relative deviation = {max(rel_dev_at_radian):.6f}')
    tally(check('5.4 Supplied phi=2/9 cosine fixture passes rounded-vector relative tolerance .001', pdg_match_at_radian and max(rel_dev_at_radian) < 0.001, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    omega = complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))
    tally(check('6.1 Supplied cubic root of unity cubed agrees with 1', abs(omega ** 3 - 1.0) < 1e-12, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    L_box = 4
    k_BZ = [2 * math.pi * n / L_box for n in range(L_box)]
    tally(check('6.2 Four prescribed momenta lie in [0,2pi)', all((0 <= k < 2 * math.pi for k in k_BZ)), 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('6.3 2*pi as FREE SCALAR multiplying pure rational 2/9 is NOT retained', True, 'The 2*pi is locked in period structure, not available as a free multiplier')
    historical('6.4 Primitive P requires 2*pi as free scalar; this is structurally distinct from period 2*pi', True, 'P: literal-rational-as-radian convention where rationals q ∈ Q identify with q rad')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    d = 3
    historical('7.1 d = |C_3| = 3 (retained, three-generation observable theorem)', d == 3)
    historical('7.2 d^2 = 9 = real dim Herm_3 (retained, KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md R3)', d * d == 9)
    n_eff = 2
    historical('7.3 n_eff = 2 from C_3 conjugate-pair forcing (retained, KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20 §1.3)', n_eff == 2)
    phi_dimless = n_eff / (d * d)
    tally(check('7.4 Supplied quotient 2/3^2 agrees with 2/9', abs(phi_dimless - 2.0 / 9.0) < 1e-12, 'Scope: supplied fixtures only; original expression and threshold preserved.'))
    historical('7.5 Step 1 (Probe 24): dimensionless 2/9 retained; Step 2 (this probe): radian-from-dimensions FAILS', True, 'Together: P = literal-rational-as-radian remains the bounded admission')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('8.1 pi is transcendental (Lindemann 1882, Lindemann-Weierstrass theorem)', True, 'Theorem-grade external mathematical input')
    historical('8.2 e is transcendental (Hermite 1873)', True, 'Theorem-grade external mathematical input')
    historical('8.3 e^pi is transcendental (Gelfond-Schneider 1934)', True, 'Theorem-grade external mathematical input')
    historical('8.4 No finite arithmetic combination of {rationals, e, <P>} produces 2*pi', True, 'Algebraic numbers ∪ {e, e^q, <P>} field excludes 2*pi by transcendentality results above')
    historical('8.5 Retained dimensional ratios involve {e, rationals, <P>, substrate parameters} only', True, 'After convention-fixing, no algebraic combination produces literal 2*pi')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('9.1 Radian is dimensionless: theta_rad = arc_length / radius = L/L = 1', True, 'Continuum geometry definition')
    historical("9.2 'Period of e^{i theta} = 2*pi' is a unit-convention, not a physics ratio", True, 'Equivalently: the radian sets the literal scalar value of one full cycle')
    framework_retained_angles = {'Z_3 character period (full)': 2 * math.pi, 'Z_3 character per step': 2 * math.pi / 3, 'Spin-1/2 SU(2) period': 4 * math.pi, 'SO(3) period': 2 * math.pi, 'Bargmann triangle on equator CP^1': math.pi, 'BZ momentum range (per L)': 2 * math.pi}
    print()
    print(f"UNSCORED LEGACY DATA (historical labels):   Framework's retained natural angles:")
    for label, val in framework_retained_angles.items():
        print(f'UNSCORED LEGACY DATA (historical labels):     {label:<40} = {val:.6f}')
    historical('9.3 All framework retained natural angles contain 2*pi (or pi, 4*pi) in PERIOD STRUCTURE', True, 'None supplies 2*pi as a free scalar to multiply rationals')
    historical("9.4 Primitive P is the unit convention 'identify rational q with q rad'", True, 'Distinct from period-2*pi convention; the latter forces (rational q -> q*2*pi rad)')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('10.1 BAE-campaign admission count unchanged: (BAE) + (P, radian-bridge) = 2 admissions', True, 'Probe 30 does not introduce new admissions')
    five_routes = ['Z_3 qubit Pancharatnam-Berry (Probe 20)', 'Selected-line local Berry (selected-line no-go 2026-04-20)', 'Irreducibility audit (Probe campaign 2026-04-24)', 'Native-angle exhaustion (Probe 24)', 'Dimensional-inventory exhaustion (THIS Probe 30)']
    print()
    print(f'UNSCORED LEGACY DATA (historical labels):   Independent no-go routes against P:')
    for r in five_routes:
        print(f'UNSCORED LEGACY DATA (historical labels):     - {r}')
    historical('10.2 P is now closed negatively against 5 independent routes', len(five_routes) == 5, 'Probe 30 adds dimensional-inventory route to existing 4 no-go routes')
    historical('10.3 Closing P requires inputs (a), (b), or (c) from Probe 20 §4', True, '(a) lattice propagator radian quantum, (b) 4x4 hw=1+baryon Wilson holonomy, (c) Z_3-orbit Wilson-line d^2-power quantization')
    historical('10.4 Wilson-chain structure hints toward (a) or (c); none currently realized', True, 'Future closure path; no admission added by this probe')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('11.1 Section 1 (inventory) uses only retained constants', True, '(a_s, a_tau, v_LR, M_Pl, <P>, g_bare, hbar) all retained')
    historical('11.2 Section 2 (dim algebra) uses only dimensional analysis', True, 'Buckingham-Pi style group theory on the dimensions')
    historical('11.3 Section 3 (no 2*pi in inventory) uses transcendentality theorems', True, 'Lindemann-Weierstrass, Nesterenko, Gelfond-Schneider')
    historical('11.4 Sections 6-10 use only structural/conventional analysis', True, 'No PDG input; Section 4-5 PDG appears only as falsifiability comparator')
    historical('11.5 PDG firewall holds: PDG values used only in Section 4-5 as comparators, never as derivation input', True, 'Step 1 (positive closure) and Step 2 (negative closure) use only cited source-stack content')
    heading('Supplied finite diagnostic block; historical conclusions withdrawn')
    print()
    historical('12.1 VERDICT FLAG: KOIDE_BAE_PROBE_RADIAN_FROM_DIMENSIONS_CLOSES_P=FALSE', True)
    historical('12.2 RESIDUAL: P remains bounded; closure requires inputs (a), (b), or (c)', True)
    historical('12.3 NEW SHARPENING: dimensional-analysis route to P is closed negatively', True)
    historical('12.4 NO NEW AXIOMS, NO NEW ADMISSIONS, NO PDG-INPUT VIOLATIONS', True)
    print()
    print('=' * 72)
    print('=' * 72)
    D = ((1, 0, 1, 0, 2, 0, 0), (0, 1, -1, 0, -1, 0, 0), (0, 0, 0, 1, 1, 0, 0))
    basis = ((-1, 1, 1, 0, 0, 0, 0), (1, 0, 1, 1, -1, 0, 0), (0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 1))
    tally(check('Kernel basis exact zero products', all((sum((row[j] * v[j] for j in range(7))) == 0 for row in D for v in basis))))
    minor = tuple((tuple((row[j] for j in (0, 1, 3))) for row in D))
    tally(check('Rank-three identity minor', minor == ((1, 0, 0), (0, 1, 0), (0, 0, 1))))
    tally(check('Exact reconstruction of seven exponents in representative integer controls', all((tuple(((r + t) * basis[0][j] - t * basis[1][j] + u * basis[2][j] + w * basis[3][j] for j in range(7))) == (-r - 2 * t, r + t, r, -t, t, u, w) for r, t, u, w in ((0, 0, 0, 0), (2, -3, 4, -5), (-7, 2, -1, 6))))))
    tally(check('Free x2 can equal 2pi for positive supplied parameters', abs(2 * math.pi * 1 * 1 / 1 - 2 * math.pi) < 1e-12))
    tally(check('Principal logarithm of 1 is zero', math.log(1) == 0))
    baseline = [math.cos(2 / 9 + 2 * math.pi * k / 3) for k in range(3)]
    tally(check('Periodicity counterexample at alpha=1+9pi', max((abs(math.cos(2 / 9 * (1 + 9 * math.pi) + 2 * math.pi * k / 3) - baseline[k]) for k in range(3))) < 1e-12))
    tally(check('Nearby alpha counterexample to tolerance uniqueness', max((abs(math.cos(2 / 9 * (1 + 1e-08) + 2 * math.pi * k / 3) - baseline[k]) for k in range(3))) < 1e-06))
    print(f'=== TOTAL: PASS={pass_count}, FAIL={fail_count} ===')
    return 0 if fail_count == 0 else 1
if __name__ == '__main__':
    raise SystemExit(main())
