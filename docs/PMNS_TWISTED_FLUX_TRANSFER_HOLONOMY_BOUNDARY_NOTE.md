# PMNS Twisted Flux Transfer Holonomy Boundary
**Type:** bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem;
Tier-A routing made explicit 2026-06-11 — see "Registered Tier-A routing")
**Admitted context inputs:** staggered-Dirac realization derivation target
(canonical parent: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`;
registered Tier-A derivation target `AC_phi_lambda` (display `AC_φλ`) —
see "Registered Tier-A routing").

**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py`

## Question

Can a twisted transfer, flux insertion, or cycle-holonomy law on the
graph-first oriented-cycle frame select the remaining values of the retained
PMNS cycle channel?

## Answer

Partially.

On the canonical graph-first cycle frame `E12, E23, E31`, the flux-threaded
transfer kernel

```text
T(xbar, ybar, phi) = xbar I + ybar (e^{i phi} C + e^{-i phi} C^2)
```

has an exact holonomy/spectral value law:

```text
tr(T)/3 = xbar
tr(C^2 T)/3 = ybar e^{i phi}
```

so `xbar`, `ybar`, and `phi` are recovered exactly from the twisted transfer
data. This is a genuine axiom-native value law for the fluxed transfer carrier.

But the current exact bank still does not select the full reduced PMNS oriented
cycle family

```text
A_fwd(u, v, w) = (u + i v) E12 + w E23 + (u - i v) E31
```

with one flux holonomy alone. The one-angle holonomy probe has a 2-real kernel
on that reduced carrier, so it does not collapse the full reduced family to a
unique point.

## What This Buys

- The graph-first frame remains canonical.
- The flux-threaded transfer carrier now has an exact nontrivial value law.
- The retained PMNS reduced carrier is still not fully value-selected by a
  single holonomy probe.

## What Remains

Any further positive selection law would have to use genuinely new dynamics or
a further admitted extension beyond the current exact bank.

## Verification

```bash
python3 scripts/frontier_pmns_twisted_flux_transfer_holonomy_boundary.py
```



## Hypothesis set used (axiom-reset 2026-05-03; memo reference current as of 2026-06-11)

Per the current axiom memo `MINIMAL_AXIOMS_2026-06-05.md` ("Open Gates
And Admissions Outside The Axioms"; the 2026-05-03 memo cited by the
original retag is superseded), this note depends on the
**staggered-Dirac realization derivation target**, which is currently an open gate. The note's load-bearing claim defines or relies on fermion fields, fermion-number operators, fermion correlators, fermion bilinears, the staggered Dirac action, the BZ-corner doubler structure, the `hw=1` triplet, charged-lepton sector content, neutrino sector content, quark / hadron content, the Koide / PMNS / CKM observable surfaces, or the Grassmann CAR boundary structure — all of which depend on the staggered-Dirac realization derivation target registered by the current admission registry and described by `MINIMAL_AXIOMS_2026-06-05.md`.

Canonical parent note: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (`claim_type: open_gate`). Historical in-flight supporting work from the original 2026-05-03 retag:

- `PHYSICAL_LATTICE_NECESSITY_NOTE.md`
- `THREE_GENERATION_STRUCTURE_NOTE.md`
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`
- `scripts/frontier_generation_rooting_undefined.py`
- `GENERATION_AXIOM_BOUNDARY_NOTE.md` (preserved)

Therefore `claim_type: bounded_theorem` until that gate closes. When that gate closes, the lane becomes eligible for independent audit/governance retagging as `positive_theorem`; the audit pipeline recomputes `effective_status`, but it does not silently invent a new `claim_type`. The substantive science content of this note is unchanged by this retag.

## Registered Tier-A routing (2026-06-11; audit-requested repair)

The 2026-06-11 conditional audit's repair target was: "obtain
retained-grade audit/closure for the staggered-Dirac gate or remove the
admitted carrier dependency." This section takes the precedented third
form of that repair (per
`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`,
plain-text precedent pointer): the carrier dependency is routed
explicitly into the **registered Tier-A derivation target**, so the
citation graph carries a registered admission rather than an
unregistered conditional blocker.

1. **The algebra is standalone.** The load-bearing computations of this
   note close as exact finite matrix algebra with no carrier input:
   from `C³ = I` and `tr(C) = tr(C²) = 0`, the trace recovery law
   `tr(T)/3 = x̄`, `tr(C²T)/3 = ȳ e^{iφ}` is an identity on the
   abstract cyclic frame, and the one-angle holonomy probe
   `h(u,v,w) = 2cos(φ)u + 2sin(φ)v + w` has a 2-real kernel by linear
   algebra. The runner verifies both without consuming any fermion
   content.
2. **What the carrier admission carries.** Only the *naming* of the
   cycle frame as the **PMNS** channel (the physical identification of
   `E12, E23, E31` with the lepton-sector observable surface) depends
   on the staggered-Dirac realization. That naming is the admitted
   context input declared above.
3. **The admission is a registered Tier-A target.** The canonical
   parent `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is the
   registered Tier-A derivation target `AC_phi_lambda` (display
   `AC_φλ`) in the admission registry
   (`docs/audit/data/premise_decision_history.json`). This note
   routes the carrier naming **into** that registered target; it does
   **not** close the gate. Under the published chain rule
   (`docs/audit/scripts/compute_effective_status.py`), a clean
   `bounded_theorem` row whose only non-retained, non-axiom one-hop
   dependency is a registered Tier-A derivation target is a candidate
   for the Tier-A-bounded class rather than an unregistered
   conditional blocker.
4. **No status assertion.** This section makes the narrow re-audit
   case only. The audit lane is the sole authority on whether to honor
   it; this note asserts no `effective_status` and predicts no audit
   outcome.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
