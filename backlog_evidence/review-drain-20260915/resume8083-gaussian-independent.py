# Finite synthetic determinant check via direct Leibniz series and Fock powers.
# No native inputs, producer code, diagonalization, oracle, or full event replay.
import signal,time,resource,json,itertools,math
from fractions import Fraction as F
signal.alarm(30);start=time.monotonic()
# Rational complex as Python complex-free pairs.
def z(x=0,y=0):return(F(x),F(y))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sc(a,b):return(a[0]*b,a[1]*b)
Z=z();O=z(1);ii=z(0,1)
def eye(n):return [[O if i==j else Z for j in range(n)]for i in range(n)]
def ma(a,b):return [[add(x,y)for x,y in zip(r,s)]for r,s in zip(a,b)]
def ms(a,c):return [[mul(x,c)for x in row]for row in a]
def mm(a,b):return [[sumz(mul(x,y)for x,y in zip(row,col))for col in zip(*b)]for row in a]
def sumz(xs):
 out=Z
 for x in xs:out=add(out,x)
 return out
def kron(a,b):return [[mul(a[i][j],b[k][l])for j in range(len(a))for l in range(len(b))]for i in range(len(a))for k in range(len(b))]
X=[[Z,O],[O,Z]];Y=[[Z,neg(ii)],[ii,Z]];ZZ=[[O,Z],[Z,z(-1)]];I=eye(2)
g=[kron(X,I),kron(Y,I),kron(ZZ,X),kron(ZZ,Y)]
N=6;checks=0
for freq in [(F(1),F(2)),(F(3,2),F(1,2))]:
 h=[[Z]*4 for _ in range(4)]
 for k,w in enumerate(freq):h[2*k][2*k+1]=z(0,w);h[2*k+1][2*k]=z(0,-w)
 P=eye(4)
 for k,w in enumerate(freq):
  for a in range(2):
   for b in range(2):P[2*k+a][2*k+b]=sc(add(O if a==b else Z,sc(h[2*k+a][2*k+b],-1/w)),F(1,2))
 for d in [(0,0,1,1),(0,1,1,0)]:
  V=[[Z]*4 for _ in range(4)]
  for j in range(4):V[0][j]=add(V[0][j],z(0,2*d[j]));V[j][0]=add(V[j][0],z(0,-2*d[j]))
  H=ma(ms(mm(g[0],g[1]),z(0,freq[0]/2)),ms(mm(g[2],g[3]),z(0,freq[1]/2)))
  H=ma(H,ms(eye(4),z(sum(freq)/2)))
  B=ms(mm(g[0],sum_m([ms(g[j],z(d[j]))for j in range(4)])) ,ii) if False else None
  gd=[[Z]*4 for _ in range(4)]
  for j in range(4):gd=ma(gd,ms(g[j],z(d[j])))
  D=ma(H,ms(mm(g[0],gd),ii))
  # Direct many-body powers for Z, no logarithm recurrence.
  power=eye(4);zz=[]
  for n in range(N+1):zz.append(sc(power[0][0],F((-1)**n,math.factorial(n))));power=mm(power,D)
  target=[sumz(mul(zz[k],zz[n-k])for k in range(n+1))for n in range(N+1)]
  def expseries(M,sgn):
   out=[];p=eye(4)
   for n in range(N+1):out.append(ms(p,z(F(sgn**n,math.factorial(n)))));p=mm(p,M)
   return out
  e=expseries(h,1);f=expseries(ma(h,V),-1);U=[]
  for n in range(N+1):
   a=[[Z]*4 for _ in range(4)]
   for k in range(n+1):a=ma(a,mm(e[k],f[n-k]))
   U.append(eye(4)if n==0 else mm(P,a))
  def pm(a,b):return[sumz(mul(a[k],b[n-k])for k in range(n+1))for n in range(N+1)]
  det=[Z]*(N+1)
  for perm in itertools.permutations(range(4)):
   inv=sum(perm[i]>perm[j]for i in range(4)for j in range(i+1,4));v=[O]+[Z]*N
   for i,j in enumerate(perm):v=pm(v,[U[n][i][j]for n in range(N+1)])
   det=[add(x,sc(y,(-1)**inv))for x,y in zip(det,v)]
  assert det==target;checks+=N+1
  assert zz[2]!=Z and det[2]!=zz[2];checks+=1 # no-half-log countercontrol
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<384*1024**2
print(json.dumps({'status':'PASS_FINITE_SYNTHETIC_ONLY','exact_coefficient_checks':checks,'order':N,'fock_dimension':4,'seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'native_runs':0,'producer_imports':0}))
