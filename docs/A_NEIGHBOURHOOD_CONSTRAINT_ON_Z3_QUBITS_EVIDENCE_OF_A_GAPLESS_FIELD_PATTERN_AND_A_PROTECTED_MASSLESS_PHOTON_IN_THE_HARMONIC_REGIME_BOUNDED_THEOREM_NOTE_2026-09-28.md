---
claim_id: a_neighbourhood_constraint_on_z3_qubits_evidence_of_a_gapless_field_pattern_and_a_protected_massless_photon_in_the_harmonic_regime_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied model, not adopted: qubits on the Z^3 sites with exactly one odd coordinate (the links of the coarse cubic lattice of spacing 2), a hard neighbourhood constraint (ice rule: at every all-even site the six nearest neighbours balance, div E = 0) and nearest-neighbour ring-exchange moves at the two-odd sites (four in-plane neighbours flip together when they circulate); H = -K sum F_p + V sum F_p^2 in the constrained space. Pre-registered and passed: (T1) the constraint and moves are nearest-neighbour operations on single Z^3 sites' neighbourhoods; (T2) the moves keep the constraint exactly; (T3) at the Rokhsar-Kivelson point V = K (ground state = equal superposition of constrained configurations) the longitudinal field is exactly zero and the transverse two-point correlations are flat (3/2 by a sum rule; zero stiffness at this point), consistent with a Coulomb phase on 8^3 and 12^3 coarse tori; (T4) the single-mode (Feynman-Bijl) upper bound on the lowest excitation at wavevector q, omega_SMA = 8 K rho sin^2(q/2)/S_T(q), goes to zero as q -> 0 at each finite size (small-q exponent 2; fitted 1.85 with the lattice form factor); gaplessness in the infinite-size limit follows if S_T stays finite there, which the finite sizes support but do not prove; (T5) exact diagonalisation of the 24-qubit cluster reproduces the single-mode expression (1.600000); the lowest level at q = pi (momentum-projected) is 1.161, and the sector's lowest excitation (0.970) is at zero momentum; (T7) beyond the RK point on a 2x2x3 cluster (34,080 states) the bound holds at V/K = 1, 0.5, 0 and S_T at the smallest q falls (1.54, 0.89, 0.59): the mode stiffens, but linear vs quadratic is not decidable at these momenta; (T6) in the harmonic (weak-coupling) regime of the same lattice gauge theory there are exactly two massless polarisations with omega = |phat(k)|, random local gauge-invariant perturbations keep them massless (omega/|k| constant, ~4.06), and a gauge-breaking A^2 term gaps them. Not computed: the linear photon of the full quantum model (quantum Monte Carlo; literature reference only), the stability of the Coulomb phase, charges, and any link to Admissibility beyond a reading. The embedding types sites by coordinate parity, so the model is covariant only under translations by two sites and rotations about vertex or cube sites, while the axioms ask for full Z^3 covariance and a qubit at every site."
upstream_dependencies:
  - minimal_axioms
runner: scripts/a_photon_from_a_neighbourhood_constraint_on_z3_2026_09_28.py
---

# A neighbourhood constraint on Z^3 qubits: evidence of a gapless field pattern, and a protected massless photon in the harmonic regime

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a pre-registered test with exact checks, Monte Carlo and small
exact diagonalisation; a supplied model; unaudited. Independent checks are
recorded below.

## In one paragraph

Can the qubits and a neighbourhood rule be the force carriers themselves?
Here is one case where they are.
- **The rule.** Put qubits on every other site of `Z^3`. Around each
  remaining site, the six neighbouring qubits must balance: three pointing
  in, three out. The only allowed moves flip four qubits around a square
  together, which keeps every balance.
