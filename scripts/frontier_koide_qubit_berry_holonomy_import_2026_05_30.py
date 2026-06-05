#!/usr/bin/env python3
"""
Qubit-factor Berry holonomy on R^3 (x) C^2: faithful embedding gives ZERO;
nonzero requires an import; and even then it is r-non-selective.

CONTEXT. The charged-lepton Koide value Q=2/3 <=> r=|b|^2/a^2 = 1/2 reduces to one
object: whether the native generation matter action carries a symplectic form omega
(Kähler -> count 1 -> Q=2/3) or not (Hermitian -> count 2 -> Q=1). On the BARE
generation R^3 factor omega is forced-absent (circulant flatness: the C3-equivariant
mass operator Hgen(a,br,bi)=a I + br B + bi (i Jcs) is simultaneously diagonal in the
b-INDEPENDENT C3-Fourier basis, so the Berry curvature over the complex-b plane is 0;
this is the koide_z3_equivariant_anticommuting_no_go wall). The one
open seam the equivariant-eta route named: tensor with the NATIVE qubit C^2 from the Quantum baseline,
where the C3-equivariant anticommutant of B(x)sigma_z is dim 6 (vs dim 0 for B(x)I2),
and a Berry phase can be nonzero where the eta-index is blind (+/- symmetric spectrum).

This runner runs that never-executed computation FROM SCRATCH and certifies:

  F1  EQUIVARIANT ANTICOMMUTANT DIMS: dim{X : {X, B(x)s}=0, [X, C(x)I2]=0} is
      0 for s=I2 (bare-tensor wall) and 6 for EACH of s=sx,sy,sz (sigma_z is
      UNPRIVILEGED -- the three are qubit-SU(2)-related).
  F2  FAITHFUL EMBEDDING -> ZERO. The faithful image of b=|b|e^{i delta},
      M(delta) = (cos d * B + sin d * (i Jcs)) (x) sigma_z  (+ coin t I(x)sx),
      has sigma_y component IDENTICALLY 0 per Fourier mode (B, i Jcs circulant and
      commuting), so the loop is PLANAR -> zero solid angle -> the gauge-invariant
      lowest-band Berry holonomy = 0 EXACTLY (Wilson-loop and Uhlmann/projector agree).
      The bare-R^3 flatness persists verbatim into the tensor seam.
  F3  NONZERO REQUIRES IMPORT. A nonzero gapped holonomy appears only for the
      NON-COLLINEAR coin B(x)(cos d sigma_z + sin d sigma_y); but B(x)sigma_y is
      Hilbert-Schmidt ORTHOGONAL to the entire (i Jcs)(x)* sector, so it is NOT the
      faithful image of arg(b) -- it is the C3-orbit-splitting chiral grading inserted
      by hand (the import). Its holonomy is Gamma(r) = -pi(1 - 1/sqrt(1+4r)).
  F4  IMPORT IS r-NON-SELECTIVE. Gamma(r) is smooth and strictly monotone:
      dGamma/dr != 0 at r=1/2 (no stationarity / quantization / kink there). It hits
      |Gamma|=2/9 rad at r ~ 0.0395, |Gamma|=2pi/9 at r ~ 0.163, the clean -2pi/3 at
      r=2 -- NEVER at the value point r=1/2 (where Gamma = -pi(1-1/sqrt3), an irrational
      multiple of pi). So r=1/2 / 2/9 are never selected; only the holonomy's EXISTENCE
      is (and that existence is import-sourced).

CONCLUSION (negative / structural localization, NOT a closure): the qubit-factor Berry
route does NOT natively source omega / r=1/2 / Q=2/3. It maps WHERE the r=1/2-selecting
principle is missing -- it is the single chiral import shared with Koide-Q and
generation-ID (a C3-orbit-splitting qubit grading / the inter-axis relative-i, which
breaks the SU(2) frame symmetry and is not supplied by the Lattice + Quantum + Record
baseline) -- it does not supply it. The next open path: whether the framework baseline
forces a nontrivial qubit Z3/chiral action that canonically picks the relative axis
(not shown here; needs its own derivation or an explicitly approved input).

BOUNDARY HONESTY: the bare-tensor wall (F1, dim 0 for B(x)I2) and the bare-R^3
flatness are reproduced exactly here. This runner's numbers are first-principles
and reproducible, but this script does not set any status verdict.
"""

import sys

import numpy as np
from scipy.optimize import brentq

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


