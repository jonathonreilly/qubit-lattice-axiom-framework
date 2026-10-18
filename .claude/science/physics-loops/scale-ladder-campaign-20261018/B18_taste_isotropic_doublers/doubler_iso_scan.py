#!/usr/bin/env python3
"""B18 part 3: scan the B1 Clifford-phase families (links S, S.R_L, R_L.S times on-site U from
H_on and Lambda spectral projectors with phases in {1,i,-1,-i}) for steps whose doublers at
k*+pi e_x (and -k*+pi e_x) are Weyl doublets at the k* node quasi-energy, and report how close
they are to isotropic at the k* speed. Coarse pass q=1e-4 symmetric differences, then refined
(Richardson q -> 0) on the best candidates. Prints PASS/FAIL and TOTAL."""
import time, pickle
exec(open('b18lib.py').read())
t0=time.time()
onH=[(f"H{a}{b}",UHf(a,b)) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",ULf(a,b,c)) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]+[(l[0]+"*"+h[0],l[1]@h[1]) for h in onH for l in onL]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
q=1e-4
DX=[EX[0],EX[1],EX[2],np.array([0,1,1])/np.sqrt(2),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3)]
pts={"k*":kst,"D+x":kst+np.pi*EX[0],"D-x":-kst+np.pi*EX[0]}
need=[]
for k0 in pts.values():
    need.append(k0)
    for d in DX: need+= [k0+q*d, k0-q*d]
LK={nm:{tuple(np.round(k,9)):f(k) for k in need} for nm,f in links.items()}
def get(nm,k): return LK[nm][tuple(np.round(k,9))]
def pair_speed(nm,U,k0,d,E):
    out=[]
    for sg in (1,-1):
        ee=wrap(np.angle(np.linalg.eigvals(get(nm,k0+sg*q*d)@U))-E); ee=np.sort(ee[np.abs(ee)<0.02])
        if len(ee)!=2: return np.nan
        out.append(ee)
    return (out[0][1]-out[0][0]+out[1][1]-out[1][0])/(4*q)
res=[]; nweyl=0
for nm in links:
    for un,U in cands:
        W0=get(nm,kst)@U
        for E,m in levels(lambda k: W0,kst):
            if m!=2: continue
            vk=[pair_speed(nm,U,kst,d,E) for d in DX]
            if np.any(np.isnan(vk)) or min(vk)<1e-3: continue
            nweyl+=1
            rec={"link":nm,"U":un,"E":round(float(E),5),"v*":float(np.mean(vk)),"aniso*":float(np.ptp(vk))}
            okD=True
            for lab in ("D+x","D-x"):
                k0=pts[lab]
                ee=np.abs(wrap(np.angle(np.linalg.eigvals(get(nm,k0)@U))-E))
                mult=int(np.sum(ee<1e-7))
                vs=[pair_speed(nm,U,k0,d,E) for d in DX] if mult==2 else [np.nan]*6
                rec[lab]=(mult,vs)
            res.append(rec)
print(f"{nweyl} (step, node) pairs with a Weyl doublet at k*  [{time.time()-t0:.0f}s]")
def score(r,mode='both'):
    best=np.inf
    for lab in ("D+x","D-x"):
        m,vs=r[lab]
        if not weyl_ok(m,vs): continue
        va,vt=vs[0],0.5*(vs[1]+vs[2])
        best=min(best,max(abs(va-vt),abs(va-r["v*"]),abs(vt-r["v*"])) if mode=="both" else abs(va-vt))
    return best
def weyl_ok(m,vs):
    """isolated 2-fold, nonzero speed in all six directions, and the uniaxial (D4) form:
    v_y = v_z and v(yz)^2 = v_t^2, v(xy)^2 = (v_a^2+v_t^2)/2 to 1e-4."""
    if m!=2 or np.any(np.isnan(vs)) or min(vs)<1e-3: return False
    va,vt=vs[0],vs[1]
    return abs(vs[1]-vs[2])<1e-4 and abs(vs[3]-vt)<1e-4 and abs(vs[4]**2-(va**2+vt**2)/2)<1e-4
