# Exact source capture of the already executed inline diagnosis, before the
# main control's subtraction-block repair. It was not run as this file.
import two_detector_controls as own
from pathlib import Path
import numpy as np,math,json,hashlib
v,c=own.covariance(12,(6,0,0));a=np.array([1.,0.]);A=v;B=c*c/v;r=c
nodes,w=np.polynomial.hermite.hermgauss(32);Z1,Z2=np.meshgrid(np.sqrt(2)*nodes,np.sqrt(2)*nodes,indexing='ij');weight=w[:,None]*w[None,:]/np.pi;X=math.sqrt(v)*Z1;Y=c/math.sqrt(v)*Z1+math.sqrt(v-c*c/v)*Z2
rows=[]
for g in [.4,.2,.1,.05]:
 E1=2*np.sin(g*X/2)**2;E2=2*np.sin(g*Y/2)**2;one=Z1*Z1
 q=[float(np.sum(weight*f)) for f in [E1,E2,E1*E2,one*E1,one*E2,one*E1*E2]]
 num=q[5]-q[3]*q[1]-q[0]*q[4]+q[0]*q[1];den=(q[3]-q[0])*(q[4]-q[1]);z=g*g*c;cm=2*math.sinh(z/2)**2;exact=((1-g*g*(A+B))*cm+2*g*g*r*math.sinh(z))/(g**4*A*B)
 rows.append({'g':g,'v':v,'c':c,'A':A,'B':B,'direct_normalized':num/den,'stable_exact_normalized':exact,'difference':abs(num/den-exact),'subtraction_numerator':num,'subtraction_denominator':den,'conditioning_scale':(abs(q[5])+abs(q[3]*q[1])+abs(q[0]*q[4])+abs(q[0]*q[1]))/abs(den)})
out={'scope':'Narrow diagnosis of first failed normalized subtraction test; own code only.','own_source_sha256':hashlib.sha256(Path('two_detector_controls.py').read_bytes()).hexdigest(),'rows':rows}
Path('DIRECT_SUBTRACTION_DIAGNOSTIC.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
