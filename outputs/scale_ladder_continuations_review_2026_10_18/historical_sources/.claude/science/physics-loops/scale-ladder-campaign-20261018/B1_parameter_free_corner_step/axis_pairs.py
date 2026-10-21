exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
U=(Ps[0]+ph[2]*Ps[1]+ph[3]*Ps[2])@(Qs[0]+ph[1]*Qs[1]+ph[1]*Qs[2]+ph[0]*Qs[3])
W=lambda k: Hk(blS,k)@RL(k)@U
E=-np.pi/2
def speeds(k0):
    out={}
    for nm,d in (("x",[1,0,0]),("y",[0,1,0]),("z",[0,0,1]),("xy",[1,1,0]),("xyz",[1,1,1])):
        d=np.array(d,float); d/=np.linalg.norm(d); q=1e-4
        ee=wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E); ee=np.sort(ee[np.abs(ee)<0.01]); out[nm]=round((ee[-1]-ee[0])/(2*q),5)
    return out
for lab,k0 in (("k*",kst),("k*+pi ex",kst+np.pi*np.array([1,0,0])),("k*+pi ey",kst+np.pi*np.array([0,1,0])),("k*+pi ez",kst+np.pi*np.array([0,0,1])),("-k*+pi ex",-kst+np.pi*np.array([1,0,0]))):
    print(lab, speeds(k0))
