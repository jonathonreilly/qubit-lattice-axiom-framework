from pathlib import Path
import json,hashlib,datetime
D=Path(__file__).resolve().parent;B=D.parent

def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):assert row(Path(r['path']))==r,r['path']
author=row(B/'FIRST_EVENT_INSTRUMENT_AUTHOR_SEAL.json');assert author['sha256']=='2c446eb379dafa054df99ecb872e25ba0a9799d0f4801398132506bf0f2c48da'
sources=json.loads(Path(author['path']).read_text())['artifacts']
for r in sources:verify(r)
for rel,h in [('fast_matter_formation_independent/FINAL_SEAL.json','63ddf9823aa23d678e8f61863ddeedf36596918e2cb600f100fa334e6d1432db'),('finite_formation_independent/FINAL_SEAL.json','b558e79f077b639690d702d0dbcd6328b724c8768defc093ef0714e852c51004')]:
 r=row(B/rel);assert r['sha256']==h;sources.append(r)
assert row(D/'REPORT.md')['sha256']=='ec6fed3b6c3646f2bb0d2928fff7e605cdf6dac01abec11e071517e4224006ab'
artifacts=[row(p) for p in sorted(D.iterdir()) if p.is_file() and p.name!='FINAL_SEAL.json']
s={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Bounded source-informed review complete; F1 and F2 corrected and acknowledged, no unresolved mathematical finding in scope. No formal audit or publication status.','source_informed':True,'author_seal':author,'sources':sources,'artifacts':artifacts,'findings':{'F1':'Closed: zero total rate explicitly has no first event; normalized probabilities require r>0.','F2':'Closed: removes overbroad matter-erasure information-loss claim; orthogonal field-divergence recovery is qualified.'},'independent_control':'Exact independently assembled K2,3 two-cycle physical rotor sector: all 12 resolved and 6 coherent Gram and recovery maps, plus zero-rate countercontrol.','scope':'Unit-rotor first mark, retained links and mark, logical recovery; no physical annihilating inverse, later-event or erased-mark theorem.'}
assert not (D/'FINAL_SEAL.json').exists()
(D/'FINAL_SEAL.json').write_text(json.dumps(s,indent=2)+'\n')
for r in sources+artifacts+[author]:verify(r)
print(json.dumps({'report':row(D/'REPORT.md'),'correction_ack':row(D/'CORRECTION_ACK.json'),'final_seal':row(D/'FINAL_SEAL.json'),'source_rows':len(sources),'artifact_rows':len(artifacts),'author_seal':1},indent=2))
