exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam); Qt=Vl[:,-2:]@Vl[:,-2:].conj().T
for lab,U in (("S exp(i pi/2 Qtop)",np.eye(12)+(1j-1)*Qt),("S exp(-i pi/2 Qtop)",np.eye(12)+(-1j-1)*Qt)):
    W=lambda k: SK(k)@U
    lv=levels(W,kst); print("=====",lab,"levels at k*:",[(round(a,4),m) for a,m in lv])
    E=[a for a,m in lv if m==2][0]
    dist=lambda k: np.sort(np.abs(wrap(np.angle(np.linalg.eigvals(W(np.asarray(k))))-E)))
    g=np.linspace(-np.pi,np.pi,24,endpoint=False)
    pts=sorted(((dist(np.array(k)+0.05)[0],np.array(k)+0.05) for k in itertools.product(g,repeat=3)),key=lambda x:x[0])
    found=[]
    for d0,k0 in pts[:40]:
        r=minimize(lambda k: dist(k)[0],k0,method='Nelder-Mead',options=dict(xatol=1e-8,fatol=1e-12,maxiter=4000))
        if r.fun<1e-5:
            kk=np.mod(r.x+np.pi,2*np.pi)-np.pi
            if not any(np.allclose(np.exp(1j*(kk-f)),1,atol=1e-3) for f in found): found.append(kk)
    print("   zeros of min|eps-E| found:", [np.round(f/(np.pi/2),3).tolist() for f in found])
    print("   global min over grid away from ±k* (>0.3):", round(min(d for d,k in pts if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.3),4))
    for k0 in (kst,-kst):
        sp={}
        for q in (4e-3,2e-3,1e-3):
            sp[q]=np.array([ (lambda ee:(ee[-1]-ee[0])/(2*q))(np.sort(wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E)[np.abs(wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E))<0.1])) for d in DIRS])
        an=[np.ptp(sp[q])/sp[q].mean() for q in sp]
        print("   node",np.round(k0/(np.pi/2)).tolist(),"speed %.9f"%sp[1e-3].mean(),"aniso",np.round(an,10),"ratios",np.round([an[0]/an[1],an[1]/an[2]],3))
