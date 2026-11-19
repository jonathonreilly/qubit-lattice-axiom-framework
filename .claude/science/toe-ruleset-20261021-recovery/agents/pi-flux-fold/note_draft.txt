---
claim_id: the_nested_sea_orders_its_face_flux_to_pi_but_the_flux_fold_is_a_scale_free_quartic_hilltop_and_a_split_cannot_pass_pi_flux_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Spinless half-filled nearest-neighbour cubic sea (hop 1) with link phases A whose every face carries flux of magnitude Phi (0 <= Phi <= pi); Bloch form on the 2^3 cell (k grids 6^3 to 48^3), a q-site magnetic cell for the uniform field, 8^3 and 12^3 tori; Inglis cranking mass M = 2 sum |<b|dH/dPhi|a>|^2/(E_b - E_a)^3 in the zero-mean gauge; semiclassical slow roll. Results: (A) all 288 divergence-free separable face-sign patterns on the 2^3 cell end in the one pi-flux class (E = -1.19380 against -1.00243 at zero flux); E(Phi) falls monotonically on the scaled Kogut-Susskind path S and on the lowest path N (which carries the nesting vector (pi,pi,pi)); the uniform field is highest. Phi = 0 is a maximum: V = V0 - 0.0278 Phi^2 on S, E - E0 ~ -0.029 Phi^2 ln(1/Phi) on N. Random face flux already sits 29% down. (B) No flux pattern gaps the whole nested surface (m(k+Q) = -m(k)); S keeps a surface, N leaves zero-energy lines, and Dirac points appear only at Phi = pi. Z_S = [1/(32 pi) + (ln(16/Phi) - 1)/(32 pi^2)]/Phi + O(1), matched by the lattice to 0.3% at Phi = 0.05 pi: a finite field distance, not the plateau's 1/Phi^2. On N the stiffness grows with L (0.14, 0.34, 0.59 at L = 16, 32, 48), so the roll is damped into the sea. (C) On S with its own stiffness the roll is a log-corrected quartic hilltop: n_s = 0.948-0.949 at N* = 55 (rungs 0-4), 3.8 sigma below Planck, r < 1e-7, exit at Phi_end = 0.04-0.2 pi. The quartic coupling is rung-free, so P = 2.4e5 at rung 0 and ln(P/A_s) stays above 25 to rung 200: A_s cannot be met. (D) The parent face holonomy is the product of its four child faces, so children at pi read 0 at the parent; a faithful split gives children Phi/4 (x = 0.953 of the Lieb drop still to release) or, as a Z2 lift, x = 0.299; per-face flux is kept only at 0, 2pi/3 and 4pi/3. (E) pi flux is a stable minimum on S and N. (F) E(Phi) = E(-Phi), and +pi = -pi: no selector. Supplied: hop 1 and half filling, the face flux as a dynamical register, the adiabatic stiffness as the kinetic term, J a = sqrt3, M_P a = 1 at the flat rung, N* = 55, semiclassical FRW."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_nested_sea_orders_its_face_flux_to_pi_but_the_flux_fold_is_a_scale_free_quartic_hilltop_and_a_split_cannot_pass_pi_flux_2026_10_22.py
---

# The nested sea orders its face flux to pi, but the flux fold is a scale-free quartic hilltop and a split cannot pass pi flux

Claim type: bounded_theorem. The candidate-law register has zero premise weight, and the axioms are unchanged.

The nested-prefold-sea note found two things. CL-1's Dirac sea is exactly the pi-flux staggered sea (R^2 = 1 holds if and only if every face phase is -1). The bare axis-hop (zero-flux) sea is nested, and a density-wave fold of it rolls slowly, but that fold is not the mass angle and a split cannot pass it.