# ---- native objects -------------------------------------------------------------
w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)  # cyclic shift, C^3=I
C2 = C @ C
B = C + C2                       # spec {-1,-1,2}; real symmetric doublet coupling
Jcs = (C - C2) / np.sqrt(3)      # anti-Hermitian complex structure; [B, iJcs]=0
iJ = 1j * Jcs                    # Hermitian, spec {0, +1, -1}
I3 = np.eye(3, dtype=complex)
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
g = np.kron(C, I2)               # C3 generation action on R^3 (x) C^2

# Fourier basis of C3 (columns are eigenvectors of C)
F = np.array([[1, 1, 1], [1, w, w**2], [1, w**2, w]], dtype=complex) / np.sqrt(3)
# per-mode eigenvalues of B and iJ in the Fourier basis
Bk = np.round(np.real(np.diag(F.conj().T @ B @ F)), 10)      # (2, -1, -1)
Jk = np.round(np.real(np.diag(F.conj().T @ iJ @ F)), 10)     # (0, -1, +1)


def equivariant_anticommutant_dim(O: np.ndarray) -> int:
    """dim_C { X (6x6) : X O + O X = 0  and  X g - g X = 0 }."""
    n = O.shape[0]
    Ic = np.eye(n, dtype=complex)
    # vec(X O + O X) = (O^T (x) I + I (x) O) vec(X);  vec(X g - g X) = (g^T(x)I - I(x)g)
    anti = np.kron(O.T, Ic) + np.kron(Ic, O)
    equi = np.kron(g.T, Ic) - np.kron(Ic, g)
    M = np.vstack([anti, equi])
    # complex null space dimension = n^2 - rank
    rank = np.linalg.matrix_rank(M, tol=1e-9)
    return n * n - rank


def lowest_band_states(Hfun, deltas):
    out = []
    for d in deltas:
        vals, vecs = np.linalg.eigh(Hfun(d))
        out.append(vecs[:, np.argmin(vals)])
    return out


def min_gap(Hfun, deltas, lower_index=0):
    gaps = []
    for d in deltas:
        ev = np.sort(np.linalg.eigvalsh(Hfun(d)))
        gaps.append(ev[lower_index + 1] - ev[lower_index])
    return float(np.min(gaps))


def berry_wilson(states):
    """Fukui-Hatsugai gauge-invariant Wilson-loop Berry phase (closed loop)."""
    prod = 1.0 + 0j
    n = len(states)
    for i in range(n):
        z = np.vdot(states[i], states[(i + 1) % n])
        prod *= z / abs(z)
    return float(np.angle(prod))


def berry_uhlmann(states):
    """Projector (Pancharatnam/Uhlmann) holonomy: arg tr(P0 P1 ... P_{N-1}).

    tr(P0 P1 ... P_{N-1}) = <u0|u1><u1|u2>...<u_{N-1}|u0> (closed loop via trace
    cyclicity), so its argument matches the Wilson-loop phase in sign & magnitude.
    """
    P = [np.outer(s, s.conj()) for s in states]
    M = P[0]
    for i in range(1, len(states)):
        M = M @ P[i]
    return float(np.angle(np.trace(M)))


def block_lower_berry(hfun, deltas):
    """Lower-band Wilson-loop Berry phase of a 2-level block (gapped along loop)."""
    st = []
    for d in deltas:
        vals, vecs = np.linalg.eigh(hfun(d))
        st.append(vecs[:, np.argmin(vals)])
    return berry_wilson(st)


