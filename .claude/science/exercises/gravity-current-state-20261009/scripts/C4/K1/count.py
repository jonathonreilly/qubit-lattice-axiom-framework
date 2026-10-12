"""K1 step 3: assemble the one-loop coefficients, project out EH / O(4), TT speed spread, and the tuning count.
Inputs: loop_fermion_m*.json (largest L), loop_photon.json (largest L), photon_q0.json (largest L), forms_data.npz.
Conventions: action density Gamma/V = sum_k cM_k M_k(h) + sum_j c_j K_j(dh,dh)  (K_j with s -> derivative).
Per 4D staggered field = naive/4 (stated proxy); QED content = 1 staggered field + 1 photon.
"""
import numpy as np, json, glob, sys
sys.path.insert(0, '.')
from forms import TTbasis, pairs, sym   # re-runs the (2 s) form enumeration; harmless
fd = np.load("forms_data.npz"); MF = fd["M"]; KF = fd["K"]
names = ["F1", "F2", "F3", "F4", "A1", "A2", "A3", "A4", "A6"]
EH = np.array([1, -2, 2, -1, 0, 0, 0, 0, 0]) / 4.0
# Haar projection onto O(4) span = Frobenius-orthogonal projection onto span(F1..F4) (Frobenius is O(4)-invariant)
# Frobenius must be taken in O(4)-orthonormal h-coordinates w (offdiag weight sqrt2, so |w|^2 = h:h)
Dinv = np.diag([1.0 if m == n else 1 / np.sqrt(2) for (m, n) in pairs])
Kv = np.array([np.einsum('Ai,Bj,ijab->ABab', Dinv, Dinv, K).ravel() for K in KF])
Fo = Kv[:4]
def o4avg(j):
    c, *_ = np.linalg.lstsq(Fo.T, Kv[j], rcond=None); return c
print("O(4) (Haar) averages of the anisotropic forms, in F1..F4:")
for j in range(4, 9):
    print(f"  <{names[j]}> = " + " ".join(f"{x:+.5f}" for x in o4avg(j)))
P_o4 = np.zeros((4, 9)); P_o4[:, :4] = np.eye(4)
for j in range(4, 9):
    P_o4[:, j] = o4avg(j)
# gauge map (cubic in s) on the 9 coefficients, from random samples (as in forms.py)
rng = np.random.default_rng(2)
samples = [(rng.normal(size=10), rng.normal(size=4), rng.normal(size=4)) for _ in range(120)]
def unsym(h): return np.array([h[m, n] for (m, n) in pairs])
Gk = np.array([[np.einsum('A,B,a,b,ABab->', h, unsym(np.outer(s, xi) + np.outer(xi, s)), s, s, KF[j], optimize=True)
                for j in range(9)] for (h, xi, s) in samples])
def analyse(label, cM, cK, tad):
    cM = np.array(cM); cK = np.array(cK)
    Lam = 2 * tad
    cMnet = cM + np.array([Lam / 4, Lam / 4, -Lam / 8])
    o4 = P_o4 @ cK                      # O(4) part (F1..F4 coefficients)
    an = cK[4:]                         # anisotropic part = coefficients of the canonical A-hat forms
    kap = (o4 @ EH[:4]) / (EH[:4] @ EH[:4])
    o4ng = o4 - kap * EH[:4]
    W = Gk @ cK; Wn = np.linalg.norm(W) / (np.linalg.norm(Gk, 2) * np.linalg.norm(cK))
    print(f"\n== {label} ==")
    print(f"  tadpole t = {tad:+.6f};  net masses after CC: " + " ".join(f"{x:+.6f}" for x in cMnet)
          + f"   (TT-visible: M1, M2)")
    print("  kinetic: " + " ".join(f"{n}={c:+.3e}" for n, c in zip(names, cK)))
    print(f"  O(4) part (F1..F4) = {o4};  best EH multiple kappa = {kap:+.4e};  non-EH O(4) residual = {o4ng} "
          f"(|res|/|O(4)| = {np.linalg.norm(o4ng)/np.linalg.norm(o4):.3f})")
    print(f"  anisotropic (A-hat) coefficients = {an};  |aniso|/|O(4) part| = {np.linalg.norm(an)/np.linalg.norm(o4):.3f}")
    print(f"  Ward violation at O(s^3): |G c| / (|G| |c|) = {Wn:.3f}  (0 iff c is EH-shaped)")
    # TT stiffness per polarisation and direction, relative to 1/2 q^2 h:h
    spread = []
    for nlab, n in (("axis", [1, 0, 0, 0]), ("face", [1, 1, 0, 0]), ("body", [1, 1, 1, 1]), ("(2,1,0,0)", [2, 1, 0, 0])):
        n = np.array(n, float); n /= np.linalg.norm(n)
        B = TTbasis(n)
        P2 = 0.5 * sum(cK[j] * np.einsum('ABab,a,b->AB', KF[j], n, n) for j in range(9))
        N2 = 0.5 * np.einsum('ABab,a,b->AB', KF[0], n, n)        # 1/2 q^2 h:h
        ev = np.sort(np.real(np.linalg.eigvals(np.linalg.solve(B @ N2 @ B.T, B @ P2 @ B.T))))
        spread += list(ev)
        print(f"  TT stiffness / (1/2 q^2 h:h), {nlab:9s}: " + " ".join(f"{x:+.4e}" for x in ev))
    spread = np.array(spread)
    print(f"  TT stiffness range over directions/polarisations: [{spread.min():+.4e}, {spread.max():+.4e}]; "
          f"max/min = {spread.max()/spread.min():.2f}")
    return dict(cMnet=cMnet.tolist(), cK=cK.tolist(), o4=o4.tolist(), an=an.tolist(), kap=kap, TTmin=spread.min(), TTmax=spread.max())
