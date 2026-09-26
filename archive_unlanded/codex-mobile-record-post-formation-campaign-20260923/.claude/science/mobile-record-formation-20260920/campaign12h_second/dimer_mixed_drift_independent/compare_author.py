#!/usr/bin/env python3
"""Authenticate the frozen author evidence and compare with sealed exact sums."""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;RAW=P.parent
def row(f):
    b=f.read_bytes();return {'path':str(f),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pre=json.loads((P/'PRE_COMPARISON_SEAL.json').read_text())
assert row(P/'PRE_COMPARISON_SEAL.json')['sha256']=='0bb97a1123d58603376f6e98c4768d9d45a06b50d6016ef39059c4cd65373790'
for r in pre['sources']+pre['artifacts']:assert row(Path(r['path']))==r
author=json.loads((P/'AUTHOR_SOURCES.json').read_text())
for r in author['sources']:assert row(Path(r['path']))==r
a=json.loads((RAW/'DIMER_MIXED_ENCODING_INITIAL_DRIFT_AMBIGUITY_RESULTS.json').read_text())
assert json.loads((RAW/'DIMER_MIXED_ENCODING_DRIFT_AMBIGUITY_RUN.log').read_text())==a
assert (RAW/'DIMER_MIXED_ENCODING_DRIFT_AMBIGUITY_RUN.stderr').read_bytes()==b''
for r in a['sources']:assert row(Path(r['path']))==r
own=json.loads((P/'INDEPENDENT_RESULTS.json').read_text());d=own['exact_initial_derivatives']
rows=[r for r in d['rows'] if r['x']==1]
assert a['X2_drifts']==[r['X2_derivative'] for r in rows]
assert a['X2_derivative_difference']==d['X2_derivative_difference']
assert a['physical_A2_derivative_difference']==d['A2_derivative_difference']
assert a['minimum_probability']==own['encoding']['minimum_profile_probability']
assert a['same_pair_density_at_all_coordinates'] and all(r['exact_local_density_equality'] for r in own['encoding']['rows'])
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Complete author source/result/streams read. No author runner execution or additional mathematical enumeration; saved exact results compared with independently sealed direct-rate calculations.',
     'pre_rows_verified':len(pre['sources'])+len(pre['artifacts']),'author_files_verified':len(author['sources']),
     'embedded_source_rows_verified':len(a['sources']),'exact_X2_derivatives':a['X2_drifts'],
     'X2_difference':a['X2_derivative_difference'],'A2_difference':a['physical_A2_derivative_difference'],
     'minimum_probability':a['minimum_probability'],'all_reported_mathematical_values_agree':True,
     'author_command_receipt':'None supplied or claimed; source-bound result and both streams are authenticated.',
     'source_drift':'No consequential prose/code discrepancy found. Author contracts the exact current; independent pre-sealed checker separately enumerates the actual rate on all 14^4 configurations.'}
with (P/'COMPARISON_RESULTS.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
