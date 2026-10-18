from neutral_slow_host import host
import numpy as np,json
from scipy.special import ai_zeros
from scipy.sparse import diags
from scipy.sparse.linalg import eigs
G0=host(-2);a=G0[0,0]/(1+G0[0,0]);source=np.array([1,2])/np.sqrt(2);LAMBDA=.1;f=LAMBDA**2/8;L=f**(-1/3);N=int(14*L)
pred=-2+f**(2/3)*abs(ai_zeros(1)[0][0])+f*(2+a)
# Energy shifted by +4, so host band[-4,4], armedge-2.
diagonal=f*(np.arange(N)+3).astype(complex);diagonal[0]+=G0[0,0]
H=diags([-np.ones(N-1),diagonal,-np.ones(N-1)],[-1,0,1],format='csc')
es,vs=eigs(H,k=1,sigma=pred,tol=1e-12);ep=es[0];width=-2*ep.imag;rows=[]
for E in np.linspace(ep.real-8*width,ep.real+8*width,161):
 G=host(E);g=0j
 for n in range(N,0,-1):g=1/(complex(E,1e-10)-f*(n+2)-g)
 background=source@G@source;vertex=source@G[:,0];full=background+vertex**2/(1/g-G[0,0])
 rows.append(dict(E=float(E),spectral=-full.imag/np.pi,background=-background.imag/np.pi))
out=dict(lam=LAMBDA,f=f,prediction=[pred.real,pred.imag],frozen_pole=[ep.real,ep.imag],rows=rows,minimum_spectral=min(r['spectral'] for r in rows),scope='Slow partial coefficient model; source limit has logarithmic corrections; no native observable identification')
print('min',out['minimum_spectral'],'background',rows[80]['background'],'central',rows[80]['spectral'])
open(__file__.replace('.py','.json'),'w').write(json.dumps(out,indent=2)+'\n')
