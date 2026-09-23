#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
base=Path(__file__).resolve().parent;D4=base.parent
spec=[(D4/'local_compensation_author/LOCAL_CONSTRUCTION_AUTHOR_SEAL.json','88d002cd35fb4b71859bc23efe2f41d465dd2ac5c33a0826db596934189f70b3'),(D4/'local_compensation_locality_author/AUTHOR_SEAL.json','b275ae727810f32fe3c2721e2c3d294a8dfc9873f5a4a97344590217ffe76413')]
def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 pre=base/'PRE_COMPARISON_SEAL.json';assert bind(pre)['sha256']=='bc1f83597d26466a02d2a1375fea91624b3adb99dcac25f7902262935a9feeb2'
 p=json.loads(pre.read_text());pre_rows=p['sources']+p['artifacts']
 for r in pre_rows:assert bind(Path(r['path']))=={k:r[k] for k in ['path','bytes','sha256']}
 packets=[]
 for s,want in spec:
  assert bind(s)['sha256']==want
  data=json.loads(s.read_text());rows=[]
  for k in ['science_sources','author_artifacts','artifacts']:
   for r in data.get(k,[]):
    assert bind(Path(r['path']))==r
    rows.append({**r,'seal_role':k})
  packets.append({'seal':bind(s),'bindings':rows})
 return {'pre_seal':bind(pre),'pre_bindings_unchanged':len(pre_rows),'author_packets':packets,'boundary':'Hash authentication of every bound source; scientific content reads separately scoped in COMPARISON.md. No author builder imported or executed.'}
if __name__=='__main__':print(json.dumps(main(),indent=2))
