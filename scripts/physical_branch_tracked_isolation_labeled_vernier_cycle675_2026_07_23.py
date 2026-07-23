#!/usr/bin/env python3
"""Cycle 675: branch-tracked theta_2 isolation and amplitude-labeled vernier.

Completion rows for the Cycle-662 block (contract Addendum A, frozen before
output): (1) the physical second A2 line at +0.31368 is evaluated on the
branch-informed narrow window with an order-stability criterion, yielding
either an isolated-zero certificate or an honest width-proxy reading; (2) the
vernier reconstruction is rerun with amplitude-labeled line pairing, repairing
the two sorted-pair degeneracy failures without touching the gold row.

Authority: none.  Audit: unset.  Firewalls: a width proxy is a finite-order
quadrature reading, not a decay rate or energy; joint max 674 observed,
claiming Cycle 675; stacked on the open Cycle-662 block branch.
"""
from __future__ import annotations
import importlib.util, json, math, sys, time
from hashlib import sha256
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
CONTRACT_SHA = "174ce1cae3edce3f888f1ecb10e6d258d9ffd23c620aea5f92d6524c74e1bf32"
RECEIPT = ROOT / "outputs/physical_branch_tracked_isolation_labeled_vernier_cycle675_receipt_2026_07_23.json"
PASS = 0; FAIL = 0

def check(label, condition, detail=""):
    global PASS, FAIL
    if condition: PASS += 1; print("PASS", label, "::", detail)
    else: FAIL += 1; print("FAIL", label, "::", detail)

def load(name):
    p = ROOT / "scripts" / (name + ".py"); d = sha256(p.read_bytes()).hexdigest()
    s = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(s)
    sys.modules[name] = m; s.loader.exec_module(m); return m, d

C662, C662_SHA = load("physical_infinite_volume_a2_two_line_vernier_tournament_cycle662_2026_07_23")
C610 = C662.C610; C611 = C662.C611; C622 = C662.C622

