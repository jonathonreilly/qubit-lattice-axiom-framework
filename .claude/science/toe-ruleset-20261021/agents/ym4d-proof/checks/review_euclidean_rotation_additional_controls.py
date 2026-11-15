"""Additional post-inspection controls; original criteria and attempts preserved."""
from pathlib import Path
import hashlib
import json
import sympy as s

# Independently differentiate the closed Gaussian-square cumulant generator.
t = s.symbols('t')
cg = -t - s.log(1 - 2*t)/2
cumulants = [s.diff(cg, t, n).subs(t, 0) for n in range(1, 9)]
assert cumulants[0] == 0
assert all(cumulants[n-1] == 2**(n-1)*s.factorial(n-1) for n in range(2, 9))
x = s.symbols('x', real=True)
assert s.integrate(s.exp(-x*x/4)/s.sqrt(2*s.pi), (x, -s.oo, s.oo)) == s.sqrt(2)
assert s.integrate(s.exp(-s.Rational(1, 2))/s.sqrt(2*s.pi), (x, -s.oo, s.oo)) == s.oo

# Gaussian covariance exp(-(t-s)^2): positive stationary covariance need not be RP.
rp = s.Matrix([[s.exp(-4), s.exp(-9)], [s.exp(-9), s.exp(-16)]])
assert s.simplify(rp.det() - (s.exp(-20) - s.exp(-18))) == 0
assert rp.det() < 0

source = Path(__file__).with_name('euclidean_rotation_import_exact.py').read_text()
cases = [
    ('crossing_height', 'sorted(h) == [-1, 0, 0, 1]', 'sorted(h) == [-2, 0, 0, 2]', 'diagonal_geometry'),
    ('fixed_corners_opposite', '(zeros[0] - zeros[1]) % 4 == 2', '(zeros[0] - zeros[1]) % 4 == 1', 'diagonal_geometry'),
    ('clover_radius', 'min(heights) == -2 and max(heights) == 2', 'min(heights) == -1 and max(heights) == 1', 'support_footprints'),
    ('boundary_block_restriction', 'min(boundary_heights) == -(L-1) < 0', 'min(boundary_heights) == -(L-2) < 0', 'support_footprints'),
    ('torus_fixed_corner_count', 'len(set(p)&fixed) == 1', 'len(set(p)&fixed) == 2', 'torus_geometry'),
    ('torus_fourier_normalizer', 'for p,q in it.product(range(4),repeat=2)),Q())/16', 'for p,q in it.product(range(4),repeat=2)),Q())/8', 'gaussian_torus_control'),
    ('torus_minor_expected_value', '-Q(19,3675)', '-Q(19,3674)', 'gaussian_torus_control'),
    ('rotation_pole_expected_value', '-sp.Rational(277056,390625)', '-sp.Rational(277056,390624)', 'analytic_controls'),
    ('isotropic_power_control', 'sum(t*t for t in rot)**4-sum(t*t for t in p)**4', 'sum(t*t for t in rot)**3-sum(t*t for t in p)**4', 'analytic_controls'),
    ('high_frequency_power', 'sp.limit(r**8/(r*r+1)', 'sp.limit(r**2/(r*r+1)', 'analytic_controls'),
    ('gaussian_integral_normalization', 'sp.exp(-x*x/4)/sp.sqrt(2*sp.pi)', 'sp.exp(-x*x/4)/sp.sqrt(sp.pi)', 'analytic_controls'),
]
results = []
for label, old, new, fn in cases:
    assert source.count(old) == 1, (label, source.count(old))
    modified = source.replace(old, new)
    ns = {'__name__': 'review_mutant'}
    exec(compile(modified, 'review_mutant_' + label, 'exec'), ns)
    try:
        ns[fn]()
    except AssertionError:
        results.append({'mutation': label, 'rejected_by': 'AssertionError',
                        'mutant_sha256': hashlib.sha256(modified.encode()).hexdigest()})
    else:
        raise AssertionError('SURVIVED ' + label)
print(json.dumps({'gaussian_square_cumulants_1_to_8': list(map(str, cumulants)),
                  'gaussian_square_laplace_at_radius': 'infinite',
                  'stationary_gaussian_non_rp_determinant': str(s.expand(rp.det())),
                  'additional_mutations': results,
                  'scope': 'Listed controls only; no continuum or full-theorem certification.'}, indent=2))
