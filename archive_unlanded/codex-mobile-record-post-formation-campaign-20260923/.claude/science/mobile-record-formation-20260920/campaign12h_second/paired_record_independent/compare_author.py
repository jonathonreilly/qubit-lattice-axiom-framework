"""Post-seal exact graph comparison and selective actual mutation controls."""
from pathlib import Path
from itertools import permutations,product
from collections import defaultdict
from contextlib import redirect_stdout,redirect_stderr
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,io,json,traceback
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def rec(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
for r in [pre['source']]+pre['artifacts']:assert rec(Path(r['path']))==r
paths=[ROOT/n for n in ['PAIRED_RECORD_FORMATION_AND_DIMER_GAUSS.md','paired_record_dimer_check.py','PAIRED_RECORD_DIMER_RESULTS.json','PAIRED_RECORD_DIMER_RUN.log','PAIRED_RECORD_CUBE_ABSORPTION.json']]
source=paths[1];raw=source.read_bytes();assert sha(raw)=='65ad8acc7384f25196132b23876f4510347832c4a7f4db548d9c9aead71d2288'
def load():
 ns={'__file__':str(source),'__name__':'reviewed_author_module'};exec(compile(raw,str(source),'exec'),ns);return ns
ns=load();authorstates=ns['matching_states']();own=json.loads((HERE/'CUBE_GRAPH.json').read_text())
vertices=list(map(tuple,own['vertices']));vi={v:i for i,v in enumerate(vertices)}
edge_keys=[tuple(sorted((vertices[a],vertices[b]))) for a,b in own['edges']];ei={e:i for i,e in enumerate(edge_keys)}
M=own['matching_masks'];mi={m:i for i,m in enumerate(M)}
def mask(edges):return sum(1<<ei[tuple(sorted(map(tuple,e)))] for e in edges)
assert set(map(mask,authorstates))==set(M)
expected=[own[k] for k in ['birth_rows','translation_rows','cube_rows']]
expected=[[{int(j):w for j,w in row.items()} for row in family] for family in expected]
actual=[[{} for _ in M] for _ in range(3)]
for m in authorstates:
 i=mi[mask(m)];r=ns['records_from_matching'](m)
 rows=[defaultdict(int) for _ in range(3)]
 for edge in ns['EDGES']:
  if not set(edge)&r.keys():rows[0][mi[mask((*m,edge))]]+=1
 for x,y in m:
  for a in ns['D']:
   if any(ns['add'](z,a) not in ns['CUBESET'] for z in (x,y)):continue
   try:new=ns['translate'](r,x,a)
   except ValueError:continue
   rows[1][mi[mask(ns['bonds'](new))]]+=1
 for axis in range(3):
  try:new=ns['cube_exchange'](r,axis=axis)
  except ValueError:continue
  rows[2][mi[mask(ns['bonds'](new))]]+=1
 for a,row in enumerate(rows):actual[a][i]=dict(row)
assert actual==expected
# Independently recover closed components and symmetry orbits from the sealed graph.
adj=[set(expected[0][i])|set(expected[1][i])|set(expected[2][i]) for i in range(108)];reach=[]
for i in range(108):
 seen={i};todo=[i]
 while todo:
  q=todo.pop()
  for j in adj[q]-seen:seen.add(j);todo.append(j)
 reach.append(seen)
closed=[];done=set()
for i in range(108):
 if i in done:continue
 component=frozenset(j for j in reach[i] if i in reach[j]);done|=component
 if all(adj[j]<=component for j in component):closed.append(component)
categories=own['classes'];families={c:{comp for comp in closed if categories[next(iter(comp))]==c} for c in (7,8,9)}
group=[]
for perm in permutations(range(3)):
 for signs in product((-1,1),repeat=3):
  destv=[tuple(signs[i]*p[perm[i]]+int(signs[i]<0) for i in range(3)) for p in vertices]
  deste=[ei[tuple(sorted((destv[a],destv[b])))] for a,b in own['edges']]
  dest=[mi[sum(1<<deste[e] for e in range(12) if m>>e&1)] for m in M];group.append(dest)
for comps in families.values():
 first=next(iter(comps));orbit={frozenset(dest[i] for i in first) for dest in group};assert orbit==comps
absorption=json.loads(paths[4].read_text());assert absorption['rates']=={'beta':1,'kappa':1,'nu':1}
assert Fraction(absorption['unfilled_absorption_probability'])==Fraction(4,21)
aggregate={7:Fraction(4,21),8:Fraction(13,49),9:Fraction(80,147)}
seen=set();hitting=[]
for row in absorption['closed_classes']:
 i=mi[mask(row['representative_edges'])];comp=next(c for c in closed if i in c)
 assert comp not in seen;seen.add(comp)
 assert len(comp)==row['size'] and M[i].bit_count()==row['dimers']
 cat=categories[i];want=aggregate[cat]/len(families[cat]);assert Fraction(row['empty_start_hitting_probability'])==want
 hitting.append({'category':own['class_names'][cat],'size':len(comp),'probability':str(want)})
assert seen==set(closed)
result=json.loads(paths[2].read_text());log=[json.loads(line) for line in paths[3].read_text().splitlines()]
assert log[:-1]==result['rows'] and log[-1]['all_pass']==result['all_pass']==True
assert log[-1]['groups']==len(result['rows'])==12
assert result['sources_sha256']=={paths[0].name:rec(paths[0])['sha256'],source.name:sha(raw)}
assert log[-1]['sources_sha256']==result['sources_sha256']
# Selective real mutations of helper functions, not just constant anti-controls.
mutations=[]
for case in ['baseline','identity_translation','identity_cube','missing_staggering']:
 module=load();failure=None
 if case=='identity_translation':module['translate']=lambda records,x,a:records.copy()
 if case=='identity_cube':module['cube_exchange']=lambda records,*args,**kwargs:records.copy()
 if case=='missing_staggering':
  original=module['sixB']
  module['sixB']=lambda records,N:{key:module['parity'](key[0])*value for key,value in original(records,N).items()}
 out=io.StringIO();err=io.StringIO()
 with redirect_stdout(out),redirect_stderr(err):
  try:
   cube,swapped=module['histories']();module['fourier_increment'](cube,swapped)
  except (AssertionError,ValueError) as exc:
   failure={'type':type(exc).__name__,'message':str(exc)};traceback.print_exc()
 (HERE/(case.upper()+'.stdout')).write_text(out.getvalue());(HERE/(case.upper()+'.stderr')).write_text(err.getvalue())
 mutations.append({'case':case,'failure':failure,'rows':module['ROWS']})
assert mutations[0]['failure'] is None
assert mutations[1]['failure']=={'type':'ValueError','message':'occupied birth endpoint'}
assert mutations[2]['failure']=={'type':'AssertionError','message':'dense_cube_moves_eight_immutable_records_and_returns'}
assert mutations[3]['failure']=={'type':'AssertionError','message':'exact_staggered_gauss_identity'}
(HERE/'MUTATION_RESULTS.json').write_text(json.dumps({'author_source_sha256':sha(raw),'receipts':mutations},indent=2)+'\n')
output={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':[rec(p) for p in paths],
 'pre_comparison_seal_authenticated':True,'all_108_states_all_three_channel_families_match_exactly':True,
 'closed_class_probabilities_confirmed_via_independent_lumping_and_graph_symmetry':hitting,
 'author_log_and_source_bindings_match':True,'actual_mutations_rejected':[{'case':x['case'],'failure':x['failure']} for x in mutations[1:]],
 'full_author_absorption_inverse_rerun':False,'actionable_findings':[],
 'scope':'Post-seal complete-source comparison plus targeted helper execution. The independent ten-class solve and exact harmonic proof remain distinct from the author 91-state inverse.'}
(HERE/'SOURCE_COMPARISON.json').write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
