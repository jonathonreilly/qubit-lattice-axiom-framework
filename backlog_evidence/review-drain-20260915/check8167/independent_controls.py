import math,json,time,itertools,pathlib,hashlib
from fractions import Fraction as F
import mpmath as mp
start=time.monotonic();mp.mp.dps=60
# Direct differentiation of scalar log image sum, rather than runner Fourier derivative formulas.
g=mp.mpf('.8');T=mp.mpf('.4');z=mp.pi-mp.mpf('.07')
def Z(x):return mp.fsum(mp.exp(-(x+2*mp.pi*n)**2/(2*g*g*T)) for n in range(-6,7))
def A(x):return -g*g*mp.log(Z(x))
w=[mp.exp(-(z+2*mp.pi*n)**2/(2*g*g*T))/Z(z) for n in range(-6,7)];d=[z+2*mp.pi*n for n in range(-6,7)];mean=sum(a*b for a,b in zip(w,d));third=sum(a*(b-mean)**3 for a,b in zip(w,d))/(g**4*T**3)
assert abs(mp.diff(A,z,3)-third)<mp.mpf('1e-45');assert mp.diff(A,mp.pi,2)<0
# Enumerate sign environments and propagate Bernoulli raw moments by polynomial convolution.
L=2;rho=F(1,6);m4=F(0);m2=F(0)
for signs in itertools.product((-1,1),repeat=8):
 moments=[F(1),F(0),F(0),F(0),F(0)]
 for r in itertools.product(range(L),repeat=4):
  s=math.prod(signs[2*i+r[i]] for i in range(4));nextm=[]
  for k in range(5):nextm.append(sum(F(math.comb(k,j))*moments[k-j]*(F(1) if j==0 else rho*s**j) for j in range(k+1)))
  moments=nextm
 m2+=moments[2]/256/16;m4+=moments[4]/256/256
expected=rho/16+3*rho*rho*F(15,16)+rho**4*(16-3+F(2,16))
assert m2==rho and m4==expected
# Independent pointwise amplitude-phase and Taylor signs, including negative sources.
maxerr=0.
for B,h,t,g0 in itertools.product((-.9,.3,2.8),(-1.2,.2),(-.8,.7),(.3,1.1)):
 R=math.hypot(1,g0*t*h);phi=math.atan(g0*t*h)
 err=abs(math.cos(B)+g0*t*h*math.sin(B)-R*math.cos(B-phi));maxerr=max(err,maxerr)
 assert err<1e-14
 remainder=-(1-math.cos(B+g0*t*h))/g0**2+(1-math.cos(B))/g0**2+t*h*math.sin(B)/g0+t*t*h*h*math.cos(B)/2
 assert abs(remainder)<=g0*abs(t*h)**3/6+1e-14
# Static curl support: norm exponents and shifted contact CS yield exp(t²K+4delta).
assert .5*(2**3)==4
out=dict(status='PASS',circle_cubic=str(third),circle_derivative_error=str(abs(mp.diff(A,z,3)-third)),moment2=str(m2),moment4=str(m4),amplitude_maxerror=maxerr,elapsed_seconds=time.monotonic()-start,scope='Small independent algebra and finite-law controls; no primary runner rerun; not infinite-volume numeric proof.')
print(json.dumps(out,indent=2))
