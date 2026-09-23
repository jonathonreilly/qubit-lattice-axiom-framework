#!/usr/bin/env python3
"""Read-only source/stream/receipt authentication for the reconstruction."""
from pathlib import Path
import json,hashlib,platform
import numpy,scipy,sympy
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent.parent/'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md'
EXPECTED='002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(SOURCE)==EXPECTED
rows=[]
for prefix,script in [('BLOCK','block_expansion_check.py'),('DENSITY','density_residual_check.py')]:
 r=json.loads((HERE/(prefix+'_RECEIPT.json')).read_text())
 assert r['exit_code']==0 and r['script_sha256']==sha(HERE/script)
 assert r['builder_sha256']==sha(HERE/'finite_blocks.py')
 assert r['stdout_sha256']==sha(HERE/(prefix+'.stdout'))
 assert r['stderr_sha256']==sha(HERE/(prefix+'.stderr'))
 assert not (HERE/(prefix+'.stderr')).read_bytes()
 assert (HERE/(prefix+'_RESULTS.json')).read_bytes()==(HERE/(prefix+'.stdout')).read_bytes()
 rows.append({'receipt':prefix+'_RECEIPT.json','source_and_builder_and_streams_verified':True})
b=json.loads((HERE/'BLOCK_RESULTS.json').read_text());d=json.loads((HERE/'DENSITY_RESULTS.json').read_text())
assert b['exact_Riccati_orders_1_to_3_zero'] and b['canonical_fourth_formula_verified']
assert b['commutator_M_C0_frobenius_squared']=='202'
assert b['graph_fourth_antihermitian_frobenius_squared']=='202'
assert len(d['density_controls'])==32
assert max(r['trace_error_over_epsilon'] for r in d['density_controls'])==d['maximum_trace_error_over_epsilon']
assert all(r['corrector_hermiticity_error']<1e-12 for r in d['residual_controls'])
assert all(r['corrected_embedding_minimum_eigenvalue']<0 for r in d['residual_controls'])
print(json.dumps({'source':{'path':str(SOURCE),'bytes':len(SOURCE.read_bytes()),'sha256':EXPECTED},
 'execution_receipts':rows,'exact_and_density_result_internal_checks':True,
 'failed_executions':0,'countercontrols_preserved':['Raw graph fourth coefficient is non-Hermitian in canonical coordinates.','Omitting C1 leaves a nonzero fourth-coefficient discrepancy.','The off-block generator discrepancy diverges although the corrected density approximation converges.','The proof corrector is not a positive preparation.'],
 'environment':{'python':platform.python_version(),'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},
 'read_boundary':'Only the single pinned parent model source; no new author compensation or other packet accessed.'},indent=2))
