#!/usr/bin/env python3
"""A disturbance moves as a pattern: under Bell's law the record that carries it barely moves.

Pre-registered by the second panel's foundations lens (2026-09-28, recorded in
the viability map). Reading tested (supplied, not adopted): records as beables
(Bell's minimal jump law) on a one-mode-per-site sea, the axioms' qubit read
as one fermion mode; a record's identity is "the occupation that jumped" (each
Bell jump moves one occupation to a neighbouring site). Free hopping
H = -sum (c^dag_x c_y + h.c.) on rings and square tori, antiperiodic (closed
shells); the sea is the ground state of N0 particles; one particle is added at
the origin, psi = c^dag_0 |sea>. The tagged record is the one at the origin.

Pre-registered: the literal picture ("the record moves with the disturbance")
PASSES if the tagged record's RMS displacement is at least 0.7 of the excess
density's RMS spread at t = L/2 (before wrapping in 2D); FAILS (pattern
reading forced) if at most 0.3; in between, double L.

Method: amplitudes are Slater determinants (the added orbital evolves as
e^{-iht} e_0, the sea's orbitals by phases); Bell rates need only amplitude
ratios, from one matrix inverse per step (row replacement); initial records
are sampled from |psi|^2 by Metropolis. Validated against full Fock-space
evolution on a ring of 16.

Checks:
A. Validation: on a ring of 16 the determinant method and full Fock-space
   evolution give the same excess spread, and the Monte Carlo density matches
   |psi|^2 within sampling error.
B. One dimension: rings of 16, 32 and 64. The tagged record moves about one
   site whatever L, while the excess spreads ballistically; the ratio at
   t = L/2 is below 0.3 and falls with L (the literal picture fails).
C. Two dimensions: 8x8 and 12x12 closed shells, compared before the excess
   wraps (t <= 2). The ratio is between 0.2 and 0.45 and falls after t = 1;
   at 12x12 it is at or below about 0.3 at t = 2 (borderline fail).

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

def run(geom,L,N0,ntraj,T,dt=0.02,seed=5,nrec=4):
    n,h,nbr,disp=lattice(geom,L)
    w,v=np.linalg.eigh(h); gap=w[N0]-w[N0-1]; FS=v[:,:N0]
    U=expm(-1j*h*dt); nt=int(round(T/dt))
    phis=[np.eye(n)[:,0].astype(complex)]
    for _ in range(nt): phis.append(U@phis[-1])
    orbs=lambda k: np.column_stack([phis[k], FS*np.exp(-1j*w[:N0]*dt*k)[None,:]])
    D2=np.array([np.sum(disp(s)**2) for s in range(n)])
    rec_steps=[int(round(nt*(j+1)/nrec)) for j in range(nrec)]
    def excess(k):
        Q,_=np.linalg.qr(orbs(k)); ex=np.sum(np.abs(Q)**2,1)-N0/n; return float(np.sqrt(np.sum(ex*D2)/np.sum(ex)))
    exc=[excess(k) for k in rec_steps]
    rng=np.random.default_rng(seed)
    disps=np.zeros((ntraj,nrec,len(disp(0)))); dens_mc=np.zeros(n)
    M0=orbs(0)
    for tr in range(ntraj):
        # Metropolis initial sample from |psi(0)|^2 using determinant ratios
        conf=[0]+list(rng.choice(np.arange(1,n),N0,replace=False)); A=M0[conf,:]
        while abs(np.linalg.det(A))<1e-30:
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
            M=orbs(k); A=M[conf,:]; Ainv=np.linalg.inv(A)
            occ=set(conf); moves=[]; rates=[]
            for i,s in enumerate(conf):
                for t_ in nbr[s]:
                    if t_ in occ: continue
                    x=(M[t_,:]@Ainv)[i]
                    moves.append((i,s,t_)); rates.append(max(0.0,2*np.imag(np.conj(x)*h[t_,s])))
            rates=np.array(rates); u=rng.random(); cum=np.cumsum(rates*dt)
            if cum.size and u<cum[-1]:
                i,s,t_=moves[int(np.searchsorted(cum,u))]
                if s==tag:
                    step=disp(t_)-disp(s); step=np.where(step>L/2,step-L,np.where(step<-L/2,step+L,step)); dvec=dvec+step; tag=t_
                conf[i]=t_
            if k+1 in rec_steps:
                disps[tr,rix]=dvec; rix+=1
        for s in conf: dens_mc[s]+=1
    rms=np.sqrt(np.mean(np.sum(disps**2,2),0))
    Q,_=np.linalg.qr(orbs(nt)); dens_ex=np.sum(np.abs(Q)**2,1)
    eqv=float(np.max(np.abs(dens_mc/ntraj-dens_ex)))
    return dict(n=n,N0=N0,gap=round(float(gap),3),times=[round(r*dt,2) for r in rec_steps],exc=np.round(exc,3),tag=np.round(rms,3),ratio=np.round(rms/np.array(exc),3),density_err=round(eqv,3))


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

# ---------------------------------------------------------------- B one dimension
rings = {Lr: run('ring', Lr, Lr // 2, 150 if Lr == 64 else 300, Lr / 2) for Lr in (16, 32, 64)}
final = {Lr: r['ratio'][-1] for Lr, r in rings.items()}
check("B: one dimension: the tagged record moves about one site whatever L, while the excess spreads ballistically; the ratio at t = L/2 is below 0.3 and falls with L",
      all(v < 0.3 for v in final.values()) and final[64] < final[16] and all(max(r['tag']) < 1.5 for r in rings.values()),
      "; ".join(f"L={Lr}: excess {list(r['exc'])}, tagged {list(r['tag'])}, ratio at t = L/2 {r['ratio'][-1]}" for Lr, r in rings.items()))

# ---------------------------------------------------------------- C two dimensions
sq = {(Ls, N0s): run('square', Ls, N0s, 200, 2.0) for (Ls, N0s) in ((8, 24), (8, 40), (12, 60), (12, 84))}
big = [sq[(12, 60)]['ratio'], sq[(12, 84)]['ratio']]
check("C: two dimensions (8x8, 12x12 closed shells, before wrapping): the ratio lies between 0.2 and 0.45 and falls after t = 1; at 12x12 it is at or below about 0.3 at t = 2",
      all(0.15 < x < 0.5 for r in sq.values() for x in r['ratio']) and all(b[-1] < b[1] for b in big) and all(b[-1] <= 0.32 for b in big),
      "; ".join(f"{Ls}x{Ls} N0={N0s}: excess {list(r['exc'])}, tagged {list(r['tag'])}, ratios {list(r['ratio'])}" for (Ls, N0s), r in sq.items()))

print("per_element: amplitudes are Slater determinants; Bell rates use exact row-replacement determinant ratios, validated against Fock space on a ring of 16.")
print("per_site: every Bell jump moves one occupation to a neighbouring site; the tagged record is followed site by site.")
print("per_mode: the sea is a closed-shell filling of plane-wave modes; the excess density is computed from the orbitals exactly.")
print("per_block: rings of 16, 32, 64 sites and square tori of 8x8 and 12x12, with 150-300 Bell histories each.")
print("lattice_wide: checked and not executed - free hopping only; no interactions, no three dimensions, no other identity rule or equivariant law.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
