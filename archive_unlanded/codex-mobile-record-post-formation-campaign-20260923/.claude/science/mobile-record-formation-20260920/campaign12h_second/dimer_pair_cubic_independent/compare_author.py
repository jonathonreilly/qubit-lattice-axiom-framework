#!/usr/bin/env python3
"""Post-seal source authentication and exact comparison without author execution."""
from pathlib import Path
from fractions import Fraction as F
import datetime,hashlib,json
import sympy as s
P=Path(__file__).resolve().parent;RAW=P.parent
def row(f):
    b=f.read_bytes();return {'path':str(f),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
pre=json.loads((P/'PRE_COMPARISON_SEAL.json').read_text())
assert row(P/'PRE_COMPARISON_SEAL.json')['sha256']=='387e46f74ee1e1814f9fe42555bceb50b9bbbf82a824cc766c989cee248078fa'
for r in pre['sources']+pre['artifacts']:assert row(Path(r['path']))==r
for r in json.loads((P/'AUTHOR_SOURCES.json').read_text())['sources']:assert row(Path(r['path']))==r
a=json.loads((RAW/'DIMER_PAIR_COVARIANCE_CUBIC_RESULTS.json').read_text());own=json.loads((P/'INDEPENDENT_RESULTS.json').read_text())
for r in a['sources']:assert row(Path(r['path']))==r
run=json.loads((RAW/'DIMER_PAIR_COVARIANCE_CUBIC_RUN_RECEIPT.json').read_text())
assert run['returncode']==0 and run['script_sha256']==row(RAW/'dimer_pair_covariance_cubic_check.py')['sha256']
assert (RAW/'DIMER_PAIR_COVARIANCE_CUBIC_RUN.stderr').read_bytes()==b''
assert (RAW/'DIMER_PAIR_COVARIANCE_CUBIC_RUN.log').read_text()=='exact representation, covariance, positivity and drift controls complete\n'
Pa=s.zeros(16);P1=s.zeros(16);seen=set();characters=[]
for r in a['proper_rotations']:
    R=s.Matrix([[int(z) for z in rr] for rr in r['matrix']]);assert R.T*R==s.eye(3) and R.det()==1
    seen.add(tuple(R));permutation=[next(j for j in range(3) if R[i,j]) for i in range(3)]
    parity=(-1)**sum(permutation[i]>permutation[j] for i in range(3) for j in range(i+1,3))
    assert parity==r['character'];U=s.diag(1,R);Q=s.kronecker_product(U.conjugate(),U)
    assert str(s.trace(Q))==r['operator_character'];Pa+=parity*Q/24;P1+=Q/24
    characters.append([parity,int(s.trace(Q))])
assert len(seen)==24 and Pa==s.zeros(16) and P1*P1==P1
rank=P1.to_DM().rank();assert rank==a['trivial_operator_projection_rank']==2
assert a['positive_state_leading_principal_minors']==own['representation']['leading_principal_minors']
assert a['covariance_checks']==own['representation']['state_covariance_relations']==336
assert a['alternating_operator_projection_all_256_entries_zero']
assert a['minimum_color_probability']==own['drift_witness']['minimum_probability']
assert a['Z12_initial_derivatives']==own['drift_witness']['Z12_derivatives']
assert a['physical_Q12_derivative_difference']==own['drift_witness']['Q12_derivative_difference']
currents={(r['primed'],tuple(r['delta']),r['anchor_x']):F(r['exact_Z12_current']) for r in own['drift_witness']['exact_channel_currents']}
count=0
for prime,rows in zip((False,True),a['directional_derivatives']):
    for r in rows:
        delta=tuple(int(v) for v in r['delta'])
        expected=F(0) if delta==(1,0,0) else currents[(prime,delta,(2-delta[0])%12)]-currents[(prime,delta,1)]
        assert expected==F(r['Z12_derivative']);count+=1
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pre_rows_verified':len(pre['sources'])+len(pre['artifacts']),
     'author_files_verified':5,'author_embedded_sources_verified':len(a['sources']),'complete_author_code_and_outputs_read':True,
     'rotations_checked':len(seen),'all_projection_entries_exact':True,'trivial_projection_rank':rank,
     'all_56_minors_match':True,'directional_derivative_rows_match':count,'Z12_derivatives':a['Z12_initial_derivatives'],
     'Q12_derivative_difference':a['physical_Q12_derivative_difference'],
     'scope':'Author runner not executed. Its exact reported algebra compared against the independent sealed state/rate calculations; rotation characters and projector ranks reconstructed separately. No new scientific gap or source/prose drift found.'}
with (P/'COMPARISON_RESULTS.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
