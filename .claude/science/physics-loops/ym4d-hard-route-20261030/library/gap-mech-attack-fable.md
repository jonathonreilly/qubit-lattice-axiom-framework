lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-26T07:53Z

# Row 1529, gap-mech-attack-fable: solve brief on the selective mechanism

Started 2026-11-25T19:53Z (date -u). Pinned commit e7c98d99e, branch claude/ym4d-hard-route. Author: Claude Fable 5.2
(Anthropic), high effort, Mac mini worker 1. Not yet checked by another model. Research-stage working state; no
public claim.

Machine: memory_pressure reported 37 percent free at the start, below the 50 percent floor. No numeric job is
started unless this changes; work is by hand.

## 0. Plan (written first, per the save protocol)

1. Read the seed statement and its consumer (library/gap-k2-tool-design-fable.md 3.1, lean/gapchain), rows
   1378, 1386, 1442, 1443, and the RESULT text of rows 1510 to 1527.
2. List the candidate selective inputs. For each: the 4D U(1) test, the 5D SU(2) test, the Villain test (row
   1442 Proposition VIL), the K7 test, and a grep of library/open-core.md and the FINISH rows.
3. Push the best candidate. Write each stage here before thinking further.
4. End with the exact stopping statement, why it is not equivalent to the seed, and why it is selective.

## Status log

- 2026-11-25T19:53Z file created, plan written.

- 20:13Z Section 1 written (frame; nothing new in it).

<!-- LOG-END -->

## 1. The frame used in this row

Marks: PROVED (by hand here, checked by no one), ON FILE (with the anchor), ARGUED, OPEN, FAILS.

### 1.1 The target in the two channels

Notation of `library/gap-k2-tool-design-fable.md` 3.1. E_i are the neutral levels of H = -log T on (Z/n)^3,
E_0 the vacuum, m = E_1 - E_0, s(u) = sum over i > 0 of exp(-u (E_i - E_0)).

- (a) ON FILE (Fact PUR; Lemma B of row 1515): P_K >= 457/625 gives s(u) <= 4/21, and
  log(1 + s(u)) <= -log P_K <= 2 log(1 + s(u)). So the seed is a bound on the neutral thermal sum at the
  temperature 512/n. In one number: the dimensionless neutral gap z = n m must be large against 512.
- (b) ON FILE (Theorem S, `library/gap-crux-restate.md` 3.4; Lean `wilson_theoremS`, row 1525): at one fixed
  coupling a seed at one size gives a gap on all larger dyadic boxes. So the lane already has a finite-size
  criterion in law at fixed coupling. What is missing is uniformity along beta_K.
- (c) Crossed channel (the torus algebra; ON FILE as the flux formalism of `gap-flux-exercise.md` 3.0-3.1, twelve
  files use "crossed channel"). Read direction 1 as time. Then
  Z_+(v) = (1/4) sum over m in Z_2^2 of Tr over H_m(n, n, v) of (P' T'^n).
  H_m is the state space of the box n x n x v with magnetic twists m in the planes (0,2), (0,3). P' projects
  on even electric flux along the short side. So the seed is the pair: the magnetic twists of the thin box
  are degenerate, and its vacuum energy is additive in v between u and 2u (no Casimir term).

### 1.2 Where selectivity has to sit (ARGUED; the reading is Remark PAIR of row 1386)

- Compact U(1), d = 4, Coulomb side: free photons have z = 2 pi at every size. The seed fails at every size,
  so every transport statement of the form "a seed at beta_w gives a seed at larger beta" is vacuous there.
  The group-reading input is the base seed.
- SU(2), d = 5: a base seed exists on the strong side of the bulk transition and none on the weak side. So
  the transport along the coupling is the dimension-reading input.
- Hence a proof needs both: a base that fails for U(1), and a transport that fails in d = 5. Theorem T of row
  1332 has this form ((KER) and (A2)).

### 1.3 The transport in one line (ON FILE: row 708 (VIR_K); row 1517; Feynman-Hellmann in 20 files)

Write T(beta) = exp(beta W/2) K_beta exp(beta W/2), W = sum over spatial plaquettes of (1/2) tr U_p, K_beta the
product over links of the convolution with exp((beta/2) tr g). Then for a normalized eigenvector psi_i

    - dE_i/dbeta = <psi_i, W psi_i> + Re <e^(beta W/2) psi_i, D e^(-beta W/2) psi_i>,   D = sum over links of d_beta(Casimir) >= 0.

The first term is the spatial action insertion, the second the temporal one. The transport statement is a
relative bound: the action insertion of a low neutral level exceeds that of the vacuum by at most kappa times
its excitation energy, with kappa below about 4.0 (one loop: 2.69). In continuum words: the trace anomaly as an
inequality. Free photons have kappa = 0. Nothing in this row proves it at a coupling of order one.

