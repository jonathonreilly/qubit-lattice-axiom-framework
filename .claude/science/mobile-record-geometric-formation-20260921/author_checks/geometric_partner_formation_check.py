"""Exact author controls for geometric partners; no wave/quantum-instrument test."""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import Counter,deque
from fractions import Fraction as F
import hashlib,json,random
import sympy as sp

HERE=Path(__file__).resolve().parent;OUT=HERE/'geometric_partner_checks';OUT.mkdir(exist_ok=True)
ROWS=[]
def check(name,ok,**data):
 row={'name':name,'pass':bool(ok),**data};ROWS.append(row);print(json.dumps(row),flush=True);assert ok,name
def edge(a,b):return tuple(sorted((a,b)))
def graph(shape,periodic=False):
 sites=list(product(*(range(n) for n in shape)));index={x:i for i,x in enumerate(sites)};edges=set();faces=set()
 for x in sites:
  for i in range(3):
   y=list(x);y[i]+=1
   if y[i]>=shape[i]:
    if not periodic:continue
    y[i]=0
   edges.add(edge(index[x],index[tuple(y)]))
  for i,j in combinations(range(3),2):
   corners=[]
   for di,dj in [(0,0),(1,0),(1,1),(0,1)]:
    y=list(x);y[i]+=di;y[j]+=dj
    if any(y[k]>=shape[k] for k in range(3)) and not periodic:break
    y=tuple(y[k]%shape[k] for k in range(3));corners.append(index[y])
   if len(corners)==4:faces.add(tuple(corners))
 neighbors=[set() for x in sites]
 for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
 axis=next(i for i,n in enumerate(shape) if n%2==0)
 perfect=set()
 for u,x in enumerate(sites):
  if x[axis]%2==0:
   y=list(x);y[axis]+=1;perfect.add(edge(u,index[tuple(y)]))
 return {'sites':sites,'index':index,'edges':sorted(edges),'neighbors':neighbors,'faces':sorted(faces),'perfect':frozenset(perfect)}
def partners(M):return {u:v for a,b in M for u,v in [(a,b),(b,a)]}
def valid(M,G):
 p=partners(M)
 return len(p)==2*len(M) and all(e in G['edge_set'] for e in M)
def prepare(G):G['edge_set']=set(G['edges']);return G
def enumerate_matchings(G):
 def visit(free,M):
  if not free:yield frozenset(M);return
  a=min(free);remaining=free-{a}
  yield from visit(remaining,M)
  for b in sorted(remaining&G['neighbors'][a]):yield from visit(remaining-{b},M+[edge(a,b)])
 return list(visit(set(range(len(G['sites']))),[]))
def channels(M,G,beta=1,kappa=1,nu=1):
 p=partners(M);result=[]
 for a,b in G['edges']:
  if a not in p and b not in p and beta:result.append((M|{(a,b)},beta,('birth',a,b)))
 if kappa:
  for v1,v0 in sorted(p.items()):
   for v2 in sorted(G['neighbors'][v1]):
    if v2 not in p:result.append(((M-{edge(v0,v1)})|{edge(v1,v2)},kappa,('slide',v0,v1,v2)))
 if nu:
  for face in G['faces']:
   a,b,c,d=face
   first={edge(a,b),edge(c,d)};second={edge(a,d),edge(b,c)}
   for old,new in [(first,second),(second,first)]:
    if old<=M:
     for direction in [-1,1]:result.append(((M-old)|new,nu,('flip',face,direction)))
 return result