- **What appears.** Evidence of a wave of flipping that costs arbitrarily
  little energy at long wavelengths. At every size computed its energy bound
  falls toward zero. That this persists for an infinite lattice is
  supported, not proved.
  - At the special point computed exactly, its energy grows as the square
    of the wavenumber. It is massless but not yet light-like.
  - In the weak-coupling (harmonic) regime of the same theory it is a
    linear, two-polarisation photon.
- **Why it stays massless.** The balance rule is an exact local conservation
  law, a Gauss law. Any extra rule that respects the balance keeps the
  harmonic photon massless; only a rule that breaks the balance gives it a
  mass.
- **Not shown.** That the full quantum model has the linear photon. Small
  clusters beyond the special point show the mode stiffening, but cannot
  decide it.

That is the protection the gravity field (probe 6) lacked. Here the grid
supplies it through a neighbourhood constraint.

## Why this question

The owner's question (2026-09-28) was why the qubits and neighbourhood
record rules could not themselves be the force carriers and gravity, as
patterns of records. Probe 6 found that a field laid over a fixed grid stays
massless only if an exact local conservation law protects it. Qubit models
with a local constraint are the known way to get such a law and an emergent
photon (quantum spin ice; U(1) quantum link models; reference only: Hermele,
Fisher and Balents 2004; Banerjee et al. 2008; Shannon et al. 2012). This
note builds the smallest in-framework version and tests it against criteria
written before the run.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): `Z^3`, a qubit at each
  site, a nearest-neighbour rule, records. The memo supplies no Hamiltonian.
- **Supplied, not adopted: the embedding.** Type each site of a `Z^3` torus
  of size `2L` by how many of its coordinates are odd:
  - *none odd:* vertex (V);
  - *one odd:* link (E), with the odd axis as the link's direction;
  - *two odd:* plaquette centre (P);
  - *three odd:* cube centre (C).

  The E sites carry the qubits. Up or down is the field `E = ±1` along the
  link's positive axis. The other sites are spectators here.
- **The constraint (ice rule, a Gauss law).** At every V site, its six
  nearest neighbours satisfy `div E = sum_a (E(v+e_a) − E(v−e_a)) = 0`.
- **The moves (ring exchange).** At every P site, its four in-plane nearest
  neighbours flip together when they circulate. `F_p` is that flip.
- **The Hamiltonian** in the constrained space:
  `H = −K sum_p F_p + V sum_p F_p^2`.
  - At `V = K` (the Rokhsar–Kivelson, or RK, point) the ground state of each
    sector is the equal superposition of its constrained configurations.
  - Its correlations are those of the uniform constrained ensemble.
