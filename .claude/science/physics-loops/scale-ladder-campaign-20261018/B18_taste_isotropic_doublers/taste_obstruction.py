#!/usr/bin/env python3
"""B18 part 1: taste-like unitaries T = (-1)^{e.x} V(k) for the corner-model step ingredients and
for the eight-node step Ws = S.R_L.U_H.U_L.  Supplied model only (corner fermion, L=4 torus
gauge, Bloch blocks exact in infinite volume).  Prints PASS/FAIL and TOTAL.
Claims checked: (a) S admits an intertwiner S(k) -> w S(k+pi e) only for e in {0,(1,1,1)};
(b) H_link admits diagonal on-site tastes for every e, but none that also commutes with H_on or
(anti)commutes with Lambda; (c) orbit-stabiliser: k* has little group O, k*+pi e_x only D4, so
no T normalising the gauge-dressed rotation group maps one to the other; with the H_link tastes
adjoined, the enlarged group's little group at k*+pi e_x acts on q as all of O; (d) the eight-node
step has no taste of any form mapping k* -> k*+pi e_x (spectra differ; velocity determinants
differ); (e) the same spectral test over all B1 Clifford-phase steps."""
import time
exec(open('b18lib.py').read())
t0=time.time()
PASS=FAIL=0
def check(name,ok,detail=""):
    global PASS,FAIL; PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}",flush=True)
PIV=[np.array(v) for v in itertools.product((0,1),repeat=3) if any(v)]
OM=[1,-1,1j,-1j]
def dims(bl):
    return {(tuple(e),om):len(intertwiners(bl,shifted(bl,e,om),r=0)[0]) for e in PIV for om in OM}
# (a) S
FC=[tuple(int(x) for x in np.add(*[np.array(d) for d in c])) for c in C.CORNERS]   # face diagonal d+e of each corner
diagS=all(np.allclose(SK(k),np.diag(np.diag(SK(k)))) for k in np.random.default_rng(1).uniform(-np.pi,np.pi,(4,3)))
expo_ok=all(np.isclose(abs(SK(np.zeros(3))[i,i]),1) and set(blS)=={f for f in FC} for i in range(12))
sign_const={tuple(e):len({(-1)**int(np.dot(e,f)) for f in FC})==1 for e in PIV}
dS=dims(blS)
okS=[tuple(e) for e in PIV if any(dS[(tuple(e),om)] and generic_invertible(intertwiners(blS,shifted(blS,e,om))[0])>1e-6 for om in OM)]
check("(a) S(k) = diag(sigma_c e^{i k.(d_c+e_c)}) over the 12 distinct face diagonals; an invertible on-site intertwiner "
      "V S(k) = w S(k+pi e) V exists only for e=(1,1,1), w=1 (the exact proof extends this to any continuous V(k), any constant w)",
      diagS and expo_ok and okS==[(1,1,1)] and [e for e,v in sign_const.items() if v]==[(1,1,1)],
      f"invertible intertwiners for e in {okS}; null-space dims for e=(1,0,0): {[dS[((1,0,0),om)] for om in OM]}")
# (b) H_link
dL=dims(blli)
taste={}
for i in range(3):
    ei=tuple(int(x) for x in EX[i]); taste[i]=np.diag([(-1.0)**(ei in c) for c in C.CORNERS])
okL=all(np.allclose(taste[i]@HL(k)@taste[i],HL(k+np.pi*EX[i])) for i in range(3) for k in np.random.default_rng(2).uniform(-np.pi,np.pi,(3,3)))
planes=[[i for i,c in enumerate(C.CORNERS) if {abs(x) for d in c for x in d if x}=={1} and set(np.nonzero(np.abs(np.add(*[np.array(d) for d in c])))[0])==set(p)] for p in ((0,1),(0,2),(1,2))]
comm0=intertwiners(blli,blli,r=0)[0]
okplanes=len(comm0)==3 and all(np.allclose(np.abs(b[(0,0,0)]),np.diag(np.diag(np.abs(b[(0,0,0)])))) for b in comm0)
check("(b1) H_link preserves the plane of each corner (commutant = 3 plane projectors) and has the diagonal tastes "
      "V_i = diag((-1)^[+e_i in c]): V_i H_link(k) V_i = H_link(k+pi e_i); intertwiner spaces are 3-dim for every e and w=+-1",
      okL and okplanes and all(dL[(tuple(e),om)]==3 for e in PIV for om in (1,-1)) and all(dL[(tuple(e),om)]==0 for e in PIV for om in (1j,-1j)),
      f"plane sizes {[len(p) for p in planes]}")
