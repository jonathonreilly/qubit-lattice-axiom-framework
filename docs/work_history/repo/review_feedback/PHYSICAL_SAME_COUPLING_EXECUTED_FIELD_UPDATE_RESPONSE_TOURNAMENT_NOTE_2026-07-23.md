# Same-parameter executed positive field-update response support test

Date: 2026-07-23

**Type:** meta

Authority: none

Audit: unset

Scope: historical bounded-support packet. It is not source or audit authority,
and no dependent may consume it as a physical coupling, source/action,
observable, energy, stress, or gravity bridge.

Cycle claim: 681 (claimed strictly above the joint visible max 680 at freeze:
680 is this lane's evaluator campaign claim, 679 the Record/Born
discriminator PR, campaign tip `fb0ab5636e` filenames reach 678). Descriptive
filenames per the owner directive; the cycle number appears only in runner,
receipt, and note content.

## Submitted question and conjunctive success gate

Does an EXECUTED, exactly time-reversible, finite-step field update on two
declared positive-sector carriers — with ONE declared coupling parameter q
entering BOTH the source insertion and the receiver readout — reproduce the
literal transcribed Cycle-626 stationary q^2 comparator in the adiabatic limit
at the submitted frozen convergence rate without refit, with simultaneous
q-sign cancellation holding in the executed update and flipping when the
source and readout parameters are decoupled — while claiming no physical
coupling, energy, stress, source, gravity, rate, time, or receiver-association
content? The q_rec = 0 row is only a definition/wiring control.

The submitted runner declares seven success gates. The repository contains no
independently timestamped preregistration artifact, so this note does not claim
temporal preregistration. The gates are: exact
reversibility and symplecticity with bounded quadratic energy; both carriers
positive with the literal transcribed Cycle-626 comparator eigenvalues matched;
adiabatic convergence to the independently solved stationary value at the
submitted frozen rate p = 2; the same-parameter sign law (even in q, decoupled
readout sign flips, receiver-zero definition control); q^2 response scaling;
the declared D2 near/far inequality against frozen far controls; and
kick/drift ordering agreement
within the declared O(dt^2) bound with one shared adiabatic limit.

## Construction

Carriers (declared supplied structure, constructed in-run): D1, the standard
periodic combinatorial Laplacian constructed directly on the L3/L6/L7 cubic
site sets used by Cycle 576, restricted to the zero-mode-removed P0 sector;
D2, the real finite-difference scalar Laplacian on L interior points per axis,
with homogeneous Dirichlet values outside the grid (no zero mode). No Cycle-576
graph object is imported. The literal transcribed Cycle-626 comparators match:
D1 P0 minimum nonzero eigenvalue 0.75302 at L7 (the 0.753 anchor; L3/L6 give
3.0/1.0 by construction), and D2 minima 1.75736 / 0.59419 / 0.45672 on
L3/L6/L7 against the 1.757 / 0.594 / 0.457 anchors — all within 1e-3, no
tuning. These absent campaign artifacts are provenance only, not independently
authenticated authority. Both carriers are strictly positive on the tested
sectors.

Source and receiver: bounded, non-negative, disjoint-support profiles built
from the reviewed Cycle-576 `source_profiles` function — the TRAIN_XY texture
windowed
to a declared ball and made non-negative (|texture|; the windowing and sign
drop are declared supplied structure). The parent supplies only the site-set
convention and texture function; it does not supply these windowed profiles or
the carriers. Frozen near and far receiver displacements per (carrier, size);
the support-overlap
census is empty on every fixture.

Executed update: leapfrog / Stormer-Verlet at dt = 0.01 in both kick-drift-
kick and drift-kick-drift orderings, with the quartic ramp g = 4u^3 - 3u^4 on
[0, tau] then a fixed hold window (g''(0) = 0 removes the ramp-start endpoint
oscillation; g''(tau) != 0 leaves the clean tau^-2 non-adiabatic envelope,
which supplies the submitted frozen target p = 2). ONE declared scalar q is
wired to both the source insertion q g(t) <rho_src, phi> and the defined readout
q <rho_rec, phi>; the decoupled arm introduces a second constant explicitly
and only as the falsifier.

Executed diagnostics: forward-negate-forward-negate recovery at frozen
g to 4.1e-14 and full ramp-schedule reversal to 2.0e-15 (no
dissipative or projective operation anywhere); the one-step linear map is
symplectic to 4.5e-17 (L3, dense 2n x 2n check); source-free quadratic energy
stays in a relative band of at most 1.3e-4 with secular fraction below the
declared threshold.

Stationary reference (independent solve): phi* = -q H^{-1} P rho_src by
eigen-decomposition on the sector; the inverse residual is at most 4.3e-15;
the stationary sign cancellation E_stat(q) = E_stat(-q) is exact; source-off
and receiver-zero stationary responses are exactly zero. These identities
agree with the literal transcribed zero comparators; they do not authenticate
or promote the absent campaign artifacts.

## Results

