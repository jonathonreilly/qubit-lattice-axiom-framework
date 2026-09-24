"""Root exact operator reconstruction; reuses the sealed root Gauss builder.

This is author evidence, not a second independent implementation. All vector
coefficients and moments are rational. The old unpublished Z-norm calculation
is extended to the complete H4 action and loss operator.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/full_rotor_energy_control.py', 'scripts/cube_high_flux_birth.py')
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'cube_high_flux_birth.py'
EXPECTED = 'd3f0a282d6a8ad0024c0794bd507fa3e25a3a500b420f7d77b39cc84eeb8cfab'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED
spec = importlib.util.spec_from_file_location('sealed_root_gauss', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def clean(v):
    return {s: a for s, a in v.items() if a}


def add(*vectors):
    out = defaultdict(F)
    for v in vectors:
        for s, a in v.items():
            out[s] += a
    return clean(out)


def scale(v, factor):
    return clean({s: a * factor for s, a in v.items()})


def dot(v, w):
    return sum((a * w.get(s, 0) for s, a in v.items()), F(0))


def hops(v, outward=True):
    out = defaultdict(F)
    for (q, E), amp in v.items():
        for x, y in m.EDGES:
            a, b = (x, y) if x in m.A else (y, x)
            source, dest = (a, b) if outward else (b, a)
            if q[source] and not q[dest]:
                qq, ff = m.move(q, E, source, dest)
                out[tuple(qq), tuple(ff)] -= amp
    return clean(out)


def z(v):
    return hops(hops(v))


def h4(v):
    return scale(hops(hops(z(v), False), False), F(-1, 2))


def d(v, full=False):
    return clean({s: amp * (sum(e * e for e in s[1]) if full
                            else m.electric(*s)) for s, amp in v.items()})


def birth(v, edge, sign, adjoint=False):
    out = defaultdict(F)
    x, y = edge
    center = x if x in m.A else y
    for (q, E), amp in v.items():
        if adjoint:
            if q[x] != sign or q[y] != -sign:
                continue
            qq, ff = list(q), list(E)
            qq[x] = qq[y] = 0
            ff[m.EDGE[edge]] -= sign
            assert m.gauss(qq, ff)
            for c in range(8):
                if tuple(sorted((center, c))) not in m.EDGE or not qq[c]:
                    continue
                q2, f2 = m.move(qq, ff, c, center)
                if all(q2[a] for a in m.A):
                    out[tuple(q2), tuple(f2)] += amp
        else:
            if not q[center] or q[y if center == x else x]:
                continue
            for c in range(8):
                if tuple(sorted((center, c))) not in m.EDGE or q[c] or c in edge:
                    continue
                qq, ff = m.move(q, E, center, c)
                assert not qq[x] and not qq[y]
                qq[x], qq[y] = sign, -sign
                ff[m.EDGE[edge]] += sign
                assert m.gauss(qq, ff)
                out[tuple(qq), tuple(ff)] += amp
    return clean(out)


def moments(v):
    norm = dot(v, v)
    V = h4(v)
    D = d(v)
    E2 = d(v, True)
    mean_v = dot(v, V) / norm
    mean_d = dot(v, D) / norm
    mean_e2 = dot(v, E2) / norm
    return {
        'norm_squared': norm, 'H4_mean': mean_v,
        'H4_second_moment': dot(V, V) / norm,
        'H4_variance': dot(V, V) / norm - mean_v ** 2,
        'D_mean': mean_d, 'D_variance': dot(D, D) / norm - mean_d ** 2,
        'symmetrized_D_H4_covariance': dot(D, V) / norm - mean_d * mean_v,
        'E2_mean': mean_e2, 'E2_variance': dot(E2, E2) / norm - mean_e2 ** 2,
        'symmetrized_E2_H4_covariance': dot(E2, V) / norm - mean_e2 * mean_v,
        'H4_image_size': len(V), 'Z_norm_squared': dot(z(v), z(v)),
    }


def case(n):
    q, E = m.initial(n)
    omega = {(tuple(q), tuple(E)): F(1)}
    result = {'n': n, 'input': moments(omega), 'instruments': {}}
    for coherent in (False, True):
        vectors = []
        gamma_parts = []
        cross_terms = []
        for edge in m.EDGES:
            plus, minus = birth(omega, edge, 1), birth(omega, edge, -1)
            cross_terms.append(dot(z(plus), z(minus)))
            if coherent:
                v = add(plus, minus)
                vectors.append(v)
                gamma_parts.append(add(birth(v, edge, 1, True),
                                       birth(v, edge, -1, True)))
            else:
                vectors.extend((plus, minus))
                gamma_parts.extend((birth(plus, edge, 1, True),
                                    birth(minus, edge, -1, True)))
        gamma_omega = add(*gamma_parts)
        assert gamma_omega == scale(omega, 48)
        post_d = sum(dot(v, d(v)) for v in vectors)
        post_e2 = sum(dot(v, d(v, True)) for v in vectors)
        post_h4 = sum(dot(v, h4(v)) for v in vectors)
        result['instruments']['coherent' if coherent else 'resolved'] = {
            'number_of_marks': len(vectors),
            'loss_eigenvalue_verified': 48,
            'all_Z_cross_terms': cross_terms,
            'post_D_weighted': post_d,
            'D_drift_over_kappa': post_d - dot(gamma_omega, d(omega)),
            'post_E2_weighted': post_e2,
            'E2_drift_over_kappa': post_e2 - dot(gamma_omega, d(omega, True)),
            'post_H4_weighted': post_h4,
            'H4_drift_over_kappa': post_h4 - dot(gamma_omega, h4(omega)),
        }
    result['selected_resolved'] = moments(birth(omega, (0, 1), 1))
    assert result['input']['H4_mean']==-84 and result['input']['H4_variance']==48
    selected=result['selected_resolved']
    assert selected['H4_mean']==-20 and selected['H4_variance']==392
    assert selected['symmetrized_D_H4_covariance']==0
    assert selected['H4_image_size']==47
    for values in result['instruments'].values():
        assert values['post_H4_weighted']==-816 and values['H4_drift_over_kappa']==3216
        assert values['D_drift_over_kappa']==-96*n*n and values['E2_drift_over_kappa']==96
        assert not any(values['all_Z_cross_terms'])
    result['selected_coherent'] = moments(add(birth(omega, (0, 1), 1),
                                            birth(omega, (0, 1), -1)))
    return result


if __name__ == '__main__':
    rows = [case(n) for n in (-7, -2, -1, 0, 1, 2, 19)]
    print(json.dumps({'source_sha256': EXPECTED,
                      'scope': 'root exact full operator control, not independent',
                      'rows': rows}, default=str, indent=2))
