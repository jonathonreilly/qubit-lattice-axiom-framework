"""Finite exact-source numerical Loewner check for the one-link bound.

The source is the independently built PRE seven-site path matrix, not the
root rotor builder. Floating eigenvalues corroborate; they do not prove the
all-graph inequality or the unbounded-domain passage.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/finite_weight_generator_check.py', 'scripts/finite_path_control.py')

from pathlib import Path
import hashlib
import json
import math
import os

import numpy as np

HERE = Path(__file__).resolve().parent
PRE = HERE / 'FINITE_PATH_RESULTS.json'
assert hashlib.sha256(PRE.read_bytes()).hexdigest() == 'cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553'
OUT = Path(os.environ.get('FIELD_EXPONENTIAL_OUTPUT_DIR', HERE))
OUT.mkdir(parents=True, exist_ok=True)
data = json.loads(PRE.read_text())
n = len(data['states'])


def dense(entries):
    M = np.zeros((n, n), dtype=np.float64)
    for i, j, value in entries:
        M[i, j] = value
    return M


V = dense(data['sparse_H4'])
assert np.array_equal(V, V.T)
Gamma = dense(data['sparse_Gamma'])
resolved = [dense(v) for v in data['resolved_jumps'].values()]
coherent = [dense(v) for v in data['coherent_jumps'].values()]
assert np.array_equal(Gamma, sum(L.T @ L for L in resolved))
assert np.array_equal(Gamma, sum(L.T @ L for L in coherent))

z = 2
C_h = 4 * z**4 * (z-1)
R_e = 2 * z * (z-1)**2
results = []
for link_index, edge in enumerate(data['edges']):
    E = np.array([s['E'][link_index] for s in data['states']], dtype=int)
    for lam in (math.log(2), math.log(3)):
        for cutoff in (None, 0, 1, "absolute", "absolute_cut1"):
            weight_index = E if cutoff is None else np.abs(E) if cutoff == "absolute" else np.minimum(np.abs(E),1) if cutoff == "absolute_cut1" else np.minimum(E,cutoff)
            W = np.exp(lam * weight_index)
            invroot = 1 / np.sqrt(W)
            c = 4 * C_h * math.sinh(lam/2) + 12 * math.exp(lam/2) * math.sinh(lam/2) * R_e
            vals = []
            for channels in (resolved, coherent):
                dissipator = sum(L.T @ np.diag(W) @ L for L in channels)
                dissipator -= (Gamma * W[None, :] + W[:, None] * Gamma) / 2
                generator = 1j * (V * W[None, :] - W[:, None] * V) + dissipator
                weighted = invroot[:, None] * generator * invroot[None, :]
                assert np.max(np.abs(weighted - weighted.conj().T)) < 1e-12
                vals.append(float(np.linalg.eigvalsh(weighted)[-1]))
            assert max(vals) <= c + 1e-9
            results.append(dict(link=list(edge), lambda_name='log2' if lam == math.log(2) else 'log3',
                                cutoff=cutoff, resolved_max_eigenvalue=vals[0],
                                coherent_max_eigenvalue=vals[1], analytic_bound=c,
                                conventions_agree=abs(vals[0]-vals[1]) < 1e-10))

result = dict(source_sha256=hashlib.sha256(PRE.read_bytes()).hexdigest(),
              matrix_dimension=n, entries=len(results),
              max_observed_ratio=max(max(v['resolved_max_eigenvalue'], v['coherent_max_eigenvalue'])/
                                     v['analytic_bound'] for v in results),
              min_analytic_margin=min(v['analytic_bound']-
                                      max(v['resolved_max_eigenvalue'], v['coherent_max_eigenvalue'])
                                      for v in results),
              all_analytic_bounds_hold=True,
              all_coherent_resolved_weighted_eigenvalues_agree=all(v['conventions_agree'] for v in results),
              rows=results,
              scope='Finite seven-site numerical matrix check only; no all-graph proof.')
(OUT / 'FINITE_WEIGHT_GENERATOR_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k != 'rows'}, indent=2))
