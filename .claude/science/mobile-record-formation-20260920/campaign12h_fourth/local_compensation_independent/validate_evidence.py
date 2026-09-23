#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent
D4=base.parent;D3=D4.parent/'campaign12h_third'
def binding(p,expected=None):
 b=p.read_bytes();h=hashlib.sha256(b).hexdigest()
 if expected is not None:assert h==expected,(str(p),h)
 return {'path':str(p),'bytes':len(b),'sha256':h}

def main():
 source_specs=[
 (D3/'FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md','002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e','Complete parent definition and bounded target proof, reread'),
 (D4/'compensation_target_independent/REPORT.md','dcd02298d9a27ea9eadfb387a81f9f1336c66f681fb84933ee48cac225ed5401','Reused independently checked general compensation theorem; relevant derivation reread'),
 (D4/'compensation_target_independent/PRE_COMPARISON_SEAL.json','0504a3fc90cca1b0f9b7bab3a1aa346b11e0889bc25abf55bd65966965375a46','Unchanged independent provenance'),
 (D4/'compensation_target_independent/FINAL_SEAL.json','d29e5a9e335bce98e5cd405318beb2373e84ffdd116768637147f5c13fed2854','Unchanged comparison provenance'),
 (D4/'local_compensation_author/ROOT_GENERAL_TARGET_CORRECTION.md','c906ed162db678fc2f10bc67afd2af22d929be3fe97fd3a1658cfe12ecd339a9','Only newly authorized author read; narrow self-adjointness qualification'),
 (D4/'compensation_target_independent/correction_ack/F1_ACK.json','a2347caff2ae4c09d9066a0a359ee9af60e43c66e3bd1e9dd27908b207160d6a','Separate completed correction acknowledgment'),
 (D4/'compensation_target_independent/correction_ack/ACK_SEAL.json','9aa5e1d41b8e6021dfa22d80ad497d3c8d6fd568c7528b2a41688ef0aa2e5b7a','Separate acknowledgment identity'),
 (D4/'cube_point_spectrum_independent/cube_point_check.py','f25ade25a98715a142f53c11c64df730d51dbfb242a3ae4550a8e0f66b8c2265','Own earlier cube physical-coordinate builder, reread; not imported'),
 (D4/'second_event_independent/operators.py','a152167dff2cfff397397fcc56121cd9b2d79d7f412eb2e134f2f9cbbfa54c95','Own earlier legal-hop/formation conventions, reread; not imported')]
 sources=[]
 for p,h,scope in source_specs:
  row=binding(p,h);row['reuse_or_read_scope']=scope;sources.append(row)
 target=base/'SOURCE_BINDINGS.json';assert not target.exists();target.write_text(json.dumps({'read_boundary':'No specific author construction accessed; independent precomparison stage','sources':sources},indent=2)+'\n')
 receipts=[]
 for label in ['ROTOR','GRAM','SPIN']:
  r=json.loads((base/(label+'_RECEIPT.json')).read_text());assert r['exit_code']==0
  for row in r['inputs']+r['outputs']:
   assert binding(Path(row['path']))==row
  raw=(base/(label+'.stdout')).read_bytes();parsed=json.loads(raw)
  assert (base/(label+'.stderr')).read_bytes()==b''
  result=base/(label+'_RESULTS.json');assert not result.exists();result.write_bytes(raw)
  receipts.append({'label':label,'receipt':binding(base/(label+'_RECEIPT.json')),'result':binding(result),'empty_stderr':True})
 rotor=json.loads((base/'ROTOR_RESULTS.json').read_text());gram=json.loads((base/'GRAM_RESULTS.json').read_text());spin=json.loads((base/'SPIN_RESULTS.json').read_text())
 assert rotor['cube_initial_H4']['diagonal']==-84
 assert rotor['two_formation_witness']['ordered_output_norm_squared']==1
 assert [r['expectation_on_equal_plus_pair'] for r in gram['cube_formation_Grams']]==[9,9]
 assert spin['eight_site_tree_recycling_control']['rotor_number_probabilities_at_final_time']['8']>0
 return {'source_bindings_verified':len(sources),'scientific_runs_authenticated':receipts,'preserved_failures':'No failed executions. Ungated zero-fourth-order and field-dependent hazard countercontrols preserved.','proof_vs_controls':'Report contains the proof. Finite Gaussian-integer/path and finite floating generator controls corroborate it without author-builder imports.','prior_evidence_unchanged':True}

if __name__=='__main__':print(json.dumps(main(),indent=2))
