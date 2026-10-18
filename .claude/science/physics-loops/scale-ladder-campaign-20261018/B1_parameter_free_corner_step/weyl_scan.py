exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.optimize import minimize
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
wl,Vl=np.linalg.eigh(Lam); Qt=Vl[:,-2:]@Vl[:,-2:].conj().T
U=np.eye(12)-2*Qt
def phases(k):
    e=np.angle(np.linalg.eigvals(Hk(blS,k)@U)); return np.sort(np.mod(e,2*np.pi))   # in [0,2pi)
# bands sorted in [0,2pi): the pi-pair are the two bands closest to pi at k*
g=np.linspace(-np.pi,np.pi,24,endpoint=False)
allp=np.array([phases(np.array(k)) for k in itertools.product(g,repeat=3)])
print("quasi-energy band ranges (sorted bands):")
for b in range(12): print("  band",b,"min %.4f max %.4f"%(allp[:,b].min(),allp[:,b].max()))
pts=list(itertools.product(g,repeat=3))
near=[(np.min(np.abs(allp[i]-np.pi)), np.sum(np.abs(allp[i]-np.pi)<1e-6), np.round(np.array(pts[i])/(np.pi/2),3)) for i in range(len(pts))]
exact=[(n,k) for d,n,k in near if n>0]
from collections import Counter
print("grid points with quasi-energy exactly pi:",len(exact)); print(Counter(n for n,k in exact))
for n,k in exact[:30]: print("  mult",n,"at k/(pi/2) =",k)
