#!/usr/bin/env python3
"""Mixed-precision raw-kernel certificate at h = 0.125.

This runner answers the literal narrow gate question from
`docs/LATTICE_NN_HIGH_PRECISION_NOTE.md` directly:

    does the raw nearest-neighbor lattice refinement trend extend one
    more step to h = 0.125, without any rescaling trick, while keeping
    the same raw kernel and the same observables?

It does so by re-executing the raw NN kernel from
`scripts/lattice_nn_continuum.py` with the same per-edge factor
`exp(1j * k * act) * w / L` and the same observables. Geometry and
per-edge phases retain the canonical float64 evaluation; amplitude
accumulation uses mpmath so the large dynamic range at h = 0.125 does
not overflow.

The mpmath accumulator does not rescale the kernel: there is no schedule,
observable inspection, or data-dependent correction. This is a specified
mixed-precision computation, not a claim of exact-real arithmetic.

What this runner establishes:

  1. RAW-KERNEL h = 0.125 IS NUMERICALLY EVALUABLE
     The full propagation succeeds at h = 0.125 with mpmath amplitude
     accumulation at dps = 30. This closes the historical noncompletion
     gate for the specified mixed-precision implementation.

  2. THE FULL RAW OBSERVABLE ROW AT h = 0.125
     Gravity centroid, k = 0 centroid, MI, classical purity,
     total-variation distance, and Born residual are computed from the
     raw kernel at h = 0.125 directly. This is the "h = 0.125
     Born-clean raw row" the note's gate was asking for. Born stays
     machine-clean, confirming the Born-clean refinement trend extends
     one more step.

  3. LIVE ALL-OBSERVABLE COMPARATOR
     The deterministic-rescale row is recomputed in the same process,
     without rounded or hard-coded targets. Gravity, k = 0, MI, purity,
     d_TV, and Born are all asserted with an explicit absolute tolerance;
     both Born residuals must also satisfy the declared diagnostic threshold.
     This is a pointwise numerical comparison at h = 0.125 in the recorded
     numerical environment, not a universal exact step-scale-invariance
     theorem or a cross-platform forward-error theorem.

  4. PRECISION AND CANONICAL-IMPLEMENTATION GUARDS
     At h = 0.25 the mixed-precision row is checked against both the canonical
     raw implementation and the deterministic-rescale implementation. At
     h = 0.125 the raw row is recomputed at dps = 40 and must agree with the
     dps = 30 row within 1e-24 on every returned quantity. The latter threshold
     is declared before either row is computed and is eight orders tighter
     than the separate 1e-12 raw/rescaled protocol-acceptance threshold.

PERFORMANCE NOTE
   The runner uses mpmath at `dps = 30` because: (a) the dynamic range
   issue is exponent, not mantissa — the loose order-10^442 scale warning
   for 320 transitions needs an
   exponent field, not 100+ decimal digits; (b) modest precision is
   independently checked against dps = 40. The 1e-12 comparator threshold is
   a predeclared acceptance bound for the two implemented rows, not an
   accuracy claim for either row. To keep run time inside the cache budget,
   the kernel is structured so the bulk of per-edge work uses float64 for the
   phase `act = dl - ret` and only the amplitude multiplications are mpmath.
   This preserves the phase evaluation of the canonical float64 runner and
   changes only the accumulator's dynamic range.
"""

from __future__ import annotations

import math
import os
import platform
import sys
import time
from collections import defaultdict

AUDIT_INPUT_PATHS = (
    "scripts/lattice_nn_continuum.py",
    "scripts/lattice_nn_deterministic_rescale.py",
)

try:
    import mpmath as mp
except ImportError:  # pragma: no cover
    raise SystemExit(
        "mpmath is required. Install it (pip install mpmath) and rerun."
    )

try:
    from scripts.lattice_nn_continuum import measure_full as measure_canonical
    from scripts.lattice_nn_deterministic_rescale import (
        measure_full as measure_rescaled,
    )
except ImportError:  # Direct execution from scripts/.
    from lattice_nn_continuum import measure_full as measure_canonical
    from lattice_nn_deterministic_rescale import (
        measure_full as measure_rescaled,
    )


