---
claim_id: zoom_fixed_point_tick_is_exactly_perfect_only_at_history_level_finite_band_ticks_keep_liv_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "(T1) No update with finitely many bands per cell and real-analytic (exponentially local) Bloch unitary or Hamiltonian has an exactly relativistic lowest band on any open momentum set; Lorentz violation survives at some finite order, so a tick cannot be the zoom's fixed point. (T2) Block averaging keeps every physical pole; zooming sends lattice-unit coefficients to c0/B^2 but leaves the finest rung's physical Lorentz violation unchanged. (F) At history level the free blocking fixed point exists exactly in d = 3+1. It was built in momentum space by proper-time-factorised image sums: lowest band relativistic to 9e-11 (scalar and fermion, m = 0 and 0.3, |p| <= pi/2), on the metric null cone in a constant anisotropic metric (4e-15); fermion couplings exponentially local (kappa 2.7 at alpha = 1/2, 1.8 at alpha = 1); Ginsparg-Wilson exact (4e-16); no doublers; the overlap of the perfect kernel is the kernel itself (3e-16). Truncated to range R, its overlap c falls from 2e-2 to 3e-7 (R = 1..5) but is nonzero; the Wilson-kernel overlap has c = -(S+1)/6. A gauged hypercube truncation gives index Q = 0, 1, 2 exactly in 2D U(1). (E) The tree-level rescue is complete for free matter only. Radiative dimension-six terms with one-loop size alpha/4pi (5.8e-4 to 1.6e-3) would put 14N breakup at 48-84 EeV, against the < 5.5e-5 to 4.9e-4 needed; protecting them takes a dressed condition, which is not a theorem. Verdict: PARTIAL."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/zoom_fixed_point_tick_is_exactly_perfect_only_at_history_level_finite_band_ticks_keep_liv_2026_10_26.py
---

# The zoom fixed point is exactly perfect only at history level: finite-band ticks keep Lorentz violation

Runner: runner.py. TOTAL: PASS=15 FAIL=0 in 3.5 s, seeded, AUDIT_TIMEOUT_SEC = 120, 2.7 k characters, 136 MB.
Criteria were fixed before the run (criteria_pre_run.txt). It was re-run under a unique filename with identical output.

Labels: [T] exact or theorem, [F] finite diagnostic, [E] estimate against measurement, [S] reading.
The axioms are unchanged, CL is not edited, and nothing is adopted.

Pre-run deviation, stated:
- P5b used the alpha = 1/2 kernel, because the alpha = 1 truncations converge too slowly in R for an R <= 7 test (c = 0.12, 0.08, 0.05, 0.02 at R = 4..7).
- My first in-run threshold (dec[3] < 1e-4 dec[0]) was stricter than the pre-registered P5 condition. It was reset to the pre-registered "nonzero, reduced against Wilson, falling", with numbers reported.

## Builds on, uses, contradicts
- Inputs: agents/nuclear-vacuum-breakup (walls; the scaling P_open ~ |c|^(-1/4); the dimension-eight formula) and agents/assumed-inputs-model section 3 (c_g = -S/24, c6, E* = 1.217e18 GeV).
- main: docs/ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md lists "an anisotropic/perfect action" as a live completion that it does not select. This note tests that completion and narrows it (T1).
- No main note on block-spin fixed points or perfect actions (git grep origin/main: 0 hits for perfect action, Bietenholz, or blocking fixed point). The 14 Ginsparg-Wilson notes are not contradicted.
- Open PR #10049 (overlap from the walk): P4b makes its overlap step redundant if the kernel is the fixed point.
- agents/repaired-kernel-anomaly: the repaired kernel (r_s = 1/3, T-even pieces) would be replaced.
- Literature, supplied:
  - Hasenfratz-Niedermayer, NPB 414 (1994) 785;
  - Bietenholz-Wiese, NPB 464 (1996) 319;
  - Ginsparg-Wilson, PRD 25 (1982) 2649;
  - Hasenfratz-Laliena-Niedermayer, PLB 427 (1998) 125 (index theorem for fixed-point operators);
  - Collins-Perez-Sudarsky-Urrutia-Vucetich, PRL 93 (2004) 191301;
  - Chadha-Nielsen, NPB 217 (1983) 125.

