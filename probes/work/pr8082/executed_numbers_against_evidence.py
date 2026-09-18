#!/usr/bin/env python3
"""J:attack:PR8082 - native Gaussian moment-jet note (PR #8082), attack pattern (c) EXECUTED NUMBERS: every executed range, count,
width and resource figure the note states, checked against the retained evidence on the PR branch (the packet's source_draft/high and
source_draft/omega RESULT, ROOT_ACCEPTANCE and EVENTS files and the two runtime protocols), read at the pinned PR head:
  * high moments: 189 events (and the EVENTS.ndjson line count), six retained output files, eight new P/O moment intervals (orders 7-10
    of two classes), both CERTIFIED_PILOT_WIDTH, the fixed full-width target 1e-6, every reported width recomputed exactly from its
    interval's integer endpoints on the 2^-256 grid, the largest reported width 'about 1.848e-19', zero native oracle calls, first order 7;
    3.87 s external, 68,386,816 bytes external RSS and 119,685,120 bytes sampled tree peak, within 60 s / 384 MiB;
  * omega79: 1742 reused Gauss nodes, 3484 endpoint oracle evaluations, zero new oracle calls, 40-term tails, new exact moments M44/M45,
    omega7 and omega9 CERTIFIED_TARGET with widths (recomputed from the interval endpoints) below 1e-22 and 1e-20; 9.79 s external
    within 30 s / 384 MiB.
Supplementary (the note's stated algebra, exact or to 1e-12): the scalar Euler recurrence n Z_n = sum_j j l_j Z_(n-j) for Z = exp(sum l_j t^j)
(sympy, n <= 10); the coefficient recurrence n A_n = [h0, A_(n-1)] - A_(n-1) V for U(t) = e^{t h0} e^{-t(h0+V)}, the one-defect sector
-ad_(h0)^(n-1)(V)/n! and the vanishing of its projected trace for n >= 2 when [P, h0] = 0 (random finite matrices, n <= 10).
HIT if a stated executed number differs from the retained evidence or a stated identity fails.
"""
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "codex/native-gaussian-moment-jet-20260910"
HEAD = "dee7f1f07698bc36cfffc4e6495168a9107ff956"
PK = ".claude/science/physics-loops/native-gaussian-moment-jet-20260910/source_draft/"


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def show(path):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path}: {r.stderr.strip()}")
    return r.stdout


