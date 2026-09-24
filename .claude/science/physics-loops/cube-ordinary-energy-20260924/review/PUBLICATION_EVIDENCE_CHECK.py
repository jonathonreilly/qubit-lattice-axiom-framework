#!/usr/bin/env python3
"""Read-only source/result correspondence; no scientific runner execution."""
from pathlib import Path
import ast,hashlib,json,re
HERE=Path(__file__).resolve().parent
PUB=HERE.parent/'ordinary-energy-publication'
S=HERE/'PUBLICATION_sources'
runner='scripts/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py'
rb=(PUB/runner).read_bytes();rsha=hashlib.sha256(rb).hexdigest()
assert rsha=='4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d'
tree=ast.parse(rb)
paths=None
for node in tree.body:
 if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUDIT_INPUT_PATHS' for t in node.targets):paths=ast.literal_eval(node.value)
assert paths and len(paths)==len(set(paths))
digest=hashlib.sha256();digest.update(b'runner-cache-input-fingerprint-v1\0');inputs=[]
for rel in paths:
 body=(PUB/rel).read_bytes();name=rel.encode()
 digest.update(len(name).to_bytes(8,'big'));digest.update(name)
 digest.update(len(body).to_bytes(8,'big'));digest.update(body)
 inputs.append({'path':rel,'sha256':hashlib.sha256(body).hexdigest()})
fp=digest.hexdigest()
execution=json.loads((S/'THIRD_PUBLICATION_CACHE_EXECUTION.json').read_text())
result=json.loads((S/'ORDINARY_ENERGY_CONTROL_RESULTS.json').read_text())
r=execution['result'];assert r['status']=='ok' and r['exit_code']==0 and r['stderr']==''
assert r['runner']==runner and result['source_sha256']==rsha
stdout=r['stdout'];decoder=json.JSONDecoder();objects=[];offset=0
while True:
 while offset<len(stdout) and stdout[offset].isspace():offset+=1
 if offset>=len(stdout) or stdout[offset]!='{':break
 value,end=decoder.raw_decode(stdout,offset);objects.append(value);offset=end
assert len(objects)==6
assert objects[0]==result['structural']
assert objects[1:5]==result['second_high_band']['projector_rows']
assert objects[5]==result
assert stdout[offset:].strip()=='TOTAL: PASS=4 FAIL=0'
cache=(S/'ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.txt').read_text()
header,cstdout=cache.split('----- stdout -----\n',1)
cstdout,cstderr=cstdout.rsplit('----- stderr -----\n',1)
assert cstdout.strip()==stdout.strip() and cstderr.strip()==''
assert f'runner_sha256: {rsha}' in header
assert f'input_fingerprint_sha256: {fp}' in header
assert 'exit_code: 0' in header and 'status: ok' in header
rows=result['second_high_band']['projector_rows']
assert [x['epsilon'] for x in rows]==[.12,.08,.05,.03]
assert all(x['quadrature_difference']<5e-11 for x in rows)
assert all(all(2<z<12 for z in x['norm_over_epsilon_fourth']) for x in rows)
assert all(x['preparation']['eigen_residual']<2e-10 and x['preparation']['orthogonality_error']<2e-10 and x['preparation']['minimum_overlap_eigenvalue']>.6 for x in rows)
assert all(x['integer_residual_nonzeros']==0 and x['changed_middle_coefficient_norm']>0 for x in result['second_high_band']['leading_cancellation'])
checks={'runner_sha256':rsha,'declared_input_fingerprint_sha256':fp,'declared_inputs':inputs,
 'execution_status':r['status'],'exit_code':r['exit_code'],'stderr_empty':True,
 'complete_stdout_objects_match_result_json':True,'cache_stdout_matches_execution':True,
 'execution_elapsed_seconds':r['elapsed_sec'],'result_elapsed_seconds':result['elapsed_seconds'],
 'complete_physical_dimensions':result['second_high_band']['complete_physical_dimensions'],
 'maximum_contour_refinement_difference':max(x['quadrature_difference'] for x in rows),
 'maximum_eigen_residual':max(x['preparation']['eigen_residual'] for x in rows),
 'minimum_overlap_eigenvalue':min(x['preparation']['minimum_overlap_eigenvalue'] for x in rows),
 'verification_scope':'Source/receipt/cache/output correspondence, no independent rerun of the scientific numerical calculation.'}
(HERE/'PUBLICATION_EVIDENCE_VALIDATION.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
