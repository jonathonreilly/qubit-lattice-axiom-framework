#!/usr/bin/env python3
"""Class-A verifier: the TM2 magic residual generator is a native dynamical unitary.

Verifies, on the hw=1 generation triplet V1 = span{|100>,|010>,|001>}:

  (A) the magic reflection S = 2|W><W| - I (W = C3-singlet (1,1,1)/sqrt3) is NOT a
      static S3 permutation (non-monomial; S3 has no V4 subgroup by Lagrange);
  (B) S = exp(i*pi/3*(C + C^dag)) up to a global phase -- the time-pi/3 evolution of
      the democratic C3-symmetric coupling H_dem = C + C^dag;
  (C) <S, P23> = the Klein four-group V4;
  (D) M_nu invariant under V4 + charged leptons diagonal => TM2 magnitudes
      (exact trimaximal column, mu-tau modulus, sin^2 theta23 = 1/2) with theta13 FREE
      (NOT the TM3 overshoot of a full circulant);
  (E) a W-preserving (magic-S-commuting) M_nu realizes theta13 in the observed band
      while keeping the exact trimaximal column -- so W-preservation is NOT excluded by
      theta13 (the "must break the democratic structure" reading tests only full
      circulant => TM3).

All checks are finite-dimensional linear algebra (class A).
"""

from __future__ import annotations
import numpy as np
import itertools

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ---- carrier objects ----
w = np.ones(3) / np.sqrt(3)                       # C3-singlet / democratic / W-state
PW = np.outer(w, w)                               # projector onto W
S = 2 * PW - np.eye(3)                            # magic reflection
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)   # C3 cyclic shift
Hdem = C + C.conj().T                             # democratic C3-symmetric coupling
P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=float)   # graph-first mu-tau swap
# doublet (W-orthogonal) plane basis
u1 = np.array([2, -1, -1]) / np.sqrt(6)
u2 = np.array([0, 1, -1]) / np.sqrt(2)


def is_monomial(M, tol=1e-9):
    cols = all(np.count_nonzero(np.abs(M[:, j]) > tol) == 1 for j in range(3))
    rows = all(np.count_nonzero(np.abs(M[i, :]) > tol) == 1 for i in range(3))
    return cols and rows


def group_closure(gens, tol=1e-9):
    G = [np.eye(3, dtype=complex)]
    changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                gh = g @ h
                if not any(np.allclose(gh, x, atol=tol) for x in G):
                    G.append(gh); changed = True
    return G


def expm_spectral(H, t):
    """exp(i t H) for Hermitian H via numpy eigendecomposition (numpy-only)."""
    vals, vecs = np.linalg.eigh(H)
    return vecs @ np.diag(np.exp(1j * t * vals)) @ vecs.conj().T


def angles_present(P):
    """min |U|^2 over the matrix == a proxy for sin^2 theta13 (smallest mixing)."""
    return P.min()


