import itertools, random, cmath, json
rng=random.Random(8871)
sites=[(x,y,0) for x in range(-2,3) for y in range(-2,3)]
def rnd():return rng.uniform(-1,1)+1j*rng.uniform(-1,1)
fvals={tuple(sorted(p)):rnd() for p in itertools.combinations(sites,2)}
gvals={tuple(sorted(p)):rnd() for p in itertools.combinations(sites,2) if abs(p[0][0]-p[1][0])+abs(p[0][1]-p[1][1])==1}
def f(a,b):
 if a==b or a[2]!=b[2]:return 0j
 return fvals.get(tuple(sorted(((a[0],a[1],0),(b[0],b[1],0)))),0j)
def g(a,b):return gvals.get(tuple(sorted(((a[0],a[1],0),(b[0],b[1],0)))),0j)
def feat(A):
 A=tuple(A)
 if len(A)==2:return f(*A)
 if len(A)!=4:return 0j
 cs=sorted({(x,y) for x,y,z in A});zs={z for x,y,z in A}
 if len(cs)!=2 or len(zs)!=2 or max(zs)-min(zs)!=1:return 0j
 return g((*cs[0],0),(*cs[1],0))
def wave(A):
 A=tuple(A);ans=0j
 for n in [2,4]:
  for B in itertools.combinations(A,n):ans+=feat(B)*feat(set(A)-set(B))
 return ans
def walls(A):return sum(((x,y,z-1) not in A)+((x,y,z+1) not in A) for x,y,z in A)
def neighbors(a):
 x,y,z=a
 for axis in (0,1):
  for s in (-1,1):yield axis,(x+s*(axis==0),y+s*(axis==1),z)
def action(S):
 bonds=set()
 for x,y,z in S:
  for zz in (z-1,z,z+1):
   for ax,b in neighbors((x,y,zz)):bonds.add((ax,tuple(sorted(((x,y,zz),b)))))
 ans=0j
 for ax,edge in bonds:
  I=S.symmetric_difference(edge)
  if walls(I)!=8:continue
  h=-1 if ax==0 else (1 if ((edge[0] in I)==(edge[1] in I)) else -1)
  ans+=h*wave(I)
 return ans
def pairaction(a,b):
 ans=0j
 for i,j in ((a,b),(b,a)):
  for ax,k in neighbors(i):
   if k!=j:ans-=f(k,j)
 if abs(a[0]-b[0])+abs(a[1]-b[1])==1:ans+=2*(-1 if a[1]==b[1] else 1)*g(a,b)
 return ans
def sum_pair_eq(S):
 a,b,c,d=tuple(S)
 return 2*sum(pairaction(i,j)*f(k,l)+f(i,j)*pairaction(k,l) for i,j,k,l in ((a,b,c,d),(a,c,b,d),(a,d,b,c)))
def contact(S):
 ans=0j
 for i in S:
  for ax,j in neighbors(i):
   if j in S:
    k,l=tuple(S-{i,j});ans+=4*f(j,k)*f(j,l)
 return ans
err=0
for _ in range(400):
 S=set(rng.sample(sites,4));err=max(err,abs(action(S)-sum_pair_eq(S)-contact(S)))
# Permanent factor check for arbitrary finite f(0,k), no eigenstate/translation assumptions.
coords=[(x,y) for x in range(-2,3) for y in range(-2,3)]
z=(0,0);d=(1,0);rest=[k for k in coords if k not in (z,d)]
a={k:rnd() for k in rest};ps=[(rng.random()*3,rng.random()*3) for _ in range(4)]
def phase(p,k):return cmath.exp(-1j*(p[0]*k[0]+p[1]*k[1]))
lhs=0j
for k,l in itertools.combinations(rest,2):
 F=sum(__import__('functools').reduce(lambda u,v:u*v,(phase(p,x) for p,x in zip(ps,perm)),1) for perm in itertools.permutations((z,d,k,l)))
 lhs+=a[k]*a[l]*F
rhs=0j
for ia in range(4):
 for ib in range(4):
  if ia==ib:continue
  ic,ie=[i for i in range(4) if i not in (ia,ib)]
  Sc=sum(a[k]*phase(ps[ic],k) for k in rest);Se=sum(a[k]*phase(ps[ie],k) for k in rest)
  G=sum(a[k]**2*phase(ps[ic],k)*phase(ps[ie],k) for k in rest)
  rhs+=phase(ps[ib],d)*(Sc*Se-G)
out={'general_native_identity_cases':400,'general_native_identity_max_error':err,'permanent_factorization_error':abs(lhs-rhs),'ray_amplitudes':'independent complex values for both x/y edges; pair amplitudes arbitrary complex finite support'}
assert err<1e-11 and abs(lhs-rhs)<1e-10
print(json.dumps(out,indent=2))