def main():
    hits, rows_out = [], []

    def check(name, ok, detail):
        rows_out.append(f"[{'ok' if ok else 'MISMATCH'}] {name}: {detail}")
        if not ok:
            hits.append(f"{name}: {detail}")

    note = show("docs/NATIVE_GAUSSIAN_MOMENT_JET_NOTE_2026-09-10.md")
    hr = json.loads(show(PK + "high/RESULT.json"))
    ha = json.loads(show(PK + "high/ROOT_ACCEPTANCE.json"))
    ev = show(PK + "high/EVENTS.ndjson").strip().splitlines()
    proto_high = show(PK + "sources/native-gaussian-high-moment-runtime-design-PROTOCOL.md")
    orr = json.loads(show(PK + "omega/RESULT.json"))
    oa = json.loads(show(PK + "omega/ROOT_ACCEPTANCE.json"))
    omega_review = show(PK + "proofs/native-omega79-root-cold-review-REVIEW.md")
    # ---------------------------------------------------------------- high moments
    check("events", hr["events"] == 189 and len(ev) == 189 and ha["schema"]["events"] == 189,
          f"RESULT {hr['events']}, EVENTS.ndjson {len(ev)} lines, acceptance schema {ha['schema']['events']} (note: 189)")
    check("six files", len(ha["output_hashes"]) == 6, f"{len(ha['output_hashes'])} retained outputs: {', '.join(sorted(ha['output_hashes']))} (note: six)")
    intervals = [(r["kind"], n) for r in hr["rows"] for n in r["moments"]]
    check("eight intervals", len(intervals) == 8 and sorted(r["kind"] for r in hr["rows"]) == ["O", "P"] and all(r["orders"] == [7, 8, 9, 10] for r in hr["rows"]),
          f"{len(intervals)} intervals: classes {sorted(r['kind'] for r in hr['rows'])}, orders {hr['rows'][0]['orders']} (note: eight new P/O intervals, orders 7-10)")
    check("pilot flags", all(r["status"] == "CERTIFIED_PILOT_WIDTH" and r["width_gate"] for r in hr["rows"]), "both rows CERTIFIED_PILOT_WIDTH with width_gate")
    check("pilot target", all(F(r["target_full_width"]) == F(1, 10 ** 6) for r in hr["rows"]), "target_full_width 1/1000000 (note: 10^-6)")
    widths = {}
    exact = True
    for r in hr["rows"]:
        for n, ((lo, hi), (ilo, ihi)) in r["moments"].items():
            w = F(r["widths"][n])
            exact = exact and w == F(int(hi) - int(lo), 2 ** 256) and int(ilo) == int(ihi) == 0
            widths[(r["kind"], int(n))] = w
    check("widths from endpoints", exact, "every reported width equals (hi - lo)/2^256 of its integer-grid interval; imaginary parts exactly 0")
    wmax_key = max(widths, key=widths.get)
    wmax = widths[wmax_key]
    check("largest width", round(float(wmax), 22) == 1.848e-19 or abs(float(wmax) - 1.848e-19) < 5e-23,
          f"largest reported width {float(wmax):.6e} ({wmax_key[0]}, order {wmax_key[1]}) (note: about 1.848e-19); all widths below 1e-6: "
          f"{all(w < F(1, 10 ** 6) for w in widths.values())}")
    check("oracle calls / first order", hr["native_oracle_calls"] == 0 and hr["first_order"] == 7 and hr["native_lower_moments_recomputed"] == 0,
          "native_oracle_calls 0, first_order 7, lower moments not recomputed (note: only orders seven through ten evaluated)")
    lim_ok = "60s external" in proto_high.replace(" ", "") or "60sexternal" in proto_high.replace(" ", "")
    check("high resources", ha["external_seconds"] == 3.87 and ha["external_rss_bytes"] == 68386816 and ha["sampled_whole_tree_peak"] == 119685120
          and ha["external_seconds"] < 60 and ha["sampled_whole_tree_peak"] <= 384 * 2 ** 20 and lim_ok and "384MiB" in proto_high.replace(" ", ""),
          f"external {ha['external_seconds']} s, RSS {ha['external_rss_bytes']:,} B, tree peak {ha['sampled_whole_tree_peak']:,} B; protocol "
          f"60 s / 384 MiB = {384 * 2 ** 20:,} B (note: 3.87 s, 68,386,816 B, 119,685,120 B)")
    # ---------------------------------------------------------------- omega79
    check("omega nodes", orr["nodes"] == 1742 and orr["endpoint_oracles_reused"] == 3484 == 2 * 1742 and orr["oracle_calls"] == 0,
          f"nodes {orr['nodes']}, endpoint oracles reused {orr['endpoint_oracles_reused']}, new oracle calls {orr['oracle_calls']} (note: 1742, 3484, zero)")
    check("omega tails", orr["tail_terms_each"] == 40 and orr["new_moments"] == [44, 45],
          f"tail terms {orr['tail_terms_each']}, new exact moments {orr['new_moments']} (note: 40-term tails, M44/M45)")
    ok_t, det = True, []
    for r in orr["rows"]:
        lo, hi = (F(x) for x in r["interval"])
        w = F(r["width"])
        tgt = F(r["target"])
        want_t = {"omega7": F(1, 10 ** 22), "omega9": F(1, 10 ** 20)}[r["observable"]]
        ok_t = ok_t and r["status"] == "CERTIFIED_TARGET" and w == hi - lo and w <= tgt and tgt == want_t
        det.append(f"{r['observable']}: width {float(w):.3e} = hi - lo, target {float(tgt):.0e}")
    check("omega targets", ok_t, "; ".join(det) + " (note: 1e-22 and 1e-20 met)")
    check("omega resources", oa["external_seconds"] == 9.79 and oa["external_seconds"] < 30 and oa["sampled_whole_tree_peak"] <= 384 * 2 ** 20
          and "30/29.5/29-second" in omega_review.replace(" ", "") and "384MiB" in omega_review.replace(" ", ""),
          f"external {oa['external_seconds']} s, tree peak {oa['sampled_whole_tree_peak']:,} B; the reviewed protocol 30 s / 384 MiB (note: 9.79 s)")
    check("note text", all(s in note for s in ("1742", "3484", "189", "3.87", "68,386,816", "119,685,120", "9.79", "1.848")),
          "the figures checked above are the ones printed in the note")
    # ---------------------------------------------------------------- supplementary identities
    import sympy as sp
    t = sp.symbols("t")
    ls = sp.symbols("l1:11")
    Z = sp.series(sp.exp(sum(l * t ** (j + 1) for j, l in enumerate(ls))), t, 0, 11).removeO()
    Zc = [sp.expand(Z.coeff(t, n)) for n in range(11)]
    euler = all(sp.expand(n * Zc[n] - sum(j * ls[j - 1] * Zc[n - j] for j in range(1, n + 1))) == 0 for n in range(1, 11))
    check("Euler recurrence", euler, "n Z_n = sum_(j=1..n) j l_j Z_(n-j) for Z = exp(sum l_j t^j), n <= 10 (sympy)")
    rng = np.random.default_rng(8082)
    d = 8
    X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    h0 = (X + X.conj().T) / 2
    Y = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    V = (Y + Y.conj().T) / 2
    ev0, U0 = np.linalg.eigh(h0)
    Pn = U0[:, ev0 < 0] @ U0[:, ev0 < 0].conj().T
    A = [np.eye(d, dtype=complex)]
    for n in range(1, 11):
        A.append((h0 @ A[-1] - A[-1] @ h0 - A[-1] @ V) / n)
    from scipy.linalg import expm
    tt = 0.05
    Ut = expm(tt * h0) @ expm(-tt * (h0 + V))
    series = sum(a * tt ** n for n, a in enumerate(A))
    rec_ok = np.abs(Ut - series).max() < 1e-12
    # one-defect sector: the part of A_n linear in V follows the recurrence at linear order, A1_1 = -V, n A1_n = [h0, A1_(n-1)] (the
    # constant A0_m vanishes for m >= 1), and must equal -ad_(h0)^(n-1)(V)/n!
    lin_ok, tr_ok = True, True
    lin_dev = tr_dev = 0.0
    A1 = [None, -V]
    for n in range(2, 11):
        A1.append((h0 @ A1[-1] - A1[-1] @ h0) / n)
    for n in range(1, 11):
        ad = V.copy()
        for _ in range(n - 1):
            ad = h0 @ ad - ad @ h0
        Ln = -ad / math.factorial(n)
        scale = max(1e-300, np.abs(Ln).max())
        lin_dev = max(lin_dev, np.abs(A1[n] - Ln).max() / scale)
        if n >= 2:
            tr_dev = max(tr_dev, abs(np.trace(Pn @ Ln)) / (scale * d))
    lin_ok = lin_dev < 1e-12
    tr_ok = tr_dev < 1e-12
    # and the linear part really is the V-linear part of the full recurrence: 2 A(eps)/eps - A(2eps)/(2eps) = A1 + O(eps^2)
    def An_at(eps, n):
        B = [np.eye(d, dtype=complex)]
        for m in range(1, n + 1):
            B.append((h0 @ B[-1] - B[-1] @ h0 - B[-1] @ (eps * V)) / m)
        return B[n]
    dq_dev = max(np.abs(2 * An_at(1e-4, n) / 1e-4 - An_at(2e-4, n) / 2e-4 - A1[n]).max() / max(1e-300, np.abs(A1[n]).max()) for n in range(1, 8))
    lin_ok = lin_ok and dq_dev < 1e-6
    check("coefficient recurrence", rec_ok and lin_ok and tr_ok,
          f"sum A_n t^n = e^(t h0) e^(-t(h0+V)) to {np.abs(Ut - series).max():.1e} at t = 0.05; the linear-order recurrence gives -ad_(h0)^(n-1)(V)/n! "
          f"to {lin_dev:.1e} (n <= 10) and is the V-linear part of the full recurrence to {dq_dev:.1e} (Richardson difference quotient, n <= 7); "
          f"Tr(P L_n)/(|L_n| d) at most {tr_dev:.1e} for n >= 2 with [P, h0] = 0 (8 x 8 random Hermitian)")
    for line in rows_out:
        print(line)
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (c) EXECUTED NUMBERS - the note's executed figures against the retained evidence at the PR head: 189 events, "
          f"six files, eight P/O intervals (orders 7-10), widths exactly (hi - lo)/2^256 with the largest {float(wmax):.4e} ({wmax_key[0]}, order "
          f"{wmax_key[1]}) and all below the 1e-6 target, 1742 nodes / 3484 endpoint evaluations / zero oracle calls / 40-term tails / M44-M45, "
          f"omega7 and omega9 widths {float(F(orr['rows'][0]['width'])):.2e} and {float(F(orr['rows'][1]['width'])):.2e} under 1e-22 and 1e-20, "
          f"3.87 s / 68,386,816 B / 119,685,120 B within 60 s / 384 MiB and 9.79 s within 30 s / 384 MiB; the Euler and coefficient recurrences "
          f"hold; {len(hits)} mismatches; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