def main():
    start = time.time()
    receipt = {"cycle": 675, "authority": "none", "audit": "unset",
               "contract_sha256": CONTRACT_SHA, "consumed_cycle662": C662_SHA}
    # --- Row 1: branch-tracked isolation / width proxy.
    window = (0.310, 0.318)
    rows = {}
    for order in (32, 40):
        thetas = np.linspace(window[0], window[1], 33)
        vals = [abs(C662.a2_scalar_infinite(float(t), C662.BETA, order)) for t in thetas]
        i = int(np.argmin(vals)); lo, hi = float(thetas[max(0,i-1)]), float(thetas[min(32,i+1)])
        for _ in range(50):
            th = (hi-lo)/3; a, b = lo+th, hi-th
            if abs(C662.a2_scalar_infinite(a, C662.BETA, order)) < abs(C662.a2_scalar_infinite(b, C662.BETA, order)): hi = b
            else: lo = a
        t0 = 0.5*(lo+hi)
        rows[order] = {"theta": t0, "abs_b": float(abs(C662.a2_scalar_infinite(t0, C662.BETA, order)))}
    stable = abs(rows[32]["theta"] - rows[40]["theta"]) < 1e-3
    theta_star = rows[40]["theta"]; min_b = rows[40]["abs_b"]
    if min_b < 1e-6:
        eps = 1e-5
        deriv = abs((C662.a2_scalar_infinite(theta_star+eps, C662.BETA, 40)
                     - C662.a2_scalar_infinite(theta_star-eps, C662.BETA, 40))/(2*eps))
        reading = {"kind": "isolated_zero", "transversality": float(deriv)}
        ok = stable and deriv > 1e-3
    else:
        reading = {"kind": "width_proxy_embedded_resonance", "min_abs_b": min_b}
        ok = stable
    receipt["branch_tracked"] = {"orders": rows, "order_stable": bool(stable),
                                 "theta_star": theta_star, "reading": reading,
                                 "plateau_reference": 0.31368}
    check("branch-tracked theta_2 on the narrow window is order-stable and near "
          "the finite-L plateau, with the frozen either-outcome reading",
          ok and abs(theta_star - 0.31368) < 2e-3, receipt["branch_tracked"])
    # --- Row 2: amplitude-labeled vernier (all six rows + unchanged gold).
    engine = C611.PositionEngine(C611.L_TRAIN, C662.BETA)
    keep = C622.chebyshev_radii(engine.length) <= 2
    state = engine.source()
    for _ in range(256): state = engine.step(state, C662.CONTACT) * keep[..., None]
    word = C622.channel_word(engine, state, -1, C662.CONTACT)
    theta_b = -2.975574708447
    seg0 = word[64:]; sp0 = np.fft.fft(seg0)
    fr0 = 2*math.pi*np.fft.fftfreq(len(seg0)); mg0 = np.abs(sp0)
    o0 = np.argsort(mg0)[::-1]
    ref = {"b": C662.peak_position(mg0, fr0, int(o0[0])),
           "2": C662.peak_position(mg0, fr0, int(o0[1]))}
    q = np.arange(len(word)); results = []; all_ok = True
    for alpha_true in C662.ALPHA_ROWS:
        seg = (word * np.exp(1j*alpha_true*q))[64:]
        sp = np.fft.fft(seg); fr = 2*math.pi*np.fft.fftfreq(len(seg))
        mg = np.abs(sp); o = np.argsort(mg)[::-1]
        i1 = int(o[0])
        n = len(mg)
        i2 = next(int(k) for k in o[1:]
                  if min(abs(int(k)-i1), n-abs(int(k)-i1)) > C662.BAND_HALFWIDTH)
        m_b = C662.peak_position(mg, fr, i1)
        m_2 = C662.peak_position(mg, fr, i2)
        def mism(al):
            return (C610.wrap_angle(m_b - C610.wrap_angle(ref["b"]+al))**2
                    + C610.wrap_angle(m_2 - C610.wrap_angle(ref["2"]+al))**2)
        grid = np.arange(0.0, 2*math.pi, 1e-4); coarse = min(grid, key=mism)
        lo, hi = coarse-2e-4, coarse+2e-4
        for _ in range(40):
            th = (hi-lo)/3; a, b = lo+th, hi-th
            if mism(a) < mism(b): hi = b
            else: lo = a
        al = 0.5*(lo+hi); err = abs(C610.wrap_angle(al - alpha_true))
        row = {"alpha_true": alpha_true, "alpha_rec": float(al), "err": float(err),
               "ok": bool(err < 2*(2*math.pi/1984))}
        if abs(alpha_true + 0.7439) < 1e-9:
            r = (theta_b + C610.wrap_angle(al)) / theta_b
            row["R_rec"] = float(r); row["a_count"] = int(math.copysign(math.floor(4*abs(r)+0.5), r))
        results.append(row); all_ok = all_ok and row["ok"]
    receipt["labeled_vernier"] = results
    gold = next(r for r in results if "R_rec" in r)
    check("amplitude-labeled pairing reconstructs all six frozen rows within two "
          "bins (repairing the sorted-pair degeneracy) with the gold row unchanged",
          all_ok and abs(gold["R_rec"] - 1.25) < 1e-3 and gold["a_count"] == 5,
          {"errors": [round(r["err"], 6) for r in results],
           "gold": {k: gold[k] for k in ("R_rec", "a_count")}})
    receipt["elapsed_seconds"] = time.time() - start
    receipt["pass_count"] = PASS; receipt["fail_count"] = FAIL; receipt["pass"] = FAIL == 0
    RECEIPT.write_text(json.dumps(receipt, indent=1, default=float) + "\n")
    print("RESULT", PASS, FAIL, "elapsed", round(time.time()-start, 2), "s")
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
