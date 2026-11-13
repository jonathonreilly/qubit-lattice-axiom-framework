# Two-plaquette marginal coercivity: repo and literature record

2026-11-09. Read-only extraction plus this source record, in Luna's detached
checkout `551840d63d189573688c763445b2eff9f99559d1`; current `origin/main`
was freshly fetched at `bf92a1d763030836ed55631d5d7a7ef3b288f284`. PR #10149
is open at the checkout head; prior PR #10133 draft `89faef229ff6e6bde42baad15ed8270c2f4087d8`
is provenance only. No Git mutation, commit, push, proof attack, or
scientific status change was performed; Git inspection below is read-only. This is a targeted source search, not
an absence or novelty proof.

## Exact target and nearest repo supplier

Target: for odd `L>=3`, `kappa>0`, finite four-dimensional torus with terminal
side `m>=3`, terminal identity and zero sources, integrate the seven distinct
terminal links `J` of two elementary plaquettes sharing an edge. Keep the
actual normalized paired-root-leg means. On the same terminal-root fine
forest slice (all intermediate links retained), establish

    sum_retained [1-w(a_e)] <= C(L,kappa) E_J,
    E_J = W0 + kappa sum_all gamma0,c + kappa sum_(c outside J) gamma1,c,

uniformly in volume, position and coplanar/hinged geometry, including zero
means. Only the exact last-layer kernels for `J` may be integrated out; every
normalizer for the remaining kernels stays in the conditional law.

