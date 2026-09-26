---
claim_id: round_five_synthesis_one_exact_identity_per_block_of_the_third_campaign_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Collects the third campaign's blocks (open PRs 9255, 9258, 9263, 9264, 9265 and 9268, and draft PR 9266) on two supplied models, the composite-site network in the six-Majorana representation and the link-qubit ring clause with and without a single-link term and charge mass, and recomputes one exact identity per block by exact linear algebra on small clusters: the projection rule gives the exact 16-qubit ground energy on 8 sites; the matching bound at J_z = 2.5 on 256 sites (z-part singular values 5, x- and y-part norms 2, every level at least 1); the section flux on 2^3 (equal on every plane, conserved by every flip) with the exact sector grounds; the averaged f-sum 2 u s^2 on the exact 2^3 component; the f-sum with the single-link term, 2 u s^2 + (2t/3N) sum <sigma^x>, and the central differences that estimate <sigma^x>. The finite diagnostics are quoted from the blocks, not recomputed. No limit, phase or physical-field claim."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - gaussian_lattice_maxwell_comparator_gives_a_linear_size_independent_transverse_structure_factor_and_misses_the_pure_ring_level_step_bounded_theorem_note_2026-09-24
runner: scripts/round_five_synthesis_one_exact_identity_per_block_of_the_third_campaign_2026_09_25.py
---

# Round five: one exact identity per block of the third campaign

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied models recomputed in one runner; the blocks' finite diagnostics are quoted; unaudited.

## Result

The third campaign ran seven blocks on two supplied models, each opened as a
note, runner and cache: the composite-site network's flux sector (open PR
9255) and its excitations (open PR 9264); the ring clause's winding-sector
coupling (open PR 9258), its energy-only photon bound on 20³ (open PR 9265),
and the ring clause with a charge-creating single-link term (open PRs 9263
and 9268, and draft PR 9266). This runner recomputes one exact identity from each, from the
model's definition and without Monte Carlo, in about ten seconds.

| block | identity recomputed here | value |
|---|---|---|
| open PR 9255 | the projection rule's lowest physical energy over the 32 sectors of the 8-site cluster equals the exact ground energy of the 16-qubit spin model | `−35.66888833` at `J = (1, 1, 2.5)`, `−23.61311995` at `(0.4, 1, 1.6)`; differences `1.4 × 10⁻¹⁴`, `9.9 × 10⁻¹⁴` |
| open PR 9264 | at `J_z = 2.5`, `κ = 0` on 256 sites the z-bond part has every singular value 5 and the x- and y-bond parts norm 2, so every level of every winding class is at least 1 | singular values `5.000000000000`; norms `2.000000000000`; lowest level `1.000000000000` |
| open PR 9258 | on 2³ the section flux is the same through every plane for each of the 9600 ice states and is conserved by all 49920 plaquette flips | exact sector grounds `−9.026721` (880 states) and `−7.399111` (464 states); comparator reading `L [E(1) − E(0)] / 2 = 1.62761` |
| open PR 9265 (bound of open PR 9236) | the cyclic-triple first moment on the exact 2³ component equals `2 u s²` without any symmetry of the state | `3.008906971` for both, each mode `3.008907` |
| open PR 9263 and draft PR 9266 | with the single-link term on the six links at one vertex of 2³ (184320 states), the averaged first moment equals `2 u s² + (2t/3N) Σ ⟨σ^x⟩`; central differences of the energy estimate `Σ ⟨σ^x⟩` | `3.053953358` at `(t, M) = (0.8, 1.5)` and `3.023601331` at `(0.4, 2)`, differences below `10⁻¹⁴`; `Σ ⟨σ^x⟩ = 0.918975` at `t = 0.4` against `0.919318` and `0.920343` from steps `0.05` and `0.1` |

The identities are exact statements about the supplied models; the
finite-cluster and projector diagnostics of the blocks stand on their own
runners and are quoted below, not recomputed.

## What the third campaign's blocks say together

Two supplied models carry this round: the link-qubit ring clause (the
photon lane) and the composite-site network (the fermion lane). Each
block is a note, runner and cache; the identities above are recomputed
here exactly, and the finite diagnostics below are quoted from the blocks.

