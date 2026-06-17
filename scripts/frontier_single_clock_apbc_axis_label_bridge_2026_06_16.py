#!/usr/bin/env python3
"""APBC boundary datum selects the single-clock axis label.

This runner extracts the positive half of the 2026-06-11 single-clock
axis-selection no-go: a supplied per-axis boundary-condition datum

    bc = (APBC, PBC, PBC, PBC)

breaks the tau <-> x_1 exchange exactly. The theorem is deliberately
conditional on that datum. It does not derive the datum, the time step,
the transfer construction, or the no-second-clock premise.
"""

from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
TARGET = ROOT / "docs" / "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{status}] [{tag}] {label}{suffix}")


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, ord=2))


def build_surface(ls: tuple[int, int, int, int], mass: float = 0.3, apbc: tuple[int, ...] = ()):
    sites = list(itertools.product(*[range(n) for n in ls]))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)

    def eta(mu: int, x: tuple[int, int, int, int]) -> int:
        return (-1) ** sum(x[:mu])

    mat = np.zeros((n, n))
    sectors: list[np.ndarray] = []
    for mu in range(4):
        sector = np.zeros((n, n))
        for x in sites:
            y = list(x)
            y[mu] = (y[mu] + 1) % ls[mu]
            wrap_sign = -1.0 if (mu in apbc and x[mu] == ls[mu] - 1) else 1.0
            sector[idx[x], idx[tuple(y)]] += wrap_sign * eta(mu, x)
            sector[idx[tuple(y)], idx[x]] -= wrap_sign * eta(mu, x)
        sectors.append(sector)
        mat += sector
    mat += mass * np.eye(n)
    return mat, sectors, sites, idx


def exchange_w(sites: list[tuple[int, int, int, int]], idx: dict[tuple[int, int, int, int], int]):
    n = len(sites)
    perm = np.zeros((n, n))
    sign = np.zeros((n, n))
    for x in sites:
        perm[idx[(x[1], x[0], x[2], x[3])], idx[x]] = 1.0
        sign[idx[x], idx[x]] = (-1.0) ** (x[0] * x[1])
    return perm @ sign, perm


def kernel_dim(mat: np.ndarray, tol: float = 1e-10) -> int:
    return int(np.sum(np.linalg.svd(mat, compute_uv=False) < tol))


def boundary_automorphisms(bc: tuple[str, str, str, str]) -> list[tuple[int, int, int, int]]:
    out = []
    for perm in itertools.permutations(range(4)):
        if all(bc[i] == bc[perm[i]] for i in range(4)):
            out.append(perm)
    return out


