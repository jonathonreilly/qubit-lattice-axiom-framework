#!/usr/bin/env python3
"""P2 finite determinant/relabeling boundary manifest.

In-repo verification companion for
docs/OBSERVABLE_PRINCIPLE_P2_DET_REALIZATION_BRIDGE_CONDITIONAL_ON_FERMIONIC_FRAME_NARROW_THEOREM_NOTE_2026-05-28.md.

This runner re-exhibits, on finite carriers, the finite determinant and
relabeling facts that the 2026-06-07 source boundary now makes direct. The
physical realization reading remains conditional on FS, on the actual
matter-operator identification D = M_KS, on determinant-to-trace routing, and on
the premise that AC_phi_lambda is only an S_3 relabeling of the hw=1 triplet.

  BLOCK 1 -- BEREZIN GAUSSIAN-DETERMINANT IDENTITY.
    The fermion partition function is the finite Grassmann Gaussian
        Z_F[M] = int prod_x dchi-bar_x dchi_x exp(-sum_xy chi-bar_x M_xy chi_y)
               = det(M),
    for any complex matrix M. We compute Z_F via the permutation-expansion
    Berezin formula and match sympy's exact det(M) for generic 1x1, 2x2, 3x3 M.
    (Method re-used from the retained Berezin runner
    scripts/audit_companion_spin_statistics_berezin_determinant_exact_2026_05_10.py.)
    Setting the supplied M = D + J, this is the bridge core: the readout is
    det(D+J) on that supplied frame.

  BLOCK 2 -- STAGGERED DETERMINANT POSITIVITY (zero-source surface).
    Build the free staggered Kogut-Susskind operator M_KS (clean temporal hop
    eta_t=1, spatial eta_x(t)=(-1)^t) on an even/balanced periodic lattice.
    Verify M_KS is anti-Hermitian, the chirality operator eps(t,x)=(-1)^(t+x)
    anticommutes ({eps,M_KS}=0), and det(M_KS + m I) = prod_i (m^2 + sigma_i^2)
    > 0 for m>0 (matched to the direct matrix determinant). On this surface
    log|det| = log det (no phase). (Conventions match the retained note
    STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.)

  BLOCK 3 -- RELABELING-INVARIANCE (the SEPARABILITY crux; novel content).
    The determinant readout factors through det(M_KS+mI), spec(H_hat), and
    Z = Tr(e^{-beta H_hat}) ONLY (det-to-trace bridge). These are conjugation
    invariants. We permute/relabel the hw=1 corner-triplet by EVERY element of
    S_3 (and embedded staggered-mode relabelings) and verify
        det(P X P^dag) = det(X),  spec(P X P^dag) = spec(X),  Z invariant,
    to machine precision. Hence the determinant readout is BLIND to AC_phi_lambda
    (which is exactly a species relabeling / delta mass-pattern of the hw=1
    triplet). This is the concrete witness for the residual re-attribution
    under the supplied relabeling premise: the realization bridge's residual is
    FS, not AC_phi_lambda.
    (Method re-used from
    scripts/rp_p2_gauge_extension_and_labeling_indifference_2026_05_28.py Task B.)

Standalone: numpy + sympy, no framework imports, no fitted values, no PDG data,
no g_bare, no audit-lane data.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# Conventions (match the cited retained notes; no new convention introduced)
# ---------------------------------------------------------------------------
MASS = 0.7          # staggered mass m > 0 (zero-source and positive-mass baselines)
A_TAU = 1.0         # temporal lattice spacing (sets beta = L_t * a_tau)
TOL = 1e-12         # machine-precision tolerance for invariance / positivity
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/OBSERVABLE_PRINCIPLE_P2_DET_REALIZATION_BRIDGE_CONDITIONAL_ON_FERMIONIC_FRAME_NARROW_THEOREM_NOTE_2026-05-28.md"
LEDGER = ROOT / "docs/audit/data/audit_ledger.json"

DEPENDENCY_STATUS = {
    "spin_statistics_berezin_determinant_narrow_theorem_note_2026-05-10": "retained_bounded",
    "staggered_only_det_positivity_case_a_note_2026-05-17": "retained",
    "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16": "retained_bounded",
    "staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25": "retained_no_go",
}


def _walk_ledger(node):
    if isinstance(node, dict):
        yield node
        for value in node.values():
            yield from _walk_ledger(value)
    elif isinstance(node, list):
        for value in node:
            yield from _walk_ledger(value)


def ledger_row(claim_id: str) -> dict:
    ledger = json.loads(LEDGER.read_text())
    for row in _walk_ledger(ledger):
        if row.get("claim_id") == claim_id or row.get("id") == claim_id:
            return row
    return {}


def check_source_boundary() -> list[tuple[str, bool]]:
    text = NOTE.read_text()
    out: list[tuple[str, bool]] = []

    out.append((
        "note carries 2026-06-07 finite-determinant boundary retargeting",
        "2026-06-07 finite-determinant boundary retargeting" in text,
    ))
    out.append((
        "direct claim is finite determinant/relabeling boundary, not physical realization",
        "finite determinant/relabeling boundary manifest" in text
        and "not load-bearing direct-claim inputs" in text,
    ))
    out.append((
        "FS, D=M_KS, determinant-to-trace, and AC relabeling remain outside direct proof load",
        "does not ask audit to accept `FS`, `D = M_KS`, determinant-to-trace routing, or" in text
        and "`AC_phi_lambda`-as-relabeling as proved framework premises" in text,
    ))
    out.append((
        "historical conditional assembly is context, not the direct bounded target",
        "kept as context but no longer the direct" in text,
    ))
    for claim_id, expected in DEPENDENCY_STATUS.items():
        row = ledger_row(claim_id)
        out.append((
            f"ledger dependency {claim_id} has effective_status={expected}",
            row.get("effective_status") == expected,
        ))
    return out


# ===========================================================================
# BLOCK 1: Berezin Gaussian-determinant identity  Z_F[M] = det(M)
# ===========================================================================

def berezin_gaussian(M: sp.Matrix) -> sp.Expr:
    """Evaluate the finite quadratic Grassmann Gaussian
        Z_F[M] = int prod_x dchi-bar_x dchi_x exp(-sum_xy chi-bar_x M_xy chi_y)
    by its exact permutation expansion. With N generators (chi, chi-bar), the
    only surviving term saturates each dchi-bar_x dchi_x exactly once; the
    coefficient is the permanent-signed sum that equals det(M):
        Z_F[M] = sum_{perm sigma} sign(sigma) prod_x M_{x, sigma(x)} = det(M).
    We build this sum independently of sympy's det() so the match is a genuine
    cross-check, mirroring the retained Berezin runner's harness.
    """
    n = M.shape[0]
    total = sp.Integer(0)
    for perm in itertools.permutations(range(n)):
        # parity (sign) of the permutation
        sign = 1
        seen = [False] * n
        for start in range(n):
            if seen[start]:
                continue
            length = 0
            j = start
            while not seen[j]:
                seen[j] = True
                j = perm[j]
                length += 1
            if length % 2 == 0:
                sign = -sign
        term = sp.Integer(sign)
        for x in range(n):
            term *= M[x, perm[x]]
        total += term
    return sp.expand(total)


def check_berezin() -> list[tuple[str, bool]]:
    """Z_F[M] = det(M) for generic 1x1, 2x2, 3x3 complex M (symbolic), and a
    numeric M = D + J cross-check to show the bridge object is literally
    det(D+J)."""
    out: list[tuple[str, bool]] = []

    # symbolic generic matrices: Berezin permutation sum == sympy det
    for n in (1, 2, 3):
        entries = sp.symbols(f"m0:{n*n}")
        M = sp.Matrix(n, n, list(entries))
        zf = berezin_gaussian(M)
        det = sp.expand(M.det())
        ok = sp.simplify(zf - det) == 0
        out.append((f"berezin Z_F[M]=det(M) generic {n}x{n}", ok))

    # explicit complex numeric M = D + J (the bridge object) at 3x3
    rng = np.random.default_rng(3)
    D = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    J = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    M_num = sp.Matrix((D + J).tolist())
    zf = complex(berezin_gaussian(M_num))
    det = complex(M_num.det())
    ok = abs(zf - det) < 1e-9
    out.append(("berezin Z_F[D+J]=det(D+J) numeric 3x3", ok))
    return out


# ===========================================================================
# BLOCK 2 + BLOCK 3 helper: free staggered Kogut-Susskind operator
# ===========================================================================

def staggered_M_KS(Lt: int, Ls: int) -> np.ndarray:
    """Free staggered (Kogut-Susskind) hopping operator M_KS (NO mass term),
    U = 1, clean temporal hop eta_t = +1, spatial eta_x(t) = (-1)^t, periodic
    even/balanced lattice. Conventions match
    STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17. On this surface M_KS is
    anti-Hermitian and {eps, M_KS} = 0 with eps(t,x) = (-1)^(t+x)."""
    n = Lt * Ls
    M = np.zeros((n, n), dtype=complex)

    def idx(t, x):
        return (t % Lt) * Ls + (x % Ls)

    for t in range(Lt):
        for x in range(Ls):
            i = idx(t, x)
            M[i, idx(t + 1, x)] += 0.5            # temporal forward, eta_t=+1
            M[i, idx(t - 1, x)] += -0.5           # temporal backward
            eta_x = (-1.0) ** t                   # spatial staggered phase
            M[i, idx(t, x + 1)] += 0.5 * eta_x
            M[i, idx(t, x - 1)] += -0.5 * eta_x
    return M


def chirality(Lt: int, Ls: int) -> np.ndarray:
    return np.diag([(-1.0) ** (t + x) for t in range(Lt) for x in range(Ls)]).astype(complex)


# ===========================================================================
# BLOCK 2: staggered determinant positivity (zero-source surface)
# ===========================================================================

def check_det_positivity() -> list[tuple[str, bool]]:
    """M_KS anti-Hermitian, {eps, M_KS} = 0, and det(M_KS + m I) =
    prod_i (m^2 + sigma_i^2) > 0 for m > 0; log|det| = log det (no phase).
    Tested on a few even/balanced lattices and masses."""
    out: list[tuple[str, bool]] = []
    for (Lt, Ls) in [(4, 4), (4, 2), (6, 2)]:
        M_KS = staggered_M_KS(Lt, Ls)
        n = Lt * Ls
        eps = chirality(Lt, Ls)

        antiherm_err = float(np.max(np.abs(M_KS + M_KS.conj().T)))
        out.append((f"M_KS anti-Hermitian  L=({Lt},{Ls})  err={antiherm_err:.1e}",
                    antiherm_err < TOL))

        anticomm_err = float(np.max(np.abs(eps @ M_KS + M_KS @ eps)))
        out.append((f"{{eps,M_KS}}=0  L=({Lt},{Ls})  err={anticomm_err:.1e}",
                    anticomm_err < TOL))

        # M_KS anti-Hermitian => eigenvalues are purely imaginary and come in
        # conjugate pairs {+i*sigma, -i*sigma}. Hence
        #   det(M_KS + m I) = prod_lambda (m + lambda)
        #                   = prod_{pairs} (m + i sigma)(m - i sigma)
        #                   = prod_{pairs} (m^2 + sigma^2)  > 0  for m > 0.
        evals = np.linalg.eigvals(M_KS)
        # |Im(lambda)| sorted; eigenvalues come in {+i sigma, -i sigma} pairs, so
        # the n/2 pair representatives are every other entry (sigma=0 pairs incl.).
        pos_sigmas = np.sort(np.abs(evals.imag))[0::2]      # one sigma per +-pair
        for m in (0.3, 0.7, 1.5):
            full = M_KS + m * np.eye(n, dtype=complex)
            det_direct = np.linalg.det(full)
            det_spec = np.prod(m + evals)                   # exact: prod(m + i sigma)
            det_pairform = float(np.prod(m * m + pos_sigmas * pos_sigmas))
            real_pos = (abs(det_direct.imag) < 1e-9) and (det_direct.real > 0)
            matches_spec = abs(det_direct - det_spec) < 1e-9
            matches_pairform = abs(det_direct.real - det_pairform) < 1e-7
            out.append((f"det(M_KS+mI)=prod(m^2+sigma^2)>0  L=({Lt},{Ls}) m={m}  "
                        f"det={det_direct.real:.6f}",
                        real_pos and matches_spec and matches_pairform))

        # log|det| = log det on this phase-free surface (one representative)
        full = M_KS + MASS * np.eye(n, dtype=complex)
        det = np.linalg.det(full)
        logabs = math.log(abs(det))
        logdet = math.log(det.real) if det.real > 0 else float("nan")
        out.append((f"log|det| = log det  L=({Lt},{Ls})  m={MASS}",
                    abs(logabs - logdet) < 1e-9))
    return out


# ===========================================================================
# BLOCK 3: relabeling-invariance (the SEPARABILITY crux)
# ===========================================================================

def permutation_unitary(perm: list[int], block: int = 1) -> np.ndarray:
    """Permutation unitary relabeling len(perm) blocks of size `block`; column
    j of block i lands in block perm[i]. (Same construction as the RP->P2
    Task B runner.)"""
    n = len(perm)
    P = np.zeros((n * block, n * block), dtype=complex)
    Ib = np.eye(block, dtype=complex)
    for i in range(n):
        P[perm[i] * block:(perm[i] + 1) * block, i * block:(i + 1) * block] = Ib
    return P


def hw1_triplet_operator(seed: int = 7) -> np.ndarray:
    """Generic Hermitian operator on the hw=1 corner triplet C^3. Its det,
    spectrum, and Z = Tr(e^{-H3}) stand in for any relabeling-invariant readout
    on the triplet sector. AC_phi_lambda acts by conjugation H3 -> P H3 P^dag."""
    g = np.random.default_rng(seed)
    a = g.standard_normal((3, 3)) + 1j * g.standard_normal((3, 3))
    return (a + a.conj().T) / 2.0


def check_relabeling_invariance() -> list[tuple[str, bool]]:
    """det(P X P^dag) = det(X), spec(P X P^dag) = spec(X), Z invariant, under
    EVERY S_3 relabeling of the hw=1 triplet (and embedded staggered-mode
    relabelings of det(M_KS + m I)). This is the witness that the determinant
    readout is BLIND to AC_phi_lambda under the supplied relabeling premise."""
    out: list[tuple[str, bool]] = []

    # --- (i) all six S_3 permutations on the hw=1 triplet operator ---
    H3 = hw1_triplet_operator()
    det_H3 = np.real(np.linalg.det(H3))
    spec_H3 = np.sort(np.linalg.eigvalsh(H3))
    Z3 = float(np.sum(np.exp(-spec_H3)))         # Tr(e^{-H3})

    max_det_dev = 0.0
    max_spec_dev = 0.0
    max_z_dev = 0.0
    n_perms = 0
    for perm in itertools.permutations(range(3)):
        P = permutation_unitary(list(perm), block=1)
        H3p = P @ H3 @ P.conj().T
        det_dev = abs(np.real(np.linalg.det(H3p)) - det_H3)
        spec_dev = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(H3p)) - spec_H3)))
        z_dev = abs(float(np.sum(np.exp(-np.linalg.eigvalsh(H3p)))) - Z3)
        max_det_dev = max(max_det_dev, det_dev)
        max_spec_dev = max(max_spec_dev, spec_dev)
        max_z_dev = max(max_z_dev, z_dev)
        n_perms += 1
    out.append((f"det(hw=1) invariant over all {n_perms} S_3 relabelings  "
                f"maxdev={max_det_dev:.1e}", max_det_dev < TOL and n_perms == 6))
    out.append((f"spec(hw=1) invariant over all S_3 relabelings  "
                f"maxdev={max_spec_dev:.1e}", max_spec_dev < TOL))
    out.append((f"Z=Tr(e^-H) invariant over all S_3 relabelings  "
                f"maxdev={max_z_dev:.1e}", max_z_dev < TOL))

    # --- (ii) det(M_KS + m I) invariant under embedded triplet relabelings ---
    Lt, Ls = 4, 4
    M = staggered_M_KS(Lt, Ls) + MASS * np.eye(Lt * Ls, dtype=complex)
    det_M = np.linalg.det(M)
    n = Lt * Ls
    g = np.random.default_rng(11)
    max_M_dev = 0.0
    n_embed = 0
    # exhaust the 6 S_3 permutations of 3 chosen staggered modes (a fixed triplet)
    chosen = [0, 1, 2]
    for perm in itertools.permutations(range(3)):
        perm_full = list(range(n))
        for slot, src in zip(chosen, perm):
            perm_full[slot] = chosen[src]
        Pfull = permutation_unitary(perm_full, block=1)
        Mp = Pfull @ M @ Pfull.conj().T
        max_M_dev = max(max_M_dev, abs(np.linalg.det(Mp) - det_M))
        n_embed += 1
    # plus a few random embedded triplet relabelings elsewhere in the mode space
    for _ in range(3):
        perm_full = list(range(n))
        ch = list(g.choice(n, size=3, replace=False))
        cyc = ch[1:] + ch[:1]
        for a, b in zip(ch, cyc):
            perm_full[a] = b
        Pfull = permutation_unitary(perm_full, block=1)
        Mp = Pfull @ M @ Pfull.conj().T
        max_M_dev = max(max_M_dev, abs(np.linalg.det(Mp) - det_M))
        n_embed += 1
    out.append((f"det(M_KS+mI) invariant over {n_embed} embedded relabelings  "
                f"maxdev={max_M_dev:.1e}  baseline={det_M.real:.8f}",
                max_M_dev < 1e-9 and abs(det_M.imag) < 1e-9 and det_M.real > 0))

    # --- (iii) explicit AC_phi_lambda model: a delta mass-pattern on the triplet
    # is a relabeling of three masses; the det of (diag(masses)) is permutation
    # invariant -> the readout cannot see WHICH state is named e/mu/tau.
    masses = np.array([0.9, 1.1, 1.4])          # stand-in delta mass-pattern
    base_det = float(np.prod(masses))
    max_pat_dev = 0.0
    for perm in itertools.permutations(range(3)):
        permuted = masses[list(perm)]
        max_pat_dev = max(max_pat_dev, abs(float(np.prod(permuted)) - base_det))
    out.append((f"det blind to delta mass-pattern relabeling (AC_phi_lambda)  "
                f"maxdev={max_pat_dev:.1e}", max_pat_dev < TOL))
    return out


# ===========================================================================
# Main
# ===========================================================================

def main() -> int:
    print("=" * 78)
    print("P2 FINITE DETERMINANT/RELABELING BOUNDARY MANIFEST")
    print("bounded finite algebra; physical realization premises stay conditional")
    print("=" * 78)

    sections: list[tuple[str, list[tuple[str, bool]]]] = [
        ("SOURCE BOUNDARY  direct bounded claim and ledger dependency classes",
         check_source_boundary()),
        ("BLOCK 1  Berezin Gaussian-determinant identity  Z_F[M] = det(M)",
         check_berezin()),
        ("BLOCK 2  staggered determinant positivity (zero-source, phase-free)",
         check_det_positivity()),
        ("BLOCK 3  relabeling-invariance SEPARABILITY under supplied AC relabeling premise",
         check_relabeling_invariance()),
    ]

    npass = 0
    nfail = 0
    for title, results in sections:
        print(f"\n--- {title} ---")
        for label, ok in results:
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {label}")
            if ok:
                npass += 1
            else:
                nfail += 1

    print("\n" + "=" * 78)
    print("INTERPRETATION")
    print("-" * 78)
    print("Source boundary: the direct bounded claim is finite determinant")
    print("  algebra plus relabeling invariance. It does not derive FS, actual")
    print("  D=M_KS, determinant-to-trace routing, or AC_phi_lambda-as-relabeling.")
    print("Block 1: finite Berezin Gaussian algebra gives Z_F[M] = det(M).")
    print("Zero-source section: on the supplied finite zero-source staggered surfaces,")
    print("  det(M_KS+mI) > 0, so log|det| = log det there.")
    print("Block 3: det, spec(H_hat), and Z are invariant under all finite S_3")
    print("  relabelings of the hw=1 triplet and the delta mass-pattern.")
    print("=" * 78)
    print(f"SCORECARD: PASS={npass} FAIL={nfail}")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
