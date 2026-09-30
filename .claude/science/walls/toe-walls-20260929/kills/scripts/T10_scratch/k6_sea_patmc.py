import numpy as np, json, sys, beam_vs_sea as b
from patmc import mi_pattern
from gauss import holevo
from numbound import num_info
rng=np.random.default_rng(7)
def sea(L,T,g,coup):
    h=b.chain_h(L); j0=L//2
    e,U=np.linalg.eigh(h); Phi0=U[:,:L//2]
    Vu,Vd=(g,0.0) if coup=='proj' else (g,-g)
    Pu=b.evolve(h,j0,Vu,Phi0,T); Pd=b.evolve(h,j0,Vd,Phi0,T)
    ov=float(np.prod(np.linalg.svd(Pu.conj().T@Pd,compute_uv=False)))
    return b.corr(Pu),b.corr(Pd),j0,ov
Du,Dd,j0,ov=sea(240,30.0,3.0,'sym')
for (i,m) in [(j0-9,8),(j0+1,8)]:
    a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
    mi,se=mi_pattern(a,c,1500,rng)
    print('sanity m=8 offset',i-j0,'exact',round(holevo(a,c),4),'pattern-MC',round(mi,4),'+-',round(se,4),'number',round(num_info(a,c),4),flush=True)
out=[]
for (L,T,g,coup) in [(240,30.0,3.0,'sym'),(240,30.0,20.0,'proj')]:
    Du,Dd,j0,ov=sea(L,T,g,coup)
    p=(1+ov)/2
    print('config',L,T,g,coup,'branch overlap',round(ov,4),'whole-env info <=',round(-(p*np.log2(p)+(1-p)*np.log2(1-p)),3),flush=True)
    for m in (16,32):
        for name,i in (('right-adjacent',j0+1),('left-adjacent',j0-m),('centred',j0-m//2)):
            a,c=Du[i:i+m,i:i+m],Dd[i:i+m,i:i+m]
            mi,se=mi_pattern(a,c,300,rng)
            r=dict(L=L,T=T,g=g,coup=coup,m=m,where=name,mi_pattern=round(mi,3),se=round(se,3),num=round(num_info(a,c),3))
            print(r,flush=True); out.append(r)
json.dump(out,open('k6_sea_patmc.json','w'),indent=1)
