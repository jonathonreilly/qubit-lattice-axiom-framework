exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
import time; t0=time.time()
rng=np.random.default_rng(11)
g=np.linspace(-np.pi,np.pi,16,endpoint=False)+0.0731; GRID=np.array(list(itertools.product(g,repeat=3)))
def UH(p): return sum(np.exp(1j*a)*P for a,P in zip(p,Ps))
def UL(p): return sum(np.exp(1j*a)*Q for a,Q in zip(p,Qs))
def rsign(w,E):
    Ws=Wbatch(w,GRID); c0=np.linalg.det(Ws[0]); r=(np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0))).real
    return r.min()<0<r.max(), Ws
clean=[]; tot=0
for trial in range(150):
    a=rng.uniform(0,2*np.pi,3); b=rng.uniform(0,2*np.pi,4); b[3]=b[0]
    for nm,w in [("S.R.UH.UL",['S','R',UH(a),UL(b)]),("S.UH.R.UL",['S',UH(a),'R',UL(b)])]:
        lv=[(e,m) for e,m in node_levels(w,kst,1e-8) if m==2]; lvm=[(e,m) for e,m in node_levels(w,-kst,1e-8) if m==2]
        for E,_ in lv:
            if not any(abs(wrap(E-f))<1e-8 for f,_ in lvm): continue
            tot+=1; fs,Ws=rsign(w,E)
            if not fs:
                d=np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws))-E)),axis=-1)
                far=np.array([min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.3 for k in GRID])
                clean.append((d[far].min(),nm,a,b,E))
print(tot,"pairs;",len(clean),"pass the det sign test", time.time()-t0)
clean.sort(key=lambda x:-x[0])
for c in clean[:10]: print(round(c[0],4),c[1],np.round(c[2],3),np.round(c[3],3),round(c[4],4))
import pickle; pickle.dump(clean,open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/probe_p6.pkl','wb'))
