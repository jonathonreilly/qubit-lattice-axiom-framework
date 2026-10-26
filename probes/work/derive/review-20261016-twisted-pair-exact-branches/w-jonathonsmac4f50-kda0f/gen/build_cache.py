import pickle
exec(open('setup.py').read())
U=build_unitarity()
eqs=set()
for m,acc in U.items():
    for a in range(4):
        for b in range(4):
            for part in acc[a][b]:
                if part: eqs.add(tuple(sorted(part.items())))
eqs=sorted(eqs)
log('equations',len(eqs))
# Linear axis data: B_r = sum_{n_x=r} A_n  -> complex entries as pairs of real-linear polys (dict var->coef)
def lin_entry(r,a,b):
    re={};im={}
    for n in cell:
        if n[0]!=r: continue
        for j,Mj in Mn.get(n,[]):
            g=Mj[a][b]
            if g==Z0: continue
            # (x_j+i y_j) * g
            padd_inplace(re,(j,),g[0]); padd_inplace(im,(j,),g[1])
            padd_inplace(re,(NP+j,),-g[1]); padd_inplace(im,(NP+j,),g[0])
    return re,im
Bent={(r,a,b):lin_entry(r,a,b) for r in (-1,0,1) for a in range(4) for b in range(4)}
# U(0)=1 linear: sum_n A_n = I
def sum_entry(a,b):
    re={};im={}
    for n in cell:
        for j,Mj in Mn.get(n,[]):
            g=Mj[a][b]
            if g==Z0: continue
            padd_inplace(re,(j,),g[0]); padd_inplace(im,(j,),g[1])
            padd_inplace(re,(NP+j,),-g[1]); padd_inplace(im,(NP+j,),g[0])
    return re,im
Sent={(a,b):sum_entry(a,b) for a in range(4) for b in range(4)}
pickle.dump({'NP':NP,'NV':NV,'params':params,'M':M,'eqs':eqs,'Bent':Bent,'Sent':Sent,
 'G':[(key(R),str(D.tolist())) for R,D in G]},open('cache.pkl','wb'))
log('saved')
