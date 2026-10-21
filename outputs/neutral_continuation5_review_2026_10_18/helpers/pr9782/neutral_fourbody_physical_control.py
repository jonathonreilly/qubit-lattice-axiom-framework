import itertools,math,json,random
r=2**-.5; Eb=-3*2**.5

def f(a,b):
 x,y,z=a;X,Y,Z=b
 return ((-1)**min(y,Y))*r**abs(X-x) if z==Z and abs(Y-y)==1 else 0.
def feature(A):
 A=sorted(A)
 if len(A)==2:return f(*A)
 if len(A)!=4:return 0.
 cols={(x,y) for x,y,z in A};zs={z for x,y,z in A}
 if len(cols)!=2 or len(zs)!=2 or max(zs)-min(zs)!=1:return 0.
 (x,y),(X,Y)=sorted(cols)
 if x!=X or abs(y-Y)!=1:return 0.
 return -r*f((x,y,min(zs)),(X,Y,min(zs)))
def wave(A):
 A=tuple(A);out=0.
 for n in [2,4]:
  for sub in itertools.combinations(A,n):
   B=set(A)-set(sub)
   out+=feature(sub)*feature(B)
 return out

def walls(A):
 return sum(((x,y,z-1) not in A)+((x,y,z+1) not in A) for x,y,z in A)
def direct(S):
 # Enumerate every possible bond with nonzero 4/6-spin input wave amplitude.
 # Candidate six-spin inputs add a pair one layer above/below output;
 # four-spin inputs move one output spin by a transverse edge.
 bonds=set()
 for x,y,z in S:
  for zz in [z-1,z,z+1]:
   for axis in [0,1]:
    for s in [-1,1]:
     a=(x,y,zz);b=(x+s*(axis==0),y+s*(axis==1),zz)
     bonds.add((axis,tuple(sorted((a,b)))))
 val=0.;parts={4:0.,6:0.,2:0.};active=[]
 for axis,edge in bonds:
  I=S.symmetric_difference(edge)
  if walls(I)!=8:continue
  w=wave(I)
  if not w:continue
  # <S|-XX|I>=-1; <-YY>=+1 for equal bits, -1 for mixed.
  h=-1 if axis==0 else (1 if ((edge[0] in I)==(edge[1] in I)) else -1)
  val+=h*w;parts[len(I)]+=h*w
  active.append((axis,edge,len(I),h*w))
 return val-2*Eb*wave(S),parts,active

def target(S):
 out=0.
 for i in S:
  for j in S-{i}:
   if i[2]==j[2] and abs(i[0]-j[0])+abs(i[1]-j[1])==1:
    k,l=tuple(S-{i,j});out+=4*f(j,k)*f(j,l)
 return out
sites=[(x,y,0) for x in range(-2,3) for y in range(-1,3)]
rng=random.Random(712)
cases=[set(t) for t in itertools.combinations(sites[:10],4)]
cases += [set(rng.sample(sites,4)) for _ in range(500)]
err=0.;example=None;nonzero=0
for S in cases:
 v,parts,active=direct(S);w=target(S);err=max(err,abs(v-w))
 if abs(w)>1e-10:nonzero+=1
 if parts[6] and example is None:example={'S':sorted(S),'direct_residual':v,'target':w,'parts':parts,'wave':wave(S),'active':active}
out={'cases':len(cases),'max_error':err,'nonzero_residual_cases':nonzero,'six_spin_example':example}
print(json.dumps(out,indent=2));assert err<1e-11
