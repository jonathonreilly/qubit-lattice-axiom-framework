import numpy as np, json
from scipy.optimize import brentq
from yukawa_chunked import run_chunked as run
def g(eps,m,mu): return run(48,48,eps,m,mu)['gap'] if eps>=1 else None
out={}
for (m,mu) in [(0.5,0.5),(1.0,0.3),(0.3,1.0),(0.7,0.7)]:
    es=np.linspace(1.02,3.0,12)
    vals=[run(48,48,e,m,mu)['gap'] for e in es]
    zs=[]
    for i in range(len(es)-1):
        if vals[i]*vals[i+1]<0:
            f=lambda e: run(48,48,e,m,mu)['gap']
            zs.append(brentq(f,es[i],es[i+1],xtol=1e-6))
    print(f"m={m} mu={mu}: gap(eps>1) sign pattern {[round(v,5) for v in vals[:6]]} ...  zeros at eps>1: {zs}")
    out[f"{m},{mu}"]=zs
json.dump(out,open('scan6.json','w'))