def comm_basis(ops):
    I=np.eye(12); M=np.vstack([np.kron(A.T,I)-w*np.kron(I,A) for A,w in ops]); _,s,Vh=np.linalg.svd(M); s=np.concatenate([s,np.zeros(144-len(s))])
    return [v.conj().reshape(12,12,order='F') for v in Vh[s<1e-9]]
joint={}
for e in PIV:
    for wL in (1,-1):
        for nm,ops in (("H_on",[(Hon0,1)]),("Lam+",[(Lam,1)]),("Lam-",[(Lam,-1)])):
            joint[(tuple(e),wL,nm)]=len(intertwiners(blli,shifted(blli,e,wL),r=0,basis=comm_basis(ops))[0])
nz=[k for k,v in joint.items() if v and k[0]!=(1,1,1)]
check("(b2) no on-site V intertwines H_link(k) -> +-H_link(k+pi e) for e != 0,(1,1,1) while commuting with H_on, or "
      "commuting/anticommuting with Lambda (range-1 V(k) also excluded for e = e_x: probe3.log)",
      not nz, f"nonzero joint spaces: {nz}; e=(1,1,1): {[(k[1],k[2],v) for k,v in joint.items() if k[0]==(1,1,1)]}")
# real-space confirmation on the L=4 torus
xs=np.array([v[0] for v,c in C.VERTS]); Treal=[np.diag([(-1.0)**v[i]*taste[i][CI[c],CI[c]] for v,c in C.VERTS]) for i in range(3)]
Sr2=Sreal@Sreal; Hl=H0(0.0,1.0); Ho=H0(1.0,0.0)
LamR=np.zeros((nV,nV),complex)
for v in TV:
    idx=[C.VID[(v,c)] for c in C.CORNERS]; LamR[np.ix_(idx,idx)]=Lam
okR=(all(np.allclose(T@Hl@T,Hl) for T in Treal) and all(np.allclose(T@Sr2@T,Sr2) for T in Treal)
     and not any(np.allclose(T@Ho@T,Ho) for T in Treal) and not any(np.allclose(T@Sreal@T,Sreal) for T in Treal)
     and not any(np.allclose(T@LamR@T,s*LamR) for T in Treal for s in (1,-1)))
TT=[np.allclose(Treal[i]@Treal[j],Treal[j]@Treal[i]) for i in range(3) for j in range(3)]
check("(b3) real space (L=4 torus, gauge signs included): T_i = (-1)^{x_i} V_i commutes with the link hopping and with S^2, "
      "not with H_on, Lambda or S; the T_i mutually commute (abelian Z2^3, unlike the Clifford-type staggered tastes)",
      okR and all(TT))
# (c) orbit-stabiliser and the enlarged group
KS=[np.array(t)*2*np.pi/L for t in TV]
def Bloch(k):
    B=np.zeros((nV,12),complex)
    for a,(v,c) in enumerate(C.VERTS): B[a,CI[c]]=np.exp(1j*np.dot(k,v))/np.sqrt(L**3)
    return B
BK=[Bloch(k) for k in KS]
def kidx(k): return [i for i,q in enumerate(KS) if np.allclose(np.exp(1j*(q-k)),1)][0]
def mom_map(M):
    out={}
    for i in range(64):
        w=[np.linalg.norm(BK[j].conj().T@M@BK[i]) for j in range(64)]; j=int(np.argmax(w))
        assert abs(w[j]-np.sqrt(12))<1e-8; out[i]=j
    return out
Rm=[]
for P,s_ in rots:
    M=np.zeros((nV,nV)); M[P,np.arange(nV)]=(-1.0)**s_; Rm.append(M)