This note tests the unification that follows. Let the fold be the face flux itself:
- Before roles, the link registers carry zero face flux, so the sea is the nested sea and the plateau.
- The face fluxes order to pi (Lieb's flux phase), which turns the nested sea into the Dirac sea.
- So inflation is the flux ordering, its end is the appearance of Dirac matter, and the order parameter is the face-flux magnitude Phi, going from 0 to pi.

The questions are:
1. What is E(Phi), and what is the stiffness near Phi = 0?
2. What do the slow-roll numbers come out as?
3. Does a split pass the flux order?
4. How does the roll exit and reheat?
5. Does the flux sign need a selector?

## Results

### A. The energy landscape (question 1)

**A1 [D]. End points.** E(0) = -1.00243 and E(pi) = -1.19380 per site. These reproduce Theorem 6 of the main note HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02, and V0 = 0.19137.

**A2 [T+D]. Paths.** "Uniform face flux Phi" is not one configuration.
- Every face-sign pattern sigma_f = +-1 with zero divergence on each cube (three faces in, three out) gives a path A(Phi) with |flux| = Phi on every face. Scaling commutes with gauge transformations of real A, so the integer lift is what labels the path.
- There are 288 separable patterns (sigma_p = s_p (-1)^(v_p.r) per plane) with zero mean on the 2^3 cell. All of them end in the same pi-flux class (energy spread 2e-16).
- The lowest at Phi = 0.2 pi is a family of 24 degenerate cubic images. All of them carry a (pi,pi,pi) Fourier component; this is path N.
- Path S is the scaled Kogut-Susskind field in the zero-mean gauge: A_y = (Phi/2)(-1)^x, A_z = (Phi/2)(-1)^(x+y).
- Path U is the uniform field B = (Phi, Phi, Phi).

**A3 [D]. Ordering of the paths.** E falls monotonically on N and S, and N < S < U at every Phi tested.

| Phi/pi | N | S | U (Hofstadter) |
|---|---|---|---|
| 0.25 | -1.0387 | -1.0200 | -1.0114 |
| 0.5 | -1.1019 | -1.0737 | -1.0353 |
| 0.75 | -1.1651 | -1.1521 | -1.1138 |

**A4 [D]. The top.** Phi = 0 is a maximum.
- On S, V = V0 - (k/2) Phi^2 with k = 0.0555. The value of (E - E0)/Phi^2 is flat to 1e-3.
- On N, E - E0 = -Phi^2 [alpha ln(1/Phi) + beta] with alpha = 0.029. This is the nesting log, so the zero-flux nested sea is unstable to flux at any strength: the 3D analogue of the square-lattice flux instability.

**A5 [D]. Random flux.** Random face flux (Z2 or U(1), 12^3 torus) gives -1.0580, which is already 29% of the way down. A random start and a zero start are not the same initial state, and only the zero start sits at the top.

### B. Stiffness: no 1/Phi^2 pole (question 1)

**B1 [D]. Gapless set** (box count from n = 12 to 24).
- On S it stays a surface (x4.4, x4.0).
- On N it becomes lines (x2.1, x1.9).
- Dirac points appear only at Phi = pi exactly.

**B2 [T]. No flux gaps the whole nested surface.** A flux coupling at Q = (pi,pi,pi) has the matrix element m(k) = 2i Phi sum_mu a_mu cos k_mu. This is odd under k -> k + Q, which maps the surface to itself, so m changes sign on the surface and vanishes on a curve. The density wave's scalar coupling has no such zero, which is why it gave a 1/D^2 pole and the flux does not.

**B3 [T+D]. The pole on S.** In the zero-mean gauge the S coupling links k to k + (pi,0,0) and to k + (pi,pi,0), with matrix elements -sin k_y and -sin k_z. A two-level reduction on the crossing lines gives

Z_S = [1/(32 pi) + (ln(16/Phi) - 1)/(32 pi^2)] / Phi + O(1).

- The (pi,0,0) lines (kx = +-pi/2, cos ky = -cos kz) give 1/(32 pi) exactly.
- The (pi,pi,0) family separates into the 2D square-lattice band in (kx, ky), whose van Hove log gives the ln(16/Phi) term.
- The exact quadrature at Phi = 1e-3 agrees to 4e-4 (0.02749 against 0.02748).

**B4 [D]. Lattice check.** The lattice Z_S on 40^3 cells is 0.1360 at Phi = 0.05 pi (asymptotic 0.1364) and 0.0593 at 0.1 pi (0.0612). A pole of order 1 gives a finite field distance, int sqrt(Z) dPhi ~ sqrt(Phi ln(1/Phi)). It is not the plateau's 1/Phi^2: in fold-inflaton's classification this is the d = 2 case, with a log.

**B5 [D]. Path N is dissipative.** On N the zero-energy nodal lines make the adiabatic stiffness grow with the grid: 0.144, 0.343 and 0.590 at L = 16, 32 and 48 for Phi = 0.4 pi. The roll along the energetically preferred channel is therefore Ohmically damped into particle-hole pairs, not inertial. At pi the Dirac points give only a log (0.0067, 0.0082, 0.0090).

### C. Slow roll on S, with no free kinetic constant (question 2)

**C1 [D]. Spectral index and tensors.**
- Setup: chi = zeta int sqrt(Z_S) dPhi with zeta = (J a)^-1/2/(M_P a_r), J a = sqrt3 and M_P a = 1 at the flat rung. V is the computed S landscape and Z_S is the computed stiffness (the asymptotic form below 0.05 pi).
- Class: Z ~ 1/Phi turns V0 - k Phi^2/2 into V0(1 - lambda chi^4), a quartic hilltop, so n_s = 1 - 3/N* plus a log correction.
- Numbers at N* = 55: n_s = 0.9491, 0.9479 and 0.9479 at rungs 0, 2 and 4. The tensor ratio r is 9e-8, 6e-10 and 3e-12.
- Exit: eps reaches 1 at Phi_end = 0.20, 0.09 and 0.04 pi.

**C2 [T+E]. Against measurement.**
- n_s is 3.8 sigma below Planck (0.9649 +- 0.0042), and further below ACT with DESI. It would need N* of about 77 (with the log correction) to 85.
- Amplitude, theorem: V/M_P^4 ~ 2^-4r, while the canonical field ~ 2^-r sqrt(Phi). So V_r(chi) = 2^-4r V0 - lambda chi^4 with lambda independent of the rung: the fold is a scale-free quartic, and P ~ lambda N^3 does not depend on where the fold sits.
- Amplitude, numbers: P = 2.4e5 at rung 0, and ln(P/A_s) = 32.4, 29.8, 27.9, 26.6 and 25.6 at rungs 0, 20, 60, 120 and 200. Only the stiffness log drifts it. A_s = 2.1e-9 cannot be met at any rung.
- P > 1 also means the near-top roll is dominated by quantum diffusion rather than by classical slow roll.

The density-wave fold's amplitude, by contrast, fixed a rung because its plateau kept V0 and the field distance apart.

### D. Passing (question 3)

**D1 [T]. Stokes.** A parent link is two child links in series, so a parent face holonomy is the product of the four child faces it bounds (checked on 20 random U(1) fields to 6e-16). Three consequences follow:
- Children at pi on every face read (-1)^4 = +1 at the parent: the Dirac sea of rung n is a zero-flux sea seen from rung n+1.
- A parent pi face forces an odd number of child pi faces (Z2) or a child mean of pi/4 (U(1)). The all-pi child pattern is forbidden.
- A per-face flux survives the split only at the fixed points of Phi -> 4 Phi mod 2 pi, which are 0, 2pi/3 and 4pi/3. pi is not among them.

CL-1's passing carries "each excitation of given charges, flux and momentum", so it is holonomy-faithful, and these consequences apply to it.

**D2 [D]. Born children.**
- The self-similar (uniform-field) state passes Phi -> Phi/4. At the child pi/4, E = -1.0114, so x = 0.953 of the Lieb drop is still to release: the children are re-seeded almost at the top.
- The Z2 lift (child KS field times the parent KS sign on the first half of each parent edge) keeps every parent face at -1. On 8^3 it gives E = -1.1302 against the child pi value -1.1902, so x = 0.299.

**D3 [T+D]. Clock arithmetic.**
- In one split interval (ln 2 e-folds) a slow roll grows Phi by 2^|eta| = 1.018, while faithful passing divides it by 4. The order is reset at every split.
- A fixed born share x gives power-law inflation or, as x -> 1, de Sitter with no exit (fold-inflaton C5). Neither is a clock.
- Keeping pi per face across the split needs a passing that threads a pi flux line through every parent face. That passing is not holonomy-faithful, and it writes the clock into the rule.

### E. Exit and reheating (question 4)

**E1 [D].** pi flux is a stable minimum on both paths: V''/2 at pi is 0.0745 on S and 0.0509 on N.
- On S, eps reaches 1 well before pi (C1), so the exit is graceful and lands on the Dirac sea, releasing V0 = 0.191 per site.
- The q = 0 particle-hole density of the Dirac sea goes as omega^2 and is nonzero at every omega > 0, so oscillations of Phi about pi can decay into Dirac pairs: neutral particle-hole matter.
- On N the energy goes into the sea during the roll itself, through B5.
- Rates are not computed.

### F. The flux sign (question 5)

**F1 [T+D].** E(Phi) = E(-Phi) by complex conjugation (exact to 0e+00 on N), and +pi and -pi are one holonomy. Every pattern ends in the same class (A2). So:
- The roll breaks T transiently, into +Phi and -Phi domains and the 24 cubic images.
- All of these merge at exit, so no selector is needed and no domain walls survive.
- Torus Wilson-line classes (main note, Theorem 3) are a finite-volume effect and are not a selector in infinite volume.

## Verdict

**Positive.**
- The nested sea's own energy forces the flux ordering. Phi = 0 is a log-unstable maximum along the nesting channel, pi is the global end (Lieb, and the main note's 4^3 certificate), and the end state is CL-1's Dirac sea, with no sign selector and no relic walls.
- "Inflation ends when Dirac matter appears" is therefore a consistent picture: Dirac points exist only at Phi = pi.

