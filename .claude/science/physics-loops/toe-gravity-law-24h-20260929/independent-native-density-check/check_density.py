"""Independent exact local and geometric controls; no author code imported."""
from collections import defaultdict
from fractions import Fraction
from itertools import product, combinations
from pathlib import Path
import json
import resource
import time

t0 = time.perf_counter()
import sympy as s

# A literal 16-dimensional four-physical-qubit check, not bosonic pairs.
def lowering_pair(i, j):
    M = s.zeros(16)
    mask = (1 << i) | (1 << j)
    for word in range(16):
        if word & mask == mask:
            M[word ^ mask, word] = 1
    return M

d1, d2 = lowering_pair(0, 1), lowering_pair(2, 3)
q = d1-d2                            # sqrt(2) Q_E1
M = s.I*(q.T-q)                      # sqrt(2) K_x
z = s.symbols('z')
charpoly = s.factor(M.charpoly(z).as_expr())
assert s.expand(charpoly-z**6*(z*z-1)**4*(z*z-4)) == 0
assert M == M.conjugate().T
number = s.diag(*[i.bit_count() for i in range(16)])
ad = number
local_derivatives = []
for r in range(1, 4):
    ad = M*ad-ad*M
    # The odd cases vanish; the second has the exact sqrt(2)^2 denominator.
    numerator = s.simplify(s.I**r*ad[0, 0])
    if r % 2 == 0:
        numerator /= 2**(r//2)
    assert numerator == ([0, 4, 0][r-1])
    local_derivatives.append(int(numerator))

def add(x, y, L):
    return tuple((a+b) % L for a, b in zip(x, y))

def neg(x):
    return tuple(-a for a in x)

unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
zero = (0, 0, 0)
D = set()
for e in unit:
    D.add(tuple(2*a for a in e)); D.add(tuple(-2*a for a in e))
for i, j in combinations(range(3), 2):
    for a, b in product([-1, 1], repeat=2):
        D.add(tuple(a*unit[i][k]+b*unit[j][k] for k in range(3)))
assert len(D) == 18

def pair(x, y):
    assert x != y
    return tuple(sorted([x, y]))

def channel_words(x, L):
    d = [pair(add(x, e, L), add(x, neg(e), L)) for e in unit]
    out = [({d[0]: 1, d[1]: -1}, 2),
           ({d[0]: 1, d[1]: 1, d[2]: -2}, 6)]
    for i, j in combinations(range(3), 2):
        terms = {}
        for a, b in product([-1, 1], repeat=2):
            u = tuple(a*k for k in unit[i]); v = tuple(b*k for k in unit[j])
            terms[pair(add(x, u, L), add(x, v, L))] = a*b
        assert len(terms) == 4
        out.append((terms, 4))
    return out

torus_checks = []
for L in [5, 6, 7]:
    sites = list(product(range(L), repeat=3)); V = L**3
    channels = {x: channel_words(x, L) for x in sites}
    state = defaultdict(int)  # sqrt(2) sum_x Q_E1(x)^dagger Omega
    axial_centers = {}
    for x in sites:
        for i, e in enumerate(unit):
            key = pair(add(x, e, L), add(x, neg(e), L))
            assert key not in axial_centers
            axial_centers[key] = (x, i)
        for key, coeff in channels[x][0][0].items():
            state[key] += coeff
    assert len(state) == 2*V
    scaled_norm2 = sum(c*c for c in state.values())
    assert scaled_norm2 == 2*V
    result = defaultdict(Fraction)
    for key, c in state.items():
        result[key] = Fraction(2*c)  # mu=1, N=2
    contractions = {}
    for x in sites:
        scalars = []
        for A, (terms, norm2) in enumerate(channels[x]):
            val = sum(coeff*state.get(key, 0) for key, coeff in terms.items())
            scalars.append(val)
            for key, coeff in terms.items():
                result[key] -= Fraction((2 if A < 2 else 1)*coeff*val, norm2)
        assert scalars == [2, 0, 0, 0, 0]
        contractions[x] = scalars
    assert all(v == 0 for v in result.values())
    # Every actual gradient annihilator vanishes, before its adjoint is applied.
    for x in sites:
        for e in unit:
            assert contractions[add(x, e, L)] == contractions[x]

    # K incidences and the complete h_x support, checked without a Hilbert space.
    Ksupport = {x: {add(x, e, L) for e in unit[:2]} |
                    {add(x, neg(e), L) for e in unit[:2]} for x in sites}
    incidence = defaultdict(int)
    for supp in Ksupport.values():
        assert len(supp) == 4
        for y in supp:
            incidence[y] += 1
    assert set(incidence.values()) == {4}
    hsupport = {zero} | {add(zero, d, L) for d in D}
    for words, _ in channels[zero]:
        for key in words:
            hsupport.update(key)
    assert len(hsupport) == 25
    for e in unit:
        for words, _ in channels[e]:
            for key in words:
                assert set(key) <= hsupport
    first_step_terms = sum(bool(hsupport & supp) for supp in Ksupport.values())
    assert first_step_terms <= 4*25
    assert len(list(combinations(D, 2))) == 153
    torus_checks.append({'L': L, 'V': V, 'scaled_pair_norm_squared': scaled_norm2,
                         'H_pair_residual_zero': True, 'all_gradient_annihilators_zero': True,
                         'h_support_size': len(hsupport), 'K_incidence': 4,
                         'K_terms_touching_h_support': first_step_terms})

CH_multiplier = 24**4*25*28*31*34
CN = 24**4*1*4*7*10
A_multiplier, B_constant = Fraction(CH_multiplier, 24), Fraction(CN, 24)
assert A_multiplier.denominator == B_constant.denominator == 1
nu, A, B, y = s.symbols('nu A B y', positive=True)
poly = (A+nu*B)*y*y-2*nu*y
assert s.simplify(poly.subs(y, nu/(A+nu*B))+nu**2/(A+nu*B)) == 0
assert s.simplify(poly+nu**2/(A+nu*B) - (A+nu*B)*(y-nu/(A+nu*B))**2) == 0

result = {'local_K_scaled_characteristic_polynomial': str(charpoly),
          'local_K_norm': 'sqrt(2)', 'local_number_derivatives_1_2_3': local_derivatives,
          'tori': torus_checks, 'C_H_multiplier_of_182mu_plus_240tau': CH_multiplier,
          'C_N': CN, 'A_multiplier_of_182mu_plus_240tau': int(A_multiplier),
          'B': int(B_constant), 'variational_square_identity': True,
          'coercivity_assumed_or_checked': False, 'author_code_imported': False,
          'elapsed_seconds': time.perf_counter()-t0,
          'maxrss_bytes': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
out = Path(__file__).parent
(out/'results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
