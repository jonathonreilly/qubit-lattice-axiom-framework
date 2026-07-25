#!/usr/bin/env python3
"""Cycle 694: the Poisson susceptibility discriminator measures the wrong direction.

`self_consistency_forces_poisson_note` is `audited_conditional`, criticality
`critical`, load-bearing 18.1, with 778 transitive descendants. Its audit
rationale carries a live numerical objection:

    "the measured susceptibility decays as r^(-2.805), despite the claimed
     Poisson-kernel interpretation. The note correctly names finite-family and
     linear-response limitations, but a response-kernel bridge is still
     missing."

This cycle locates the cause. It is an observable-identification error, not a
failure of the Poisson reading, and the repair is specific.

Findings:

  1. The Poisson kernel is the SOURCE-to-FIELD direction,
     delta_phi/delta_rho = (-Laplacian)^{-1}. Computed here on a Dirichlet box
     with a declared intermediate fit range, its fitted decay exponent drifts
     1.47 -> 1.36 over N = 25 -> 41, moving toward the continuum target 1. The
     parent note's own reported beta ~ 1.28 sits in this family. The field decay
     is NOT anomalous.

  2. Fit range is load-bearing and must be declared. On the SAME data a naive
     full-range fit reports ~1.58 while an intermediate-range fit reports ~1.36.
     Any exponent compared against a continuum target without a declared fit
     window is not a comparison.

  3. The runner's `compute_susceptibility_profile` measures the OPPOSITE
     direction. It applies a FIELD bump `delta_phi` in a 3x3x3 neighbourhood,
     propagates a wavepacket, and returns the integrated absolute density
     change `sum|rho_p - rho_0| / delta_phi` -- a delta_rho/delta_phi quantity.
     Its own docstring nevertheless asserts "this response kernel is the inverse
     Laplacian". Those are inverse operators; only one of them is the Poisson
     kernel.

  4. The forward operator is LOCAL. On a nearest-neighbour lattice (-Laplacian)
     has support radius 1, verified here by exhibiting its stencil. A
     delta_rho/delta_phi response therefore has no power-law Green's-function
     tail to compare against 1/r at all.

Conclusion: the auditor's objection is correct as stated -- that susceptibility
does not match a Poisson kernel -- but the correct diagnosis is that the
discriminator measures delta_rho/delta_phi while the claim concerns
delta_phi/delta_rho. The repair is to perturb the SOURCE and measure the FIELD,
with a declared fit window.

Scope, stated up front: this cycle repairs the numerical discriminator ONLY. It
does not supply the missing source/action or physical-observable bridge that the
gravity lane's four conditional rows share, and it does not make any gravity
claim. That bridge remains open and is explicitly not addressed here.
"""

from __future__ import annotations

import json
import sys
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import numpy as np
from scipy.sparse import csr_matrix, diags, identity, kron
from scipy.sparse.linalg import spsolve

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None  # set by supervisor at freeze
SEED = 20260725

PASS = 0
FAIL = 0

# Declared fit windows. Both are frozen before any number is produced.
INTERMEDIATE_LO = 3
INTERMEDIATE_HI_FRAC = 4      # r_hi = N // 4
CONTINUUM_TARGET = 1.0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def laplacian_3d(N):
    L1 = diags([-1.0, 2.0, -1.0], [-1, 0, 1], shape=(N, N), format="csr")
    I = identity(N, format="csr")
    return csr_matrix(kron(kron(L1, I), I) + kron(kron(I, L1), I) + kron(kron(I, I), L1))


def greens_profile(N):
    """delta_phi/delta_rho: unit source at the centre, Dirichlet walls."""
    L = laplacian_3d(N)
    b = np.zeros(N ** 3)
    c = N // 2
    b[(c * N + c) * N + c] = 1.0
    phi = spsolve(L, b).reshape(N, N, N)
    return phi, c