# Kernel constants — exactly as in scripts/lattice_nn_continuum.py.
BETA = 0.8
K_PHYS = 5.0
LAM = 10.0
N_YBINS = 8
PHYS_W = 20.0
PHYS_L = 40.0
SLIT_Y = 3.0
MASS_Y = 8.0
OBS_ABS_TOL = mp.mpf("1e-12")
BORN_CLEAN_TOL = mp.mpf("1e-10")
PRIMARY_DPS = 30
PRECISION_CHECK_DPS = 40
PRECISION_ABS_TOL = mp.mpf("1e-24")
OBSERVABLE_KEYS = ("gravity", "gk0", "MI", "pur_cl", "dtv", "born")


def _generate_nn_lattice(spacing: float):
    """3-edge NN lattice — identical geometry to lattice_nn_continuum.py."""
    nl = int(PHYS_L / spacing) + 1
    hw = int(PHYS_W / spacing)
    pos = []
    adj = defaultdict(list)
    nmap = {}
    for layer in range(nl):
        x = layer * spacing
        for iy in range(-hw, hw + 1):
            y = iy * spacing
            idx = len(pos)
            pos.append((x, y))
            nmap[(layer, iy)] = idx
    for layer in range(nl - 1):
        for iy in range(-hw, hw + 1):
            si = nmap.get((layer, iy))
            if si is None:
                continue
            for diy in (-1, 0, 1):
                iyn = iy + diy
                if abs(iyn) > hw:
                    continue
                di = nmap.get((layer + 1, iyn))
                if di is not None:
                    adj[si].append(di)
    return pos, dict(adj), nl, hw, nmap


def _build_mass_field(pos, mass_idx):
    """Same 1/r mass-coupling field as lattice_nn_continuum.py."""
    mx, my = pos[mass_idx]
    field = [0.0] * len(pos)
    strength = 0.0005
    for i, (ix, iy) in enumerate(pos):
        r = math.sqrt((ix - mx) ** 2 + (iy - my) ** 2) + 0.1
        field[i] = strength / r
    return field


def _propagate_mpmath(pos, adj, field, k, blocked, n, spacing):
    """Raw NN propagation in mpmath.

    Identical kernel to lattice_nn_continuum.propagate:
       ea = exp(1j * k * act) * w / L
       amps[j] += amps[i] * ea

    The amplitude accumulator is mpmath complex so the float64 overflow
    at h = 0.125 disappears. Per-edge phase `act = dl - ret` is computed
    in float64 (it is a smooth, ~O(1) quantity) and only the
    accumulator multiplication is mpmath. The kernel itself is unchanged.
    """
    order = sorted(range(n), key=lambda i: pos[i][0])
    amps = [mp.mpc(0)] * n
    src = next(
        i for i, (x, y) in enumerate(pos)
        if abs(x) < 1e-10 and abs(y) < 1e-10
    )
    amps[src] = mp.mpc(1)

    # Precompute the three field-free edge kernels.
    base_kernels = {}
    for diy in (-1, 0, 1):
        dy = diy * spacing
        L = math.sqrt(spacing * spacing + dy * dy)
        theta = math.atan2(abs(dy), spacing)
        w = math.exp(-BETA * theta * theta)
        # Field-free phase angle:
        phase = k * L
        # Stored as mpmath so multiplication does not narrow precision.
        base_kernels[diy] = mp.mpc(
            math.cos(phase) * w / L,
            math.sin(phase) * w / L,
        )

    field_free = all(f == 0.0 for f in field)

    if field_free:
        for i in order:
            ai = amps[i]
            if i in blocked:
                continue
            # Use mpmath abs for overflow safety
            if mp.almosteq(ai, mp.mpc(0)):
                continue
            xi, yi = pos[i]
            iy_i = round(yi / spacing)
            for j in adj.get(i, []):
                if j in blocked:
                    continue
                xj, yj = pos[j]
                iy_j = round(yj / spacing)
                diy = iy_j - iy_i
                amps[j] += ai * base_kernels[diy]
        return amps

    # Field-coupled: per-edge act varies due to lf.
    for i in order:
        ai = amps[i]
        if i in blocked:
            continue
        if mp.almosteq(ai, mp.mpc(0)):
            continue
        xi, yi = pos[i]
        iy_i = round(yi / spacing)
        for j in adj.get(i, []):
            if j in blocked:
                continue
            xj, yj = pos[j]
            iy_j = round(yj / spacing)
            diy = iy_j - iy_i
            dy = diy * spacing
            L = math.sqrt(spacing * spacing + dy * dy)
            lf = 0.5 * (field[i] + field[j])
            dl = L * (1.0 + lf)
            inner = dl * dl - L * L
            ret = math.sqrt(inner) if inner > 0 else 0.0
            act = dl - ret
            phase = k * act
            theta = math.atan2(abs(dy), spacing)
            w = math.exp(-BETA * theta * theta)
            inv_L = w / L
            ker = mp.mpc(
                math.cos(phase) * inv_L,
                math.sin(phase) * inv_L,
            )
            amps[j] += ai * ker
    return amps


