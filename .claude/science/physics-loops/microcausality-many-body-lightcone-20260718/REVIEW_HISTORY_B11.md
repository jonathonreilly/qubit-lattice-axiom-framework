# Review history — block11 (graph-metric class + d = 3 discharge)

## Round 0 — workhorse worker grading (two Opus 4.8 max workers)

Ground truth recorded in BLOCK11_PLAN.md before reading either
deliverable. Both workers graded CORRECT on every item:

- **Scout (adversarial metric audit):** block07's load-bearing chain
  (activity definition, chain lemma, weight split, meeting bound,
  peeling, assembly, display, velocity, fermionic lift, no-go
  disposition) verified metric-agnostic step by step with quotes; the
  naive "only the declaration binds Z^3" claim REFUTED (slack ladder
  + kappa_3D are Z^3 incidence facts — adopted into the note's
  honesty rows); the dispersion note confirmed one-particle-only,
  even-periods/torus carrier, 2^d taste corners (p_r = k + pi r),
  E_d display, native C_d kernel bound with eta < arcsinh(m), parity
  rule, r_d = arcsinh(m)/(2d) remark; block10's two open-item
  sentences located verbatim (became runner needles N3).
- **Math worker (torus + assembly):** (Z/6)^3 l1 spheres 6/18/35 vs
  Z^3 6/18/38 with the first deficit exactly at r = L/2; l_inf
  (Z/8)^3 26/98/218 = 24r^2+2; conversion d1 <= 3 d_inf descends;
  coordinatewise |a|_L <= |a| => kappa_torus <= kappa_ambient term by
  term; factor tracking "FLAG: NONE" (2 and a_tau dimension-blind; d
  enters only inside E_d's argument); the block10 wrap term has
  torus diameter 1 — the open-boundary restriction was an artifact
  of the ambient metric on an open embedding (became the note's
  "dissolves" paragraph, with the exhibit's correctness for the open
  embedding preserved); flagged the lightcone-wrap caveat (torus
  distances bounded) — adopted verbatim into Results and N7
  steelman (b).

Supervisor-added content beyond the workers: the position-space
single-mode-per-site argument (taste = cell-transform momentum
labels => scalar-fiber pair family, no fiber factor at U = 1), and
the no-CT-dependency observation (the dispersion note's C_d bound is
native at U = 1).

## Round 0.5 — first runner pass + battery

Runner 17/0 on first pass (G1-G10 + N1-N7 under the ordered label
manifest). Battery: 12 probes in scratchpad copies with ROOT pinned,
each attacking one ASSERTION (torus counts, seam diameter, chain
lemma direction, radicand term count, taste sign, the 2 a_tau
factor, the d-increment, the 585 instance, the threshold direction,
a needle's meaning, and a silent gate deletion vs the manifest) —
12/12 flip exactly their target. Self-subtraction scan of symbolic
gates: none (G7 compares exp/log round-trip vs direct construction;
G8/G9 compare distinct substitutions/expansions).

## Round 1 — combined adversarial lens (codex, cross-family)

Spec: `lens_b11_spec.md`. The raw lens transcript was NOT landed
(review-loop dropped it: 419 KB of reviewer stdout that duplicated
repo governance documents verbatim, embedded a machine-local
worktree path, tripped `git diff --check`, and replayed its
pre-repair findings as if current — the dispositions below are the
durable record). One BLOCKER, six MAJORs, three MINORs — all
repaired:

1. **BLOCKER: finite-torus aliasing.** The dispersion note's kernel
   bound is for the INFINITE-lattice Fourier coefficient; the torus
   kernel is the alias sum h_L(z) = sum_n h(z + nL), so the
   same-constant claim was FALSE. ACCEPTED and repaired natively:
   the alias lemma is now a Results display (DFT identity gated
   exactly on a finite-support toy where the naive restriction is
   exhibited wrong — G11), the geometric input ||z+nL||_inf >=
   max(L||n||_inf - L/2, ||z||_inf,L) enumerated, and the explicit
   alias constant A_3(beta) = 1 + 2 sqrt(u)(13+10u+u^2)/(1-u)^3
   (the SAME landed shell generating identity; finite-N telescoping
   gates — G12) with the rate split eta -> eta' < eta. The theorem
   restated with K_L = C_3 A_3((eta-eta')L) and mu < eta'/3. An
   end-to-end d = 1 torus instance gated (exact DFT of the actual
   E_1 symbol, exact parity zeros, 50-digit bound margins — G13).
2. **MAJOR: construction status / C = 1.** ACCEPTED: the many-body
   d-dim object is a CONSTRUCTION under the vacuum normalization
   convention (d-dependent scalar not excluded, drops from
   commutators); "closure"/"C = 1 inherited" language replaced; the
   action-level identity named open (claim_scope, Results,
   Non-Claims, N5/N6/N7).
3. **MAJOR: G10 false universal quantifier.** ACCEPTED: thresholds
   are per-chosen-eta; G10 rewritten with an interior-eta instance,
   a rejector, and the lens's own false-universal exhibit gated.
4. **MAJOR: G8/G9 assembly honesty.** ACCEPTED: with the alias
   gates added the assembly now has real native gates; the
   Verification section rewritten to say what each gate kind does
   and does not establish ("exact throughout" phrasing dropped).
5. **MAJOR: N2 needle label vs content.** ACCEPTED: taste-corner
   degeneracy sentence and p_r = k + pi r needles added; the mode
   count (L/2)^d 2^d = L^d added as a symbolic gate (G7); N7
   relabeled a self-pin (anti-drift, not evidence).
6. **MINOR: G4 scope.** ACCEPTED: relabeled instance illustration.
7. **MAJOR: note N2/N3 gate quality.** ACCEPTED: N2 rewritten as a
   pairwise wall table (including the split/alias parameter); N3
   now names the aliasing wall as review-found and repaired.
8. **MINOR: two-site-cell misnomer.** ACCEPTED: fold-by-two in
   every direction (2^d-site cell); the source's own "two-site-cell
   corners" phrase contextualized.
9. **MAJOR: "already landed" false.** ACCEPTED: provenance split —
   dispersion + RP notes on origin/main; blocks 07/08/10 are stack
   dependencies pending merge (Purpose + Non-Claims).
10. **MINOR: "bridge-campaign" vocabulary.** ACCEPTED: purged from
    the note (PR-linkage lives in the PR description only).

Lens-confirmed survivals: the graph-metric proof, quotient-metric
triangle inequality, torus sphere counts, seam diameter,
d1 <= 3 d_inf, mode count, scalar position-space fiber, Gamma
factor algebra, wrap caveat, no-audit-verdict boundary.

## Round 2 — landing race re-anchor

While block11 was in build, the owner landed the ENTIRE stack
(blocks 03-10) on origin/main as REWRITTEN notes (PR #5527 closed =
landed via the reviewer's own condensation; branches deleted). The
lens's Finding 9 ("not landed authorities") was thereby overtaken by
events, but the deeper consequence was needle/framing drift: the
landed block07 keeps the identical chain as displays (1)-(7) in
tighter prose; the landed block08 keeps the identical feed (variable
q, display (6), numerator (7), 585 at q = 1/2); the landed block10
is pared to the finite-mode functor theorem + free-corner
composition and DECLINES all activity claims, naming the missing
prerequisites: "A one-particle locality estimate cannot be fed into
a many-body bound until the operator identification and boundary
convention are both supplied." Block11 re-anchored per the house
rule (re-anchor at landing time; judge by content-on-main): fresh
branch from origin/main, all sibling needles retargeted to landed
sentences (verified present before editing), the framing changed
from "answers block10's two open items" (stack-draft sentences that
no longer exist) to "supplies the landed corner-note's two named
prerequisites and assembles the d = 3 feed", and the
open-boundary-restriction story corrected (the landed block10 has
no restriction to dissolve — the torus class IS the missing
boundary convention). Runner re-run 20/0 against landed texts.

## Post-repair state

Runner 20/0 under the ordered label manifest (G1-G13 + N1-N7),
needled against the LANDED sibling texts. Battery regenerated from
the final runner: 16 probes, each flipping exactly its target
(incl. the alias law, the alias-constant identity, the parity
zeros, the geometric-inequality strength, the threshold rejector, a
needle-meaning attack on the landed corner-note sentence, and a
silent gate deletion vs the manifest).

## Round 3 — independent review-loop (landing pass)

Run by a separate review-loop worker with a cross-family reviewer
seat, against the PR head rebased on `origin/main`. The claimed
"16/16 battery" above did NOT cover the headline constants: an
independent mutation battery showed the runner still printed
`PASS=20 FAIL=0` after replacing `A_3`'s `2√u` by `2u`, after
changing `A_3`'s numerator `13 → 14`, and after changing `C_d`'s
`(d−1)` offset to `(d+1)`. The formulas themselves survived
independent re-derivation (brute-force shell enumeration of
`N_d(j)`, `A_3`/`A_1` matched to 12 digits at five `β`; the
geometric input verified exhaustively at `d = 3`, `L = 5..8`
including odd `L`; the alias identity cross-checked against
numerical quadrature of the infinite-lattice kernel; block08's
`κ_bar/K = 585` recomputed by brute force; block07's chain lemma
verified on random weighted graph metrics) — so the repair was to
the GATES, not to the science: `G8` now pins the `(d−1)` offset at
`d = 1` and derives its `C_3` instance by substitution, and `G12`
adds a half-integer shell pin that fixes the `√u` and the numerator
coefficients. All eight previously-slipping mutations now fail.

Claim narrowing applied in the same pass: the note no longer says
it supplies BOTH of the landed corner-note's prerequisites. Only
the boundary convention is supplied; the operator identification is
replaced by a construction, and the Lieb-Robinson display is scoped
to the constructed `dΓ(h_{3,L})` — the finite-torus kernel, i.e. the
alias sum of `h_3`. Three factual misattributions to the
landed corner-note were corrected (it has no open-boundary
restriction and no open-embedding exhibit; it proves the canonical
intertwiner natively and does not cite the RP-positivity note; it
carries no `a_τ` reconciliation), the bare `block09` label was
replaced by the sibling note's name, and block08's own
"no periodic-graph extension" boundary was disclosed. The
`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE` was
removed from `upstream_dependencies` and de-linked, since nothing
here rests on it.

## Round 4 — reviewer confirmation pass (same seat, scoped)

The reviewer re-read the narrowed state and returned
`LANDABLE AS NARROWED: NO` on four surviving items, all repaired
before landing:

1. Two sentences (the corner-note dependency role and the N8
   prior-wall echo) still read "two prerequisites this note
   supplies". Rewritten to "supplies ONE, replaces the other with a
   construction, so the corner-note's wall stands".
2. The new Non-Claim had regressed to `dΓ(h_3)` for a finite-torus
   object. Corrected to `dΓ(h_{3,L})` throughout, and the
   construction display now says explicitly that on the torus the
   same mode-by-mode functor is applied to `h_{d,L}`.
3. `G12`'s half-integer pin was a finite-`N` truncation test only:
   adding a `u^6` numerator term to `A_3` or `A_1` still passed.
   Closed with the EXACT identity
   `A_d − 1 = u^{−1/2} × (integer-power shell generating function)`,
   which forbids an extra numerator term at any order. Both `u^6`
   mutations now fail.
4. `G14` hardcoded the weight factor `4` and the diagonal `1` on
   both sides, so changing both copies passed. Restructured into two
   decoupled halves: the shell-count domination now carries NO
   weight factor at all, and the weights are DERIVED from the
   constructed objects (number of operator terms in `h_{xy}`,
   support sizes) and must reproduce the CITED closed-form display
   `1 + 8x(13+10x+x²)/(1−x)³`. A wrong envelope factor, wrong
   support size, dropped diagonal, or altered shell count is now
   rejected by the landed note's own `8`.

Runner 21/0 after the repairs; every mutation the reviewer named as
a false PASS now fails.