def augment(M,G):
 assert valid(M,G) and len(M)<len(G['sites'])//2
 p=partners(M);vac=next(u for u in range(len(G['sites'])) if u not in p)
 diff=M^G['perfect'];adj={u:[] for u in range(len(G['sites']))}
 for a,b in diff:adj[a].append(b);adj[b].append(a)
 path=[vac]
 while True:
  nxt=[v for v in adj[path[-1]] if len(path)==1 or v!=path[-2]]
  if not nxt:break
  assert len(nxt)==1 and nxt[0] not in path;path.append(nxt[0])
 assert len(path)%2==0 and path[-1] not in p
 current=M;events=[]
 for j in range(0,len(path)-2,2):
  v2,v1,v0=path[j:j+3]
  assert edge(v0,v1) in current and v2 not in partners(current)
  current=(current-{edge(v0,v1)})|{edge(v1,v2)};events.append(('slide',v0,v1,v2));assert valid(current,G)
 a,b=path[-2:];assert a not in partners(current) and b not in partners(current)
 current=current|{edge(a,b)};events.append(('birth',a,b));assert valid(current,G) and len(current)==len(M)+1
 assert len(events)<=len(G['sites'])//2
 return frozenset(current),events
def key(j):
 t=F(1,j+2);return (2*t/(1+t*t),F(0),(1-t*t)/(1+t*t))
def negate(n):return tuple(-v for v in n)
def records_from(M,G):
 state={};births=Counter()
 for j,(a,b) in enumerate(sorted(M)):
  state[a]=(2*j,key(j));state[b]=(2*j+1,negate(key(j)));births[a]+=1;births[b]+=1
 return state,births,len(M)
def read_matching(state,G):
 content={n:u for u,(_,n) in state.items()};assert len(content)==len(state)
 M=set()
 for u,(rid,n) in state.items():
  assert sum(v*v for v in n)==1
  v=content[negate(n)];assert v in G['neighbors'][u];M.add(edge(u,v))
 assert len(M)*2==len(state);return frozenset(M)
def apply_record_event(state,event,G,next_key,births):
 before={rid:n for rid,n in state.values()};oldpos={rid:x for x,(rid,n) in state.items()}
 if event[0]=='slide':
  _,a,b,c=event;assert c not in state and state[a][1]==negate(state[b][1])
  first=state.pop(a);second=state.pop(b);state[b]=first;state[c]=second
 elif event[0]=='birth':
  _,a,b=event;assert a not in state and b not in state
  state[a]=(2*next_key,key(next_key));state[b]=(2*next_key+1,negate(key(next_key)));next_key+=1;births[a]+=1;births[b]+=1
 elif event[0]=='flip':
  _,face,direction=event;old={u:state.pop(u) for u in face}
  for j,u in enumerate(face):state[face[(j+direction)%4]]=old[u]
 else:raise ValueError(event)
 after={rid:n for rid,n in state.values()};assert all(after[rid]==n for rid,n in before.items())
 for u,(rid,n) in state.items():
  if rid in oldpos:assert u==oldpos[rid] or u in G['neighbors'][oldpos[rid]]
 read_matching(state,G);return next_key

def birth_controls():
 eps=F(1,2);dirs=[tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in [-1,1]]
 dot=lambda a,b:sum(x*y for x,y in zip(a,b));n=(F(2,3),F(1,3),F(2,3));cases=0
 rotation_maps=[]
 for perm in permutations(range(3)):
  for signs in product([-1,1],repeat=3):
   R=sp.zeros(3)
   for i in range(3):R[i,perm[i]]=signs[i]
   if R.det()==1:rotation_maps.append((perm,signs))
 for mask in range(64):
  D=[d for j,d in enumerate(dirs) if mask>>j&1];r=len(D);m=tuple(sum(d[i] for d in D) for i in range(3))
  def density(v):return F(1) if not r else 1+eps*dot(v,m)/r
  assert sum(density(v) for v in dirs)/6==1 and all(density(v)>0 for v in dirs)
  mean=tuple(sum(v[i]*density(v) for v in dirs)/6 for i in range(3))
  assert mean==(tuple(eps*m[i]/(3*r) for i in range(3)) if r else (0,0,0))
  for perm,signs in rotation_maps:
   rot=lambda v:tuple(signs[i]*v[perm[i]] for i in range(3))
   nn=rot(n);mm=rot(m);assert dot(nn,mm)==dot(n,m);cases+=1
 for d in dirs:assert 1+eps*dot(n,d)==1+eps*dot(negate(n),negate(d))
 check('all_neighbor_masks_normalization_variation_and_proper_covariance',True,masks=64,rotation_cases=cases,single_neighbor_mean=['1/6','0','0'],six_neighbor_mean=[0,0,0])

