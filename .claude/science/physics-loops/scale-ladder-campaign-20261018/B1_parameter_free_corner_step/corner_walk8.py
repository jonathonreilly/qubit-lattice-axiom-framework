exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
X0=1j*(Hon0@Lam-Lam@Hon0)
def projs(M):
    w,V=np.linalg.eigh(M); ls=sorted(set(np.round(w,6)))
    return [V[:,np.abs(w-l)<1e-6]@V[:,np.abs(w-l)<1e-6].conj().T for l in ls]
PX=projs(X0); PL=projs(Lam)
tests={"RL*(1-2P2)":lambda k: RL(k)@(np.eye(12)-2*Ps[2]),
       "RL*signLam":lambda k: RL(k)@msign(Lam),
       "RL*(1-2PX+)":lambda k: RL(k)@(np.eye(12)-2*PX[-1]),
       "RL*(1-2PX+)*(1-2P2)":lambda k: RL(k)@(np.eye(12)-2*PX[-1])@(np.eye(12)-2*Ps[2]),
       "RL*(PX- + i PX0 - PX+)":lambda k: RL(k)@(PX[0]+1j*PX[1]-PX[2])}
for nm,W in tests.items():
    degs=[]
    for k in KG:
        e=np.sort(np.angle(np.linalg.eigvals(W(k)))); d=np.diff(e); degs.append(int(np.sum(d<1e-7)))
    print(nm,"pairs of degenerate eigenvalues at generic k:",degs, " k* levels:",[(round(a,3),m) for a,m in levels(W,kst)])
analyse(tests["RL*(1-2PX+)"],"RL*(1-2PX+)")
analyse(tests["RL*(PX- + i PX0 - PX+)"],"RL*(PX- + i PX0 - PX+)")
