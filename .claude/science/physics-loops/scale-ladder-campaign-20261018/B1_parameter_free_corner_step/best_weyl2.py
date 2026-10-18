exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
U=(Ps[0]+ph[2]*Ps[1]+ph[3]*Ps[2])@(Qs[0]+ph[1]*Qs[1]+ph[1]*Qs[2]+ph[0]*Qs[3])
W=lambda k: SK(k)@RL(k)@U
E=-np.pi/2
cands=[kst,-kst]+[kst+np.pi*e for e in np.eye(3)]+[-kst+np.pi*e for e in np.eye(3)]+[kst+np.pi*(np.ones(3)-e) for e in np.eye(3)]+[np.zeros(3),np.pi*np.ones(3)]
def berry(k0,r=0.02,n=16):
    th=np.linspace(0,np.pi,n+1); phh=np.linspace(0,2*np.pi,2*n,endpoint=False); Uv=[]
    for t in th:
        row=[]
        for p in phh:
            k=k0+r*np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])
            e,v=np.linalg.eig(W(k)); a=wrap(np.angle(e)-E); idx=np.argsort(np.where(np.abs(a)<0.3,a,9))[0]
            row.append(v[:,idx]/np.linalg.norm(v[:,idx]))
        Uv.append(row)
    tot=0
    for i in range(n):
        for j in range(2*n):
            a,b,c,d=Uv[i][j],Uv[i+1][j],Uv[i+1][(j+1)%(2*n)],Uv[i][(j+1)%(2*n)]
            tot+=np.angle(np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a))
    return tot/(2*np.pi)
for k0 in cands:
    e=np.sort(np.abs(wrap(np.angle(np.linalg.eigvals(W(k0)))-E)))
    m=int(np.sum(e<1e-7))
    if m==0: print("k/(pi/2)=",np.round(k0/(np.pi/2),3)," no level at E (closest %.3f)"%e[0]); continue
    sp=[]
    for d in DIRS[:30]:
        ee=np.sort(wrap(np.angle(np.linalg.eigvals(W(k0+1e-3*d)))-E)); ee=ee[np.abs(ee)<0.05]; sp.append((ee[-1]-ee[0])/2e-3)
    print("k/(pi/2)=",np.round(k0/(np.pi/2),3)," multiplicity",m," half-split/q mean %.6f spread %.2e"%(np.mean(sp),np.ptp(sp))," Berry %+.3f"%berry(k0))
