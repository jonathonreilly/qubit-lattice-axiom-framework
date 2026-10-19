#!/usr/bin/env python3
"""B12 independent check, part 2: exact single-plaquette (d=2) Wilson character coefficients by direct
Weyl-integration (periodic trapezoid on the eigenphase torus; spectrally accurate), NOT Bessel determinants.
a_lam(beta) = <chi_lam>/d_lam under exp((beta/N) Re tr U).  tau_eff := -log a_F / C_F = (N/beta)(1 + k/beta + ...).
Checks k = (N^2-2)/4; Casimir-scaling residue beta^3[log a_lam - (C2/CF) log a_F] vs (9/4)(C2^2 - C2 CF) (SU(3));
and the repo multiplier: d_lam a_lam = beta^{3/2}[W + W2/beta] + O(beta^{1/2-2})."""
import itertools, math, numpy as np
FAIL=[]
def chk(n,ok,d=""):
    print(("PASS" if ok else "FAIL")+": "+n+" "+d); (None if ok else FAIL.append(n))
def alt(lam,ph):  # Vandermonde-type alternant det[e^{i l_j phi_k}] over a grid; ph shape (N, M)
    N=len(lam); A=np.exp(1j*np.einsum('j,km->jkm',np.array(lam,float),ph))
    return np.linalg.det(np.moveaxis(A,2,0))
def coeffs(N,beta,lams,M):
    g=2*np.pi*np.arange(M)/M - np.pi
    grids=np.meshgrid(*([g]*(N-1)),indexing='ij'); ph=np.array([x.ravel() for x in grids]); ph=np.vstack([ph,-ph.sum(0)])
    w=np.exp((beta/N)*(np.cos(ph).sum(0)-N))
    rho=list(range(N-1,-1,-1)); D0=alt(rho,ph); Z=np.sum(w*np.abs(D0)**2)
    out={}
    for lam in lams:
        dim=np.prod([ (lam[i]-lam[j]+j-i)/(j-i) for i in range(N) for j in range(i+1,N)])
        out[lam]=(np.sum(w*alt([l+r for l,r in zip(lam,rho)],ph)*np.conj(D0)).real/Z/dim, dim)
    return out
def C2(lam,N):
    s=sum(l*(l+N+1-2*(j+1)) for j,l in enumerate(lam)); return 0.5*(s-sum(lam)**2/N)
def rich(xs):  # betas doubling, model x0 + a/beta + b/beta^2
    r1=[2*xs[i+1]-xs[i] for i in range(len(xs)-1)]; return [(4*r1[i+1]-r1[i])/3 for i in range(len(r1)-1)]
# --- k for N=2,3,4
for N,betas,Ms in ((2,(200,400,800,1600),(2048,)), (3,(200,400,800,1600),(700,1000)), (4,(100,200,400),(140,180))):
    F=(1,)+(0,)*(N-1); CF=(N*N-1)/(2*N); ks={}
    for M in Ms:
        kk=[]
        for b in betas:
            if N==4 and b>200 and M<180: kk.append(np.nan); continue
            aF=coeffs(N,b,[F],M)[F][0]; tau=-math.log(aF)/CF; kk.append(b*(tau*b/N-1))
        ks[M]=kk
    kk=ks[Ms[-1]]
    if N==4:  # 3 betas -> one Richardson-2 value
        r=rich(kk); est=r[-1]
    else: est=rich(kk)[-1]
    print(f"   SU({N}) raw k(beta)={['%.5f'%x for x in kk]}  M-stability={[ '%.2e'%abs(a-b) for a,b in zip(ks[Ms[0]],ks[Ms[-1]]) if not np.isnan(a)] if len(Ms)>1 else '-'}")
    chk(f"SU({N}) d=2 k -> (N^2-2)/4 = {(N*N-2)/4}",abs(est-(N*N-2)/4)<5e-3,f"Richardson {est:.6f}")
# --- SU(3) Casimir-scaling residue and repo multiplier
N=3; CF=4/3
reps={"8":(2,1,0),"6":(2,0,0),"10":(3,0,0),"27":(4,2,0)}
F=(1,0,0); betas=(200,400,800,1600); res={k:[] for k in reps}; mult=[]
for b in betas:
    co=coeffs(3,b,[F]+list(reps.values()),1000)
    for nm,l in reps.items():
        res[nm].append(b**3*(math.log(co[l][0])-C2(l,3)/CF*math.log(co[F][0])))
    # repo multiplier at rep (p,q) Dynkin: x=(p+1)/sqrt(b), y=(q+1)/sqrt(b)
    for l in [F]+list(reps.values()):
        p,q=l[0]-l[1],l[1]-l[2]; x,y=(p+1)/math.sqrt(b),(q+1)/math.sqrt(b)
        Q=x*x+x*y+y*y; H=x*y*(x+y)/2; W=H*math.exp(-Q); W2=(3-7*Q/4+Q*Q/4)*W
        v=b**-1.5*co[l][1]*co[l][0]
        mult.append((b,l,b*b*(v-W-W2/b)/W, b*(v-W)/W - W2/W))
for nm,l in reps.items():
    c2=C2(l,3); pred=9/4*(c2*c2-c2*CF); r=rich(res[nm])
    print(f"   rep {nm}: beta^3 r = {['%.3f'%x for x in res[nm]]}, Richardson {r[-1]:.4f}, pred (9/4)(C2^2-C2 CF)={pred:.3f}")
    chk(f"SU(3) 2D residue rep {nm} -> {pred}",abs(r[-1]-pred)<0.02*pred)
for b in betas:
    worst=max(abs(m[2]) for m in mult if m[0]==b); worst1=max(abs(m[3]) for m in mult if m[0]==b)
    print(f"   beta={b}: max_lam |beta(v-W)/W - W2/W| = {worst1:.4f};  max beta^2|v-W-W2/beta|/W = {worst:.3f}")
chk("repo W2 = (3-7Q/4+Q^2/4)W reproduced to O(1/beta) by Weyl integration", max(abs(m[3]) for m in mult if m[0]==1600) < 4*max(abs(m[3]) for m in mult if m[0]==800)/2+1e-9 and max(abs(m[3]) for m in mult if m[0]==1600)<0.05)
print("SUMMARY:", "ALL PASS" if not FAIL else FAIL)
