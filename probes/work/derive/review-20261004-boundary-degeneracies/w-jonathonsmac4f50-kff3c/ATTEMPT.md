# Attempt: the u = P/4 zone-centre merger for J_x != J_y

Task `J:derive:review-20261004-boundary-degeneracies:a1`. Worker: Claude Sonnet 5.5, same family as the sources, unrefereed.

## Plain language first

The comparator is a four-band lattice model with couplings (J_x, J_y, J_z) and an odd term kappa. On the boundary J_z = J_x + J_y the middle two bands always touch at the zone centre Gamma. For kappa^2 = P/4 (P = J_x J_y) a pair of other touchings is being born exactly at Gamma, which is why this case was left out of the seven fixtures.

I took ONE omitted case: u = kappa^2 = P/4 exactly, on J_z = J_x + J_y, with J_x != J_y. I computed the exact expansion of the model near Gamma in its natural weighting, and found a radius inside which Gamma is the only touching. I showed the two spare bands stay apart from the two middle ones there. I showed the occupied pair of bands has Chern number 0 on every sphere around Gamma inside that radius. The radius is explicit and uniform along the whole curve u = P/4 for any fixed range of the ratio J_x/J_y. It cannot be uniform in u: just above P/4 the pair sits arbitrarily close to Gamma.

## What I read (as instructed)

