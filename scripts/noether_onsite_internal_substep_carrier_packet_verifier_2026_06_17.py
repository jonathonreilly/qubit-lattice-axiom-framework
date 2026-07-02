#!/usr/bin/env python3
"""Packet verifier for the onsite/internal lattice-Noether carrier repair.

This verifier is source-side only. It checks that the Noether packet no longer
uses the broad staggered-realization gate as a markdown dependency and that the
finite Kawamoto-Smit carrier needed by the current theorem is constructed and
checked directly.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_ONSITE_INTERNAL_NARROW_THEOREM_NOTE_2026-06-05.md"
RUNNER = ROOT / "scripts" / "audit_companion_lattice_noether_onsite_internal_2026_06_05.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def eta(x: tuple[int, ...], mu: int) -> float:
    if mu == 0:
        return 1.0
    return float((-1) ** sum(x[:mu]))


def build_staggered_m(L: int, dim: int) -> tuple[np.ndarray, list[tuple[int, ...]], dict[tuple[int, ...], int]]:
    sites = list(product(range(L), repeat=dim))
    index = {x: i for i, x in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)), dtype=float)
    for x in sites:
        row = index[x]
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            M[row, index[xp]] += 0.5 * eta(x, mu)
            M[row, index[xm]] -= 0.5 * eta(x, mu)
    return M, sites, index


def torus_l1(a: tuple[int, ...], b: tuple[int, ...], L: int) -> int:
    total = 0
    for x, y in zip(a, b):
        d = abs(x - y)
        total += min(d, L - d)
    return total


def fermi_ann(n: int) -> list[np.ndarray]:
    I2 = np.eye(2, dtype=complex)
    Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    ann = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    out: list[np.ndarray] = []
    for k in range(n):
        mats = [Z] * k + [ann] + [I2] * (n - 1 - k)
        op = mats[0]
        for m in mats[1:]:
            op = np.kron(op, m)
        out.append(op)
    return out


def continuity_errors() -> tuple[float, float, float, float]:
    M, sites, index = build_staggered_m(L=3, dim=1)
    n = len(sites)
    a = fermi_ann(n)
    adag = [op.conj().T for op in a]
    H1 = 1j * M
    H = sum(H1[p, q] * (adag[p] @ a[q]) for p in range(n) for q in range(n))
    fock_dim = a[0].shape[0]

    def rho(site_index: int) -> np.ndarray:
        return adag[site_index] @ a[site_index]

    def jmu(x: tuple[int, ...], sign: float) -> np.ndarray:
        xp = ((x[0] + 1) % 3,)
        i0 = index[x]
        i1 = index[xp]
        return sign * (-0.5) * eta(x, 0) * (adag[i0] @ a[i1] + adag[i1] @ a[i0])

    def divj(x: tuple[int, ...], sign: float) -> np.ndarray:
        xm = ((x[0] - 1) % 3,)
        return jmu(x, sign) - jmu(xm, sign)

    fixed = 0.0
    flipped = 0.0
    drho_norm = 0.0
    for x in sites:
        ix = index[x]
        drho = 1j * (H @ rho(ix) - rho(ix) @ H)
        fixed = max(fixed, float(np.max(np.abs(drho + divj(x, +1.0)))))
        flipped = max(flipped, float(np.max(np.abs(drho + divj(x, -1.0)))))
        drho_norm = max(drho_norm, float(np.max(np.abs(drho))))
    herm_err = float(np.max(np.abs(H1 - H1.conj().T)))
    return fixed, flipped, drho_norm, herm_err


def main() -> int:
    print("Noether onsite/internal substep-carrier packet verifier")
    print("status authority: source-side verifier only; no audit verdicts are applied")
    print()

    note = read(NOTE)
    runner = read(RUNNER)
    note_flat = " ".join(note.split())

    print("A. source-boundary checks")
    check("packet verifier is registered in the note", "2026-06-17 packet verifier" in note)
    check("broad realization gate has no markdown dependency edge", "](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)" not in note)
    check("old admitted-context section is absent", "Admitted context input" not in note)
    check("finite carrier exhibit section is present", "Finite carrier exhibit (constructed here, not a broad-gate dependency)" in note)
    check("physical realization/readout bridge is not consumed", "downstream and is not consumed here" in note_flat)
    check("no audit verdict language is applied", "actual_current_surface_status" not in note and "audited_clean" not in note)
    check("abstract bilinear authority is cited", "AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md" in note)
    check("substep-1 Grassmann authority is cited", "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md" in note)
    check("det positivity authority is cited", "STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md" in note)
    check("runner boundary uses finite carrier language", "finite free staggered carrier" in runner)
    check("runner no longer requires physical charge-density wording", "physical (>= 0) charge" not in runner)

    print("\nB. finite Kawamoto-Smit carrier checks")
    M, sites, index = build_staggered_m(L=4, dim=3)
    anti_err = float(np.max(np.abs(M + M.T)))
    H = 1j * M
    herm_err = float(np.max(np.abs(H - H.conj().T)))
    nonzero = [(sites[i], sites[j]) for i, j in zip(*np.nonzero(np.abs(M) > 0))]
    nn_ok = all(torus_l1(a, b, 4) == 1 for a, b in nonzero)
    check("massless KS exhibit is real antisymmetric", anti_err < 1e-12, f"err={anti_err:.3e}")
    check("iM is Hermitian on the finite exhibit", herm_err < 1e-12, f"err={herm_err:.3e}")
    check("support is nearest-neighbour only", nn_ok and len(nonzero) > 0, f"edges={len(nonzero)}")
    T = 1j * np.eye(len(sites))
    u1_err = float(np.max(np.abs(T @ M - M @ T)))
    check("onsite U(1) generator commutes with the finite carrier", u1_err < 1e-12, f"err={u1_err:.3e}")

    print("\nC. continuity sign checks")
    fixed, flipped, drho_norm, h1_herm = continuity_errors()
    check("1D continuity replay has Hermitian iM", h1_herm < 1e-12, f"err={h1_herm:.3e}")
    check("d rho/dt is nonzero in the replay", drho_norm > 1e-6, f"norm={drho_norm:.3e}")
    check("formula-(4*) sign satisfies d rho/dt + div j = 0", fixed < 1e-10, f"err={fixed:.3e}")
    check("flipped sign violates continuity", flipped > 1e-6, f"err={flipped:.3e}")

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print(
            "VERDICT: source-side packet is ready for reviewer/auditor re-check: "
            "the onsite/internal Noether theorem uses a constructed finite "
            "carrier exhibit and no broad realization-gate dependency edge."
        )
        return 0
    print("VERDICT: packet verifier failed; do not use this repair yet.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
