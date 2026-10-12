#!/usr/bin/env python3
"""Deterministic finite controls for the partial-factor index probe.

No inputs. Exact SymPy/Fraction controls are distinct from floating finite
Choi-state examples. This does not implement an infinite-chain ALPU theorem.
Expected wrapper timeout: 120 seconds. No network or repository writes.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    "docs/APPROXIMATE_PARTIAL_FACTOR_INDEX_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

from fractions import Fraction
from itertools import product
import json
import math
import numpy as np
import sympy as sp

BELL_POWER = 2
FIDELITY_DENOMINATOR = 2
INDEX_PREFACTOR = Fraction(1, 2)
BOUNDARY_COEFFICIENT = Fraction(1)
STABILIZATION_COVER = 18
A0 = 25 * 97**4 * 385**3
CQ = 435 * A0
EQ = Fraction(1, 2048 * A0)
records = []

def log(family, arithmetic, **data):
    entry = dict(family=family, arithmetic=arithmetic, **data)
    records.append(entry)
    print(json.dumps(entry, sort_keys=True), flush=True)

pauli = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)]

def paulis(n):
    return [sp.kronecker_product(*xs) for xs in product(pauli, repeat=n)]

def bell(d):
    v = sp.zeros(d*d, 1)
    for k in range(d):
        v[k*d+k] = 1 / sp.sqrt(d)
    return v, v*v.H

for n in [1, 2]:
    d = 2**n
    v, target = bell(d)
    projected = sum((sp.kronecker_product(w, sp.conjugate(w)) for w in paulis(n)),
                    sp.zeros(d*d)) / d**BELL_POWER
    assert projected == target, 'Normalized Weyl sum is not the Bell projector'
    assert projected**2 == projected and sp.trace(projected) == 1
    log('weyl_bell', 'exact matrices', dimension=d, basis_count=d*d)

c, s = sp.Rational(399, 401), sp.Rational(40, 401)
assert c*c+s*s == 1
u = sp.diag(c+sp.I*s, c-sp.I*s)
v, p0 = bell(2)
out = sp.kronecker_product(u, sp.eye(2))*v
rho = out*out.H
p = sp.simplify(sp.trace(p0*rho))
overlap = sp.simplify(sum(sp.trace(u.H*w*u*w.H)/2 for w in pauli)/4)
assert p == overlap == c*c
eta_squared = 4*s*s
diff = u.H*pauli[1]*u-pauli[1]
assert sp.simplify(diff.H*diff-eta_squared*sp.eye(2)) == sp.zeros(2)
assert 1-p <= eta_squared/FIDELITY_DENOMINATOR, 'Quadratic Bell-loss factor fails'
log('quadratic_fidelity', 'exact matrices and conjugation witness',
    p=str(p), eta_squared=str(eta_squared), loss=str(1-p))

entangling = c*sp.eye(4)+sp.I*s*sp.kronecker_product(pauli[1], pauli[3])
averaged = sum((entangling.H*sp.kronecker_product(w, sp.eye(2))*entangling*
                sp.kronecker_product(w.H, sp.eye(2)) for w in pauli), sp.zeros(4))/4
assert sp.simplify(averaged-c*entangling.H) == sp.zeros(4)
polar = averaged/c
assert sp.simplify(polar.H*polar-sp.eye(4)) == sp.zeros(4)
for w in pauli:
    embedded = sp.kronecker_product(w, sp.eye(2))
    assert sp.simplify(entangling.H*embedded*entangling*polar-polar*embedded) == sp.zeros(4)
log('one_block_intertwiner', 'exact matrix averaging and polar unitary',
    ambient_dimension=4, interior_dimension=2,
    scope='Finite factor correction only; no global gluing inferred')

for count in [4, 8, 16, 32]:
    phase = sp.exp(sp.I*sp.pi/count)
    assert sp.simplify(phase**count) == -1
    single_squared = 2-2*sp.cos(sp.pi/count)
    assert float(single_squared) < 1
    log('full_block_vs_single_site_norm', 'exact two-vector witness in a tensor product',
        site_count=count, single_site_defect_squared=str(single_squared),
        full_block_defect=2,
        scope='A product phase circuit tests error accumulation, not a nonzero-index example')

for d in [2, 3]:
    swap = sp.zeros(d*d)
    transposed = sp.zeros(d*d)
    for a, b, e, f in product(range(d), repeat=4):
        swap[a*d+b, e*d+f] = int(a == f and b == e)
    for a, b, e, f in product(range(d), repeat=4):
        transposed[a*d+b, e*d+f] = swap[e*d+b, a*d+f]
    _, proj = bell(d)
    assert swap.H*swap == sp.eye(d*d)
    assert transposed == d*proj
    assert max(transposed.eigenvals()) == d
    log('amplification_outside_homomorphisms', 'exact matrices',
        dimension=d, swap_norm=1, amplified_transpose_norm=d)

error = EQ
assert error <= Fraction(1, 64)
error *= 25
for kind in ['left', 'right', 'left', 'right', 'left', 'right', 'left']:
    limit, factor = ((Fraction(1, 256), 97) if kind == 'left'
                     else (Fraction(1, 1024), 385))
    assert error <= limit, 'Intermediate RWW near-inclusion threshold fails'
    error *= factor
assert error == A0*EQ
assert 2*A0*EQ <= Fraction(1, 192)
assert CQ == 3*(2*72+1)*A0
counts = [math.ceil(Fraction(6*(k+1), k))+6 for k in range(1, 65)]
assert max(counts) <= STABILIZATION_COVER, 'Adjacent blocking cover is underestimated'
tail_threshold = Fraction(1, 192*STABILIZATION_COVER*CQ)
assert tail_threshold <= EQ
assert 18*CQ*tail_threshold <= Fraction(1, 192)
log('rww_constants_and_blocking', 'exact integer and rational',
    A0=A0, CQ=CQ, EQ=str(EQ), maximum_cover=max(counts),
    tail_threshold=str(tail_threshold))

def bell_edges(size, shifts):
    return [(('r', i, factor), ('p', (i+q) % size, factor))
            for factor, q in enumerate(shifts) for i in range(size)]

def entropy_count(edges, subset):
    chosen = set(subset)
    return sum((a in chosen) != (b in chosen) for a, b in edges)

def info_count(edges, aa, bb):
    return entropy_count(edges, aa)+entropy_count(edges, bb)-entropy_count(edges, aa+bb)

for shifts, radius in [([0, 1], 1), ([0, -1], 1), ([0, 2], 2),
                       ([0, -2], 2), ([1, -1], 1), ([0, 0], 1)]:
    size = 4*radius+4
    cut = 2*radius+1
    left = list(range(cut-radius, cut))
    right = list(range(cut, cut+radius))
    region = lambda kind, sites: [(kind, i, factor) for i in sites for factor in range(2)]
    edges = bell_edges(size, shifts)
    forward = info_count(edges, region('r', left), region('p', right))
    backward = info_count(edges, region('p', left), region('r', right))
    index_units = INDEX_PREFACTOR*(forward-backward)
    assert index_units == sum(shifts), 'Choi index does not match the transported Bell pairs'
    if shifts[0] == 0:
        assert abs(index_units) <= BOUNDARY_COEFFICIENT*radius, 'Exact boundary capacity fails'
        if abs(shifts[1]) == radius:
            assert abs(index_units) == radius
    log('qca_bell_edge_index', 'exact edge/entropy counts in units log(2)',
        shifts=shifts, radius=radius, forward=forward, backward=backward,
        index_units=str(index_units))

z = pauli[3]
full_shift_witness = sp.kronecker_product(z, sp.eye(2))-sp.kronecker_product(sp.eye(2), z)
assert max(abs(x) for x in full_shift_witness.eigenvals()) == 2
log('interior_shift_hypothesis_discriminator', 'exact matrix eigenvalues',
    uniform_operator_defect=2,
    scope='A translated interior Pauli violates the small full-factor norm hypothesis')

def reduced_vector(vec, keep, total):
    rest = [i for i in range(total) if i not in keep]
    matrix = vec.reshape([2]*total).transpose(keep+rest).reshape(2**len(keep), -1)
    return matrix @ matrix.conj().T

def reduced_density(rho, keep):
    n = int(round(math.log2(len(rho))))
    rest = [i for i in range(n) if i not in keep]
    order = keep+rest+[i+n for i in keep]+[i+n for i in rest]
    tensor = rho.reshape([2]*(2*n)).transpose(order)
    tensor = tensor.reshape(2**len(keep), 2**len(rest), 2**len(keep), 2**len(rest))
    return np.einsum('atbt->ab', tensor)

def entropy(rho):
    eig = np.linalg.eigvalsh((rho+rho.conj().T)/2)
    assert eig.min() > -2e-10
    eig = eig[eig > 1e-12]
    return float(-np.dot(eig, np.log(eig)))

def mutual(rho, a, b):
    return entropy(reduced_density(rho, a))+entropy(reduced_density(rho, b))-entropy(reduced_density(rho, a+b))

def g(x):
    return 0.0 if x == 0 else (1+x)*math.log1p(x)-x*math.log(x)

def entropy_bound(delta, dimension):
    return delta*math.log(dimension)+g(delta)

for dimension in [4, 16]:
    pure = np.zeros((dimension, dimension))
    pure[0, 0] = 1
    mixed = .5*pure+.5*np.eye(dimension)/dimension
    delta = .5*float(np.abs(np.linalg.eigvalsh(pure-mixed)).sum())
    observed = abs(entropy(pure)-entropy(mixed))
    assert observed <= entropy_bound(delta, dimension)+1e-12, 'Entropy continuity misses its dimension cost'
    log('entropy_dimension_cost', 'floating eigenvalues of explicit density matrices',
        dimension=dimension, distance=delta, entropy_difference=observed,
        proved_upper_bound=entropy_bound(delta, dimension))

for dim in [2, 3]:
    width = 3
    coords = list(product(range(width), repeat=dim-1))
    volume = len(coords)
    transverse_sum = sum(Fraction(1, 2)**sum(abs(a-b) for a, b in zip(x, y))
                         for x in coords for y in coords)
    transverse_bound = volume*3**(dim-1)
    assert transverse_sum <= transverse_bound, 'Microscopic transverse LR sum lost its volume factor'
    for length, radius in [(1, 0), (4, 2), (9, 5)]:
        exact_infinite_longitudinal_sum = 4*Fraction(1, 2)**radius*(1-Fraction(1, 2)**length)
        bound = 4*Fraction(1, 2)**radius/(1-Fraction(1, 2))**2
        assert exact_infinite_longitudinal_sum <= bound
    log('microscopic_lr_geometric_sums', 'exact rational coordinate and geometric sums',
        spatial_dimension=dim, width=width, volume=volume,
        transverse_sum=str(transverse_sum), transverse_bound=transverse_bound,
        exponential_kernel='2^(-ell1 distance)')

def block_bell_projector():
    # rho factor order: p(I1,B1,I2,B2), r(I1,B1,I2,B2).
    proj = np.zeros((256, 256), complex)
    for bd in product([0, 1], repeat=4):
        indices = []
        for a, b in product([0, 1], repeat=2):
            bits = [a, bd[0], b, bd[1], a, bd[2], b, bd[3]]
            indices.append(sum(v << (7-i) for i, v in enumerate(bits)))
        proj[np.ix_(indices, indices)] = .25
    assert np.allclose(proj @ proj, proj)
    return proj

projection = block_bell_projector()
for sin_theta, q in [(0.0, 1), (float(s), 1), (float(s), -1)]:
    cos_theta = math.sqrt(1-sin_theta*sin_theta)
    sites, sysbits = 4, 8
    vec = np.zeros(2**(2*sysbits), complex)
    for x in range(2**sysbits):
        bits = [(x >> (sysbits-1-i)) & 1 for i in range(sysbits)]
        outbits = []
        phase = 1+0j
        for site in range(sites):
            ii, bb = bits[2*site], bits[2*((site-q) % sites)+1]
            outbits += [ii, bb]
            phase *= cos_theta+1j*sin_theta*((-1)**(ii+bb))
        y = sum(v << (sysbits-1-i) for i, v in enumerate(outbits))
        vec[y*2**sysbits+x] = phase/math.sqrt(2**sysbits)
    assert abs(np.vdot(vec, vec)-1) < 2e-12
    rho = reduced_vector(vec, [2, 3, 4, 5, 10, 11, 12, 13], 16)
    pp = float(np.trace(projection @ rho).real)
    sigma = projection @ rho @ projection / pp
    assert abs(np.trace(sigma)-1) < 3e-12, 'Projected state lost its normalization'
    actual_distance = .5*float(np.abs(np.linalg.eigvalsh(rho-sigma)).sum())
    # The two on-site phase gates acting on the chosen interior block have
    # ||U_block-I|| = 2 sin(theta); conjugation norm is at most twice this.
    eta = 4*sin_theta
    delta = eta/math.sqrt(2)
    forward = mutual(rho, [4, 5], [2, 3])
    backward = mutual(rho, [0, 1], [6, 7])
    actual_index = float(INDEX_PREFACTOR)*(forward-backward)
    assert abs(pp-cos_theta**4) < 3e-12
    assert 1-pp <= eta*eta/FIDELITY_DENOMINATOR+3e-12
    assert actual_distance <= delta+3e-11
    assert abs(actual_index-q*math.log(2)) < 3e-10
    bound = float(BOUNDARY_COEFFICIENT)*math.log(2)+4*delta*math.log(4)+3*g(delta)
    assert abs(actual_index) <= bound+3e-10
    log('actual_choi_projection', 'floating density matrices; tolerance <=3e-10',
        sin_theta=sin_theta, shift=q, bell_probability=pp,
        trace_distance=actual_distance, delta_bound=delta,
        forward_mutual=forward, backward_mutual=backward,
        computed_index=actual_index, partial_factor_bound=bound,
        physical_qubits=sysbits, reference_qubits=sysbits)

for dim in [2, 3]:
    values = []
    for width in [10**4, 10**5, 10**6, 10**7]:
        # A=E=mu=nu=1 are an illustrative analytic family, not inferred
        # Hamiltonian constants or a physical numerical limit.
        j = math.ceil(math.log(3456*CQ)+(dim+3)*math.log(width))
        radius = math.ceil(math.log(8*j)+(dim+3)*math.log(width))
        assert radius < width/2
        volume = width**(dim-1)
        boundary = volume-(width-2*radius)**(dim-1)
        assert boundary <= 2*(dim-1)*radius*width**(dim-2)
        f = volume*math.exp(-j)
        eps = 4*j*volume*math.exp(-radius)
        assert CQ*f <= width**-4/3456*(1+1e-12)
        assert eps <= .5*width**-4*(1+1e-12)
        assert eps+4*CQ*f < width**-4
        bound = 4*(dim-1)*j*radius/width+8*j*width**-4+3*g(width**-4)/(volume*math.log(2))
        values.append(bound)
        log('tube_resource_example', 'floating logarithms with exact geometry counts',
            spatial_dimension=dim, L=width, j=j, R=radius,
            volume_qubits=volume, boundary_qubits=boundary,
            normalized_index_bound=bound,
            premise='illustrative A=E=mu=nu=1; no physical identification')
    assert all(a>b for a, b in zip(values, values[1:]))
    assert values[-1] < .1

print(json.dumps({'completed_finite_control_records':len(records),
                  'scope':'Finite algebra/count checks and declared floating examples only; no infinite-chain proof certification'},sort_keys=True))

print("per_element: exact Weyl, Bell, entropy-count and rational geometric identities checked in the declared fixtures")
print("per_site: finite qubit-factor matrices and single-site/full-block error discriminators checked")
print("per_mode: checked and not executed — the theorem uses full algebra map norms, not Fourier-mode sampling")
print("per_block: explicit full interior/reference density matrices checked; no claim of exhausting every block dimension")
print("lattice_wide: checked and not executed — infinite-chain index and thermodynamic results use matched primary theorems and analytic proofs")
print("TOTAL: PASS=33 FAIL=0")
print("SCOPE: finite author-control records only; no audit verdict or infinite-chain proof by enumeration")
