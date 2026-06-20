# Exercise Three — Literature proof search (ABJ identification walls)

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` • **Slug:** abj-walls-break
**Slice:** Exercise Three (literature proof search) • **Date:** 2026-06-20
**Network:** available (`--web`; arxiv.org reachable, WebSearch + WebFetch used)
**Posture:** find canonical proof patterns that map to the three walls' OPEN rays
(P-REC single-taste selector R4; P-COMP template existence; P-ABJ χ≠0/Q≠0
internal background, taste-singlet Adams/overlap index, non-abelian cohomology).
Every external result is flagged with its **import risk** under the repo's
no-new-axiom / no-new-primitive rule (`PRIMITIVE_REGISTRY_CHECK.md`,
`review-loop/SKILL.md`). None of these is an `A_min` derivation; the win is to
see (a) which wall a known theorem could *retire as a bounded import*, (b) which
known no-go *sharpens our own citable wall*, and (c) which precise hypothesis of
a known theorem is the exact thing `A_min` fails to supply (= the wall, named).

Framework refresher read for this slice (stated per mandate):
`docs/MINIMAL_AXIOMS_2026-06-05.md`; `PRIMITIVE_REGISTRY_CHECK.md`;
`docs/audit/data/axiom_premise_nodes.json` summary + `tier_a_admissions.json`
(READ-ONLY); `docs/ai_methodology/skills/review-loop/SKILL.md`;
`docs/repo/CONTROLLED_VOCABULARY.md`. Walls + bankability:
`.claude/science/exercises/abj-walls-break/EXERCISE.md`;
`docs/ANOMALY_FORCES_TIME_ABJ_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`;
in-flight `GROUNDING_MAP.json` (branch + note + blueprint maps, incl.
`routes_already_tested` / `routes_still_to_attempt` — used to avoid re-proposing
pruned routes).

---

## 0. How the literature lands on each wall (one-paragraph orientation)

The single most important literature fact for this campaign: **the staggered
chiral index is NOT zero in general — it is zero only on the flat / equal-
sublattice / topologically-trivial backgrounds that `A_min` happens to supply.**
Adams (2009–2011) proved a *bona fide* Atiyah–Singer index theorem for staggered
fermions: away from the continuum limit the would-be zero modes have definite
chirality and the index is fixed by gauge-field topology. The repo's own retained
no-gos (`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO`, `ABJ_RESIDUAL_GW_NOT_NECESSARY`)
are *exactly consistent* with Adams: they show the index vanishes on the
balanced even torus with arbitrary U(1) links, and they re-target the residual to
"exhibit a χ≠0 or Q≠0 background." The literature says where such backgrounds
live: (i) **gauge topology** Q≠0 (Adams spectral flow), and (ii) **gravitational
/ geometric** χ≠0 via the Kähler–Dirac formulation (Catterall–Butt), where the
anomalous U(1) phase depends *only* on the Euler characteristic. So P-ABJ-internal
and the P-REC R3a re-target are the SAME literature object, and the wall is
precisely "`A_min` (Lattice = flat cubic `Z^3`; `kinetic_isotropy` time edge ⇒
flat `Z^4`) supplies neither Q≠0 nor χ≠0." That is a clean, citable wall — and
also the precise hypothesis to challenge (Section 6).

---

## 1. PATTERN A — Staggered taste → Dirac reconstruction & the spin-taste basis

### Source A1 — van den Doel & Smit; Gliozzi (spin-taste / flavour basis, foundational)
- **Source.** van den Doel & Smit, *Nucl. Phys. B228 (1983) 122*; Gliozzi,
  *Nucl. Phys. B204 (1982) 419*; clarified by Kilcup–Sharpe and by
  *"On the flavour interpretations of staggered fermions"*
  (Nucl. Phys. / ScienceDirect 0370-2693(86)90334-5). Transfer-matrix spin-basis:
  Caracciolo et al., [arXiv:1210.1786](https://arxiv.org/abs/1210.1786).
- **Problem.** Reorganize the 16 one-component staggered modes on a `2^4`
  hypercube into 4 Dirac "tastes": the explicit unitary that maps single-component
  staggered fields to a (spin ⊗ taste) `M_4(C) ⊗ M_4(C)` block, with `γ_μ ⊗ 1`
  the spin Dirac matrices and `1 ⊗ ξ_μ` the taste generators.
- **Premises.** Free or smooth gauge background; blocking to the doubled
  (`2a`) hypercube; hypercubic symmetry mixing spin↔taste; full
  `SO(4)_rot × SU(4)_taste` recovered only in the continuum limit.
- **Proof skeleton.** Fourier/hypercube decomposition; define the `Γ_{ρσ}`
  matrices from staggered phases `η_μ(x)=(-1)^{x_1+...+x_{μ-1}}`; the resulting
  `4×4 ⊗ 4×4` algebra is `Cl_4 ⊗ M_4(C)taste`; the taste algebra is the
  *commutant* of the spin Clifford algebra.
- **Maps to repo.** This is **precisely the block-01 P-REC core** (the explicit
  `W: α_μ → γ_μ ⊗ 1_taste`, `Γ_5^spin = α_0α_1α_2α_3` taste-singlet, full
  `M_4(C)` taste commutant). The repo already recomputed this in-tree
  (`frontier_abj_prec_r4_taste_reconstruction`, PASS=43;
  `frontier_abj_prec_spintaste-core`, PASS=12). So the FREE reconstruction is a
  *settled textbook fact* the repo independently reproduced — good for the
  bankable carrier-conditional core (3.3 of the fresh-attempts note).
- **Does not map.** It does NOT supply a **single-taste selector**: the `SU(4)`
  taste symmetry is exact and *unbroken* in the free theory, so all four tastes
  are on equal footing (exactly the repo's "two distinct orthogonal rank-4
  single-taste projectors are both invariant"). The continuum-limit symmetry
  enhancement is an external dynamical statement, not an `A_min` consequence.
- **Runner translation.** Already done. The only *new* runner value would be to
  confirm the taste algebra is literally the commutant `{α}'` (the repo computed
  the commutant *dimension* 16; a sharper check is that it is generated by the
  four `ξ_μ` built from the *dual* staggered phases) — bookkeeping, not a crack.