i0=kidx(kst); ix=kidx(kst+np.pi*EX[0])
rmaps=[mom_map(M) for M in Rm]
stab0=[r for r in range(24) if rmaps[r][i0]==i0]; stabx=[r for r in range(24) if rmaps[r][ix]==ix]
check("(c1) under the gauge-dressed rotations k* has little group O (24) and k*+pi e_x only D4 (8): no operator normalising "
      "this group (with the translations) maps k* to k*+pi e_x (conjugation would carry Stab(k*) onto Stab(k*+pi e_x))",
      len(stab0)==24 and len(stabx)==8, f"|Stab(k*)|={len(stab0)}, |Stab(k*+pi e_x)|={len(stabx)}")
tmaps=[mom_map(T) for T in Treal]
# enlarged group G' = <rotations, T_i>: its elements g = (product of T's) * R act on k as k -> R k + pi s_R + pi e
# little group of k*+pi e_x in G': for each R in O find a T-product t with t R (k*+pi e_x) = k*+pi e_x
Tprod={}
for bits in itertools.product((0,1),repeat=3):
    M=np.eye(nV)
    for i,b in enumerate(bits):
        if b: M=M@Treal[i]
    Tprod[bits]=(M,mom_map(M))
enl=0
for r in range(24):
    j=rmaps[r][ix]
    if any(tm[j]==ix for _,tm in Tprod.values()): enl+=1
# H_link commutes with every element of G'; and qualitatively the conjugated group T_x O T_x^-1 acts on q as O itself
commG=all(np.allclose(M@Hl@M.T,Hl) for M in Rm)
check("(c2) adjoining the H_link tastes T_i: every rotation R in O, composed with a T-product, fixes k*+pi e_x, so the little "
      "group of k*+pi e_x in G' = <PSG, T_i> acts on q through all of O (isotropy forced for any operator commuting with G')",
      enl==24 and commG, f"{enl}/24 rotations lift into Stab_G'(k*+pi e_x)")
# (d) the eight-node step
rng=np.random.default_rng(7)
def spec(W,k): return np.sort(np.mod(np.angle(np.linalg.eigvals(W(k))),2*np.pi))
def match(a,b):
    """min over phi of the optimal multiset distance between b and a+phi (mod 2pi)."""
    best=np.inf
    for j in range(len(a)):
        phi=b[0]-a[j]; c=np.sort(np.mod(a+phi,2*np.pi))
        d=min(np.max(np.abs(wrap(np.roll(c,s)-b))) for s in range(len(c))); best=min(best,d)
    return best
maps={"k->k+pi ex, E->E+phi":(lambda k: k+np.pi*EX[0],1),"k->k+pi ex, E->-E+phi":(lambda k: k+np.pi*EX[0],-1),
      "k->-k+pi ex, E->E+phi":(lambda k: -k+np.pi*EX[0],1),"k->-k+pi ex, E->-E+phi":(lambda k: -k+np.pi*EX[0],-1)}
KR=rng.uniform(-np.pi,np.pi,(6,3))
md={nm:max(match(sg*spec(Ws,k),spec(Ws,f(k))) for k in KR) for nm,(f,sg) in maps.items()}
# control: the Q=(pi,pi,pi) shift is a genuine symmetry (S(k+Q)=S(k), R_L(k+Q) ~ R_L(k) up to an on-site V?)
mdQ=max(match(spec(Ws,k),spec(Ws,k+np.pi*np.ones(3))) for k in KR)
check("(d1) the eight-node step: for each momentum map k -> +-k + pi e_x (all 48 point-group maps reduce to these, the step "
      "being O-symmetric) the eigenphase spectra at k and its image are NOT related by E -> +-E + phi for any phi",
      min(md.values())>1e-2, "worst-case mismatch over 6 random k: "+", ".join(f"{k}: {v:.3f}" for k,v in md.items())+f"; control Q-shift mismatch {mdQ:.2e}")
