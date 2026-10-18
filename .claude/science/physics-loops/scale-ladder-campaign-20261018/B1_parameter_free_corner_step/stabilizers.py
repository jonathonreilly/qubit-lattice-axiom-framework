exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
TVl=TV; KS=[np.array(t)*2*np.pi/L for t in TVl]
def Bloch(k):
    B=np.zeros((nV,12),complex)
    for a,(v,c) in enumerate(C.VERTS): B[a,CI[c]]=np.exp(1j*np.dot(k,v))/np.sqrt(L**3)
    return B
BK=[Bloch(k) for k in KS]; BALL=np.hstack(BK)
def opmat(r):
    P,s=rots[r]; M=np.zeros((nV,nV)); M[P,np.arange(nV)]=(-1.0)**s; return M
img={}
for r in range(24):
    Y=np.abs(BALL.conj().T@opmat(r)@BALL)**2; Wb=Y.reshape(64,12,64,12).sum(axis=(1,3))
    for i in range(64): img[(r,i)]=int(np.argmax(Wb[:,i]))
def idx(k): return [i for i,q in enumerate(KS) if np.allclose(np.exp(1j*(q-k)),1)][0]
cube=[np.array(s)*np.pi/2 for s in itertools.product((1,-1),repeat=3)]
for c in cube:
    i=idx(c); stab=[r for r in range(24) if img[(r,i)]==i]
    orbit=sorted(set(img[(r,i)] for r in range(24)))
    axes=[]
    for r in stab:
        R=C.ROTS[r]; w,v=np.linalg.eig(R.astype(float)); ax=np.real(v[:,np.argmin(np.abs(w-1))]); ang=np.degrees(np.arccos(np.clip((np.trace(R)-1)/2,-1,1)))
        axes.append((round(ang),tuple(np.round(ax/np.max(np.abs(ax)),2))))
    print(np.round(c/(np.pi/2)).astype(int).tolist(),"stabilizer order",len(stab),"orbit size",len(orbit), sorted(set(axes))[:8])