- Axiom memo `docs/MINIMAL_AXIOMS_2026-06-29.md` (read in full, lines 1-233 at main_wt, head `a77a3449c9`): four axioms Lattice, Qubit, Admissibility, Record. They fix no Hamiltonian, hopping signs, couplings or a u = +1 Majorana comparator (lines 114-130). The whole attempt is therefore about a SUPPLIED MODEL, not about the axioms.
- Primitive registry check `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (read in full, 130 lines): three approved primitives (scale reference, kinetic isotropy, realized state). None is used and none supplies any dimensionless content here.
- All six source objects were hashed at `2868a0c453e667d1267f0e1e7403732a11893d78` and match (see `RECOVERY_STATUS.json`).
- Current origin/main moved on (`3e1a2dd2`); the pinned source commit was used.

## Setting and premises (all ASSUMED, supplied by the lane, none by the axioms)

- P0. ASSUMED: the comparator of the landed notes: 4x4 Bloch matrix H(f) = i M(f), u = +1 sector, landed hopping-sign convention, network terms exactly as embedded in the landed census runner (18 terms; `check.py` TERMS). A touching is a zero of det H (spectrum {+-l1, +-l2}, det H = (l1 l2)^2 >= 0).
- P1. ASSUMED (standard topology): for a continuous family of Hermitian matrices that stay non-singular on a sphere, the bundle of negative eigenvectors is unchanged by homotopy; the Chern number of the negative eigenline of a 2x2 Hermitian map (a + n.sigma) with |n| > |a| equals (+-) the degree of n/|n|.
- Notation: s = J_x + J_y, P = J_x J_y, u = kappa^2, E2 = 16 J_z^2 = 16 s^2; coordinates theta = 2 pi f = x (1,-1,0) + y (1,1,0) + z (0,0,1); weights x:1, y:4, z:4; quasi-radius r = max(|x|, |y|^(1/4), |z|^(1/4)).

## Steps

1. CHECKED (exact, symbolic in J_x, J_y, kappa; S1.0-S1.5). At J_z = s: H(0) has spectrum {0, 0, +-4s} independent of kappa, kernel spanned by (1,0,-1,0), (0,1,0,-1). The complement block C(0) has eigenvalues +-4s. det C(0) = -E2.
2. CHECKED (exact; S2.1-S2.6). With the Schur numerator Num = det C (A - B C^-1 B+) (Laurent polynomials, Pauli components N_x, N_y, N_z, N_0; det Num = det C det H), the exact Taylor jets are, for ANY kappa: N_x = -16 s^2 (2 J_y y - s z) + ..., N_z = 128 kappa s^2 y + ..., N_y = 16 s (4u - P) x^2 + c4 x^4 + ..., N_0 of weight >= 9 with weight-9 part 8 kappa s x z (s z + 2 J_y y). Here c4 = -(4/3)(-J_x^2 J_y - 4 J_x J_y^2 + 16 J_x u + 28 J_y u). On the relation u = P/4: c4 = -4 P s. So at u = P/4, Num = -E2 d_lead + G with d_lead = (2 J_y y - s z, P x^4/(4 s), -8 kappa y) and G of weight >= 6 (all monomials of total degree <= 12 checked).
3. CHECKED (S2.7). With the weights (1;2,2) that the landed boundary-census ball method uses, the leading jet at u = P/4 has N_y == 0, so it vanishes on the whole x-axis. That method does not apply here (it needs a = (P - 4u)/s != 0). The quartic weights (1;4,4) are required. The line-nodes note states the leading map at this weight (leading order, no radius); step 2 re-derives it from the full Laurent objects for all couplings and adds the weight-6 and weight-9 structure.
4. CHECKED (exact, from the independent full 4x4 Leibniz determinant; S2.8-S2.9). At u = P/4, det H has no Taylor monomial of weight < 8, and its weight-8 part is 16 s^2 |d_lead|^2. Along the axis (1,-1,0), det H = 16 q(c)^2 with q = (c-1)(4u(c+1) - 2P) for all kappa (landed identity re-derived). At u = P/4: det H = 16 P^2 (1 - cos x)^4, order 8 in x.
5. PROVED (conditional on 2 and on the inequalities below). Isolation criterion. Let 0 < r <= rho <= 1 and write |d_lead| >= sqrt(lam) r^4 with lam = min(p^2, e^2, b^2 e^2/(a^2 + e^2)) for d_lead = (a y - b z, p x^4, -e y) (proof: minimise over the boundary of the (x/r, y/r^4, z/r^4) cube: |X| = 1 gives >= p^2, |Y| = 1 gives >= e^2, |Z| = 1 gives >= b^2 e^2/(a^2 + e^2)). Let K_G be a bound with |G| <= K_G r^6 and K_0 with |N_0| <= K_0 r^9 (Taylor terms plus Lagrange remainder |e^{i phi} - T_12| <= |phi|^13/13!, with |m.theta| <= mu_m r). If K_G rho^2 + K_0 rho^5 < E2 sqrt(lam) and the C-gap 4s - K_C rho > 0 (Weyl, |e^{i phi} - 1| <= |phi|), then on 0 < r <= rho: C has one negative and one positive eigenvalue; the homotopy -E2 d_lead + t G never vanishes; |N_0| < |N|. Hence det Num < 0, det H = det Num / det C > 0, and Gamma is the unique zero of det H in the quasi-ball. The Pauli map has degree 0 because d_y >= 0, so the map omits a point of the sphere.
6. CHECKED (exact rational; S3). The inequalities of step 5 hold with these quasi-radii (x <= rho, |y|,|z| <= rho^4):

   | (J_x, J_y, J_z; kappa) | rho | C gap at least (of 4s) |
   |---|---|---|
   | (9/5, 1/5, 2; 3/10) | 0.143 | 6.17 (8) |
   | (1/5, 9/5, 2; 3/10) | 0.120 | 4.93 (8) |
   | (2, 1/2, 5/2; 1/2) | 0.162 | 6.60 (10) |
   | (1/2, 2, 5/2; 1/2) | 0.146 | 5.18 (10) |
   | (4, 1, 5; 1) | 0.162 | 13.2 (20) |
   | (1, 1, 2; 1/2), equal in-plane control | 0.174 | 3.82 (8) |

   The control sits inside the landed J = 2 note's own radius (0.2); it is not new.
7. CHECKED (exact rational; S4.0, S4). Homogeneity: every coefficient of Num is of degree exactly 3 and of C of degree exactly 1 in (J_x, J_y, kappa), so only the ratio J_x : J_y matters. By majorants of the reduced coefficient polynomials (after kappa^2 -> P/4) with s = 1, J_x, J_y <= 1, kappa <= 1/4, and lam >= min((P0/4)^2, 16 P0, 16 P0/(4 + 16 P0)) with P0 = a0 (1 - a0), a0 = 1/(1+m), one rho works for every coupling of the curve u = P/4, J_z = s with J_x/J_y in [1/m, m]: m = 2: rho = 127/2000; m = 5: rho = 1/20; m = 10: rho = 77/2000. This is a uniform statement along an intermediate-coupling curve, not just seven fixtures.
8. PROVED given P1 and steps 5-7 (the argument is the landed one, applied to the new inputs). Local occupied-bundle statement. On a quasi-sphere inside the ball, H = L+ diag(S, C) L with L = [[1, 0], [C^-1 B+, 1]] and S = Num/det C. Scaling the off-diagonal block of L by t in [0,1] keeps H_t non-singular (Sylvester inertia, signature of S plus signature of C), so the occupied rank-2 bundle is the sum of the negative line of C and the negative line of S. The negative line of C is defined on the whole ball (eigenvalues of opposite sign), so it is trivial on the sphere. The negative line of S is the pullback of the spin line by N/|N|, of degree 0. So the Chern number of the occupied two-band bundle on every such sphere is 0, and the middle gap is open on it.
9. CHECKED (FLOAT, S6). Chern number of the two lowest bands on the certified quasi-sphere by the Fukui method is 0 (1e-16) at (9/5,1/5,2;3/10) and (1/2,2,5/2;1/2); the maximum plaquette phase is 0.65 (resolved). The numpy Bloch eigenvalue product agrees with (N_0^2 - |N|^2)/det C at 300 random ball points (rel. err 3e-8). The floating checks are diagnostics, not the proof.
10. CHECKED (exact line identity plus 40-digit mpmath; S5). The nonisolated set just above the merger: for u = (1+d) P/4 with d > 0, the axis zero cos x0 = (1-d)/(1+d) lies in (-1,1) (x0 ~ 2 sqrt(d)), with a two-dimensional kernel. So no quasi-ball radius can be uniform as u -> P/4+. Controls (S5.4-S5.7): at kappa = 601/2000 (J = (9/5,1/5,2)) the weight-2 term of N_y is nonzero and a touching sits at x0 = 0.115 < 0.143, inside the u = P/4 ball; swapping J_y <-> J_x in d_lead is detected; the inequalities fail at rho = 1/2.

## What is new relative to the sources

NEW (scoped to the supplied comparator): step 2's symbolic jets at weight 6 and 9 for all couplings, steps 6-7 (explicit radii, complement gap and the uniform radius along the curve u = P/4, J_z = s for compact ratio ranges), and step 10 as the exact statement of non-uniformity.
NOT new: the leading map at u = P/4 and its degree 0 (landed line-nodes note, leading order, "no remainder radius"); the occupied-bundle argument (landed in the census note); the equal-in-plane point (1,1,2;1/2) (landed J = 2 note); the line identity and pair birth at c2 = P/(2u) - 1; source retrieval and hash verification.
Related landed note not used for new claims: the J = 2 zone-centre note (J_x = J_y = 1 only).

## First unresolved step

Step 7 stops at ratio ranges [1/m, m]: as J_x/J_y -> 0 or infinity, P0 -> 0 and lam -> 0, so the stated radius shrinks to zero; whether Gamma stays isolated with a radius that does not vanish there is open (it is the decoupling limit, where kappa = sqrt(P)/2 -> 0 as well). Step 8 relies on the standard degree-to-Chern identification (P1), not re-proved. Not attempted: the other omitted cases (endpoint merger at the u = P/2 flip, the corner (1/2,1/2,0) on J_z = |J_x - J_y|, the interior between the seven fixtures), global band Chern numbers beyond local spheres, and any physical reading.

## Process notes for the supervisor

- No file under the repository was written. Ai/probes steps (`claim.py`, committing the checker, `run_probe.py`) were not run by this worker because the brief forbids editing the repository outside the output directory.
- Ordinary cross-model confirmation has NOT been done; the whole attempt is same-family and unrefereed.
- Open PR search (`gh pr list --search`) found nothing on the Gamma, P/4 or quartic-weight theme; the only hit for the composite-site theme was a closed PR (#9300) on slice fluxes.