def main() -> int:
    section("Qubit-factor Berry holonomy on R^3 (x) C^2 — import-confirmed")
    print(f"  per-mode B eigenvalues   Bk = {tuple(Bk)}")
    print(f"  per-mode iJ eigenvalues  Jk = {tuple(Jk)}")

    # ---- F1: equivariant anticommutant dims ------------------------------------
    section("F1 — C3-equivariant anticommutant dims (sigma_z UNPRIVILEGED)")
    dims = {name: equivariant_anticommutant_dim(np.kron(B, s))
            for name, s in [("I2", I2), ("sx", sx), ("sy", sy), ("sz", sz)]}
    record("F1.1 dim anticommutant of B(x)I2 = 0 (bare-tensor wall holds)",
           dims["I2"] == 0, f"dim = {dims['I2']}")
    record("F1.2 dim of B(x)sx = B(x)sy = B(x)sz = 6 (sigma_z unprivileged)",
           dims["sx"] == 6 and dims["sy"] == 6 and dims["sz"] == 6,
           f"dims: sx={dims['sx']}, sy={dims['sy']}, sz={dims['sz']}")

    # ---- F2: faithful embedding -> zero ----------------------------------------
    section("F2 — faithful embedding of arg(b) -> Berry holonomy = 0 EXACTLY")
    a, bmag, t = 1.0, 1.0, 0.7   # generic; r=|b|^2/a^2=1 here, swept below

    def H_faithful(delta, a=a, bmag=bmag, t=t):
        mass = (np.cos(delta) * B + np.sin(delta) * iJ)
        return a * np.kron(I3, I2) + bmag * np.kron(mass, sz) + t * np.kron(I3, sx)

    # per-mode qubit d-vector has sigma_y component identically 0
    deltas = np.linspace(0, 2 * np.pi, 400, endpoint=False)
    max_dy = 0.0
    for k in range(3):
        for d in deltas:
            mz = bmag * (np.cos(d) * Bk[k] + np.sin(d) * Jk[k])
            hk = a * I2 + mz * sz + t * sx          # qubit block
            dy = np.real(0.5 * np.trace(hk @ sy))    # sigma_y coefficient
            max_dy = max(max_dy, abs(dy))
    record("F2.1 sigma_y component of every Fourier-mode qubit block ≡ 0",
           max_dy < 1e-12, f"max |d_y| over modes & loop = {max_dy:.2e}")

    # The modes DECOUPLE (block diagonal in the Fourier basis); the global lowest
    # band crosses, so the correct gauge-invariant objects are (i) each gapped 2x2
    # mode block's lower-band phase and (ii) the non-abelian holonomy on the isolated
    # lower-3-band subspace (gap to upper = 2t).
    def hk_faithful(k):
        return lambda d: a * I2 + bmag * (np.cos(d) * Bk[k] + np.sin(d) * Jk[k]) * sz + t * sx
    per_mode = [block_lower_berry(hk_faithful(k), deltas) for k in range(3)]
    gap3 = min_gap(H_faithful, deltas, lower_index=2)   # ev3-ev2 isolates lower 3
    record("F2.2 every gapped Fourier-mode lower-band Berry phase = 0 (planar loop)",
           all(abs(p) < 1e-6 for p in per_mode),
           f"per-mode Berry = {[round(p, 8) for p in per_mode]}; "
           f"lower-3-band gap to upper = {gap3:.3f}")

    # non-abelian Wilson loop on the isolated lower-3 subspace -> trivial (|det|=1, phase 0)
    def lower3_frame(d):
        vals, vecs = np.linalg.eigh(H_faithful(d))
        return vecs[:, np.argsort(vals)[:3]]   # 6x3 frame of the lower 3 bands
    Wna = np.eye(3, dtype=complex)
    frames = [lower3_frame(d) for d in deltas]
    for i in range(len(deltas)):
        Wna = Wna @ (frames[i].conj().T @ frames[(i + 1) % len(deltas)])
    detphase = float(np.angle(np.linalg.det(Wna)))
    record("F2.3 non-abelian lower-3-band holonomy is trivial (det-phase = 0)",
           abs(detphase) < 1e-6, f"det-phase of Wilczek-Zee Wilson loop = {detphase:.2e}")

    # ---- F3: nonzero requires an IMPORT (non-collinear coin) --------------------
    section("F3 — nonzero holonomy requires the non-collinear coin (IMPORT)")
    # B(x)sigma_y HS-orthogonal to the entire (i Jcs)(x)* sector
    Bsy = np.kron(B, sy)
    max_overlap = 0.0
    for s in [I2, sx, sy, sz]:
        ov = abs(np.trace(Bsy.conj().T @ np.kron(iJ, s)))
        max_overlap = max(max_overlap, ov)
    record("F3.1 B(x)sigma_y is HS-orthogonal to (i Jcs)(x)* (NOT a faithful arg(b) image)",
           max_overlap < 1e-12, f"max |<B(x)sy, iJ(x)s>_HS| = {max_overlap:.2e}")

    # clean reduced import construction giving Gamma(r) = -pi(1 - 1/sqrt(1+4r)):
    # rotating in-plane field d=(2|b| cos d, 2|b| sin d, a) on the qubit
    def H_import(delta, a=a, bmag=bmag):
        return a * sz + 2 * bmag * (np.cos(delta) * sx + np.sin(delta) * sy)

    st = lowest_band_states(H_import, deltas)
    g_imp_wilson = berry_wilson(st)
    g_imp_uhl = berry_uhlmann(st)
    gap_imp = min_gap(H_import, deltas)
    expected = -np.pi * (1 - 1 / np.sqrt(1 + 4 * (bmag**2 / a**2)))
    record("F3.2 import construction: nonzero, gapped, Wilson=Uhlmann=-pi(1-1/sqrt(1+4r))",
           abs(g_imp_wilson - expected) < 1e-3 and abs(g_imp_uhl - expected) < 1e-3
           and gap_imp > 1e-6,
           f"Wilson={g_imp_wilson:.6f}, Uhlmann={g_imp_uhl:.6f}, "
           f"expected={expected:.6f}, min gap={gap_imp:.3f}")

    # ---- F4: import is r-NON-SELECTIVE -----------------------------------------
    section("F4 — Gamma(r) smooth/monotone, NOT stationary at r=1/2")

    def Gamma(r):  # closed form, cross-checked numerically below
        return -np.pi * (1 - 1 / np.sqrt(1 + 4 * r))

    # numerical Berry vs r matches closed form (random check across r)
    maxerr = 0.0
    for r in [0.05, 0.25, 0.5, 1.0, 2.0, 4.0]:
        bm = np.sqrt(r) * a
        str_ = lowest_band_states(lambda d: H_import(d, a=a, bmag=bm), deltas)
        maxerr = max(maxerr, abs(berry_wilson(str_) - Gamma(r)))
    record("F4.1 numerical Berry(r) == -pi(1-1/sqrt(1+4r)) across r",
           maxerr < 1e-3, f"max|numeric - closed form| = {maxerr:.2e}")

    dGdr_half = (Gamma(0.5 + 1e-6) - Gamma(0.5 - 1e-6)) / 2e-6
    record("F4.2 dGamma/dr != 0 at r=1/2 (NO stationarity -> not value-selective)",
           abs(dGdr_half) > 0.1,
           f"dGamma/dr|_{{r=1/2}} = {dGdr_half:.4f}; Gamma(1/2) = {Gamma(0.5):.6f} "
           f"= -pi(1-1/sqrt3) = {-np.pi*(1-1/np.sqrt(3)):.6f}")

    # special-r values: 2/9 and 2pi/9 occur OFF r=1/2; -2pi/3 at r=2
    def solve_abs(target):
        return brentq(lambda r: abs(Gamma(r)) - target, 1e-4, 50)
    r_2_9 = solve_abs(2 / 9)
    r_2pi_9 = solve_abs(2 * np.pi / 9)
    record("F4.3 |Gamma| = 2/9 rad at r~0.0395, = 2pi/9 at r~0.163, -2pi/3 at r=2 "
           "(NEVER r=1/2)",
           abs(r_2_9 - 0.0395) < 0.01 and abs(r_2pi_9 - 0.163) < 0.01
           and abs(Gamma(2.0) - (-2 * np.pi / 3)) < 1e-9,
           f"r(|G|=2/9)={r_2_9:.4f}, r(|G|=2pi/9)={r_2pi_9:.4f}, "
           f"Gamma(r=2)={Gamma(2.0):.6f} = -2pi/3={-2*np.pi/3:.6f}")

    # ---- summary ----------------------------------------------------------------
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"  {n_pass}/{n_total} checks passed")
    print()
    print("  Faithful embedding of arg(b) on R^3(x)C^2  -> Berry holonomy = 0 EXACTLY")
    print("    (bare-R^3 circulant flatness persists into the tensor seam)")
    print("  Nonzero holonomy  -> requires non-collinear coin B(x)(cos d sz+sin d sy)")
    print("    = the C3-orbit-splitting chiral IMPORT (B(x)sy _|_ iJ(x)* sector)")
    print("  Even granting the import: Gamma(r)=-pi(1-1/sqrt(1+4r)) is monotone,")
    print("    NOT stationary at r=1/2; hits 2/9 at r~0.0395, never r=1/2.")
    print()
    print("  => qubit-factor Berry route does NOT natively source omega / r=1/2 / Q=2/3.")
    print("     It maps where the r=1/2 principle is missing (the shared chiral import),")
    print("     it does not supply it. Next open path: does the framework baseline")
    print("     force a nontrivial qubit Z3/chiral action that canonically picks the relative axis?")

    if n_pass == n_total:
        print("\nALL CHECKS PASSED")
        return 0
    print(f"\n{n_total - n_pass} CHECK(S) FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