## Theorems
**[T] T1, the finite-band no-go.**
- Setting: U(p) is an N x N Bloch unitary (or Hamiltonian), real-analytic and 2pi-periodic in p. Real-analytic is the same as exponentially local couplings.
- Claim: if one eigenvalue equals exp(-i tau sqrt(p^2 + m^2)) on an open set, then P(p, z) = det(z - U(p)) vanishes on g(p) = exp(-i tau E(p)) there.
- By analyticity, P(p, g(p)) = 0 on all of R^3 (on R^3 minus the origin for m = 0, which is still connected for d >= 2).
- By periodicity, every image g(p + 2 pi l) is also a root of P(p, .).
- Two images agree identically only if E_l - E_l' is constant on an open set, which is impossible for l != l'.
- So P has infinitely many distinct roots, against its N roots. Contradiction.
- Hence some Taylor order of the lowest band is Lorentz-violating, for any finite range or exponential tail and any number of sites per cell.
- Lemma check: 343 images are distinct at a random p (P5c).
- Corollary: an exactly perfect band needs the infinite image tower Sum_l of the perfect propagator, meaning states of every momentum |p + 2 pi l|. That is a continuum folded under the sites. It is not available to a tick on one qubit per site.

**[T] T2, zooming keeps physical poles.**
- The blocked propagator is a positive weighted sum of fine propagators at preimage momenta. So its poles are the fine poles.
- In coarse-lattice units c_B = c0/B^2. P2c gives c_B B^2 = -1/12 for B = 1..8, equal to c0 = -(S+1)/24 on the axis.
- The zoom fixed point is therefore the infrared attractor of lattice-unit coefficients. In physical units E* the finest rung's Lorentz violation is unchanged.
- "Finest tick = fixed point" means the finest rung is the zoom of an infinitely finer theory. That is T1's continuum again.

## Finite diagnostics in d = 3+1, exact construction
- Construction:
  - G*(p) = Sum_l Prod_mu s(q_mu)^2 / q^2 (+ alpha), with q = p + 2 pi l and s(q) = sin(q/2)/(q/2), for 2x2x2-cube (factor-B) averaging.
  - Proper time factorises the image sum into 1D sums.
  - The 1D sums are done in closed Poisson/erfc form, matching a direct 4e4-term sum to 3e-16.
  - The fermion is G* = -i gamma.rho + alpha, D = G*^(-1).
- P1, exact dispersion: the lowest band read from the lattice time correlator equals sqrt(p^2 + m^2) to 9.0e-11.
  - This holds for scalar and fermion, m = 0 and 0.3, at 0.3 (axis), pi/4 (face) and pi/2 (body).
  - It is independent of alpha, which only moves the t = 0 contact term.
  - In a constant metric gamma^ii = (1.7, 0.6, 1) the pole lies on the metric null cone (4e-15).
- P2, the zoom flow: the iterated factor-2 map equals closed-form B = 4 blocking (2e-16).
  - Starting from the naive scalar, the flow converges to G*.
  - |G_B - G*| = 2.8e-2, 7.2e-3, 1.8e-3, 4.5e-4 for B = 2..16, ratio 4.00. This is the p^4 operator being irrelevant.
- P3, locality: the fermion couplings decay as exp(-kappa r), with kappa = 2.74 per spacing (alpha = 1/2) and 1.76 (alpha = 1), along the axis and similarly along the diagonal.
- P4, chiral structure:
  - Ginsparg-Wilson gamma5 D + D gamma5 = 2 alpha D gamma5 D holds to 4e-16, and gamma5-hermiticity is exact.
  - The overlap with m0 = 1/(2 alpha) returns D* itself (3e-16).
  - The 15 corners sit at D = 1/alpha (rho = 0 to 1e-10), and |rho| <= 0.40 wherever |p|_inf >= pi/2. So there is one light cone, at p = 0, and no doublers.