**Negative.** As a primordial clock it fails on four counts.
- (i) No flux pattern can gap the whole nested surface (B2). There is no 1/Phi^2 pole and no Starobinsky plateau.
- (ii) The adiabatic channel S is a scale-free quartic hilltop. Its n_s = 0.948 is 3.8 sigma low, and its amplitude misses A_s by more than e^25 at every rung (C2).
- (iii) The preferred channel N is damped into the sea, not inertial (B5).
- (iv) A holonomy-faithful split, which is CL-1's passing, sends pi to an average of pi/4 per child face, so the order is reset at every split (D1-D3).

This is a sharper failure than the density-wave fold, which at least had the right index.

## Candidate law text (tested, not recommended)

> CL-1 (face clause). "Each face of the cube tick carries a face phase read from the plaquette of its link registers; the first odds carry face phase zero (the bare axis hop); face phases are dynamical registers advanced by the update's sea, whose half-filled energy is least at phase pi."

> Split (flux passing), needed for a clock. "A split passes each parent face phase to every child face it contains."

Smuggling check:
- The face clause unifies CL-1's spin-3/2 overlap phases (R^2 = 1 iff pi) with the link plaquettes: one register instead of a fixed coefficient plus a link term, which is the simplification sought. Its pi end is forced by energy (A2, and Lieb), not supplied.
- The zero-flux start is supplied. Random flux is not the top (A5).
- The passing clause violates Stokes, because pi is not a fixed point of Phi -> 4 Phi (D1). It inserts a pi vortex line per parent face, so it writes the clock into the rule.
- Even granted, it does not cure (i)-(iii).
- Lopsidedness: none. The sign is symmetric and merges (F1).

