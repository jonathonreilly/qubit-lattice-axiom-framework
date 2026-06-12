#!/usr/bin/env python3
"""Wilson-mass holonomy-twisted edge realization (signed-gravity twist datum).

Companion runner for
docs/SIGNED_GRAVITY_WILSON_MASS_HOLONOMY_TWISTED_EDGE_REALIZATION_NARROW_THEOREM_NOTE_2026-06-11.md

Verifies:

  [W0] pure staggered hosts no twist datum on ANY closed background:
       {Gamma_5, H_stag} = 0 exactly (free + random U(1) backgrounds),
       block-off-diagonality in the parity grading, eta_delta = 0.
  [W1] Wilson-mass cylinder (named route, minimal model) in the gapped
       window with boundary-cycle holonomy theta: in-gap edge sector
       sharply localized (edge weight > 0.999); label table — theta = 0:
       h_delta = 1 per
       edge (no label); theta = +/-0.7: chi_bottom = sign(theta);
       theta = pi: eta_delta = 0.
  [W2] orientation pairing chi_top = -chi_bottom at every defined theta.
  [W3] controls: trivial window m = +1 has an EMPTY in-gap edge set;
       label stable under L_x = 20 -> 40 while the tower grows.

Deterministic, numpy only, runtime seconds.
Exit code 0 iff TOTAL: PASS=n FAIL=0.
"""

from __future__ import annotations

import sys

import numpy as np

PASS = 0
FAIL = 0
DELTA = 1e-8