doub=[r for r in res if any(weyl_ok(*r[l]) for l in ("D+x","D-x"))]
print(f"{len(doub)} of them have a uniaxial Weyl doublet (nonzero speeds, D4 form) at the node quasi-energy at k*+pi e_x or -k*+pi e_x")
nz=sum(1 for r in res for l in ("D+x","D-x") if r[l][0]==2 and not weyl_ok(*r[l]))
print(f"{nz} doubler doublets at the node quasi-energy fail the Weyl test (a zero or non-uniaxial speed: not linear Weyl cones)")
vals=sorted({(round(r[l][1][0],4),round(r[l][1][1],4)) for r in doub for l in ("D+x","D-x") if weyl_ok(*r[l])})
print(f"distinct (v_axial, v_transverse) doubler pairs: {len(vals)}:",vals)
iso=sorted(doub,key=lambda r: score(r,'iso'))[0]
print("most isotropic doubler regardless of speed:",iso['link'],iso['U'],"E",iso['E'],"|v_a-v_t| =",round(score(iso,'iso'),5))
mults={}
for r in res:
    key=(r["D+x"][0],r["D-x"][0]); mults[key]=mults.get(key,0)+1
print("multiplicity at node E at (k*+pi ex, -k*+pi ex):",dict(sorted(mults.items())))
doub.sort(key=score)
print("best 12 by max(|v_ax-v_tr|,|v_ax-v*|,|v_tr-v*|) (coarse q=1e-4):")
for r in doub[:12]:
    print(f"  {r['link']:5s} {r['U']:12s} E={r['E']:+.4f} v*={r['v*']:.5f}  D+x {r['D+x'][0]} {np.round(r['D+x'][1],4)}  D-x {r['D-x'][0]} {np.round(r['D-x'][1],4)}  score {score(r):.4f}")
vstars=sorted(set(round(r['v*'],5) for r in res)); print("distinct k* speeds:",vstars[:20])
pickle.dump(res,open('doubler_iso_scan.pkl','wb'))
# refinement of the best few: Richardson-extrapolated speeds along x, y, z, yz-diagonal
def parse(un):
    U=np.eye(12,dtype=complex)
    for part in un.split("*"):
        U=U@(UHf(int(part[1]),int(part[2])) if part[0]=="H" else ULf(int(part[1]),int(part[2]),int(part[3])))
    return U
def speed_ref(W,k0,d,E):
    vals=[]
    for qq in (2e-3,1e-3):
        s=[]
        for sg in (1,-1):
            ee=wrap(np.angle(np.linalg.eigvals(W(k0+sg*qq*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); s.append((ee[-1]-ee[0])/(2*qq))
        vals.append(np.mean(s))
    return (4*vals[1]-vals[0])/3
print("refined (Richardson) speeds of the best 5:")
best_ref=[]
for r in doub[:5]:
    U=parse(r["U"]); W=lambda k,f=links[r["link"]],U=U: f(k)@U
    out={}
    for lab in ("k*","D+x","D-x"):
        if lab!="k*" and not weyl_ok(*r[lab]): continue
        out[lab]=[speed_ref(W,pts[lab],d,r["E"]) for d in DX[:4]]
    best_ref.append((r["link"],r["U"],out))
    print(" ",r["link"],r["U"],{k:np.round(v,6) for k,v in out.items()})
# checks
PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
ref8=[x for x in res if x["link"]=="S.RL" and x["U"]=="H23*L110"]
check("the scan contains the eight-node step S.R_L.H23.L110 and reproduces its uniaxial doublers (0.2467 axial, 0.5838 transverse)",
      any(x["D+x"][0]==2 and abs(x["D+x"][1][0]-0.2467)<1e-3 and abs(x["D+x"][1][1]-0.5838)<1e-3 for x in ref8),
      str([(x["E"],np.round(x["D+x"][1][:3],4)) for x in ref8]))
check("every k* Weyl doublet in the scanned families has the speed sqrt2/3 (O-forced isotropy)",
      all(abs(x["v*"]-np.sqrt(2)/3)<1e-5 and x["aniso*"]<1e-5 for x in res), f"{len(res)} nodes")
sc=score(doub[0]) if doub else np.inf
check("no scanned step has isotropic doublers at the k* speed (best score > 0.01; a negative search result, not a no-go)", sc>0.01, f"best score {sc:.4f}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
