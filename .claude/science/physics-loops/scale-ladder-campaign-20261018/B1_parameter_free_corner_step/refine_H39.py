exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
U=Ps[0]+1j*Ps[1]-1j*Ps[2]
W=lambda k: Hk(blS,np.asarray(k))@RL(np.asarray(k))@U
lv=levels(W,kst); print("levels at k*",[(round(a,4),m) for a,m in lv])
for E in [a for a,m in lv if m==2]:
    dist=lambda k: np.sort(np.abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E)))
    g=np.linspace(-np.pi,np.pi,24,endpoint=False)
    pts=sorted(((dist(np.array(k)+0.031)[0],np.array(k)+0.031) for k in itertools.product(g,repeat=3)),key=lambda x:x[0])
    found=[]
    for d0,k0 in pts[:60]:
        r=minimize(lambda k: dist(k)[0],k0,method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-13,maxiter=5000))
        kk=np.mod(r.x+np.pi,2*np.pi)-np.pi
        if r.fun<1e-6 and not any(np.allclose(np.exp(1j*(kk-f)),1,atol=1e-3) for f in found): found.append(kk)
    far=[d for d,k in pts if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.3]
    print("E=%.4f: zeros found:"%E,[np.round(f/(np.pi/2),4).tolist() for f in found],"; 24^3 grid min away from nodes %.4f"%min(far))
