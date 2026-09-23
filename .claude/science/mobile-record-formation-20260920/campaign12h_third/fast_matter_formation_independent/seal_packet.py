from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent; B=D.parent

def row(p):
 p=Path(p); b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def verify(r):
 assert row(r['path'])==r, r['path']
author=row(B/'FAST_MATTER_FORMATION_AUTHOR_SEAL.json')
assert author['sha256']=='5aeee4c3db513daafc32c22ceb7e2a7c5dc0c1a3e7d89208fec4244806c67577'
sources=json.loads(Path(author['path']).read_text())['artifacts']
for r in sources: verify(r)
extras={
 'finite_formation_independent/finite_control.py':'abb86e2fec6d9202471dc1cd3a0a1cc27a4758202b42550d3231ededc8c728d1',
 'finite_formation_independent/FINAL_SEAL.json':'b558e79f077b639690d702d0dbcd6328b724c8768defc093ef0714e852c51004',
 'large_spin_rotor_independent/FINAL_SEAL.json':'7620bb6ff3b16ec319f12ad0d588d45a56f0fd084ed192b59e8c86d0f9ac30d4'}
for name,h in extras.items():
 r=row(B/name);assert r['sha256']==h; sources.append(r)
assert row(D/'REPORT.md')['sha256']=='0a114dadc553ccbb4ef9bf15faf87a70f64a0d5719bf1d1743de86b94a0205b5'
artifacts=[row(p) for p in sorted(D.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
s={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Source-informed bounded scientific review complete; no required correction; no formal audit or publication status.','source_informed':True,'author_seal':author,'sources':sources,'artifacts':artifacts,'coverage':'Full current arguments and necessary premises, independent exact coefficients and residual-map checks, complete author source/history inspection and selective independent no-event endpoint; no complete author grid replay.','excluded':'FOURTH_SCALE_REPEATED_FORMATION_AUTHOR_SEAL and later frontier/checkpoint/registry were not opened.'}
assert not (D/'FINAL_SEAL.json').exists()
(D/'FINAL_SEAL.json').write_text(json.dumps(s,indent=2)+'\n')
for r in s['sources']+s['artifacts']+[s['author_seal']]:verify(r)
print(json.dumps({'report':row(D/'REPORT.md'),'final_seal':row(D/'FINAL_SEAL.json'),'sources':len(sources),'artifacts':len(artifacts),'top_level_author_seal':1},indent=2))
