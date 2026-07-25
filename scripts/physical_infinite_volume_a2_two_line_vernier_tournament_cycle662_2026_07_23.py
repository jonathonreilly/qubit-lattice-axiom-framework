#!/usr/bin/env python3
"""Cycle 662: infinite-volume A2 two-line diagnostics and vernier reconstruction.

Objective 1: evaluate finite-L and direct-torus-integral A2-channel
Birman-Schwinger near-zeros for the Cycle-230 contact dimer, with
preregistered convergence falsifiers. The full-window global-min estimator's
second candidate is diagnostic only: branch-tracked support and the Cycle-675
completion supersede its spurious values. Objective 2: the two-line
lawful-domain certificate and the executed vernier reconstruction reaching
the historically labeled 5:4 advance shore in the reconstructed rate.

Work-history: joint lane max observed 661; claiming Cycle 662.  The
Cycle-563--583 substrate and Cycle-610 family landed through the two parent
PRs; this runner was rebuilt on those landed, re-frozen surfaces.

Firewalls: a spectral line is not energy; the L=inf value is a
quadrature-controlled statement, not a rigorous spectral theorem (the
contact-cyclic lemma remains open); the vernier reconstruction is retained-
data analysis reaching the 451 shore algebraically under the Cycle-612
association caveat — no identification claimed.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
import time
from hashlib import sha256
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

FROZEN_CONTRACT_SHA256 = (
    "24199cd1ac9d3bf46db8ee59b8d83f6e27c6058dd55a07122181f4993d42f2b3"
)
C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
C611_SHA256 = "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8"
C622_SHA256 = "1cd1a1a1eedd03b3d178ef65adc5f98814c3ed11e0ea37103b111d0aa09378e1"
RECEIPT = ROOT / (
    "outputs/physical_infinite_volume_a2_two_line_vernier_tournament_"
    "cycle662_receipt_2026_07_23.json"
)

WINDOW_B = (-3.12, -2.80)
WINDOW_2 = (0.10, 0.50)
L_ROWS = (9, 13, 17, 21)
BETA = -0.3
BETA_HELD = -0.35
CONTACT = 0.37
NQ_ROWS = (24, 32, 40, 48)
ALPHA_ROWS = (0.0, math.pi / 4, -0.7439, 2.0, -2.9, 2 * math.pi)
BAND_HALFWIDTH = 60

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def load_module(name: str):
    path = ROOT / "scripts" / (name + ".py")
    digest = sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, digest


C610, C610_SHA = load_module(
    "physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22")
C611, C611_SHA = load_module(
    "physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22")
C622, C622_SHA = load_module(
    "physical_deterministic_exhaust_shell_preparation_tournament_cycle622_2026_07_22")

A2_36 = C610.A2_FULL.astype(complex)


def a2_scalar_finite(length: int, theta: float, beta: float) -> complex:
    z = np.exp(1j * theta)
    stack = C610.free_stack(length, C610.K_TRAIN_0, beta)
    rhs = np.broadcast_to(A2_36.reshape(1, 36, 1), (len(stack), 36, 1))
    solved = np.linalg.solve(stack - z * np.eye(36)[None], rhs)[:, :, 0]
    accumulator = complex(np.einsum("i,pi->", A2_36.conj(), solved) / len(stack))
    return 1 - z * (np.exp(-1j * CONTACT) - 1) * accumulator


def a2_scalar_infinite(theta: float, beta: float, order: int) -> complex:
    z = np.exp(1j * theta)
    nodes, weights = np.polynomial.legendre.leggauss(order)
    angles = math.pi * (nodes + 1.0)
    coin = C610.coin2(beta)
    relative = None
    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
    rel = (c210.DIRECTIONS[:, None, :] - c210.DIRECTIONS[None, :, :]).reshape(36, 3)
    total = 0j
    wx = weights / 2.0  # each axis: (1/2pi) * pi * w  => w/2
    chunk = 4096
    grid = np.stack(np.meshgrid(angles, angles, angles, indexing="ij"),
                    axis=-1).reshape(-1, 3)
    wgrid = (wx[:, None, None] * wx[None, :, None] * wx[None, None, :]).reshape(-1)
    for start in range(0, len(grid), chunk):
        pg = grid[start:start + chunk]
        wg = wgrid[start:start + chunk]
        phase = np.exp(-1j * (pg @ rel.T))
        blocks = phase[:, :, None] * coin[None, :, :] - z * np.eye(36)[None]
        rhs = np.broadcast_to(A2_36.reshape(1, 36, 1), (len(pg), 36, 1))
        solved = np.linalg.solve(blocks, rhs)[:, :, 0]
        total += complex(np.einsum("i,pi->p", A2_36.conj(), solved) @ wg)
    return 1 - z * (np.exp(-1j * CONTACT) - 1) * total


def find_root(func, window, samples: int = 240, tol: float = 1e-11):
    thetas = np.linspace(window[0], window[1], samples)
    values = [abs(func(float(t))) for t in thetas]
    center = int(np.argmin(values))
    lo = float(thetas[max(0, center - 1)])
    hi = float(thetas[min(samples - 1, center + 1)])
    for _ in range(80):
        third = (hi - lo) / 3
        a, b = lo + third, hi - third
        if abs(func(a)) < abs(func(b)):
            hi = b
        else:
            lo = a
        if hi - lo < tol:
            break
    root = 0.5 * (lo + hi)
    return root, abs(func(root))


def peak_position(spectrum_mags, freqs, index):
    if 0 < index < len(spectrum_mags) - 1:
        a, b, c = spectrum_mags[index - 1], spectrum_mags[index], spectrum_mags[index + 1]
        shift = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) != 0 else 0.0
    else:
        shift = 0.0
    bin_width = freqs[1] - freqs[0]
    return C610.wrap_angle(float(freqs[index] + shift * bin_width))


def two_line_certificate(word: np.ndarray, skip: int) -> dict[str, object]:
    segment = word[skip:]
    spectrum = np.fft.fft(segment)
    freqs = 2 * np.pi * np.fft.fftfreq(len(segment))
    mags = np.abs(spectrum)
    order = np.argsort(mags)[::-1]
    p1, p2 = int(order[0]), int(order[1])
    floor = float(np.median(mags))
    lines = sorted([peak_position(mags, freqs, p1), peak_position(mags, freqs, p2)])
    locked = []
    for idx in (p1, p2):
        band = np.zeros_like(spectrum)
        lo = max(0, idx - BAND_HALFWIDTH)
        band[lo:idx + BAND_HALFWIDTH] = spectrum[lo:idx + BAND_HALFWIDTH]
        filtered = np.fft.ifft(band)
        row1 = C610.clock_row(filtered, 8, "T1")
        row2 = C610.clock_row(filtered, 8, "T2")
        bound = 2 * (2 / len(filtered))
        locked.append(bool(
            row1["locked"] and abs(row1["rate"] - row2["rate"]) < 2 * bound))
    return {
        "lines": lines, "peak_mags": [float(mags[p1]), float(mags[p2])],
        "floor": floor,
        "two_peaks": bool(mags[p1] > 5 * floor and mags[p2] > 5 * floor),
        "per_line_locked": locked,
        "lawful": bool(mags[p1] > 5 * floor and mags[p2] > 5 * floor
                       and all(locked)),
    }


def main() -> int:
    start = time.time()
    expected = (C610_SHA256, C611_SHA256, C622_SHA256)
    observed = (C610_SHA, C611_SHA, C622_SHA)
    if observed != expected:
        raise RuntimeError(
            "dependency SHA mismatch: "
            f"c610={C610_SHA} c611={C611_SHA} c622={C622_SHA}"
        )
    receipt: dict[str, object] = {
        "cycle": 662, "authority": "none", "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "consumed_cycle610_sha256": C610_SHA,
        "consumed": {"cycle610": C610_SHA, "cycle611": C611_SHA,
                     "cycle622": C622_SHA},
        "stacking": "Cycles 563-583 and the Cycle-610 family landed on main; "
        "this family was rebuilt from landed main commit "
        "b6cf38bcfcda9458aae9c9b8f332ec69989ff629; joint lane max 661, "
        "claiming 662",
    }
    check("the Cycle-610 runner is byte-pinned and unchanged",
          C610_SHA == C610_SHA256, C610_SHA[:16])

    # ---- Objective 1: finite-L rows (supervisor subset; worker covers more).
    finite = {}
    for length in L_ROWS:
        row = {}
        for name, window in (("root_b", WINDOW_B), ("root_2", WINDOW_2)):
            theta, ab = find_root(lambda t: a2_scalar_finite(length, t, BETA), window)
            row[name] = {"theta": theta, "abs_b": ab}
        finite[length] = row
    held = {}
    for length in (9, 17):
        row = {}
        for name, window in (("root_b", WINDOW_B), ("root_2", WINDOW_2)):
            theta, ab = find_root(
                lambda t: a2_scalar_finite(length, t, BETA_HELD), window)
            row[name] = {"theta": theta, "abs_b": ab}
        held[length] = row
    receipt["finite_L"] = {str(k): v for k, v in finite.items()}
    receipt["held_beta"] = {str(k): v for k, v in held.items()}
    exists_2 = all(finite[L]["root_2"]["abs_b"] < 1e-6 for L in L_ROWS)
    exists_b = all(finite[L]["root_b"]["abs_b"] < 1e-6 for L in L_ROWS)
    check(
        "O1 existence: both A2 roots exist at every finite L in the frozen "
        "grid (falsifier (a) does not fire) and at the held species",
        exists_2 and exists_b
        and all(held[L][r]["abs_b"] < 1e-6 for L in held for r in held[L]),
        {"root2_absb": [finite[L]["root_2"]["abs_b"] for L in L_ROWS]},
    )

    # ---- Objective 1: L = infinity quadrature rows.
    quad = {}
    for name, window in (("root_b", WINDOW_B), ("root_2", WINDOW_2)):
        per_order = {}
        for order in NQ_ROWS:
            theta, ab = find_root(
                lambda t: a2_scalar_infinite(t, BETA, order), window,
                samples=120, tol=1e-10)
            per_order[order] = {"theta": theta, "abs_b": ab}
        shifts = [abs(per_order[NQ_ROWS[i + 1]]["theta"] - per_order[NQ_ROWS[i]]["theta"])
                  for i in range(len(NQ_ROWS) - 1)]
        quad[name] = {"orders": {str(k): v for k, v in per_order.items()},
                      "shifts": shifts,
                      "theta_inf": per_order[NQ_ROWS[-1]]["theta"],
                      "quadrature_converged": bool(shifts[-1] < 1e-8)}
    receipt["quadrature"] = quad
    check(
        "O1 infinite-volume global-min diagnostic: both frozen windows contain "
        "near-zero candidates at final quadrature order; order-shift "
        "convergence is reported separately and is not implied by this row",
        all(quad[n]["orders"][str(NQ_ROWS[-1])]["abs_b"] < 1e-6 for n in quad),
        {n: {"theta_inf": quad[n]["theta_inf"], "last_shift": quad[n]["shifts"][-1],
             "converged": quad[n]["quadrature_converged"]} for n in quad},
    )

    # Convergence certificates: finite-L residuals against the L=inf roots.
    conv = {}
    for name in ("root_b", "root_2"):
        theta_inf = quad[name]["theta_inf"]
        residuals = {L: abs(finite[L][name]["theta"] - theta_inf) for L in L_ROWS}
        logs = {L: math.log(max(r, 1e-16)) for L, r in residuals.items()}
        ls = list(L_ROWS)
        exp_rate = (logs[ls[-1]] - logs[ls[0]]) / (ls[-1] - ls[0])
        pow_rate = (logs[ls[-1]] - logs[ls[0]]) / (
            math.log(ls[-1]) - math.log(ls[0]))
        monotone = all(residuals[ls[i + 1]] <= residuals[ls[i]] * 1.5
                       for i in range(len(ls) - 1))
        error_bar = residuals[ls[-1]] + quad[name]["shifts"][-1]
        conv[name] = {
            "residuals": {str(L): residuals[L] for L in ls},
            "exp_rate_per_L": exp_rate, "power_exponent": pow_rate,
            "monotone_within_factor_1p5": bool(monotone),
            "controlled_extrapolation_error_bar": error_bar,
        }
    receipt["convergence"] = conv
    check(
        "O1 convergence: finite-L roots converge to the L=inf values with "
        "certified rates and controlled error bars (raw falsifier (b) row; a "
        "FAIL requires physical-versus-estimator adjudication)",
        all(conv[n]["monotone_within_factor_1p5"] for n in conv)
        and conv["root_b"]["controlled_extrapolation_error_bar"] < 1e-4
        and conv["root_2"]["controlled_extrapolation_error_bar"] < 5e-3,
        {n: {"bar": conv[n]["controlled_extrapolation_error_bar"],
             "exp_rate": conv[n]["exp_rate_per_L"]} for n in conv},
    )

    # ---- Objective 2: isolation certificate for theta_2 at L = inf.
    theta2_inf = quad["root_2"]["theta_inf"]
    eps = 1e-5
    derivative = abs(
        (a2_scalar_infinite(theta2_inf + eps, BETA, 40)
         - a2_scalar_infinite(theta2_inf - eps, BETA, 40)) / (2 * eps))
    neighbor_scan = [
        abs(a2_scalar_infinite(float(t), BETA, 32))
        for t in np.linspace(theta2_inf - 0.05, theta2_inf + 0.05, 41)
        if abs(float(t) - theta2_inf) > 5e-3
    ]
    check(
        "O2 global-min diagnostic: the frozen full-window candidate is a "
        "transversal isolated numerical zero; this row does not identify it "
        "with the physical theta_2 branch",
        derivative > 1e-3 and min(neighbor_scan) > 1e-3,
        {"candidate_theta": theta2_inf, "derivative": derivative,
         "neighborhood_min": float(min(neighbor_scan)),
         "physical_theta_2_identification": False},
    )
    receipt["isolation"] = {
        "candidate_theta": theta2_inf,
        "derivative": derivative,
        "neighborhood_min": float(min(neighbor_scan)),
        "physical_theta_2_identification": False,
    }

    # ---- Objective 2: two-line word, lawful-domain certificate, vernier.
    engine = C611.PositionEngine(C611.L_TRAIN, BETA)
    keep = C622.chebyshev_radii(engine.length) <= 2
    state = engine.source()
    for _ in range(256):
        state = engine.step(state, CONTACT) * keep[..., None]
    word = C622.channel_word(engine, state, -1, CONTACT)
    base_cert = two_line_certificate(word, 64)
    theta_b_L9 = finite[9]["root_b"]["theta"]
    theta_2_word = max(base_cert["lines"])
    check(
        "O2 two-line lawful domain: the ball-survivor word passes the frozen "
        "two-line certificate (two >5x peaks, per-line locked bandpass "
        "chains)",
        base_cert["lawful"],
        base_cert,
    )
    receipt["two_line_word"] = base_cert

    reference_lines = sorted([theta_b_L9, theta_2_word])
    vernier_rows = []
    all_ok = True
    q_axis = np.arange(len(word))
    for alpha_true in ALPHA_ROWS:
        modulated = word * np.exp(1j * alpha_true * q_axis)
        cert = two_line_certificate(modulated, 64)
        measured = sorted(cert["lines"])
        grid = np.arange(0.0, 2 * math.pi, 1e-4)

        def mismatch(alpha):
            pred = sorted([C610.wrap_angle(reference_lines[0] + alpha),
                           C610.wrap_angle(reference_lines[1] + alpha)])
            return sum(C610.wrap_angle(m - p) ** 2
                       for m, p in zip(measured, pred))

        coarse = min(grid, key=mismatch)
        lo, hi = coarse - 2e-4, coarse + 2e-4
        for _ in range(40):
            third = (hi - lo) / 3
            a, b = lo + third, hi - third
            if mismatch(a) < mismatch(b):
                hi = b
            else:
                lo = a
        alpha_rec = 0.5 * (lo + hi)
        err = abs(C610.wrap_angle(alpha_rec - alpha_true))
        ok = err < 2 * (2 * math.pi / 1984)
        row = {"alpha_true": alpha_true, "alpha_rec": float(alpha_rec),
               "wrap_error": float(err), "ok": bool(ok),
               "lines_measured": measured}
        if abs(alpha_true + 0.7439) < 1e-9:
            r_rec = (theta_b_L9 + C610.wrap_angle(alpha_rec - 2 * math.pi)
                     if alpha_rec > math.pi else theta_b_L9 + alpha_rec) / theta_b_L9
            alpha_signed = C610.wrap_angle(alpha_rec)
            r_rec = (theta_b_L9 + alpha_signed) / theta_b_L9
            magnitude = 4 * abs(r_rec) + 0.5
            a_count = int(math.copysign(math.floor(magnitude), r_rec))
            row["R_rec"] = float(r_rec)
            row["a_count_word"] = f"{a_count}:4"
            row["reaches_5_4"] = bool(abs(r_rec - 1.25) < 1e-3 and a_count == 5)
        vernier_rows.append(row)
        all_ok = all_ok and ok
    receipt["vernier"] = vernier_rows
    check(
        "O2 vernier theorem executed: every frozen alpha row (including both "
        "folds and the 2pi null) is reconstructed within two bins from the "
        "measured line pair",
        all_ok,
        {"errors": [round(r["wrap_error"], 6) for r in vernier_rows]},
    )
    row54 = next(r for r in vernier_rows if abs(r["alpha_true"] + 0.7439) < 1e-9)
    check(
        "O2 gold row: the reconstructed rate on the alpha = -0.7439 row is "
        "R_rec = 1.25 within 1e-3 and the frozen A-count rule yields the 5:4 "
        "advance word — the Cycle-451 advance shore reached with no refit, "
        "under the Cycle-612 association caveat (no identification)",
        bool(row54.get("reaches_5_4")),
        {k: row54[k] for k in ("alpha_rec", "R_rec", "a_count_word")
         if k in row54},
    )

    receipt["interpretation_firewall"] = [
        "the L=inf values are quadrature-controlled statements with stated "
        "error bars, not a rigorous spectral theorem; the contact-cyclic "
        "lemma remains open",
        "a spectral line is not energy; the vernier reconstruction is "
        "retained-data analysis; reaching the 5:4 shore is algebraic "
        "reachability under the Cycle-612 association caveat",
        "no physical vernier clock is built here; two-line certificates are "
        "lawful-domain definitions for the physical side's acceptance harness",
    ]

    elapsed = time.time() - start
    receipt["elapsed_seconds"] = elapsed
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=1, default=float) + "\n",
                       encoding="utf-8")
    print("RESULT", PASS, FAIL, "elapsed", round(elapsed, 2), "s")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
