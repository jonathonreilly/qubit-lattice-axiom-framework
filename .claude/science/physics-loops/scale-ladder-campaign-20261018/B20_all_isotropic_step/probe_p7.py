exec(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/b20lib.py').read())
import pickle
clean=pickle.load(open('/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B20_all_isotropic_step/probe_p6.pkl','rb'))
def UH(p): return sum(np.exp(1j*a)*P for a,P in zip(p,Ps))
def UL(p): return sum(np.exp(1j*a)*Q for a,Q in zip(p,Qs))
for d0,nm,a,b,E in clean[::2]:
    w=['S','R',UH(a),UL(b)]
    # det sign on a finer grid
    g=np.linspace(-np.pi,np.pi,32,endpoint=False)+0.011; G=np.array(list(itertools.product(g,repeat=3)))
    rr=[]
    for i in range(0,len(G),4096):
        Ws=Wbatch(w,G[i:i+4096]); c0=np.linalg.det(Wk(w,np.zeros(3))); rr.append((np.linalg.det(Ws-np.exp(1j*E)*np.eye(12))/(np.exp(6j*E)*np.sqrt(c0))).real)
    rr=np.concatenate(rr); print(nm,"E=%.4f 32^3 det sign: min %.3e max %.3e"%(E,rr.min(),rr.max()))
    sols,gmin=find_crossings(w,E,ngrid=24,nstart=60)
    print("  crossings:",len(sols))
    for s in sols[:10]:
        v=vel_matrix(w,s,E); print("   ",np.round(s/np.pi,4),np.round(v['sv'],4),v['chi'],"spread %.1e"%v['spread'])
