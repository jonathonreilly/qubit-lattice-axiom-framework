#!/usr/bin/env python3
"""
The matter-attachment pin reduces to a Kawamoto-Smit/state-law bridge question:
D + merger give only OPERATOR-FRAME (adjoint) covariance; the matter-STATE
spinor law -- and hence the C^2-spin attachment -- is not supplied by this
native-D packet alone. The native-D route supplies only single-component
phase/gauge data, not a C^2 spin-state law.

Faithfulness (PR #2463) reduced to the matter-attachment pin: "matter field index = the C^2 qubit STATE
carries the j=1/2 SPINOR rep of the PHYSICAL spatial rotation as its transformation law." This runner
establishes, non-circular (never assumes the faithful rep or Q=2/3):

  (A) The native first-order real anti-Hermitian D is SINGLE-COMPONENT on the lattice (one amplitude per
      site, no per-site spinor index) and SPIN-BLIND on the C^2; -D^2 is a scalar lattice mass-shell.
  (B) The merger gives only OPERATOR-FRAME covariance: U(R)=exp(i theta.S) rotates the gamma OPERATORS as a
      3-vector by CONJUGATION (adjoint action), U(R) sigma_i U(R)^dag = R_ij sigma_j. This is one level BELOW
      a matter-STATE spinor law (the fundamental action on the ket), which per_site explicitly disclaims.
  (C) THE KS BRIDGE: the C^2-spinor kinetic-frame structure of the naive
      2-component Dirac operator is diagonalized AWAY into the single-component
      staggered phases by the KS operator Omega(x)=sigma_1^{x1} sigma_2^{x2}
      sigma_3^{x3}: Omega(x)^dag sigma_mu Omega(x+e_mu) = eta_mu(x) I (the staggered phase, a SCALAR). So the
      C^2-spin kinetic-frame <-> single-component translator IS Omega = the KS reconstruction. A physical
      matter-state spinor-law bridge remains separate.

DISPOSITION: this runner counts only algebraic/matrix checks. It records, but
does not count as PASS, the current boundary: matter-attachment is not forced
KS-free; the KS route is a bounded bridge surface, and an elementary state-law
posit remains admitted-not-forced. Faithfulness therefore does not collapse to
(3,1)+carrier-id from this packet alone.
"""
import numpy as np
PASSES = []
BOUNDARIES = []
def record(name, ok, detail=""):
    PASSES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
def boundary(name, detail=""):
    BOUNDARIES.append(name); print(f"[BOUNDARY] {name}" + (f" -- {detail}" if detail else ""))
def section(t): print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)

s1=np.array([[0,1],[1,0]],dtype=complex); s2=np.array([[0,-1j],[1j,0]],dtype=complex); s3=np.array([[1,0],[0,-1]],dtype=complex)
sig=[s1,s2,s3]; I2=np.eye(2,dtype=complex)
def mpow(M,n): return np.linalg.matrix_power(M, n%2) if n%2==0 else M  # sigma^2=I

# ----------------------------------------------------------------------
section("A. Native first-order D: single-component on the lattice, spin-blind on C^2, scalar mass-shell")
# ----------------------------------------------------------------------
L=4; sites=[(x,y,z) for x in range(L) for y in range(L) for z in range(L)]; idx={s:i for i,s in enumerate(sites)}; n=len(sites)
def eta(s,mu): return 1.0 if mu==0 else ((-1.0)**s[0] if mu==1 else (-1.0)**(s[0]+s[1]))
D=np.zeros((n,n))
for s in sites:
    for mu in range(3):
        sp=list(s); sp[mu]=(s[mu]+1)%L; sm=list(s); sm[mu]=(s[mu]-1)%L
        D[idx[s],idx[tuple(sp)]] += eta(s,mu)/2; D[idx[s],idx[tuple(sm)]] -= eta(s,mu)/2
record("native D is single-component (one amplitude per SITE), real antisymmetric -> H=iD Hermitian",
       np.allclose(D,-D.T), "no per-site spinor index in D")
mass2 = np.unique(np.round(np.linalg.eigvalsh(-D@D),6))
record("normalized -D^2 is the SCALAR lattice mass-shell {0,1,2,3} (no spinor structure)",
       np.allclose(mass2, np.array([0.0, 1.0, 2.0, 3.0])),
       f"-D^2 spectrum = {mass2.tolist()}")
mass2_unscaled = np.unique(np.round(np.linalg.eigvalsh(-(2*D)@(2*D)),6))
record("unscaled finite-difference convention gives {0,4,8,12} and is not the note's normalized D",
       np.allclose(mass2_unscaled, np.array([0.0, 4.0, 8.0, 12.0])),
       f"unscaled spectrum = {mass2_unscaled.tolist()}")
record("native D is SPIN-BLIND on the C^2: [H (x) I_2, I (x) sigma_i/2] = 0",
       all(np.allclose(np.kron(1j*D,I2)@np.kron(np.eye(n),sig[i]/2) - np.kron(np.eye(n),sig[i]/2)@np.kron(1j*D,I2),0) for i in range(3)))

