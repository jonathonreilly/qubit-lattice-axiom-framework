from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
D=Path(__file__).resolve().parent;A=D.parent/'second_event_tail_author'
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(r):assert row(Path(r['path']))==r,r['path']
pr=row(D/'PRE_COMPARISON_SEAL.json');ar=row(A/'AUTHOR_SEAL.json')
assert pr['sha256']=='0aac7b39eefeacd4464660b824af56638ed05f30865abcc2cd16024a756bbb2c'
assert ar['sha256']=='0ffc4d68970054377f6b80c4b5cc0ec593d38380944d8e5d202a6aa0090648c7'
pre=json.loads(Path(pr['path']).read_text());author=json.loads(Path(ar['path']).read_text())
for r in pre['sources']+pre['artifacts']+author['sources']+author['artifacts']:check(r)
sources={r['path']:r for r in pre['sources']+author['sources']+author['artifacts']+[ar]}
artifacts={r['path']:r for r in pre['artifacts']+[pr]}
for n in ['comparison_check.py','COMPARISON_RESULTS.json','comparison_run.stdout','comparison_run.stderr',
          'comparison_run_RECEIPT.json','COMPARISON.md','seal_comparison.py']:
 r=row(D/n);artifacts[r['path']]=r
r=json.loads((D/'comparison_run_RECEIPT.json').read_text());assert r['exit_code']==0
for key in ('runner','stdout','stderr'):check(r[key])
assert not (D/'comparison_run.stderr').read_bytes()
assert (D/'comparison_run.stdout').read_bytes()==(D/'COMPARISON_RESULTS.json').read_bytes()
assert len(sources)==12 and len(artifacts)==21
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Completed bounded source-informed comparison; no required mathematical correction within the stated scope. No formal audit or publication status.',
 'prior_PRE':pr,'author_seal':ar,'sources':sorted(sources.values(),key=lambda r:r['path']),
 'artifacts':sorted(artifacts.values(),key=lambda r:r['path']),
 'coverage':['Full author note, runner, result, streams and receipt read; all eight author bindings authenticated.',
             'Exact complete Lyapunov matrices solved anew; all 36 two-state rows, 24 tail rows and five excision rows checked.',
             'Tail rows checked by a separately derived frequency integral; no author builder imported or executed.',
             'PRE unchanged. Additional independent Laplace and general positive-moment/density results remain separately attributed.'],
 'excluded':['Finite-spin and other new author packets','Campaign plans/checkpoint/registry','Microscopic long-time or infinite-volume extension','Publication or formal audit status'],
 'new_failed_attempts':[]}
p=D/'FINAL_SEAL.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'comparison':row(D/'COMPARISON.md'),'FINAL':row(p),'source_rows':len(sources),'artifact_rows':len(artifacts)},indent=2))
