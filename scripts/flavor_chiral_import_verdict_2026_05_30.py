#!/usr/bin/env python3
"""
Chiral-import derivation press (workflow wf_95d69898) + the two unrun routes
executed/reasoned here. VERDICT: the single irreducible pin is the Koide VALUE
r=|b|^2/a^2 = 1/2 (a CONTINUOUS modulus); no identified native route forces it.

WHAT THE PRESS ESTABLISHED (7 angles, 0 native derivations):
- Cl(3) volume omega=e1e2e3=iI is CENTRAL (no chiral action on states) -- fails.
- anomaly/'t Hooft is flavor-symmetric -> reaches only DISCRETE data (count, charges),
  cannot select a generation operator -- fails.
- the native spacetime chirality eps=(-1)^(x+y+z) (retained cpt_exact) is GENERATION-BLIND.
- the native antiunitary T acts as b->bbar (complex conjugation), which SUPPRESSES the
  orientation (forces Im b=0 -> degenerate) -- wrong sign.
- the three retained no-gos are airtight for their routes; the only unforbidden gap is a
  native C3-NON-equivariant operator (joint-commutant characterization not yet done).

THE TWO UNRUN ROUTES, now executed/reasoned:
(II) qubit-factor grading [RUN HERE]: on C^2(qubit) (x) R^3(gen), grading sigma3 (x) I3
     (signature (3,3), balanced). D=[[0,A],[A^dag,0]] anticommutes with it automatically
     and has 3 distinct masses = singular values of A. BUT the masses are the SINGULAR-VALUE
     (Yukawa) readout of A, which is generic for generic A and theta-dependent <=2/3 for
     circulant A (verified: circulant r=1/2,theta=0 -> Q=0.4317, NOT 2/3). The (1,2)
     generation grading that gives Q=2/3 (signed-eigenvalue/Brannen) is NOT supplied by the
     (3,3) qubit grading. So escape (II) RELOCATES the import to 'A has Koide singular values'
     and forces the WRONG (singular-value) readout -> does NOT force 2/3.
(anomaly) discrete Z3 cobordism: anomalies are topological/DISCRETE; r=1/2 is a CONTINUOUS
     modulus -> category mismatch (same as the time-emergence panel) -> cannot force r=1/2.

CORRECTION to my earlier framing (phase-dof / move-1 notes): the antisymmetric generator
i(C-C^2) is part of the CIRCULANT (= Im b), is C3-EQUIVARIANT, and COMMUTES with Gamma_chi --
it is NOT the chiral import. A circulant with complex b already gives 3 DISTINCT masses while
commuting with Gamma_chi (verified). So the import is NOT 'the antisymmetric dof for
3-distinctness'; 3-distinctness needs only the orientation theta!=0, which may be NATIVE
(positivity_orientation_selects_c3, retained_bounded -- positivity selects the C3 orientation).
The single irreducible pin is specifically the VALUE r=1/2 (b/a=1/sqrt2), i.e. the
eigenvector-cone condition <v|Gamma_chi|v>=0.

HONEST VERDICT: the charged-lepton flavor structure decomposes as
  - n_gen=3 (count): DERIVED (retained three_generation_hw1).
  - 3 distinct masses: needs orientation theta!=0, possibly NATIVE (positivity selects C3).
  - Q=2/3 (the VALUE r=1/2): the SINGLE irreducible pin -- a continuous modulus no native
    route forces (measure->1, dynamics->1/3, criticality->inf, Cl(3) volume central, anomaly
    discrete, time-arrow->orientation-not-value, reflection->suppresses, qubit-factor->wrong
    readout). Reproduced (given the pin, Q=2/3 derived via retained koide_anticommuting_operator)
    but NOT derived. = the same single pin shared across Koide/quark/generation-ID/strong-CP.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    s3 = np.diag([1, 1, 1, -1, -1, -1.0])
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)

    def D_of(A):
        Z = np.zeros((3, 3), complex); return np.block([[Z, A], [A.conj().T, Z]])

    def Qsv(A):
        sv = np.linalg.svd(A, compute_uv=False)
        return sv.sum() / np.sqrt(sv).sum() ** 2, np.round(np.sort(sv), 3)

    sep("Escape (II): qubit-factor grading sigma3(x)I3 -- anticommutes, but wrong readout")
    A = np.random.RandomState(0).randn(3, 3) + 1j * np.random.RandomState(1).randn(3, 3)
    print("  {D, sigma3(x)I3}=0 ?", np.allclose(D_of(A) @ s3 + s3 @ D_of(A), 0), "(anticommutation NATIVE via qubit)")
    print("  circulant A=aI+bC+bbar C^2, singular-value (Yukawa) Q:")
    for r in [0.5, 1.0]:
        for th in [0.0, 0.6]:
            b = np.sqrt(r) * np.exp(1j * th); A2 = np.eye(3) + b * C + np.conj(b) * C.conj().T
            q, sv = Qsv(A2); print(f"    r={r:.1f} th={th:.1f}: Q={q:.4f} sv={sv}")
    print("  r=1/2 gives Q=0.43 (singular-value readout), NOT 2/3 -> escape (II) does not force 2/3.")

    sep("Correction: i(C-C^2) is circulant (commutes with Gamma_chi), gives 3-distinct natively")
    Gx = (2 / 3) * np.ones((3, 3)) - np.eye(3)
    H = np.eye(3) + (0.4 * np.exp(1j * 0.8)) * C + np.conj(0.4 * np.exp(1j * 0.8)) * C.conj().T  # complex b
    ev = np.linalg.eigvalsh(H)
    print(f"  circulant H (complex b): eigenvalues {np.round(ev,3)} -> {len(set(np.round(ev,3)))} DISTINCT")
    print(f"  [H, Gamma_chi]=0 ? {np.allclose(H@Gx-Gx@H,0)}  (commutes -> i(C-C^2) is NOT the chiral import)")
    print("  => 3-distinctness comes from the circulant orientation (theta), NOT an anticommuting op.")

    sep("VERDICT")
    print("  Single irreducible pin = the Koide VALUE r=|b|^2/a^2=1/2 (a CONTINUOUS modulus).")
    print("  No native route forces it (measure->1, dynamics->1/3, criticality->inf, Cl(3) volume")
    print("  central, anomaly discrete (can't reach a continuous modulus), time-arrow->orientation")
    print("  not value, reflection->suppresses, qubit-factor escape->wrong singular-value readout).")
    print("  n_gen=3 DERIVED; 3-distinct (orientation) possibly NATIVE (positivity selects C3);")
    print("  Q=2/3 reproduced-not-derived = the one shared chiral/value pin = observed SM content.")


if __name__ == "__main__":
    main()
