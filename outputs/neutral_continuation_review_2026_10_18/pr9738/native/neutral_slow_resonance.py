from neutral_slow_host import host
import numpy as np,json
from scipy.optimize import root
from scipy.special import ai_zeros
G0=host(-2);a=G0[0,0]/(1+G0[0,0]);source=np.array([1,2])/np.sqrt(2);rows=[]
for lam in [.3,.2,.1,.05,.025]:
 f=lam**2/8;L=f**(-1/3);N=int(14*L)
 pred=-2+f**(2/3)*abs(ai_zeros(1)[0][0])+f*(2+a)
 def denominator(E):
  g=0j
  for n in range(N,1,-1):g=1/(E-f*(n+2)-g)
  return E-3*f-host(E)[0,0]-g
 sol=root(lambda v:[denominator(complex(*v)).real,denominator(complex(*v)).imag],[pred.real,pred.imag],tol=1e-10);e=complex(*sol.x)
 g=gp=0j
 for n in range(N,1,-1):
  gn=1/(e-f*(n+2)-g);gp=-gn**2*(1-gp);g=gn
 h=1e-5;dG=(host(e+h)[0,0]-host(e-h)[0,0])/(2*h);denprime=1-dG-gp
 vertex=source@host(e)[:,0];residue=lam**4*vertex**2/denprime
 rows.append(dict(lam=lam,N=N,length=L,success=bool(sol.success),residual=abs(denominator(e)),pole=[e.real,e.imag],width_over_lambda4=-2*lam**2*e.imag/lam**4,residue_over_lambda6=[residue.real/lam**6,residue.imag/lam**6]))
out=dict(rows=rows,asymptotic_width=-a.imag/4,asymptotic_residue=[((source@G0[:,0])**2*(1-a)**2/8).real,((source@G0[:,0])**2*(1-a)**2/8).imag],scope='Partial slow coefficient graph and limiting source, not native pole or physical detector')
print(json.dumps(out,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
