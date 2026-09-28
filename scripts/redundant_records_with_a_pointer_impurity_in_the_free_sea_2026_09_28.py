#!/usr/bin/env python3
"""Redundant records with a pointer: an impurity's bit in a free sea is carried by the whole, not copied.

Pre-registered by the second panel's strategy and foundations lenses
(2026-09-28, recorded in the viability map), as the fair version of the
first redundancy test (which had no pointer). Option A of the map: records
emerge as facts copied redundantly into the surroundings (reference only:
Zurek 2009; Riedel and Zurek 2010).

Setting: a ring of L one-mode sites (spinless fermions, free hopping,
antiperiodic, half filling) plus one impurity qubit. The coupling
g sigma_z(impurity) n_1 conserves the impurity's sigma_z (a pointer). The
impurity starts in (|0> + |1>)/sqrt 2, the sea in its ground state. Exact
evolution in the full Fock space.

Measures (bits): H(S) of the impurity; I(S:F) averaged over random sea
fragments of f sites; redundancy R_0.1 = L / f_min, where f_min is the smallest f
with I(S:F) >= 0.9 H(S); the predictability sieve (entropy of the impurity
started in a z or x eigenstate).

Pre-registered: PASS (option A lives in the free sea given a pointer) if
R_0.1 >= 3 at some t <= L/2 with the z basis preferred by >= 0.5 bit; FAIL
if R_0.1 < 2 at all t; otherwise in between. R = 2 is the value of a
scrambled state (the bit readable only from half the surroundings).

Checks:
A. The pointer works: the z-started impurity stays pure, while the
   x-started one decoheres (by more than 0.5 bit at g = 3).
B. No redundancy: for L = 10 and 12 and g = 1 and 3, R_0.1 stays between
   1.6 and 2.5 at every time up to L/2; never 3 (not a pass). By the letter
   of the pre-registration this is "in between". R ~ 2 is the scrambled
   value, not copies.
C. Small fragments know little: fragments of 1 site hold at most about a
   fifth of the bit, and the curve reaches the bit only near half the sea.

Prints one line per check, the N5 resolution lines and TOTAL: PASS=N FAIL=M.
"""
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply, eigsh

AUDIT_TIMEOUT_SEC = 900

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


