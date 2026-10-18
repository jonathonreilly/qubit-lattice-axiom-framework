#!/usr/bin/env python3
"""R3 test 1: (a) how much an irrelevant flavour-splitting anomalous dimension can
accumulate over an RG window; (b) data-side numbers each RG mechanism would have to fix.

Comparator masses: same recalled XZZ / MIX sets as HIER-2 fit_control.py (no fetch).
"""
import numpy as np

SETS = {
    'MZ':  dict(u=1.27e-3, c=0.619, t=171.7, d=2.90e-3, s=0.055, b=2.89,
                e=0.48657e-3, mu=0.102718, tau=1.74624),
    'GUT': dict(u=0.48e-3, c=0.235, t=74.0, d=1.14e-3, s=0.022, b=1.00,
                e=0.469652e-3, mu=0.0991466, tau=1.68558),
    'MIX': dict(u=2.16e-3, c=1.27, t=172.69, d=4.67e-3, s=0.0934, b=4.18,
                e=0.511e-3, mu=0.1057, tau=1.777),
}
SECT = {'up': ('u', 'c', 't'), 'down': ('d', 's', 'b'), 'lep': ('e', 'mu', 'tau')}
VUS, VCB, VUB = 0.2250, 0.0418, 0.00369          # recalled magnitudes (comparator)
MPL, V = 1.22e19, 246.22
L = np.log(MPL / V)                               # window length IF v were fixed (it is not: HIER-1)
ALPHA_LM = 0.0907                                 # main's plaquette-surface coupling (conditional on g_bare = 1)

print(f"L = ln(M_Pl/v) = {L:.3f}  (comparator only; v is not framework-fixed)")

# ---------------- (a) accumulation bound -----------------
print("\n(a) Irrelevant splitting: Delta_gamma(mu) = c (mu/Lambda)^y, integrated from Lambda down to Lambda e^{-L}")
print("    accumulated ln ratio A(c,y,L) = (c/y)(1 - e^{-yL});  sup over L = c/y")
need = {}
for nm, m in SETS.items():
    for s, (a1, a2, a3) in SECT.items():
        need[(nm, s)] = np.log(m[a3] / m[a1])
print("    needed ln(m3/m1):", {k: round(v, 2) for k, v in need.items() if k[0] == 'MZ'})
for c in (0.1, 0.3, 1.0):
    row = []
    for y in (2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.0):
        A = c * L if y == 0 else (c / y) * (1 - np.exp(-y * L))
        row.append(f"y={y:<4}: {A:6.2f}")
    print(f"    c={c:<4}", " | ".join(row))
nmax = max(v for k, v in need.items() if k[0] == 'MZ')
print(f"    largest needed (MZ set) = {nmax:.2f};  y_max(c) = c/needed: c=1 -> {1/nmax:.4f}, c=0.3 -> {0.3/nmax:.4f}")
# numerical check of the closed form by direct quadrature
for c, y in ((1.0, 2.0), (0.3, 0.5), (1.0, 0.1)):
    t = np.linspace(0, L, 200001)
    q = np.trapezoid(c * np.exp(-y * t), t)
    print(f"    quadrature check c={c}, y={y}: {q:.6f} vs closed form {(c/y)*(1-np.exp(-y*L)):.6f}")

# historic intake (MASS_HIERARCHY_HONEST_ASSESSMENT) number, re-evaluated as written
dg, Lh = 0.173, 39.0
print(f"\n    historic formula 3*exp(dg*L)*L with dg={dg}, L={Lh}: {3*np.exp(dg*Lh)*Lh:.3e} (note says ~12,000)")
print(f"    the same dg as an irrelevant y=2 (staggered) or y=1 (Wilson) splitting: exp(dg/y) = {np.exp(dg/2):.3f}, {np.exp(dg/1):.3f}")

# ---------------- (b) data-side numbers -----------------
print("\n(b) What an exponent mechanism with FREE window L can predict: only L-independent log ratios")
for nm, m in SETS.items():
    out = []
    for s, (a1, a2, a3) in SECT.items():
        l31 = np.log(m[a3] / m[a1]); l32 = np.log(m[a3] / m[a2])
        out.append(f"{s}: R={l31/l32:.3f} (ln m3/m2={l32:.2f}, ln m3/m1={l31:.2f}; dgam per unit L: {l32/L:.3f}, {l31/L:.3f})")
    print(f"  {nm}: " + "; ".join(out))
print(f"  CKM left-doublet spacing ratio ln(1/Vus)/ln(1/Vcb) = {np.log(1/VUS)/np.log(1/VCB):.3f}  (equal spacing would be 1)")
print(f"  partial-compositeness / FN structural relation Vub ~ Vus*Vcb: {VUS*VCB:.5f} vs {VUB} (ratio {VUS*VCB/VUB:.2f})")

print("\n(c) Radiative ladder with one loop factor per step")
for nm, m in SETS.items():
    st = {}
    for s, (a1, a2, a3) in SECT.items():
        st[s] = (m[a2] / m[a3], m[a1] / m[a2], m[a1] / m[a3])
    print(f"  {nm}: steps m2/m3, m1/m2, m1/m3:",
          {k: tuple(f"{x:.2e}" for x in v) for k, v in st.items()})
    # u/d blindness of QCD loops: a common ladder must fit up and down within x3 each => ratio <= 9
    r21 = st['down'][0] / st['up'][0]; r11 = st['down'][2] / st['up'][2]; r12 = st['down'][1] / st['up'][1]
    print(f"     down/up step ratios: (m2/m3) {r21:.1f}, (m1/m2) {r12:.1f}, (m1/m3) {r11:.1f}   [x3 each side allows <= 9]")
print(f"  framework loop factors: alpha_LM/4pi = {ALPHA_LM/(4*np.pi):.3e}, alpha_LM/pi = {ALPHA_LM/np.pi:.3e}, (alpha_LM/4pi)^2 = {(ALPHA_LM/(4*np.pi))**2:.2e}")
print("  sector ordering of steepness ln(m3/m2): " +
      ", ".join(f"{nm}: " + " > ".join(sorted(SECT, key=lambda s: -np.log(SETS[nm][SECT[s][2]]/SETS[nm][SECT[s][1]]))) for nm in SETS))
print("  sector ordering of steepness ln(m2/m1): " +
      ", ".join(f"{nm}: " + " > ".join(sorted(SECT, key=lambda s: -np.log(SETS[nm][SECT[s][1]]/SETS[nm][SECT[s][0]]))) for nm in SETS))
