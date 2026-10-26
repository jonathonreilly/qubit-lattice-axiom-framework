from dev_engine import *
import time
tabs=pickle.load(open('tabs.pkl','rb'))
Ms=commutant_z()
# Frobenius-orthonormalize
Gm=np.array([[np.trace(a@b).real for b in Ms] for a in Ms])
w,U=np.linalg.eigh(Gm); Lm=U@np.diag(w**-0.5)@U.T
Mb=[sum(Lm[i,j]*Ms[j] for j in range(5)) for i in range(5)]
print([[round(np.trace(a@b).real,6) for b in Mb] for a in Mb][0])
rng=np.random.default_rng(1)
def Mof(c):
    Mz=sum(ci*b for ci,b in zip(c,Mb)); return Mz
def scanM(Mz,tabs,verbose=False):
    Mall=build_M_all(Mz)
    # embed M in 24x24 block diag per bond
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    best=(-99,None)
    rows=[]
    for tab in tabs:
        for g in levels_tab(tab,M24):
            o=weights_tab(tab,g,M24)
            if o is None: continue
            ev=np.linalg.eigvalsh(o['Wsum'])
            rows.append((tab['E'],g,o['null'],ev.max(),ev.min(),o['first'],o['gap']))
    return rows
if __name__=="__main__":
    t=time.time()
    c=np.zeros(5); c[:]=rng.normal(size=5); c/=np.linalg.norm(c)
    rows=scanM(Mof(c),tabs)
    print(time.time()-t)
    for r in rows[:5]: print(r)
    print(max(r[3] for r in rows))
