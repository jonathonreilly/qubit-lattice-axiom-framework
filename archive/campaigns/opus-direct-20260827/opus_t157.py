"""T157 - COMPLETE POSITIVITY: the sharp constraint on the admissibility rule.

R93 left a bounded four-parameter family.  Mere positivity gives a convex region,
but the physically correct condition is COMPLETE positivity: if the rule takes the
neighbours' states to the site's distribution, the underlying operation must be CP.

STRUCTURE, derived rather than assumed.  A first attempt -- rho_out = kappa I +
sum_i Phi_i(rho_i) with each Phi_i CP -- FAILS IMMEDIATELY, and the failure is
instructive: those Phi_i have Tr Phi_i(rho) = 0 for all rho, so their Choi
matrices are PSD with zero trace, hence zero.  Requiring CP of the pieces that way
kills the rule outright.  The correct structure is a convex mixture of CHANNELS:

     rho_out = sum_i w_i Psi_i(rho_i),   w_i >= 0,  sum w_i = 1,  Psi_i CPTP

Covariance then forces w_i = 1/6 and Psi_i = R_i Psi R_i^{-1} for a SINGLE channel
Psi, whose Bloch action must commute with rotations about its own axis:

     M = alpha I + beta n n^T + delta [n]_x ,     gamma = gamma_0 n

so   v_out = (1/6)[ alpha V + beta N + delta C + gamma_0 sum_i n_i ]
and sum_i n_i = 0 on a balanced pattern -- reproducing R93's G = 0 independently,
which is a consistency check on the whole construction.

So (c,f,g,e) = (alpha,beta,delta,gamma_0)/6 and CP of Psi is a hard constraint on
them.  Compute the CP region exactly via the Choi matrix.

CONTROLS: the identity channel (alpha=1, rest 0) must be CP; a known-NON-CP map
(the Bloch-vector transpose, alpha=1 with a reflection) must be rejected."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),
   np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def choi(M,gam):
    """Choi matrix of the qubit map (a0,a) -> (a0, M a + gamma a0), CPTP iff PSD."""
    def Psi(X):
        a0=np.trace(X)/2
        a=np.array([np.trace(X@S[k])/2 for k in range(3)])
        b=M@a+gam*a0
        return a0*I2+sum(b[k]*S[k] for k in range(3))
    C=np.zeros((4,4),dtype=complex)
    for i in range(2):
        for j in range(2):
            E=np.zeros((2,2),dtype=complex); E[i,j]=1
            C[2*i:2*i+2,2*j:2*j+2]=Psi(E)
    return C
def is_cp(M,gam,tol=-1e-10):
    return np.linalg.eigvalsh(0.5*(choi(M,gam)+choi(M,gam).conj().T))[0]>tol
n=np.array([0,0,1.0])
def Mof(al,be,de):
    P=np.outer(n,n); X=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    return al*np.eye(3)+be*P+de*X
print("T157  complete positivity of the covariant admissibility channel")
print()
print("   CONTROLS")
print(f"      identity channel (alpha=1)            CP? {is_cp(Mof(1,0,0),np.zeros(3))}   (must be True)")
print(f"      Bloch transpose (diag(1,-1,1))        CP? {is_cp(np.diag([1.,-1.,1.]),np.zeros(3))}   (must be False)")
print(f"      full depolarising (alpha=0)           CP? {is_cp(Mof(0,0,0),np.zeros(3))}   (must be True)")
print(f"      amplification (alpha=1.5)             CP? {is_cp(Mof(1.5,0,0),np.zeros(3))}   (must be False)")
print()
print("   CP region, scanned")
print(f"      {'constraint':>34} {'range of alpha':>22}")
for nm,be,de,g0 in (("pure V channel (beta=delta=gamma=0)",0,0,0),
                    ("with N (beta=alpha)",None,0,0),
                    ("with C (delta=alpha)",0,None,0),
                    ("with gradient (gamma_0=0.3)",0,0,0.3)):
    lo,hi=None,None
    for al in np.linspace(-1.5,1.5,3001):
        b=al if be is None else be; d=al if de is None else de
        if is_cp(Mof(al,b,d),g0*n):
            lo=al if lo is None else lo; hi=al
    print(f"      {nm:>34} {f'[{lo:+.4f}, {hi:+.4f}]' if lo is not None else 'EMPTY':>22}")
print()
print("   the gamma_0 (gradient) axis at alpha fixed:")
print(f"      {'alpha':>8} {'max |gamma_0| with CP':>24}")
for al in (1.0,0.8,0.5,0.0,-1.0/3):
    best=0.0
    for g0 in np.linspace(0,1.5,1501):
        if is_cp(Mof(al,0,0),g0*n): best=g0
        else: break
    print(f"      {al:8.4f} {best:24.4f}")
print()
print("   alpha in [-1/3, 1] for the pure channel is the standard qubit depolarising")
print("   range; if that is what appears, CP has pinned the covariant rule to exactly")
print("   the physically admissible band with no input beyond the axioms.")
