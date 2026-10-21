exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam); lv_=sorted(set(np.round(wl,6)))
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in lv_]
print("Lam eigenvalues",lv_,"dims",[int(round(np.trace(Q).real)) for Q in Qs])
for nm,U in (("1-2Q_top",np.eye(12)-2*Qs[3]),("1-2Q_bottom",np.eye(12)-2*Qs[0]),("identity",np.eye(12))):
    W=lambda k: SK(k)@U
    print("=====",nm, "levels at k*:",[(round(a,4),m) for a,m in levels(W,kst)], " at -k*:",[(round(a,4),m) for a,m in levels(W,-kst)])
    for k0,lab in ((kst,"k*"),(-kst,"-k*")):
        for E,m in levels(W,k0):
            if m!=2: continue
            sp={}
            for q in (4e-3,2e-3,1e-3):
                Sx=[]
                for d in DIRS:
                    ee=wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E); ee=np.sort(ee[np.abs(ee)<0.1]); Sx.append((ee[-1]-ee[0])/(2*q))
                sp[q]=np.array(Sx)
            an=[np.ptp(sp[q])/sp[q].mean() for q in (4e-3,2e-3,1e-3)]
            # Berry flux of lower band of the doublet through sphere
            def berry(k0,E,r=0.02,n=16):
                th=np.linspace(0,np.pi,n+1); phh=np.linspace(0,2*np.pi,2*n,endpoint=False); Uv=[]
                for t in th:
                    row=[]
                    for p in phh:
                        k=k0+r*np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)])
                        e,v=np.linalg.eig(W(k)); a=wrap(np.angle(e)-E); idx=np.argsort(np.where(np.abs(a)<0.1,a,9))[0]
                        row.append(v[:,idx]/np.linalg.norm(v[:,idx]))
                    Uv.append(row)
                tot=0
                for i in range(n):
                    for j in range(2*n):
                        a,b,c,d=Uv[i][j],Uv[i+1][j],Uv[i+1][(j+1)%(2*n)],Uv[i][(j+1)%(2*n)]
                        tot+=np.angle(np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a))
                return tot/(2*np.pi)
            print(f"  {lab} doublet at {E:+.4f}: speed {sp[1e-3].mean():.9f} (sqrt2/3={np.sqrt(2)/3:.9f}) rel.anisotropy {np.round(an,10)} ratios {np.round([an[0]/an[1],an[1]/an[2]],3)} Berry {berry(k0,E):+.4f}")
