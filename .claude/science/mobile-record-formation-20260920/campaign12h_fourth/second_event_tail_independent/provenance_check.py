from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, platform
import numpy, scipy, sympy, mpmath
D=Path(__file__).resolve().parent
P=D.parent/'second_event_independent'
expected={
 'REPORT.md':'39e2b04f9140f10db8d8bbd178a086902d9b09f6854b0e317a663071bacf4582',
 'PRE_COMPARISON_SEAL.json':'e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734',
 'FINAL_SEAL.json':'44d2a76280ebbbc97d2a1f34d83c7ccac28647de54d3cceaf6212d17b7b32731',
 'ring_survival_repaired.py':'fdea16a0511ede653dc995dd30978cc077ce35c7656a38b851e1076cf694ece4',
 'RING_EXACT_RESULTS.json':'a874ba8cf03d5c02f63b79dcbce0cc71f981986a2cfca9bc5ba237a9eb290538'}
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
rows=[]
for n,h in expected.items():
 r=row(P/n);assert r['sha256']==h;rows.append(r)
receipt=json.loads((D/'tail_run_RECEIPT.json').read_text())
assert receipt['exit_code']==0
for k in ('runner','stdout','stderr'):
 r=receipt[k];assert row(Path(r['path']))==r
assert not (D/'tail_run.stderr').read_bytes()
assert (D/'tail_run.stdout').read_bytes()==(D/'TAIL_RESULTS.json').read_bytes()
out={'created_utc':datetime.now(timezone.utc).isoformat(),'source_rows':rows,
     'scientific_receipt':receipt,'runtime':{'python':platform.python_version(),'numpy':numpy.__version__,
       'scipy':scipy.__version__,'sympy':sympy.__version__,'mpmath':mpmath.__version__},
     'read_boundary':'Only our previously frozen exact ring clock and its evidence reused. No second_event_tail_author contents, finite-spin folders, campaign plans or checkpoint opened.',
     'known_unopened_author_seal_sha256':'0ffc4d68970054377f6b80c4b5cc0ec593d38380944d8e5d202a6aa0090648c7',
     'new_failed_attempts':[]}
p=D/'SOURCE_BINDINGS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