def main() -> int:
    print("=" * 72)
    print("PMNS TM2 MAGIC RESIDUAL -- NATIVE DYNAMICAL GENERATOR (class A)")
    print("=" * 72)

    # ---- (A) magic S basic structure + not a static S3 element ----
    eig = np.sort(np.linalg.eigvalsh(S))
    check("S has spectrum {-1,-1,+1}", np.allclose(eig, [-1, -1, 1]),
          detail=f"eig={np.round(eig,4).tolist()}")
    check("S is an involution (S^2 = I)", np.allclose(S @ S, np.eye(3)))
    check("S fixes the C3-singlet W (S W = W)", np.allclose(S @ w, w))
    perms = [np.array([[1.0 if p[i] == j else 0.0 for j in range(3)]
                       for i in range(3)]) for p in itertools.permutations(range(3))]
    check("S equals NO S3 permutation matrix", not any(np.allclose(S, P) for P in perms))
    check("S is non-monomial (not reachable by permutations+phases)", not is_monomial(S))
    check("S3 has no V4 subgroup (Lagrange: 4 does not divide 6)", (6 % 4) != 0)

    # ---- (B) S = exp(i pi/3 (C+Cdag)) up to global phase ----
    # H_dem = C + Cdag = C + C^2 = J - I exactly: the native SECOND-ORDER double-shift
    # corner coupling P(sum_{a<b} S_a S_b)P^T = J - I (retained_bounded), NOT a first-order
    # edge -- a single shift P S_mu P^T = 0 vanishes on the hw=1 generation triplet.
    Jall = np.ones((3, 3))
    check("H_dem = C + Cdag equals J - I (native double-shift corner coupling)",
          np.allclose(Hdem, Jall - np.eye(3)))
    hdem_eig = np.sort(np.linalg.eigvalsh(Hdem))
    check("H_dem=C+Cdag spectrum {-1,-1,+2} (W non-degenerate, complement degenerate)",
          np.allclose(hdem_eig, [-1, -1, 2]), detail=f"eig={np.round(hdem_eig,4).tolist()}")
    U = expm_spectral(Hdem, np.pi / 3)
    # Hilbert-Schmidt overlap |<U,S>|/3 == 1  <=>  U = (global phase) * S.
    # For U = exp(i a) S with S^2 = I: hs = tr(U^dag S)/3 = exp(-i a), so the global
    # phase is gphase = conj(hs) = exp(i a) and U = gphase * S.
    hs = np.trace(U.conj().T @ S) / 3.0
    check("exp(i pi/3 H_dem) = global-phase * S  (|<U,S>|/3 = 1)",
          np.isclose(abs(hs), 1.0, atol=1e-12), detail=f"|hs|={abs(hs):.12f}")
    gphase = np.conj(hs) / abs(hs)
    check("global phase is exp(2 i pi/3)", np.isclose(gphase, np.exp(2j * np.pi / 3), atol=1e-9))
    check("U = global-phase * magic S exactly", np.allclose(U, gphase * S, atol=1e-12))

    # ---- (C) <S,P23> = Klein V4 ----
    V = group_closure([S.astype(complex), P23.astype(complex)])
    check("<S,P23> has order 4", len(V) == 4)
    check("<S,P23> is abelian", all(np.allclose(a @ b, b @ a) for a in V for b in V))
    check("<S,P23> all elements are involutions => Klein V4",
          all(np.allclose(g @ g, np.eye(3)) for g in V))

    # ---- (D) M_nu V4-invariant + charged-diagonal => TM2 (not TM3) ----
    rng = np.random.default_rng(7)
    A = rng.standard_normal((3, 3)); A = A + A.T
    M = A.copy()
    for g in V:
        M = (M + g.real @ M @ g.real.T) / 2.0       # symmetrize over V4
    M = (M + M.T) / 2.0
    check("symmetrized M_nu commutes with magic S", np.allclose(S @ M, M @ S))
    check("symmetrized M_nu commutes with P23", np.allclose(P23 @ M, M @ P23))
    check("V4-invariant M_nu is NOT circulant (doublet not forced degenerate)",
          not np.allclose(C.real @ M, M @ C.real))
    en, Un = np.linalg.eigh(M)
    Pm = np.abs(np.eye(3) @ Un) ** 2                  # charged diagonal => PMNS = U_nu
    tri = [j for j in range(3) if np.allclose(Pm[:, j], 1 / 3, atol=1e-9)]
    check("PMNS has an exact trimaximal column (|U|^2 = 1/3)", len(tri) >= 1,
          detail=f"col={tri}")
    check("PMNS mu-tau modulus |U_mu i|^2=|U_tau i|^2 (rows 1,2 equal)",
          np.allclose(Pm[1, :], Pm[2, :], atol=1e-9))
    # sin^2 theta23 = 1/2 from a column split equally between mu,tau
    s23 = any(np.isclose(Pm[1, j], Pm[2, j]) and np.isclose(Pm[1, j], (Pm[1, j]+Pm[2, j])/2)
              for j in range(3))
    check("maximal atmospheric: a column splits 1/2 : 1/2 over mu,tau", s23)

    # ---- (E) W-preserving M_nu can hit observed theta13 (TM2, not TM3) ----
    # negative control: full circulant neutrino => TM3 overshoot (theta13 proxy = 1/3)
    Mcirc = (2.0 * np.eye(3) + (0.3 + 0.1j) * C + (0.3 - 0.1j) * C.conj().T)
    enc, Unc = np.linalg.eigh(Mcirc)
    Pcirc = np.abs(np.eye(3) @ Unc) ** 2
    check("NEG CONTROL: full-circulant neutrino => all |U|^2=1/3 (TM3, theta13=1/3 overshoot)",
          np.allclose(Pcirc, 1 / 3, atol=1e-9), detail="this is what 'must break W' tested")
    # W-preserving (magic-S only) tilt: a|W><W| + 2x2 B on doublet plane, scan for small theta13
    D = np.column_stack([u1, u2])
    found = None
    rng2 = np.random.default_rng(3)
    for _ in range(20000):
        a = rng2.uniform(-1, 1); b = rng2.uniform(-1, 1, 3)
        B = np.array([[b[0], b[2]], [b[2], b[1]]])
        Mw = a * PW + D @ B @ D.T
        enw, Uw = np.linalg.eigh(Mw)
        Pw = np.abs(np.eye(3) @ Uw) ** 2
        if any(np.allclose(Pw[:, j], 1 / 3, atol=1e-9) for j in range(3)) and 0.015 < Pw.min() < 0.030:
            found = Pw.min(); break
    check("W-preserving M_nu hits theta13 in observed band 0.015-0.030 WITH exact trimaximal column",
          found is not None, detail=f"sin^2 theta13 proxy={found:.4f}" if found else "none")
    check("=> W-preservation (TM2) is NOT excluded by theta13; only full circulant (TM3) is",
          found is not None)

    # ---- negative control: charged CIRCULANT destroys the trimaximal column ----
    Uc = Unc                                          # circulant charged-lepton eigenbasis (DFT)
    Pdestroy = np.abs(Uc.conj().T @ Un) ** 2
    check("NEG CONTROL: charged-circulant rotation destroys the trimaximal column",
          not any(np.allclose(Pdestroy[:, j], 1 / 3, atol=1e-6) for j in range(3)))

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: dynamical-magic-generator narrow theorem FAILED.")
        return 1
    print("VERDICT: TM2 magic residual is a native dynamical unitary; "
          "trimaximal-column gap reduces to M_nu V4-invariance (W-preservation).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
