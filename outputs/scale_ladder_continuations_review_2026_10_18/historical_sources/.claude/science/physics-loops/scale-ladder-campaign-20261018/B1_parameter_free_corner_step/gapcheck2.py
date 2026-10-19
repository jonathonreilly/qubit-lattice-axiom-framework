exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
U=(Ps[0]+ph[2]*Ps[1]+ph[3]*Ps[2])@(Qs[0]+ph[1]*Qs[1]+ph[1]*Qs[2]+ph[0]*Qs[3])
W=lambda k: Hk(blS,k)@RL(k)@U
g=np.linspace(-np.pi,np.pi,28,endpoint=False)
allph=np.concatenate([np.angle(np.linalg.eigvals(W(np.array(k)+0.031))) for k in itertools.product(g,repeat=3)])
h,edges=np.histogram(allph,bins=1440,range=(-np.pi,np.pi))
empty=edges[:-1][h==0]
# group contiguous empty bins
runs=[];
for x in empty:
    if runs and abs(x-runs[-1][1]-2*np.pi/1440)<1e-9: runs[-1][1]=x
    else: runs.append([x,x])
print("empty arcs on 28^3 grid:",[(round(a,3),round(b+2*np.pi/1440,3)) for a,b in runs])
