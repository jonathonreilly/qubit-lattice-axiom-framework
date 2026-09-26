"""Root exact electric identities using the explicitly bound root path helper.

This reuses the capacity author's elementary rotor builder, not an independent
reconstruction. New calculations test complete sparse moment identities and
both instrument conventions. No trajectory or cutoff-evolution fit is made.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import importlib.util, sys, hashlib, json, time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
HELPER = HERE.parent/'formation_capacity_author/capacity_and_dark_state_check.py'
EXPECTED = '3e9621b36280d19373909922b104c1ead0df9aa47c043d372abd9f9424393a4a'
assert hashlib.sha256(HELPER.read_bytes()).hexdigest() == EXPECTED
spec = importlib.util.spec_from_file_location('bound_root_rotor_paths', HELPER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def compact(v):
    return {s: a for s, a in v.items() if a}


def add(dst, vector, coefficient=1):
    for s, a in vector.items():
        dst[s] += coefficient*a


def channel(g, state, edge, sign, adjoint=False):
    if sign is not None:
        return g.jump(state, edge, sign, adjoint)
    out = defaultdict(int)
    for sigma in (-1, 1):
        add(out, g.jump(state, edge, sigma, adjoint))
    return compact(out)


def moment_columns(g, state, observed, coherent):
    Ein = state[1][observed]
    twice_b, twice_m, q = defaultdict(int), defaultdict(int), defaultdict(int)
    for edge in range(len(g.edges)):
        for sigma in ([None] if coherent else [-1, 1]):
            def adj(s):
                return channel(g, s, edge, sigma, True)
            Lpsi = channel(g, state, edge, sigma)
            gram = m.apply(adj, Lpsi)
            middle1 = m.apply(adj, {s: s[1][observed]*a for s, a in Lpsi.items()})
            middle2 = m.apply(adj, {s: s[1][observed]**2*a for s, a in Lpsi.items()})
            add(twice_b, middle1, 2)
            add(twice_m, middle2, 2)
            for s, a in gram.items():
                Eout = s[1][observed]
                twice_b[s] -= (Ein+Eout)*a
                twice_m[s] -= (Ein**2+Eout**2)*a
            Cpsi = {s: (s[1][observed]-Ein)*a for s, a in Lpsi.items()}
            def Cadjoint(s):
                return {v: (s[1][observed]-v[1][observed])*a for v, a in adj(s).items()}
            CdagC = m.apply(Cadjoint, Cpsi)
            assert CdagC.get(state, 0) == m.norm2(Cpsi)
            add(q, CdagC)
    twice_b, twice_m, q = map(compact, (twice_b, twice_m, q))
    residual = defaultdict(int, twice_m)
    for s, a in twice_b.items():
        residual[s] -= (Ein+s[1][observed])*a
    add(residual, q, -2)
    assert not compact(residual)
    assert all(g.gauss(s) for v in (twice_b, twice_m, q) for s in v)
    return twice_b, twice_m, q


def graph_checks(g, name):
    z = max(len(g.adj[a]) for a in g.A)
    Cd, Q, Ch = 4*(z-1)**2, 2*z*(z-1), 4*z**4*(z-1)
    count = seeds = 0
    maxima = dict(twice_drift_column_norm_squared=0, q_column_norm_squared=0,
                  Hamiltonian_drift_column_norm_squared=0)
    for state in m.all_physical_words(g):
        seeds += 1
        h = g.magnetic(state)
        for observed in range(len(g.edges)):
            r = moment_columns(g, state, observed, False)
            c = moment_columns(g, state, observed, True)
            assert r == c
            twice_b, twice_m, q = r
            Ein = state[1][observed]
            # Divide the Hamiltonian commutator by i for exact integer algebra.
            bh = {s: (Ein-s[1][observed])*a for s, a in h.items()}
            mh = {s: (Ein**2-s[1][observed]**2)*a for s, a in h.items()}
            assert compact(mh) == compact({s: (Ein+s[1][observed])*a for s, a in bh.items()})
            assert m.norm2(twice_b) <= (2*Cd)**2
            assert m.norm2(q) <= Q**2
            assert m.norm2(bh) <= Ch**2
            maxima['twice_drift_column_norm_squared'] = max(maxima['twice_drift_column_norm_squared'], m.norm2(twice_b))
            maxima['q_column_norm_squared'] = max(maxima['q_column_norm_squared'], m.norm2(q))
            maxima['Hamiltonian_drift_column_norm_squared'] = max(maxima['Hamiltonian_drift_column_norm_squared'], m.norm2(bh))
            count += 2
    return {'graph': name, 'maximum_A_degree': z, 'Gauss_matter_words': seeds,
            'both_instrument_field_columns': count, 'exact_dissipative_quadratic_identity': True,
            'exact_Hamiltonian_derivation_identity': True, 'coherent_and_resolved_E_and_E_squared_images_equal': True,
            'analytic_constants_at_delta_kappa_1': {'C_h': Ch, 'C_d': Cd, 'Q': Q},
            'largest_observed_column_norms_squared': maxima,
            'scope': 'One spanning-tree field per allowed matter word; sparse output identities include all generated fields. Column checks corroborate, but do not prove, the separately derived operator-norm bounds.'}


def initial_star(d):
    zero = (0,)*d
    neighbors = [tuple(sign*int(i == j) for i in range(d))
                 for j in range(d) for sign in (-1, 1)]
    # Alternate stored orientations to check the electric sign convention.
    edges = [(0, i+1) if i % 2 == 0 else (i+1, 0) for i in range(2*d)]
    g = m.Graph([zero]+neighbors, edges)
    state = g.flow([1]+[0]*(2*d))
    rows = []
    for observed, (u, v) in enumerate(g.edges):
        orient = 1 if u == 0 else -1
        answer = []
        for coherent in (False, True):
            b, e2, q = moment_columns(g, state, observed, coherent)
            drift = Fraction(b.get(state, 0), 2)
            second = Fraction(e2.get(state, 0), 2)
            assert drift == -2*(2*d-1)*orient
            assert second == q.get(state, 0) == 4*(2*d-1)
            answer.append({'instrument': 'coherent' if coherent else 'resolved',
                           'initial_E_drift_over_kappa': str(drift),
                           'initial_E_squared_drift_over_kappa': str(second)})
        rows.append({'stored_orientation_relative_to_A_to_B': orient, 'results': answer})
    return {'d': d, 'z': 2*d, 'rows': rows,
            'scope': 'All channels that can affect the chosen link are anchored at its A endpoint. The initial Hamiltonian contribution to either diagonal field expectation is analytically zero; the star isolates the exact initial dissipative diagnostic.'}


def main():
    started = time.monotonic()
    path = m.Graph([(i,) for i in range(8)], [(i, i+1) for i in range(7)])
    ring = m.Graph([(i,) for i in range(8)], [(i, (i+1) % 8) for i in range(8)])
    rows = [graph_checks(g, label) for g, label in [(path, 'path8'), (ring, 'ring8'), (m.box(3, 2), 'cubeQ3')]]
    result = {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'inherited_root_helper': {'path': str(HELPER), 'sha256': EXPECTED, 'bytes': HELPER.stat().st_size},
              'exact_moment_identities': rows, 'initial_physical_diagnostics': [initial_star(d) for d in (2, 3, 4)],
              'elapsed_seconds': time.monotonic()-started,
              'scope': 'Root exact integer/Fraction algebra; explicit root-builder reuse. No independent-check claim, numerical evolution, thermodynamic extrapolation or cutoff-dynamics error estimate.'}
    target = HERE/'MOMENT_IDENTITY_RESULTS.json'
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
