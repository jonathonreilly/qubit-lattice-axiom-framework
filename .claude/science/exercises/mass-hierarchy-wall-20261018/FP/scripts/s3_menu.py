# S3: exact residual-symmetry mixing menu for the lattice image groups on a generation triplet.
# B3 = signed perms (star placement, scalar modes; also = O(T1) x {+-1} for internal T1 placement).
# S3 = plain perms (internal axis-permutation placement A1+E, V4 acting trivially).
import itertools, numpy as np
rng=np.random.default_rng(1)
def perms(signed):
    out=[]
    for p in itertools.permutations(range(3)):
        for s in (itertools.product([1,-1],repeat=3) if signed else [(1,1,1)]):
            M=np.zeros((3,3));
            for i in range(3): M[p[i],i]=s[i]
            out.append(M)
    return out
def is_scalar(g): return np.allclose(g,g[0,0]*np.eye(3))
def joint_basis(gs):
    # eigenbasis of a generic combination of commuting unitaries; return None if degenerate
    C=sum(complex(*rng.normal(size=2))*g for g in gs)
    w,V=np.linalg.eig(C)
    if min(abs(w[i]-w[j]) for i in range(3) for j in range(i+1,3))<1e-6: return None
    V=V/np.linalg.norm(V,axis=0); return V
def unique_eigvec(g):
    w,V=np.linalg.eig(g); w=np.round(w,8)
    vals,counts=np.unique(w,return_counts=True)
    if len(vals)==2 and min(counts)==1:
        v=V[:,list(w).index(vals[counts==1][0])]; return v/np.linalg.norm(v)
    return None
def canon(P):
    P=np.round(P,6); best=None
    for r in itertools.permutations(range(3)):
        for c in itertools.permutations(range(3)):
            t=tuple(P[list(r)][:,list(c)].ravel())
            best=t if best is None or t<best else best
    return best
def canon_col(v): return tuple(sorted(np.round(v,6)))
def menu(G,label):
    # Dirac residuals: cyclic and 2-generated abelian subgroups with nondegenerate joint spectrum
    dirac=[]
    for g in G:
        if is_scalar(g): continue
        B=joint_basis([g]); 
        if B is not None: dirac.append(B)
    for g,h in itertools.combinations(G,2):
        if np.allclose(g@h,h@g) and not is_scalar(g) and not is_scalar(h):
            B=joint_basis([g,h])
            if B is not None: dirac.append(B)
    # Majorana residuals: order-2 elements (single Z2 -> one column) and commuting pairs (Klein -> full)
    inv=[g for g in G if np.allclose(g@g,np.eye(3)) and not is_scalar(g)]
    col=[v for v in (unique_eigvec(g) for g in inv) if v is not None]
    klein=[B for g,h in itertools.combinations(inv,2) if np.allclose(g@h,h@g) for B in [joint_basis([g,h])] if B is not None]
    full_dd=sorted({canon(np.abs(Bl.conj().T@Bn)**2) for Bl in dirac for Bn in dirac})
    full_dm=sorted({canon(np.abs(Bl.conj().T@Bn)**2) for Bl in dirac for Bn in klein})
    cols=sorted({canon_col(np.abs(Bl.conj().T@v)**2) for Bl in dirac for v in col})
    print(f"== {label}: |G|={len(G)}, Dirac residual bases={len(dirac)}, Z2 columns={len(col)}, Klein bases={len(klein)}")
    print(" Dirac x Dirac full |V|^2 patterns (sorted canonical):")
    for p in full_dd: print("   ",np.array(p).reshape(3,3).round(4).tolist())
    print(" Dirac x Klein full |U|^2 patterns:")
    for p in full_dm: print("   ",np.array(p).reshape(3,3).round(4).tolist())
    print(" Dirac x Z2 fixed-column patterns (sorted entries):",[tuple(round(x,4) for x in c) for c in cols])
    return full_dd,full_dm,cols
B3=perms(True); S3=perms(False)
r_B=menu(B3,"B3 (star placement / internal T1)")
r_S=menu(S3,"S3 (internal axis-permutation A1+E)")
# --- data tests ---
def U_pmns(s12,s13,s23,d):
    c12,c13,c23=np.sqrt(1-s12),np.sqrt(1-s13),np.sqrt(1-s23); s12,s13,s23=np.sqrt(s12),np.sqrt(s13),np.sqrt(s23); e=np.exp(1j*d)
    return np.array([[c12*c13,s12*c13,s13/e],[-s12*c23-c12*s23*s13*e,c12*c23-s12*s23*s13*e,s23*c13],[s12*s23-c12*c23*s13*e,-c12*s23-s12*c23*s13*e,c23*c13]])
# comparator ranges (3 sigma): s12^2 NuFIT-6.1 as quoted on main [0.2893,0.3295]; s13^2 [0.0203,0.02388]; s23^2 [0.435,0.585]; delta free
grid=[(a,b,c,d) for a in np.linspace(0.2893,0.3295,21) for b in np.linspace(0.0203,0.02388,7) for c in np.linspace(0.435,0.585,31) for d in np.linspace(0,2*np.pi,73)]
def col_fit(col):
    best=9
    for (a,b,c,d) in grid:
        P=np.abs(U_pmns(a,b,c,d))**2
        for j in range(3):
            for r in itertools.permutations(range(3)):
                best=min(best,max(abs(P[list(r),j]-np.array(col))))
    return best
print("== PMNS fixed-column tests (min over 3-sigma box of max |dev|; grid step ~2e-3):")
for label,res in [("B3",r_B),("S3",r_S)]:
    for col in res[2]:
        print(f"  {label} column {tuple(round(x,4) for x in col)}: {col_fit(col):.4f}")
# TM1 predictions
s13=0.02215; s12_tm1=1-2/(3*(1-s13)); print(f"TM1: s12^2 = 1 - 2/(3 c13^2) = {s12_tm1:.4f} at s13^2={s13}")
for s23 in [0.470,0.500,0.561]:
    c12,s12=np.sqrt(1-s12_tm1),np.sqrt(s12_tm1); c23,sn23=np.sqrt(1-s23),np.sqrt(s23); sn13=np.sqrt(s13)
    cd=(1/6-s12**2*c23**2-c12**2*sn23**2*sn13**2)/(2*s12*c12*sn23*c23*sn13)
    print(f"  s23^2={s23}: cos(delta) = {cd:.3f}  -> |delta| = {np.degrees(np.arccos(np.clip(cd,-1,1))):.1f} deg")
# CKM: PDG magnitudes; does any Dirac x Dirac pattern fit within x2 on every entry?
Vckm=np.array([[0.97435,0.22501,0.003732],[0.22487,0.97349,0.04183],[0.00858,0.04111,0.999118]])**2
for label,res in [("B3",r_B),("S3",r_S)]:
    ok=[p for p in res[0] if any(np.all(np.abs(np.array(p).reshape(3,3)[list(r)][:,list(c)]-Vckm)<0.5*Vckm+1e-12) for r in itertools.permutations(range(3)) for c in itertools.permutations(range(3)))]
    print(f"CKM: {label} exact-residual patterns within x1.5 of every |V|^2 entry: {len(ok)}")
