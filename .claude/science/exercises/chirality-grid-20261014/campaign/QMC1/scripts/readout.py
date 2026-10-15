"""QMC-1 readout: tables over all runs and the FIXED readings (PREREG section 5).

    python3 readout.py            # scans runs/L4_*, runs/L6_*, runs/L1D*_* npz files
"""
import glob, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import summarize

HERE = os.path.dirname(os.path.abspath(__file__))


def table(pattern, title):
    rows = []
    for p in sorted(glob.glob(os.path.join(HERE, pattern))):
        try:
            r = summarize(p, verbose=False)
        except Exception as e:
            print(f"  skip {p}: {e}")
            continue
        rows.append(r)
    rows.sort(key=lambda r: (r["args"]["filt"], tuple(r["args"]["dims"]), r["args"]["W"]))
    print(f"\n### {title}")
    print("| filter | L | W | dtau | n_s | sweeps | acc | S10(Q0) | S10/N | S_{9,10}/S10 | S(Qpi) | W<Q>/N | gap E1 | gap E2 | "
          "w_1 E3 / E3w | G_m(beta/2) | max light dev | max phase | wrap dev | s/sweep |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        a = r["args"]; N = int(np.prod(a["dims"])); nt = len(r["tau"])
        print(f"| {a['filt']} | {'x'.join(map(str, a['dims']))} | {a['W']} | {a['dtau']} | {a['ns']} | {r['n']} | {r['acc']:.2f} | "
              f"{r['S10']:.2f}({r['S10_err']:.2f}) | {r['S10_over_N']:.3f}({r['S10_over_N_err']:.3f}) | "
              f"{(r['SX0'][8:].sum() + r['SY0'][8:].sum()) / r['S10']:.2f} | "
              f"{r['Spi']:.2f}({r['Spi_err']:.2f}) | {r['WQ'] / N:.3f}({r['WQ_err'] / N:.3f}) | "
              f"{r['gap']:.3f}({r['gap_err']:.3f}) | {r['gap2']:.3f}({r['gap2_err']:.3f}) | {r['w1']:.3f}({r['w1_err']:.3f}) / {r['w1w']:.3f}({r['w1w_err']:.3f}) | "
              f"{r['Gm'][nt // 2]:.4f}({r['Gm_err'][nt // 2]:.4f}) | "
              f"{r['light_dev']:.1e} | {r['maxphase']:.1e} | {r['maxdev']:.1e} | {r['sec']:.1f} |")
    return rows


def readings(rows4, rows6, beta=4.0):
    """FIXED readings for f2 between L = 4 and L = 6 with each gap estimator (PREREG section 5 + follow-up D)."""
    thr = max(0.2, 4.0 / beta)
    by4 = {r["args"]["W"]: r for r in rows4 if r["args"]["filt"] == "f2"}
    by6 = {r["args"]["W"]: r for r in rows6 if r["args"]["filt"] == "f2"}
    out = {}
    for est in ("E1", "E2", "E3", "E3w"):
        print(f"\n### Readings (f2, 2+1D, L = 4 vs 6), gap estimator {est}")
        smg_window, gpr_all, open_any = [], True, False
        for W in sorted(set(by4) & set(by6)):
            r4, r6 = by4[W], by6[W]
            if est in ("E3", "E3w"):
                k, ke = ("w1", "w1_err") if est == "E3" else ("w1w", "w1w_err")
                o4 = r4[k] + 2 * r4[ke] < 0.1; o6 = r6[k] + 2 * r6[ke] < 0.1
                stable = abs(r6[k] - r4[k]) <= 2 * np.hypot(r4[ke], r6[ke])
                g4, g6 = f"{k} {r4[k]:.4f}({r4[ke]:.4f})", f"{k} {r6[k]:.4f}({r6[ke]:.4f})"
            else:
                k, ke = ("gap", "gap_err") if est == "E1" else ("gap2", "gap2_err")
                o4 = r4[k] - 2 * r4[ke] > thr; o6 = r6[k] - 2 * r6[ke] > thr
                stable = abs(r6[k] - r4[k]) <= 2 * np.hypot(r4[ke], r6[ke])
                g4, g6 = f"{r4[k]:.3f}({r4[ke]:.3f})", f"{r6[k]:.3f}({r6[ke]:.3f})"
            s4, e4 = r4["S10_over_N"], r4["S10_over_N_err"]
            s6, e6 = r6["S10_over_N"], r6["S10_over_N_err"]
            se = np.hypot(e4, e6)
            dec = s6 < s4 - 2 * se
            flat_or_grow = s6 >= s4 - 2 * se
            R = s6 / s4; Re = R * np.hypot(e4 / s4, e6 / s6)
            print(f"W={W}: L4 {g4} open={o4}; L6 {g6} open={o6}; stable={stable}; S10/L^2 L4 {s4:.4f}({e4:.4f}) "
                  f"L6 {s6:.4f}({e6:.4f}) ratio {R:.3f}({Re:.3f}); decreases={dec}; flat_or_growing={flat_or_grow}")
            if o4 and o6:
                open_any = True
                if stable and dec:
                    smg_window.append(W)
                if not flat_or_grow:
                    gpr_all = False
        rd = "SMG-PILOT" if smg_window else ("GPR-PILOT" if (open_any and gpr_all) else "OPEN")
        print(f"READING ({est}, mechanical): {rd}; SMG window {smg_window}; gap open at some W: {open_any}; "
              f"S10/L^2 flat-or-growing at every open W: {gpr_all}")
        out[est] = rd
    return out


def size_ratios(rowsA, rowsB, filt, title):
    """S10/N and S(Qpi)/N ratios between two sizes at common W (control and 1D comparisons; no fixed reading)."""
    a = {r["args"]["W"]: r for r in rowsA if r["args"]["filt"] == filt}
    b = {r["args"]["W"]: r for r in rowsB if r["args"]["filt"] == filt}
    print(f"\n### {title}")
    for W in sorted(set(a) & set(b)):
        ra, rb = a[W], b[W]
        Na, Nb = int(np.prod(ra["args"]["dims"])), int(np.prod(rb["args"]["dims"]))
        s1, e1, s2, e2 = ra["S10"] / Na, ra["S10_err"] / Na, rb["S10"] / Nb, rb["S10_err"] / Nb
        p1, f1, p2, f2 = ra["Spi"] / Na, ra["Spi_err"] / Na, rb["Spi"] / Nb, rb["Spi_err"] / Nb
        print(f"W={W}: S10/N {s1:.3f}({e1:.3f}) -> {s2:.3f}({e2:.3f}), ratio {s2 / s1:.3f}({s2 / s1 * np.hypot(e1 / s1, e2 / s2):.3f}); "
              f"S(Qpi)/N {p1:.3f}({f1:.3f}) -> {p2:.3f}({f2:.3f}), ratio {p2 / p1:.3f}({p2 / p1 * np.hypot(f1 / p1, f2 / p2):.3f}); "
              f"gap E2 {ra['gap2']:.3f}({ra['gap2_err']:.3f}) -> {rb['gap2']:.3f}({rb['gap2_err']:.3f}); "
              f"E3w {ra['w1w']:.3f}({ra['w1w_err']:.3f}) -> {rb['w1w']:.3f}({rb['w1w_err']:.3f})")


if __name__ == "__main__":
    r4 = table("runs/L4_*.npz", "2+1D L = 4")
    r6 = table("runs/L6_*.npz", "2+1D L = 6")
    r1 = table("runs/L1D*.npz", "1+1D")
    if r4 and r6:
        readings(r4, r6)
        size_ratios(r4, r6, "one", "Control f == 1, 2+1D, L = 4 -> 6 (power reference; no fixed reading)")
        size_ratios(r4, r6, "f2", "f2, 2+1D, L = 4 -> 6 (same data as the readings)")
    if r1:
        r8 = [r for r in r1 if r["args"]["dims"] == [8]]; r16 = [r for r in r1 if r["args"]["dims"] == [16]]
        size_ratios(r8, r16, "f1", "1+1D f1, L = 8 -> 16 (validation / NT-3 comparison; Coleman: no LRO in 1D)")
        size_ratios(r8, r16, "one", "1+1D control, L = 8 -> 16")