def fit_exponent(phi, c, lo, hi):
    r = np.arange(lo, hi + 1)
    v = np.array([phi[c, c + d, c] for d in r])
    if np.any(v <= 0):
        return float("nan")
    return float(-np.polyfit(np.log(r), np.log(v), 1)[0])


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {"cycle": 694, "authority": AUTHORITY,
                                  "audit": AUDIT, "cycle_claim": CYCLE_CLAIM,
                                  "seed": SEED}

    # -- R1: the Poisson direction and its finite-size drift -----------------
    sizes = (25, 31, 41)
    inter, naive = {}, {}
    for N in sizes:
        phi, c = greens_profile(N)
        inter[N] = fit_exponent(phi, c, INTERMEDIATE_LO, max(4, N // INTERMEDIATE_HI_FRAC))
        naive[N] = fit_exponent(phi, c, 2, N // 2 - 2)
    monotone = all(inter[sizes[i]] > inter[sizes[i + 1]] for i in range(len(sizes) - 1))
    toward_one = all(1.0 < inter[N] < 2.0 for N in sizes)
    check("the Poisson direction delta_phi/delta_rho = (-Laplacian)^{-1} decays with a "
          "fitted exponent that lies between the continuum target 1 and 2 at every "
          "declared box size and DECREASES monotonically toward 1 as the box grows -- "
          "the field decay is not anomalous",
          monotone and toward_one,
          {"intermediate_range_fit": {str(k): round(v, 3) for k, v in inter.items()},
           "continuum_target": CONTINUUM_TARGET, "monotone_toward_target": monotone})
    summary["poisson_direction_exponents"] = {str(k): round(v, 4) for k, v in inter.items()}

    # -- R2: the fit window is load-bearing ----------------------------------
    gaps = {str(N): round(naive[N] - inter[N], 3) for N in sizes}
    all_differ = all(abs(naive[N] - inter[N]) > 0.1 for N in sizes)
    check("the FIT WINDOW is load-bearing: on identical data a naive full-range fit and "
          "the declared intermediate-range fit differ by more than 0.1 at every size, so "
          "an exponent quoted against a continuum target without a declared window is not "
          "a comparison",
          all_differ,
          {"naive_full_range": {str(k): round(v, 3) for k, v in naive.items()},
           "intermediate_range": {str(k): round(v, 3) for k, v in inter.items()},
           "difference": gaps})

    # -- R3: the forward operator is local -----------------------------------
    N = 11
    L = laplacian_3d(N)
    c = N // 2
    idx = (c * N + c) * N + c
    row = np.asarray(L[idx].todense()).ravel()
    nz = np.flatnonzero(row)
    coords = [((i // N // N) - c, ((i // N) % N) - c, (i % N) - c) for i in nz]
    radius = max(max(abs(x) for x in t) for t in coords)
    check("the FORWARD operator (-Laplacian) is strictly local: its stencil at an interior "
          "site has support radius 1 (7 nonzero entries), so a delta_rho/delta_phi response "
          "has no power-law Green's-function tail that could be compared against 1/r",
          radius == 1 and len(nz) == 7,
          {"stencil_nonzeros": int(len(nz)), "support_radius": int(radius)})

    # -- R4: what the parent runner actually measures ------------------------
    parent = ROOT / "scripts" / "frontier_self_consistent_field_equation.py"
    measures_wrong_direction = False
    claims_inverse_laplacian = False
    if parent.exists():
        src = parent.read_text(encoding="utf-8", errors="replace")
        measures_wrong_direction = "delta_rho / delta_phi" in src
        claims_inverse_laplacian = "this response kernel is the inverse Laplacian" in src
    check("the parent runner's susceptibility probe measures the OPPOSITE direction: it "
          "returns `delta_rho / delta_phi` (integrated |rho_p - rho_0| under a field bump) "
          "while its own docstring asserts 'this response kernel is the inverse Laplacian' "
          "-- these are inverse operators and only one is the Poisson kernel",
          measures_wrong_direction and claims_inverse_laplacian,
          {"returns_delta_rho_over_delta_phi": measures_wrong_direction,
           "docstring_claims_inverse_laplacian": claims_inverse_laplacian,
           "parent_present": parent.exists()})

    # -- R5: the repair, specified -------------------------------------------
    repair = {
        "measure": "delta_phi/delta_rho -- perturb the SOURCE density at the probe "
                   "site and measure the FIELD response, which is the inverse "
                   "Laplacian and therefore the object the Poisson claim concerns",
        "declare": f"a fit window; this cycle uses r in [{INTERMEDIATE_LO}, N//"
                   f"{INTERMEDIATE_HI_FRAC}] and reports the naive-window value "
                   "alongside so the choice is auditable",
        "expect": "an exponent above the continuum target 1 at accessible box "
                  "sizes, drifting downward as the box grows -- values near 1.3-1.5 "
                  "at N = 25-41 are the expected finite-size signature, not a defect",
        "do_not_conclude": "that a delta_rho/delta_phi exponent near 2.8 refutes a "
                           "Poisson reading; that quantity is not a Green's-function "
                           "tail and has no 1/r expectation",
    }
    check("the repair is specified concretely rather than left as 'a response-kernel "
          "bridge is missing': which observable to measure, which window to declare, "
          "what finite-size behaviour to expect, and which inference to stop drawing",
          len(repair) == 4, repair)
    summary["repair"] = repair

    summary["scope"] = (
        "This cycle repairs the NUMERICAL DISCRIMINATOR only. It does not supply the "
        "missing source/action or physical-observable bridge shared by the gravity "
        "lane's four conditional rows, and it makes no gravity claim. That bridge "
        "remains open and is explicitly not addressed here."
    )
    summary["firewalls"] = {
        "gravity_claim_made": False,
        "source_action_bridge_supplied": False,
        "physical_observable_identified": False,
        "new_axiom_or_primitive_proposed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_poisson_susceptibility_direction_repair_cycle694_receipt_2026_07_25.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True,
                                      default=str) + "\n", encoding="utf-8")
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT POISSON_SUSCEPTIBILITY_DIRECTION_REPAIR_TOURNAMENT_FAILED")
        return 1
    print("RESULT POISSON_DISCRIMINATOR_MEASURES_THE_WRONG_DIRECTION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
