"""Kill checks for T02 (Claude Sonnet 5.5, same family as attacker; not independent).

K2  Nonvanishing.  Attack claims (suggested): given the trace-rule interface, the generator is
    nonzero because 'varies with' needs the odds to depend on the six NN records.
    Test: is the record-level odds law able to tell a nonzero compressed generator from H = 0?
      Model A : Heisenberg J (any sign/scale), site relaxed to the ground state of h(N).s  -> odds
      Model B : H = 0 (nothing to compress), site state = rho(N) set by a records-only
                preparation rule chosen to equal Model A's state (a formation kernel)
      Model C : H = 0, N-independent state r0 (no preparation rule)
      Model D : Heisenberg J, N-independent generic r0, stationarity required (landed Thm 3)
    Pre-registered reading: if A and B give identical odds for all N and all menus, then
    Admissibility ('determined by and varies with N') + trace rule cannot force H != 0; the
    forcing needs the extra premise 'the state's N-dependence enters only through the generator'.
    If C is constant in N, that extra premise is what makes 'varies with' bite.

K5  Thermal time (Connes-Rovelli).  The attack's test uses the product of marginals; K of any
    product state is a sum of one-site terms, so rank 1 is a tautology.  Check the tautology on
    random product and on the tracial (maximally mixed) state that the repo takes as the
    pre-record reference state (docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md):
    modular flow of the tracial state is the identity for every N (selects H = 0).
"""
import numpy as np, scipy.linalg as sl
rng = np.random.default_rng(20260929)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2)
S=[sx,sy,sz]
F=[np.array(v,float) for v in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
def unit(v): return v/np.linalg.norm(v)
def rq(n):
    q=rng.normal(size=(n,3)); return q/np.linalg.norm(q,axis=1,keepdims=True)
def hN(q,J): return J*sum(q)
def rho_from_bloch(r): return 0.5*(I2+sum(r[a]*S[a] for a in range(3)))
def odds(rho,p):   # menu {p,-p}: probability of +p, trace rule
    P=0.5*(I2+sum(p[a]*S[a] for a in range(3))); return float(np.trace(P@rho).real)

# ---------------- K2
maxdiff_AB=0; maxdiff_AC=0; nvar_C=0.0; stat_viol=0.0; cesaro_var=0.0; tiny=0.0
for trial in range(2000):
    q=rq(6); p=unit(rng.normal(size=3))
    for J in (-1.0,-7.3,+2.0,-1e-9):
        h=hN(q,J)
        w,v=np.linalg.eigh(sum(h[a]*S[a] for a in range(3)))
        g=v[:,0]; rhoA=np.outer(g,g.conj())                     # Model A: ground state of h.s
        rB=rho_from_bloch(-unit(h))                             # Model B: H=0, prepared by records-only rule
        maxdiff_AB=max(maxdiff_AB,abs(odds(rhoA,p)-odds(rB,p)))
    # Model C: H = 0, N-independent state -> constant odds
    r0=np.array([0.3,-0.5,0.4]); rhoC=rho_from_bloch(r0)
    q2=rq(6)
    nvar_C=max(nvar_C,abs(odds(rhoC,p)-odds(rhoC,p)))           # identical by construction: no N in it
    # Model D: nonzero Heisenberg, N-independent r0: stationarity [rho0, h.s] = 0 ?
    h=hN(q,-1.0); comm=rhoC@sum(h[a]*S[a] for a in range(3))-sum(h[a]*S[a] for a in range(3))@rhoC
    stat_viol=max(stat_viol,np.linalg.norm(comm))
    # Cesaro (time-average) reading of Model D: lam = r0.h^ -> odds vary with N (this is where H != 0 bites)
    lam=r0@unit(h); cesaro_var=max(cesaro_var,abs(0.5*(1+lam*(p@unit(h)))-0.5*(1+lam*(p@unit(hN(q2,-1.0))))))
print("K2 Model A (ground state of compressed Heisenberg, J in {-1,-7.3,+2,-1e-9}) vs Model B (H=0 + records-only preparation):")
print(f"   max |odds_A - odds_B| over 8000 draws = {maxdiff_AB:.2e}   -> identical odds law; H=0 realises it")
print(f"K2 Model C (H=0, N-independent state): odds do not depend on N at all (violates 'varies with').")
print(f"K2 Model D (H!=0, N-independent generic r0): commutator norm with h.s up to {stat_viol:.2f} -> stationarity forces rho0 = 1/2 (odds 1/2), or needs prep rule")
print(f"K2 Model D, time-averaged (Cesaro) reading: odds vary with N by up to {cesaro_var:.2f} -> this is the only place 'varies with' forces H != 0, and it needs (i) N-independent r0 and (ii) a phase-averaging formation-time premise")

# zero-resultant configurations: h(N)=0 under Heisenberg -> direction undefined, every state stationary
q=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
print("K2 zero-resultant record configuration (three antipodal pairs): |h| =",np.linalg.norm(hN(q,1.0)),
      "-> Heisenberg odds undefined there; Admissibility says 'determined by N' at EVERY N")

# ---------------- K5
def ptrace(rho, keep):
    r=rho.reshape(2,2,2,2); return np.einsum('abcb->ac',r) if keep==0 else np.einsum('abad->bd',r)
def opschmidt(U,tol=1e-9):
    M=U.reshape(2,2,2,2).transpose(0,2,1,3).reshape(4,4); s=np.linalg.svd(M,compute_uv=False); return int(np.sum(s>tol*s[0]))
rk=[]
for t in range(200):
    a=rho_from_bloch(0.9*unit(rng.normal(size=3))); b=rho_from_bloch(0.9*unit(rng.normal(size=3)))
    K=-sl.logm(np.kron(a,b)); rk.append(opschmidt(sl.expm(-1j*K*0.7)))
print("K5 any product state: operator-Schmidt rank of modular flow =",set(rk),"(tautology: log of a tensor product is a sum of one-site terms)")
Ktr=-sl.logm(np.eye(4)/4)
print("K5 tracial (maximally mixed) reference state: modular flow exp(-iKt) - identity =",np.abs(sl.expm(-1j*Ktr*0.7)-np.exp(-1j*0.7*np.log(4))*np.eye(4)).max(),
      "(K = log 4 * 1: flow is trivial, selects H = 0)")
