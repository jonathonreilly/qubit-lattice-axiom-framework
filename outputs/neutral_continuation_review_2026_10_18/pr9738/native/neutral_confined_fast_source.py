import numpy as np,json
from numba import njit
from scipy.special import ai_zeros
from neutral_outgoing_host import G
@njit
def arm(E,f,N):
 g=0j
 for n in range(N,0,-1):g=1/(E-f*(n+1)-4*g)
 return g
# Host outgoing near-zero asymptotic tested numerically later; here track sufficient g conditions.
rows=[]
for lam in [.2,.1,.05,.025,.02]:
 fs=lam**2/8;slow=-6+fs**(2/3)*abs(ai_zeros(1)[0][0])+fs*(2+complex(-.2796521330954,-.4544316488004))
 z=lam*slow;ff=lam**3/16;N=int(10/ff)
 g=arm(z,ff,N)
 rows.append(dict(lam=lam,z=[z.real,z.imag],f_fast=ff,N=N,abs_g=abs(g),g=[g.real,g.imag],abs_z_over_g=abs(z/g),eta_over_f=-z.imag/ff))
for row in rows:
 z=complex(*row['z']);g=complex(*row['g']);h=G(z);R=h/(1-4*g*h);A=(1-z*R)/2**.5;D=2**.5*(1-R/h)
 row.update(host_G=[h.real,h.imag],source_A=[A.real,A.imag],source_D=[D.real,D.imag])
print(json.dumps(rows,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(rows,indent=2)+'\n')
