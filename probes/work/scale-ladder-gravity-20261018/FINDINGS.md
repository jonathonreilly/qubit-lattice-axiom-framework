# Findings log: gravity on the scale ladder (supplied models; finite floating-point checks)

## F1 (M1). Symmetry census of two-derivative quadratic forms (scratch/census.py)
Gauge-invariant forms under each group (invariant forms in parentheses):

| field | B4 | B4+ | K48 = S4 x inversion (the Kuhn complex) | OhT | OT | K12T |
|---|---|---|---|---|---|---|
| scalar k^2 | 1 | 1 | **2** | 2 | 2 | 3 |
| spin-1 | 1 (3) | 1 (3) | **2** (9) | 2 (7) | 2 (7) | 4 (15) |
| spin-2 | 1 (9) | 1 (9) | **2** (38) | 2 (26) | 2 (26) | 3 (67) |
| spin-2 mass | 0 (3) | 0 (3) | 0 (7) | 0 (6) | 0 (6) | 0 (11) |

So the complex's own symmetry plus linearised diffeo does NOT single out EH. A second form exists.

## F2 (M2). Metric universality of the Regge leading symbol (scratch/regge_project.py)
- The K48 gauge-invariant spin-2 pair is spanned by linearised EH of K48-invariant flat metrics
  g0 = delta + b u u^T, with u = (1,1,1,1). EH_g0 lies in the span (residual 1e-14) and is not
  proportional to EH_delta (misfit 0.42 at b = 0.3).
- Lengths l^2 = v^T g0 v give a Regge O(k^2) symbol of exactly -(1/4) sqrt(det g0) EH_g0:
  coefficients -0.250000, -0.370810 and -0.158114 at b = 0, 0.3, -0.15, matching -sqrt(1+4b)/4,
  with misfit <= 1.2e-7 (Richardson).
- So the graviton's leading form and cone are those of the edge-length metric. This is metric
  universality, not lattice symmetry.

## F3 (M3). A common cone at leading order (scratch/fem.py)
On the same complex, with the same g0 (b = 0 and 0.3), both fields match their continuum forms
to 1e-8:
- P1 (Whitney 0-form) scalar: leading symbol = sqrt(g) k g0^-1 k exactly (ratio 1.000000000).
- Whitney 1-form Maxwell: leading symbol = sqrt(g) x continuum F^2/2.

## F4 (M3). O(k^4) fingerprints at b = 0, by exact Schur elimination of lattice-only edge modes (scratch/onshell.py)
Write omega^2 = k^2 (1 + alpha k^2).
- Regge TT: alpha = -(1 + sum n^4)/12 for both polarisations (reproduces the OK4 note by an
  independent method).
- P1 scalar: the same law, exactly.
- Whitney Maxwell: birefringent and S4-only. Axis gives -0.1027 and -0.0859; face+ gives
  -0.0707 and -0.0665, against -0.0820 and -0.0636 for face-.

