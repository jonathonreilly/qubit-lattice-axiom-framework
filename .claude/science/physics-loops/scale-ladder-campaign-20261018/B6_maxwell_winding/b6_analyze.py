#!/usr/bin/env python3
"""B6 analysis of b6_exact_ed_results.json: P2 (K_T at the smallest momenta vs chi_L) and
P3 (winding-sector gaps with the Gaussian-comparator Coulomb/confined diagnostics).
Comparator (supplied, noncompact Gaussian, not the ring model): uniform flux W through a section of
area A_a (links) along an axis of length L_a costs dE = U W^2 L_a / (2 A_a), so
U_W := 2 A_a dE / (L_a W^2) is size- and W-independent; a string-tension (confined) reading
has dE ~ sigma |W| L_a (A_a-independent, linear in W).  Exploratory; no claim.
"""
import json, os, sys
import numpy as np

D = os.path.dirname(os.path.abspath(__file__))
R = json.load(open(os.path.join(D, "b6_exact_ed_results.json")))
RES = []


def check(label, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


sizes = [k for k in ("2x2x2", "2x2x3", "2x2x4") if k in R]
Vs = list(R[sizes[0]]["V"].keys())


def KT(rec, qpi):
    for b in rec["blocks"]:
        if np.allclose(b["q_over_pi"], qpi, atol=1e-5):
            return max(b["ev"])
    return None


print("== P2: co-exact source stiffness K_T(q) vs uniform (harmonic) chi_L, same field component ==")
print("   B_z (xy plaquettes): chi_z = chi(o=0) vs K_T(0,0,2pi/Lz);  B_x (yz plaquettes): chi_x = chi(o=1) vs K_T(pi,0,0)")
print(f"{'torus':6} {'V':>5} {'chi_z':>9} {'K_T(0,0,2pi/Lz)':>16} {'ratio':>7} {'K_T(0,0,pi)':>12} | {'chi_x':>9} {'K_T(pi,0,0)':>12} {'ratio':>7} | {'K_T(pi,pi,pi)':>13} {'gap':>8}")
for s in sizes:
    Lz = int(s.split("x")[2])
    for V in Vs:
        r = R[s]["V"][V]
        cz, cx = r["chi_orient"][0], r["chi_orient"][1]
        kz = KT(r, [0, 0, 2 / Lz])
        kzpi = KT(r, [0, 0, 1.0]) if Lz % 2 == 0 else float("nan")
        kx = KT(r, [1.0, 0, 0])
        kq = KT(r, [1.0, 1.0, 1.0]) if Lz % 2 == 0 else KT(r, [1.0, 1.0, 2 / Lz * (Lz // 2)])
        print(f"{s:6} {float(V):+5.2f} {cz:9.6f} {kz:16.6f} {kz / cz:7.4f} {kzpi:12.6f} | {cx:9.6f} {kx:12.6f} {kx / cx:7.4f} | {kq:13.6f} {r['gap']:8.5f}")

print("\n== P3: winding-sector gaps dE(W) = E_min(sector) - E(0), min over all flip components ==")
for s in sizes:
    Lx, Ly, Lz = map(int, s.split("x"))
    sec = R[s]["sectors"]
    for a, (La, A) in ((0, (Lx, Ly * Lz)), (2, (Lz, Lx * Ly))):
        Ws = sorted(int(k.strip("()").split(",")[a]) for k in sec if all(int(x) == 0 for i, x in enumerate(k.strip("()").split(",")) if i != a))
        Ws = [w for w in Ws if w > 0]
        for V in Vs:
            if float(V) == 1.0:
                continue
            E0 = sec["(0, 0, 0)"]["E"][V]
            row = []
            for W in Ws:
                key = str(tuple(W if i == a else 0 for i in range(3)))
                dE = sec[key]["E"][V] - E0
                row.append((W, dE, 2 * A * dE / (La * W * W)))
            print(f"{s:6} flux axis {'xyz'[a]} (L_a={La}, A={A}) V={float(V):+.2f}: "
                  + "  ".join(f"W={W}: dE={dE:.5f} U_W={u:.4f}" for W, dE, u in row)
                  + (f"   dE(4)/dE(2)={row[1][1] / row[0][1]:.3f} [Coulomb 4, string 2]" if len(row) > 1 else ""))

print("\n== Size dependence of the W=2 x-flux (L_x = 2 fixed, A_x = 2 Lz grows): Coulomb dE ~ 1/Lz (U_W const), string dE ~ const (U_W ~ Lz) ==")
for V in Vs:
    if float(V) == 1.0:
        continue
    out = []
    for s in sizes:
        Lx, Ly, Lz = map(int, s.split("x"))
        sec = R[s]["sectors"]
        dE = sec["(2, 0, 0)"]["E"][V] - sec["(0, 0, 0)"]["E"][V]
        out.append((Lz, dE, 2 * Ly * Lz * dE / (Lx * 4)))
    lz = np.log([o[0] for o in out]); le = np.log([o[1] for o in out])
    slope = np.polyfit(lz, le, 1)[0]
    print(f"V={float(V):+.2f}: " + "  ".join(f"Lz={a}: dE={b:.5f} U_W={c:.4f}" for a, b, c in out)
          + f"   d ln dE / d ln Lz = {slope:+.3f} [Coulomb -1, string 0]")

print("\n== Cubic comparison (V=0): exact L=2 here; 4^3, 6^3, 8^3 are the LANDED projector-MC values (W=2, q=1) ==")
sec = R["2x2x2"]["sectors"]
u2 = (sec["(2, 0, 0)"]["E"]["0.0"] - sec["(0, 0, 0)"]["E"]["0.0"]) * 2 / 2
print(f"L=2 exact U_W = L dE/2 = {u2:.4f};  landed MC: 4^3 1.463(17), 6^3 1.110(59), 8^3 0.674(177)")

# internal consistency
for s in sizes:
    for V in Vs:
        r = R[s]["V"][V]
        sec = R[s]["sectors"]
        if float(V) < 1:
            check(f"{s} V={V}: vacuum component energy equals the W=0 sector minimum", abs(r["E0"] - sec["(0, 0, 0)"]["E"][V]) < 1e-8)
check("2x2x2: chi_x = chi_z (cubic symmetry) at every V", all(abs(R["2x2x2"]["V"][V]["chi_orient"][0] - R["2x2x2"]["V"][V]["chi_orient"][1]) < 1e-9 for V in Vs))
for s in sizes[1:]:
    check(f"{s}: chi_x = chi_y (x<->y symmetry) at every V", all(abs(R[s]["V"][V]["chi_orient"][1] - R[s]["V"][V]["chi_orient"][2]) < 1e-9 for V in Vs))
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES) - sum(RES)}")
sys.exit(0 if all(RES) else 1)
