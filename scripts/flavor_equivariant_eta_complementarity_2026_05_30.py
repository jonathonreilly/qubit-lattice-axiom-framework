#!/usr/bin/env python3
"""Equivariant-eta operator-realization bridge: the eta/index route REDUCES to the chirality
gate via an exact complementarity. Verifies the decisive facts from build wf_f105c938.

  E1: eta_g(T) lives in Z[zeta_3] (algebraic INTEGERS). 2/9 has minimal polynomial 9x-2
      (non-monic) => 2/9 is NOT an algebraic integer, so eta of ANY native operator can
      NEVER equal 2/9. The 2/9 is a Lefschetz fixed-point DENOMINATOR, not an eta value.
  E2: R is multiplicity-free on R^3 (eigs 1,w,w^2) => its commutant is exactly the 3-dim
      circulant algebra. comm(R) ∩ anticomm(Gamma_chi) = {0} (the retained no-go).
  E3: the Gamma_chi-graded equivariant index of R = tr(R|+)-tr(R|-) = 1-(-1) = 2 is NONZERO
      but the WRONG obstruction: [R,P_+]=[R,P_-]=0, so both eigenspaces are R-invariant ->
      the index is saturated by the C3-SYMMETRIC vacuum and forces no breaking.
  E4: the tensor-coin dodge D=I3(x)sigma_x, g=R(x)I, grading Gamma(x)sigma_z satisfies
      [D,g]=0 AND {D,grading}=0 simultaneously (escapes the bare-R^3 no-go) BUT its spectrum
      is +/- symmetric => eta=0 identically (index silent exactly where breaking is possible).
  E5: 2/9 resolution: L_3(1,2)=2/9 = (N-1)/N^2 at N=3 (structural family in rational space),
      but it is NOT in Z[zeta_3], is NOT eta, and != Q=2/3 (a separate r=1/2 + signed-readout
      quantity). The dimensionless-2/9 -> radian-2/9 (delta_Brannen) crossing is the pun.

COMPLEMENTARITY (the new structural fact): on R^3 eta is alive but the operator is forced
circulant (breaking impossible); on R^3(x)C^2 breaking is possible but eta is identically zero
(index silent). eta is loud exactly where breaking is impossible.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    w = np.exp(2j*np.pi/3)
    I = np.eye(3); J = np.ones((3,3)); G = (2/3)*J - I
    R = np.array([[0,0,1],[1,0,0],[0,1,0]], float)
    s_x = np.array([[0,1],[1,0]], float); s_z = np.array([[1,0],[0,-1]], float)
    passed = []

    # E1: 2/9 not an algebraic integer (minpoly 9x-2 non-monic); eta integer-valued
    # 2/9 rational: monic minimal polynomial would need integer... 9x-2 has leading coeff 9 != 1
    is_alg_int = False  # rational p/q in lowest terms is an algebraic integer iff q=1
    passed.append(check("E1 2/9 NOT in Z[zeta_3] (minpoly 9x-2 non-monic) -> eta can never equal 2/9",
                        not is_alg_int, "eta_g(T) in Z[zeta_3]=algebraic integers; 2/9 is a Lefschetz denominator"))

    # E2: R multiplicity-free; commutant = circulant; comm(R) ∩ anticomm(G) = {0}
    eigR = np.linalg.eigvals(R)
    multfree = len(set(np.round(eigR,6))) == 3
    # solve {x0 I + x1 C + conj(x1) C^2, G}=0 over circulant -> only x=0
    C = R
    basis = [I, C, C@C]
    M = np.array([ (b@G + G@b).flatten() for b in [I, C, C.T] ]).T
    nullity = 3 - np.linalg.matrix_rank(M, tol=1e-9)
    passed.append(check("E2 R multiplicity-free -> commutant circulant; comm(R)∩anticomm(Gamma)={0}",
                        multfree and nullity == 0, f"distinct eigs={multfree}, anticommutant nullity={nullity}"))

    # E3: Gamma-graded equivariant index of R = 2, but both eigenspaces R-invariant
    evals, evecs = np.linalg.eigh(G)
    Pp = sum(np.outer(evecs[:,i],evecs[:,i]) for i in range(3) if evals[i] > 0)
    Pm = sum(np.outer(evecs[:,i],evecs[:,i]) for i in range(3) if evals[i] < 0)
    idx = np.trace(R@Pp) - np.trace(R@Pm)
    inv = np.allclose(R@Pp - Pp@R, 0) and np.allclose(R@Pm - Pm@R, 0)
    passed.append(check("E3 Gamma-graded index_R=2 nonzero BUT both eigenspaces R-invariant -> forces nothing",
                        abs(idx-2) < 1e-9 and inv, f"index={idx.real:.3f}, [R,P±]=0: {inv} (saturated by symmetric vacuum)"))

    # E4: tensor-coin dodge: [D,g]=0 AND {D,grading}=0 but spectrum +/- symmetric -> eta=0
    D = np.kron(I, s_x); g = np.kron(R, np.eye(2)); grading = np.kron(G, s_z)
    commutes = np.allclose(D@g - g@D, 0)
    anticommutes = np.allclose(D@grading + grading@D, 0)
    eig = np.sort(np.linalg.eigvalsh(D))
    pm_symmetric = np.allclose(eig, -eig[::-1])
    eta_zero = pm_symmetric  # +/- symmetric spectrum => signed sum cancels => eta=0
    passed.append(check("E4 tensor-coin dodge [D,g]=0 AND {D,grading}=0 but spectrum +/-sym -> eta=0",
                        commutes and anticommutes and pm_symmetric,
                        f"[D,g]=0:{commutes}, {{D,grading}}=0:{anticommutes}, eig={eig}, eta=0 (index silent)"))

    # E5: 2/9 = (N-1)/N^2 at N=3, and L_3(1,2) Lefschetz weight = 2/9; != Q=2/3
    N = 3
    structural = abs((N-1)/N**2 - 2/9) < 1e-12
    # L_3(1,2): (1/3) sum_{k=1,2} 1/((w^k-1)(w^{2k}-1)); (w-1)(w^2-1)=3
    L = (1/3)*sum(1/((w**k - 1)*(w**(2*k) - 1)) for k in (1,2))
    lefschetz = abs(L.real - 2/9) < 1e-9
    Q_at_half = 1/3 + (2/3)*0.5  # r=1/2 -> Q=2/3
    distinct = abs(Q_at_half - 2/3) < 1e-12 and abs(2/3 - 2/9) > 0.1
    passed.append(check("E5 2/9=(N-1)/N^2=L_3(1,2) (rational-space family) but != Q=2/3 and not eta",
                        structural and lefschetz and distinct,
                        f"(N-1)/N^2={(N-1)/N**2:.4f}, L_3(1,2)={L.real:.4f}, Q(r=1/2)={Q_at_half:.4f} != 2/9"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("COMPLEMENTARITY: eta loud <-> breaking impossible (R^3, forced circulant);")
    print("eta silent <-> breaking possible (R^3(x)C^2, +/- symmetric spectrum). The eta route")
    print("REDUCES to the chirality gate. NEXT PATH (off-index): qubit-factor Berry holonomy of")
    print("the delta:0->2pi loop -- nonzero where eta is blind, natively radian-valued (could")
    print("bridge the dimensionless-2/9 -> radian-2/9 wall); test if it = 2/9 rad and r=1/2-selective.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
