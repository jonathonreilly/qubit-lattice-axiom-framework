"""Activate corrected runtime contracts at required paths, preserving prior versions."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
N=Path(__file__).resolve().parents[1];W=N.parent/'correlation_worktree';D=N/'publication_integration/reflection_preparation_runner_repair'
def rd(p):return json.loads(p.read_text())
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def write(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
assert not (D/'actions').exists() and not (D/'canonical_source').exists()
assert subprocess.check_output(['git','status','--porcelain','-z'],cwd=W)==b''
A=D/'superseded_runtime_contracts';A.mkdir()
saved=[]
for name in ('ACTUAL_BASE_BINDING_INPUT.json','ROOT_BINDING_INPUT.json'):
 p=D/name;b=p.read_bytes();target=A/name;target.write_bytes(b);assert target.read_bytes()==b
 saved.append(dict(original=pin(p),preserved=pin(target)))
write(A/'PRESERVATION.json',dict(utc=datetime.now(timezone.utc).isoformat(),files=saved,scope='Runtime inputs before any successful prepare; original bytes preserved at explicit archive paths. Actual previous reviews still identify their original historical bytes.'))
write(D/'ROOT_PATH_GUARD_OBSERVATION.json',dict(kind='actual_tool_observation_not_reconstructed_process_receipt',utc=datetime.now(timezone.utc).isoformat(),tool_chunk='04db37',actual_exit_code=1,failure="bind_runtime requires exactly D/ROOT_BINDING_INPUT.json and D/ACTUAL_BASE_BINDING_INPUT.json; suffixed v2 paths refused",phase_started=False,canonical_mutations=False,scope='No action receipt/capture existed; none invented. Corrected values now activated only at required runtime paths after preserving originals.',preservation=pin(A/'PRESERVATION.json')))
base=rd(D/'ACTUAL_BASE_BINDING_INPUT_v2.json');write(D/'ACTUAL_BASE_BINDING_INPUT.json',base)
r=rd(D/'ROOT_INTEGRATION_REVIEW_v2.json');r['utc']=datetime.now(timezone.utc).isoformat();r['actual_base_binding']=pin(D/'ACTUAL_BASE_BINDING_INPUT.json')
r['runtime_path_correction']=pin(D/'ROOT_PATH_GUARD_OBSERVATION.json');r['preserved_original_runtime_contracts']=pin(A/'PRESERVATION.json')
r['scope']+=' Runtime input filenames are fixed by the unchanged adapter; suffixed inputs were refused before phase execution. Original inputs now archived byte-exactly; corrected base activated at required path. New root input will bind this actual review execution.'
write(D/'ROOT_INTEGRATION_REVIEW_v3.json',r)
print(json.dumps(dict(review=pin(D/'ROOT_INTEGRATION_REVIEW_v3.json'),base=pin(D/'ACTUAL_BASE_BINDING_INPUT.json'),preservation=pin(A/'PRESERVATION.json'),observation=pin(D/'ROOT_PATH_GUARD_OBSERVATION.json'))))

