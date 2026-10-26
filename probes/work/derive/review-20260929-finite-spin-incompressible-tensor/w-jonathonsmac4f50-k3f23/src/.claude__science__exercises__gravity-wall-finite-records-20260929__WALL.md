# The gravity wall: step 0 (history) and step 1 (the wall, stated twice)

Exercise run on 2026-09-29 with the candidate exercise skill at commit
7e109b7b04 (PR #9389, reviewed by gpt-5.6-sol, "approve with corrections",
corrections applied). Supervisor: Claude Opus 5.5.

## Step 0 — what the repo already knows

The wall has been met from three directions. None of the results below is
audited.

| When | Surface | What it found |
| --- | --- | --- |
| 2026-05-02 | `docs/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md` (landed) | The exact canonical commutation relation [a, a†] = 1 cannot be realised by bounded operators in one site's M₂(C) (trace identity). |
| 2026-06-08 to 06-17 | the "universal GR" lane (`docs/UNIVERSAL_GR_*`, landed) | Given a metric degree of freedom, the lattice matter induces Einstein–Hilbert (Sakharov; G ~ a²/N_f) with a healthy spin-2 channel. The residual wall is "the metric-DOF / conformal-class posit" (`UNIVERSAL_GR_SAKHAROV_GNEWTON_INDUCED_RESIDUAL_IS_METRIC_DOF_POSIT_NARROW_THEOREM_NOTE_2026-06-17.md`). |
| 2026-06-06 | `EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md` (landed, open gate) | The Lorentzian conformal class is not assembled from records on the current source packet. |
| 2026-09-14 | `LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` (landed) | The tensor balance law on Z³ gives gravitons with ω ∝ k² (momentum rule) or k³ (with the time rule), not ∝ k. |
| 2026-09-24 | `TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_BOTH_CANONICAL_VARIABLES_MUST_BE_NON_COMPACT_BOUNDED_THEOREM_NOTE_2026-09-24.md` (landed) | A light-like, partner-free graviton appears when both canonical variables are non-compact (continuous, unbounded). |
| 2026-09-21 to 09-27 | the member programme (blocks 53–62, 112, 134–152; source-link lane) | Supplied tick rates and lengths give the comparator's ADM structure at linear order. The lapse algebra closes only at β = −α (112). The walker's clock algebra closes only for uniform lapses (150). A trilemma (panels of 09-26/27). |
| 2026-09-28/29 | PR #9363 probes 10–21, panels 3 and 4 (this lane) | On finite slots of the supplied tensor complex, at the harmonic level with the time rule exact: exact rules give slow waves; light-like waves bring a light-like helicity ±1 mode, whatever the residual symmetry. Every probe was confirmed by sol. |
| pre-registered, not run | 2026-09-25 panel, programme A step A1 | The second-order lapse algebra, i.e. nonlinear closure on the fixed grid. |

Tried already, so not to be re-derived here:
- the swap of which variable is stored (probe 15);
- quantum-link deformations (probe 14);
- composites of photon fields (probes 11, 16);
- on-site stiffness (probe 18);
- every move set (probe 20);
- residual symmetries (probe 21);
- exact additive Gauss laws (probe 17);
- induced gravity given a metric (June lane).

Not tried in the repo:
- gravity as an equation of state of the qubits' entanglement (Jacobson-type
  derivations);
- adjacency as a recorded, dynamical object (option B);
- strongly correlated phases of finite-slot tensor models beyond the exact
  sum rules;
- the phenomenology of the helicity ±1 partners, if they were kept.

## Step 1 — the wall

### Plain version (after the blind check)

We want gravity to come out of the framework rather than be assumed. The
framework is a grid of sites. Each site holds one qubit. Records are
permanent facts: once a site's value is recorded, it never changes.

Einstein's gravity has a signature we can test on paper. Its waves travel at
light speed and have only one shape: a stretch-and-squeeze across the
direction of travel.

We tried about a dozen ways of building gravity waves out of finite,
record-like variables on the fixed grid. Every one came out wrong in one of
two ways: the waves were too slow, or they were light-fast but dragged along
an extra sideways shake that Einstein's waves do not have.

The only construction we have that works gives every place in space extra
continuous numbers, its local lengths and angles. That puts Einstein's
geometry in as an assumption instead of deriving it.

The failure is proved only for small, smooth waves, and only in one model we
built ourselves. It is not proved for the framework's own one-qubit sites,
for strongly interacting states, or for non-local patterns.

Getting past the wall means one of two things:
- a finite-record version with light-fast waves of the one right shape;
- or a clear statement of which premise has to go: the finite qubit, the
  fixed grid, or gravity as a local wave pattern.