def _abs2(z):
    """|z|^2 for mpmath complex, returns mpf."""
    return z.real * z.real + z.imag * z.imag


def measure_raw_kernel(spacing: float):
    """Measure all framework observables at this spacing using the raw kernel.

    Mirrors lattice_nn_continuum.measure_full exactly, but uses
    arbitrary-precision arithmetic in the amplitude accumulator.
    """
    pos, adj, nl, hw, nmap = _generate_nn_lattice(spacing)
    n = len(pos)
    det_layer = nl - 1
    det = [nmap[(det_layer, iy)] for iy in range(-hw, hw + 1)
           if (det_layer, iy) in nmap]
    bl = nl // 3
    gl = 2 * nl // 3

    # Slit setup — same recipe as the continuum runner.
    slit_iy = max(1, round(SLIT_Y / spacing))
    bi = [nmap[(bl, iy)] for iy in range(-hw, hw + 1)
          if (bl, iy) in nmap]
    sa_range = range(slit_iy, min(slit_iy + max(2, round(2 / spacing)), hw + 1))
    sb_range = range(-min(slit_iy + max(1, round(1 / spacing)), hw),
                     -slit_iy + 1)
    sa = [nmap[(bl, iy)] for iy in sa_range if (bl, iy) in nmap]
    sb = [nmap[(bl, iy)] for iy in sb_range if (bl, iy) in nmap]
    if not sa or not sb:
        return None
    blocked = set(bi) - set(sa + sb)
    field_f = [0.0] * n

    mass_iy = round(MASS_Y / spacing)
    mass_idx = nmap.get((gl, mass_iy))
    if mass_idx is None:
        return None
    field_m = _build_mass_field(pos, mass_idx)

    # Gravity (full slits, with and without mass).
    af = _propagate_mpmath(pos, adj, field_f, K_PHYS, blocked, n, spacing)
    am = _propagate_mpmath(pos, adj, field_m, K_PHYS, blocked, n, spacing)
    pf = sum((_abs2(af[d]) for d in det), mp.mpf(0))
    pm = sum((_abs2(am[d]) for d in det), mp.mpf(0))
    if pf == 0 or pm == 0:
        return None
    yf = sum((_abs2(af[d]) * pos[d][1] for d in det), mp.mpf(0)) / pf
    ym = sum((_abs2(am[d]) * pos[d][1] for d in det), mp.mpf(0)) / pm
    gravity = ym - yf

    # k = 0 centroid (with and without mass).
    am0 = _propagate_mpmath(pos, adj, field_m, 0.0, blocked, n, spacing)
    af0 = _propagate_mpmath(pos, adj, field_f, 0.0, blocked, n, spacing)
    pm0 = sum((_abs2(am0[d]) for d in det), mp.mpf(0))
    pf0 = sum((_abs2(af0[d]) for d in det), mp.mpf(0))
    gk0 = mp.mpf(0)
    if pm0 > 0 and pf0 > 0:
        gk0 = (
            sum((_abs2(am0[d]) * pos[d][1] for d in det), mp.mpf(0)) / pm0
            - sum((_abs2(af0[d]) * pos[d][1] for d in det), mp.mpf(0)) / pf0
        )

    # Slit-A / slit-B propagations (no mass, single slit open).
    pa = _propagate_mpmath(pos, adj, field_f, K_PHYS, blocked | set(sb), n, spacing)
    pb = _propagate_mpmath(pos, adj, field_f, K_PHYS, blocked | set(sa), n, spacing)
    bw = 2 * (PHYS_W + spacing) / N_YBINS
    prob_a = [mp.mpf(0)] * N_YBINS
    prob_b = [mp.mpf(0)] * N_YBINS
    for d in det:
        b2 = max(0, min(N_YBINS - 1, int((pos[d][1] + PHYS_W + spacing) / bw)))
        prob_a[b2] += _abs2(pa[d])
        prob_b[b2] += _abs2(pb[d])
    na = sum(prob_a, mp.mpf(0))
    nb = sum(prob_b, mp.mpf(0))
    MI = mp.mpf(0)
    if na > 0 and nb > 0:
        pa_n = [p / na for p in prob_a]
        pb_n = [p / nb for p in prob_b]
        H = mp.mpf(0)
        Hc = mp.mpf(0)
        for b3 in range(N_YBINS):
            pm2 = mp.mpf('0.5') * pa_n[b3] + mp.mpf('0.5') * pb_n[b3]
            if pm2 > 0:
                H -= pm2 * mp.log(pm2, 2)
            if pa_n[b3] > 0:
                Hc -= mp.mpf('0.5') * pa_n[b3] * mp.log(pa_n[b3], 2)
            if pb_n[b3] > 0:
                Hc -= mp.mpf('0.5') * pb_n[b3] * mp.log(pb_n[b3], 2)
        MI = H - Hc

    # Classical purity (CL decoherence overlay).
    env_depth = max(1, round(nl / 6))
    st = bl + 1
    sp = min(nl - 1, st + env_depth)
    mid = []
    for l in range(st, sp):
        mid.extend([nmap[(l, iy)] for iy in range(-hw, hw + 1)
                    if (l, iy) in nmap])
    ba = [mp.mpc(0)] * N_YBINS
    bb = [mp.mpc(0)] * N_YBINS
    for m in mid:
        b2 = max(0, min(N_YBINS - 1, int((pos[m][1] + PHYS_W + spacing) / bw)))
        ba[b2] += pa[m]
        bb[b2] += pb[m]
    S = sum((_abs2(a - b) for a, b in zip(ba, bb)), mp.mpf(0))
    NA = sum((_abs2(a) for a in ba), mp.mpf(0))
    NB = sum((_abs2(b) for b in bb), mp.mpf(0))
    Sn = S / (NA + NB) if (NA + NB) > 0 else mp.mpf(0)
    Dcl = mp.e ** (-mp.mpf(LAM) ** 2 * Sn)
    rho = {}
    for d1 in det:
        for d2 in det:
            rho[(d1, d2)] = (
                mp.conj(pa[d1]) * pa[d2]
                + mp.conj(pb[d1]) * pb[d2]
                + Dcl * mp.conj(pa[d1]) * pb[d2]
                + Dcl * mp.conj(pb[d1]) * pa[d2]
            )
    tr = sum((rho[(d, d)].real for d in det), mp.mpf(0))
    pur_cl = mp.mpf(1)
    if tr > 0:
        for key in rho:
            rho[key] /= tr
        pur_cl = sum((_abs2(v) for v in rho.values()), mp.mpf(0))

    # Total-variation distance.
    da = {d: _abs2(pa[d]) for d in det}
    db = {d: _abs2(pb[d]) for d in det}
    na2 = sum(da.values(), mp.mpf(0))
    nb2 = sum(db.values(), mp.mpf(0))
    dtv = mp.mpf(0)
    if na2 > 0 and nb2 > 0:
        dtv = mp.mpf('0.5') * sum(
            (abs(da[d] / na2 - db[d] / nb2) for d in det), mp.mpf(0)
        )

    # Born (3-slit).
    born = mp.nan
    upper = sorted([i for i in bi if pos[i][1] > spacing],
                   key=lambda i: pos[i][1])
    lower = sorted([i for i in bi if pos[i][1] < -spacing],
                   key=lambda i: -pos[i][1])
    middle = [i for i in bi if abs(pos[i][1]) <= spacing]
    if upper and lower and middle:
        s_a = [upper[0]]
        s_b = [lower[0]]
        s_c = [middle[0]]
        all_s = set(s_a + s_b + s_c)
        other = set(bi) - all_s
        probs = {}
        for key, open_set in [
            ("abc", all_s),
            ("ab", set(s_a + s_b)),
            ("ac", set(s_a + s_c)),
            ("bc", set(s_b + s_c)),
            ("a", set(s_a)),
            ("b", set(s_b)),
            ("c", set(s_c)),
        ]:
            bl2 = other | (all_s - open_set)
            a = _propagate_mpmath(pos, adj, field_f, K_PHYS, bl2, n, spacing)
            probs[key] = [_abs2(a[d]) for d in det]
        I3 = mp.mpf(0)
        P = mp.mpf(0)
        for di in range(len(det)):
            i3 = (
                probs["abc"][di]
                - probs["ab"][di]
                - probs["ac"][di]
                - probs["bc"][di]
                + probs["a"][di]
                + probs["b"][di]
                + probs["c"][di]
            )
            I3 += abs(i3)
            P += probs["abc"][di]
        born = I3 / P if P > 0 else mp.nan

    return {
        "h": spacing, "n": n, "nl": nl, "npl": 2 * hw + 1,
        "gravity": gravity, "gk0": gk0,
        "MI": MI, "pur_cl": pur_cl, "dtv": dtv, "born": born,
    }


