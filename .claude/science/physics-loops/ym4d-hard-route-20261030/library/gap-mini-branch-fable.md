lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:12Z

# gap-mini-branch-fable (row 1179): the Wilson branch selection

Research-stage working state. Nothing here grants status. Pinned commit 6a3a26b93.
Every statement below carries one label: PROVED (written proof in this file, not yet checked by
another model), ARGUED, GUIDE (numeric or heuristic, never a proof step) or OPEN.

## 0. Plan (written first, 2026-11-19 21:12Z by `date -u`)

Moves: the wall (W) of row 720, in the exact forms of rows 1175 and 1177
(twist cost o(N^2/log N), or the planar tension test), given a one-cube physical neutral upper bound.

Steps, one per response, each appended here before the next:

1. Read `library/gap-council-synthesis.md`, `parts/gap.md` (methods 1-36, route registry), the FINISH
   RESULT lines of rows 1143-1177, and the two latest files (`gap-solve16-astra62.md`,
   `gap-solve17-astra62.md`). Record the exact statement of the branch selection in Section 1.
2. Repo search and duplicate check (`library/open-core.md`, FINISH rows, cross-branch) for each
   candidate attack, recorded in Section 2 before any attack.
3. Attacks on the selective inequality, each ending in a proof, a disproof or a precise obstruction
   theorem. Section 3 onward.
4. Re-read of every PROVED item, then the RESULT line.

## Status log

- 21:12Z file created; reading inputs.
- 21:13Z read: FINISH rule sections, GOAL.md, `gap-council-synthesis.md`, `parts/gap.md` L1-160 (formulation, methods 19-36, lead rules, obligations to row 1072), FINISH RESULT lines of rows 1141-1178 and the sibling rows 1180 (neutral bound) and 1181 (free method). Row 1178 (gpt-6.2-astra, continue chain on (W)) runs in parallel. Next: the exact statements of rows 1175 and 1177.
- 21:18Z read `gap-solve16-astra62.md` L1-135 (statements (1)-(13)). Section 1 below written from it.

## 1. The statement (from row 1175, `gap-solve16-astra62.md` L59-64; unchecked there)

Fixed bare coupling beta = beta_j, symmetric periodic lattice torus N^4 with 4 | N. Z_0 is the periodic Wilson SU(2)
partition function, Z_14 the one with the elementary centre twist in the (1,4) plane (the sign of the coupling is
reversed on one co-closed stack of N^2 plaquettes), and zeta_beta(N) = Z_14(N^4)/Z_0(N^4).

**Branch selection (BS), OPEN.** At each sufficiently fine fixed cutoff beta_j,

    liminf over N to infinity, 4 | N, of (log(2 + N)/N^2) [ - log zeta_beta_j(N) ] = 0.          (6)