def check(tag: str, label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        s = "PASS"
    else:
        FAIL += 1
        s = "FAIL"
    print(f"  [{s}] [{tag}] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 76)
    print(title)
    print("-" * 76)


def eta_h(lam: np.ndarray, delta: float = DELTA) -> tuple[int, int]:
    eta = int(np.sum(lam > delta) - np.sum(lam < -delta))
    h = int(np.sum(np.abs(lam) <= delta))
    return eta, h


# ---------------------------------------------------------------------------
# (W0) massless staggered on a torus with arbitrary U(1) background
# ---------------------------------------------------------------------------

def staggered_torus(L: int, seed=None) -> np.ndarray:
    rng = np.random.default_rng(seed)
    N = L * L
    idx = lambda x, y: (x % L) * L + (y % L)
    H = np.zeros((N, N), dtype=complex)
    if seed is None:
        Ux = np.ones((L, L)); Uy = np.ones((L, L))
    else:
        Ux = np.exp(1j * rng.uniform(0, 2 * np.pi, (L, L)))
        Uy = np.exp(1j * rng.uniform(0, 2 * np.pi, (L, L)))
    for x in range(L):
        for y in range(L):
            i = idx(x, y)
            H[i, idx(x + 1, y)] += 0.5j * Ux[x, y]
            H[idx(x + 1, y), i] += -0.5j * np.conj(Ux[x, y])
            ey = (-1.0) ** x
            H[i, idx(x, y + 1)] += 0.5j * ey * Uy[x, y]
            H[idx(x, y + 1), i] += -0.5j * ey * np.conj(Uy[x, y])
    return H


# ---------------------------------------------------------------------------
# (W1) Wilson-mass cylinder (QWZ-form minimal model of the named route)
# ---------------------------------------------------------------------------

S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.diag([1.0, -1.0]).astype(complex)


def cylinder_edge_data(Lx, Ly, m, r, theta, gap_half=0.5):
    """Harvest in-gap states with per-edge localization weights.

    Returns (bottom_levels, top_levels, ambiguous_count, min_edge_weight)."""
    bot, top = [], []
    ambiguous = 0
    min_w = 1.0
    for n in range(Lx):
        k = (2 * np.pi * n + theta) / Lx
        Hk = np.zeros((2 * Ly, 2 * Ly), dtype=complex)
        ons = np.sin(k) * S1 + (m + r * (1 - np.cos(k)) + r) * S3
        hop = (-0.5j) * S2 + (-0.5 * r) * S3
        for y in range(Ly):
            Hk[2 * y:2 * y + 2, 2 * y:2 * y + 2] += ons
            if y + 1 < Ly:
                Hk[2 * y:2 * y + 2, 2 * y + 2:2 * y + 4] += hop
                Hk[2 * y + 2:2 * y + 4, 2 * y:2 * y + 2] += hop.conj().T
        w, V = np.linalg.eigh(Hk)
        wt_b = (np.abs(V[:6, :]) ** 2).sum(axis=0)
        wt_t = (np.abs(V[-6:, :]) ** 2).sum(axis=0)
        for lam, wb, wt in zip(w, wt_b, wt_t):
            if abs(lam) < gap_half:
                if wb > 0.5:
                    bot.append(lam)
                    min_w = min(min_w, wb)
                elif wt > 0.5:
                    top.append(lam)
                    min_w = min(min_w, wt)
                else:
                    ambiguous += 1
    return np.array(sorted(bot)), np.array(sorted(top)), ambiguous, min_w


def label_of(lam: np.ndarray) -> str:
    e, h = eta_h(lam)
    if h > 0:
        return "UNDEF(gap)"
    if e == 0:
        return "UNDEF(eta=0)"
    return "+1" if e > 0 else "-1"


def main() -> int:
    print("=" * 76)
    print("WILSON-MASS HOLONOMY-TWISTED EDGE REALIZATION (signed-gravity)")
    print("(W0) pure staggered: no twist datum on ANY background;")
    print("(W1/W2) the named Wilson-mass route hosts it, twist = holonomy")
    print("=" * 76)

    # =======================================================================
    section("[W0] structural obstruction: pure staggered, arbitrary background")
    # =======================================================================
    L = 6
    G5 = np.diag([(-1.0) ** ((i // L) + (i % L)) for i in range(L * L)])
    for seed, lab in ((None, "free background"), (1, "random U(1) seed 1"),
                      (2, "random U(1) seed 2")):
        H = staggered_torus(L, seed)
        anti = np.abs(G5 @ H @ G5 + H).max()
        lam = np.linalg.eigvalsh(H)
        e, _ = eta_h(lam)
        check("W0", f"{{Gamma_5, H_stag}} = 0 exactly and eta_delta = 0 "
                    f"({lab})", anti < 1e-14 and e == 0,
              f"max|anti| = {anti:.1e}, eta = {e:+d}")
    # structural block-off-diagonality: P_even H P_even = 0 = P_odd H P_odd
    par = np.array([((i // L) + (i % L)) % 2 for i in range(L * L)])
    H = staggered_torus(L, 1)
    blk_ee = np.abs(H[np.ix_(par == 0, par == 0)]).max()
    blk_oo = np.abs(H[np.ix_(par == 1, par == 1)]).max()
    check("W0", "H_stag is block-off-diagonal in the parity grading "
                "(every hop flips parity, phases irrelevant)",
          blk_ee < 1e-14 and blk_oo < 1e-14,
          f"|even-even| = {blk_ee:.1e}, |odd-odd| = {blk_oo:.1e}")

    # =======================================================================
    section("[W1] Wilson-mass cylinder: in-gap edge tower and label table")
    # =======================================================================
    Lx, Ly, m, r = 20, 24, -1.0, 1.0
    results = {}
    min_w_all, amb_all = 1.0, 0
    for theta in (0.0, 0.7, -0.7, np.pi):
        bot, top, amb, mw = cylinder_edge_data(Lx, Ly, m, r, theta)
        results[theta] = (bot, top)
        amb_all += amb
        min_w_all = min(min_w_all, mw)
    check("W1", "in-gap localization is bimodal: every in-gap state sits on "
                "exactly one edge with weight > 0.999; zero ambiguous states",
          amb_all == 0 and min_w_all > 0.999,
          f"min edge weight = {min_w_all:.6f}, ambiguous = {amb_all}")
    bot0, top0 = results[0.0]
    e0b, h0b = eta_h(bot0)
    e0t, h0t = eta_h(top0)
    check("W1", "theta = 0: zero crossing on each edge (h_delta = 1) -> "
                "label undefined, matching the untwisted no-label case",
          h0b == 1 and h0t == 1, f"h_bottom = {h0b}, h_top = {h0t}")
    botp, topp = results[0.7]
    check("W1", "theta = +0.7: chi_bottom = +1 (h_delta = 0, eta = +1)",
          label_of(botp) == "+1", f"eta = {eta_h(botp)[0]:+d}, "
          f"n_states = {len(botp)}")
    botm, topm = results[-0.7]
    check("W1", "theta = -0.7: chi_bottom = -1 (sign tracks the holonomy)",
          label_of(botm) == "-1", f"eta = {eta_h(botm)[0]:+d}")
    botpi, toppi = results[np.pi]
    check("W1", "theta = pi: eta_delta = 0 on each edge (the symmetric "
                "half-twist point) -> label undefined",
          eta_h(botpi)[0] == 0 and eta_h(toppi)[0] == 0
          and eta_h(botpi)[1] == 0,
          f"eta_bottom = {eta_h(botpi)[0]:+d}, eta_top = {eta_h(toppi)[0]:+d}")

    # =======================================================================
    section("[W2] orientation pairing: the two edges carry opposite labels")
    # =======================================================================
    ok_pair = True
    for theta in (0.7, -0.7):
        bot, top = results[theta]
        eb, _ = eta_h(bot)
        et, _ = eta_h(top)
        ok_pair &= (np.sign(eb) == -np.sign(et)) and eb != 0
    check("W2", "chi_top = -chi_bottom at every defined theta "
                "(orientation pair realized geometrically)",
          ok_pair,
          f"theta=+0.7: ({eta_h(results[0.7][0])[0]:+d}, "
          f"{eta_h(results[0.7][1])[0]:+d}); "
          f"theta=-0.7: ({eta_h(results[-0.7][0])[0]:+d}, "
          f"{eta_h(results[-0.7][1])[0]:+d})")

    # =======================================================================
    section("[W3] controls: trivial window; size stability")
    # =======================================================================
    bot_t, top_t, amb_t, _ = cylinder_edge_data(Lx, Ly, +1.0, r, 0.7)
    check("W3", "trivial window m = +1: the in-gap edge set is EMPTY "
                "(no label can be defined; the gapped-window structure is "
                "load-bearing)",
          len(bot_t) == 0 and len(top_t) == 0 and amb_t == 0,
          f"in-gap states = {len(bot_t) + len(top_t) + amb_t}")
    bot20, _, _, _ = cylinder_edge_data(20, Ly, m, r, 0.7)
    bot40, _, _, _ = cylinder_edge_data(40, Ly, m, r, 0.7)
    check("W3", "size stability: L_x = 20 -> 40 grows the edge tower while "
                "the label stays chi = +1 (quantized, not drifting)",
          eta_h(bot20)[0] == 1 and eta_h(bot40)[0] == 1
          and len(bot40) > len(bot20),
          f"n_states {len(bot20)} -> {len(bot40)}, eta stays "
          f"{eta_h(bot40)[0]:+d}")
    # holonomy continuation: a fine theta sweep never yields |eta| > 1 in
    # the defined branch (quantization across the sweep)
    ok_q = True
    for theta in np.linspace(0.15, np.pi - 0.15, 9):
        bot, top = cylinder_edge_data(Lx, Ly, m, r, float(theta))[:2]
        e, h = eta_h(bot)
        if h == 0 and abs(e) > 1:
            ok_q = False
    check("W3", "quantization across a fine holonomy sweep: |eta| <= 1 on "
                "every defined point (the label is a sign, not a magnitude)",
          ok_q)

    print()
    print("=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
