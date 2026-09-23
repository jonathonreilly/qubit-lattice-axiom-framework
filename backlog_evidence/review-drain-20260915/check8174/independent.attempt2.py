import resource,signal,json,time
from fractions import Fraction as Q
from itertools import product
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_DATA,(512*1024**2,512*1024**2));signal.alarm(45)
t0=time.monotonic()
def dissent(triple,p,q,r):
 w=[]
 for a in range(6):
  val=Q(1)
  for b in triple:val*=p if a==b else q if a//2==b//2 else r
  w.append(val)
 return sum(w[1:])/sum(w)
def devs(p,q,r):return [dissent(t,Q(p),Q(q),Q(r)) for t in [(0,0,0),(0,0,1),(0,0,2)]]
small=devs(Q(1,10),1,1);assert small[0]>max(small[1:])
print('small_p_counterexample',*[str(x) for x in small])
certs=[((4165,1,2),Q(99,1000),[Q(56694252249173,500000000000),Q(3279872914431,1000000000000),Q(168429466648591,1000000000000)]),((2085,1,1),Q(49,500),[Q(88632394933177,1000000000000),Q(3254100818939,1000000000000),Q(131311435970231,1000000000000)]),((8330,2,4),Q(99,1000),[Q(56694252249173,500000000000),Q(3279872914431,1000000000000),Q(168429466648591,1000000000000)]),((6247,1,3),Q(99,1000),[Q(24445325573453,250000000000),Q(3264868815393,1000000000000),Q(9064364177089,62500000000)])]
for args,t,(D,U,F) in certs:
 e1,*rest=devs(*args);e2=max(rest);x=t+e2/t**2;y=e1/t**3
 # Factor via complete root product, then divide the omitted slot.
 R=(1+x*U)**3*(1+3*x*D)*(1+y*F)**6
 rhs=[R/(1+x*U),R/(1+3*x*D),R/(1+y*F)]
 assert all(a>=b for a,b in zip([D,U,F],rhs)) and e1*R<Q(1,10**7)
 for triple in product(range(6),repeat=3):
  n=sum(a==0 for a in triple)
  if n>=2:assert dissent(triple,*map(Q,args)) <= (e1 if n==3 else e2)
 print('certificate',args,'bound',float(e1*R),'margins',*[float(a-b) for a,b in zip([D,U,F],rhs)])
 # Corrupt amplification parameter; independent certificate must reject.
 xm=t+Q(11,10)*e2/t**2;Rm=(1+xm*U)**3*(1+3*xm*D)*(1+y*F)**6
 assert any(a<b for a,b in zip([D,U,F],[Rm/(1+xm*U),Rm/(1+3*xm*D),Rm/(1+y*F)]))
x=Q(4,27);v=Q(3,2);assert 3*x*v*v==1
print('endpoint_fixed_point_D_equation','D = 9/4 + D: impossible finite D')
assert devs(4150,1,2)[2]>Q(256,531441)>devs(4165,1,2)[2]
print('ceiling_bracket_pass');print('elapsed',time.monotonic()-t0)