def cube_controls():
 G=prepare(graph((2,2,2)));states=enumerate_matchings(G);I={M:j for j,M in enumerate(states)};census=Counter(map(len,states));assert len(states)==108
 all_events=0;longest=0
 for M in states:
  if len(M)<4:
   new,events=augment(M,G);longest=max(longest,len(events));assert len(new)==len(M)+1
  for target,rate,event in channels(M,G):
   all_events+=1;assert target in I and valid(target,G)
   if event[0]!='birth':
    reverse=sum(r for t,r,e in channels(target,G,0,1,1) if t==M)
    forward=sum(r for t,r,e in channels(M,G,0,1,1) if t==target);assert reverse==forward
 # Complete geometry channel certificate, keeping the two flip senses.
 certificate=[{'matching':sorted(M),'channels':[{'target':I[t],'rate':r,'event':e} for t,r,e in channels(M,G)]} for M in states]
 (OUT/'CUBE_CHANNELS.json').write_text(json.dumps(certificate,indent=2)+'\n')
 transforms=[]
 for perm in permutations(range(3)):
  for flips in product([0,1],repeat=3):transforms.append({u:G['index'][tuple(x[perm[i]]^flips[i] for i in range(3))] for u,x in enumerate(G['sites'])})
 def representative(M):return min(tuple(sorted(edge(T[a],T[b]) for a,b in M)) for T in transforms)
 rep={M:representative(M) for M in states};orbits=sorted(set(rep.values()));OI={M:i for i,M in enumerate(orbits)}
 lump_results=[]
 for nu in [0,1]:
  Q=sp.zeros(len(orbits));known={}
  for M in states:
   row=[0]*len(orbits);i=OI[rep[M]]
   for target,rate,event in channels(M,G,1,1,nu):
    j=OI[rep[target]];row[j]+=rate;row[i]-=rate
   if i in known:assert known[i]==row
   else:known[i]=row
  for i,row in known.items():
   for j,value in enumerate(row):Q[i,j]=value
  transient=[i for i,M in enumerate(orbits) if len(M)<4];full=[i for i,M in enumerate(orbits) if len(M)==4]
  A=-Q.extract(transient,transient);times=A.inv()*sp.ones(len(transient),1);assert all(t>0 for t in times)
  rhs=sp.Matrix([sum(Q[i,j] for j in full) for i in transient]);hit=A.inv()*rhs;assert hit==sp.ones(len(transient),1)
  empty=transient.index(OI[()]);lump_results.append({'nu':nu,'lumped_states':len(orbits),'transient_lumps':len(transient),'expected_empty_filling_time':str(times[empty]),'full_hit_probability':'1'})
 # A deposition-only jam remains a necessary control on kappa>0.
 jam=frozenset(edge(G['index'][a],G['index'][b]) for a,b in [((1,0,0),(1,1,0)),((0,1,0),(0,1,1)),((0,0,1),(1,0,1))])
 assert len(channels(jam,G,1,0,1))==0 and any(e[0]=='slide' for t,r,e in channels(jam,G))
 # The nine complete matchings communicate under the supplied flips on this cube only.
 fulls={M for M in states if len(M)==4};seen={next(iter(fulls))};queue=deque(seen)
 while queue:
  M=queue.popleft()
  for t,r,e in channels(M,G,0,0,1):
   if t not in seen:seen.add(t);queue.append(t)
 assert seen==fulls and len(fulls)==9
 check('complete_cube_graph_augmentation_and_exact_absorption',True,states=len(states),count_census=dict(sorted(census.items())),channels=all_events,longest_augmentation=longest,exact_lumped_results=lump_results,full_flip_component=9,deposition_only_jam_retained=True)
 return G,states

