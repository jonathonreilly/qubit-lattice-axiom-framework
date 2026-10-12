#!/usr/bin/env python3
"""Receipt and response arithmetic only; never opens campaign velocities."""
import datetime
import hashlib
import json
import math
from pathlib import Path
import time

RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RUNTIME/'gravity/response_inverse/independent_margin_review'
manifest=json.loads((OUT/'snapshot_manifest_v1.json').read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
assert not any((RUNTIME/p).exists() for p in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
for row in manifest['sources']+manifest['receipts']:
    assert sha(row['original'])==sha(row['snapshot'])==row['sha256']
sources={Path(r['original']).name:r['sha256'] for r in manifest['sources']}
receipts={Path(r['original']).name:r for r in manifest['receipts']}
freeze=json.loads(Path(receipts['FOLLOWUP_MARGIN_FREEZE.json']['snapshot']).read_text())
candidate=json.loads(Path(receipts['margin_candidate_v1.json']['snapshot']).read_text())
parent=json.loads(Path(receipts['shared_response_fits_v1.json']['snapshot']).read_text())
assert len(parent['cases'])==6
original=next(c['best_sampled'] for c in parent['cases']
              if c['family']=='D' and c['constraints']=='galaxies_external_solar')
E=freeze['fixed_external_newtonian_SI']
assert E==original['external_newtonian_SI']==candidate['external_newtonian_SI']
assert candidate['source_sha256']==sources['direct_margin_candidate.py']
assert candidate['protocol_sha256']==freeze['protocol_sha256']==sources['FOLLOWUP_MARGIN_PROTOCOL.md']
assert candidate['parent_fits_sha256']==freeze['parent_fits_sha256']==receipts['shared_response_fits_v1.json']['sha256']
assert candidate['freeze_sha256']==receipts['FOLLOWUP_MARGIN_FREEZE.json']['sha256']
assert parent['source_sha256']==sources['direct_shared_response_fit.py']
assert parent['operator_source_sha256']==sources['direct_galaxy_response_operator.py']
assert parent['solar_basis_source_sha256']==sources['direct_response_basis.py']
assert parent['protocol_sha256']==sources['FROZEN_DIRECT_INVERSE_PROTOCOL.md']
assert candidate['operator_receipts']==parent['operator_receipts']
for name,expected in candidate['operator_receipts'].items():
    assert sha(OUT.parent/f'operator_{name}_v1.json')==expected
freeze_at=datetime.datetime.fromisoformat(freeze['at'])
candidate_at=datetime.datetime.fromisoformat(candidate['at'])
assert freeze_at<candidate_at
w=candidate['weights'];knots=[10**(-13+j/4) for j in range(21)]
assert len(w)==20 and min(w)>=0 and sum(w)<=100
D=[1+sum(w[j+1:])-w[j]/math.log(knots[j+1]/knots[j]) for j in range(20)]
assert min(D)>0
ramps=[max(0.,min(1.,math.log(hi/E)/math.log(hi/lo))) for lo,hi in zip(knots[:-1],knots[1:])]
ge=E*(1+sum(a*b for a,b in zip(w,ramps)))
assert abs(ge/candidate['predicted_external_physical_SI']-1)<1e-14
assert abs(sum(w)-candidate['total_weight'])<1e-14
external_margin=2*min(ge-2e-10,2.64e-10-ge)/.64e-10
assert abs(external_margin-candidate['external_margin'])<1e-14
z=candidate['secondary_z']
assert abs(candidate['primary_max_z']-z-1e-8)<1e-14
assert min(*candidate['galaxy_matrix_margins'].values(),external_margin,candidate['solar_margin'])>=z-1e-7
assert abs(1-candidate['Q2_s_minus2']/5.2e-27-candidate['solar_margin'])<1e-14
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,
        'source_sha256':sha(__file__),'frozen_sources_unchanged':True,'original_six_fit_receipt_unchanged':True,
        'seconds_between_recorded_freeze_and_candidate':(candidate_at-freeze_at).total_seconds(),
        'fixed_E_SI':E,'primary_z':candidate['primary_max_z'],'secondary_z':z,
        'sum_weights':sum(w),'minimum_D_slack':min(D),'independent_external_physical_SI':ge,
        'independent_external_margin':external_margin,
        'operator_receipts':candidate['operator_receipts'],
        'limits':'Receipt timestamps support recorded ordering, not cryptographic wall-clock proof. No target velocities or field validation opened; no Q2 quadrature repeated here. Solar basis previously independently checked.'}
path=OUT/'provenance_checks_v1.json'
assert not path.exists()
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
