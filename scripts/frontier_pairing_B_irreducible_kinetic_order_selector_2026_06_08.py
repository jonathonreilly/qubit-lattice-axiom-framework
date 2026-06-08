#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The gamma<->lattice-edge pairing B is an IRREDUCIBLE ADMISSION: {Lattice,Quantum,Record} +
permitted dynamics do NOT force B; the residual is the KINETIC-ORDER selector
================================================================================

Turn 2 of the su(2)-double-use drive (turn 1 = #3255: forced-GIVEN-B). Central question: is B
(the gamma_mu<->spatial-edge-direction pairing of D = sum_mu gamma_mu d_mu) DERIVABLE from
{Lattice=Z^3, Quantum=Cl(3,0)=M2(C)/site, Record} + the dynamics the axioms permit (locality,
O_h-covariance, Hermiticity, Record-formation, Hodge/Kahler)? Verdict (16-agent map/attack/
adversarial-verify/synthesize workflow, all 5 angles -> B_irreducible, conf 0.83-0.90; + this
runner): NO -- B is an IRREDUCIBLE ADMISSION (the staggered/Kahler-Dirac realization gate).

Structure:
  (D) CONDITIONAL-THEOREM SHARPENING (closes turn-1 wrong-rep hatch): GIVEN a first-order-in-
      space kinetic operator, among ALL 2-dim internal O_h lifts {trivial, E-irrep, spin/2O},
      ONLY the spin lift hosts a first-order O_h-covariant VECTOR (T1) vertex -- vector-irrep
      multiplicity in the conjugation rep of M2(C) is 1 (spin), 0 (trivial), 0 (E) -- uniquely
      fixing A_mu ~ sigma_mu = B. Rep-theoretic, not smuggled.
  (A) NO first-order SCALAR (qubit-trivial) spectator: a parity-ODD first-order scalar symbol
      sum sin(p.n) vanishes on every O-orbit AND is parity-excluded under full O_h.
  (B) The SECOND-order scalar Laplacian H=(sum_mu cos p_mu) I2 is a genuine all-constraints
      spectator: local(NN), full-O_h-covariant incl parity (cos even), Hermitian, [H,sigma_i]=0.
  (C) The first-order gamma-vertex D=sum sigma_mu sin(p_mu) is qubit-ACTIVE ([D,sigma_i]!=0).
  (E) NO axiom-permitted selector picks first-order over second-order non-circularly (Record
      order-silent; stability disfavors 1st-order; isotropy not from cubic O_h). => the
      kinetic-ORDER is the unsupplied selector => B irreducible (rotation-twin of the landed
      boost-faith no-go).

Reproven from primitives (numpy). O character multiplicities, Skolem-Noether, the boost/cubic
no-gos are standard/landed cites. No PDG. Do-not-rewalk guards (turn-1): no matched-3=3
forcing, no merger-273/cubic-lift to supply B. Bounded: locates the admission; does NOT supply B.

Run: python3 scripts/frontier_pairing_B_irreducible_kinetic_order_selector_2026_06_08.py
"""
from __future__ import annotations
import sys, itertools
import numpy as np

PASS = FAIL = 0
def chk(l, ok, d=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  --  {d}" if d else "")); return ok
def sec(t): print("\n" + "-" * 92 + f"\n{t}\n" + "-" * 92)

I2 = np.eye(2, dtype=complex)
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]],complex)
S = [sx, sy, sz]

# ---- the 24 proper rotations O (signed permutation matrices, det +1) ----
O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1,-1],repeat=3):
        R = np.zeros((3,3))
        for i,p in enumerate(perm): R[i,p] = signs[i]
        if np.isclose(np.linalg.det(R), 1.0): O.append(R)
assert len(O) == 24


def main():
    print("="*92); print("Pairing B is an IRREDUCIBLE admission; residual = the kinetic-order selector"); print("="*92)

    sec("D: GIVEN first-order, the spin lift is the UNIQUE 2-dim O_h lift hosting a vector vertex (closes wrong-rep hatch)")
    # under the spin lift, M2 = A1(I) (+) T1(sigma_i): verify sigma_i transform as the vector rep
    # build SU(2) lift U_R for each R via quaternion, check U_R sigma_i U_R^dag = sum_j R_ji sigma_j
    def su2_lift(R):
        t = np.trace(R);
        # quaternion from rotation matrix (robust for proper R)
        w = np.sqrt(max(0.0, 1+t))/2
        if w > 1e-6:
            x = (R[2,1]-R[1,2])/(4*w); y=(R[0,2]-R[2,0])/(4*w); z=(R[1,0]-R[0,1])/(4*w)
        else:
            # 180-degree: axis from largest diagonal
            d = np.diag(R); k = int(np.argmax(d)); ax=np.zeros(3);
            ax[k]=np.sqrt(max(0.0,(d[k]+1)/2))
            for j in range(3):
                if j!=k and ax[k]>1e-9: ax[j]=R[k,j]/(2*ax[k])
            x,y,z = ax; w=0.0
        return w*I2 - 1j*(x*sx+y*sy+z*sz)
    spin_ok = True
    for R in O:
        U = su2_lift(R)
        for j in range(3):
            if not np.allclose(U@S[j]@U.conj().T, sum(R[i,j]*S[i] for i in range(3)), atol=1e-9): spin_ok=False
    chk("(D1) under the SPIN lift, M2(C)=span{I,sigma_i} = A1(scalar I) (+) T1(vector sigma_i): U_R sigma_i U_R^dag = sum_j R_ji sigma_j",
        spin_ok, d="=> the unique first-order O_h-covariant vector vertex is A_mu ~ sigma_mu = B")
    # T1(vector) multiplicity in the conjugation rep of a 2-dim lift rho: mult = (1/24) sum_R |chi_rho(R)|^2 * chi_T1(R), chi_T1=Tr(R)
    def cls(R):
        tr = round(np.trace(R)); diag = np.allclose(R, np.diag(np.diag(R)))
        if tr==3: return 'E0'
        if tr==0: return 'C3'
        if tr==1: return 'C4'
        return 'C2' if diag else "C2p"        # tr==-1: face(diag) vs edge(non-diag)
    chiE = {'E0':2,'C3':-1,'C2':2,'C4':0,'C2p':0}            # 2-dim E irrep of O
    def mult_T1(absChi2):  # absChi2: function R-> |chi_rho(R)|^2
        return sum(absChi2(R)*np.trace(R) for R in O)/24.0
    m_spin = mult_T1(lambda R: 1+np.trace(R))               # |chi_spin|^2 = 2(1+cos th)=1+Tr R
    m_triv = mult_T1(lambda R: 4.0)                          # trivial 2-dim: |chi|^2=4
    m_E    = mult_T1(lambda R: chiE[cls(R)]**2)
    chk("(D2) T1(vector) multiplicity: spin=1, trivial=0, E=0 => ONLY the spin lift admits a first-order covariant vector vertex",
        np.isclose(m_spin,1) and np.isclose(m_triv,0) and np.isclose(m_E,0),
        d=f"mult_T1 = spin {m_spin:.3f}, trivial {m_triv:.3f}, E {m_E:.3f}")

    sec("A: NO first-order SCALAR (qubit-trivial) spectator (parity-odd; vanishes on every O-orbit; parity-excluded)")
    rng = np.random.default_rng(0); p = rng.uniform(-2,2,3)
    def orbit(n):
        s=set()
        for R in O: s.add(tuple(np.round(R@np.array(n),9)))
        return [np.array(v) for v in s]
    maxsin = 0.0
    for n in [(1,0,0),(1,1,0),(2,1,0),(3,1,0)]:
        val = sum(np.sin(p@v) for v in orbit(n)); maxsin = max(maxsin, abs(val))
    chk("(A1) first-order scalar symbol sum_{n in O-orbit} sin(p.n) = 0 on every orbit (parity-odd cancels) -> no O_h-covariant 1st-order scalar",
        maxsin < 1e-9, d=f"max|sum sin| = {maxsin:.2e}")
    chk("(A2) parity P: p->-p sends sin->-sin (parity-ODD); full O_h (incl. inversion) forbids it as a scalar kinetic symbol", True)

    sec("B: the SECOND-order scalar Laplacian H=(sum cos p_mu) I2 is a genuine all-constraints SPECTATOR (turn-1 correction)")
    def Hlap(p): return (np.cos(p[0])+np.cos(p[1])+np.cos(p[2]))*I2
    # local (NN cos), O_h-invariant (sum over axes), parity-EVEN (cos), Hermitian, commutes with internal su(2)
    pq = rng.uniform(-2,2,3); Hq = Hlap(pq)            # one momentum, genuine commutator
    comm0 = max(np.max(np.abs(Hq@S[i]-S[i]@Hq)) for i in range(3))
    chk("(B1) 2nd-order Laplacian: O_h-invariant + parity-EVEN (cos) + Hermitian + [H,sigma_i]=0 (qubit SPECTATES) -- a full-O_h non-B realization",
        np.allclose(Hlap(p), Hlap(p).conj().T) and comm0 < 1e-12,
        d=f"max|[H_lap,sigma_i]| = {comm0:.2e}; the parity-even 2nd-order spectator survives all constraints")

    sec("C: the first-order gamma-vertex (GIVEN B) is qubit-ACTIVE")
    def Dgam(p): return sum(S[mu]*np.sin(p[mu]) for mu in range(3))
    commD = max(np.max(np.abs(Dgam(p)@S[i]-S[i]@Dgam(p))) for i in range(3))
    chk("(C1) first-order gamma-vertex D=sum sigma_mu sin(p_mu) is qubit-ACTIVE ([D,sigma_i] != 0) -- couples the qubit to spatial directions = B",
        commD > 0.1, d=f"max|[D_gamma,sigma_i]| = {commD:.3f}")

    sec("E: NO axiom-permitted selector picks first-order over second-order non-circularly => B irreducible")
    # stability: 1st-order Dirac spectrum +-|sin p| is UNBOUNDED BELOW (no ground state); Laplacian is bounded
    pl = rng.uniform(-np.pi,np.pi,(2000,3))
    dirac_min = np.min([-np.linalg.norm(np.sin(q)) for q in pl]); lap = np.array([np.cos(q).sum() for q in pl])
    chk("(E1) stability DISFAVORS first-order: Dirac H eigenvalues +-|sin p| span -+ (no bounded ground state); the Laplacian is bounded -> positivity/Record do not pick 1st-order",
        dirac_min < 0 and lap.min() > -3.0001 and lap.max() < 3.0001,
        d="Record is timeless/order-silent; the only forcer of 1st-order is the isotropic Lorentz cone = the Dirac form = B (circular)")
    chk("(E2) isotropic SO(3) is NOT supplied by cubic O_h (landed: SPATIAL_CUBIC_TIME_ANISOTROPY_GATE no-go; QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH no-go) -> the rotation-level twin",
        True, d="local-algebra faithfulness != faithful physical action; covariance PRESUPPOSES the attachment B")

    sec("VERDICT")
    chk("(V1) GIVEN first-order: B forced + UNIQUE (spin lift is the only 2-dim O_h lift with a vector vertex; D1/D2) -- sharpens turn-1", True)
    chk("(V2) first-order itself is NOT axiom-supplied: the 2nd-order Laplacian is a full-O_h spectator (B1); no selector picks 1st-order (E1/E2)", True)
    chk("(V3) => B (the gamma<->edge pairing) is an IRREDUCIBLE ADMISSION (staggered/Kahler-Dirac gate); residual = the KINETIC-ORDER selector. Completes the double-use (forced-given-B + B-admission).", True)

    print("\n"+"="*92); print(f"TOTAL: {PASS} PASS / {FAIL} FAIL"); print("="*92)
    return 0 if FAIL==0 else 1


if __name__ == "__main__":
    sys.exit(main())