# ----------------------------------------------------------------------
section("B. The merger is OPERATOR-FRAME (adjoint): U(R) rotates the gamma OPERATORS by conjugation")
# ----------------------------------------------------------------------
from scipy.linalg import expm
S=[x/2 for x in sig]; th=0.7
U=expm(1j*th*S[2])
record("U(R)=exp(i th S_z) conjugates sigma as the 3-vector R sigma (ADJOINT action on OPERATORS)",
       np.allclose(U@s1@U.conj().T, np.cos(th)*s1 - np.sin(th)*s2),
       "operator-frame covariance -- one level BELOW the matter-STATE spinor law (per_site disclaims that)")

# ----------------------------------------------------------------------
section("C. THE KS BRIDGE: Omega(x) diagonalizes the C^2 spinor AWAY into the staggered phase (= KS)")
# ----------------------------------------------------------------------
def Omega(x): return mpow(s1,x[0]) @ mpow(s2,x[1]) @ mpow(s3,x[2])
def eta_KS(x,mu):  # staggered phase eta_mu(x) = (-1)^{x_0+...+x_{mu-1}}
    return 1.0 if mu==0 else ((-1.0)**x[0] if mu==1 else (-1.0)**(x[0]+x[1]))
ok=True; samples=[(0,0,0),(1,0,0),(1,1,0),(0,1,1),(1,1,1),(2,1,0)]
for x in samples:
    for mu in range(3):
        xp=list(x); xp[mu]+=1
        lhs = Omega(x).conj().T @ sig[mu] @ Omega(tuple(xp))
        if not np.allclose(lhs, eta_KS(x,mu)*I2): ok=False
record("Omega(x)^dag sigma_mu Omega(x+e_mu) = eta_mu(x) I  (the spinor sigma_mu -> a SCALAR staggered phase)",
       ok, "Omega = sigma_1^x1 sigma_2^x2 sigma_3^x3 is the KS reconstruction operator")
boundary("KS supplies a bounded bridge surface, not a physical matter-state law in this packet",
         "Omega translates the kinetic-frame Pauli matrices into scalar staggered phases; a KS-to-physical-state-law bridge remains separate")

# ----------------------------------------------------------------------
section("D. Scalar sign-field guard and current boundary")
# ----------------------------------------------------------------------
def build_open_D(Lbox, phase_func):
    box_sites=[(x,y,z) for x in range(Lbox) for y in range(Lbox) for z in range(Lbox)]
    box_idx={s:i for i,s in enumerate(box_sites)}
    out=np.zeros((len(box_sites),len(box_sites)))
    for s in box_sites:
        for mu in range(3):
            sp=list(s); sp[mu]+=1
            if sp[mu] >= Lbox:
                continue
            sp=tuple(sp)
            val=phase_func(s,mu)/2
            out[box_idx[s],box_idx[sp]] += val
            out[box_idx[sp],box_idx[s]] -= val
    return out, box_sites

def gauge_sign(x):
    return 1.0 if ((x[0]*x[1] + x[2]) % 2 == 0) else -1.0

def eta_gauge(x,mu):
    xp=list(x); xp[mu]+=1
    return gauge_sign(x) * eta_KS(x,mu) * gauge_sign(tuple(xp))

D_open, open_sites = build_open_D(3, eta_KS)
D_gauge, _ = build_open_D(3, eta_gauge)
G = np.diag([gauge_sign(s) for s in open_sites])
record("single-component scalar sign field W gauge-conjugates a KS phase representative without any C^2 spin action",
       np.allclose(D_gauge, G @ D_open @ G),
       "D_eta' = W D_eta W for a nontrivial W(x) in {+-1}")
boundary("matter-state spinor law remains the missing bridge",
         "the runner proves spin-blind D, adjoint operator covariance, KS scalarization, and scalar sign-field gauge equivalence only")
boundary("no (3,1)+carrier-id collapse is claimed",
         "borrowing a Majorana R^4 boost spinor for the per-site C^2 module remains outside this packet")

# ----------------------------------------------------------------------
section("RESULT")
# ----------------------------------------------------------------------
n_,p_=len(PASSES),sum(PASSES); print(f"\n{p_}/{n_} checks passed.")
print(f"{len(BOUNDARIES)} boundary lines recorded.")
print("The native single-component D is spin-blind on the C^2; the merger gives only OPERATOR-FRAME")
print("(adjoint) covariance U(R)sigma U(R)^dag = R sigma, one level below the matter-STATE spinor law.")
print("Omega(x) converts sigma_mu -> the scalar staggered phase eta_mu on the KS kinetic bridge surface,")
print("and a scalar sign field W gauge-conjugates KS representatives without any C^2 spin action.")
print("This is bounded localization only: a KS-to-physical-matter-state spinor-law bridge or an")
print("elementary state-law theorem is still required before matter attachment is forced.")
import sys; sys.exit(0 if p_==n_ else 1)
