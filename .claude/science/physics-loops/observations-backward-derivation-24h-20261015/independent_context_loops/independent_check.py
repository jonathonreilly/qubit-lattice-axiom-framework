import mpmath as m
from itertools import product
from pathlib import Path
import json
m.mp.dps=40
def sinc(x):return m.sin(x)/x if x else m.mpf(1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(v):return m.sqrt(sum(x*x for x in v))
def axis(t,b):return (m.sin(b)*m.cos(t),m.sin(b)*m.sin(t),m.cos(b))
def sig(a):return m.matrix([[a[2],a[0]-1j*a[1]],[a[0]+1j*a[1],-a[2]]])
def rotor(a,b):return (m.eye(2)+sig(b)*sig(a))/m.sqrt(2*(1+sum(x*y for x,y in zip(a,b))))
rows=[]
for N,beta in [(3,m.mpf('.7')),(5,m.mpf('1.8')),(9,m.mpf('2.6'))]:
 axes=[axis(2*m.pi*j/N,beta) for j in range(N)];axes.append(axes[0]);v=[cross(a,b) for a,b in zip(axes,axes[1:])]
 mat=m.eye(2)
 for a,b in zip(axes,axes[1:]):mat=rotor(a,b)*mat
 spin=m.matrix([m.cos(beta/2),m.sin(beta/2)]);phase=(spin.transpose_conj()*mat*spin)[0]
 gamma=-m.pi+N*m.atan(m.cos(beta)*m.tan(m.pi/N))
 assert abs(phase-m.exp(1j*gamma))<m.mpf('1e-35')
 rho=m.mpf('.63');k=m.mpf('2.7')
 def phi(i,j):
  acc=(0,0,0)
  for vv in v[i:j]:acc=add(acc,vv)
  return sinc(k*norm(acc)/2)
 F=[m.mpf(1)]
 for j in range(1,N+1):F.append(rho**(j-1)*phi(0,j)+(1-rho)*sum(rho**(j-i)*F[i-1]*phi(i-1,j) for i in range(2,j+1)))
 total=0
 for breaks in product((0,1),repeat=N-1):
  starts=[0]+[i+1 for i,z in enumerate(breaks) if z]+[N]
  weight=m.mpf(1)
  for z in breaks:weight*=1-rho if z else rho
  for i,j in zip(starts,starts[1:]):weight*=phi(i,j)
  total+=weight
 assert abs(total-F[-1])<m.mpf('1e-35')
 rows.append({'N':N,'loop_error':str(abs(phase-m.exp(1j*gamma))),'renewal_error':str(abs(total-F[-1]))})
for alpha,q in [(m.mpf('.2'),m.mpf('2.7')),(m.pi/2,m.mpf('.4')),(m.pi,0)]:
 mu=m.quad(lambda x:(1+m.cos(alpha-q*x))/4,[-1,1]);second=m.quad(lambda x:((1+m.cos(alpha-q*x))/2)**2/2,[-1,1])
 theoretical=(1+sinc(q)*m.cos(alpha))/2
 variance=((1+sinc(2*q)*m.cos(2*alpha))/2-sinc(q)**2*m.cos(alpha)**2)/4
 assert abs(mu-theoretical)<m.mpf('1e-35') and abs(second-mu**2-variance)<m.mpf('1e-35')
rows.append({'moment_quadrature':'three cases including degenerate endpoint; endpoint reservoir definition still needed'})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows))
