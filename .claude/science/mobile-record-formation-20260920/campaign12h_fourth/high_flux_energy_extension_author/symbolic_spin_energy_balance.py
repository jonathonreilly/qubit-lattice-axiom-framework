"""Exact symbolic all-path energy sums for the author's cube family.

Imports the sealed root Gauss/hop builder; not independent verification.
The 48 individual rational path weights and energies are saved, so symbolic
factorization supplements the explicit path certificate rather than fitting
an asymptotic polynomial to finite-spin observations.
"""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
FALLBACK = Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth')
SOURCE = HERE.parent / 'high_flux_energy_author/cube_high_flux_birth.py'
if not SOURCE.exists():
    SOURCE = FALLBACK / 'high_flux_energy_author/cube_high_flux_birth.py'
SOURCE_SHA = 'c1a13a2c954095fe1fb76272d7f13abe498220ab1e95d167cc150e136e031a9c'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA
spec = importlib.util.spec_from_file_location('root_gauss', SOURCE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
n, C = sp.symbols('n C', real=True)
q, E = m.initial(n)


def weight(e, shift):
    return 1 - e * (e + shift) / C


rows = []
for edge in m.EDGES:
    x, y = edge
    a, b = (x, y) if x in m.A else (y, x)
    for c in range(8):
        old_edge = tuple(sorted((a, c)))
        if c == b or old_edge not in m.EDGE:
            continue
        old_shift = -1 if a < c else 1
        old_weight = weight(E[m.EDGE[old_edge]], old_shift)
        mid_q, mid_E = m.move(q, E, a, c)
        for sign in (-1, 1):
            path_weight = old_weight * weight(mid_E[m.EDGE[edge]], sign)
            out_q, out_E = list(mid_q), list(mid_E)
            out_q[x], out_q[y] = sign, -sign
            out_E[m.EDGE[edge]] += sign
            assert m.gauss(out_q, out_E)
            rows.append({'edge': edge, 'old_destination': c, 'sign': sign,
                         'weight': sp.factor(path_weight),
                         'D': sp.expand(m.electric(out_q, out_E)),
                         'E2': sp.expand(sum(e * e for e in out_E)),
                         'charges': out_q, 'field': out_E})
rate = sp.factor(sum(r['weight'] for r in rows))
post_d = sp.factor(sum(r['weight'] * r['D'] for r in rows))
post_e2 = sp.factor(sum(r['weight'] * r['E2'] for r in rows))
summary = {'rate': rate, 'post_D_weighted': post_d,
           'D_drift_over_kappa': sp.factor(post_d - 4*n*n*rate),
           'post_E2_weighted': post_e2,
           'E2_drift_over_kappa': sp.factor(post_e2 - 4*n*n*rate)}
x = sp.symbols('x', positive=True)
S = sp.symbols('S', positive=True)
summary['high_flux_rate_limit'] = sp.limit(rate.subs({n:x*S,C:S*(S+1)}),S,sp.oo)
summary['high_flux_D_drift_over_kappa_n2_limit'] = sp.factor(sp.limit(
    (summary['D_drift_over_kappa']/n**2).subs({n:x*S,C:S*(S+1)}),S,sp.oo))
summary['high_flux_E2_drift_over_kappa_limit'] = sp.factor(sp.limit(
    summary['E2_drift_over_kappa'].subs({n:x*S,C:S*(S+1)}),S,sp.oo))
print(json.dumps({'source_sha256':SOURCE_SHA,'path_count':len(rows),
                  'summary':summary,'paths':rows},default=str,indent=2))
