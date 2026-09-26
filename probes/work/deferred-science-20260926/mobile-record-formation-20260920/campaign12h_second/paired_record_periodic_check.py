"""Exact support checks for the original periodic jam and its new local escape."""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
HERE=Path(__file__).resolve().parent
AX=((1,0,0),(0,1,0),(0,0,1));D=tuple(tuple(s*v for v in e) for e in AX for s in (-1,1))
BITS=tuple(product((0,1),repeat=3));ROWS=[]
def step(x,d,N):return tuple((a+b)%N for a,b in zip(x,d))
def opposite(d):return tuple(-x for x in d)
def check(name,ok,**data):
 row={'name':name,'pass':bool(ok),**data};ROWS.append(row);print(json.dumps(row));assert ok,name

def valid(r,N):
 return len({i for i,d in r.values()})==len(r) and all(d in D and r.get(step(x,d,N),(None,None))[1]==opposite(d) for x,(i,d) in r.items())
def birth(r,x,d,N):
 y=step(x,d,N);assert x not in r and y not in r
 out=r.copy();i=max((a for a,d in r.values()),default=-1)+1;out[x]=(i,d);out[y]=(i+1,opposite(d));return out
def pairs(r,N):return sorted({tuple(sorted((x,step(x,d,N)))) for x,(i,d) in r.items()})
def contents(r):return dict(r.values())
def periodic_jam(N):
 r={}
 for base in product(range(0,N,2),repeat=3):
  for x,d in [((1,0,0),AX[1]),((0,1,0),AX[2]),((0,0,1),AX[0])]:r=birth(r,step(base,x,N),d,N)
 return r

def original_channels(r,N):
 births=[];translations=[];cubes=[]
 for x in product(range(N),repeat=3):
  for e in AX:
   y=step(x,e,N)
   if x not in r and y not in r:births.append((x,y))
 for pair in pairs(r,N):
  old=set(pair)
  for a in D:
   new={step(x,a,N) for x in pair}
   if not((new-old)&r.keys()):translations.append((pair,a))
 for base in product(range(N),repeat=3):
  cube={b:step(base,b,N) for b in BITS}
  if any(x not in r for x in cube.values()):continue
  for axis in range(3):
   p,q=[j for j in range(3) if j!=axis]
   def face_aligned(face,j):
    return all(r[x][1]==tuple((1-2*b[j]) if k==j else 0 for k in range(3)) for b,x in cube.items() if b[axis]==face)
   if (face_aligned(0,p) and face_aligned(1,q)) or (face_aligned(0,q) and face_aligned(1,p)):cubes.append((base,axis))
 return {'births':births,'translations':translations,'full_cube_exchanges':cubes}

def parallel_swaps(r,edges,N):
 old=r.copy();out=r.copy();support=[x for e in edges for x in e]
 assert len(support)==len(set(support))
 for x,y in edges:
  assert y in {step(x,d,N) for d in D}
  out.pop(x,None);out.pop(y,None)
  if x in old:out[y]=old[x]
  if y in old:out[x]=old[y]
 if not valid(out,N):raise ValueError('reciprocal relation violated')
 return out

def gauss(r,N):
 B={}
 for x in product(range(N),repeat=3):
  sign=1 if sum(x)%2==0 else -1
  for i,e in enumerate(AX):
   n=int(x in r and r[x][1]==e)
   B[x,i]=sign*(6*n-1)
 for x in product(range(N),repeat=3):
  div=sum(B[x,i]-B[step(x,opposite(e),N),i] for i,e in enumerate(AX))
  if div!=6*((-1)**sum(x))*(int(x in r)-1):return False
 return True

def history(N):
 r=periodic_jam(N);ch=original_channels(r,N)
 check('periodic_original_process_has_zero_exits',valid(r,N) and len(r)==3*N**3//4 and all(not rows for rows in ch.values()),side=N,records=len(r),vacancies=N**3-len(r),enabled_channels={k:len(v) for k,v in ch.items()},direction_census={str(d):n for d,n in Counter(d for i,d in r.values()).items()})
 edges=[((0,0,0),(0,1,0)),((0,0,1),(0,1,1)),((1,0,1),(1,1,1))]
 moved=parallel_swaps(r,edges,N);inverse=parallel_swaps(moved,edges,N)
 oldpos={i:x for x,(i,d) in r.items()};newpos={i:x for x,(i,d) in moved.items()};moving=[i for i in oldpos if oldpos[i]!=newpos[i]]
 assert len(moving)==4 and all(newpos[i] in {step(oldpos[i],d,N) for d in D} for i in moving)
 assert contents(r)==contents(moved) and inverse==r and moved!=r
 new=birth(moved,(0,1,0),AX[1],N)
 assert valid(new,N) and len(new)==len(r)+2
 assert all(contents(new)[i]==d for i,d in contents(r).items())
 assert all(gauss(s,N) for s in (r,moved,new))
 check('four_record_local_escape_and_rebirth',True,side=N,moved_records=moving,birth_edge=[[0,1,0],[0,2,0]],record_counts=[len(r),len(moved),len(new)],gauss_identity=True)
 # Save an actual reconstructible witness, not only aggregate PASSs.
 return {'side':N,'base_pattern_edges':[[[1,0,0],[1,1,0]],[[0,1,0],[0,1,1]],[[0,0,1],[1,0,1]]],'swap_edges':edges,'birth_edge':[[0,1,0],[0,2,0]],'moved_id_displacements':[[i,oldpos[i],newpos[i]] for i in moving]}

def cube_cut_census():
 vertices=set(BITS);all_matches=[]
 def enum(free,matching):
  if not free:all_matches.append(matching);return
  x=min(free);enum(free-{x},matching)
  for y in free-{x}:
   if sum(abs(a-b) for a,b in zip(x,y))==1:enum(free-{x,y},matching+[(x,y)])
 enum(vertices,[]);one_each=[]
 for matching in all_matches:
  counts=Counter(next(i for i in range(3) if x[i]!=y[i]) for x,y in matching)
  if counts!=Counter({0:1,1:1,2:1}):continue
  vacant=vertices-{z for pair in matching for z in pair};a,b=sorted(vacant)
  assert len(vacant)==2 and all(a[i]!=b[i] for i in range(3));one_each.append(matching)
 check('every_cube_matching_with_one_dimer_per_axis_has_opposite_vacancies',len(all_matches)==108 and len(one_each)==8,total_matchings=len(all_matches),one_each_matchings=len(one_each))

def main():
 witnesses=[history(N) for N in (4,6,8)];cube_cut_census()
 source={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),HERE/'PAIRED_RECORD_PERIODIC_JAM_AND_ESCAPE.md']}
 result={'scope':'Author exact support controls; no typical density, phase, wave or general accessibility claim.','sources_sha256':source,'rows':ROWS,'witnesses':witnesses}
 (HERE/'PAIRED_RECORD_PERIODIC_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'groups':len(ROWS),'all_pass':all(r['pass'] for r in ROWS),'sources_sha256':source}))
if __name__=='__main__':main()
