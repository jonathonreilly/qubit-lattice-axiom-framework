# Same-coupling executed positive field-update response tournament

Date: 2026-07-23

Authority: none

Audit: unset

Cycle claim: 681 (claimed strictly above the joint visible max 680 at freeze:
680 is this lane's evaluator tournament claim, 679 the Record/Born
discriminator PR, campaign tip `fb0ab5636e` filenames reach 678). Descriptive
filenames per the owner directive; the cycle number appears only in runner,
receipt, and note content.

## Frozen question and conjunctive success gate

Does an EXECUTED, exactly time-reversible, finite-step field update on two
declared positive-sector carriers — with ONE physical coupling constant q
entering BOTH the source insertion and the receiver readout — reproduce the
campaign Cycle-626 stationary q^2-elimination response in the adiabatic limit
at a preregistered convergence rate without refit, with orientation-sign
cancellation holding in the executed update, flipping under preregistered
source/receiver decoupling, and nulling under receiver decoupling (no contact
leakage) — while claiming no energy, stress, source, gravity, or receiver
association content?

Success was frozen before running and requires all seven gates: exact
reversibility and symplecticity with bounded shadow energy; both carriers
positive with the transcribed Cycle-626 anchor eigenvalues reproduced;
adiabatic convergence to the independently solved stationary value at the
preregistered rate p = 2; the same-coupling sign law (even in q, decoupled
arm flips, receiver-zero nulls); q^2 response scaling; open-carrier near/far
ordering against frozen far controls; and kick/drift ordering agreement
within the declared O(dt^2) bound with one shared adiabatic limit.

## Construction

Carriers (DECLARED SUPPLIED STRUCTURE, constructed in-run): D1, the periodic
combinatorial graph Laplacian of the landed Cycle-576 L3/L6/L7 cubic site
graph restricted to the zero-mode-removed P0 sector; D2, the real open
Dirichlet finite-difference scalar Laplacian on the same site sets (no zero
mode). The transcribed Cycle-626 comparator anchors are reproduced in-run:
D1 P0 minimum nonzero eigenvalue 0.75302 at L7 (the 0.753 anchor; L3/L6 give
3.0/1.0 by construction), and D2 minima 1.75736 / 0.59419 / 0.45672 on
L3/L6/L7 against the 1.757 / 0.594 / 0.457 anchors — all within 1e-3, no
tuning. Both carriers are strictly positive on the tested sectors.

Source and receiver: bounded, non-negative, DISJOINT-support profiles built
from the landed c576 source machinery — the TRAIN_XY source texture windowed
to a declared ball and made non-negative (|texture|; the windowing and sign
drop are declared supplied structure, judged sufficient provenance because
the profile is the c576 texture restricted, not an invented shape). Frozen
near and far receiver displacements per (carrier, size); the support-overlap
census is empty on every fixture (nothing is contact).

Executed update: leapfrog / Stormer-Verlet at dt = 0.01 in both kick-drift-
kick and drift-kick-drift orderings, with the quartic ramp g = 4u^3 - 3u^4 on
[0, tau] then a fixed hold window (g''(0) = 0 removes the ramp-start endpoint
oscillation; g''(tau) != 0 leaves the clean tau^-2 non-adiabatic envelope,
fixing the preregistered rate p = 2 before any run). ONE scalar q is wired to
both the source insertion q g(t) <rho_src, phi> and the certified readout
q <rho_rec, phi>; the decoupled arm introduces a second constant explicitly
and only as the falsifier.

Executed certificates: forward-negate-forward-negate recovery at frozen
coupling to 4.1e-14 and full ramp-schedule reversal to 2.0e-15 (no
dissipative or projective operation anywhere); the one-step linear map is
symplectic to 4.5e-17 (L3, dense 2n x 2n check); source-free shadow energy
stays in a relative band of at most 1.3e-4 with secular fraction below the
declared threshold.

Stationary reference (independent solve): phi* = -q H^{-1} P rho_src by
eigen-decomposition on the sector; the inverse residual is at most 4.3e-15;
the stationary sign cancellation E_stat(q) = E_stat(-q) is exact; source-off
and receiver-zero stationary actions are exactly zero — reproducing the
Cycle-626 comparator identities on both declared domains.

## Results

Adiabatic bridge (per fixture, both orderings, no refit): the RMS deviation
of the executed readout about the independently solved E_stat over the hold
window falls on the preregistered tau^-2 law across the geometric ramp ladder
(20, 40, 80, 160): fitted slopes -1.96 to -2.04 on all six fixtures for both
kick/drift orderings against the frozen p = 2 with tolerance 0.35; the decay
is monotone; the frozen envelope deviation * tau^2 <= 1.0 holds; and the
executed hold-mean converges to E_stat (terminal deviations down to 3.6e-7).

