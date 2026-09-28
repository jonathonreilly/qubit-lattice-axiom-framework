#!/usr/bin/env python3
"""Records as beables: which record carries a disturbance is a choice of identity.

Pre-registered by the second panel's foundations lens (2026-09-28, recorded in
the viability map). Reading tested (supplied, not adopted): records as beables
(Bell's minimal jump law) on a one-mode-per-site sea (the axioms' qubit read as
one fermion mode), free hopping H = -sum (c^dag_x c_y + h.c.), antiperiodic
closed shells; one particle added at the origin, psi = c^dag_0 |sea>. Bell's
law moves unlabelled occupations; a record's identity is an extra rule. Two
rules are compared on the same trajectories:
  - hop-following: the record that jumps keeps its identity (a nearest-neighbour
    process); the tagged record is the occupation at the origin at t = 0;
  - Laplace: at each time, occupation i carries the added particle with
    weight |A_i0 (A^-1)_0i|^2 (normalised), the squared terms of the Laplace
    expansion of the amplitude determinant along the added orbital's column
    (a per-time assignment; no nearest-neighbour process realising it is built
    here). The weights depend on how the added column is written: adding
    occupied orbitals to it leaves every amplitude unchanged but changes them.
    The canonical choice projects the added orbital off the sea.
Pre-registered: the literal picture ("the record moves with the disturbance")
passes if the tagged RMS displacement is >= 0.7 of the excess density's RMS
spread at the latest time before the excess wraps; fails if <= 0.3.

Method: Slater-determinant amplitudes; Bell rates from row-replacement ratios
(one inverse and one matrix product per step); initial records by Metropolis
(single-occupation moves to random sites, 40 n attempts from a random start,
one fresh chain per history). Validated against full Fock-space evolution on a
ring of 16.

Checks:
A. Validation against Fock space (excess spread) and equivariance (Monte
   Carlo density vs |psi|^2).
B. One dimension, hop-following: rings of 16, 32, 64 at half filling: the
   tagged record stays within about 1/(2 nu) sites while the excess spreads
   ballistically; the ratio at t = L/4 (before the first wrap) is below 0.3
   and falls with L.
C. Two dimensions, hop-following (dt = 0.005, with the fraction of steps whose
   total jump probability exceeds 0.5 reported): 8x8, 12x12, 16x16 closed
   shells up to t = L/4 (when the fastest front first reaches the seam): the
   ratio falls with time, to about 0.2 on 16x16 at t = 4 (bootstrap error
   given). The tagged record lags; the pre-registered 0.3 decision at the
   pre-registered time t = L/2 (after wrapping) is not made.
D. Identity decides it: on the same trajectories, at the latest time, the
   canonical Laplace identity's RMS displacement matches the excess spread
   (ratio 0.9-1.1) on a ring of 32 and on 12x12, where the hop-following
   ratio is below 0.35; and an altered representation of the same wave (the
   added column plus 10 times an occupied orbital) moves the Laplace ratio,
   so that identity is itself a choice.
E. Density: in a dilute ring (nu = 1/8) the hop-following record carries the
   disturbance further (about 1/(2 nu) sites), and the ratio is larger than at
   half filling.

Prints one line per check, the N5 resolution lines and TOTAL: PASS=N FAIL=M.
"""
import numpy as np, itertools
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply, eigsh
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


def lattice(geom,L):
    if geom=='ring':
        n=L; nbr=[[(x+1)%n,(x-1)%n] for x in range(n)]
        h=np.zeros((n,n),complex)
        for x in range(n):
            y=(x+1)%n; ph=-1.0 if x==n-1 else 1.0; h[x,y]+=-ph; h[y,x]+=-ph
        disp=lambda s: np.array([s-n if s>n/2 else s],float)
    else:
        n=L*L; h=np.zeros((n,n),complex); nbr=[[] for _ in range(n)]
        for x in range(L):
            for y in range(L):
                s=x*L+y
                for (xx,yy,wrap) in (((x+1)%L,y,x==L-1),(x,(y+1)%L,y==L-1)):
                    t_=xx*L+yy; ph=-1.0 if wrap else 1.0; h[s,t_]+=-ph; h[t_,s]+=-ph; nbr[s].append(t_); nbr[t_].append(s)
        def disp(s):
            x,y=divmod(s,L); return np.array([x-L if x>L/2 else x, y-L if y>L/2 else y],float)
    return n,h,nbr,disp