- P5, finite range:
  - The Wilson-kernel overlap has sinh w = |sin p|, so c = -(S+1)/6 (sympy): -1/3 on the axis, -2/9 on the body diagonal. Ginsparg-Wilson alone does not remove the dimension-six term.
  - Range-R truncations of D* (alpha = 1/2) used as overlap kernels have
    - c_axis = 2.0e-2, 7.8e-3, -9.4e-5, -2.4e-6, 3.1e-7 for R = 1..5 (body about 2/3 of these).
    - These are exponentially small but nonzero, as T1 requires.
- P6, chiral content: a 2D U(1) torus 8x8 with flux Q = 0, 1, 2 plus seeded noise of 0.25 rad per link. The overlap on the gauged hypercube-truncated perfect kernel has index 0.000000, -1.000000, -2.000000, and GW holds to 2e-15.
  - The 4D gauged index and domain-wall content were not computed. They are supplied by Hasenfratz-Laliena-Niedermayer for fixed-point operators.
- P7, sympy, range-2 improved ticks (fixed point through the first irrelevant order):
  - The link band 4s^2 + (4/3)s^4 has zero p^4; c8 = -1/180 S6, i.e. -0.0056 on the axis.
  - The fermion sin p + sin^3 p/6 has zero p^3; c8 = -(3/40) S6, i.e. -0.075 on the axis.
  - The lattice-time (step) piece must be cancelled as well, for example by a symmetric two-rung composition. That is not built here.
  - The c8 values depend on which improvement is chosen. They are illustrative, not predictions.

