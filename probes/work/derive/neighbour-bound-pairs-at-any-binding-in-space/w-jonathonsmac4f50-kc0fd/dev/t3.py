from dev_engine import *
import collections
Mz=np.eye(4,dtype=complex); Mall=build_M_all(Mz)
g=30.0; V=Vmat(g,Mall); N=24
roots=find_levels(V,N,+1,nscan=14)
grp=[]
for j,r in sorted(roots,key=lambda t:t[1]):
    if grp and abs(grp[-1][0]-r)<1e-5: grp[-1][1].append(j)
    else: grp.append([r,[j]])
for r,js in grp:
    E0=np.mean([x for x in [r]])
    out=level_weights(r,V,N)
    ev=np.linalg.eigvalsh(out['Wsum'])
    print(f"E0={r:.8f} mult={len(js)} null={out['null']} first={out['first']:.1e} gap={out['gap']:.3f} Wsum eig={np.round(ev,5)}  g^2*(ev-lead)=",np.round((ev)*1,4))