What is worth keeping is the face clause without the clock role. It is an energy-forced derivation of CL-1's pi-flux phases from the half-filled sea, so the fixed phases need not be stipulated. That still needs a dynamics (the dissipative roll of B5) and holds only at half filling: the main note's window is filling 0.34-0.66.

## Smuggling review

Supplied:
- hop 1 and half filling;
- the face flux as a dynamical register;
- the path family (separable 2^3 patterns; non-separable patterns not searched);
- the zero-mean gauge (no uniform electric field, which is the Wilson-line degree of freedom);
- the Inglis stiffness as the kinetic term (no link electric term; adding one with coupling g only adds a finite Z, which does not change the order-1 pole, and makes n_s a function of g);
- J a = sqrt3;
- M_P a = 1 at the flat rung;
- N* = 55;
- semiclassical FRW with Hubble friction.

Forced, given those:
- the pi end and its uniqueness of class;
- the monotone landscape and the top's instability;
- the impossibility of a full-surface flux gap;
- the order-1 pole with the van Hove log;
- the quartic class and n_s ~ 1 - 3/N;
- the rung-free quartic coupling and the A_s failure;
- Stokes and the 4-to-1 dilution;
- E(Phi) = E(-Phi).

Not computed:
- the Ohmic friction coefficient of path N, and a warm (dissipative) roll on it;
- interactions (the main note's repulsive theorem covers the end point only);
- non-separable or larger-cell patterns;
- reheating rates;
- quantum diffusion near the top.

## Dependencies

- Used: nested-prefold-sea (R^2 = 1 iff pi flux; CL-1's tick is the KS band; the nested surface; the slow-roll dictionary); fold-inflaton (theorem B, Z ~ m^(d-3); C5 re-seeding).
- On main:
  - HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02 (end-point energies, the 4^3 certificate, Wilson lines, filling window; Lieb 1994);
  - CUBIC_REPULSIVE_FLUX_FIXED_HALF_AND_CANONICAL_TWISTS_BOUNDED_THEOREM_NOTE_2026-09-04 (the pi minimum survives repulsion).
- Narrows: the unification "fold = flux ordering". It is right about the end state and wrong about the clock.
- Open PRs: #9982 (nested-prefold-sea), #9979 (fold-inflaton), #9968 (face-plaquette-law).

## How to run

python3 scripts/the_nested_sea_orders_its_face_flux_to_pi_but_the_flux_fold_is_a_scale_free_quartic_hilltop_and_a_split_cannot_pass_pi_flux_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120. It takes about 19 s, peaks at about 230 MB, prints 5841 characters and ends with TOTAL: PASS=17 FAIL=0. It was checked through scripts/runner_cache.execute_runner from a temporary origin/main worktree (status ok, exit 0).
