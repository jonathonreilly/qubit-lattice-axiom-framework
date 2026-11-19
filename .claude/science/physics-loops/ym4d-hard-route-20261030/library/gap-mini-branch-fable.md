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