def main() -> int:
    print("Single-clock APBC axis-label bridge")
    print("claim_type_author_hint: bounded_theorem")
    print("actual_current_surface_status: exact-support conditional on supplied APBC/PBC datum")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    ls = (4, 4, 2, 2)
    mass = 0.3

    print("A. symmetric surface sanity checks")
    m_pbc, sec_pbc, sites, idx = build_surface(ls, mass, apbc=())
    w, plain = exchange_w(sites, idx)
    record("A", "W is orthogonal", opnorm(w @ w.T - np.eye(len(sites))) < 1e-14)
    record("A", "all-PBC staggered surface is W-invariant", opnorm(w @ m_pbc @ w.T - m_pbc) < 1e-13)
    record("A", "plain tau<->x_1 swap without the sign field fails", opnorm(plain @ m_pbc @ plain.T - m_pbc) > 1.0)
    record("A", "periodic tau and periodic x_1 hop sectors have matching kernel dimensions",
           kernel_dim(sec_pbc[0]) == kernel_dim(sec_pbc[1]),
           f"ker tau={kernel_dim(sec_pbc[0])}, ker x1={kernel_dim(sec_pbc[1])}")

    print("\nB. supplied APBC/PBC datum breaks the exchange")
    m_ap, sec_ap, sites_ap, idx_ap = build_surface(ls, mass, apbc=(0,))
    w_ap, _ = exchange_w(sites_ap, idx_ap)
    ap_resid = opnorm(w_ap @ m_ap @ w_ap.T - m_ap)
    record("B", "APBC on tau and PBC on x_1 breaks W exactly", ap_resid > 1.0, f"resid={ap_resid:.6f}")
    record("B", "temporal APBC hop sector has trivial kernel", kernel_dim(sec_ap[0]) == 0,
           f"ker tau={kernel_dim(sec_ap[0])}")
    record("B", "periodic x_1 hop sector has nonzero kernel", kernel_dim(sec_ap[1]) > 0,
           f"ker x1={kernel_dim(sec_ap[1])}")
    record("B", "kernel dimension separates tau from x_1 invariantly",
           kernel_dim(sec_ap[0]) != kernel_dim(sec_ap[1]))

    print("\nC. symmetric APBC falsifier")
    m_sym, sec_sym, sites_sym, idx_sym = build_surface(ls, mass, apbc=(0, 1))
    w_sym, _ = exchange_w(sites_sym, idx_sym)
    record("C", "APBC on both tau and x_1 restores W-invariance",
           opnorm(w_sym @ m_sym @ w_sym.T - m_sym) < 1e-13)
    record("C", "symmetric APBC makes tau and x_1 kernel dimensions match again",
           kernel_dim(sec_sym[0]) == kernel_dim(sec_sym[1]),
           f"ker tau={kernel_dim(sec_sym[0])}, ker x1={kernel_dim(sec_sym[1])}")
    record("C", "therefore the selecting input is BC asymmetry, not APBC alone",
           ap_resid > 1.0 and opnorm(w_sym @ m_sym @ w_sym.T - m_sym) < 1e-13)

    print("\nD. boundary-datum automorphism group")
    bc = ("A", "P", "P", "P")
    autos = boundary_automorphisms(bc)
    record("D", "APBC/PBC boundary vector has exactly S_3 residual symmetry", len(autos) == 6,
           f"|Aut(bc)|={len(autos)}")
    record("D", "every boundary-datum automorphism fixes the APBC axis", all(p[0] == 0 for p in autos))
    record("D", "spatial axes remain permutable under the residual S_3", {tuple(p[1:]) for p in autos} == set(itertools.permutations((1, 2, 3))))
    swapped_bc = ("P", "A", "P", "P")
    record("D", "tau<->x_1 exchange changes the datum rather than preserving it", swapped_bc != bc)

    print("\nE. composition and source-scope guards")
    note = NOTE.read_text(encoding="utf-8")
    target = TARGET.read_text(encoding="utf-8")
    flat = " ".join(note.split())
    target_flat = " ".join(target.split())
    record("E", "source note states supplied-datum conditionality",
           "Conditional on a supplied per-axis boundary-condition datum" in flat)
    record("E", "source note refuses to derive the BC datum",
           "does not derive the APBC/PBC datum" in flat)
    record("E", "source note leaves B-AXIS.1 and B-AXIS.3 untouched",
           "B-AXIS.1" in flat and "B-AXIS.3" in flat and "untouched" in flat)
    record("E", "source note excludes audit-data/status edits",
           "does not update audit data" in flat and "does not set audit status" in flat)
    record("E", "target single-clock note cites the bridge without promoting status",
           "SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md" in target
           and "no status change" in target)
    record("E", "target note still says B-AXIS remains live unless the datum is supplied",
           "B-AXIS remains live unless the APBC/PBC datum is itself supplied" in target_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: Given a supplied APBC-on-axis/PBC-on-others boundary datum, "
            "the axis-label component of B-AXIS.2 is selected exactly. The datum, "
            "the time step, the transfer construction, and the no-second-clock "
            "premise are not derived here."
        )
        return 0
    print("VERDICT: APBC axis-label bridge failed; do not cite this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
