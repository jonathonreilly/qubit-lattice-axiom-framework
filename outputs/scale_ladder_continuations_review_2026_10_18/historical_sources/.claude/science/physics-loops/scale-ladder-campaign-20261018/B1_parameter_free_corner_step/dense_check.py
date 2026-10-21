exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.linalg import expm
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
U=expm(1j*np.pi*Hon0/6)
W=lambda k: Hk(blS,np.asarray(k))@RL(np.asarray(k))@U
for E in (np.pi/3,-2*np.pi/3):
    dist=lambda k: np.min(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E)))
    g=np.linspace(-np.pi,np.pi,32,endpoint=False)
    vals=[]
    for k in itertools.product(g,repeat=3):
        k=np.array(k)+0.017
        if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.3: vals.append((dist(k),k))
    vals.sort(key=lambda x:x[0])
    mins=[]
    for d0,k0 in vals[:80]:
        r=minimize(dist,k0,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-14,maxiter=6000))
        if min(np.linalg.norm(wrap(r.x-kst)),np.linalg.norm(wrap(r.x+kst)))>0.05: mins.append((r.fun,np.round(np.mod(r.x+np.pi,2*np.pi)-np.pi,4)))
    mins.sort(key=lambda x:x[0])
    print("E=%.4f: 32^3 grid min %.5f; refined minima:"%(E,vals[0][0]),[(round(m,6),(k/(np.pi/2)).round(3).tolist()) for m,k in mins[:6]])
