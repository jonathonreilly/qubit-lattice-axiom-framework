exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
import pickle,time; t0=time.time()
res=pickle.load(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/probe_p9.pkl','rb'))
Rpl=onL(2,0,2)
def UH(p): return sum(np.exp(1j*a)*P for a,P in zip(p,Ps))
def UL(p): return sum(np.exp(1j*a)*Q for a,Q in zip(p,Qs))
g=np.linspace(-np.pi/2,np.pi/2,40,endpoint=False)+0.0071; G=np.array(list(itertools.product(g,repeat=3)))
for d0,a,b,order,E in res[::2][:18]:
    A=UH(a)@UL(b) if order==0 else UL(b)@UH(a); w=['S',A,'S',Rpl]
    rr=[]
    for i in range(0,len(G),8000):
        Ws=Wbatch(w,G[i:i+8000]); c0=np.linalg.det(Ws[0]); rr.append((np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0))).real)
    rr=np.concatenate(rr)
    if rr.min()<0<rr.max(): print("E=%.3f: 40^3 det sign change -> Fermi surface"%E); continue
    sols,gmin=find_crossings(w,E,ngrid=20,nstart=80,lo=-np.pi/2,hi=np.pi/2,period=np.pi)
    desc=[]
    for s in sols:
        v=vel_matrix(w,s,E); desc.append((np.round(s/np.pi,3).tolist(),np.round(v['sv'],4).tolist(),v['chi'],'%.0e'%v['spread']))
    print("E=%.3f a=%s b=%s ord=%d: %d crossings"%(E,np.round(a,3),np.round(b,3),order,len(sols)),desc[:8],flush=True)
print(time.time()-t0)