The closest proved-in-note mechanism is [one-step compact path filling and
centered-gap coercivity, CUT_SECTOR_COERCIVITY_ASTRA CS7–CS12](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/89faef229ff6e6bde42baad15ed8270c2f4087d8/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/CUT_SECTOR_COERCIVITY_ASTRA.md#L145-L233), exact source SHA-256
`4e6c70786aa4458293c4fe7294767128253477176f9eea87b7720254d62a159e` at
that draft. It proves a compact nonlinear link-to-curvature estimate using
actual path words, a maximal-tree gauge, Wilson plaquette cost and centered
kernel mismatch; arbitrary terminal holonomies are retained. Its local
version explicitly requires complete filling/phase supports in the paid
reader sets (CS12). It is one-step, not the present two-step SU(2) marginal.

The closest two-step composition is [compact-energy-coercivity.md, §§1–6,
lines 20–45, 69–105, 107–160, 165–235](../parts/compact-energy-coercivity.md),
SHA-256 `7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa`.
It proves the desired summed forest-link bound when **all** terminal
`gamma1,c` terms are paid. Its step (7) uses each terminal edge's own gap to
control its straight root-to-root transporter; step (8) passes that control
to fine transport; steps (9)–(11) sum it. Therefore it does not directly
prove the target after deleting seven `gamma1,c` terms. This precise mismatch
is the outstanding bridge: replace each missing root-to-root constraint by a
bounded detour/path argument using retained terminal constraints and the
already paid lower-level terms, with an explicit volume-uniform multiplicity
bound, or find a counterexample. No such bridge was found in the searched
material.

Exact marginal bookkeeping is already derived in [partial-terminal-normalization.md,
§§1–2, lines 26–80](../parts/partial-terminal-normalization.md), SHA-256
`722e622dd64763e7f85461ef037f78810ec1c96d5bb71ddc7d60647c858b9867`.
Integrating `J` deletes each full normalized last-layer kernel by its exact
Haar integral in numerator and denominator; all surviving terminal kernels
and their input-dependent radial normalizers remain. Thus the energy
comparison must apply to precisely the held-outside-`J` law above.

The related [released-terminal gauge-directions.md, §§2–4, lines 42–79,
94–128, and concrete witness lines 130–end](../parts/released-terminal-gauge-directions.md),
SHA-256 `a8271fb33178da46f747075f8b98f266cb06833ae900b99ef0544f36adcb403b`,
proves exact residual component gauge symmetry and a `3(r-1)`-dimensional
null family on the unchanged forest slice. Its example releases **all eight**
terminal edges incident to one vertex. It expressly says that this does not
settle the seven-edge two-plaquette case. For the target, connectivity of the
retained terminal graph would remove this particular component-mode witness,
but would not itself prove quantitative coercivity or rule out other soft
modes.

`SOURCE_MAP.md` lines 33–34 and `PROOF_TREE.md` lines 132–153 independently
name this exact missing supplier. PR #10149's body says the seven-edge
quantitative denominator remains open; #10133 is an earlier draft and was
not treated as authority. Among the directly relevant PRs checked, neither supplies an additional
seven-edge estimate beyond the source record above; this was not a repository-wide
open-PR inventory.

## Literature search and scope

Searches run on 2026-11-09 for primary material with these variants:

- `lattice gauge theory axial gauge plaquette action tree gauge fixing compact group coercivity theorem`
- `lattice gauge theory path filling plaquette holonomy bound lattice Poincare inequality compact group axial gauge`
- `finite graph compact group gauge fixing spanning tree holonomy estimates plaquette Wilson action inequality`
- `lattice gauge Poincare inequality plaquette holonomy tree gauge`, including non-Abelian/compact Wilson-action variants and sparse-removed-constraint terms.

The nearest accessible primary source located is J. Dimock, [“Covariant Axial
Gauge” (2014)](https://arxiv.org/abs/1410.2798). I inspected its full-text
HTML, especially §§2.1–2.2 (lines 20–110): on a finite cube for an **abelian
real-valued** gauge field, Proposition 1 states that tree or averaged axial
gauge fixing plus zero curl yields a coercive quadratic estimate
`||dA||^2 >= C(L)||A||^2`. It motivates tree gauge fixing and finite-volume
curl control. This is not a compact SU(2) holonomy estimate, has no nonlinear
centered mean gaps, no two-step kernels, no torus winding issue, and no sparse
removed set of terminal constraints. Its later torus/RG discussion does not
supply the target statement.

The search also surfaced standard maximal-tree/axial-gauge descriptions and
Bałaban's lattice gauge renormalization papers, but the accessible material
inspected did not state the needed finite-holonomy coercivity with sparse
missing terminal constraints. No applicable compact-group Poincare theorem,
finite-holonomy filling estimate for this marginal, or sparse-removal lemma
was located in the targeted queries. This is a bounded search result, not a
claim that no such theorem exists. No external result is used as proof.

## Search boundary

Read in full the closest two-step coercivity proof and released-terminal
gauge-directions proof; read the exact normalization sections listed above;
read the relevant source map/proof-tree windows. Read PR #10149 metadata/body
at the exact head and the earlier #10133 draft provenance; no broad PR inventory
was attempted. Read Dimock's
primary text at the stated sections. Search scope was limited to these target
records, their named suppliers, the directly relevant open PR(s), and the
queries above; unrelated repository material and an exhaustive literature
survey were not attempted. The subsequent proof attack must begin from the
missing seven-constraint bridge identified above.


## Broader repo and open-PR sweep

This follow-up remained read-only. Full grep outputs were saved under `/tmp`
for bounded inspection; they are not repo artifacts:

- On exact `origin/main` `bf92a1d763030836ed55631d5d7a7ef3b288f284`, searched
  `docs` and `.claude/science` for `missing (terminal|constraint)`, `removed
  constraint`, `sparse constraint`, path-filling, compact coercivity,
  centered-gap, punctured-coercivity, two-plaquette coercivity and terminal
  detour variants (`/tmp/two-plaquette-main-grep-20261109.log`). One hit was
  an unrelated admissibility note's “missing terminal obligations.” A second
  targeted set matching plaquette filling/tree-gauge/coercivity and path-fill
  holonomy terms over `docs`, `.claude/science`, and archived notes returned
  zero (`/tmp/two-plaquette-targeted-doc-grep-20261109.log`). `git grep -l`
  for `axial gauge|maximal tree` over current-main `docs` also returned zero.
- A broader docs filename sweep returned possible phrase matches, not candidate
  theorems. Read the matching mechanism windows in
  `ACTUAL_INPUT_ENERGY_AND_ORIGINAL_MARK_POWER...` (lines 95–117, 445–455),
  `EXACT_GAUGE_WARD_RESPONSE_IDENTITIES...` (lines 50–65, 140–185),
  `FIXED_COUPLING_HAAR_VILLAIN_FULL_SCORE_GAUSSIAN_MAXWELL_LIMIT...` (lines
  298–318), and `MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE...`
  (lines 70–130). The first concerns signed plaquette-row fillings of
  commuting angle words in a different matter/charged preparation; the Ward
  and Maxwell notes use real/abelian link-angle or U(1) Villain cochains; the
  last controls loop fillings for noncompact covariance and compact U(1)
  defect ratios. These are methodological analogies only. None estimates
  compact SU(2) two-step forest coordinates from the specified centered gaps,
  none deletes a sparse set of terminal constraints, and none is imported.
  Relevant log: `/tmp/two-plaquette-doc-claim-lines-20261109.log`.
- Historical proof-name sweep found no CUT supplier on current main: the
  `CUT_SECTOR_COERCIVITY_ASTRA.md` path is absent at `origin/main`. At prior
  draft `89faef229ff6e6bde42baad15ed8270c2f4087d8`, read its exact CS7–CS12
  and local-support clauses in lines 145–235 and the matching review row
  (`REVIEW_CUT_SECTOR_COERCIVITY_ASTRA.md`, line 31). This is the same
  one-step compact path-filling supplier discussed above; it is on the
  historical draft, not a current-main theorem. Log:
  `/tmp/two-plaquette-archive-cs-grep-20261109.log`.
- At the same prior draft, read HOLEPAY's definition and conclusion, not its
  helpers: source blob `73c428de6d113c689e7612116167079ede0eabec`. Its
  lines 31–70 define holes as connected components of the complement of an
  active mask in a face graph for an all-history RG activity; lines 124–145
  charge failed bad-block components using their interior plaquettes; lines
  538–543 leave the same-law integrated history estimate HP14 open. Thus
  “hole” means RG mask/complement components, not deleted terminal output
  constraints in `J`. It is not a stronger supplier for this target. Related
  `RECOVERY_ALIGNMENT_ASTRA.md`, `RECOVERY_CLUSTER_ASTRA.md`,
  `RECOVERY_UIR_ASTRA.md`, and `REVIEW_HOLEPAY.md` headers identify other
  YM construction/route-recovery work; no statement match was found. They
  were not treated as proof inputs. A neutral phrase sweep of that old YM folder
  for `unused axis/direction`, `fourth axis/direction`, `transverse detour`,
  and missing/removed terminal constraints found only the unrelated fourth
  direction identified as Euclidean time in `MASS_GAP_CROSSOVER_REDUCTION.md`
  lines 35–39 and “missing terminal term” in the N5B Markov covariance review
  (its criteria lines 8–18 define this as the omitted terminal covariance, not
  missing link constraints). No unused-axis detour or terminal-constraint
  recovery statement appeared in that bounded sweep; this reports coverage,
  not novelty. Log: `/tmp/two-plaquette-oldlane-neutral-grep-20261109.log`.
- GitHub read-only issue search, restricted to open PRs in this repository:
  `"compact coercivity"` returned only #10149; `"path filling"` and
  `"missing terminal"` returned none. A broader
  `(path-filling OR "missing constraints" OR "removed constraints" OR
  terminal)` query returned #10149, #10114, and #10142. Read #10114's body:
  it reports chart-conditioned two-step control but explicitly leaves the
  compact complement open. #10142 is about finite Bell/gauge link models;
  its “two plaquettes” wording is unrelated. Neither supplies the target.
  PR #10133 remains draft provenance. Search results and inspected metadata
  are bounded to those queries; this is not an exhaustive review of every
  open PR.

Commands used for the repo pass were `git grep` / `git ls-tree` / `git show`
against immutable refs, with outputs saved in `/tmp/two-plaquette-*-20261109.log`;
no worktree content was changed beyond this source record.
