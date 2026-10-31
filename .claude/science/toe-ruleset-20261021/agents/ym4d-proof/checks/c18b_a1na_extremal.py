#!/usr/bin/env python3
"""Check c18b (session 6, POST HOC, added after c18's first run showed that c18's fields sit far from the extremal ratio):
near-extremal test of Lemma A1-NA(1). Background: one flux quantum of constant abelian (tau_3) field strength in the (0,1)
plane of the 6^4 fine torus (the A1 extremal mode, cf. E8*-ob), times a smooth non-abelian perturbation exp(t H).
Reports R(t) = S_c/S_f and (R(t) - R(0))/t. Criterion (pre-stated here, post hoc relative to c18): |R(t) - R(0)| <= C t
with the fitted C finite and R(t) - R(0) -> 0 as t -> 0. Finite instance only.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
import runpy, sys, numpy as np, time
T0 = time.time()
sys.argv = ["c18"]; G = {}
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "c18_a1na_onestep.py")).read()
src = src[:src.index("TS = (")]          # reuse geometry, coarse(), plaq_action(), field(); skip c18's own run
exec(compile(src, "c18_a1na_onestep.py", "exec"), G)
d, S, Tc, su2_exp, coarse, plaq_action, field = G["d"], G["S"], G["Tc"], G["su2_exp"], G["coarse"], G["plaq_action"], G["field"]
F = 2 * np.pi / S ** 2 * 2          # tau_3/2 generator: angle 2*pi/S^2 per plaquette after the 1/2
a = np.zeros((d,) + (S,) * d + (3,)); x = np.indices((S,) * d)
a[0][..., 2] = -F * x[1]                                  # A_0(x) = -F x_1
a[1][..., 2] = np.where(x[1] == S - 1, F * S * x[0], 0.0)  # twist closes the flux on the torus
Ub = su2_exp(a); Sf0, ph0 = plaq_action(Ub, S); print(f"background: S_f={Sf0:.6f} max plaquette angle/2={ph0:.4f}")
H = field("smooth-nonabelian", 5); NP = NF = 0; rows = []
for t in (0.0, 0.005, 0.01, 0.02, 0.04):
    U = np.einsum("...ij,...jk->...ik", Ub, su2_exp(t * H)); Sf, ph = plaq_action(U, S); Sc, _ = plaq_action(coarse(U), Tc)
    rows.append((t, Sc / Sf)); print(f"t={t:g} R={Sc / Sf:.6f}")
R0 = rows[0][1]; Cs = [abs(R - R0) / t for t, R in rows[1:]]
print("(R(t)-R(0))/t: " + " ".join(f"{c:.4f}" for c in Cs))
ok = max(Cs) < 10 and abs(rows[1][1] - R0) < abs(rows[-1][1] - R0) + 1e-12
print(("PASS" if ok else "FAIL") + f" c18b: |R(t)-R(0)| <= C t with C={max(Cs):.3f}, R(0)={R0:.6f}")
print(f"runtime {time.time() - T0:.1f} s\nTOTAL: PASS={int(ok)} FAIL={int(not ok)}")