def _live_comparison(raw, rescaled):
    """Compare every returned observable without rounding either row."""
    diffs = {
        key: abs(mp.mpf(raw[key]) - mp.mpf(rescaled[key]))
        for key in OBSERVABLE_KEYS
    }
    finite = all(
        mp.isfinite(mp.mpf(row[key]))
        for row in (raw, rescaled)
        for key in OBSERVABLE_KEYS
    )
    each_observable_ok = finite and all(
        diff <= OBS_ABS_TOL for diff in diffs.values()
    )
    raw_born_ok = mp.mpf(raw["born"]) < BORN_CLEAN_TOL
    rescaled_born_ok = mp.mpf(rescaled["born"]) < BORN_CLEAN_TOL
    return diffs, each_observable_ok and raw_born_ok and rescaled_born_ok


def _print_comparison(raw, comparator, diffs):
    """Print full-value live comparisons used by the exit-code assertions."""
    labels = {
        "gravity": "gravity",
        "gk0": "k=0",
        "MI": "MI",
        "pur_cl": "purity",
        "dtv": "d_TV",
        "born": "Born",
    }
    for key in OBSERVABLE_KEYS:
        raw_value = mp.nstr(mp.mpf(raw[key]), 24, min_fixed=0, max_fixed=0)
        comparator_value = mp.nstr(
            mp.mpf(comparator[key]), 24, min_fixed=0, max_fixed=0
        )
        print(
            f"    {labels[key]:7s}: raw={raw_value}  "
            f"comparator={comparator_value}  "
            f"abs_diff={float(diffs[key]):.3e}"
        )