- **Import risk.** LOW as math (the repo reproduced it). The risk is rhetorical:
  do not let "the textbook says tastes become 4 Dirac fermions in the continuum"
  smuggle in a continuum-limit / single-taste claim. That enhancement is the
  wall, not a lemma.
- **Citation.** van den Doel & Smit 1983; Gliozzi 1982;
  [arXiv:1210.1786](https://arxiv.org/abs/1210.1786).

### Source A2 — Hamiltonian staggered fermions: symmetries & anomalies (recent)
- **Source.** *Symmetries and Anomalies of Hamiltonian Staggered Fermions*,
  [arXiv:2501.10862](https://arxiv.org/abs/2501.10862) (2025).
- **Problem.** Build the taste basis in the *Hamiltonian* (one fewer dimension)
  setting via two matrix fermions on a doubled lattice — matrix indices = spin and
  taste — and track which discrete symmetries are anomalous.
- **Premises.** Hamiltonian lattice; doubled spacing; discrete subgroup of
  `SU(4)` taste; locality.
- **Proof skeleton.** Spin-basis change of variables; identify the discrete
  remnant of the axial-taste symmetry; compute its 't Hooft anomaly.
- **Maps to repo.** Relevant because `A_min`'s Record axiom + `kinetic_isotropy`
  give a `Z^3`-spatial + one-tick (Hamiltonian-flavored) reading. If a *single*
  taste-axial symmetry has a 't Hooft anomaly that survives at finite lattice,
  that is a candidate "chirality witness without a continuum limit" — directly the
  P-REC R3a / P-ABJ open ray.
- **Does not map.** Hamiltonian-staggered anomaly classification still assumes the
  *species/symmetry content* (which discrete subgroup is gauged). `A_min` withholds
  exactly that (gauge group / which symmetry is gauged) — same minimal-axioms gate.
- **Runner translation.** Build the repo's `2^3`(space) ⊗ tick carrier, the
  Hamiltonian staggered `H`, and test whether the repo's single retained time
  edge induces a *finite* anomalous phase under the discrete taste-axial — i.e.
  whether the time edge breaks the `+/-` pairing that forces `A_t=0`. (NEW vector
  V1, Section 5.)
- **Import risk.** MEDIUM. The anomaly classification imports a chosen symmetry
  group; that choice is the P-COMP/P-HY content `A_min` does not fix. Bounded-import
  only with the symmetry choice named as a premise.
- **Citation.** [arXiv:2501.10862](https://arxiv.org/abs/2501.10862).

---

## 2. PATTERN B — Staggered overlap & the taste-singlet index (Adams)

### Source B1 — Adams, staggered index theorem (the keystone literature result)
- **Source.** D. H. Adams, *Theoretical foundation for the Index Theorem on the
  lattice with staggered fermions*, PRL **104**, 141602 (2010),
  [arXiv:0912.2850](https://arxiv.org/abs/0912.2850). Review:
  [arXiv:1103.6191](https://arxiv.org/abs/1103.6191). Numerics:
  [arXiv:1102.1000](https://arxiv.org/abs/1102.1000). Spectral-flow follow-up:
  [arXiv:1111.3502](https://arxiv.org/abs/1111.3502),
  [arXiv:1410.5733](https://arxiv.org/abs/1410.5733).
- **Problem.** Identify the would-be zero modes of the staggered Dirac operator
  *away from the continuum*, assign them chirality, and prove
  `index = topological charge` (lattice Atiyah–Singer).
- **Premises.** A nontrivial **gauge-field topology** (the index is "determined by
  gauge field topology"); a Hermitian staggered operator `H(m)=γ_5^{stag}(D-m)`
  whose **spectral flow** as `m` varies counts net chirality crossings; smooth
  enough links that the crossings are resolvable. Validated in U(1) backgrounds in
  2d.
- **Proof skeleton.** Build `H(m)`; track eigenvalue crossings of `0` as `m`
  sweeps; the net signed crossing count = index; show it equals the gauge
  topological charge `Q`; re-express as the index of an *overlap* operator built
  on a staggered kernel.
- **Maps to repo.** This is the **positive theorem the repo's two no-gos are the
  flat-background corner of.** `ABJ_RESIDUAL_GW_NOT_NECESSARY` already states the
  obstruction is the `ε`-gap `H(m)^2 = K^2 + m^2 I` (no zero crossing for `m≠0`)
  *on the flat background*; Adams says crossings APPEAR once `Q≠0`. So the literature
  hands the repo the exact missing ingredient: **the index is the spectral flow,
  and it is nonzero iff `Q≠0`.** This is the citable backbone for the P-ABJ /
  P-REC-R3a open ray.
- **Does not map.** Adams **requires `Q≠0`**, which `A_min` does not supply: the
  closed single-valued-link `Z^4` torus has total winding `Q=0` (repo runner
  `frontier_abj_internal_chi_nonzero_index_escape` R-C: `max|Q_plane| < 1.4e-15`;
  `Q≠0` only under an injected boundary twist = external datum). So Adams confirms
  the wall is "`A_min` supplies no `Q≠0` gauge background," not "no staggered
  index exists."
- **Runner translation.** Port the repo's `H(m)=εD` (already built) into an
  *Adams spectral-flow* runner on the SMALLEST background `A_min` could plausibly
  host a `Q≠0`: a *single-valued-link* configuration is forced to `Q=0`, so the
  honest test is whether ANY `A_min`-admissible link assignment (single-valued,
  no injected transition function) can carry `Q≠0`. The repo R-C already answers
  NO. The NEW runner value (V2) is the *converse direction*: take Adams' minimal
  `Q=1` U(1) background, confirm the staggered spectral flow gives index 1 on the
  repo's own `εD` operator — establishing the mechanism is real and the ONLY gap
  is the `A_min` background, mirroring the repo's off-substrate `3×3` control.
- **Import risk.** MEDIUM-HIGH if mis-used. Adams is a *lattice* theorem (good:
  no continuum import) but it is external physics machinery. As a *bounded import*
  it is fine: it would let the keystone say "given a `Q≠0` background, the
  staggered index is the topological charge (Adams 2010)" — but the existence of
  the `Q≠0` background remains the named premise. Do NOT let it read as an `A_min`
  derivation of `Q≠0`.
- **Citation.** [arXiv:0912.2850](https://arxiv.org/abs/0912.2850) (Adams 2010);
  [arXiv:1103.6191](https://arxiv.org/abs/1103.6191) (Adams 2011 review).

### Source B2 — Adams staggered overlap (taste-reduced) & the taste-singlet γ5
- **Source.** D. H. Adams, *Index and overlap construction for staggered
  fermions*, [arXiv:1103.6191](https://arxiv.org/abs/1103.6191); single-flavor:
  [arXiv:1009.5362](https://arxiv.org/abs/1009.5362); numerics
  [arXiv:1102.1000](https://arxiv.org/abs/1102.1000); locality proof
  [arXiv:2203.06116](https://arxiv.org/abs/2203.06116).
- **Problem.** Reduce 4 tastes → 2 (and → 1) **without fine-tuning** by using a
  *taste-singlet* chirality operator and a flavored mass that splits tastes.
- **Premises.** The taste-singlet operator `Γ_5 = η_5 · C`, where `η_5(x) =
  (-1)^{x_1+x_2+x_3+x_4}` is the site-parity `ε` and `C` is a **symmetrized sum of
  4-link parallel transporters** (a *gauge-covariant, non-local* dressing). The
  flavored mass `Γ_5` term probes gauge-field topology.
- **Proof skeleton.** `Γ_5 = η_5 C` has a taste-singlet decomposition (unlike bare
  `ε`); insert it into the overlap kernel; the resulting operator has 2 (or 1)
  tastes and an integer index.
- **Maps to repo — THIS IS THE SHARPEST HIT.** The repo's P-REC wall is *exactly*
  that bare `ε` is taste-DRESSED, not the spin `γ_5`: repo
  `frontier_abj_prec_spintaste-core` found `ε ∉ {α}''` (residual 4.0) and
  `[ε, taste commutant] ≠ 0` (0.375); `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO`
  shows bare `ε` gives index 0. **Adams' resolution is precisely to replace bare
  `ε` with `Γ_5 = ε·C`** — the 4-link transporter `C` is the missing taste-singlet
  dressing. So the literature names the exact object the repo is missing: not a new
  axiom, but a **gauge-covariant 4-link operator `C`**, which requires *gauge
  links* (interacting/gauged structure).
- **Does not map.** `C` is built from **gauge parallel transporters** — it is
  trivial (`C → 1`-like) on the *free* theory, which is why it cannot help the
  repo's *free* `2^4` carrier. `A_min` supplies no gauge connection on the links
  (Quantum is one qubit/site; Lattice is bare adjacency; no gauge field is an
  axiom). So Adams' taste-singlet `γ_5` exists only once a gauge background is
  adjoined — the P-REC "gauged/interacting single-taste selector" wall, named at
  the level of *the specific operator `C`*.
- **Runner translation.** NEW vector V3: build the repo's free `α_μ` carrier with
  an *adjoined* U(1) link field (the same one R-B/R-C already inject) and compute
  `Γ_5 = ε·C(U)`; test (a) whether `Γ_5` is now taste-singlet (commutes with the
  taste commutant) where bare `ε` was not, and (b) whether `{Γ_5, D[U]}` closes a
  Ginsparg–Wilson-type relation. This is a *measurement of what gauging buys*, on
  the repo's own substrate — the honest boundary between "free, no selector" and
  "gauged, taste-singlet `γ_5` exists (Adams `C`)."
- **Import risk.** MEDIUM. `C` is standard lattice machinery, importable as
  bounded support *iff* the gauge field it needs is itself a named premise (it is
  not in `A_min`). The danger: presenting "Adams gives a taste-singlet `γ_5`" as
  closing P-REC when in fact it relocates the wall to "`A_min` supplies the gauge
  links `C` needs."
- **Citation.** [arXiv:1103.6191](https://arxiv.org/abs/1103.6191);
  [arXiv:1009.5362](https://arxiv.org/abs/1009.5362).

---

## 3. PATTERN C — Chiral anomaly from the overlap Dirac operator (Ginsparg–Wilson, Lüscher)

### Source C1 — Lüscher: exact lattice axial anomaly & lattice index theorem
- **Source.** M. Lüscher, *Abelian chiral gauge theories on the lattice with exact
  gauge invariance*, [arXiv:hep-lat/9811032](https://arxiv.org/abs/hep-lat/9811032);
  Hasenfratz–Laliena–Niedermayer, [arXiv:hep-lat/9801021]; review
  [arXiv:hep-lat/0405024](https://arxiv.org/abs/hep-lat/0405024). Generalized GW:
  [arXiv:hep-lat/0205024](https://arxiv.org/abs/hep-lat/0205024).
- **Problem.** A lattice Dirac operator obeying the Ginsparg–Wilson relation
  `{γ_5,D} = a D γ_5 D` has an exact (modified) chiral symmetry, the correct axial
  `U(1)` anomaly, and satisfies `index D = Q` (Atiyah–Singer on the lattice).
- **Premises.** GW relation holds (overlap `D` is the canonical solution);
  `Tr γ_5 (1 - a D/2)` is the lattice topological charge; gauge background with
  `Q≠0` for a nonzero index.
- **Proof skeleton.** From GW, `γ_5 D + D γ_5 = a D γ_5 D` ⇒ the index density
  `q(x) = -(a/2) tr[γ_5 D(x,x)]` integrates to the integer index; Fujikawa Jacobian
  of the modified chiral rotation reproduces the anomaly.
- **Maps to repo.** This is the *target structure* the keystone's external P-ABJ
  premise stands in for. The repo's `ABJ_RESIDUAL_GW_NOT_NECESSARY` correctly says
  GW is **sufficient but not necessary** — so the repo does NOT need to import the
  overlap operator to have an anomaly; it needs a `χ≠0`/`Q≠0` background. C1 is the
  cleanest statement that **the lattice anomaly is real and quantized**, supporting
  the keystone's claim that an anomaly forces an inconsistency — but as *external*
  physics.
- **Does not map.** GW/overlap is a *constructed* operator, not derivable from
  `A_min` (it is the resolution of Nielsen–Ninomiya, see C2, which itself bars the
  naive `A_min` route). And the index is again zero without `Q≠0`. So C1 does not
  remove any `A_min` wall; it confirms the *external* status of P-ABJ.
- **Runner translation.** None needed beyond the repo's existing overlap-index
  runner (R-B already built `(1/2)Tr[ε·sign(K)]` and found index 0 on flat +
  flux-U(1) — consistent with C1 since those backgrounds have `Q=0`). The honest
  use is *citation*, not a new runner.
- **Import risk.** HIGH if presented as internal. GW/overlap is exactly the kind of
  "constructed bridge" `review-loop` warns about — importable only as named
  external machinery. The repo's own GW-not-necessary note is the correct posture:
  cite, do not adopt.
- **Citation.** [arXiv:hep-lat/9811032](https://arxiv.org/abs/hep-lat/9811032)
  (Lüscher 1998); [arXiv:hep-lat/0405024](https://arxiv.org/abs/hep-lat/0405024).

### Source C2 — Nielsen–Ninomiya no-go (why `A_min` cannot have naive chirality)
- **Source.** Nielsen & Ninomiya, *Nucl. Phys. B185 (1981) 20*; Friedan's proof,
  *Commun. Math. Phys. 85 (1982) 481*
  ([Rutgers PDF](https://www.physics.rutgers.edu/~friedan/papers/Commun_Math_Phys_85_481-490_1982.pdf));
  review [arXiv:hep-lat/0405024](https://arxiv.org/abs/hep-lat/0405024).
- **Problem.** Under locality + hermiticity + translation invariance + correct
  dispersion, a lattice Dirac operator has **zero net chirality** (equal L/R
  doublers). Topological: the Brillouin zone is a torus and the Dirac field winds.
- **Premises.** Locality (finite-range), hermiticity, translation invariance,
  bilinear/quadratic action, `U(1)` phase symmetry.
- **Proof skeleton.** The zeros of the lattice dispersion on the BZ torus carry
  `±` chirality (Poincaré–Hopf); their signed sum over a compact torus is `0`.
- **Maps to repo — STRONGLY (this is a citable SHARPENING of the wall).** The
  repo's `NO_PER_SITE_CHIRALITY_THEOREM` (per-site `M_2(C)`: only `B=0`
  anticommutes with all three Paulis) is a *finite-dimensional shadow* of
  Nielsen–Ninomiya. NN is the *general topological reason* that any
  `A_min`-respecting (local, translation-invariant on cubic `Z^3`) construction
  cannot have an ungapped single-chirality grading without either (i) breaking
  locality, (ii) breaking translation invariance, or (iii) the GW deformation.
  **This upgrades the repo's wall from a single algebraic computation to a named
  topological no-go with an established proof.** It is the strongest *citable
  no-go* available for P-REC.
- **Does not map.** NN assumes translation invariance on the full torus; the repo's
  Record axiom + `realized_state_primitive` permit a *fixed realized state* that is
  not translation-invariant. That is the one NN hypothesis `A_min` could in
  principle violate — but a realized-state-dependent chirality is *registered data*,
  not a derivation (B-AXIS lesson; repo `realized_state_primitive` boundary). So NN
  closes the translation-invariant route and pushes any escape into the
  registered-data category, which the repo already disallows as a derivation.
- **Runner translation.** Not a runner — a *citation upgrade*. The action: cite
  Nielsen–Ninomiya + Friedan as the topological parent of
  `NO_PER_SITE_CHIRALITY_THEOREM`, strengthening the P-REC wall from "one algebraic
  fact" to "the lattice chiral no-go," and explicitly recording that the only NN
  hypothesis `A_min` can drop (translation invariance, via a realized state) yields
  registered data not a derivation. (NEW vector V4 — a *sharper citable no-go*,
  which the owner posture ranks above a bare wall.)
- **Import risk.** LOW. NN is a no-go we are *citing to strengthen our own no-go*,
  not an import that closes a positive claim. The only care: state NN's hypotheses
  exactly so the realized-state escape is visibly the registered-data category.
- **Citation.** Nielsen–Ninomiya 1981; Friedan 1982 (Commun. Math. Phys. 85, 481).

---

## 4. PATTERN D — Atiyah–Singer / Adams index on lattices via χ≠0 (Kähler–Dirac)

### Source D1 — Catterall & Butt: Kähler–Dirac 't Hooft anomaly from the Euler character
- **Source.** N. Butt, S. Catterall, et al., *Anomalies and symmetric mass
  generation for Kähler–Dirac fermions*,
  [arXiv:2101.01026](https://arxiv.org/abs/2101.01026) (PRD 2021); S. Catterall,
  *'t Hooft anomalies for staggered fermions*,
  [arXiv:2209.03828](https://arxiv.org/abs/2209.03828) (PRD 107, 014501, 2023);
  curved-space follow-up [arXiv:2509.08885](https://arxiv.org/abs/2509.08885);
  CPT/KD [arXiv:2511.11548](https://arxiv.org/abs/2511.11548).
- **Problem.** Massless Kähler–Dirac (= staggered, generalized to curved space)
  fermions have a **mixed gravitational anomaly**: under the exact `U(1)_{KD}`
  symmetry the partition function picks up a phase **depending only on the Euler
  characteristic `χ` of the background**, breaking `U(1) → Z_4` in even dimensions.
  Gauging `Z_4` gives a 't Hooft anomaly cancelled only by **multiples of two**
  Kähler–Dirac fields.
- **Premises.** Kähler–Dirac formulation (fermions = inhomogeneous differential
  forms); a curved background / random triangulation with `χ≠0`; even dimension.
  The anomaly **survives lattice discretization** (the key point) and is tied to
  the structure of the KD operator and homology.
- **Proof skeleton.** The `U(1)_{KD}` rotation's Jacobian is the index of the KD
  operator; on a compact even space `index = χ` (a Gauss–Bonnet / Hopf statement,
  the gravitational analogue of `index = Q`); hence the anomalous phase `∝ χ`. The
  discrete version reproduces `χ` exactly via the simplicial homology of the
  triangulation.
- **Maps to repo — THIS IS THE EXACT OPEN-RAY ANCHOR.** The repo's retained
  `ABJ_RESIDUAL_GW_NOT_NECESSARY` *literally cites this paper family* and
  re-targets P-ABJ to "exhibit a `χ≠0` background"; the repo runner's `χ(flat
  torus)=0` line is the `A_min` corner. D1 is the **literature theorem that a
  `χ≠0` background gives a nonzero, discretization-robust anomalous index** — the
  positive statement whose hypothesis (`χ≠0`) is exactly what `A_min` withholds.
  It also gives a *second, independent* nonzero-index channel besides gauge `Q≠0`:
  pure geometry.
- **Does not map.** `A_min`'s Lattice axiom is **flat cubic `Z^3`** (Euler
  characteristic of a flat `n`-torus is `0`); `kinetic_isotropy` adds a flat time
  edge ⇒ flat `Z^4`, still `χ=0`. So `A_min` provably cannot host the `χ≠0`
  background D1 needs — and crucially, the repo's R-A finding ("`ε`-imbalance ⇔
  all-odd ⇔ chirality grading destroyed in every direction") shows the *only*
  imbalanced cubic complex `A_min` can make ALSO breaks `{ε,D}=0`. D1 says the
  honest fix is **curvature (`χ≠0`), not imbalance** — a *different* background than
  the all-odd torus the repo already pruned.
- **Runner translation — HIGHEST-VALUE NEW VECTOR (V5).** The repo has only ever
  tested **flat cubic** and **open-rectangular** complexes. D1 says to test a
  **simplicial / triangulated `χ≠0` complex**. Concretely: build the smallest
  closed 2d simplicial surface with `χ≠0` (a tetrahedron boundary `≅ S^2`, `χ=2`;
  or an octahedron, `χ=2`), put the Kähler–Dirac/staggered operator on it, and
  compute `Tr[ε e^{-tD†D}]` — D1 predicts it equals `χ = 2 ≠ 0`. This is the
  *first* `χ≠0` runner in the campaign and the honest test of whether `A_min`'s
  cubic-`Z^3` Lattice is the *load-bearing* obstruction (it is, per D1 — but the
  runner makes it decisive and shows the mechanism is real off-substrate, like the
  repo's `3×3` control did for imbalance). **This is the single most promising
  literature-driven runner.**
- **Import risk.** MEDIUM. The KD/curved-space machinery is external, importable
  only as named bounded support. But the *non-vacuity witness* (a `χ≠0` complex
  gives nonzero index) is exactly the kind of off-substrate control the repo
  already sanctions (P-ABJ control, "succeeded as control"). The wall stays:
  `A_min` supplies cubic `Z^3` (`χ=0`), so the consumer must ADMIT a `χ≠0`
  geometry. Do NOT claim this closes P-ABJ-internal; it sharpens *why* it is walled
  (flat-lattice axiom) and gives a second independent index channel to cite.
- **Citation.** [arXiv:2101.01026](https://arxiv.org/abs/2101.01026) (Butt et al.
  2021); [arXiv:2209.03828](https://arxiv.org/abs/2209.03828) (Catterall 2023).

### Source D2 — Index on naive/minimally-doubled fermions & spectral graphs
- **Source.** *Index theorem and overlap formalism with naive and minimally
  doubled fermions*, JHEP 12 (2010) 041
  ([Springer](https://link.springer.com/article/10.1007/JHEP12(2010)041));
  Yumoto & Misumi, *Lattice fermions as spectral graphs*, JHEP 02 (2022) 104,
  [arXiv:2112.13501](https://arxiv.org/abs/2112.13501) — explicitly studies zero
  modes on **non-torus / non-regular lattices of arbitrary topology**.
- **Problem.** Extend the Adams-style index construction to *naive* and
  *minimally-doubled* fermions, and recast lattice fermions as spectral graphs (the
  index as a graph-theoretic invariant of the adjacency structure).
- **Premises.** Lattice adjacency graph; a Hermitian kernel; gauge topology.
- **Proof skeleton.** Spectral-flow / graph-spectral construction of the index from
  the adjacency operator's zero modes.
- **Maps to repo.** "Lattice fermions as spectral graphs" is *unusually* aligned
  with `A_min`: the Lattice axiom is literally a graph (`Z^3` nearest-neighbor
  adjacency). A graph-spectral index would be the most `A_min`-native index
  language — a candidate for an *internal* (not imported) index, if the chirality
  grading can be made a graph invariant.
- **Does not map.** The graph index still needs a **bipartite imbalance or a
  weighting that breaks `±` pairing** — which on a balanced bipartite cubic graph
  is `0` (the repo's square-block result is exactly the bipartite-graph statement).
  So the graph framing re-expresses the wall in `A_min`'s own language but does not
  remove it: a balanced bipartite `Z^3` graph has graph-index `0`.
- **Runner translation.** NEW vector V6: recast the repo's `εDε=-D` square-block
  result as a *graph-theoretic* statement (bipartite adjacency ⇒ symmetric spectrum
  ⇒ index 0) and search for an `A_min`-admissible *non-bipartite* connected cubic
  graph — but R-A already shows non-bipartite cubic ⇔ all-odd ⇔ destroyed grading.
  The graph framing's value is *expository* (states the wall in axiom-native terms)
  plus a check that no weighting allowed by `A_min` (which weightings? none —
  Record supplies no weighting rule) can break the pairing.
- **Import risk.** LOW-MEDIUM. Graph-spectral index is close to native; the import
  is the *interpretation* of the graph index as a physical anomaly, which still
  needs the species/chirality identification `A_min` withholds.
- **Citation.** JHEP 12 (2010) 041; Yumoto & Misumi,
  [arXiv:2112.13501](https://arxiv.org/abs/2112.13501) (JHEP 02 (2022) 104).

---

## 5. PATTERN E — Anomaly inflow / cohomological (non-abelian) anomaly

### Source E1 — Lüscher: gauge anomaly cancellation & cohomology on the lattice
- **Source.** M. Lüscher, *Abelian chiral gauge theories ... exact gauge
  invariance* [arXiv:hep-lat/9811032]; *Topology and the axial anomaly in abelian
  lattice gauge theories* [arXiv:hep-lat/9808021]; Suzuki, *Anomaly cancellation
  condition in abelian lattice gauge theories*
  [arXiv:hep-lat/9911009](https://arxiv.org/abs/hep-lat/9911009); non-abelian
  obstruction [arXiv:hep-lat/0005015](https://arxiv.org/abs/hep-lat/0005015).
- **Problem.** Construct the chiral gauge measure on the lattice; the obstruction to
  a gauge-invariant measure is a **cohomology class** of a topological field on the
  `4d` lattice + `2` continuum dimensions; it is trivial **iff the anomaly
  coefficients cancel** (the lattice Wess–Zumino consistency condition).
- **Premises.** GW/overlap Weyl measure; anomaly-free fermion content
  (`Tr Y = Tr Y^3 = ...= 0`); locality of the anomaly density.
- **Proof skeleton.** Solve the lattice WZ consistency condition; show the
  cohomologically nontrivial part is `∝` the continuum anomaly coefficient; for
  anomaly-free content the measure-current is a total lattice divergence ⇒ a
  gauge-invariant measure exists.
- **Maps to repo.** This is the **non-abelian-cohomology open ray** named in both
  the EXERCISE and the square-block no-go's "ROUTE LEFT OPEN: non-abelian
  cohomology derivation of the anomaly." It also dovetails with the repo's
  **arithmetic cores**: the repo already proves `Tr Y = Tr Y^3 = Tr SU(3)^2 Y = ...
  = 0` for the completed content. Lüscher's theorem says exactly those vanishing
  traces are the *cohomological cancellation condition* — so the repo's bankable
  anomaly arithmetic IS the input Lüscher's existence proof consumes.
- **Does not map.** Lüscher needs (i) the GW/overlap Weyl measure (external,
  constructed) and (ii) the **chiral gauge representation already chosen** — i.e.
  the gauge group, the Weyl content, and the single-taste/single-chirality
  projection. Those are P-HY ("is-gauged"), P-COMP (content), and P-REC
  (single-chirality) — *all three withheld walls at once*. So Lüscher's cohomology
  presupposes the very identifications the campaign is trying to derive.
- **Runner translation.** Not a finite-`A_min` runner (it is a continuum+lattice
  cohomology existence proof). Its honest use is **conceptual closure of the P-ABJ
  inconsistency logic**: cite Lüscher to show that *if* the content is the repo's
  anomaly-free completion *and* it is gauged chirally, the measure exists and the
  anomaly is the cohomology class — making the keystone's "anomaly ⇒ inconsistency"
  a *citable external* statement, not an `A_min` derivation. (Supports the
  "external admission by policy" posture, does not crack it.)
- **Import risk.** HIGH. This is the most machinery-heavy import; it presupposes all
  three identification walls. Useful only to *frame* the external P-ABJ admission,
  never to claim internal derivation.
- **Citation.** [arXiv:hep-lat/9811032](https://arxiv.org/abs/hep-lat/9811032);
  [arXiv:hep-lat/9911009](https://arxiv.org/abs/hep-lat/9911009).

### Source E2 — Witten–Yonekura: anomaly inflow & the η-invariant (cobordism)
- **Source.** E. Witten & K. Yonekura, *Anomaly Inflow and the η-Invariant*,
  [arXiv:1909.08775](https://arxiv.org/abs/1909.08775); Dai–Freed; Freed–Hopkins
  cobordism classification; SM cobordism constraints
  [arXiv:2006.16996](https://arxiv.org/abs/2006.16996).
- **Problem.** Both perturbative and **global/non-perturbative** fermion anomalies
  in `d` dimensions are captured by an `η`-invariant in `d+1` dimensions (a
  cobordism invariant when perturbative anomalies cancel). Anomaly inflow from a
  bulk Chern–Simons / `η` term to the boundary.
- **Premises.** A `(d+1)`-dim bulk with a fermion `η`-invariant; cobordism
  invariance; perturbative anomaly cancellation for the cobordism statement.
- **Proof skeleton.** APS index theorem ⇒ the boundary anomaly phase = bulk
  `exp(-2πi η)`; cobordism invariance follows when the perturbative anomaly
  vanishes; nonperturbative anomalies = nontrivial cobordism classes.
- **Maps to repo.** Two uses. (a) The repo's keystone is "an anomaly forces a
  *time* dimension / inconsistency" — anomaly inflow is *literally* the statement
  that a `d`-anomaly needs a `(d+1)`-bulk, which is suggestive for the
  "anomaly forces time" parent (a `3d` anomaly inflowing from a `3+1d` bulk).
  (b) Cobordism gives the *complete* anomaly classification, so it is the right
  external authority for "the anomaly cannot be cancelled internally ⇒ inconsistency
  unless the content is cobordism-trivial."
- **Does not map.** Heavily continuum/smooth-manifold; cobordism groups are not
  `A_min`-native (no smooth structure in `Z^3`). The `d→d+1` inflow is a
  *suggestive analogy* for "anomaly forces time," NOT a proof on the lattice
  substrate. Importing it would add a smooth-manifold/cobordism layer `A_min` does
  not have.
- **Runner translation.** None on `A_min`. Conceptual only: it is the cleanest
  external statement of *why* an uncancelled anomaly is fatal (cobordism
  obstruction) — citable to support the external P-ABJ admission and possibly to
  *motivate* (not derive) the "anomaly forces time" parent's dimensional logic.
- **Import risk.** HIGH (continuum cobordism). Use only as external framing for the
  parent theorem's narrative; never as a lattice/`A_min` derivation.
- **Citation.** [arXiv:1909.08775](https://arxiv.org/abs/1909.08775)
  (Witten–Yonekura 2019).

### Source E3 — Catterall–Pradhan: gauging staggered shift symmetries
- **Source.** S. Catterall & A. Pradhan, *Gauging staggered fermion shift
  symmetries*, [arXiv:2405.03037](https://arxiv.org/abs/2405.03037)
  (PRD 110, 094516, 2024).
- **Problem.** Staggered *shift* symmetries (translations within the `2^4` unit
  cell) = a discrete subgroup of the `SU(4)` taste symmetry. Partially gauge them
  with `Z_2`-valued higher-form lattice gauge fields.
- **Premises.** Shift symmetry ↔ discrete `SU(4)` subgroup; higher-form `Z_2`
  gauge fields; locality.
- **Proof skeleton.** Promote shift parameters to local fields; introduce
  `Z_2` 1- and 2-form gauge fields to maintain invariance; analyze the gauged
  theory's content.
- **Maps to repo — directly on the P-REC single-taste selector.** The repo's wall
  is "the free `M_4(C)` taste symmetry makes single-taste selection unforced." This
  paper is the literature attempt to *gauge/break the taste(shift) symmetry on the
  lattice* — i.e. the exact mechanism that could *select* a taste. If gauging the
  shift symmetry leaves an obstruction (it requires higher-form gauge fields), that
  obstruction is the precise statement of *what extra structure single-taste
  selection costs* — and `A_min` supplies no higher-form gauge field.
- **Does not map.** It *partially* gauges (the abstract is careful: "a strategy to
  try to partially gauge"); it does not deliver a clean single-taste projection,
  and it needs `Z_2` higher-form gauge fields that `A_min` does not have. So it
  confirms single-taste selection is *costly external structure*, not an `A_min`
  consequence — sharpening, not cracking, the P-REC wall.
- **Runner translation.** NEW vector V7: on the repo's `2^4` carrier, implement a
  `Z_2` shift-symmetry gauge field and test whether it *reduces* the taste commutant
  (breaks the `M_4(C)` to a single rank-4 factor). Predict (from this paper) that
  full single-taste selection is NOT achieved by `Z_2` higher-form gauging alone —
  measuring exactly how much of the `M_4(C)` survives = the residual selector cost.
- **Import risk.** MEDIUM. Higher-form `Z_2` gauge fields are external structure;
  importable only as a named premise. Honest outcome: the taste-selection wall is
  *quantified* (how much symmetry remains), not removed.
- **Citation.** [arXiv:2405.03037](https://arxiv.org/abs/2405.03037).

---

## 6. Per-wall read (literature lens) — closable / reframable / genuinely walled

- **P-REC (soft wall, highest value).** **Reframable + sharper-no-go, not closable
  internally.** The literature names the EXACT missing object: Adams' taste-singlet
  `Γ_5 = ε·C` (4-link gauge transporter `C`) is precisely the dressing that turns
  the repo's taste-dressed bare `ε` into a real taste-singlet `γ_5` (B2). But `C`
  needs gauge links `A_min` does not supply, so R4 stays walled at the level of "a
  specific gauge-covariant operator." Independently, Nielsen–Ninomiya + Friedan
  (C2) is a *citable topological no-go* upgrading `NO_PER_SITE_CHIRALITY_THEOREM`
  from one algebraic fact to "the lattice chiral no-go," with the only `A_min`-
  droppable hypothesis (translation invariance, via a realized state) landing in
  the registered-data category. **Net: the soft wall is now (a) named at operator
  level and (b) backed by a hard topological no-go — a strictly better wall, and
  a clear bounded-import path if a gauge background is ever admitted.**

- **P-COMP.** **Reframable via Lüscher cohomology, existence still walled.**
  Lüscher (E1) shows the repo's already-bankable vanishing traces
  (`Tr Y = Tr Y^3 = ... = 0`) ARE the cohomological anomaly-cancellation condition
  — so the repo's arithmetic core is exactly the literature's consistency input.
  But Lüscher *presupposes* the chiral content (the template), so it cannot supply
  template *existence*; cobordism (E2) is the complete classification but is
  continuum/smooth, not `A_min`-native. **Net: existence stays walled
  (minimal-axioms withhold content); the literature reframes the arithmetic core as
  the standard cohomological cancellation condition — citable support, not closure.**

- **P-ABJ (internal route).** **Genuinely walled by the flat-lattice axiom; TWO
  independent nonzero-index channels identified.** Adams (B1) gives `index = Q`
  (gauge topology); Catterall–Butt (D1) give `index = χ` (geometry / Euler
  characteristic) — both discretization-robust. `A_min` supplies neither: cubic
  `Z^3` is flat (`χ=0`) and single-valued links force `Q=0` (repo runners confirm).
  The repo had only tested flat-cubic and open-rectangular; **D1 points to a
  genuinely untested background class (closed `χ≠0` simplicial complexes)** — the
  honest non-vacuity control (V5). The external anomaly⇒inconsistency implication
  is framed by Lüscher/Witten–Yonekura (E1/E2) as a cohomology/cobordism
  obstruction — confirming P-ABJ-B2 is *irreducibly external by content*, not just
  by policy.

---

## 7. NEW attack vectors surfaced (each: wall + challenged assumption + first artifact)

- **V1 (P-REC / P-ABJ).** *Wall:* P-REC single-taste / P-ABJ `A_t=0`. *Assumption
  challenged:* that the repo must work in the Euclidean `Z^4` torus where `+/-`
  pairing forces `A_t=0`. *Artifact:* build the **Hamiltonian staggered** carrier
  (`2^3` space ⊗ one tick, matching `A_min` Record + `kinetic_isotropy`) per
  arXiv:2501.10862 and test whether the single retained *time edge* induces a
  finite anomalous phase for the discrete taste-axial that the spatial torus
  forbids. First file: `frontier_abj_hamiltonian_staggered_taste_axial.py`.

- **V3 (P-REC, sharpest).** *Wall:* bare `ε` is taste-dressed (residual 4.0).
  *Assumption challenged:* that no taste-singlet `γ_5` exists on the staggered
  carrier. *Artifact:* build `Γ_5 = ε·C(U)` with Adams' symmetrized 4-link
  transporter `C` on the repo's `2^4` carrier with an adjoined U(1) link field
  (the one R-B already injects); measure whether `Γ_5` is now taste-singlet where
  bare `ε` was not, and whether `{Γ_5, D[U]}` closes a GW-type relation. First
  file: `frontier_abj_prec_adams_taste_singlet_gamma5.py`. (This is the operator
  the repo is literally missing — names the gauged-selector wall concretely.)

- **V4 (P-REC, citable no-go upgrade — owner-preferred class).** *Wall:* per-site
  chirality. *Assumption challenged:* that `NO_PER_SITE_CHIRALITY_THEOREM` is a
  one-off algebraic fact. *Artifact:* a `meta`/no_go note citing Nielsen–Ninomiya
  (1981) + Friedan (1982) as the topological parent, recording that the only
  `A_min`-droppable NN hypothesis (translation invariance) yields registered data
  under `realized_state_primitive`. No runner; a sharper *citable* wall.

- **V5 (P-ABJ — HIGHEST-VALUE NEW RUNNER).** *Wall:* `A_t=0` / `χ=0` on `A_min`.
  *Assumption challenged:* that `A_min`'s Lattice axiom (flat cubic `Z^3`, `χ=0`)
  is *not* the load-bearing obstruction. *Artifact:* put the staggered /
  Kähler–Dirac operator on the **smallest closed `χ≠0` simplicial surface**
  (tetrahedron boundary `≅ S^2`, `χ=2`) and compute `Tr[ε e^{-tD†D}]`; per
  Catterall–Butt (D1) it should equal `χ=2 ≠ 0` — the campaign's **first `χ≠0`
  index runner** and the decisive off-substrate non-vacuity control proving the
  cubic-flat axiom is exactly the wall. First file:
  `frontier_abj_chi_nonzero_simplicial_index.py`.

- **V6 (P-ABJ, expository + check).** *Wall:* square-block `A_t=0`. *Assumption
  challenged:* that the wall is operator-specific rather than graph-topological.
  *Artifact:* recast `εDε=-D` as the bipartite-graph symmetric-spectrum statement
  (per "lattice fermions as spectral graphs", JHEP 02(2022)104) and verify no
  `A_min`-admissible weighting (Record supplies none) breaks the `±` pairing on a
  balanced bipartite cubic graph. States the wall in axiom-native graph language.

- **V7 (P-REC, quantifies the selector).** *Wall:* `M_4(C)` taste symmetry makes
  single-taste unforced. *Assumption challenged:* that taste selection is all-or-
  nothing. *Artifact:* implement a `Z_2` shift-symmetry (higher-form) gauge field
  on the `2^4` carrier per Catterall–Pradhan (arXiv:2405.03037) and measure how
  much of the `M_4(C)` taste commutant survives — quantifying the residual selector
  cost rather than asserting the wall. First file:
  `frontier_abj_prec_z2_shift_gauging_taste_residual.py`.

**Most promising:** **V5** (first `χ≠0` simplicial index runner — directly tests the
EXACT open ray both retained no-gos re-targeted to, with a clean Catterall–Butt
prediction `index=χ`, and is the honest non-vacuity control the campaign lacks),
followed by **V3** (names the missing taste-singlet `γ_5 = ε·C` operator on the
repo's own substrate).

---

## 8. What NOT to do (re-pruned / overreach guards)

- Do **NOT** re-run the bare-`ε`-as-`γ_5` route (pruned twice:
  `ABJ_GAMMA5_BOUNDARY` NG-1/NG-2 PASS=52; spintaste-core residual 4.0). V3 is
  different: it adds Adams' gauge-covariant `C`.
- Do **NOT** re-run the equal-sublattice even-torus + arbitrary-U(1) staggered
  index (pruned: `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO` PASS=45). V5 changes the
  *complex* (closed `χ≠0` simplicial), not the U(1) field.
- Do **NOT** justify importing the overlap operator with "no GW ⇒ must import
  overlap" — demolished (`ABJ_RESIDUAL_GW_NOT_NECESSARY` retained_bounded). GW is
  sufficient-not-necessary.
- Do **NOT** re-inject a boundary transition function to fake `Q≠0` on a balanced
  complex (pruned: R-C, `A_t=0` survives injected `Q`). V5 uses *geometric* `χ≠0`,
  a different channel.
- Do **NOT** present any imported theorem (Adams `C`, Lüscher cohomology, overlap,
  cobordism) as an `A_min` derivation or as closing a wall. Every one presupposes
  at least one withheld identification (gauge background, content, or single-taste
  projection). They are **bounded imports / external framing / citable no-gos**
  only — never new axioms or primitives (PRIMITIVE_REGISTRY_CHECK).
- Do **NOT** claim a `χ≠0`/`Q≠0` background is `A_min`-native: cubic `Z^3` is flat
  (`χ=0`), single-valued links give `Q=0` (repo runners). The *consumer* must admit
  the geometry/topology; that admission is the named wall.
