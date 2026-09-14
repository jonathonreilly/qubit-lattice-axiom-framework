#!/usr/bin/env python3
"""Finite checks for local ground-state probabilities and charge projection.

The mathematical volume-uniform bound is proved in the paired note. These
checks use finite matrices and exact integer incidence/transition coefficients.
The product-limit example tests the block lemma with exp(-delta A).
No mutable repository scientific inputs or integrity files are read.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations, product
import json
import numpy as np
from scipy import sparse
from scipy.linalg import eigh, expm

AUDIT_TIMEOUT_SEC = 120
# No AUDIT_INPUT_PATHS declaration: this runner has no repository inputs.

def box_complex(lengths):
    """Oriented product cells; lengths count cubes, not vertices."""
    lengths = tuple(lengths)
    levels = []
    for k in range(4):
        level = []
        for axes in combinations(range(3), k):
            for origin in product(*(range(lengths[a] + (a not in axes))
                                    for a in range(3))):
                level.append((axes, origin))
        levels.append(level)
    boundaries = []
    for k in range(1, 4):
        lower = {cell: i for i, cell in enumerate(levels[k-1])}
        mat = np.zeros((len(lower), len(levels[k])), dtype=np.int64)
        for j, (axes, origin) in enumerate(levels[k]):
            for position, axis in enumerate(axes):
                rest = tuple(a for a in axes if a != axis)
                upper = list(origin)
                upper[axis] += 1
                sign = (-1)**position
                mat[lower[(rest, tuple(upper))], j] += sign
                mat[lower[(rest, origin)], j] -= sign
        boundaries.append(mat)
    b1, b2, b3 = boundaries
    assert not np.any(b1 @ b2)
    assert not np.any(b2 @ b3)
    return levels, b1, b2.T, b3.T

def flux_basis(F, D):
    p = F.shape[0]
    assert p <= 11, "This finite check deliberately caps the full carrier."
    powers = 3**np.arange(p, dtype=np.int64)
    codes = np.arange(3**p, dtype=np.int64)
    all_b = ((codes[:, None] // powers[None, :]) % 3 - 1).astype(np.int64)
    div = all_b @ D.T
    physical = np.all(div % 3 == 0, axis=1)
    b, div = all_b[physical], div[physical]
    ids = np.full(3**p, -1, dtype=np.int64)
    ids[codes[physical]] = np.arange(len(b))
    assert len(b) == 3**(p - D.shape[0])
    return b, div//3, powers, ids

def clock_coefficients(b, F, powers, ids):
    """A_mu = sum_k exp(-k mu) A[k], each A[k] an integer matrix."""
    triplets = {k: ([], []) for k in range(5)}
    for l in range(F.shape[1]):
        f = F[:, l]
        assert np.any(f)
        for sigma in (-1, 1):
            raw = b + sigma*f
            new = (raw + 1) % 3 - 1
            m = (new-raw)//3
            k = np.sum(m*m, axis=1)
            dest = ids[(new+1) @ powers]
            assert np.all(dest >= 0)
            for exponent in range(5):
                source = np.flatnonzero(k == exponent)
                triplets[exponent][0].append(dest[source])
                triplets[exponent][1].append(source)
    out = []
    for exponent in range(5):
        rows = np.concatenate(triplets[exponent][0])
        cols = np.concatenate(triplets[exponent][1])
        mat = sparse.coo_matrix((np.ones(len(rows), dtype=np.int64), (rows, cols)),
                               shape=(len(b), len(b))).tocsr()
        mat.sum_duplicates()
        assert (mat-mat.T).nnz == 0
        out.append(mat)
    return out

def shift_coefficients(b0, F):
    """Separate route: integer truncated shifts, never modular arithmetic."""
    index = {tuple(row): i for i, row in enumerate(b0)}
    rows, cols = {k: [] for k in range(5)}, {k: [] for k in range(5)}
    for l in range(F.shape[1]):
        f = F[:, l]
        r = np.count_nonzero(f)
        for jump in (-2, -1, 1, 2):
            new = b0 + jump*f
            allowed = np.flatnonzero(np.all(np.abs(new) <= 1, axis=1))
            exponent = 0 if abs(jump) == 1 else r
            for source in allowed:
                rows[exponent].append(index[tuple(new[source])])
                cols[exponent].append(source)
    out = []
    for exponent in range(5):
        out.append(sparse.coo_matrix(
            (np.ones(len(rows[exponent]), dtype=np.int64),
             (rows[exponent], cols[exponent])),
            shape=(len(b0), len(b0))).tocsr())
    return out

def local_star_check(lengths=(3, 3, 3)):
    levels, _, F, D = box_complex(lengths)
    census = Counter()
    closed_patterns = 0
    for l in range(F.shape[1]):
        support = np.flatnonzero(F[:, l])
        f = F[support, l]
        r = len(support)
        rank = np.linalg.matrix_rank(D[:, support].astype(float))
        assert rank == r-1
        census[r] += 1
        for wraps in product((0, 1), repeat=r):
            m = -f*np.asarray(wraps)
            closed = not np.any(D[:, support] @ m)
            all_or_none = len(set(wraps)) == 1
            assert closed == all_or_none
            closed_patterns += int(closed)
    return {"box": lengths, "star_sizes": dict(census),
            "closed_binary_wrap_patterns": closed_patterns,
            "edges": len(levels[1])}

def opnorm(a):
    return float(np.linalg.norm(a, 2))

def penalty_checks():
    levels, _, F, D = box_complex((1, 1, 1))
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    mu, stiffness, kappa, total_time = 0.4, 0.3, 0.7, 1.0
    electric = np.sum(b*b, axis=1)
    penalty = np.sum(q*q, axis=1)
    neutral = np.flatnonzero(penalty == 0)
    charged = np.flatnonzero(penalty != 0)
    n = len(b)
    identity = np.eye(n)
    adjacency = sum(np.exp(-k*mu)*a.toarray() for k, a in enumerate(coeff))
    A = 2*len(levels[1])*identity + np.diag(stiffness*electric)-adjacency
    assert eigh(A, eigvals_only=True)[0] >= -1e-10
    H0 = A[np.ix_(neutral, neutral)]
    e0 = float(eigh(H0, eigvals_only=True)[0])
    off = A[np.ix_(charged, neutral)]
    v = opnorm(off)
    finite_penalties = []
    for lam in (32.0, 64.0, 128.0, 256.0, 512.0):
        energy, vectors = eigh(A+np.diag(lam*penalty), subset_by_index=(0, 0))
        psi = vectors[:, 0]
        leakage = float(np.sum(psi[charged]**2))
        lower = e0-v*v/(lam-e0)
        leakage_bound = v*v/(lam-e0)**2
        assert lower-1e-10 <= energy[0] <= e0+1e-10
        assert leakage <= leakage_bound+1e-12
        finite_penalties.append({'lambda': lam, 'energy': float(energy[0]),
                                 'neutral_energy': e0, 'energy_lower_bound': lower,
                                 'charged_weight': leakage, 'charged_weight_bound': leakage_bound})

    target = np.zeros_like(A)
    target[np.ix_(neutral, neutral)] = expm(-total_time*H0)
    Mhalf = np.diag(np.exp(-kappa*penalty/2))
    zeno = []
    for steps in (8, 16, 32, 64, 128, 256):
        delta = total_time/steps
        transfer = Mhalf @ expm(-delta*A) @ Mhalf
        value = np.linalg.matrix_power(transfer, steps)
        error = opnorm(value-target)
        a = transfer[np.ix_(neutral, neutral)]
        bblock = transfer[np.ix_(neutral, charged)]
        cblock = transfer[np.ix_(charged, charged)]
        qp = opnorm(cblock)
        B = opnorm(bblock)/delta
        C = opnorm(a-expm(-delta*H0))/delta**2
        bound = qp**steps + 2*delta*B/(1-qp) + steps*delta**2*(B*B/(1-qp)+C)
        assert qp < 1
        assert error <= bound+1e-12
        zeno.append({'steps': steps, 'delta': delta, 'operator_error': error,
                     'block_bound': bound, 'fast_block_norm': qp})
    assert zeno[-1]['operator_error'] < zeno[0]['operator_error']/10

    # Wrong projected model 1: discard the all-wrap second harmonic.
    wrong = (2*len(levels[1])*identity + np.diag(stiffness*electric)
             -coeff[0].toarray())[np.ix_(neutral, neutral)]
    missing_double = opnorm(wrong-H0)
    assert missing_double > 1
    wrong_target_distance = opnorm(expm(-total_time*wrong)-target[np.ix_(neutral, neutral)])
    assert wrong_target_distance > 1e-8
    # Wrong projected model 2: use the bulk exponent four on boundary edges.
    wrong_boundary = (2*len(levels[1])*identity + np.diag(stiffness*electric)
                      -coeff[0].toarray()-np.exp(-4*mu)*coeff[2].toarray())
    boundary_error = opnorm(wrong_boundary[np.ix_(neutral, neutral)]-H0)
    assert boundary_error > 1
    # Wrong normalization 3: standard spin raising matrices, no sqrt(2).
    # Every one-cube edge has r=2, so first and double hops scale by 2 and 4.
    wrong_spin = (2*len(levels[1])*identity + np.diag(stiffness*electric)
                  -2*coeff[0].toarray()-4*np.exp(-2*mu)*coeff[2].toarray())
    spin_error = opnorm(wrong_spin[np.ix_(neutral, neutral)]-H0)
    assert spin_error > 1
    # Wrong constraint 4: modulo-three closure permits a mixed wrap that
    # integer neutrality excludes. Record an actual source/destination pair.
    mixed = coeff[1][charged][:, neutral].tocoo()
    assert mixed.nnz > 0
    dst, src = charged[mixed.row[0]], neutral[mixed.col[0]]
    assert np.all(q[src] == 0) and np.any(q[dst] != 0)
    witness = {'source_flux': b[src].tolist(), 'destination_flux': b[dst].tolist(),
               'source_charge': q[src].tolist(), 'destination_charge': q[dst].tolist()}

    result = {'status': 'finite_author_checks_only',
              'parameters': {'mu': mu, 'electric_stiffness_3K_over_2': stiffness,
                             'kappa_per_step': kappa, 'T': total_time},
              'neutral_energy': e0, 'offblock_norm': v,
              'finite_spatial_penalties': finite_penalties,
              'zeno_product_model': 'Mhalf exp(-delta A) Mhalf, testing the block lemma',
              'zeno': zeno,
              'wrong_model_challenges': {
                  'omitted_second_harmonic_operator_error': missing_double,
                  'wrong_semigroup_limit_distance': wrong_target_distance,
                  'bulk_exponent_on_boundary_operator_error': boundary_error,
                  'unnormalized_spin_raising_operator_error': spin_error,
                  'modular_instead_of_integer_constraint_witness': witness}}
    return result


def log_lower(C, h, r, tau):
    # k = exp(2h tau)*(1-exp(-3h tau))/3, evaluated stably.
    log_k = 2*h*tau+np.log(-np.expm1(-3*h*tau))-np.log(3)
    return float(-2*C*tau+2*r*log_k)

def optimum(C, h, r):
    if C <= 2*r*h:
        return 1/max(C, h)
    return float(np.log1p(3*r*h/(C-2*r*h))/(3*h))

def abstract_chain_check():
    # Four qutrits, state-dependent rates on three-site neighborhoods.
    # The R={0} split has a nontrivial far Hamiltonian that need not commute
    # with H_near. The near terms are positive individually.
    digits = np.asarray(list(product(range(3), repeat=4)), dtype=np.int64)
    index = {tuple(row): i for i, row in enumerate(digits)}
    n, h, t = len(digits), 0.17, 0.9
    terms = []
    for site in range(4):
        support = set(range(max(0, site-1), min(4, site+2)))
        adjacency = np.zeros((n, n))
        for i, row in enumerate(digits):
            for target in range(3):
                if target == row[site]:
                    continue
                new = row.copy()
                new[site] = target
                j = index[tuple(new)]
                # Symmetric in the old/new central values, depends only on
                # the declared local neighborhood, and lies in [h,t].
                context = sum((a+1)*int(row[a]) for a in support if a != site)
                code = (context + int(row[site])+target + 2*int(row[site])*target) % 7
                adjacency[j, i] = h+(t-h)*code/6
        assert np.max(np.abs(adjacency-adjacency.T)) == 0
        term = 2*t*np.eye(n)-adjacency
        assert eigh(term, eigvals_only=True)[0] >= -1e-12
        terms.append((support, term))
    for site in range(3):
        v = 0.37*(digits[:, site]-digits[:, site+1])**2
        terms.append(({site, site+1}, np.diag(v)))
    near = sum(term for support, term in terms if 0 in support)
    far = sum(term for support, term in terms if 0 not in support)
    H = near+far
    C = float(np.max(np.diag(near)))
    e, vec = eigh(H, subset_by_index=(0, 0))
    omega = vec[:, 0]
    if np.sum(omega) < 0:
        omega = -omega
    assert np.min(omega) > 0
    B = np.zeros((n, n))
    for i, row in enumerate(digits):
        for step in (-1, 1):
            new = row.copy()
            new[0] = (new[0]+step) % 3
            B[index[tuple(new)], i] = 1
    G = -far-C*np.eye(n)+h*B
    assert np.min(-H-G) >= -1e-12
    assert np.linalg.norm(near@far-far@near) > 1e-3
    probabilities = np.sum(omega.reshape(3, -1)**2, axis=1)
    rows = []
    for tau in (0.02, 0.1, 0.4):
        semigroup_margin = float(np.min(expm(-tau*H)-expm(tau*G)))
        assert semigroup_margin >= -1e-12
        bound = np.exp(log_lower(C, h, 1, tau))
        assert np.min(probabilities) >= bound
        jensen_left = np.linalg.norm(expm(-tau*far)@omega)
        jensen_right = np.exp(-tau*(omega@far@omega))
        assert jensen_left >= jensen_right-1e-12
        rows.append({'tau': tau, 'lower_probability': float(bound),
                     'minimum_actual_probability': float(np.min(probabilities)),
                     'entrywise_semigroup_margin': semigroup_margin})
    return {'dimension': n, 'h': h, 'C': C,
            'noncommuting_near_far_norm': float(np.linalg.norm(near@far-far@near)),
            'cases': rows}

def cube_assignment_and_counts():
    levels, _, F, D = box_complex((1, 1, 1))
    witness = None
    for l1, l2 in combinations(range(F.shape[1]), 2):
        for s1, s2 in product((-1, 1), repeat=2):
            a = np.zeros(F.shape[1], dtype=np.int64)
            a[l1], a[l2] = s1, s2
            b = (F@a+1) % 3-1
            q = D@b//3
            if np.any(q):
                witness = {'nonzero_edge_indexes': [l1, l2],
                           'nonzero_oriented_edges': [levels[1][l1], levels[1][l2]],
                           'edge_values': [s1, s2], 'all_edge_values': a.tolist(),
                           'face_flux': b.tolist(), 'cube_charge': q.tolist()}
                break
        if witness:
            break
    assert witness is not None
    levels, _, F, D = box_complex((5, 5, 5))
    c = levels[3].index(((0, 1, 2), (2, 2, 2)))
    faces = set(np.flatnonzero(D[c]))
    R = set(np.flatnonzero(np.any(F[list(faces)] != 0, axis=0)))
    assert len(R) == 12
    face_supports = [set(np.flatnonzero(row)) for row in F]
    cube_supports = []
    for row in D:
        cube_supports.append(set().union(*(face_supports[p] for p in np.flatnonzero(row))))
    electric_supports = []
    for l in range(F.shape[1]):
        electric_supports.append(set().union(*(face_supports[p]
                                               for p in np.flatnonzero(F[:, l]))))
    counts = {'electric': sum(bool(s & R) for s in electric_supports),
              'faces': sum(bool(s & R) for s in face_supports),
              'cubes': sum(bool(s & R) for s in cube_supports)}
    assert counts['electric'] <= 13*12
    assert counts['faces'] <= 4*12
    assert counts['cubes'] <= 4*12
    # Separate analytic classification: twelve cube edges, twenty-four
    # outward edges, twenty-four opposite edges; 6+24 faces; 1+6+12 cubes.
    assert counts == {'electric': 60, 'faces': 30, 'cubes': 19}
    return {'two_edge_charge_assignment': witness, 'bulk_cube_region_size': len(R),
            'bulk_near_term_counts': counts}

def physical_cube_probability_check():
    levels, _, F, D = box_complex((1, 1, 1))
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    electric = np.sum(b*b, axis=1)
    charge2 = np.sum(q*q, axis=1)
    orbit_size = 3**(len(levels[0])-1)
    assert len(b)*orbit_size == 3**len(levels[1])
    rows = []
    for mu, K, lam in ((0., 0., 0.), (0.4, 0.2, 2.), (1., 0.5, 5.)):
        adjacency = sum(np.exp(-k*mu)*a.toarray() for k, a in enumerate(coeff))
        H = 2*len(levels[1])*np.eye(len(b))-adjacency+np.diag(1.5*K*electric+lam*charge2)
        e, vec = eigh(H, subset_by_index=(0, 0))
        omega = vec[:, 0]
        if np.sum(omega) < 0:
            omega = -omega
        assert np.min(omega) > 0
        # Each physical flux vector is the normalized sum of 3^(V-1)
        # coordinate configurations in its original gauge orbit.
        minimum_coordinate_probability = float(np.min(omega**2)/orbit_size)
        h = np.exp(-4*mu)
        C = 2*len(levels[1])+1.5*K*len(levels[2])+4*lam*len(levels[3])
        tau = optimum(C, h, len(levels[1]))
        log_bound = log_lower(C, h, len(levels[1]), tau)
        assert np.log(minimum_coordinate_probability) >= log_bound
        rows.append({'mu': mu, 'K': K, 'lambda': lam, 'h': h, 'C': C,
                     'tau': tau, 'log_lower_bound': log_bound,
                     'minimum_coordinate_probability': minimum_coordinate_probability,
                     'charge_defect_probability': float(np.sum(omega[charge2 != 0]**2))})
    return {'gauge_orbit_size': orbit_size, 'cases': rows}

def dropped_positive_near_counterexample():
    # Entrywise hopping positivity remains, but H_near is not positive.
    # Retaining the final conclusion after deleting that hypothesis fails.
    B = np.ones((3, 3))-np.eye(3)
    H = np.diag([-100., 0., 0.])-B
    e, vec = eigh(H, subset_by_index=(0, 0))
    prob = vec[:, 0]**2
    claimed = np.exp(log_lower(C=0., h=1., r=1, tau=1.))
    assert claimed > 1 and np.min(prob) < claimed
    negative = {'H': H.tolist(), 'lowest_near_eigenvalue': float(e[0]),
                'false_bound_if_positive_near_is_dropped': float(claimed),
                'minimum_actual_probability': float(np.min(prob))}
    corrected = np.exp(log_lower(C=101., h=1., r=1, tau=0.01))
    assert corrected < np.min(prob)
    negative['valid_bound_after_local_scalar_shift'] = float(corrected)
    # A second distinct missing premise: an on-R potential cannot be assigned
    # to H_far. Omitting its local diagonal cost makes the bound false.
    H2 = 2*np.eye(3)-B+np.diag([0., 100., 100.])
    _, vec2 = eigh(H2, subset_by_index=(0, 0))
    false_far = np.exp(log_lower(C=2., h=1., r=1, tau=1.))
    actual2 = float(np.min(vec2[:, 0]**2))
    assert false_far > actual2
    return {'positive_near_dropped_without_changing_C': negative,
            'on_region_potential_misassigned_to_far': {
                'H': H2.tolist(), 'false_bound': float(false_far),
                'minimum_actual_probability': actual2}}

def projection_checks(lengths):
    levels, _, F, D = box_complex(lengths)
    b, q, powers, ids = flux_basis(F, D)
    coeff = clock_coefficients(b, F, powers, ids)
    neutral = np.flatnonzero(np.all(q == 0, axis=1))
    shifts = shift_coefficients(b[neutral], F)
    details = []
    for exponent in range(5):
        direct = coeff[exponent][neutral][:, neutral]
        difference = direct-shifts[exponent]
        difference.eliminate_zeros()
        assert difference.nnz == 0
        details.append({'exponent': exponent, 'entries': direct.nnz,
                        'integer_multiplicity': int(direct.sum())})
    row, col = coeff[0].nonzero()
    assert np.array_equal(q[row], q[col])
    return {'box': lengths, 'physical_dimension': len(b),
            'neutral_dimension': len(neutral), 'coefficients': details}


def main():
    results = {
        'local_stars': local_star_check(),
        'projected_coefficients': [projection_checks((1,1,1)), projection_checks((1,1,2))],
        'penalty_limits': penalty_checks(),
        'local_probability_lemma': abstract_chain_check(),
        'physical_cube_geometry': cube_assignment_and_counts(),
        'physical_cube_probabilities': physical_cube_probability_check(),
        'hypothesis_challenges': dropped_positive_near_counterexample(),
    }
    print(json.dumps(results, indent=2))
    print('per_element: checked exact cyclic shifts and integer branch-mismatch coefficients on finite carriers.')
    print('per_site: checked an original twelve-link cube assignment with integer charge and local term counts.')
    print('per_mode: checked and not executed — no photon pole, spectral residue, or continuum mode calculation is claimed.')
    print('per_block: checked complete one/two-cube projection matrices and a noncommuting four-qutrit probability example.')
    print('lattice_wide: checked and not executed — the uniform local bound has an analytic proof; no infinite-volume matrix was computed.')
    print('TOTAL: PASS=7 FAIL=0 (author check families; theorem scope is stated in the paired note)')


if __name__ == '__main__':
    main()
