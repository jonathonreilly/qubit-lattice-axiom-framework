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

- 20:28Z Section 2 written: eight approaches, each searched on file; seven are on file, T7 is not.

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


## 2. Approaches tested in this row, each against the file

Each line was derived from first principles here and then searched in `library/gap-*.md`, `parts/gap.md`,
`library/open-core.md` and the FINISH rows (`grep -l -i -F`). "Stops" names the first step with no proof.

| # | Approach | Why it could be selective | Where it stops | On file |
|---|---|---|---|---|
| T1 | The centre twist as a discrete stiffness (vortex free energy), carried through scales | A twisted sector of SU(2) has classical action 0 (constant transition functions i sigma_1, i sigma_2). A flux sector of U(1) costs 2 pi^2 beta k^2 at every size in d = 4 | A discrete twist has no Hessian. The best case gives the flux half (string tension), not the neutral gap: a confined theory with a decoupled massless neutral field has all twist ratios near 1 | Lemma CEN and Corollary CEN2 (row 1011, `gap-pinned-cell-gauge-max.md` 4.3); row 1025 ("the flux half at one coupling, not the seed"); (T-vor) of row 1018 |
| T2 | A soft abelian twist about a colour frame, with the bracket (paramagnetic) gain | The bracket is zero for U(1); the shell sum is a logarithm only in d = 4 | A bound by a rigid link map is first order (Jensen). By gauge averaging the cost of a fixed-colour rotation depends on the potential, not on its curl. The gain is second order and needs a Ward cancellation in law | Proposition SEAG and (N1)-(N3) (row 1011, 4.4 and 7.4); Theorem C1 (row 1380); Lemma PRIV and Theorem BD (row 1034); (PARA-COVAR) of row 1526, which check 1527 rejects as a reduction |
| T3 | The time-independent gauge group as a non-abelian exact symmetry of the temporal-gauge chain. Its twist is the temporal link, and it has a bracket | The symmetry is non-abelian for SU(2) only | The direct cost of the twist is the covariant Laplacian of the slice field, not a classical form (the same mass-like term as SEAG). Small stiffness of this twist is the Gauss-law half (static adjoint sources are heavy), not the neutral gap | Proposition A and SEAG cover the Hessian; the reading as a chain symmetry is not on file under this name (grep "Polyakov-loop effective": 1 file). No new statement results |
| T4 | Transport along the coupling from a base seed (Theorem T) | Base reads the group; transport reads the dimension (1.2) | The relative bound of 1.3 at a coupling of order one | row 708 (VIR_K), (VIR-log); rows 1515-1523 (TR2, (ABS-band), (*)); registry RB |
| T5 | Double positivity: Z_+(v; beta) is a Laplace transform in beta and a Gram form in the two halves of the time circle | none by itself | Remark SAND below: the two bounds differ by an extensive term | Lemma SQ (row 1522), Lemma CLIMB (row 1332) |
| T6 | A fundamental Higgs field of fixed length as an infrared regulator; transport in the hopping parameter | For U(1) the path meets the Higgs-Coulomb line | The corner of the plane at weak gauge coupling | R5 and b5 (i) of `gap-crux-exercise2-max.md` L264, L336; I10 of `gap-outside-box-max.md` L146 |
| T7 | Make the replica swap an inner twist of a connected group: Sp(2) with a unit 5-vector field | Section 3 | Section 3.3: the same corner as T6 | The swap as the outer twist of Pin(4): `gap-laptop-solve3-fable.md` L135-139; route COVER of `gap-band-fresh-fable.md` L110-192. The Sp(2) form: not found (grep "Sp(2)", "SO(5)", "outer automorphism": 0 files) |
| T8 | A finite computation at the base | reads the Wilson weight | cost | rows 1326, 1332 (COST, SURF) |

**Remark SAND (PROVED, three lines; no gain).** Put G(beta, beta') = Tr(P_0 T_beta^u T_beta'^u). It is the
neutral partition function of the torus n^3 x 2u with the coupling beta on one half of the time circle and
beta' on the other. So G is a Laplace transform of a positive measure in (beta, beta'), and log G is jointly
convex. G is symmetric (cyclicity of the trace). It is also the Hilbert-Schmidt inner product of P_0 T_beta^u
and P_0 T_beta'^u. Hence, with bbar = (beta + beta')/2,

    Z_+(2u; bbar) <= G(beta, beta') <= ( Z_+(2u; beta) Z_+(2u; beta') )^(1/2).

The left bound is convexity at the midpoint of (beta, beta') and (beta', beta). The right bound is
Cauchy-Schwarz. The two sides differ by (beta - beta')^2/8 times the variance of the action, which is of the
order of the volume. So the sandwich moves a seed only over coupling intervals of length volume^(-1/2). This
is Lemma SQ and Lemma CLIMB again.

**GUIDE for 1.2 (continuum dispersion, two polarizations, no zero modes; not a proof step).** For a free
massless vector field the swap is a reflection in the replica rotation group O(2), so the purity is the
ratio of the charge-conjugation twist: P = product over modes of tanh(u omega/2). At u = n/512 this gives
log P = -(512^3) pi^2/24, about -5.5e7, at every size. SU(2) has no replica rotation.