Adiabatic bridge (per fixture, both orderings, no refit): the RMS deviation
of the executed readout about the independently solved E_stat over the hold
window falls on the submitted frozen tau^-2 target across the geometric ramp
ladder (20, 40, 80, 160): fitted slopes -1.96 to -2.04 on all six fixtures for both
kick/drift orderings against the frozen p = 2 with tolerance 0.35; the decay
is monotone; the frozen envelope deviation * tau^2 <= 1.0 holds; and the
executed hold-mean converges to E_stat (terminal deviations down to 3.6e-7).

Same-parameter sign law (executed): q -> -q leaves the executed response
invariant with residual exactly 0.0 on every fixture (two separate runs);
the decoupled arm (q_src = +q, q_rec = -q) flips the response sign with
magnitude matching the independent -E_stat to relative 3.6e-3 (the adiabatic
residual at the probe ramp time). The q_rec = 0 row is a definition/wiring
control: q_rec <rho_rec, phi> is identically zero while the bare receiver
projection <rho_rec, phi> remains nonzero (at least 1.8e-3). It is not a
physical leakage/no-leakage result.

Response scaling: measured exponent 2.0000 on every fixture across
q in {1/2, 1, 2}, no refit. Near/far: the near-source executed response
exceeds the frozen far control on the declared D2 fixtures at all three sizes.
This is a finite-fixture inequality, not a general locality theorem.
Kick/drift orderings agree within the declared O(dt^2)
bound at the probe ramp time and share the same adiabatic limit.

Periodic diagnostic (reported, not promoted, not generalized): on the
periodic carrier D1 the submitted near/far inequality inverts on all three
fixtures. The receipt carries the exact rows. This profile- and
displacement-specific result does not establish a general Green-function
monotonicity result, locality wall, or no-go.

## Declared falsifiers (disposition)

- Decoupled-parameter sign: flip observed and magnitude matched.
- Adiabatic rate: submitted frozen p = 2 matched on all fixtures.
- Reversibility: machine-tight recovery held.
- Literal comparators: all four transcribed eigenvalue values matched.
- D2 near/far inequality: held on all three declared fixtures.
- Kick/drift ordering: remained within the O(dt^2) bound.

## Supplied, derived, and open

Supplied: the reviewed Cycle-576 site-set convention and `source_profiles`
function; the two directly constructed carriers and sector conventions; the
bounded disjoint supports and frozen displacements; the single declared
parameter q and its wiring; the quartic ramp, hold window, step, orderings,
ramp ladder, submitted frozen rate, and all tolerances; the literal
transcribed Cycle-626 comparator values as non-authoritative provenance.

Derived or executed: literal comparator matching; exact reversibility/symplecticity
with bounded energy; the tau^-2 adiabatic bridge to the independent
stationary solve; the executed same-parameter sign identity with its
decoupled-parameter and receiver-zero definition controls; q^2 scaling; the
three D2 near/far fixture inequalities; ordering agreement.

Open: selection or derivation of the carriers, coupling, supports, ramp, and
grids (all declared, none derived); any physical identification — energy,
stress, source, gravity, coupling, rate, or time (explicitly not claimed);
the finite-Weyl NQ carrier join and any open-real-space coframe K; continuum,
nonlinear, and strong-field extensions; an endogenous source law.

## Firewalls

The tested object is a same-parameter executed-update response identity on
two declared carriers. It is not energy, stress, gravity, a physical coupling
derivation or normalization, a source-law selection, attraction language, a
rate, or physical time. The q_rec = 0 row is a definition/wiring control and
nothing more: the bare receiver projection remains nonzero. The finite-Weyl
NQ carrier join is not executed and stays open; no open-real-space coframe K
is claimed. Carriers, ramp, hold window, grids, and supports are declared
supplied structure; no new axiom, primitive, or premise class is added.

## No-go discipline

No negative claim ships. The periodic near/far rows are three exact finite
diagnostics for the submitted profiles and displacements. They are explicitly
not a general monotonicity result, locality wall, or no-go. No-Go Discipline
N1--N8 is therefore not applicable to the narrowed packet.

## Evidence anchors and pins

Reviewed parent import, verified on disk at run time: the
[Cycle-576 runner](../../../../scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py)
(`7980bff1...`), its
[note](PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md)
(`5822c14b...`), and its
[receipt](../../../../outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json)
(`bc719ca8...`). This child executes only the parent's `source_profiles`
function; the directly constructed carriers are not parent outputs.

The Cycle-626 note/receipt, Cycle-604 receipt, and unused Cycle-579 script
hashes remain literal historical provenance copied from campaign head
`fb0ab5636e`. Those artifacts are absent here, never imported or executed,
not independently authenticated by this packet, and supply no authority.

## Cold run

The canonical runner
[`scripts/physical_same_coupling_executed_field_update_response_tournament_2026_07_23.py`](../../../../scripts/physical_same_coupling_executed_field_update_response_tournament_2026_07_23.py)
closes 26/26 rows with zero failures (exit 0) on the reviewed current-main
integration. The paired [receipt](../../../../outputs/physical_same_coupling_executed_field_update_response_tournament_receipt_2026_07_23.json)
and [cold transcript](../../../../outputs/physical_same_coupling_executed_field_update_response_tournament_cold_2026_07_23.txt)
are carried as reproducibility artifacts, not audit authority.