**The ring clause, pure-ring point.** The electric coupling of the
Gaussian comparator, read from the transverse response and from the
uniform-field (winding) sectors, differs strongly between the two routes on
4³ and agrees within errors on 8³ (open PR 9258); the static pair through
its core reads higher (open PR 9244). On 20³ the energy-only susceptibility
is `0.990 ± 0.032` at `k = π/10` and `1.096 ± 0.038` at `π/5`, flat like the
16³ values, so the moment chain bounds the lowest transverse excitation by
about `1.07 s(k)` and `1.02 s(k)` (open PR 9265).

**Moving charges.** With a single-link term that creates and moves unit
charges and a charge mass `M = 2`, the moment bound keeps a part that does
not vanish at small momentum, so energies alone no longer force a linear
bound (open PR 9263). The ground state changes fastest between
`t = 0.25` and `0.5`, and weak hopping leaves the transverse susceptibility
of 6³ within errors of the pure-ring value. A fine scan on 4³–10³ put the
steepest rise between `t = 0.35` and `0.45` on every torus but exposed a
fixed-population bias that depends on the guide's charge penalty (0.6 per
cent of the energy on 6³ between two penalties), so its size trend is not
established; it is preserved as draft PR 9266. With one penalty for a whole
grid, link expectations on 6³ still differ by up to 0.08 between penalties
0.8 and 1.1 across `t = 0.30–0.50` (open PR 9268): the several-fold rise
holds at both, but where it is steepest and how it changes with size are
open, and open PR 9263 now says so.

**The composite-site network.** With the projection exact, the ground
state lies in the locally flux-free sector on the clusters searched, with
one exception at `κ = ±0.3` on 32 sites (open PR 9255). Inside that sector
the physical ground class keeps constraint product `+1` on clusters up to
4000 sites, the lowest excitation with the same bonds is a fermion pair
whose energy falls roughly as `1/L` at isotropic couplings, the odd term
thins the low levels, and `J_z = 2.5` stays gapped by the matching bound
(open PR 9264).

## What stays open

- **Moving charges.** Whether the rapid change near `t ≈ 0.3–0.5` at
  `M = 2` sharpens with size needs guide-independent link expectations:
  larger populations with an extrapolation in the inverse population, or a
  guide with charge-pair correlations, checked by two guides on each torus
  (draft PR 9266, open PR 9268); the
  static pair energy with moving charges (whether the charges screen it)
  needs static sources in the charge projector; the moment bound cannot
  show or exclude a transverse gap once the single-link term is on.
- **The pure-ring photon.** Tori beyond 20³ need a resampling step below
  `0.02` or a better guide; two seeds on 20³ leave the error heuristic.
- **The composite-site network.** The flux sectors at `κ ≠ 0` on clusters
  larger than 32 sites, the node set at `κ = 0` (line or points), and the
  energies of winding-class and bond-sector excitations.
- **Gravity.** The scoping of the tensor sector against the landed
  finite-clock theorem is deferred to a design session.

## What this does not do

- It recomputes identities; it does not re-run or re-weigh the blocks'
  Monte Carlo or finite-cluster diagnostics, which are quoted.
- It claims no limit, phase, transition or physical-field identification,
  names no graph, and compares no number with a measured value.
- It adopts no clause, network, representation, comparator or method.

## Prior art (not premises)

As in the blocks: Kitaev 2006; Yao and Lee 2011; Hermele, Fisher and
Balents 2004; Fradkin and Shenker 1979; the f-sum rule and moment
inequalities of linear response. All cited as prior art, not as premises.

## Checks

The runner has five checks, one per identity above; the fresh run takes
about ten seconds and uses no Monte Carlo.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the supplied models, clusters and couplings named in each check.
- **N2 — Independence:** self-checked; each identity is recomputed here from the model's definition, not read from the blocks' caches.
- **N3 — Imports:** the networks, clauses, representations and comparators are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern; open PRs are cited, not relied on.
- **N5 — Resolution:** floating-point exact diagonalization, determinants and singular values.
- **N6 — Residuals:** the open items above.
- **N7 — Counterroutes:** other clusters, couplings, representations and estimators remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