*Analogy (only an analogy):* a mattress made of springs that can only click
between a few positions. Push it and a ripple runs across. If the click rules
are rigid, the ripple crawls. Loosen them so the ripple runs fast, and it
starts rocking sideways as well as up and down.

### Precise version

- **Target.** A local (finite-range, analytic-symbol), stable
  (positive-semidefinite) harmonic model on the supplied tensor complex
  (vector stencil G, scalar stencil S, six slots per cell). The slots are
  finite, meaning finite-dimensional local Hilbert spaces, and the scalar
  (time) rule is exact. Its low-energy spectrum must be Einstein's linear
  spectrum: two pure-TT modes with ω ∝ |q| in every direction, and no other
  gapless mode.
- **Status.** Excluded, whatever the residual symmetry (probes 10–21; bounded
  theorems, unaudited):
  - exact transverse rules give ω = O(q²);
  - both TT polarisations linear in every direction force a linear mode
    with helicity ±1 weight on a dense set of directions.
- **What does not count as closure:** approximate Lorentz invariance with
  unequal partner speeds; a gapped tensor; ω ∝ q^n with n > 1; a spectrum
  with extra gapless modes.
- **Positive comparator.** The same complex with non-compact canonical pairs
  (continuous, unbounded h and π) gives exactly Einstein's linear spectrum
  (2026-09-24, unaudited).
- **The sharpest one-line form.** Einstein's linear graviton, in the
  comparator, is built from canonical pairs [h, π] = i. No finite-dimensional
  site can carry an exact canonical pair (the landed 2026-05-02 no-go, by
  trace). Every finite approximation tried so far breaks one of the
  graviton's two properties: speed or purity.
- **Progress would be:**
  - a finite-slot or one-qubit-per-site model, beyond harmonic order or in a
    strongly correlated phase, with Einstein's linear spectrum;
  - or a reformulation in which gravity does not need a lattice graviton
    mode;
  - or a proof that the wall is equivalent to one named premise (the price).
- **Leaned on:**
  - the supplied tensor complex and its two rules;
  - the harmonic comparators;
  - Einstein's linear spectrum as the target;
  - the landed CCR no-go;
  - the June induced-gravity lane;
  - panel strategy.

### What the axioms say / what we supplied / what was proved

| What the axioms say | What we supplied | What was proved |
| --- | --- | --- |
| Z³ with nearest-neighbour adjacency, translations and cubic rotations; no site privileged | a tensor carrier on Z³ with six slots per cell, and the stencils G and S | ω ∝ k² or k³ with exact rules (09-14) |
| one site's possibilities have algebraic presentation M₂(C) | finite slots of spin S, or qubit slots (not one qubit per site) | no exact canonical pair on M₂(C) (05-02) |
| one nearest-neighbour admissibility rule fixes each site's odds | exact local balance laws (Gauss laws) as the reading of that rule | finite slots with an exact additive law: the moves' low moments vanish (probes 10, 15, 17) |
| records form, one per site, permanent; only records are read | harmonic (small-wave) models with stable quadratic forms; local terms | light-like TT brings a light-like ±1 mode, any symmetry (probes 20, 21) |
| Admissibility is not a dynamics axiom; there is no time metric | a Hamiltonian, a time rule, a DeWitt kinetic term, Einstein's spectrum as the target | both rules soft: gapped (probe 18) |
| — | continuous canonical pairs (the comparator) | continuous pairs: Einstein's linear spectrum (09-24) |
| — | a metric degree of freedom (June lane) | given one, the matter induces G ~ a² (06-17) |
| — | tick rates and lengths per site (source-link clause C1, blocks 53–62) | the lapse algebra closes at linear order only at β = −α (112) |

**Reading.** Every entry in the middle column is supplied. The axioms say
nothing about gravity, dynamics or a metric. So the wall presses on the
supplied tensor-complex reading. It says that reading, built from finite
parts, cannot produce Einstein's linear graviton. It does not say the axioms
cannot. The middle column is also where the routes are.

### Blind check

A fresh agent (Claude Sonnet, no context, no files) was given the first draft
of the plain version.
- **Its restatement matched the precise version on all four points:** the
  goal, the failure, the scope and what passing means.
- **It flagged six unclear phrases, all now fixed:**
  - "records that lock in" was undefined;
  - "every time" gave no count;
  - "the only version that works" read as a general claim, where it should
    say "among those tried";
  - "by hand" did not say why that disqualifies it;
  - "simplest waves of one model" was ambiguous;
  - "which premise" named no candidates.
