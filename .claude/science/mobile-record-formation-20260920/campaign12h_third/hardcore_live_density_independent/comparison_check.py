"""Selective post-seal controls; no author module is imported or executed."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from itertools import product
import importlib.util
import json
import sys
import numpy as np
import sympy as s
import scipy.linalg as la

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PRE_SHA = 'caf8a8632b62fa99bcd9fad95f33aa27be44ed0ecd1b511e09827a825b04a703'
SEALS = {
    'HARDCORE_RECORD_RING_AUTHOR_SEAL.json': 'f48d6ee6d9e013bcc12019164ede7f8593feb93e62cd6076e753573b2126ef26',
    'RECORD_DENSITY_AUTHOR_SEAL.json': '7b57069bb8dce7d13eee4c9301f58f15ac62eaed63fe445b1aee63396aad38bb',
    'HOMOGENEOUS_FIELD_STAR_AUTHOR_SEAL.json': '67624b8eafbc339d4c581165ef01ef366035752bfef1e8404faf34edcf6aceaf',
}


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(Path(path).resolve()), 'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def authenticate():
    assert identity(HERE/'PRE_COMPARISON_SEAL.json')['sha256'] == PRE_SHA
    pre = json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    prior = pre['sources'] + pre['artifacts']
    for item in prior:
        assert identity(item['path']) == item
    authors = []
    for name, expected in SEALS.items():
        assert identity(BASE/name)['sha256'] == expected
        rows = json.loads((BASE/name).read_text())['artifacts']
        assert len(rows) == 7
        for row in rows:
            assert identity(row['path']) == row
        authors.extend(rows)
    groups = [
        ('HARDCORE_RECORD_RING_AND_FORMATION_RESULTS.json', 'HARDCORE_RECORD_RING_AND_FORMATION_RUN.log', 'HARDCORE_RECORD_RING_AND_FORMATION_RUN.stderr', 'HARDCORE_RECORD_RING_AND_FORMATION_RUN_RECEIPT.json', 'hardcore_record_ring_and_formation_check.py'),
        ('RECORD_DENSITY_AND_FAST_DEFECT_RESULTS.json', 'RECORD_DENSITY_RUN.stdout', 'RECORD_DENSITY_RUN.stderr', 'RECORD_DENSITY_RUN_RECEIPT.json', 'record_density_and_fast_defect_check.py'),
        ('HOMOGENEOUS_FIELD_STAR_RECORD_RESULTS.json', 'HOMOGENEOUS_FIELD_STAR_RECORD_RUN.stdout', 'HOMOGENEOUS_FIELD_STAR_RECORD_RUN.stderr', 'HOMOGENEOUS_FIELD_STAR_RECORD_RUN_RECEIPT.json', 'homogeneous_field_star_record_check.py'),
    ]
    for result, log, err, receipt, source in groups:
        assert (BASE/result).read_bytes() == (BASE/log).read_bytes()
        assert (BASE/err).read_bytes() == b''
        r = json.loads((BASE/receipt).read_text())
        assert r.get('returncode', r.get('exit_code')) == 0
        assert r.get('script_sha256', r.get('source_sha256')) == identity(BASE/source)['sha256']
        if 'stdout_sha256' in r:
            assert r['stdout_sha256'] == identity(BASE/log)['sha256']
            assert r['stderr_sha256'] == identity(BASE/err)['sha256']
    old_geometry = identity(BASE/'local_gauge_record_cooling_check.py')
    assert old_geometry['sha256'] == '9faf0f87d0574368feb0f656308308c269d3df922bfff7576a8d6d10182b5552'
    return {'prior_bindings': len(prior), 'author_artifact_bindings': len(authors),
            'author_seal_bindings': len(SEALS), 'author_output_equals_full_log': True,
            'prior_geometry_dependency': old_geometry,
            'execution_scope': 'Author runners were read, not rerun. No author module imported.'}


def load_own_builder():
    path = HERE/'finite_sector_check.py'
    assert identity(path)['sha256'] == 'c1e6142e632ae77c14fee1b76079c8cba0f2e9c73cf1fed2e40f84f0a3893122'
    spec = importlib.util.spec_from_file_location('independent_pre_sector', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def effective(a, energy, low):
    r = s.diag(*[s.Rational(1, e) if e else 0 for e in energy])
    h2 = -(a*r*a).extract(low, low)
    k2 = (a*r*r*a).extract(low, low)
    f4 = -(a*r*a*r*a*r*a).extract(low, low)
    return h2, f4 - (k2*h2 + h2*k2)/2


def matrix_strings(matrix):
    return [[str(x) for x in row] for row in matrix.tolist()]


def square_and_statistics(own, author):
    rows = []
    for apart in ({0}, {0, 2}):
        model = own.build(4, [(i, (i+1) % 4) for i in range(4)], apart, 0)
        ids = [i for i, q in enumerate(model['charges']) if all(x >= 0 for x in q)]
        a = -sum(model['hop'], s.zeros(len(model['states']))).extract(ids, ids)
        energy = [model['b'][i] for i in ids]
        low = [j for j, e in enumerate(energy) if not e]
        h2, h4 = effective(a, energy, low)
        target = author['square']['bosonic_cases'][len(apart)-1]
        assert len(ids) == target['physical_sector_dimension']
        assert matrix_strings(h2) == target['second_coefficient']
        assert matrix_strings(h4) == target['normalized_effective_fourth']
        item = {'reference_A_sites': sorted(apart), 'plus_sector_size': len(ids),
                'H2': matrix_strings(h2), 'H4': matrix_strings(h4)}
        if len(apart) == 2:
            fermion = s.zeros(len(ids))
            for edge, hop in zip(model['edges'], model['hop']):
                lo, hi = sorted(edge)
                for jj, state in enumerate(ids):
                    parity = sum(model['charges'][state][v] != 0 for v in range(lo+1, hi))
                    for ii, dest in enumerate(ids):
                        fermion[ii, jj] -= hop[dest, state] * (-1)**parity
            assert fermion == fermion.T
            _, h4f = effective(fermion, energy, low)
            assert matrix_strings(h4f) == author['square']['fermionic_two_record_fourth']
            item['fermionic_H4_same_Fock_basis'] = matrix_strings(h4f)
        rows.append(item)
    return rows


def complex_square():
    # Independently diagonalize reflection sectors of the seven-state square.
    D, a, t, E = s.symbols('D a t E', nonzero=True)
    matrices = {'odd': s.Matrix([[0, -s.sqrt(2)*t], [-s.sqrt(2)*t, a]]),
                'even': s.Matrix([[0, -s.sqrt(2)*t, 0], [-s.sqrt(2)*t, a, -2*t], [0, -2*t, 2*D]])}
    ans = {}
    for name, m in matrices.items():
        c2, c4 = s.symbols('c2 c4')
        det = s.expand((m-E*s.eye(m.rows)).det())
        substituted = s.Poly(s.expand(det.subs(E, c2*t**2+c4*t**4)), t)
        x2 = s.solve(substituted.coeff_monomial(t**2), c2)[0]
        x4 = s.simplify(s.solve(substituted.coeff_monomial(t**4).subs(c2, x2), c4)[0])
        assert x2 == -2/a
        assert s.simplify(x4-(4/a**3 if name == 'odd' else 4/a**3-4/(D*a*a))) == 0
        ans[name] = {'second': str(x2), 'fourth': str(x4)}
    return ans


def fast_defect(author):
    # Assemble the entire fixed-external-flow physical sector by Gauss, without
    # importing either author's enumeration or its prescribed three-state matrix.
    states = []
    for b0, b1 in product((0, 1), repeat=2):
        charge = (b0+b1, 1-b0, 1-b1)
        if max(charge) <= 1:
            states.append(((b0, b1), charge))
    matrix = s.zeros(len(states))
    for i, (bits, q) in enumerate(states):
        for j, (other, qq) in enumerate(states):
            if sum(x != y for x, y in zip(bits, other)) != 1:
                continue
            e = next(k for k in (0, 1) if bits[k] != other[k])
            if (q[0], q[e+1]) == (qq[e+1], qq[0]) and q[0] != q[e+1]:
                matrix[j, i] = -1
    energy = [sum(q[1:])-1 for _, q in states]
    low = [i for i, val in enumerate(energy) if val == 0]
    h2, _ = effective(matrix, energy, low)
    assert len(states) == 3 and h2 == -s.ones(2)
    D, t, E = s.symbols('D t E')
    char = s.factor((D*s.diag(*energy)+t*matrix-E*s.eye(3)).det())
    assert s.simplify(char-E*(D*E-E**2+2*t**2)) == 0
    assert matrix_strings(h2) == author['fast_defect_star']['second_order_matrix_over_t2_over_Delta']
    return {'states': states, 'relative_penalties': energy, 'hop': matrix_strings(matrix),
            'H2': matrix_strings(h2), 'det_H_minus_EI': str(char),
            'boundary': 'Fixed exterior flows; not a periodic three-site torus.'}


def exact_density_cancellations(own):
    # The nontrivial branching physical rectangle already lies in our PRE packet.
    vertices = list(product(range(3), range(2))); index = {x: i for i, x in enumerate(vertices)}
    edges = [(index[x], index[y]) for x in vertices for delta in ((1, 0), (0, 1))
             if (y := (x[0]+delta[0], x[1]+delta[1])) in index]
    apart = {i for i, x in enumerate(vertices) if sum(x) % 2 == 0}
    m = own.build(len(vertices), edges, apart, (1 << len(edges))-1)
    size = len(m['states']); zero = s.zeros(size)
    N = s.diag(*[int(sum(row)) for row in m['occ']])
    B = s.diag(*m['b'])
    K = s.diag(*[sum(q[x] == 0 for x in apart)+m['b'][i] for i, q in enumerate(m['charges'])])
    R = s.diag(*m['field'])
    mA = s.diag(*[sum(q[x] == -1 for x in apart) for q in m['charges']])
    assert B-(N-len(apart)*s.eye(size))/2 == K/2
    assert R == K/2+2*mA
    for a in m['hop']:
        outward = s.zeros(size)
        for i in range(size):
            for j in range(size):
                if B[i, i] == B[j, j]+1:
                    outward[i, j] = a[i, j]
        assert K*outward-outward*K == 2*outward
    channels_checked = 0
    for e, vv in enumerate(m['births']):
        x, y = m['edges'][e]
        a_site = x if x in apart else y
        raising = vv[-1] if a_site == x else vv[1]
        for ops in ([vv[1]+vv[-1]], [vv[1]-vv[-1]], [vv[1], vv[-1]]):
            assert all(K*j-j*K == zero for j in ops)
            assert sum((own.dual(j, R) for j in ops), zero) == 2*raising.T*raising
            channels_checked += 1
    d, C, beta, tau, ep = s.symbols('d C beta tau ep', positive=True)
    square = ep**2*(4*d+2*C*beta*tau)**2
    integral = s.integrate(d*beta*square, (tau, 0, tau))
    want = d*beta*ep**2*(16*d*d*tau+8*d*C*beta*tau*tau+s.Rational(4,3)*C*C*beta*beta*tau**3)
    assert s.simplify(integral-want) == 0
    z = s.sqrt(2)*((2*d+C/(2*(d-1)))*s.exp(2*(d-1)*beta*tau)-C/(2*(d-1)))
    assert s.simplify(s.diff(z, tau)-2*(d-1)*beta*z-s.sqrt(2)*C*beta) == 0
    assert s.simplify(z.subs(tau, 0)-2*s.sqrt(2)*d) == 0
    assert s.simplify(s.limit(z, d, 1).subs(C, 2)-2*s.sqrt(2)*(1+beta*tau)) == 0
    return {'physical_rectangle_dimension': size, 'instrument_edge_checks': channels_checked,
            'K_birth_invariant_and_counterterm': True, 'R_equals_K_over2_plus2minusA': True,
            'exact_R_birth_derivative': '2 V_(A-minus)^dagger V_(A-minus)',
            'integrated_original_bound': str(s.factor(integral)),
            'homogeneous_comparison_ODE_and_d1_limit': True}


def energy_ledgers(own):
    m = own.build(4, [(i, (i+1) % 4) for i in range(4)], {0, 2}, 0)
    size = len(m['states']); a = np.array(sum(m['hop'], s.zeros(size)), float)
    ops = [np.array(v[1]+v[-1], float) for v in m['births']]
    loss = sum((j.T@j for j in ops), np.zeros((size, size)))
    before = [i for i, q in enumerate(m['charges']) if sum(x != 0 for x in q) == 2]
    # Different, moderate parameters from all author numerical rows.
    delta, coupling, beta = 37.0, 4.0, 0.7
    rows = []
    for name, diag, target in [('sublattice', m['b'], 2*delta), ('star', m['field'], delta)]:
        h = delta*np.diag(np.array(diag, float))-coupling*a
        val, vec = la.eigh(h[np.ix_(before, before)])
        psi = np.zeros(size); psi[before] = vec[:, 0]
        adj = beta*sum((j.T@h@j-(j.T@j@h+h@j.T@j)/2 for j in ops), np.zeros_like(h))
        rate = beta*float(psi@loss@psi); power = float(psi@adj@psi)
        residual = power/rate-(target-val[0])
        assert rate > 0 and abs(residual) < 1e-10
        rows.append({'potential': name, 'Delta': delta, 't': coupling, 'beta': beta,
                     'initial_low_energy': float(val[0]), 'birth_rate': rate,
                     'power': power, 'power_per_birth': power/rate,
                     'target_energy_minus_initial': float(target-val[0]), 'residual': residual})
    return rows


def compare_censuses(ring, star):
    own = json.loads((HERE/'FOURTH_ORDER_RESULTS.json').read_text())
    # Independent PRE packet remains the mathematical evidence; below only
    # authenticates the author's declared arithmetical consequences.
    rows = []
    for entry in ring['periodic_lattice_path_columns']:
        d = len(entry['shape']); volume = int(np.prod(entry['shape'])); M = d*volume//2
        assert entry['eligible_first_hops'] == M
        assert entry['distinct_Q_two_excursions'] == (M*(M-1)-M*(2*d-2))//2
        assert entry['fourth_order_diagonal'] == M*(2*d-1)
        assert entry['every_offdiagonal_coefficient'] == -2
        assert entry['four_hop_paths_including_time_orders'] == 4*entry['distinct_Q_two_excursions']+4*entry['offdiagonal_targets']
        assert entry['leading_birth_loss_over_beta_t2_over_Delta2'] == M*(2*d-1)
        rows.append({'shape': entry['shape'], 'word': entry['field_configuration_hex'], 'arithmetic_consistent': True})
    for entry in star['bulk_first_excursions']:
        d = len(entry['shape'])
        assert entry['birth_targets_with_star_energy_1'] == d
        assert entry['birth_targets_with_star_energy_3'] == d-1
        assert abs(entry['mean_bare_target_energy_over_Delta']-(4*d-3)/(2*d-1)) < 1e-15
    return {'author_ring_columns_checked_arithmetically': rows,
            'author_star_columns_checked_arithmetically': len(star['bulk_first_excursions']),
            'independent_PRE_path_result': identity(HERE/'FOURTH_ORDER_RESULTS.json'),
            'limit': 'Random author field words were not used to regenerate every path; PRE has separate exact path enumeration.'}


def main():
    authentication = authenticate()
    own = load_own_builder()
    ring = json.loads((BASE/'HARDCORE_RECORD_RING_AND_FORMATION_RESULTS.json').read_text())
    density = json.loads((BASE/'RECORD_DENSITY_AND_FAST_DEFECT_RESULTS.json').read_text())
    star = json.loads((BASE/'HOMOGENEOUS_FIELD_STAR_RECORD_RESULTS.json').read_text())
    data = {'created_utc': datetime.now(timezone.utc).isoformat(), 'script': identity(__file__),
            'authentication': authentication,
            'square_statistics': square_and_statistics(own, ring),
            'complex_reflection_series': complex_square(), 'fast_defect': fast_defect(density),
            'sharper_density_identities': exact_density_cancellations(own),
            'energy_ledgers': energy_ledgers(own), 'censuses': compare_censuses(ring, star),
            'limits': 'Post-source selective checks. No author runner replay, literature theorem import, volume-uniform field-dynamics inference, or formal audit.'}
    text = json.dumps(data, indent=2)+'\n'
    (HERE/'COMPARISON_RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
