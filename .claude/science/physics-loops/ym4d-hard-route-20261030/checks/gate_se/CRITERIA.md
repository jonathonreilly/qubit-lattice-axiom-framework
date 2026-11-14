# gate_se: registered before the run

Question. The note's two-site and tensor tests use one flat rank-one constraint.
This test uses the true flat four-dimensional object: the orthogonal projector P
of curvature space onto minimal lifts over the composite path-average parent
(symbol of mapped Text 3.1), with Bianchi and gauge included, depth by block side
B = L^n. rho(nu) := ||W^{1/2} P W^{-1/2}||^2 is the worst trial ratio in (WAM) at
linear order over ALL trials, closed or not, so it bounds the ratio for closed ones.

Prediction from the gate's hand proof: rho - 1 <= C nu^2, C free of B and M.

Identity checks (must pass, else no result is reported):
 I1 P^2 = P and P symmetric, relative error < 1e-9 (double), 1e-4 (single).
 I2 Real-space, no symbols: for random A, G := A - A_* has zero coarse curl of Q G.
 I3 ||P dA|| <= ||dA||.

Kill criteria, with D2 := (rho - 1)/nu^2 at fixed profile and nu:
 K1 D2(B=9) > 1.5 D2(B=3) at the same M: growth with depth at L = 3.
 K2 D2(B=25) > 1.5 D2(B=5) at the same M: growth with depth at L = 5.
 K3 D2(M=6) > 1.5 D2(M=4) at B = 3: growth with volume.
 Any of these refutes the hand prediction in the model and sends the gate back
 to the proof.

Control that must fire: a global rank-one flat constraint on the same weights
must show rho growing with M, by Kantorovich. If it does not, the weights are
too weak to show anything.

Exploratory, no criterion: a piecewise-constant weight with jumps at top-block
faces, as for compatible descendants.

A pass is a linear flat statement about a few lattices. It proves nothing and
is not consumed by anything. Nonlinear (WAM) is untouched by it.

# Added after the first grid. POST HOC: written after K3 fired.

Result of the registered grid: K1 and K2 pass so far. **K3 FIRED**: at B = 3,
D2(M=6)/D2(M=4) = 2.07 (radial), 1.75 (zig), and D2 keeps growing to M = 8. So the
registered quantity rho grows with volume, as about M^2 nu^2, and the registered
statement "rho bounds the ratio, prediction rho - 1 <= C nu^2 free of M" is
FALSE for rho. That stands as a failure of what was registered.

Diagnosis, to be tested, not assumed: rho is a sup over ALL 2-forms. (WAM) only
ever sees closed trials F_t = dA_t. On non-closed forms P contains the Hodge
projector's power-law tail, so its first moment grows with M, and the sup is not
the (WAM) ratio. The hand proof uses closure of the trial.

New quantity: rho_c(nu) := sup over F in Ran d of ||P F||_w^2 / ||F||_w^2, by
generalized Lanczos with an inner CG on Pi W Pi. This is the actual linear (WAM)
worst ratio.

Criteria for rho_c, D2c := (rho_c - 1)/nu^2:
 K1c D2c(B=9) > 1.5 D2c(B=3) at the same M.
 K2c D2c(B=25) > 1.5 D2c(B=5) at the same M, if B=25 is feasible.
 K3c D2c(M=8) > 1.5 D2c(M=4) at B = 3.
 Control: at w = 1 rho_c = 1 to 1e-8 (double).
Any of these firing refutes the hand proof in the model, or finds an error in it.

# Added during the closed grid. POST HOC, second step: written after K3c fired.

Result so far: **K3c FIRED on zig**: D2c(M=8)/D2c(M=4) = 0.2301/0.1441 = 1.60 at nu = 0.1,
B = 3. Radial: 1.48, under the bar. This stands as registered. Sequence, zig:
0.074, 0.144, 0.196, 0.230 at M = 2, 4, 6, 8; radial: 0.146, 0.408, 0.538, 0.602.
Both fit D_oo - c/M, and zig is also roughly a log M. Log growth would
contradict the hand proof, whose constant is free of M. A torus of side M <= 12
cannot separate these, and 1.5 between M = 4 and 8 was an arbitrary bar: it does
not distinguish saturation from growth.

Decisive quantity, with no torus. For wide envelopes the second-order ratio is
1 + nu^2 ||Pi_H (l g)||^2 / ||g||^2, with H := Ran d minus Ran P, g in Ran P. At slope s,
l acts as i s.d/dp on Bloch sections, so
  D_oo(s) := sup_p || Pi_H(p) (s.d_p P(p)) restricted to Ran P(p) ||^2.
Registered before computing it:
 B1 D_oo finite: no growth as |p| -> 0 along rays |p| = 1, 0.3, 0.1, 0.03, 0.01. Growth
    here, by a factor above 1.5 from |p| = 0.1 to 0.01, refutes the hand proof.
 B2 D_oo free of B: D_oo(B=9) <= 1.5 D_oo(B=3).
 B3 Flag, not a kill: D2c on the torus exceeding 1.25 D_oo. A kink in the weight
    can legitimately add to the slope-only value, so B3 would need a look at kinks.
 B4 Cross-check of the formula: a smooth periodic profile l = (M/2 pi) cos(2 pi x/(M B))
    has slope at most 1 and no kink, so D2c(M) should rise to D_oo(e_0) from below.