Row 1175 proves (unchecked): given the one-cube physical neutral bound (row 1161's premise, the item of row 1180),
(BS) is equivalent to (W). In the competing branch every nonzero twist obeys
Z_B/Z_0 <= 64 exp(- c_q (N/n_0)^2 / log(2 + N/n_0)) (its (4)); in the periodic branch zeta tends to 1.

Facts used below, all elementary:

- (F1) Trivial area bound: - log zeta_beta(N) <= 2 beta N^2 (the stack has N^2 plaquettes). So (BS) asks for a gain
  of a factor o(1/log N) over the trivial bound, at fixed beta, with constants free to depend on beta.
- (F2) (BS) is a statement at fixed bare coupling and growing lattice volume. It contains no physical scale.
- (F3) For compact U(1) the uniform spread of the flux pi over a (1,4) torus gives - log zeta <= beta pi^2/2 for
  every N and every beta (Jensen with the shift theta_p -> theta_p + pi/N^2; the odd term vanishes by charge
  conjugation). So (BS) alone holds for compact U(1): it is not the selective statement. The selective content of
  (W) then sits in the neutral premise (row 1180's item). This agrees with the row's remark that every positive
  result so far is non-selective.
- 21:33Z read `gap-solve17-astra62.md` in full (planar tension test (7), bounds (14), (25), (26), obstruction (33), (35)). Section 2 written.

## 2. Where blind derivations land (no new claim in this section)

Before reading row 1177's spreading sections I derived the following by hand. Each one is on file, so none is
claimed here.

| Blind derivation | On file |
|---|---|
| Jensen with fixed (configuration-independent) insertions at half-links gives, after gauge averaging at each plaquette corner, the cost beta <w_p> sum_p [1 - eta_p prod_corners cos c], and a per-site parity constraint forces order one cost per transverse site: area law | thin-stack and Mack-Petkova stack bound, row 1175 (12), (14); row 1177 L32 |
| A spread vortex with a field-built colour axis pays beta a^2 abs(D n)^2, and abs(D n)^2 is at least c/beta on typical fields: area law with a coefficient independent of beta | row 1141 (2); row 1177 (14), (26), obstruction (33)-(35) |
| The exact sewing identity (1-z)/(1+z) = E_nu prod tanh(J_x) | row 1147 (16)-(19); row 1177 (24) |
| Twist = ratio of the weights of the two SO(3) bundle classes; frozen Q_8 has twist eaters and ratio 96/736 | rows 737, 744, 878, 1130 (counts 736, 96) |
| The 2D reading of the planar test: sigma_beta(w) is about 2 exp(-F_v(w)), F_v the free energy of one vortex spanning the transverse w x w torus | row 1177 (8), (13), the Z_2 plane model at L361 |
| Renormalization-group spreading gives at best an area law with coefficient about xi(beta)^(-2), and the competing branch allows a vortex tension that small | consistent with row 1177 (25), (31); set-aside method 23 |

Reading of the state (ARGUED): at fixed beta every first-moment or quadratic comparison is an area law in the
width (row 1177 (33)). (BS) asks for less than area by more than a logarithm. In a hypothetical competing branch
the vortex tension in physical units is at most of order (seed size)^(-2), far below what ultraviolet control can
exclude. So no argument that reads only scales below the seed size can select the branch.

## 3. Candidate: branch constancy along a path of couplings (to be checked against the lane before any claim)

Idea. Both branches are certified by finite-volume strict inequalities (a seed with margin q at one size, improved
by Theorem S at larger sizes), which are open conditions in the coupling. They exclude each other. Row 1161 says
that the neutral premise forces one of them. So on any connected set of couplings where the neutral premise holds,
the branch is constant; at strong coupling the branch is the periodic one. Then (BS) at beta_j would follow from the
neutral premise at every beta in (0, beta_j], with no flux input at all. Next step: grep the lane for this argument
(continuity method M5, (NOCRIT), carry rows 978, BR-3), then write it as a theorem with exact hypotheses, or name
the match and drop it.

Status of Section 3 (21:41Z): **the candidate is on file. Match: Corollary R6 of row 737 (`gap-means-max.md` 4.7,
"the flux phase cannot change while an even seed exists; argued, the continuity step is not written with
constants"), with the continuity method (M5) of the same file (2.5), Lemma CONT of row 1072
(`gap-bridge-exercise-opus.md` 3.2) and (NOCRIT) of row 709.** Not attacked as new. What R6 gives in the present
notation: (BS) at beta_j follows from the fixed-coupling neutral premise at every beta in (0, beta_j]. The closed
half of the method (the premise on the whole interval) is the lane's "no transition on the path", which is the
target again ((M5): absent, counterexample in the class).

Two paths other than the Wilson axis, checked by hand here (ARGUED, belief-grade inputs on the phase diagram):
- the mixed fundamental-adjoint line of constant beta_F + (8/3) beta_A from the pure adjoint axis (where zeta = 1
  identically) crosses the Z_2 first-order line near beta_F = 0.44 at large beta_A, so the neutral premise fails on it;
- the one-plaquette weight 2 cosh(beta w_p + gamma), gamma from 0 (twists free, zeta = 1) to infinity (Wilson):
  in the monopole-free approximation its twisted partition functions are the convolution over H^2(T^4; Z_2) of
  the Wilson twist sectors with those of the Z_2 gauge theory at coupling gamma, so it carries the Z_2
  transition at gamma near 0.44. Both paths are worse than the Wilson axis.

## 4. Is the branch selection on the path to the Jaffe-Witten gap? (question raised 21:41Z; reading next)

Observation to test against the lane's files: in BOTH branches the selected seed (Z or V) contains the periodic
centre-neutral sector. So the neutral premise alone should give the gap of the centre-blind sector at every larger
size (Corollary R4 of row 737 says this for the even seed (ES)). The Jaffe-Witten gap concerns local gauge-invariant
observables, which are centre-blind. If the consumer (Propositions P, P' of `gap-seed-limit.md`) reads only that
sector, then (BS) is needed for (W) as worded (flux sectors included) and for confinement, but not for the
Jaffe-Witten gap. Row 1052 (Lemma FLUX-W, target T_JW-lat) and its checks 1054, 1055 are the place to compare.
