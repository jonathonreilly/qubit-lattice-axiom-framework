"""
Check E: paired estimator.  Since <G_liquid> = 0 exactly (lemma), G_glass = < d^2/deps^2 [E_glass - E_liquid] >,
which uses the SAME points and strain and so cancels the sample-to-sample noise.
  (a) 2D, cotan (= P1 = circumcentric in 2D): calibration, expect about +1.97 per site (check B).
  (b) 3D circumcentric DEC (Voronoi-dual): the open case from check D.
  (c) 3D jittered cubic crystal, circumcentric DEC re-triangulated (= Voronoi of strained crystal).
Also counts edges of the frozen complex that are no longer Delaunay (negative circumcentric weight).
PRE-STATED: (b) glass 'stiff' iff |G_diff| > 5 SE; 'soft within resolution' otherwise (report bound).
            (c) crystal stiff iff |G| > 5 SE.
"""
import numpy as np, sys
from itertools import product
exec(open("D_3d_circumcentric.py").read().split("if sys.argv[1:]")[0])
stiffness = ns["stiffness"]

rng = np.random.default_rng(4242)
epss = np.array([-0.06, -0.04, -0.02, 0.0, 0.02, 0.04, 0.06])
S3 = np.zeros((3, 3)); S3[0, 1] = S3[1, 0] = 1.0

def paired(d, N, R, chans, op):
    L = N ** (1 / d); A0 = L * np.eye(d); out = {c: [] for c in chans}; neg = {c: [] for c in chans}
    for r in range(R):
        X = rng.uniform(0, L, size=(N, d)); vid0, voff0 = periodic_delaunay(X, A0)
        for c, S in chans.items():
            D = []
            for e in epss:
                M = expm_sym(S, e); Y, A = X @ M.T, A0 @ M.T
                v, o = periodic_delaunay(Y, A)
                if op == "dec":
                    Kg, Wg = dec_laplacian(Y, A, vid0, voff0); Kl, _ = dec_laplacian(Y, A, v, o)
                    if e == epss[-1]: neg[c].append(int((Wg < -1e-12).sum() // 2))
                else:
                    Kg = stiffness(Y, A, vid0, voff0); Kl = stiffness(Y, A, v, o)
                D.append((E_vac(Kg)[0] - E_vac(Kl)[0]) / N)
            out[c].append(2 * np.polyfit(epss, D, 4)[-3])
    for c in chans:
        a = np.array(out[c]); print(f"  {c:4s} G_glass - G_liquid = {a.mean():+.4f} +- {a.std(ddof=1)/np.sqrt(len(a)):.4f}  (n={len(a)})"
                                    + (f"  non-Delaunay edges at eps=0.06: {np.mean(neg[c]):.0f} of ~{7*N}" if neg[c] else ""))

which = sys.argv[1]
if which == "a":
    print("(a) 2D cotan, N=1000"); paired(2, 1000, 8, {"Eg": np.diag([1.0, -1.0]), "T2g": np.array([[0, 1.0], [1.0, 0]])}, "p1")
elif which == "b":
    print("(b) 3D circumcentric DEC, N=1000"); paired(3, 1000, 30, {"Eg": np.diag([1.0, -1.0, 0.0]), "T2g": S3}, "dec")
elif which == "c":
    print("(c) 3D jittered cubic crystal 10^3, circumcentric DEC, re-triangulated")
    m = 10; g1 = np.arange(m) + 0.5; A0 = m * np.eye(3)
    for c, S in {"Eg": np.diag([1.0, -1.0, 0.0]), "T2g": S3}.items():
        Gs = []
        for r in range(3):
            X = np.array(list(product(g1, repeat=3)), float) + 1e-3 * rng.standard_normal((m ** 3, 3))
            El = []
            for e in epss:
                M = expm_sym(S, e); Y, A = X @ M.T, A0 @ M.T
                v, o = periodic_delaunay(Y, A); El.append(E_vac(dec_laplacian(Y, A, v, o)[0])[0] / len(X))
            Gs.append(2 * np.polyfit(epss, El, 4)[-3]); print(f"   {c} sample {r}: E(eps) = {np.round(El, 5)}")
        Gs = np.array(Gs); print(f"  {c:4s} crystal G = {Gs.mean():+.4f} +- {Gs.std(ddof=1)/np.sqrt(len(Gs)):.4f}  e0={El[3]:.4f}")
