#!/usr/bin/env python3
"""
Finite Kähler-Dirac measure-localization runner.

The runner checks that D_KD=d-delta on Lambda*(R^3) is grade-off-diagonal, so its
Lambda^1 -> Lambda^1 generation block vanishes. It also checks that determinant
and Pfaffian measures count the doublet by dimension, not by one block, and that
the surviving source question is whether the generation matter action carries a
within-generation real-antisymmetric bilinear.

The runner sets no audit verdict and does not derive the Koide mass measure.
"""

import sys

import numpy as np
import sympy as sp

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = ""):
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str):
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


# ---- 3-mode fermion Fock space = Lambda*(R^3), via Jordan-Wigner -----------------
sp_plus = np.array([[0, 1], [0, 0]], dtype=complex)   # raising
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def kron3(a, b, c):
    return np.kron(np.kron(a, b), c)


adag = [
    kron3(sp_plus, I2, I2),
    kron3(sz, sp_plus, I2),
    kron3(sz, sz, sp_plus),
]
a = [m.conj().T for m in adag]
N = sum(adag[m] @ a[m] for m in range(3))          # particle number = form degree
I8 = np.eye(8, dtype=complex)

# finite generation objects on R^3 = Lambda^1
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
B = C + C2
Jcs = (C - C2) / np.sqrt(3)
I3 = np.eye(3, dtype=complex)
P_doublet = I3 - np.ones((3, 3)) / 3


