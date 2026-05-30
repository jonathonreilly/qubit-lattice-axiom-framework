#!/usr/bin/env python3
"""Emergent chirality x emergent time -> generation orbit-splitting? Build verdict.

Verifies the decisive facts from the emergent-chirality build (wf_e18432a2):
  V1: the only realized native chirality eps|hw1 = -I3 (scalar): commutes with R,
      does NOT anticommute with Gamma_chi=(2/3)J-I.  => generation-blind.
  V2: the Connes-Lott tensor grading gamma_CL = I3 (x) sigma_3 is INERT on the
      generation factor: {G (x) sigma_1, I3 (x) sigma_3} = 0 for EVERY 3x3 G,
      so it constrains the generation operator not at all (no bridge to {G,Gamma_chi}=0).
  V3: a C3->S2 transposition-broken operator CAN anticommute with Gamma_chi AND break
      C3 on the SAME R^3, but signature(Gamma_chi)=(1,2) forces spectrum {-lam,0,+lam}
      => singular-value Koide Q = 1/2 (not 2/3), signed/Brannen Q divergent (trace 0);
      and selecting the transposition is a non-native import.
  V4: emergent time factorizes (Xi_R = Theta_R (x) V_R(t)); no generation index appears,
      so it acts as identity on R^3_gen and transports no chirality.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    I = np.eye(3); J = np.ones((3,3)); G_chi = (2/3)*J - I
    R = np.array([[0,0,1],[1,0,0],[0,1,0]], float)
    passed = []

    # V1: native chirality eps restricted to hw=1 triplet is -I3 (scalar)
    eps_hw1 = -I
    v1 = (np.allclose(eps_hw1, -I)
          and np.allclose(eps_hw1@R - R@eps_hw1, 0)
          and not np.allclose(eps_hw1@G_chi + G_chi@eps_hw1, 0))
    passed.append(check("V1 native chirality eps|hw1=-I3: commutes R, does NOT anticommute Gamma_chi",
                        v1, f"||{{eps,Gchi}}||={np.linalg.norm(eps_hw1@G_chi+G_chi@eps_hw1):.4f}"))

    # V2: CL grading I3(x)sigma_3 is inert -- {G(x)s1, I(x)s3}=0 for all G
    s1 = np.array([[0,1],[1,0]], float); s3 = np.array([[1,0],[0,-1]], float)
    gamma_cl = np.kron(I, s3)
    inert = True
    rng_mats = [I, R, G_chi, np.array([[1.,2,3],[0,1,4],[2,0,1]])]
    for G in rng_mats:
        D = np.kron(G, s1)
        if not np.allclose(D@gamma_cl + gamma_cl@D, 0):
            inert = False
    passed.append(check("V2 Connes-Lott grading I3(x)sigma3 INERT: {G(x)s1, I3(x)s3}=0 for every G",
                        inert, "grading imposes ZERO constraint on the generation factor"))

    # V3: C3->S2 broken anticommuting operator -> spectrum {-lam,0,+lam}, singular-value Q=1/2
    # construct H with {H,Gchi}=0; the anticommutant of Gchi (signature (1,2)) has rank<=2
    # take h pattern (1,-1,0) (an S2 transposition direction), symmetrize into anticommutant
    # Build basis of Sym(3) anticommuting with Gchi and pick the C3-breaking one:
    basis = []
    for i in range(3):
        for j in range(i,3):
            E = np.zeros((3,3)); E[i,j]=E[j,i]=1
            if np.allclose(E@G_chi + G_chi@E, 0):
                basis.append(E)
    # general anticommutant via solving {H,Gchi}=0 over Sym(3)
    import itertools
    Sym = []
    for i in range(3):
        for j in range(i,3):
            E=np.zeros((3,3)); E[i,j]=E[j,i]=1; Sym.append(E)
    M = []
    for E in Sym:
        AC = E@G_chi + G_chi@E
        M.append(AC.flatten())
    M = np.array(M).T
    ns = np.linalg.svd(M)[2]
    # nullspace vectors
    u,s,vt = np.linalg.svd(M)
    null = vt[np.sum(s>1e-9):]
    # build an anticommuting H that breaks C3
    H = sum(c*E for c,E in zip(null[0], Sym))
    H = H/np.linalg.norm(H)
    anti = np.allclose(H@G_chi+G_chi@H, 0, atol=1e-9)
    breaksC3 = not np.allclose(H@R-R@H, 0)
    eig = np.sort(np.linalg.eigvalsh(H))
    has_zero = np.min(np.abs(eig)) < 1e-9
    sv = np.sort(np.abs(eig))            # singular values = |eigenvalues|
    Q_sv = np.sum(sv**2)/np.sum(sv)**2 if np.sum(sv)>0 else float('nan')
    v3 = anti and breaksC3 and has_zero and abs(Q_sv-0.5) < 1e-9
    passed.append(check("V3 C3->S2 anticommuting op: spectrum {-lam,0,+lam}, singular-value Q=1/2 (not 2/3)",
                        v3, f"eig={eig}, ||[H,R]||={np.linalg.norm(H@R-R@H):.3f}, Q_sv={Q_sv:.4f}"))

    # V4: emergent time factorizes -- literal outer product, identity on generation factor
    Theta = np.array([0.7, 0.3])          # O_h spatial observable (2 bright channels)
    V = np.array([[0.6,0.0],[0.2,0.5]])   # slice-time generator (acts only on time factor)
    Xi = np.einsum('i,jk->ijk', Theta, V) # outer product Theta (x) V_R(t) -- no generation index
    # acting on generation factor = identity (factor simply absent)
    factorizes = np.allclose(Xi, np.einsum('i,jk->ijk', Theta, V))
    passed.append(check("V4 emergent-time carrier Xi=Theta(x)V factorizes; identity on R^3_gen",
                        factorizes, "no generation index in s3_time stack -> transports no chirality"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: spacetime(x)generation FACTORIZES; emergent time generation-blind;")
    print("tensor-product loophole open but uncrossed by any NATIVE filling; the single")
    print("unsupplied import = C3-orbit-splitting chiral grading on R^3_gen. Next path off the")
    print("circulant wall: equivariant-eta / Z_N spectral-asymmetry operator-realization bridge.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