def larger_geometry_and_identity_controls():
 G12=prepare(graph((3,2,2)));states=enumerate_matchings(G12);steps=0
 for M in states:
  if 2*len(M)<12:
   target,events=augment(M,G12);steps+=len(events)
 check('exhaustive_twelve_vertex_augmentations',True,states=len(states),nonfull=sum(len(M)<6 for M in states),total_certified_events=steps)
 results=[]
 for N in [4,6,8]:
  G=prepare(graph((N,N,N),True));V=N**3
  for sample in range(6):
   rng=random.Random(2109211400+100*N+sample);candidate=list(G['edges']);rng.shuffle(candidate);M=set();used=set()
   for a,b in candidate:
    if a not in used and b not in used and rng.random()<.8:M.add((a,b));used|={a,b}
   M=frozenset(M);initial=len(M);state,births,next_key=records_from(M,G);history=[]
   while len(M)<V//2:
    target,events=augment(M,G)
    for e in events:next_key=apply_record_event(state,e,G,next_key,births);history.append(e)
    assert read_matching(state,G)==target;M=target
   # Exact staggered Gauss check on the actual final matching.
   ni={x:[0,0,0] for x in G['sites']}
   for x in G['sites']:
    u=G['index'][x]
    for i in range(3):
     y=list(x);y[i]=(y[i]+1)%N;ni[x][i]=int(edge(u,G['index'][tuple(y)]) in M)
   for x in G['sites']:
    sigma=(-1)**sum(x);div=F(0)
    for i in range(3):
     y=list(x);y[i]=(y[i]-1)%N;y=tuple(y)
     div+=sigma*(ni[x][i]-F(1,6))-((-1)**sum(y))*(ni[y][i]-F(1,6))
    assert div==0
   results.append({'N':N,'sample':sample,'initial_pairs':initial,'births':V//2-initial,'events':len(history),'max_site_births_including_initial':max(births.values())})
 check('periodic_augmentation_with_exact_antipodal_contents_and_identities',True,cases=len(results),rows=results)
 # A controlled supported history records actual site reuse and an orientation turn.
 G=prepare(graph((6,6,6),True));idx=G['index'];M=frozenset({edge(idx[(0,0,0)],idx[(1,0,0)])});state,births,j=records_from(M,G)
 events=[('slide',idx[(0,0,0)],idx[(1,0,0)],idx[(2,0,0)]),('birth',idx[(5,0,0)],idx[(0,0,0)]),('slide',idx[(1,0,0)],idx[(2,0,0)],idx[(2,1,0)])]
 for e in events:j=apply_record_event(state,e,G,j,births)
 assert births[idx[(0,0,0)]]==2 and len(state)==4
 # Both plaquette senses preserve identities and invert at the content level.
 face=next(iter(G['faces']));a,b,c,d=face;M=frozenset({edge(a,b),edge(c,d)})
 for direction in [-1,1]:
  state,births,j=records_from(M,G);original=dict(state)
  j=apply_record_event(state,('flip',face,direction),G,j,births)
  assert read_matching(state,G)==frozenset({edge(a,d),edge(b,c)})
  j=apply_record_event(state,('flip',face,-direction),G,j,births);assert state==original
 check('site_reformation_turn_and_both_reversible_plaquette_senses',True,site_zero_births=2,original_contents_preserved=True)

def main():
 birth_controls();cube_controls();larger_geometry_and_identity_controls()
 sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'GEOMETRIC_PARTNER_RECORD_FORMATION.md']}
 result={'status':'author mathematical controls; independent review pending; no phase, wave or quantum-operation conclusion','all_pass':all(r['pass'] for r in ROWS),'rows':ROWS,'sources_sha256':sources}
 (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'groups':len(ROWS),'all_pass':result['all_pass'],'sources_sha256':sources},indent=2))
if __name__=='__main__':main()