def main():
    mp.mp.dps = PRIMARY_DPS

    print("=" * 95)
    print("MIXED-PRECISION RAW-KERNEL CERTIFICATE AT h = 0.125")
    print(f"  float64 geometry/phases; mpmath amplitude accumulation "
          f"(dps = {mp.mp.dps})")
    print(f"  physical: W={PHYS_W}, L={PHYS_L}, k={K_PHYS}, "
          "field_strength=0.0005, mass at y=8.0")
    print(
        "  environment: "
        f"Python={platform.python_version()} "
        f"implementation={platform.python_implementation()} "
        f"mpmath={mp.__version__} "
        f"system={platform.system()} "
        f"machine={platform.machine()} "
        f"float_mant_dig={sys.float_info.mant_dig}"
    )
    print("=" * 95)
    print()

    # h = 0.25 sanity checks against the canonical raw implementation and
    # a live deterministic-rescale run.
    print("--- 1. RAW-KERNEL h = 0.25 SANITY CHECK ---")
    print("    (live comparisons; no rounded or hard-coded targets)")
    t0 = time.time()
    r25 = measure_raw_kernel(0.25)
    c25 = measure_canonical(0.25)
    d25 = measure_rescaled(0.25)
    elapsed_25 = time.time() - t0
    if r25 is None or c25 is None or d25 is None:
        print("    FAIL: measurement returned None")
        sys.exit(1)
    diffs_25_canonical, canonical_ok = _live_comparison(r25, c25)
    diffs_25_rescaled, rescaled_25_ok = _live_comparison(r25, d25)
    sanity_ok = canonical_ok and rescaled_25_ok
    print(f"    nl = {r25['nl']}, nodes = {r25['n']}")
    print("    canonical raw comparator:")
    _print_comparison(r25, c25, diffs_25_canonical)
    print("    deterministic-rescale comparator:")
    _print_comparison(r25, d25, diffs_25_rescaled)
    print(f"    SANITY: {'PASS' if sanity_ok else 'FAIL'}  "
          f"(elapsed {elapsed_25:.1f}s)")
    print()

    # h = 0.125: the gate target.
    print("--- 2. RAW-KERNEL h = 0.125 CERTIFICATE (gate target) ---")
    print("    (live comparison; no rounded or hard-coded targets)")
    t0 = time.time()
    r125 = measure_raw_kernel(0.125)
    d125 = measure_rescaled(0.125)
    elapsed_125 = time.time() - t0
    if r125 is None or d125 is None:
        print("    FAIL: measurement returned None")
        sys.exit(1)
    diffs_125, comparison_ok = _live_comparison(r125, d125)
    print(f"    nl = {r125['nl']}, nodes = {r125['n']}")
    _print_comparison(r125, d125, diffs_125)
    raw_born_ok = mp.mpf(r125["born"]) < BORN_CLEAN_TOL
    rescaled_born_ok = mp.mpf(d125["born"]) < BORN_CLEAN_TOL
    print(f"    raw Born diagnostic (< 1e-10):      "
          f"{'YES' if raw_born_ok else 'NO'}")
    print(f"    rescaled Born diagnostic (< 1e-10): "
          f"{'YES' if rescaled_born_ok else 'NO'}")
    print(f"    LIVE ALL-OBSERVABLE COMPARISON (abs tol 1e-12): "
          f"{'PASS' if comparison_ok else 'FAIL'}  "
          f"(elapsed {elapsed_125:.1f}s)")
    print()

    print("--- 3. RAW-KERNEL PRECISION-STABILITY CHECK ---")
    t0 = time.time()
    with mp.workdps(PRECISION_CHECK_DPS):
        r125_hi = measure_raw_kernel(0.125)
        if r125_hi is None:
            print("    FAIL: higher-precision measurement returned None")
            sys.exit(1)
        precision_diffs = {
            key: abs(mp.mpf(r125[key]) - mp.mpf(r125_hi[key]))
            for key in OBSERVABLE_KEYS
        }
        precision_ok = all(
            mp.isfinite(mp.mpf(r125_hi[key]))
            and precision_diffs[key] <= PRECISION_ABS_TOL
            for key in OBSERVABLE_KEYS
        )
    elapsed_precision = time.time() - t0
    print(
        f"    dps={PRIMARY_DPS} versus dps={PRECISION_CHECK_DPS}; "
        f"predeclared abs tol={float(PRECISION_ABS_TOL):.0e}"
    )
    for key in OBSERVABLE_KEYS:
        print(f"    {key:7s}: abs_diff={float(precision_diffs[key]):.3e}")
    print(
        f"    PRECISION STABILITY: {'PASS' if precision_ok else 'FAIL'}  "
        f"(elapsed {elapsed_precision:.1f}s)"
    )
    print()

    overall = sanity_ok and comparison_ok and precision_ok
    print("--- VERDICT ---")
    print(f"    raw-kernel h = 0.25 canonical regression: "
          f"{'PASS' if sanity_ok else 'FAIL'}")
    print(f"    raw-kernel h = 0.125 successful run:      PASS  "
          f"(mpmath at dps={mp.mp.dps})")
    print(f"    raw-kernel h = 0.125 Born diagnostic:     "
          f"{'YES' if raw_born_ok else 'NO'}")
    print(f"    live all-observable comparison:           "
          f"{'PASS' if comparison_ok else 'FAIL'}")
    print(f"    dps precision-stability guard:            "
          f"{'PASS' if precision_ok else 'FAIL'}")
    print()
    if overall:
        print("    BOUNDED CERTIFICATE: in the recorded numerical environment,")
        print("    the supplied raw NN protocol at h = 0.125 completes and its")
        print("    live deterministic-rescale comparator agrees on all six")
        print("    returned quantities within the predeclared 1e-12 threshold.")
        print("    This is not a universal rescale or cross-platform theorem.")
    else:
        print("    CERTIFICATE NOT ESTABLISHED: at least one decisive guard failed.")
    print()
    print(f"    RUNNER STATUS: {'PASS' if overall else 'FAIL'}")
    sys.exit(0 if overall else 1)


if __name__ == "__main__":
    main()
