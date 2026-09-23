"""Reauthenticate all frozen rows and seal the completed bounded comparison."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

D=Path(__file__).resolve().parent
A=D.parent/'second_event_author'
ROOT=D.parent.parent
def row(p):
    data=p.read_bytes()
    return {'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
def check(r):
    assert row(Path(r['path']))==r,r['path']
pre_path=D/'PRE_COMPARISON_SEAL.json';pre_row=row(pre_path)
assert pre_row['sha256']=='e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734'
pre=json.loads(pre_path.read_text())
for r in pre['sources']+pre['artifacts']:check(r)
author_path=A/'AUTHOR_SEAL.json';author_row=row(author_path)
assert author_row['sha256']=='47868fa10d852a2c6e57b5600b0f761ccbed01969867c87f53e4cefb71850610'
author=json.loads(author_path.read_text())
sources={r['path']:r for r in pre['sources']}
sources[author_row['path']]=author_row
for key,base in [('files',A),('dependencies',ROOT)]:
    for name,expected in author[key].items():
        r=row(base/name);assert r['sha256']==expected
        sources[r['path']]=r

artifacts={r['path']:r for r in pre['artifacts']}
artifacts[pre_row['path']]=pre_row
new_names=['comparison_check.py','COMPARISON_RESULTS.json','comparison_run.stdout',
           'comparison_run.stderr','comparison_run_RECEIPT.json','COMPARISON.md','seal_comparison.py']
for name in new_names:
    r=row(D/name);artifacts[r['path']]=r
receipt=json.loads((D/'comparison_run_RECEIPT.json').read_text())
assert receipt['exit_code']==0
for key in ('runner','stdout','stderr'):check(receipt[key])
assert not (D/'comparison_run.stderr').read_bytes()
assert (D/'comparison_run.stdout').read_bytes()==(D/'COMPARISON_RESULTS.json').read_bytes()
assert receipt['command']==['/opt/homebrew/opt/python@3.13/bin/python3.13','-B',str(D/'comparison_check.py')]
result=json.loads((D/'COMPARISON_RESULTS.json').read_text())
assert result['PRE_sha256']==pre_row['sha256'] and result['author_seal_sha256']==author_row['sha256']
assert len(sources)==31 and len(artifacts)==57
out={
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'status':'Completed bounded source-informed comparison; no required mathematical correction within stated scope. No formal audit or publication status.',
    'independence_boundary':'The PRE reconstruction and all its bytes precede author access and remain unchanged. New comparison controls are explicitly post-source.',
    'prior_PRE_seal':pre_row,'author_seal':author_row,
    'source_count':len(sources),'artifact_count':len(artifacts),
    'sources':sorted(sources.values(),key=lambda r:r['path']),
    'artifacts':sorted(artifacts.values(),key=lambda r:r['path']),
    'read_and_execution_limits':[
        'Both complete author arguments and all four complete scripts read; every author binding authenticated.',
        'All saved ring scalar/quadrature values and cube polynomial/scalar fields checked against independent definitions; author builders not imported or executed.',
        'The first-sector integer-path Grams, all first-mark weights and symbolic count convolution are new post-source checks.',
        'Author failed quadrature and rejected H4 guess, plus two earlier independent failed assertions, preserved.',
        'Independent exact finite-eta/all-time/mean results remain separate extensions, not author claims.',
        'No finite-spin author packet, checkpoint, registry, plans, external literature or unrelated research opened.'
    ]}
target=D/'FINAL_SEAL.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'comparison':row(D/'COMPARISON.md'),'final_seal':row(target),
                  'source_rows':len(sources),'artifact_rows':len(artifacts)},indent=2))
