from pathlib import Path
import json,itertools,time,hashlib
from fractions import Fraction as F
p=Path('/private/tmp/review-drain-20260915/check8061/original-8061/outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs');read=lambda n:json.loads((p/n).read_text());start=time.monotonic()
a=read('ADAPTED.json');b=read('BLOCKS.json');l=read('LEDGER.json');t=read('TRANSPORTS.json');neigh=[36,180,6,30,1,5]
assert len(a['transforms'])==len(b)==len(t['automorphisms'])==48
assert len({(tuple(x['permutation']),tuple(x['signs'])) for x in b})==48
for x,y in zip(a['transforms'],b):
 assert x['permutation']==y['permutation'] and x['signs']==y['signs']
 cols=[[F(z) for z in c] for c in x['columns']]
 assert [[cols[j][i] for j in (1,2)] for i in (1,2)]==[[F(z) for z in r] for r in y['E_unscaled']]
 assert [[cols[j][i] for j in (3,4,5)] for i in (3,4,5)]==y['T']
assert {tuple(e['pair']) for e in l['entries']}==set(itertools.combinations(range(6),2))
for e in l['entries']:
 matches=[]
 for i,x in enumerate(t['automorphisms']):
  dest=sorted(neigh.index(x['site_map'][neigh[j]]) for j in l['representatives'][e['class']])
  if dest==e['pair']:matches.append(i)
 assert e['transport']==min(matches)
for k,es in l['predecessors'].items():
 assert {tuple(e['pair']) for e in es}==set(itertools.combinations(sorted(set(range(6))-set(l['representatives'][k])),2))
 assert all(e in l['entries'] for e in es)
out={'status':'PASS','all48_blocks_exact_adapted_submatrices':True,'all15_transports_smallest_correct_site_map':True,'both_six_predecessor_sets_exact':True,'seconds':time.monotonic()-start,'canonical_helpers_imported':False,'inputs':{n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ['ADAPTED.json','BLOCKS.json','LEDGER.json','TRANSPORTS.json']}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