## What else the rules need [S/E]
- Chirality: unchanged in kind. The perfect kernel is already Ginsparg-Wilson, so Luscher's projector and the index (P6, 2D) carry over.
- Gravity:
  - The CL-3 hinge sum, the tick fraction and offsets, and the six-edge carrier read only edges. They are unchanged.
  - The derived weak-field results (gamma = beta = 1, Nordtvedt 0, frame dragging, two tensor waves, one G) use only the dimension-<=4 matter coupling, which the perfect weight reproduces exactly (P1b: matter on the edges' null cone).
  - The tensor waves keep their tick-level (ka)^2/24 correction. That is untested and unconstrained (GW170817 probes (E/E*)^2 ~ 1e-80).
  - The wave-speed-equals-light statement still needs CL-1's tick/edge ratio clause for the edges.
- Links: the photon and gluon band c_g comes from Hamiltonian ring-exchange registers. Under T1 it cannot be made perfect at tick level. A history-level perfect gauge weight (Bietenholz-Wiese free U(1)) exists classically but is not built or tested here for the registers.
- Interactions:
  - The classically perfect action is perfect at tree level only. Loops on a lattice regulator generate every term the kept cubic group allows.
  - Dimension four, unsuppressed (Collins et al.): delta c ~ alpha/pi. This is already met by the register's dressed-cone clause, a renormalisation condition. Chadha-Nielsen infrared attraction is only logarithmic.
  - Dimension six: kappa ~ g^2/16pi^2 x C, with C uncomputed.
  - The renormalized trajectory (the quantum perfect action) would protect every order. But it is the zoom of an existing continuum theory: T1/T2 again. It is not strictly defined for non-asymptotically-free sectors (hypercharge, the Higgs quartic), and the edge sector sits at no fixed point.
  - Shown: tree-level perfection and the scaling. Not shown: radiative protection.

## UHECR consequences [E]
- Residual dimension-six term kappa c, with walls scaling as kappa^(-1/4); axis-body EeV:

  | kappa | factor | d | 4He | 14N | 56Fe |
  |---|---|---|---|---|---|
  | 1e-2 | x3.16 | 8-14 | 13-22 | 27-47 | 57-98 |
  | 1e-3 | x5.62 | 14-24 | 23-39 | 48-84 | 101-174 |
  | 1e-4 | x10 | 25-43 | 41-70 | 86-149 | 179-310 |

  - 14N survives to 100 EeV on every ray only if kappa < 5.5e-5 (axis) or 4.9e-4 (body).
  - One-loop sizes: alpha_em/4pi 5.8e-4, alpha_s(E*)/4pi ~ 1.6e-3, (E*/M_P)^2/16pi^2 6.3e-5.
  - So an unprotected dimension-six term with C ~ 1 is EXCLUDED or borderline by Auger 50-100 EeV, and a dressed condition is needed.
- Dimension-eight residual only (dressed condition held):
  - Nuclear instability sets in above 2.1e21 (d), 4.2e21 (He), 1.5e22 (N) and 5.8e22 (Fe) eV at |c8| = 0.075. That is safe above every event, including Amaterasu at 2.4e20.
  - gamma -> e+e- opens at about 1.8e20 eV or not at all; the rules as written open it at 80 PeV.
  - Time of flight is unmeasurable (2e-51 s for a 10 GeV GRB photon).
  - Proton photopion (GZK) reopens: c8 E^6/E*^4 ~ 1e-9 GeV^2, far below m_pi m_p. This withdraws model.md's "no GZK" prediction, and cosmogenic EeV neutrinos come back.

## Simplification ledger
- Deleted if the matter weight is the zoom fixed point (3):
  - the walk-to-Wilson-kernel identification;
  - the m0 window (0 < m0 < 2/3), since m0 = 1/2alpha is forced;
  - the repaired kernel (r_s = 1/3, T-even pieces). The overlap step itself becomes an identity (P4b).
- Absorbed (1): the dressed-cone clause becomes a special case of the dressed fixed-point clause.
- Unchanged:
  - the edge-window repairs and the window;
  - the polar split;
  - the copy mass's copy-selection role. Its dimension-six band role leaves matter propagation, but whether it is still needed for one light copy under a per-field perfect weight is UNTESTED.
- Added: alpha (a blocking-scheme constant, physically inert: P1 shows the spectrum does not depend on it; locality is best near 1/2), plus the clause.
- Net: about -3 supplied items, +1 inert constant.

## Verdict (pre-registered rule): PARTIAL
- An exactly perfect TICK is impossible on finite bands (T1), and zooming cannot remove the finest rung's physical Lorentz violation (T2).
- The exact fixed point exists at HISTORY level, where the register already weights matter. There it is p^4-free to all orders for free matter, local, GW, doubler-free, index-correct (2D), and it deletes 3 items.
- Radiative protection is a condition, not a theorem.

Proposed CL text (UNTESTED, not adopted). "Each species' dressed two-point weight, link and edge dressing included, is fixed under the zoom (averaging over the even tiling's 2x2x2 cubes) through its first irrelevant order: its dressed cone is the edges' null cone and its dressed dimension-six term vanishes. The free matter history weight is the zoom's exact fixed point."

Gate:
- (1) No fitted number. The improvement coefficients are forced. alpha is inert for the spectrum.
- (2) No observed structure named.
- (3) Untested predictions:
  - no dimension-six LIV in any species;
  - gamma -> ee threshold >= ~1e20 eV;
  - nuclei stable below ~1e21 A eV;
  - GZK photopion and cosmogenic neutrinos restored;
  - cubic dimension-eight pattern.
- (4) It bends CL-1's dressed-cone clause (extended one order) and CL-1's tick reading for matter, already bent by the history-level weighting.
- Owner decision: the exact free history weight has an infinite image tower of poles, meaning states beyond the cell scale. Whether that reading bends one-qubit-per-site is an owner decision. The finite-order clause does not need it.
- PASS conditional on that reading.

## Smuggling review
- Forced or exact: T1, T2; the image-sum construction; the GW, overlap-identity and doubler results; the c = -(S+1)/6 formula; the improvement coefficients.
- Supplied:
  - alpha (inert);
  - the Gaussian blocking form;
  - the literature index theorem in 4D;
  - one-loop size estimates (C ~ 1 assumed);
  - nuclear walls inherited;
  - c8 example values.
- Nothing is fitted.

## Open
- One-loop dimension-six coefficient C on the rules' regulator. This is decisive at kappa ~ 1e-4.
- A history-level perfect weight for the link registers.
- A symmetric two-rung tick cancelling the step's dimension-six piece.
- 4D gauged index with the perfect kernel.
- Does the per-field perfect weight make the copy mass redundant?