def experiment(L, g, seed=3):
    n = L + 1
    def op1(mat,q):
        return sps.kron(sps.kron(sps.identity(2**q),mat),sps.identity(2**(n-q-1)),format='csr')
    cdag=sps.csr_matrix([[0,0],[1,0]]); Z=sps.csr_matrix([[1,0],[0,-1]]); num=sps.csr_matrix([[0,0],[0,1]])
    def cd(site):  # JW creation on site (1..L), string over sites before it (not the impurity)
        M=sps.identity(1,format='csr')
        for q in range(n):
            if q==0: m=sps.identity(2)
            elif q<site+1 and q>=1 and q!=site+0: m=Z if q<site else (cdag if q==site else sps.identity(2))
            else: m=cdag if q==site else sps.identity(2)
            M=sps.kron(M,m,format='csr')
        return M
    C=[None]+[cd(s) for s in range(1,L+1)]
    Hhop=sps.csr_matrix((2**n,2**n),dtype=complex)
    for s in range(1,L+1):
        t=s%L+1
        term=C[s]@C[t].conj().T
        ph=-1.0 if s==L else 1.0     # antiperiodic closing bond
        Hhop=Hhop-ph*(term+term.conj().T)
    N_op=sum(C[s]@C[s].conj().T for s in range(1,L+1))
    Himp=g*op1(Z,0)@(C[1]@C[1].conj().T)     # impurity sigma_z times occupation of site 1
    H=Hhop+Himp
    # sea ground state at half filling (impurity factor ignored: use Hhop restricted), impurity in |+>
    w,v=eigsh(Hhop+10*(N_op-(L//2)*sps.identity(2**n))@(N_op-(L//2)*sps.identity(2**n)),k=4,which='SA')
    gs=v[:,np.argmin(w)]
    # project gs onto impurity |up> (index bit 0 = 0) then build |+>
    T=gs.reshape(2,-1); sea=T[0] if np.linalg.norm(T[0])>np.linalg.norm(T[1]) else T[1]; sea=sea/np.linalg.norm(sea)
    psi0=np.kron(np.array([1,1])/np.sqrt(2),sea).astype(complex)
    def S_of(psi,A):
        B=[i for i in range(n) if i not in A]; X=A if len(A)<=len(B) else B
        Tt=psi.reshape([2]*n); rest=[i for i in range(n) if i not in X]
        M=np.transpose(Tt,X+rest).reshape(2**len(X),-1); w_=np.linalg.eigvalsh(M@M.conj().T); w_=w_[w_>1e-13]
        return float(-np.sum(w_*np.log2(w_)))
    rng=np.random.default_rng(3)
    def curve(psi,samples=8):
        hs=S_of(psi,[0]); env=list(range(1,n)); out=[]
        for f in range(1,L+1):
            vals=[]
            for _ in range(samples if f<L else 1):
                F=sorted(rng.choice(env,size=f,replace=False).tolist()); vals.append(hs+S_of(psi,F)-S_of(psi,[0]+F))
            out.append(float(np.mean(vals)))
        return hs,out
    def sieve(t):
        out={}
        for name,vec in (('z',[1,0]),('x',[1/np.sqrt(2),1/np.sqrt(2)])):
            p0=np.kron(np.array(vec,complex),sea); pt=expm_multiply(-1j*H,p0,start=0,stop=t,num=2,endpoint=True)[-1]
            out[name]=S_of(pt,[0])
        return out
    
    rng = np.random.default_rng(seed)
    out = []
    ts = [1, 2, 3, 4, L / 2]
    states = expm_multiply(-1j * H, psi0, start=0, stop=max(ts), num=int(max(ts) * 4) + 1, endpoint=True)
    grid = np.linspace(0, max(ts), int(max(ts) * 4) + 1)
    for t in ts:
        ps = states[np.argmin(abs(grid - t))]
        hs, cur = curve(ps)
        fmin = next((f for f, vv in enumerate(cur, 1) if vv >= 0.9 * hs), None) if hs > 1e-6 else None
        out.append(dict(t=t, hs=hs, R=L / fmin if fmin else 0.0, f1=cur[0] / hs, sieve=sieve(t)))
    return out


runs = {(L, g): experiment(L, g) for L in (10, 12) for g in (1.0, 3.0)}
pointer = all(max(r['sieve']['z'] for r in rr) < 1e-8 for rr in runs.values()) and all(max(r['sieve']['x'] for r in runs[(L, 3.0)]) > 0.5 for L in (10, 12))
check("A: the pointer works: the z-started impurity stays pure, the x-started one decoheres",
      pointer, "; ".join(f"L={L} g={g}: x-entropy {[round(r['sieve']['x'], 3) for r in rr]}" for (L, g), rr in runs.items()))
Rs = [r['R'] for rr in runs.values() for r in rr]
check("B: no redundancy: R_0.1 stays between 1.6 and 2.5 at every time (never 3; the scrambled value is 2)",
      all(1.6 <= x <= 2.5 for x in Rs), "; ".join(f"L={L} g={g}: R {[round(r['R'], 2) for r in rr]}" for (L, g), rr in runs.items()))
f1 = [r['f1'] for rr in runs.values() for r in rr if r['hs'] > 0.3]
check("C: small fragments know little: one site holds at most about a fifth of the bit",
      max(f1) < 0.25, f"I(S:F)/H(S) for one-site fragments: max {max(f1):.2f}, mean {np.mean(f1):.2f}")
print("per_element: exact full-Fock-space state vectors; entropies from exact reduced density matrices of the impurity and sea fragments.")
print("per_site: one-site fragments are sampled; the coupling acts on one site; the impurity's own entropy is tracked.")
print("per_mode: checked and not executed - fragments are sets of sites, not modes; no mode-resolved redundancy is computed.")
print("per_block: fragments of every size 1..L (8 random samples each) give the information curve.")
print("lattice_wide: checked and not executed - rings of 10 and 12 only, free sea only, one impurity; no interactions, no 2D or 3D.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
