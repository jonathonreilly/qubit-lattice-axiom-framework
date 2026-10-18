exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
import time,pickle; t0=time.time()
rng=np.random.default_rng(31); Rpl=onL(2,0,2)
def UH(p): return sum(np.exp(1j*a)*P for a,P in zip(p,Ps))
def UL(p): return sum(np.exp(1j*a)*Q for a,Q in zip(p,Qs))
# the Z-tastes make the spectrum pi-periodic: grid on the pi-cube
g=np.linspace(-np.pi/2,np.pi/2,14,endpoint=False)+0.0371; G=np.array(list(itertools.product(g,repeat=3)))
res=[]
for t in range(400):
    a=rng.uniform(0,6.3,3); b=rng.uniform(0,6.3,4); b[3]=b[0]
    order=rng.integers(2)
    A=UH(a)@UL(b) if order==0 else UL(b)@UH(a)
    w=['S',A,'S',Rpl]
    lv=[(e,m) for e,m in node_levels(w,kst,1e-8) if m==2]
    if len(lv)<2: continue
    Ws=Wbatch(w,G); c0=np.linalg.det(Ws[0])
    for E,_ in lv:
        r=(np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0))).real
        if r.min()<0<r.max(): continue
        d=np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws))-E)),axis=-1)
        res.append((float(d.min()),a,b,order,E))
print(len(res),"pass det test of",400*2, time.time()-t0)
res.sort(key=lambda x:-x[0])
for r_ in res[:8]: print(round(r_[0],4),np.round(r_[1],3),np.round(r_[2],3),r_[3],round(r_[4],4))
pickle.dump(res,open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/probe_p9.pkl','wb'))
