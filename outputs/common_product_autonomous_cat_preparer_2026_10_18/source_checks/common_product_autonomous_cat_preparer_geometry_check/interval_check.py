from pathlib import Path
import json,hashlib,itertools,collections
P=Path(__file__).resolve().parent;S=P.parent/'common_product_autonomous_cat_preparer_geometry/COORDINATES.json'
assert hashlib.sha256(S.read_bytes()).hexdigest()=='f8b3c4579e82abd999ebacd403b0fd040d101d37b8f43301c287ff247bcaecc5'
d=json.loads(S.read_text());heads={k:tuple(v) for k,v in d['module_heads'].items()};targets={k:tuple(v) for k,v in d['targets'].items()};ports={k:tuple(v) for k,v in d['ports'].items()}
assert len(set(heads.values())|set(targets.values()))==208==len(heads)+len(targets)
assert all(heads[k]==v for k,v in ports.items())
# Recover literal writer coordinates by inverse isometry; no path generation/BFS.
a0=[(1,0,0),(2,0,0),(2,1,0),(1,1,0)]+[(1,y,0) for y in range(2,9)]
a1=[(-1,y,0) for y in range(9)]+[(-1,8,1),(0,8,1)]
for label,shift in [('w11',0),('w10',100),('w20',200),('w21',300),('w30',400),('w31',500),('w40',600),('w41',700)]:
 def inverse(p):return (p[2],p[1],p[0]) if label=='w11' else (p[0]-shift,p[1],p[2])
 for a,path in enumerate([a0,a1]):assert [inverse(heads[f'{label}.a{a}.{i}']) for i in range(11)]==path
 assert inverse(ports[label+'.in'])==(0,8,0) and inverse(ports[label+'.out'])==(1,8,1)
expected=[('split.O0','w10.in'),('split.O1','w11.in'),('w10.out','w20.in'),('w11.out','w21.in'),('w20.out','w30.in'),('w21.out','w31.in'),('w30.out','w40.in'),('w31.out','w41.in'),('w40.out','core.I0'),('w41.out','core.I1')]
segments=[];lengths=[]
def box(a,b):return tuple((min(x,y),max(x,y)) for x,y in zip(a,b))
def in_box(p,b):return all(lo<=x<=hi for x,(lo,hi) in zip(p,b))
for ci,c in enumerate(d['cables']):
 assert (c['start'],c['end'])==expected[ci]
 pts=list(map(tuple,c['axis_aligned_corners']));assert pts[0]==ports[c['start']] and pts[-1]==ports[c['end']]
 length=0
 for si,(a,b) in enumerate(zip(pts,pts[1:])):
  assert sum(x!=y for x,y in zip(a,b))==1
  length+=sum(abs(x-y) for x,y in zip(a,b));bb=box(a,b)
  for p in list(heads.values())+list(targets.values()):
   if in_box(p,bb):assert (si==0 and p==pts[0]) or (si==len(pts)-2 and p==pts[-1]),(ci,si,p)
  segments.append((ci,si,a,b,bb))
 assert length==c['edges'];lengths.append(length)
# Closed boxes for axis-aligned segments give their complete exact intersection.
for s,t in itertools.combinations(segments,2):
 inter=[(max(x[0],y[0]),min(x[1],y[1])) for x,y in zip(s[4],t[4])]
 if all(lo<=hi for lo,hi in inter):
  assert s[0]==t[0] and t[1]==s[1]+1,(s[:2],t[:2],inter)
  assert all(lo==hi for lo,hi in inter)
  assert tuple(lo for lo,hi in inter)==s[3]==t[2]
rayxy=set()
for name in d['external_positive_z_rays']:
 o=ports[name];assert o[:2] not in rayxy;rayxy.add(o[:2])
 for p in list(heads.values())+list(targets.values()):assert p[:2]!=o[:2] or p[2]<=o[2]
 for _,_,a,b,bb in segments:
  if bb[0][0]<=o[0]<=bb[0][1] and bb[1][0]<=o[1]<=bb[1][1]:assert bb[2][1]<=o[2]
assert all(lengths[i]==lengths[i+1] for i in range(0,10,2))
# Local graph degree and all contacts; ordinary cable interiors each have degree two.
adj=collections.defaultdict(set);edgekeys=set();kinds=collections.Counter()
for aa,bb,k in d['module_and_external_first_edges']:
 a,b=tuple(aa),tuple(bb);assert sum(abs(x-y) for x,y in zip(a,b))==1
 key=tuple(sorted((a,b)));assert key not in edgekeys;edgekeys.add(key);adj[a].add(b);adj[b].add(a);kinds[k]+=1
for c in d['cables']:
 for k in ['start','end']:adj[ports[c[k]]].add(('cable',c['gap'],c['branch'],k))
assert max(map(len,adj.values()))==6
assert adj[(0,0,0)]=={(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)}
assert kinds==dict(writer_arm=160,writer_junction=32,record_contact=8,core_hop=8,program_contact=4,splitter=4,external_first_edge=4)
qubits=208+sum(x-1 for x in lengths);blocks=304+sum(lengths)
assert qubits==604496 and blocks==604602 and sum(lengths[::2])+90==302239
r=dict(status='passed',method='Exact integer segment intersections, no author path expansion or BFS replay',coordinate_sha256=hashlib.sha256(S.read_bytes()).hexdigest(),segments=len(segments),paired_lengths=lengths[::2],finite_qubits=qubits,finite_blocks=blocks,phase_power=302239,scope='Geometry, isometry coordinates, abstract wiring and counts only; no dynamics, coefficients, finite preparation or receiving handoff check')
(P/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
