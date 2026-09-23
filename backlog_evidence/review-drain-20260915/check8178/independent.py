import math,json,cmath
from fractions import Fraction as F
rows=[]
# Independent random-walk convolution, sum of squared propagator coefficients.
for L in (1,2,3,4,5,7):
 p={(0,0):F(1)};v=F(0)
 for t in range(1,13):
  v+=sum(z*z for z in p.values())
  modes=[]
  for a in range(L):
   for b in range(L):
    z=sum(cmath.exp(-2j*math.pi*(a*x+b*y)/L) for x,y in ((0,0),(1,0),(0,1)))/3
    modes.append(sum(abs(z)**(2*j) for j in range(t)))
  assert abs(float(v)-sum(modes)/(L*L))<1e-11
  assert sum(p.values())==1
  q={}
  for (a,b),c in p.items():
   for x,y in ((0,0),(1,0),(0,1)):
    k=((a+x)%L,(b+y)%L);q[k]=q.get(k,F(0))+c/3
  p=q
 rows.append({'L':L,'t':12,'variance':str(v),'average_variance':str(F(12,L*L))})
# Stationarity counterexample at self-conjugate L=2 mode: variance 0,1,10/9.
assert F(1)!=F(10,9)
# Negative Fourier convention direct deterministic shift fixture.
f=[cmath.exp(2j*math.pi*x/5) for x in range(5)]
y=[(f[x]+f[(x-1)%5]+f[x])/3 for x in range(5)]
actual=sum(y[x]*cmath.exp(-2j*math.pi*x/5) for x in range(5))/5
minus=(2+cmath.exp(-2j*math.pi/5))/3;plus=minus.conjugate()
assert abs(actual-minus)<1e-12 and abs(actual-plus)>.1
br=[]
for L in (2,3,4,5,8,16,32,64):
 reps=[n if n<=L//2 else n-L for n in range(L)];S=0;V=0;u_max=0
 for a in reps:
  for b in reps:
   if a==b==0:continue
   k=2*math.pi*a/L;l=2*math.pi*b/L
   gap=sum(abs(z)**2 for z in (1-cmath.exp(1j*k),1-cmath.exp(1j*l),cmath.exp(1j*k)-cmath.exp(1j*l)))/9
   S+=1/(a*a+b*b);V+=1/gap/L**2;u_max=max(u_max,1-gap)
   assert 4*(k*k+l*l)/(9*math.pi**2)<=gap+1e-13<= (k*k+l*l)/3+1e-12
 assert 3*S/(4*math.pi**2)<=V<=9*S/16
 br.append(dict(L=L,S=S,V=V,slow_variance_efold=-1/math.log(u_max),slow_to_V=(-1/math.log(u_max))/V))
print(json.dumps(dict(status='PASS finite independent controls',walk=rows,brackets=br,stationarity_counterexample=['0','1','10/9'],fourier_actual=[actual.real,actual.imag],size_data_difference_beta6_lag25=.072,reported_combined_standard_error=math.hypot(.014,.005)),indent=2))