res = {}
for f in sorted(glob.glob("loop_fermion_m*.json")):
    d = json.load(open(f)); Ls = sorted(int(k) for k in d if k.isdigit()); L = str(Ls[-1])
    m = f.split("_m")[1][:-5]
    r = d[L]
    res["f" + m] = analyse(f"fermion, one 4D staggered field (naive/4), m={m}, L={L}",
                           np.array(r["cM"]) / 4, np.array(r["cK"]) / 4, r["tad"] / 4)
    if len(Ls) > 1:
        r0 = d[str(Ls[-2])]
        print(f"  L-convergence (L={Ls[-2]} -> {L}) max |dc_K|/max|c_K| = "
              f"{np.abs(np.array(r['cK']) - np.array(r0['cK'])).max() / np.abs(r['cK']).max():.1e}")
try:
    dp = json.load(open("loop_photon.json")); Lp = sorted(int(k) for k in dp)
    rp = dp[str(Lp[-1])]
    res["photon"] = analyse(f"photon (noncompact U(1), corner metric), L={Lp[-1]}", rp["cM"], rp["cK"], 0.0)
    c = dict(zip(names, rp["cK"])); cm = rp["cM"]
    w1 = c["F1"] + 0.5 * c["F3"] + 4 * c["F4"] + 0.5 * c["A3"] + c["A6"]
    w2 = c["F2"] + 2 * c["F3"] + c["A4"] + c["A1"] + c["A2"] + 2 * c["A3"] - c["A6"]
    print(f"  Weyl identity (trace h on sites; photon only): q^2 tr h coeff = {w1:+.2e}, sum q_mu^2 h_mumu coeff = {w2:+.2e}"
          f" (scale {max(abs(x) for x in rp['cK']):.1e}); mass: cM1 + 4 cM3 = {cm[0] + 4*cm[2]:+.1e}")
    if len(Lp) > 1:
        r0 = dp[str(Lp[-2])]
        print(f"  L-convergence (L={Lp[-2]} -> {Lp[-1]}) max |dc_K|/max|c_K| = "
              f"{np.abs(np.array(rp['cK']) - np.array(r0['cK'])).max() / np.abs(rp['cK']).max():.1e}")
    for k in [k for k in res if k.startswith("f")]:
        d = json.load(open(f"loop_fermion_m{k[1:]}.json")); L = str(max(int(x) for x in d if x.isdigit())); r = d[L]
        res["QED" + k[1:]] = analyse(f"QED content: 1 staggered field (m={k[1:]}) + 1 photon",
                                     np.array(r["cM"]) / 4 + np.array(rp["cM"]), np.array(r["cK"]) / 4 + np.array(rp["cK"]), r["tad"] / 4)
except FileNotFoundError:
    print("no photon loop file yet")
# tree EH normalisation (reading): K7a's Q times Mbar^2/2 = 1/(16 pi) in lattice units if a = 1/M_Pl
tree = 1 / (16 * np.pi)
print(f"\nTree EH (reading, a = 1/M_Pl): action (Mbar^2/2) Q, Mbar^2/2 = {tree:.4f}; Q = EH-vector, c_F1 = Mbar^2/8;"
      f" TT stiffness / (1/2 q^2 h:h) = {tree/4:.4e}")
json.dump(res, open("count.json", "w"), indent=1, default=float)
