"""Upper-threshold size/readout scaling of conditional crossover operator."""
from pathlib import Path
import mpmath as m,json
m.mp.dps=60
poly=lambda r:16*r**4+92*r**3+39*r*r-2*r-1
rc=m.findroot(poly,(-m.mpf('.2'),-m.mpf('.15')));kc=-(rc+1)**2/(4*rc)
def data(beta,k):
 r1=m.exp(-beta);x=m.cosh(beta);e=x*x+2*k*x-1;x2=-2*k-x;r2=x2+m.sqrt(x2*x2-1);eta=2/(e+2)
 a=lambda r:k/r+1/(4*r*r)-1
 b=lambda r:1/(4*r)-eta*r
 det=a(r1)*b(r2)-a(r2)*b(r1)
 return det,r1,r2,e,-a(r1)/a(r2)
f=lambda be,k:data(be,k)[0]
slope=m.diff(lambda k:f(0,k),kc)/m.diff(lambda be:f(be,kc),0)
threshold_ratio=data(0,kc)[4];limit=(1+threshold_ratio)**2
rows=[]
for delta in ['.01','.003','.001','.0003','.0001']:
 dd=m.mpf(delta);k=kc-dd;be=m.findroot(lambda be:f(be,k),slope*dd);_,r1,r2,e,b=data(be,k)
 # psi_n=A(r1^n+b*r2^n), d= -sqrt2*psi1/(E+2).
 norm=1/(1-r1*r1)+2*b/(1-r1*r2)+b*b/(1-r2*r2)+2*(r1+b*r2)**2/(e+2)**2
 A2=1/norm;z=A2*(1+b)**2
 mean=(r1*r1/(1-r1*r1)**2+2*b*r1*r2/(1-r1*r2)**2+b*b*r2*r2/(1-r2*r2)**2)*A2
 rows.append(dict(delta=float(dd),beta=float(be),beta_over_delta=float(be/dd),binding_over_delta2=float((e-2*k)/(dd*dd)),residue=float(z),mean_host_index=float(mean),residue_times_mean=float(z*mean)))
 assert be>0 and abs(f(be,k))<m.mpf('1e-50')
out=dict(kappa_critical=str(kc),short_root=str(rc),beta_slope=str(slope),threshold_B_over_A=str(threshold_ratio),residue_times_mean_limit=str(limit),binding_quadratic=str((1+kc)*slope*slope),rows=rows,scope='Conditional effective operator only; feature size diverges by momentum approach to threshold, no parameter-free physical large feature')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