def build(sites, bonds, Np):
    confs=[c for c in itertools.combinations(range(sites),Np)]; idx={c:i for i,c in enumerate(confs)}
    rows=[];cols=[];vals=[];hop=[]
    for j,c in enumerate(confs):
        occ=set(c)
        for (a,b,phase) in bonds:   # hop amplitude -t*phase for c^dag_a c_b and h.c.
            for (p,q,ph) in ((a,b,phase),(b,a,np.conj(phase))):
                if q in occ and p not in occ:
                    s=(-1)**sum(1 for z in occ if z<q); occ2=occ-{q}; s*=(-1)**sum(1 for z in occ2 if z<p)
                    new=tuple(sorted(occ2|{p})); rows.append(idx[new]); cols.append(j); vals.append(-ph*s)
    H=sps.csr_matrix((vals,(rows,cols)),shape=(len(confs),)*2)
    return confs,idx,H

def run(geom,L,N0,ntraj,T,dt=0.02,seed=5,nrec=4,alt=False):
    n,h,nbr,disp=lattice(geom,L)
    w,v=np.linalg.eigh(h); gap=w[N0]-w[N0-1]; FS=v[:,:N0]
    U=expm(-1j*h*dt); nt=int(round(T/dt))
    phis=[np.eye(n)[:,0].astype(complex)]
    for _ in range(nt): phis.append(U@phis[-1])
    orbs=lambda k: np.column_stack([phis[k], FS*np.exp(-1j*w[:N0]*dt*k)[None,:]])
    Pun=np.eye(n)-FS@FS.conj().T                      # projector off the sea (unoccupied space)
    def lap_cols(k):                                  # Laplace representations of the added column (the determinant is the same for all)
        M=orbs(k); reps={'canonical':np.column_stack([Pun@phis[k],M[:,1:]])}
        if alt: reps['altered']=np.column_stack([Pun@phis[k]+10*M[:,1],M[:,1:]])
        return reps
    D2=np.array([np.sum(disp(s)**2) for s in range(n)])
    rec_steps=[int(round(nt*(j+1)/nrec)) for j in range(nrec)]
    def excess(k):
        Q,_=np.linalg.qr(orbs(k)); ex=np.sum(np.abs(Q)**2,1)-N0/n; return float(np.sqrt(np.sum(ex*D2)/np.sum(ex)))
    exc=[excess(k) for k in rec_steps]
    rng=np.random.default_rng(seed)
    disps=np.zeros((ntraj,nrec,len(disp(0)))); lap={'canonical':np.zeros((ntraj,nrec)),'altered':np.zeros((ntraj,nrec))}; dens_mc=np.zeros(n)
    big_steps=0; all_steps=0
    M0=orbs(0)
    for tr in range(ntraj):
        conf=[0]+list(rng.choice(np.arange(1,n),N0,replace=False)); A=M0[conf,:]
        while np.linalg.cond(A)>1e12:   # a well-conditioned start (determinants of large Slater matrices underflow harmlessly)
            conf=[0]+list(rng.choice(np.arange(1,n),N0,replace=False)); A=M0[conf,:]
        Ainv=np.linalg.inv(A)
        for _ in range(40*n):
            i=rng.integers(len(conf)); t_=rng.integers(n)
            if t_ in conf: continue
            x=(M0[t_,:]@Ainv)[i]
            if rng.random()<min(1.0,abs(x)**2):
                conf[i]=t_; A=M0[conf,:]; Ainv=np.linalg.inv(A)
        tag=0 if 0 in conf else conf[0]; dvec=np.zeros(len(disp(0))); rix=0
        for k in range(nt):
            M=orbs(k); A=M[conf,:]; Ainv=np.linalg.inv(A); X=M@Ainv
            occ=set(conf); moves=[]; rates=[]
            for i,s in enumerate(conf):
                for t_ in nbr[s]:
                    if t_ in occ: continue
                    moves.append((i,s,t_)); rates.append(max(0.0,2*np.imag(np.conj(X[t_,i])*h[t_,s])))
            rates=np.array(rates); u=rng.random(); cum=np.cumsum(rates*dt)
            all_steps+=1; big_steps+= (cum[-1]>0.5) if cum.size else 0
            if cum.size and u<cum[-1]:
                i,s,t_=moves[int(np.searchsorted(cum,u))]
                if s==tag:
                    step=disp(t_)-disp(s); step=np.where(step>L/2,step-L,np.where(step<-L/2,step+L,step)); dvec=dvec+step; tag=t_
                conf[i]=t_
            if k+1 in rec_steps:
                disps[tr,rix]=dvec
                for name,Mk in lap_cols(k+1).items():
                    Ak=Mk[conf,:]; Aik=np.linalg.inv(Ak)
                    wts=np.abs(Ak[:,0]*Aik[0,:])**2; wts/=wts.sum()          # normalised squared Laplace terms
                    lap[name][tr,rix]=np.sum(wts*D2[conf])
                rix+=1
        for s in conf: dens_mc[s]+=1
    rms=np.sqrt(np.mean(np.sum(disps**2,2),0)); lrms=np.sqrt(np.mean(lap['canonical'],0)); arms=np.sqrt(np.mean(lap['altered'],0))
    bs=[]
    for _ in range(200):                              # bootstrap over histories for the final ratio
        idx=rng.integers(ntraj,size=ntraj); bs.append(np.sqrt(np.mean(np.sum(disps[idx,-1]**2,1))))
    err_last=float(np.std(bs))
    Q,_=np.linalg.qr(orbs(nt)); dens_ex=np.sum(np.abs(Q)**2,1)
    eqv=float(np.max(np.abs(dens_mc/ntraj-dens_ex)))
    fl = lambda a: [round(float(x), 3) for x in a]
    return dict(n=n,N0=N0,gap=round(float(gap),3),dt=dt,times=[round(r*dt,2) for r in rec_steps],exc=fl(exc),tag=fl(rms),
                ratio=fl(rms/np.array(exc)),ratio_err=round(err_last/exc[-1],3),laplace=fl(lrms),lratio=fl(lrms/np.array(exc)),
                altered=fl(arms/np.array(exc)) if alt else None,big_step_frac=round(big_steps/max(all_steps,1),3),density_err=round(eqv,3))