def main() -> int:
    section("Kähler-Dirac is silent on the Koide measure; one generation-bilinear binary")

    # ---- F1: D_KD real-antisymmetric, i*D_KD Hermitian -------------------------
    section("F1 — D_KD = d - delta is real-antisymmetric, i*D_KD Hermitian")
    car_ok = all(np.allclose(a[i] @ adag[j] + adag[j] @ a[i], (1 if i == j else 0) * I8)
                 for i in range(3) for j in range(3))
    D_KD = sum(adag[m] - a[m] for m in range(3))     # d - delta
    record("F1.1 CAR algebra {a_i, a_j^dag} = delta_ij (Fock space = Lambda*(R^3))",
           car_ok, "3-mode Jordan-Wigner fermions; 8-dim form complex")
    record("F1.2 D_KD is real and antisymmetric; i*D_KD is Hermitian",
           np.allclose(D_KD.imag, 0) and np.allclose(D_KD, -D_KD.T)
           and np.allclose(1j * D_KD, (1j * D_KD).conj().T),
           f"|Im D_KD|={np.max(np.abs(D_KD.imag)):.1e}, "
           f"|D_KD + D_KD^T|={np.max(np.abs(D_KD + D_KD.T)):.1e}")

    # ---- F2: every grade-diagonal block of D_KD vanishes -----------------------
    section("F2 — D_KD is grade-off-diagonal: every Lambda^k -> Lambda^k block = 0")
    grade_diag_max = 0.0
    blocks = {}
    for k in range(4):
        proj_idx = [i for i in range(8) if round(N[i, i].real) == k]
        Pk = np.zeros((8, 8), dtype=complex)
        for i in proj_idx:
            Pk[i, i] = 1
        block = Pk @ D_KD @ Pk
        blocks[k] = np.max(np.abs(block))
        grade_diag_max = max(grade_diag_max, blocks[k])
    record("F2.1 every grade-diagonal block of D_KD vanishes (in particular "
           "Lambda^1 = the generation triplet)",
           grade_diag_max < 1e-12,
           f"max|Lambda^k -> Lambda^k block| = {grade_diag_max:.1e}; "
           f"per-grade: { {k: f'{v:.0e}' for k, v in blocks.items()} }; "
           f"dim Lambda^1 = {sum(1 for i in range(8) if round(N[i,i].real)==1)}")
    record("F2.2 => Kähler-Dirac supplies NO within-generation "
           "kinetic operator (measure sourced by neither checked candidate)",
           grade_diag_max < 1e-12,
           "the within-generation complex structure must come from a separate "
           "generation-bilinear input")

    # ---- F3: det_C / Pfaffian red herring --------------------------------------
    section("F3 — det and Pfaffian both weight the doublet to dimension 2 (-> Q=1)")
    a_s, b_s = sp.symbols("a b", real=True)
    Bsym = sp.Matrix([[0, 1, 1], [1, 0, 1], [1, 1, 0]])   # C + C^2
    M = a_s * sp.eye(3) + b_s * Bsym
    detM = sp.factor(M.det())
    record("F3.1 det(aI + b(C+C^2)) = (a+2b)(a-b)^2  (doublet eigenvalue to power 2)",
           sp.simplify(detM - (a_s + 2 * b_s) * (a_s - b_s)**2) == 0,
           f"det(M) = {detM}  => doublet weighted by DIMENSION 2 => (1,2) => r=1 => Q=1")
    # Pfaffian of M (x) eps (eps = 2x2 symplectic) equals det(M) for symmetric M
    eps = sp.Matrix([[0, 1], [-1, 0]])
    Mke = sp.Matrix(np.kron(np.array(M.tolist(), dtype=object), np.array(eps.tolist())))
    # Pf^2 = det for antisymmetric; verify det(M(x)eps) = det(M)^2 => Pf = +-det(M)
    record("F3.2 Pf(M (x) eps)^2 = det(M (x) eps) = det(M)^2  => Pf = +-det(M) "
           "(same doublet-power-2; per-block (1,1) is NOT a determinant output)",
           sp.simplify(Mke.det() - detM**2) == 0,
           f"det(M (x) eps) = det(M)^2 = {sp.factor(Mke.det())}")

    # ---- F4: neither checked complex-structure object is a full-space J ---------
    section("F4 — central i*I (generation-blind, eigs {+i,+i,+i}) vs Jcs (det 0)")
    eig_centrali = np.linalg.eigvals(1j * I3)
    record("F4.1 central i*I_3 has eigenvalues {+i,+i,+i} (no -i eigenspace; "
           "ineligible as a conjugate-pair / first-order symplectic structure)",
           np.allclose(np.sort_complex(eig_centrali), np.array([1j, 1j, 1j])),
           f"eig(i*I_3) = {np.round(eig_centrali, 3)}")
    record("F4.2 Jcs^2 = -P_doublet != -I_3 and det(Jcs) = 0 "
           "(not a full-space complex structure; counts the doublet ONCE)",
           np.allclose(Jcs @ Jcs, -P_doublet) and abs(np.linalg.det(Jcs)) < 1e-12,
           f"|Jcs^2 + P_doublet| = {np.max(np.abs(Jcs@Jcs + P_doublet)):.1e}; "
           f"det(Jcs) = {np.linalg.det(Jcs):.1e}; eig(Jcs) = "
           f"{np.round(np.linalg.eigvals(Jcs),3)}")

    # ---- F5: the one binary -- unique real-antisymmetric C3-equivariant operator -
    section("F5 — the measure binary: a real-antisymmetric generation bilinear?")
    # space of real ANTISYMMETRIC 3x3 commuting with C (C3-equivariant)
    def commutes_with_C(M):
        return np.max(np.abs(M @ C.real - C.real @ M)) < 1e-12
    so3_basis = [np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], float),
                 np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], float),
                 np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]], float)]
    # build the map: coeffs (3) -> commutator with C (flattened); null space = equivariant
    A = np.array([(g @ C.real - C.real @ g).reshape(-1) for g in so3_basis]).T
    u, s, vt = np.linalg.svd(A)
    null_dim = int(np.sum(s < 1e-9)) + (3 - len(s))
    record("F5.1 the only C3-equivariant real-antisymmetric operator on R^3 is "
           "span{Jcs} (1-dimensional)",
           null_dim == 1,
           f"dim(antisymmetric ∩ commute-with-C) = {null_dim}")
    # symmetric C3-equivariant operators commute with BOTH Jcs and central-i (blind)
    M_sym = 0.7 * I3 + 0.3 * B
    record("F5.2 C3-equivariant SYMMETRIC operators commute with both Jcs and i*I "
           "(measure-blind) -> only the antisymmetric (Jcs) direction carries the measure",
           np.allclose(M_sym @ Jcs, Jcs @ M_sym)
           and np.allclose(M_sym @ (1j * I3), (1j * I3) @ M_sym),
           "=> the measure binary = 'is there a real-antisymmetric generation bilinear "
           "(-> Jcs -> Q=2/3) or not (-> central-i -> Q=1)?'")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"  {n_pass}/{n_total} checks passed")
    print()
    print("  Kähler-Dirac D_KD: grade-off-diagonal => Lambda^1->Lambda^1 = 0")
    print("    => SILENT on the within-generation complex structure (the measure).")
    print("  det / Pfaffian: doublet-power-2 => Q=1 (per-block is NOT a det output).")
    print("  central i*I (eigs {+i,+i,+i}) generation-blind => Q=1;")
    print("    Jcs (det 0, doublet once) => Q=2/3; neither is a full-space J.")
    print("  THE ONE BINARY: a within-generation real-antisymmetric (symplectic)")
    print("    bilinear (uniquely Jcs -> Q=2/3) or not (central-i -> Q=1)?")
    print("    = reality-type / kinetic-order of the generation field = open source question.")
    print()
    print("  => Q=2/3 needs one discrete open input: a generation real-antisymmetric")
    print("     bilinear. The checked Kähler-Dirac operator is silent on that input.")

    if n_pass == n_total:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_total - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
