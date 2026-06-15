# Gauge holonomy suppresses r below the leptonic value — wrong ordering for the sector spread (narrow no-go)

- **Date:** 2026-06-15
- **Type:** narrow no-go
- **Claim type:** narrow_no_go
- **Status:** source note awaiting independent audit handling.
- **Primary runner:** [`scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py`](../scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py)
- **Cached output:** [`logs/runner-cache/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.txt`](../logs/runner-cache/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.txt)

## Claim

The sector dial `r = |b|²/a²` (Koide Q = 1/3 + 2r/3) sits at different values per fermion sector
(charged leptons r = 1/2, down-quarks r ≈ 0.597, up-quarks r ≈ 0.773). One proposed origin — the
"colour-dressed" channel left open by the unaudited
`flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (context only, no dep edge)
— is that the gauge connection dresses the generation coupling sector-dependently, since the b-term
(the C₃[111] doublet coupling) is a hop-**return** that traverses a gauge link
([`koide_gamma_axis_covariant_full_cube_orbit_law`](KOIDE_GAMMA_AXIS_COVARIANT_FULL_CUBE_ORBIT_LAW_NOTE_2026-04-18.md))
while the a-term (the singlet coupling) is **on-site** and carries no link. The link-dressed
covariant-hopping form is retained
([`matter_gauge_minimal_coupling_fiber_frame_forces_connection`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md),
[`fiber_frame_local_redundancy_bridge`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md)).

**This note shows that channel gives the wrong sign of spread, so it cannot be the origin.** Dressing
the hop with a background link U in gauge representation R and forming the gauge-invariant
(fibre-averaged) effective generation operator yields

> b_eff = b · χ_R(U)/d_R,  a_eff = a,  hence **r_R = r₀ · |χ_R(U)/d_R|²**,

where χ_R(U) = Tr_R(U), d_R = dim R, and r₀ = |b|²/a² is the trivial-rep (colourless / leptonic)
value. Because |χ_R(U)| ≤ d_R for every unitary (a sum of d_R unit-modulus eigenvalues), the
normalized character satisfies |χ_R(U)/d_R| ≤ 1, so

> **r_R ≤ r₀ for every representation and every background, with equality iff U is a centre
> (scalar-phase) element.**

A gauge-invariant hopping holonomy can therefore only **suppress** r for a nontrivial-rep (coloured)
sector *below* the trivial-rep (leptonic) value. But the observed quarks sit **above** the leptonic
value (r_down ≈ 0.597 > 1/2, r_up ≈ 0.773 > 1/2). The mechanism predicts r_coloured ≤ r_lepton; the
data has r_coloured > r_lepton. **The gauge-holonomy channel gives the wrong ordering — falsified as
the spread source.** This note forces **no** value of r: r₀ is a free bare coupling and the result is
the inequality r_R ≤ r₀.

## The no-go

**(N-bound) The character inequality caps coloured r at the leptonic value.** For any rep R and any
unitary background U, |χ_R(U)| ≤ χ_R(I) = d_R (the eigenvalues of U in rep R all have modulus 1).
The on-site a-term carries no link (a_eff = a, independent of U; verified in the runner), while the
hop-return b-term carries the link, so the gauge-invariant effective doublet coupling is
character-normalized: b_eff = b·χ_R(U)/d_R. Hence r_R = r₀·|χ_R(U)/d_R|² ≤ r₀, with equality only for
a centre element. The runner confirms r_R ≤ r₀ over 800 random unitaries across reps d ∈ {1,2,3,8},
the equality-iff-centre dichotomy, and strict suppression for generic backgrounds. (This is the
standard lattice-gauge fact that gauge-invariant coloured hopping amplitudes are character-suppressed
relative to colourless ones.)

**(N-order) The observed spread violates the cap.** The colourless leptons realize the unsuppressed
bound r_lep = r₀; any coloured sector is bounded by r_coloured ≤ r₀ = r_lep. The observed ordering is
the reverse: r_lep = 1/2 < r_down ≈ 0.597 < r_up ≈ 0.773. So the holonomy mechanism predicts coloured
sectors with *smaller* r than leptons, while reality has *larger*. The channel produces the wrong
sign of the spread.

**(N-either-horn) The result is robust to whether the b-term carries a link at all.** If the b-term
*does* carry a gauge link (the covariant-hopping reading), the holonomy is character-suppressed and
gives the wrong ordering (above). If the b-term carries *no* link (the reading on which the circulant
C is a linkless generation relabeling), then U never enters and r_R = r₀ is rep-independent — **no
spread at all** (runner: U = I gives r_R = r₀ for every rep). Either way, the gauge-connection channel
cannot source the observed sector spread.

## Significance

This decisively closes the "colour-dressed" covariant-hopping channel — the one open path named by the
preceding sector-blindness no-go — in its holonomy form. It also resolves a genuine ambiguity about
that channel: the holonomy neither trivially cancels (it does enter r, via the normalized character)
nor opens a free spread (it is bounded above by the trivial-rep value). The sharp content is the
**direction**: a gauge-invariant holonomy can only push coloured r *down* toward the degenerate
r = 0 endpoint, never *up*. Since the colourless leptons already sit at the channel's ceiling and the
coloured sectors are observed *above* it, the splitter that raises r for coloured sectors must live in
a channel that is **not** a gauge-invariant hopping holonomy — i.e. in the within-sector measure /
weighting prior (where the records campaign already localized it: PRs #4006/#4009/#4010/#4020) or an
electroweak-partner (within-doublet, T₃-asymmetric) channel. The next path this opens is that
measure/partner channel; the gauge-holonomy avenue for the spread is closed.

## Boundary (honest)

- Forces **no** value of r; r₀ is a free bare coupling and the result is the inequality r_R ≤ r₀.
  Does not derive or force r = 1/2 (the firewall holds: r is registered, sector-dependent data).
- Closes the gauge-invariant **hopping-holonomy** channel as the spread source. It does **not** close
  the within-sector measure / weighting-prior channel, nor an electroweak-partner channel — those are
  the next paths, explicitly left open.
- Uses the standard identification "colourless lepton ↔ trivial rep, coloured quark ↔ nontrivial rep."
  The bound r_R ≤ r₀ is rep-agnostic (any nontrivial rep is capped by the trivial one), so the
  conclusion is robust to the precise rep assignment; only the labelling of which sector is
  unsuppressed uses the identification.
- The fibre-average is the gauge-invariant (colour-singlet) effective generation operator; an
  un-traced coloured amplitude is gauge-variant (not a registered observable). A colour-*resolved*
  spectral/conjugacy-class reading is a distinct gauge-invariant object that does not equal the
  fibre-averaged operator — but it gives no character enhancement beyond r₀ either (it generically
  introduces colour-dependent splitting rather than a single 3-generation sector), so it does not
  rescue the holonomy channel as a source of r_coloured > r_lepton. The bound is on the colour-singlet
  generation operator.

## Dependencies

Dependency edges (retained):
- [`matter_gauge_minimal_coupling_fiber_frame_forces_connection`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md) — the covariant-hopping form H_cov = Σ aₓ† U_μ(x) a_{x+μ} + h.c. (the link rides the hop, not the on-site term).
- [`fiber_frame_local_redundancy_bridge`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md) — the link law U_xy → gₓ U_xy g_y† and the fibre V_x.
- [`koide_gamma_axis_covariant_full_cube_orbit_law`](KOIDE_GAMMA_AXIS_COVARIANT_FULL_CUBE_ORBIT_LAW_NOTE_2026-04-18.md) — the b-term is the C₃[111] second-order hop-return (traverses a link); the a-term is on-site.
- [`koide_circulant_character_bridge`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) and [`koide_kappa_spectrum_operator_bridge`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) — H = aI + bC + b̄C², r = |b|²/a², Q = 1/3 + 2r/3.
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — the gauge-uniform shared M₃(ℂ) generation carrier (the link acts on the fibre, not the generation index).

Context (no edge): `flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (unaudited;
the note whose open "colour-dressed" path this closes in its holonomy form);
`flavor_hw1_staggered_projection_democratic_r0` (retained_no_go; the bare undressed generation hop
gives r = 0 — the r₀ → 0 endpoint the suppression points toward).

## Forbidden-imports check

No new axiom. The covariant-hopping vehicle is retained (not an admission). The background link U is a
free probe (the gauge action that would set its value is unaudited — but the bound r_R ≤ r₀ holds for
*every* U, so no background value is assumed or fitted). The observed r values enter only as anchors
for the ordering contradiction, never as derivation inputs. r₀ and the per-sector couplings are free
symbols; no r value is computed or forced; Q = 1/3 + 2r/3 is the standard Koide-block relation.