# ---------------------------------------------------------------- A validation against Fock space
L = 16; n, h, nbr, disp = lattice('ring', L); N0 = 8
bonds = [(x, (x + 1) % L, (-1.0 if x == L - 1 else 1.0)) for x in range(L)]
c0, i0, H0 = build(L, bonds, N0); wv, vv = eigsh(H0, k=2, which='SA'); gs = vv[:, np.argmin(wv)]
confs, idx, H = build(L, bonds, N0 + 1)
psi0 = np.zeros(len(confs), complex)
for j, c in enumerate(c0):
    if 0 not in c:
        psi0[idx[tuple(sorted(c + (0,)))]] += gs[j]
psi0 /= np.linalg.norm(psi0)
psiT = expm_multiply(-1j * H, psi0, start=0, stop=4.0, num=2, endpoint=True)[-1]
occ = np.array([[1 if s in c else 0 for s in range(L)] for c in confs], float)
D2 = np.array([np.sum(disp(s) ** 2) for s in range(L)])
ex_f = (np.abs(psiT) ** 2) @ occ - N0 / L; spread_fock = np.sqrt(np.sum(ex_f * D2) / np.sum(ex_f))
r16 = run('ring', 16, 8, 300, 8.0)
check("A: the determinant method matches full Fock-space evolution (excess spread at t = 4) and the Monte Carlo density matches |psi|^2",
      abs(r16['exc'][1] - spread_fock) < 1e-3 and r16['density_err'] < 0.1,
      f"excess spread at t = 4: determinants {r16['exc'][1]:.4f}, Fock space {spread_fock:.4f}; largest density deviation {r16['density_err']:.3f} (300 histories)")

