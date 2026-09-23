from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent;A=D.parent/'post_birth_fast_motion_author'
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):assert row(Path(r['path']))==r,r['path']
author=row(A/'AUTHOR_SEAL.json');assert author['sha256']=='945fe1a4e76d39c09f435df29409d3dd507af94aed757dfb277f773f4bc5b79f'
sources=json.loads((A/'AUTHOR_SEAL.json').read_text())['artifacts']
for r in sources:verify(r)
assert row(D/'REPORT.md')['sha256']=='ac396a036961d37f8f0deec41538a083d66fb41b18521c714abab2ad998e6727'
artifacts=[row(p) for p in sorted(D.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
out={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Bounded source-informed scientific review complete; no required correction; no formal audit or publication status.','source_informed':True,'author_seal':author,'sources':sources,'artifacts':artifacts,'coverage':'Complete singular-block and exact physical-graph argument, independent legal-hop reconstruction, complete finite-spin matrix control, Bessel check, and all nine author bindings. No author grid replay, no fixed laboratory-time extension.','failures':'One pre-execution wrapper path guard failure is preserved; independent scientific and evidence first runs passed.','excluded':'No other frontier packet, checkpoint, registry, Git or audit state opened or changed.'}
assert not (D/'FINAL_SEAL.json').exists()
(D/'FINAL_SEAL.json').write_text(json.dumps(out,indent=2)+'\n')
for r in sources+artifacts+[author]:verify(r)
print(json.dumps({'report':row(D/'REPORT.md'),'final_seal':row(D/'FINAL_SEAL.json'),'source_rows':len(sources),'artifact_rows':len(artifacts),'author_seal':1},indent=2))