Same-coupling sign law (executed): q -> -q leaves the executed response
invariant with residual exactly 0.0 on every fixture (two separate runs);
the decoupled arm (q_src = +q, q_rec = -q) flips the response sign with
magnitude matching the independent -E_stat to relative 3.6e-3 (the adiabatic
residual at the probe ramp time); the q_rec = 0 arm certifies exactly zero
WHILE the bare contact field <rho_rec, phi> remains nonzero (at least
1.8e-3) — reported as diagnostic only and certified as nothing.

Response scaling: measured exponent 2.0000 on every fixture across
q in {1/2, 1, 2}, no refit. Near/far: the near-source executed response
exceeds the frozen far control on the open carrier D2 at all three sizes
(the hard gate). Kick/drift orderings agree within the declared O(dt^2)
bound at the probe ramp time and share the same adiabatic limit.

Declared divergence (reported, not certified, not relabelled): on the
periodic carrier D1 the near/far ordering INVERTS on all three sizes —
the compact-torus P0 Green's function is antipode-peaked (commute-time /
heat-kernel-on-torus structure), so the near/far locality gate is ill-posed
there; the receipt carries the full diagnostic rows. The near/far hard gate
lives on the open carrier only.

## Preregistered falsifiers (disposition)

F1 decoupled-arm flip: fired as designed (flip observed, magnitude matched).
F2 adiabatic rate: preregistered p = 2 confirmed on all fixtures.
F3 reversibility: machine-tight recovery held.
F4 anchors: all transcribed Cycle-626 eigenvalue anchors reproduced; the
   single declared divergence (D1 near/far) is a locality-gate scoping, not
   an anchor mismatch.
F5 near/far: hard gate held on the open carrier.
F6 kick/drift: within the O(dt^2) bound.

## Supplied, derived, and open

Supplied: the landed c576 site graph and source-texture machinery; the two
declared carriers and sector conventions; the bounded disjoint supports and
frozen displacements; the single coupling q and its wiring; the quartic
ramp, hold window, step, orderings, ramp ladder, preregistered rate, and all
tolerances; the transcribed Cycle-626 anchors.

Derived or executed: anchor reproduction; exact reversibility/symplecticity
with bounded energy; the tau^-2 adiabatic bridge to the independent
stationary solve; the executed same-coupling sign law with its decoupled and
receiver-zero arms; q^2 scaling; open-carrier near/far; ordering agreement.

Open: selection or derivation of the carriers, coupling, supports, ramp, and
grids (all declared, none derived); any physical identification — energy,
stress, source, gravity, rate, time (explicitly not claimed); the
finite-Weyl NQ carrier join (c607/c609) and any open-real-space coframe K;
continuum, nonlinear, and strong-field extensions; an endogenous source law.

## Firewalls

The certified object is a same-coupling executed-update response law on two
declared carriers. It is not energy, not stress, not gravity, not a unique
physical coupling normalization (q is declared; the Cycle-613 finding that
representation charge is not a unique physical coupling stands), not a
source-law selection, not attraction language, not a rate, not physical
time. A contact-sensitive response is not energy, stress, source, or
gravity: the q_rec = 0 bare-field readout is diagnostic only and certified
as nothing. The finite-Weyl NQ carrier join is not executed and stays open;
no open-real-space coframe K claim; the F17 domain is untouched. No 3/4
DELAY association, no PR5557 harness compilation, no 5/4 ADVANCE count-edit
driving. Carriers, ramp, hold window, grids, and supports are declared
supplied structure; no new axiom, primitive, or premise class is added.

## No-go discipline

No negative claim is frozen: the declared divergence on the periodic
carrier's near/far ordering is a scoping of where the locality gate is
well-posed, recorded with its full diagnostic rows, not a wall. All prior
campaign walls remain exactly as scoped by the Cycle-626 note, pinned below.

## Evidence anchors and pins

Landed hard import (verified on disk at run time): the Cycle-576 runner
(53d60249...), note (2d5650c5...), and receipt (06456c14...). Read-only
campaign evidence anchors at campaign head fb0ab5636e (recorded, transcribed,
never imported or executed): the Cycle-626 note (1346e9c5...) and receipt
(ab8489e9...) supplying the comparator anchor eigenvalues and exact
stationary identities, and the Cycle-604 receipt (2fe20ba1...) for P0-sector
context. The unused Cycle-579 script sha (e607e8a0...) is recorded as an
anchor only.

## Cold run

The canonical runner
`scripts/physical_same_coupling_executed_field_update_response_tournament_2026_07_23.py`
closes 26/26 rows with zero failures (exit 0) on a clean main-based tree with
the substrate PR applied; the paired receipt and cold transcript are frozen
alongside this note.