## F5. The exact lattice shell at b = 0 (scratch/exact_shell.py)
- On sum_mu 4 sin^2(p_mu/2) = 0 (the P1 scalar's exact shell, which is the hypercubic NN
  Laplacian's), the Regge 15x15 edge form has 7 machine-zero singular values (<= 1.4e-16),
  against 5 off shell (4 gauge plus the fifth branch).
- So both graviton polarisations propagate with exactly the scalar lattice dispersion at every
  sampled momentum (k up to 1.5; axis, face, body and generic directions).
- Whitney Maxwell does not: its 2nd and 3rd singular values are about 1e-4 there.
- At b != 0 (scratch/exact_b.py) the coincidence fails beyond leading order, and the fifth zero
  mode lifts. The all-orders match is special to the hypercubic edge metric.

## Phase 2 (after PR #9708 opened)
- F6. The pullback and the full form are different objects. The line-map pullback Q_h = M^T Q M is
  -(1/4) sqrt(det g0) EH_g0 at every b. With the non-metric edges eliminated (Schur), the full form
  matches it only at b != 0: at b = 0.3 and 0.05 the misfit is 1e-6. At b = 0 the eliminated block has
  an eigenvalue falling as k^2, so the reduction is singular (schur2.py, schur3.py). The first PR
  version stated C3 without this distinction; it was corrected in the second commit.
- F7. The fifth null direction (fifth*.py):
  - present on every diagonal background tested (a stretched tick keeps it);
  - lifted linearly in b, with singular value about 66 b;
  - modulo gauge, its metric part is EXACTLY u u^T - 2*1 (cosine 1 - 1e-8).
- F8. On-shell P1 stress sources the fifth direction at a fixed 9-23% of its norm, at every momentum
  scale. Conserved continuum stresses through the line map do too (12%, 19%). Linear response in the
  15-edge carrier at b = 0 is therefore ill-posed in that channel.
- F9. Newtonian rung of the pullback: h_tt k^2 -> -2 isotropically (continuum -EH/4); on the axis the
  response is exactly -2/(4 sin^2(k/2)) at all k (newton2.py).
- F10. The pullback at O(k^4) is birefringent: axis -1/9 and -2/9, face -1/9 and -0.194, body -0.148
  doubly. This reproduces the OK4 F10 values. The pullback is also off the Hodge shell (qh_k4.py).
- F11. Cubical complex (cubical.py), standard facts:
  - d d* + d* d = phat^2 I on all 16 components;
  - the fine-lattice Kahler-Dirac operator d - d* squares to -Delta, with no doublers;
  - cubical Maxwell sits on the shell exactly;
  - the P1 scalar on Kuhn equals the NN Laplacian (4e-15);
  - naive/staggered fermions have the shell at doubled momentum, so the 2a rung.
  The repo's own DK carrier uses the sin^2 k shell (reader digest).
- F12. Regge nullity 7 holds on 25 random COMPLEX points of the variety sum 4 sin^2(p/2) = 0
  (variety.py).
- TENSION (K48 family): a real spectrum needs b = 0, but at b = 0 there is a matter-sourced flat
  direction. The pullback is free of it but birefringent at O(k^4). Next: a B4-symmetric
  triangulation (barycentric subdivision of the cubical complex).

## Phase 3 (PR #9714)
- F13. The Kuhn fifth null vector is NOT flat: D x != 0 (|Dx|/|D| ~ 0.6), while the deficit-map
  rank is E - 4. It is curvature the quadratic action Q = A'^T D does not see.
- F14. Barycentric subdivision (B4 incl. tick reflection, 384 orthoschemes, 240 edges, 16 vertex
  types): nullity 64 + 16, and the extras are curved and metric-carrying (bary*.py, flatq.py).
- F15. Lifting the hidden direction: a body-diagonal tilt gives Re k_t/|k| -> 0.27 (non-real at
  leading order). A spatial skew c (1,1,1,0) gives Re k_t/|k| ~ k^2, and the full form is
  -(1/4) sqrt(det g0) EH_g0 (skew*.py).
- F16. D4 cone (d4*.py; regge_generic.d4cone): D4 = Z^4 u (Z^4 + u/2) plus deep holes; 16-cells
  coned. 96 simplices, B4-symmetric, no orthoschemes.
  - nullity = 32 vertex displacements only;
  - full-form symbol -(1/4) EH;
  - P1 scalar has real energies and NO on-shell k^4 term (W(F4) symmetry);
  - graviton has two real shells omega^2 = k^2 (1 -+ c k^2), each 1 metric + 1 non-metric mode;
  - c^2 = [(1 - S2)^2 - 12 T]/144 predicts 3 further directions within 0.4%;
  - 8 massless non-gauge directions (EH needs 6): 2 non-metric partners.
- F17. Matter on the D4 cone:
  - P1 on every vertex sources the relative vertex-type (optical) displacements at O(1), which
    is inconsistent;
  - the uniform part is O(k);
  - a site-cell metric read through the holes (d4m/d4q) is blind to non-site displacements;
  - a static T_tt source through it gives graviton -2 (h_xx = -h_tt) plus one CONFORMAL partner
    (pattern = identity) at -2/3, so the total h_xx/h_tt = -1/2: the Brans-Dicke omega = 0
    pattern (gamma = 1/2 if read as usual; excluded by solar-system tests).
- F18. A recurring direction: the Kuhn fifth direction's metric part is u u^T - 2*1, and the D4
  partner's site-metric reading is 2*1 - u u^T (orientation-biased L) or pure conformal
  (symmetric L). Both live in the conformal / body-diagonal sector.
- NEXT: a carrier with no non-metric soft modes, or a local term giving them mass without
  breaking the lattice diffeos; a site-matter Ward identity on D4; the mechanism of the Kuhn
  shell at b = 0.