E0=[E for E,m in levels(Ws,kst) if m==2]
def vel(k0,d,E):
    vals=[]
    for qq in (2e-3,1e-3):
        s=[]
        for sg in (1,-1):
            ee=wrap(np.angle(np.linalg.eigvals(Ws(k0+sg*qq*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); s.append((ee[-1]-ee[0])/(2*qq))
        vals.append(np.mean(s))
    return (4*vals[1]-vals[0])/3
# pick the node E reached at all eight cube points
Enode=[E for E in E0 if all(np.sum(np.abs(wrap(np.angle(np.linalg.eigvals(Ws(c)))-E))<1e-7)==2 for c in CUBE)][0]
vst=vel(kst,EX[0],Enode); va=vel(kst+np.pi*EX[0],EX[0],Enode); vt=vel(kst+np.pi*EX[0],EX[1],Enode); vt2=vel(kst+np.pi*EX[0],EX[2],Enode)
vam=vel(-kst+np.pi*EX[0],EX[0],Enode); vtm=vel(-kst+np.pi*EX[0],EX[1],Enode)
det_k=vst**3; det_d=va*vt*vt2
check("(d2) cones at the node quasi-energy: k* isotropic at sqrt2/3; k*+pi e_x and -k*+pi e_x uniaxial; the velocity "
      "determinants differ, so no translation-covariant (anti)unitary with ANY lattice-automorphism momentum map "
      "k -> Mk + pi e (M in GL(3,Z)) can carry the k* cone onto a doubler cone",
      abs(vst-np.sqrt(2)/3)<1e-6 and abs(vt-vt2)<1e-6 and abs(det_k-det_d)>1e-3,
      f"E={Enode:.4f}; v*={vst:.6f}; D(+x): v_ax={va:.6f}, v_tr={vt:.6f}; D(-x): v_ax={vam:.6f}, v_tr={vtm:.6f}; "
      f"det v*^3={det_k:.6f} vs v_ax v_tr^2={det_d:.6f}")
# (e) family-wide spectral test over the B1 Clifford-phase steps
onH=[(f"H{a}{b}",UHf(a,b)) for a,b in itertools.product(range(4),repeat=2)]
onL=[(f"L{a}{b}{c}",ULf(a,b,c)) for a,b,c in itertools.product(range(4),repeat=3)]
cands=onH+onL+[(h[0]+"*"+l[0],h[1]@l[1]) for h in onH for l in onL]+[(l[0]+"*"+h[0],l[1]@h[1]) for h in onH for l in onL]
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
KR3=rng.uniform(-np.pi,np.pi,(2,3))
pre={nm:{tuple(np.round(k,12)):f(k) for k0 in KR3 for k in (k0,k0+np.pi*EX[0],-k0+np.pi*EX[0])} for nm,f in links.items()}
def sp(M): return np.sort(np.mod(np.angle(np.linalg.eigvals(M)),2*np.pi))
def quick(a,b):   # cheap necessary test: sorted gaps must agree up to cyclic order (E -> E+phi) or reversal (E -> -E+phi)
    ga=np.diff(np.concatenate([a,[a[0]+2*np.pi]])); gb=np.diff(np.concatenate([b,[b[0]+2*np.pi]]))
    return min(np.max(np.abs(np.roll(ga,s)-gb)) for s in range(12)), min(np.max(np.abs(np.roll(ga[::-1],s)-gb)) for s in range(12))
survivors=[]; ntest=0
for nm in links:
    for un,U in cands:
        ntest+=1; alive=False
        for f in (lambda k: k+np.pi*EX[0], lambda k: -k+np.pi*EX[0]):
            ok=True
            for k0 in KR3:
                a=sp(pre[nm][tuple(np.round(k0,12))]@U); b=sp(pre[nm][tuple(np.round(f(k0),12))]@U)
                if min(quick(a,b))>1e-6: ok=False; break
            alive|=ok
        if alive: survivors.append((nm,un))
check("(e) family-wide: among all S.U, S.R_L.U, R_L.S.U Clifford-phase steps (B1 family), none passes the necessary spectral "
      "test for a taste k -> +-k + pi e_x (with E -> +-E + phi)", not survivors, f"{ntest} steps tested; survivors {survivors[:5]}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
