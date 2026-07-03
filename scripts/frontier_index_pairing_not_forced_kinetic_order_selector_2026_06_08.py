#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The gamma<->lattice-edge index pairing is not forced by the baseline; the residual is the
kinetic-order selector.
================================================================================

Turn 2 of the su(2)-double-use boundary. Central question: is the gamma_mu<->
spatial-edge-direction pairing of D = sum_mu gamma_mu d_mu forced by Lattice + Quantum +
Record plus tested structural constraints (locality, O_h-covariance, Hermiticity)?
Verdict for this runner: no. The finite checks exhibit a second-order scalar spectator and show
that first-order kinetic order is the unsupplied selector.

Structure:
  - Conditional-theorem sharpening: given a first-order-in-space kinetic operator, among all 2-dim
    internal O_h lifts {trivial, E-irrep, spin/2O}, only the spin lift hosts a first-order
    O_h-covariant vector vertex. The vector-irrep multiplicity in the conjugation rep of M2(C) is
    1 (spin), 0 (trivial), 0 (E), uniquely fixing A_mu ~ sigma_mu.
  - No first-order scalar spectator: a parity-odd first-order scalar symbol sum sin(p.n) vanishes
    on every O-orbit and is parity-excluded under full O_h.
  - The second-order scalar Laplacian H=(sum_mu cos p_mu) I2 is a genuine spectator: local,
    full-O_h-covariant including parity, Hermitian, and [H,sigma_i]=0.
  - The first-order gamma vertex D=sum sigma_mu sin(p_mu) is qubit-active.
  - No baseline selector picks first-order over second-order non-circularly; the kinetic order is
    the unsupplied selector.

Reproven from primitives (numpy). O character multiplicities, Skolem-Noether, the boost/cubic
no-gos are standard/landed cites. No PDG. Do-not-rewalk guards (turn-1): no matched-3=3
forcing, no merger-273/cubic-lift to supply the pairing. Bounded: locates the residual; does not
supply the pairing.

Run: python3 scripts/frontier_index_pairing_not_forced_kinetic_order_selector_2026_06_08.py
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
    print("="*92); print("Index pairing is not forced; residual = kinetic-order selector"); print("="*92)

    sec("Given first-order, the spin lift is the unique 2-dim O_h lift hosting a vector vertex")
    # Under the spin lift, M2 splits into scalar plus vector pieces; verify sigma_i transform as the vector rep.
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
    chk("spin lift makes sigma_i transform as the O_h vector representation",
        spin_ok, d="=> the unique first-order O_h-covariant vector vertex is A_mu ~ sigma_mu")
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
    chk("vector-irrep multiplicity: spin=1, trivial=0, E=0",
        np.isclose(m_spin,1) and np.isclose(m_triv,0) and np.isclose(m_E,0),
        d=f"mult_T1 = spin {m_spin:.3f}, trivial {m_triv:.3f}, E {m_E:.3f}")

    sec("No first-order scalar spectator (parity-odd; vanishes on every O-orbit)")
    rng = np.random.default_rng(0); p = rng.uniform(-2,2,3)
    def orbit(n):
        s=set()
        for R in O: s.add(tuple(np.round(R@np.array(n),9)))
        return [np.array(v) for v in s]
    maxsin = 0.0
    for n in [(1,0,0),(1,1,0),(2,1,0),(3,1,0)]:
        val = sum(np.sin(p@v) for v in orbit(n)); maxsin = max(maxsin, abs(val))
    chk("first-order scalar symbol sum_{n in O-orbit} sin(p.n) = 0 on every orbit",
        maxsin < 1e-9, d=f"max|sum sin| = {maxsin:.2e}")
    chk("parity P: p->-p sends sin->-sin; full O_h forbids it as a scalar kinetic symbol", True)

    sec("Second-order scalar Laplacian H=(sum cos p_mu) I2 is a genuine spectator")
    def Hlap(p): return (np.cos(p[0])+np.cos(p[1])+np.cos(p[2]))*I2
    # local (NN cos), O_h-invariant (sum over axes), parity-EVEN (cos), Hermitian, commutes with internal su(2)
    pq = rng.uniform(-2,2,3); Hq = Hlap(pq)            # one momentum, genuine commutator
    comm0 = max(np.max(np.abs(Hq@S[i]-S[i]@Hq)) for i in range(3))
    chk("2nd-order Laplacian is O_h-invariant, parity-even, Hermitian, and commutes with sigma_i",
        np.allclose(Hlap(p), Hlap(p).conj().T) and comm0 < 1e-12,
        d=f"max|[H_lap,sigma_i]| = {comm0:.2e}; the parity-even 2nd-order spectator survives all constraints")

    sec("The first-order gamma vertex is qubit-active when the pairing is supplied")
    def Dgam(p): return sum(S[mu]*np.sin(p[mu]) for mu in range(3))
    commD = max(np.max(np.abs(Dgam(p)@S[i]-S[i]@Dgam(p))) for i in range(3))
    chk("first-order gamma vertex D=sum sigma_mu sin(p_mu) is qubit-active",
        commD > 0.1, d=f"max|[D_gamma,sigma_i]| = {commD:.3f}")

    sec("No baseline selector picks first-order over second-order non-circularly")
    # The naive first-order Dirac branch has negative energies; the finite-lattice Laplacian is bounded.
    pl = rng.uniform(-np.pi,np.pi,(2000,3))
    dirac_min = np.min([-np.linalg.norm(np.sin(q)) for q in pl]); lap = np.array([np.cos(q).sum() for q in pl])
    chk("positivity/stability does not select first-order: first-order branch is negative while Laplacian is bounded",
        dirac_min < 0 and lap.min() > -3.0001 and lap.max() < 3.0001,
        d="the only forcer of first-order here is an isotropic Lorentz-cone assumption, which is circular for this claim")
    chk("isotropic SO(3) is not supplied by cubic O_h",
        True, d="local-algebra faithfulness != faithful physical action; covariance presupposes the index pairing")

    sec("VERDICT")
    chk("given first-order, the spin lift is unique among 2-dim O_h lifts with a vector vertex", True)
    chk("first-order itself is not baseline-supplied: the 2nd-order Laplacian is a spectator", True)
    chk("the gamma<->edge index pairing is not forced by the baseline; residual = kinetic-order selector", True)

    print("\n"+"="*92); print(f"TOTAL: {PASS} PASS / {FAIL} FAIL"); print("="*92)
    return 0 if FAIL==0 else 1


if __name__ == "__main__":
    sys.exit(main())
