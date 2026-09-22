# Independent synthetic exact controls only; no native data or producer imports.
import resource,signal,json,time
signal.alarm(30)
from fractions import Fraction as F
from itertools import combinations
start=time.monotonic();n=0
def ck(x):
 global n
 assert x
 n+=1
# Interpolation, repeated contacts and zero/endpoints for both inverse majorants.
for d in (F(1,4),F(1),F(2)):
 for t in (d/2,d,2*d,8*d):
  A=(t+2*d)/(d*d*t**3)
  for x in (d,2*d,t if t>=d else d,16*d):
   Q=(3*t-2*x)/t**3+A*(x-t)**2
   ck(Q*x*x-1==(x-d)*(x-t)**2*((t+2*d)*x+d*t)/(d*d*t**3))
   ck(Q>=1/x**2)
  for u in (d/2,d,t,3*d):
   B=1/(d*t*t*u*u);aa=B*(1/d+2/t+2/u)
   # Derive coefficients from elementary symmetric sums, distinct from convolution producer.
   roots=[d,t,t,u,u];es={0:F(1)}
   for j in range(1,6):
    es[j]=sum((__import__('functools').reduce(lambda a,b:a*b,c,F(1)) for c in combinations(roots,j)),F(0))
   coeff=[aa*es[4]-B*es[3],B*es[2]-aa*es[3],aa*es[2]-B*es[1],B-aa*es[1],aa]
   for x in (d,2*d,9*d):
    q=sum(c*x**j for j,c in enumerate(coeff));ck(q*x*x-1==(x-d)*(x-t)**2*(x-u)**2*(aa*x+B));ck(q>=1/x**2)
# Kneser adjacency, characteristic annihilator and trace dimensions.
l=list(combinations(range(6),2));T=[[int(set(a).isdisjoint(b))for b in l]for a in l]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col))for col in zip(*b)]for row in a]
T2=mm(T,T);T3=mm(T2,T)
for i in range(15):
 for j in range(15):ck(T3[i][j]-4*T2[i][j]-15*T[i][j]+18*(i==j)==0)
ck(sum(T2[i][i]for i in range(15))==90)
# Sharp remainder via scalar minimization at endpoints and critical value.
for E in (F(0),F(1),F(3,2)):
 for Ff in (F(0),E,2*E,3*E,4*E,6*E):
  target=-3*E*E-3*E*Ff if Ff<=2*E else -6*E*E-F(3,4)*Ff*Ff if Ff<=4*E else 6*E*E-6*E*Ff
  if E==0:ck(target==0);continue
  # u=sqrt(3m+18) in[3,6]; objective E²(u²/3-6)-EFu.
  u=max(F(3),min(F(6),3*Ff/(2*E)));ck(E*E*(u*u/3-6)-E*Ff*u==target)
# Alternating positive-integral polynomial division for all three supplied orders.
for r in (2,3,4):
 for x in (F(0),F(1,2),F(12)):
  for t in (F(1,2),F(2),F(8)):
   poly=sum((-1)**j*x**(r-j)*t**(2*j)for j in range(r+1))+(-1)**(r+1)*t**(2*r+2)/(x+t*t)
   ck(poly==x**(r+1)/(x+t*t))
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 384*1024**2
print(json.dumps({'status':'PASS_SYNTHETIC_ONLY','checks':n,'seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'limit_seconds':30,'limit_bytes':384*1024**2,'native_or_primary_runs':0}))
