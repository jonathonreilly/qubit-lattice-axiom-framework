"""Independent reviewer control: standard library, CPU 20 s, address space 512 MiB.
No author runner import/execution; exact convolution coefficients and direct quadrature.
"""
import resource, math, json, time
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
t0=time.monotonic()
f=math.factorial
checks={}
# Independent convolution of sinh rather than symbolic expression reused from author.
for m in range(1,16):
 convolution=sum(Q(1,f(2*j+1)*f(2*(m-j-1)+1)) for j in range(m))
 coefficient=Q(2**(2*m-1),2*f(2*m-1))+(1 if m==1 else 0)-2*convolution
 checks['sign_coefficient_'+str(m)]=coefficient>=0
# Global lower bound: multiply inequality by x sinh(x)>0 and compare entire series.
for n in range(1,16):
 actual=Q(2*n,f(2*n+1))-Q(1,3*f(2*n-1))+(Q(1,45*f(2*n-3)) if n>=2 else 0)
 closed=Q(16*n*(n-1)*(n-2)*(n+2),45*f(2*n+1))
 checks['lower_bound_coefficient_'+str(n)]=actual==closed and actual>=0
# Quadrature directly integrates normalized exponential density in w; no A used in moments.
rows=[]
N=20000
for k in [0,0.01,0.2,1,3,10]:
 zs=[0.,0.,0.]
 for j in range(N+1):
  w=-1+2*j/N; wt=1 if j in (0,N) else (4 if j%2 else 2)
  p=wt*math.exp(k*(w-1))
  for r in range(3):zs[r]+=p*w**r
 mean=zs[1]/zs[0]; longitudinal=zs[2]/zs[0]-mean**2;transverse=(1-zs[2]/zs[0])/2
 checks['covariance_'+str(k)]=longitudinal<=transverse+1e-11 and transverse<=1/3+1e-11
 if k:checks['moment_'+str(k)]=abs(mean-(1/math.tanh(k)-1/k))<1e-10
 rows.append(dict(kappa=k,mean=mean,longitudinal=longitudinal,transverse=transverse))
# Explicit admissible unit predecessor path: sum zero then change only first unit vector.
base=[(1.,0.,0.),(-0.5,math.sqrt(3)/2,0.),(-0.5,-math.sqrt(3)/2,0.)]
ratios=[]
for th in [.01,.001]:
 delta=(math.cos(th)-1,0.,math.sin(th));norm=math.sqrt(sum(v*v for v in delta))
 ratios.append((th,(1/math.tanh(norm)-1/norm)/norm))
checks['attainable_mean_derivative']=abs(ratios[-1][1]-1/3)<1e-6
# Mutation controls corrupt theorem factors; independent quadrature detects both.
checks['wrong_uniform_variance_detected']=abs(rows[0]['transverse']-1/4)>0.01
checks['wrong_mean_slope_detected']=abs(ratios[-1][1]-0.3)>0.01
print(json.dumps(dict(checks=checks,quadrature=rows,attainable_ratios=ratios,elapsed=time.monotonic()-t0,scope='finite independent controls; all-parameter conclusions require prose series and compactness proof'),indent=2))
assert all(checks.values())