- **Pre-registered** (in the runner's header, written before running):
  - P1: the embedding is nearest-neighbour.
  - P2: the moves keep the constraint.
  - P3: the transverse field fluctuations stay finite as `q -> 0`, with
    `S_T` at the smallest `q` at least `0.1` of its value at `q = π`.
  - P4: the single-mode bound goes to zero, with exponent in `[1.7, 2.3]`.
  - P5: exact diagonalisation agrees.
  - P6: in the harmonic regime, two protected massless polarisations.
  - FAIL if `S_T(q -> 0) -> 0` or the bound stays finite.

## T1 — the rule is a neighbourhood rule of Z^3

On a `6^3` torus: 27 vertex sites, 81 link sites (the qubits) and 81
plaquette sites.
- Every vertex site's six nearest neighbours are link sites.
- Every plaquette site's four in-plane nearest neighbours are link sites;
  its out-of-plane neighbours are not.

So the constraint lives on one site's neighbourhood, and so does each move.

*A reading note.* As a conditional rule for one qubit, the constraint
reaches the other links of its two vertices. These are at distance `√2`,
next-nearest in `Z^3`. The link is reached through the shared vertex site,
which is a nearest neighbour.

## T2 — the moves keep the rule

1197 ring-exchange flips on a `4^3` coarse torus leave every vertex
balanced; the largest divergence afterwards is `0`. The Monte Carlo's loop
updates reverse closed loops of arrows, so they also keep the rule.

## T3 — the constrained qubits carry a unfrozen transverse field

The uniform ensemble of constrained configurations is the RK ground state's
weights. It was sampled by long-loop Monte Carlo on `8^3` and `12^3` coarse
tori (1536 and 5184 qubits), 400 samples each. Six transverse components
were averaged: three directions of `q`, two polarisations each.

| `q` | `0.52` | `0.79` | `1.05` | `1.57` | `3.14` |
|---|---|---|---|---|---|
| `S_T` (`12^3`) | `1.49` | – | `1.51` | `1.46` | `1.60` |
| `S_T` (`8^3`) | – | `1.57` | – | `1.46` | `1.47` |

- The longitudinal part is exactly zero, at `7e-31`. That is the Gauss law,
  configuration by configuration.
- The transverse part is flat down to the smallest `q`, at `3/2`.
  - That value is fixed by a sum rule: three components per cell, with the
    longitudinal one exactly zero.
  - Flatness is the mark of this special point, where the field has no
    stiffness and the photon's speed is zero. In a linear-photon phase the
    transverse fluctuations fall like `|q|`.
  - So T3 shows a divergence-free ensemble with flat, unfrozen transverse
    two-point correlations. That is consistent with a Coulomb phase, but two
    points of correlation do not establish one. It is not a linear photon.
  - Standard errors are `0.03–0.04` per point, with samples separated by
    `L^3/8` loop updates and autocorrelation not estimated. The Fable
    check's independent sampler found the same flat value to `24^3`
    (`1.498 ± 0.014`). This is the classical Coulomb phase of ice (Henley
    2010; reference only). That `S_T` stays finite in the infinite-size
    limit is supported, not proved.
- *A correction to the pre-registration.* Its FAIL clause read
  "`S_T(q -> 0) -> 0`" as the absence of a free field. That was
  mis-specified: `S_T ∝ |q|` is what the linear-photon phase does. The Fable
  check caught it. The clause is withdrawn, and the remaining FAIL condition
  (the bound staying finite) stands.
- The fraction of flippable plaquettes is `0.26`.

## T4 — the excitations are gapless

The single-mode (Feynman–Bijl) state `A|psi_0>`, with `A` the transverse
field at wavevector `q`, bounds the lowest excitation at that wavevector from
above:
- `E_min(q) <= ω_SMA(q) = f(q)/S_T(q)`;
- `f(q) = (1/2)<[A^†, [H, A]]> = 8 K ρ sin^2(q/2)` per cell, where `ρ` is
  the flippable fraction. The diagonal `V` term commutes with `A` and does
  not enter.

| `q` | `0.52` | `0.79` | `1.05` | `1.57` | `2.09` | `3.14` |
|---|---|---|---|---|---|---|
| `ω_SMA/K` | `0.094` | `0.193` | `0.345` | `0.71` | `1.00` | `1.30–1.41` |

- The bound goes to zero at long wavelength. At small `q` its exponent is 2;
  the fitted `1.85` includes the lattice form factor `sin^2(q/2)`.
- So at each finite size the constrained qubits have low-energy excitations
  at the longest wavelength. In the infinite-size limit they are gapless if
  `S_T` stays finite, which T3 supports.
- The bound is rigorous at each finite size. Gaplessness in the
  infinite-size limit needs `S_T(q -> 0) > 0` there, which T3 supports
  numerically but does not prove.

## T5 — exact diagonalisation on the smallest cluster

`2x2x2` coarse cells (24 qubits):
- 9600 constrained configurations; 864 in the reference sector (connected by
  moves).
- The RK ground state has energy exactly `0`.
- `<psi_0|A|psi_0> = 1e-17`, so `A|psi_0>` is orthogonal to the ground
  state.
- The single-mode energy at `q = π` is `1.600000`, both directly and from the
  formula.
- The lowest level at `q = π`, found by Lanczos projected onto that
  momentum, is `1.161`, below the bound as it must be.
- The sector's lowest excitation (`0.970`) is at zero momentum. An earlier
  version said it was reached from `A|psi_0>`. That came from rounding error
  leaking into another momentum sector (the Fable check caught it).

## T6 — in the harmonic regime the photon is massless and protected

Treat the same lattice gauge theory in its weak-coupling (harmonic) regime:
`H = (U/2) sum E^2 + (K/2) sum (curl A)^2`, with the exact lattice Gauss law.
- This rotor model, with continuous `A` and `E`, is a separate weak-coupling
  model, the usual effective theory of the Coulomb phase. It is not derived
  from the spin-1/2 Hamiltonian: for `E = ±1`, `sum E^2` is a constant.
- The perturbations and mass term used are stated in the runner's header
  (couplings, seed and `m^2 = 0.05`).
- **Two polarisations.** The curl symbol has one zero mode per `k`, which is
  the gauge mode the Gauss law removes, and two modes with
  `ω = sqrt(UK) |p̂(k)|`, `p̂ = 2 sin(k/2)`. They are linear, with
  `ω/|k| = 0.995–0.9999` as `|k|` goes from `0.4` to `0.05`.
- **Gauge-invariant perturbations keep them massless.** Random local
  perturbations built from `curl A` and `E` change the speed but keep `ω`
  proportional to `|k|` (`ω/|k| = 3.89, 4.02, 4.06, 4.06`).
- **A gauge-breaking `A^2` term gaps them.** The minimum `ω` tends to
  `0.37` as `k -> 0`.

This is the contrast with probe 6. The member's mass-type terms were allowed
by every symmetry the lattice keeps. Here the lattice keeps an exact local
law, the Gauss law, and it forbids the mass.

What the Gauss law does and does not do:
- *It does:* forbid a mass term inside the Coulomb phase.
- *It does not:* guarantee that the phase is the Coulomb phase. Strong
  gauge-respecting terms can confine or order the system (T7 hints at an
  ordering channel for `V <= 0`). Some local harmonic terms can also remove
  the Maxwell stiffness and leave `ω ~ q^2`.
- So "protected" means protected against gaining a mass, within the phase.

## T7 — beyond the special point: the mode stiffens; linear or not is undecided

On a `2x2x3` cluster (34,080 states in the reference sector), at the
smallest `q = 2π/3`:

| `V/K` | lowest level at `q` | single-mode bound | `S_T` |
|---|---|---|---|
| 1 | `0.755` | `1.222` | `1.540` |
| 0.5 | `1.706` | `2.183` | `0.886` |
| 0 | `1.727` | `3.175` | `0.586` |

- The bound (a direct Rayleigh quotient here; the RK-point formula with the
  flippable density does not extend away from RK) holds.
- `S_T` falls as `V` drops below `K`: the transverse fluctuations are
  suppressed, as a photon gaining stiffness would do.
- These momenta are too large to tell linear from quadratic dispersion.
- The Fable check went further, to `2x2x4` with 1.55 million states. There
  the ratio of energies at `q = π/2` and `π` flattens as `V` decreases (from
  `0.64` to `0.98`), and at `V <= 0` other excitations drop below this mode:
  a possible ordering channel.
- So the linear photon of the full model is neither shown nor refuted here.
  Quantum Monte Carlo on larger lattices is what the literature used
  (reference only).

## What this means

- **A force carrier can be a pattern of the qubits under a neighbourhood
  rule, as far as this model goes.**
  - A constraint of the form "around each site, the neighbours balance"
    gives, on the evidence here, a gapless field pattern. The infinite-size
    limit is supported, not proved.
  - In the harmonic regime it is a two-polarisation photon whose
    masslessness is protected by the constraint itself, not by tuning.
  - What remains open is the light-like (linear) dispersion in the full
    quantum model, and whether the model's phase is the photon's at all
    (T7).
  - So the owner's question gets a qualified yes for light: the
    mechanism works; that this model realises it is not yet shown.
- **In records language.** Read "up" as a record present and "down" as none.
  - The rule balances directions, not counts. Around a vertex there can be
    0, 2, 4 or 6 records; all six is allowed. An earlier version, and an
    update to the owner, said "exactly three"; that was wrong.
  - Each move shifts two records across a square, through the vertex site.
  - In the zero-winding sector the total is half the links, and moves keep
    it. The number of records is conserved, as probe 7 requires.
  - A photon is then records circulating around squares.
  - Three tensions with the axioms remain.
    - As presence, a flip either moves two records, each by two
      nearest-neighbour steps through a spectator vertex site, or deletes two
      and creates two. The first needs an identity rule and a record passing
      through a site (probe 8's question). The second violates permanence.
    - Reading "up" as a record's content would mean the content changes.
      The Record axiom's "locks" forbids that, unless the record reading is
      presence, not content.
    - The embedding types sites by coordinate parity: qubits sit on 3/8 of
      the sites, and orientation depends on position. So the model is
      covariant only under translations by two sites and rotations about
      vertex or cube sites. The axioms ask for full `Z^3` covariance and a
      qubit at every site.
- **For the Admissibility axiom.** The ice rule is the sharp limit of a
  nearest-neighbour rule: probability zero for any content that unbalances a
  neighbouring vertex. Whether the owner's Admissibility can be read this
  way, or produces such a constraint, is a reading question. It is the
  concrete question this model poses.
- **For gravity.** The tensor version of this construction (a tensor Gauss
  law; Pretko 2017; Xu 2006; reference only) is the analogous test for a
  protected massless spin-2 pattern. The universality question of the second
  panel then applies.

## No-Go Discipline Gate

Recorded per `docs/ai_methodology/skills/no-go-discipline/SKILL.md`. The claim
is mostly positive: a gapless pattern exists, and gauge-invariant
perturbations keep the harmonic photon massless. The walled parts are named
below.

- **N1 — routes the claims could fail by:**
  1. *The RK ensemble could be ordered, so `S_T -> 0`* — ATTEMPTED (T3),
     not so.
  2. *The bound could stay finite* — ATTEMPTED (T4). It goes to zero at each
     finite size. The infinite-size limit is supported, not proved.
  3. *A small-cluster artefact in the bound* — ATTEMPTED (T5), the formula
     matches exactly.
  4. *Gauge-invariant perturbations could gap the harmonic photon* —
     ATTEMPTED (T6), they do not.
  5. *Away from the RK point the quantum model could confine, or order* —
     NOT ATTEMPTED. The literature says 3+1D compact U(1) has a stable
     Coulomb phase near the RK point for `V < K` (reference only). It is not
     re-proved here.
- **N2 — independence.** Three walls, all independent:
  - W_a: the linear photon of the full model is not computed;
  - W_b: the reading of Admissibility as a constraint;
  - W_c: covariance, the parity typing of sites.
- **N3 — hidden-wall scan.** "Harmonic (weak-coupling) regime" is a stated
  approximation, not hidden. No other scanned phrase is load-bearing.
- **N4 — residual matching.** The literature is cited as reference for W_a,
  not as a witness for the computed claims.
- **N5 — rhetoric audit.** The title says "gapless field pattern" and "a
  massless photon in the harmonic regime", which is what is shown. "Light-like"
  is used only for the harmonic regime.
- **N6 — primitive scan.** No registered primitive supplies a constraint or
  Hamiltonian. The model is supplied.
- **N7 — steelman.**
  - *The case against.* At the RK point the "photon" is quadratic, not
    light-like. The harmonic analysis presupposes the Coulomb phase it
    claims to show. So the note shows a gapless mode and a protected
    harmonic photon, not that this qubit model has light.
  - *Terminal obligation.* Show the linear photon in the full quantum model
    at `V < K`, for example by quantum Monte Carlo of the ring-exchange model
    on the embedded lattice.
  - *Disposition.* Stated as the open wall; the claim is scoped
    accordingly.
- **N8 — cross-cycle echo.** Probe 6 (no exact law, so the mass is
  unprotected) is the contrast. Probe 7 (the record count is fixed) is
  consistent with the records reading above.
- **Outcome: PASS** as scoped.

## What this does not show

- **The full quantum phase.** The linear photon away from the RK point is not
  computed. It needs quantum Monte Carlo, which exists in the literature for
  quantum spin ice (reference only) but is not re-derived.
- **Charges.** Violations of the ice rule, the model's electric charges, are
  not studied.
- **Admissibility.** No link to the owner's rule beyond a reading. This is a
  supplied model embedded in `Z^3`, with spectator sites and a parity typing
  of sites. It is not a model of the axioms as written:
  - the axioms' per-site probability distribution is not supplied;
  - a qubit's allowed value depends on links at distance `√2`, through the
    shared vertex site.
- **Other forces and gravity.** Neither non-abelian gauge fields nor the
  tensor (gravity) version is built.

## Independent checks

- **Claude Fable 5.1 subagent**, working from its own code (same vendor
  family, so not a referee).
  - **Verdict: "confirmed with corrections".**
  - Every number reproduced by different methods: a short-loop worm sampler
    validated against exact counts on `2x2x2` and `2x2x3` (flippable
    fraction `0.2594` on `8^3`, flat `S_T = 3/2` to `24^3`); an independent
    derivation of `f(q)`; transfer-matrix counting (9600, 864); the
    harmonic checks.
  - **Applied:**
    - T5's momentum-sector error;
    - the records count ("exactly three" is wrong: 0, 2, 4 or 6);
    - the inverted FAIL clause;
    - the covariance wall;
    - the overstated title;
    - its beyond-RK exact diagonalisation (T7).
- **Codex `gpt-5.6-sol` referee**, at xhigh. Another vendor family; it read
  the first version.
  - **Verdict: "fails".**
  - Reproduced: 9600, 864, `ρ = 1/3`, `S_T(π) = 5/3`, the bound `1.6`, the
    level `0.9696`, the harmonic spectrum, and flat `S_T` on `8^3` and `12^3`
    with its own directed-loop sampler.
  - Its findings:
    - gaplessness not proved in the infinite-size limit;
    - "light-like" and "protection" overreached;
    - the harmonic model was not derived from the qubit model, and its
      parameters were missing;
    - the momentum-sector misreport in T5;
    - the SMA normalisation needs the orientation-specific density;
    - the model is not the axioms' nearest-neighbour rule;
    - the records encoding was wrong.
  - **Applied:** the title and summary are narrowed; the gaplessness is
    marked "supported, not proved", with errors and the Fable check's `24^3`
    data; the harmonic model is marked a separate approximation, with its
    parameters stated; "protected" is scoped to "against a mass, within the
    phase"; T5 is fixed; the axiom fit and the records encoding are
    restated as incompatibilities, not tensions.
  - The orientation-specific density equals the global flippable fraction
    by cubic symmetry of the ensemble. The runner averages over all three
    orientations.
- **Codex `gpt-5.6-sol`, second round.**
  - Resolved: 2, 3, 4, 5, 7, 8, and T7. The referee independently
    reproduced 34,080 states and every gap, `S_T` and bound.
  - Partly resolved: the unconditional gaplessness wording (item 1) and the
    "free/Coulomb" wording (item 6).
  - Both are now rephrased as evidence consistent with a Coulomb phase, with
    the infinite-size limit supported, not proved.

## Reproduction

```bash
python3 scripts/a_photon_from_a_neighbourhood_constraint_on_z3_2026_09_28.py
```

Expected: `TOTAL: PASS=7 FAIL=0` (about 45 seconds).
