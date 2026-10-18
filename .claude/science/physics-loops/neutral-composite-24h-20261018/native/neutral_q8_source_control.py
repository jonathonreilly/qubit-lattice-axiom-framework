import mpmath as m
from fractions import Fraction as F
m.mp.dps=100
g=F(12155,33554432);D=F(15,512);de=F(5,8);A=F(432,17);d=F(1076510135,10567230160896);B=F(1616665793187,110234637824)
cb=3*D*(g/de)**2*(A-8);cd=8*g*d/de*(B-A/2);target=cb+cd
rows=[]
def mf(x):return m.mpf(x.numerator)/x.denominator
for ls in ['.03','.01','.003','.001']:
 l=m.mpf(ls);E=mf(de)*l**4;U=-3*mf(D)*l**6;t=mf(g)*l**10;s=2*mf(d)*l**12;t1=t+s;t2=t-s
 H=m.matrix([[0,-t1,-t1,0],[-t1,E,0,-t2],[-t1,0,E,-t2],[0,-t2,-t2,2*E+U]])
 ep=3*E;up=5*U;tp=mf(A)/2*t;sp=mf(B)*s
 C=m.matrix([[0,-tp-sp,-tp-sp,0],[-tp-sp,ep,0,-tp+sp],[-tp-sp,0,ep,-tp+sp],[0,-tp+sp,-tp+sp,2*ep+up]])
 ev,v=m.eigsy(H);amp=(v[:,3].T*C*v[:,0])[0]
 rows.append(dict(lambda_value=ls,scaled_amplitude=str(abs(amp)/l**18),relative_error=float(abs(amp)/l**18/mf(target)-1)))

import json
print(json.dumps(dict(binding=str(cb),detour=str(cd),coefficient=str(target),source_weight_coefficient=float(2*target**2/10),rows=rows),indent=2))