# ---------------------------------------------------------------- B one dimension, hop-following
rings = {Lr: run('ring', Lr, Lr // 2, 150 if Lr == 64 else 300, Lr / 4) for Lr in (16, 32, 64)}
final = {Lr: r['ratio'][-1] for Lr, r in rings.items()}
check("B: one dimension, hop-following: the tagged record stays within about 1/(2 nu) sites while the excess spreads ballistically; at t = L/4 the ratio is below 0.3 and falls with L",
      all(v < 0.3 for v in final.values()) and final[64] < final[16] and all(max(r['tag']) < 1.5 for r in rings.values()),
      "; ".join(f"L={Lr}: excess {list(r['exc'])}, tagged {list(r['tag'])}, ratio at t = L/4 {r['ratio'][-1]}" for Lr, r in rings.items()))

# ---------------------------------------------------------------- C two dimensions, hop-following
sq = {(8, 24): run('square', 8, 24, 200, 2.0, dt=0.005), (12, 60): run('square', 12, 60, 200, 3.0, dt=0.005, alt=True), (16, 104): run('square', 16, 104, 100, 4.0, dt=0.005)}
check("C: two dimensions, hop-following (dt = 0.005): up to t = L/4 (when the fastest front first reaches the seam) the ratio falls with time, to about 0.2 on 16x16 at t = 4; "
      "the tagged record lags (the pre-registered 0.3 line is not decided at the pre-registered time)",
      all(r['ratio'][-1] < r['ratio'][1] for r in sq.values()) and sq[(16, 104)]['ratio'][-1] + 2 * sq[(16, 104)]['ratio_err'] < 0.3,
      "; ".join(f"{Ls}x{Ls} N0={N0s}: times {r['times']}, excess {list(r['exc'])}, tagged {list(r['tag'])}, ratios {list(r['ratio'])} (+- {r['ratio_err']} at the end), steps with rate*dt > 0.5: {r['big_step_frac']}" for (Ls, N0s), r in sq.items()))

# ---------------------------------------------------------------- D identity decides it
lap32 = rings[32]['lratio']; lap12 = sq[(12, 60)]['lratio']; alt12 = sq[(12, 60)]['altered']
check("D: identity decides it: on the same trajectories, at the latest time, the canonical Laplace identity (added orbital projected off the sea) matches the excess spread (ratio 0.9-1.1) "
      "where hop-following is below 0.35; and the Laplace identity depends on how the wave is written (adding an occupied orbital to the added column, which leaves the wave unchanged, moves it)",
      0.9 <= lap32[-1] <= 1.1 and 0.9 <= lap12[-1] <= 1.1 and rings[32]['ratio'][-1] < 0.35 and sq[(12, 60)]['ratio'][-1] < 0.35 and abs(alt12[-1] - lap12[-1]) > 0.1,
      f"ring 32: canonical Laplace {list(lap32)}, hop-following {list(rings[32]['ratio'])}; 12x12: canonical Laplace {list(lap12)}, altered representation {list(alt12)}, hop-following {list(sq[(12, 60)]['ratio'])}")

# ---------------------------------------------------------------- E dilute sea
dil = run('ring', 64, 8, 150, 16.0)
check("E: in a dilute ring (nu = 1/8) the hop-following record carries the disturbance further (about 1/(2 nu) = 4 sites), and the ratio exceeds the half-filled ring's",
      2.5 < max(dil['tag']) < 6 and dil['ratio'][-1] > rings[64]['ratio'][-1],
      f"ring 64, 8 particles: excess {list(dil['exc'])}, tagged {list(dil['tag'])}, ratios {list(dil['ratio'])}; half filling ratio at t = 16: {rings[64]['ratio'][-1]}")

print("per_element: amplitudes are Slater determinants; Bell rates use exact row-replacement determinant ratios, validated against Fock space on a ring of 16.")
print("per_site: every Bell jump moves one occupation to a neighbouring site; the tagged record is followed site by site.")
print("per_mode: the sea is a closed-shell filling of plane-wave modes; the excess density is computed from the orbitals exactly.")
print("per_block: rings of 16, 32, 64 sites and square tori of 8x8, 12x12 and 16x16, with 100-300 Bell histories each.")
print("lattice_wide: checked and not executed - free hopping only; no interactions, no three dimensions; two identity rules and one equivariant law.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
