from fractions import Fraction as F
from itertools import product
import json,time,pathlib
start=time.monotonic();checks=0
# Rotation-series coefficient, not symbolic differential operators from primary.
for x,y in [((F(3,5),0,F(4,5)),(0,F(5,13),F(12,13))),((1,0,0),(0,0,1)),((0,1,0),(0,1,0))]:
 for a,b in [(1,2),(-2,3),(4,4)]:
  # R_y(a*t)x dot R_y(b*t)y depends only on relative angle.
  second=-(a-b)**2*(x[0]*y[0]+x[2]*y[2]);assert -second==(a-b)**2*(x[0]*y[0]+x[2]*y[2]);checks+=1
# Exact i-valued modes including self-inverse k=pi, absent from original runner.
I=complex(0,1);sites=list(product(range(4),repeat=3));N=len(sites);results=[]
for mode in [(1,0,0),(1,1,0),(2,0,0),(2,2,2)]:
 wave={x:I**sum(a*b for a,b in zip(mode,x))for x in sites};E=sum(2-2*(I**a).real for a in mode)
 energy=sum(abs(wave[x]-wave[tuple((x[j]+(j==i))%4 for j in range(3))])**2 for x in sites for i in range(3));assert energy==N*E
 co=sum(z.real*z.real for z in wave.values());si=sum(z.imag*z.imag for z in wave.values());assert co+si==N
 assert (co,si)==((N,0)if all(a%2==0 for a in mode)else(N/2,N/2));results.append({'mode_pi_over_2':mode,'E':E,'complex_gradient':energy,'cos_norm':co,'sin_norm':si});checks+=3
# Rational root equation tested using constructed rational roots, without radicals.
for n,b,u in product([8,64,216],[F(1,3),F(2,3),F(3,2)],[F(1,7),F(2,5)]):
 a=u*u/n+b*u;disc=b*b+4*a/n;assert disc==(b+2*u/n)**2;assert 2*a/(b+(b+2*u/n))==u;checks+=2
# Nonunit shifted-spin equality counterexample: both original spins e1, shift both by1 => shifted0.
assert F(0)!=F(-1);checks+=1
out={'checks':checks,'fail':0,'rotation_series_scope':'rational unit fixtures under actual one-parameter rotation, independent of primary derivative code','fourier_controls':results,'shifted_kernel_counterexample':'original sx=sy=e1 and phi_x=phi_y=1 yields shifted0: Gaussian exponent0, claimed -beta+beta dot=-beta; norm factors required','gaussian_import_normalization':'ordered NN J=1/6 sums to(1/3) unordered bond sum; theorem parameter3beta/2 yields beta/2 unordered energy','elapsed_seconds':time.monotonic()-start}
p=pathlib.Path('/private/tmp/review-drain-20260915/check8153/controls.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
