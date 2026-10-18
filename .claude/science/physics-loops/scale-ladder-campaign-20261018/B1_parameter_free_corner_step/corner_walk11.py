exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
X0=1j*(Hon0@Lam-Lam@Hon0)
from scipy.linalg import expm
SL=msign(Lam); R2=np.eye(12)-2*Ps[2]
for th in (0.3,0.7,np.pi/4,np.pi/2):
  for nm,Uf in (("R2",lambda th: expm(1j*th*X0/4.899)@R2),("SL",lambda th: expm(1j*th*X0/4.899)@SL),("Hon",lambda th: expm(1j*th*X0/4.899)@expm(1j*0.9*Hon0))):
    U=Uf(th); W=lambda k: RL(k)@U
    lv=levels(W,kst)
    print(f"theta={th:.3f} {nm}: k* levels", [(round(a,3),m) for a,m in lv])
    for E,m in lv:
        if m==2:
            S=[]
            for d in DIRS[:20]:
                ee=wrap(np.angle(np.linalg.eigvals(W(kst+1e-3*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); S.append((ee[-1]-ee[0])/2e-3 if len(ee)==2 else np.nan)
            print("      doublet",round(E,3),"half-split/q",np.round(np.nanmean(S),5),"spread",np.round(np.nanmax(S)-np.nanmin(S),7))
