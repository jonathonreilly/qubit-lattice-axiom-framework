from pathlib import Path
import json,hashlib,difflib,math
import numpy as np
from scipy.special import j0
D=Path(__file__).resolve().parent;A=D.parent/'post_birth_fast_motion_author'
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):assert row(Path(r['path']))==r,r['path']
seal=row(A/'AUTHOR_SEAL.json');assert seal['sha256']=='945fe1a4e76d39c09f435df29409d3dd507af94aed757dfb277f773f4bc5b79f'
s=json.loads((A/'AUTHOR_SEAL.json').read_text())
for r in s['artifacts']:verify(r)
a=json.loads((A/'POST_BIRTH_FAST_RING_RESULTS.json').read_text());old=json.loads((A/'initial_probe/POST_BIRTH_FAST_RING_RESULTS.json').read_text());r=json.loads((D/'INDEPENDENT_RESULTS.json').read_text())
for k,v in old.items():
 if k!='source_sha256':assert v==a[k],k
assert a['source_sha256']==row(A/'post_birth_fast_ring_check.py')['sha256']
assert old['source_sha256']==row(A/'initial_probe/post_birth_fast_ring_probe.py')['sha256']
assert (A/'CHECK.stdout').read_bytes()==(A/'POST_BIRTH_FAST_RING_RESULTS.json').read_bytes()
receipt=json.loads((A/'CHECK_RECEIPT.json').read_text());assert receipt['exit_code']==0
for k in ('source','stdout','stderr'):verify(receipt[k])
obs=json.loads((A/'initial_probe/EXECUTION_OBSERVATION.json').read_text())
assert obs['source_sha256']==old['source_sha256'] and obs['result_sha256']==row(A/'initial_probe/POST_BIRTH_FAST_RING_RESULTS.json')['sha256']
cert=a['exact_graph_certificate'];states=r['graph']['first_16_physical_states']
assert cert['ordered_charge_words']==[z[0] for z in states[:15]]
assert cert['vacancy_positions']==[z[0].index(0) for z in states[:15]]
assert cert['oriented_flux_increment_after_one_cycle']==r['graph']['winding_increment'][0]==3
errors=[]
for x in a['spectra']:
 target=np.sort([-2-2*math.cos((2*math.pi*k+3*x['theta'])/15) for k in range(15)])
 error=float(np.max(abs(np.array(x['eigenvalues'])-target)));assert error<1e-13;assert x['post_mark_commutator_frobenius']==2
 errors.append(error)
for x in a['controls']:
 target=(1+2*j0(2*math.sqrt(3)*x['fast_time']))/3
 assert abs(x['bessel_prediction']-target)<1e-15
 assert abs(x['vacancy_still_at_B3']-target)<2e-13
 assert abs(abs(x['vacancy_still_at_B3']-target)-x['absolute_error'])<1e-15
changes=''.join(difflib.unified_diff((A/'initial_probe/post_birth_fast_ring_probe.py').read_text().splitlines(True),(A/'post_birth_fast_ring_check.py').read_text().splitlines(True),fromfile='preserved initial probe',tofile='final expanded graph checker'))
(D/'AUTHOR_SOURCE_DELTA.txt').write_text(changes)
out={'author_seal':seal,'authenticated_artifacts':len(s['artifacts']),'initial_common_result_fields_exactly_unchanged':True,'current_stdout_exact_result_bytes':True,'certificate_matches_independent_physical_route':True,'spectral_rows':len(a['spectra']),'largest_recomputed_spectrum_error':max(errors),'probability_rows':len(a['controls']),'initial_direct_execution_boundary':obs['observation'],'independent_failures':'One wrapper invocation rejected a relative-path argument before executing science; preserved separately. Scientific first run passed.','coverage':'All bound sources/results/receipt inspected or compared completely; no author grid rerun, no RNG or production data.'}
(D/'EVIDENCE_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
