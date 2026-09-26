"""Separate author catalog oracle; not an independent scientific review."""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,random,subprocess,sys
HERE=Path(__file__).resolve().parent
EXE=Path(sys.argv[1]).resolve();OUT=HERE/'geometric_growth_validation';OUT.mkdir(exist_ok=True)
def geometry(N):
 xyz=list(product(range(N),repeat=3));index={x:i for i,x in enumerate(xyz)}
 neighbors={i:set() for i in range(N**3)};edges=set()
 for x,i in index.items():
  for axis in range(3):
   y=list(x);y[axis]=(y[axis]+1)%N;j=index[tuple(y)]
   edges.add(tuple(sorted((i,j))));neighbors[i].add(j);neighbors[j].add(i)
 return xyz,index,neighbors,edges
def write_state(path,N,M):
 partners={};ids={}
 for j,(a,b) in enumerate(sorted(M)):partners[a]=b;partners[b]=a;ids[a]=2*j;ids[b]=2*j+1
 path.write_text('N '+str(N)+'\nsite partner identity births_at_site\n'+''.join(f'{i} {partners.get(i,-1)} {ids.get(i,-1)} {int(i in partners)}\n' for i in range(N**3)))
 return partners
def main():
 rows=[];channels=0
 for N in [4,6]:
  xyz,index,neighbors,edges=geometry(N);rng=random.Random(2109211415+N)
  fixtures=[('empty',set())]
  for axis in range(3):
   x=[0,0,0];x[axis]=N-1;fixtures.append((f'wrapped_pair_{axis}',{tuple(sorted((index[tuple(x)],index[(0,0,0)])))}))
  columnar=set()
  for x,u in index.items():
   if x[0]%2==0:
    y=(x[0]+1,x[1],x[2]);columnar.add(tuple(sorted((u,index[y]))))
  fixtures.append(('full_columnar',columnar))
  jam=set()
  for x,y,z in product(range(0,N,2),repeat=3):
   for a,b in [((1,0,0),(1,1,0)),((0,1,0),(0,1,1)),((0,0,1),(1,0,1))]:
    v=tuple(a[i]+(x,y,z)[i] for i in range(3));w=tuple(b[i]+(x,y,z)[i] for i in range(3));jam.add(tuple(sorted((index[v],index[w]))))
  fixtures.append(('old_direction_tag_jam',jam))
  for sample in range(6):
   M=set();used=set();ordered=sorted(edges);rng.shuffle(ordered)
   for a,b in ordered:
    if a not in used and b not in used and rng.random()<.7:M.add((a,b));used|={a,b}
   fixtures.append((f'random_{sample}',M))
  for name,M in fixtures:
   prefix=OUT/f'N{N}_{name}';state=prefix.with_suffix('.state.txt');partner=write_state(state,N,M)
   expected=Counter()
   for a,b in edges:
    if a not in partner and b not in partner:expected[('B',a,b)]+=1
   for pivot,source in partner.items():
    for vacancy in neighbors[pivot]:
     if vacancy not in partner:expected[('S',source,pivot,vacancy)]+=1
   command=[str(EXE),'--catalog',str(N),str(state),str(prefix.with_suffix('.catalog.txt'))]
   proc=subprocess.run(command,text=True,capture_output=True);prefix.with_suffix('.stdout').write_text(proc.stdout);prefix.with_suffix('.stderr').write_text(proc.stderr);assert proc.returncode==0,proc.stderr
   actual=Counter()
   for line in prefix.with_suffix('.catalog.txt').read_text().splitlines():
    fields=line.split();kind=fields[0];values=list(map(int,fields[1:]));values.sort() if kind=='B' else None;actual[(kind,*values)]+=1
   assert actual==expected,(N,name,actual-expected,expected-actual)
   for event,count in expected.items():
    if event[0]=='S':
     _,a,b,c=event;new=dict(partner);del new[a];new[b]=c;new[c]=b
     assert a not in new and new[c]==b and a in neighbors[b] and new[b]==c
   births=sum(n for e,n in actual.items() if e[0]=='B');slides=sum(n for e,n in actual.items() if e[0]=='S')
   if name=='empty':assert births==3*N**3 and slides==0
   if name.startswith('wrapped_pair'):assert births==3*N**3-11 and slides==10
   if name=='full_columnar':assert births==slides==0
   if name=='old_direction_tag_jam':assert births==0 and slides>0
   channels+=sum(actual.values());rows.append({'N':N,'name':name,'pairs':len(M),'birth_channels':births,'slide_channels':slides,'command':command,'state_sha256':hashlib.sha256(state.read_bytes()).hexdigest()})
 result={'scope':'root catalog cross-check with a separate representation, not independent review of stochastic kinetics','fixtures':len(rows),'accepted_channels':channels,'rows':rows,'source_sha256':hashlib.sha256((HERE/'geometric_partner_growth.cpp').read_bytes()).hexdigest(),'binary_sha256':hashlib.sha256(EXE.read_bytes()).hexdigest(),'oracle_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'all_pass':True}
 (OUT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['fixtures','accepted_channels','all_pass','source_sha256','binary_sha256','oracle_sha256']},indent=2))
if __name__=='__main__':main()
