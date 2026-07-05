# The |δ| = 2/9 Theorem Chain: Retained Fixed-Locus Arithmetic + One Named Readout Identification

**Date:** 2026-06-09 (2026-06-12: dependency decoupling — the carrier surface is stipulated in-note as the supplied circulant class; the period-fork and detc/detr-fork citations are demoted to context (the period content used here is computed in this note's own runner; the circulant class is supplied in-note); the E6 orientation-strip consumption now cites its authority as a load-bearing dependency.)
**Audit repair:** 2026-07-05 — repairs the `missing_bridge_theorem` conditional
(audit row 3800b57ab): (a) the circulant-class form is now consumed from the
retained_bounded K-orbit form authority instead of bare in-note stipulation; (b) R-η is
restated as an explicitly **declared supplied readout-identification premise**
with a non-derivability boundary (it is the Tier-A sub-admission (ii) content;
no retained readout theorem supplies it on the current surface, and the retained
radian-bridge no-go covers the enumerated phase sources), so the theorem this
note claims — and the runner now checks — is the **conditional implication**
(declared premise + retained arithmetic ⟹ `|δ| = 2/9`), not R-η itself.
No claim is strengthened; the prior stipulation-style runner check is replaced
by a mechanical declaration check plus the computed implication.
**Claim type:** bounded_theorem (a conditional theorem chain; the single conditional input is a named, proposed identification — no new number, no new primitive)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_delta_eta_density_readout_chain_2026_06_09.py`](../scripts/frontier_koide_delta_eta_density_readout_chain_2026_06_09.py)
(SCORECARD: PASS=23, FAIL=0; cached:
[`logs/runner-cache/frontier_koide_delta_eta_density_readout_chain_2026_06_09.txt`](../logs/runner-cache/frontier_koide_delta_eta_density_readout_chain_2026_06_09.txt))

> **What this is.** The no-go validation pass found the |δ| portfolio soft: the
> radian-bridge audit is an enumeration no-go that does not foreclose rational
> spectral densities (it carries the 2/9 value as its own unforeclosed witness),
> and the number 2/9 is **already retained-bounded arithmetic** in the repo (the
> C₃[111] fixed-locus density with forced weights). This note assembles the
> chain that makes `|δ| = 2/9` a **theorem conditional on one named
> identification (R-η)** — a dimensionless readout-class statement naming no
> number — plus the existing carrier gate. Zero new numbers enter anywhere.
> The period discussion is a bounded diagnostic: the direct reading adds no
> import beyond the supplied R-η premise on the tested mechanisms, while the
> standard π-packaging has no currently retained registrable carrier in the
> det-class route checked here. R-η remains the explicit readout identification.

---

## The chain

**E1 — the retained arithmetic, re-derived from scratch (the #3138 guard).**
The C₃[111] axis cycle's transverse spectrum is `{ω, ω²}` — the forced weights
`(1,2)` (computed as the 3-cycle's eigenvalues); the core identity
`(ω−1)(ω²−1) = 3` holds exactly; and the Atiyah–Bott/Lefschetz fixed-locus
density is

```text
    L₃(1,2) = (1/3) Σ_{j=1,2} 1/((1−ω^j)(1−ω^{2j})) = 2/9   EXACTLY
```

with contrast cells `L₃(1,1) = L₃(2,2) = 1/9`. Independently cross-checked via
the cotangent/Dedekind packaging (same 2/9), and mechanically cross-checked
against the **retained-bounded** fixed-locus note
([`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)).

**E2 — the declared supplied premise (R-η).**

> **Supplied-premise declaration (R-η).** *The registered C₃-breaking phase
> magnitude is the fixed-locus spectral density, read directly as the angle:*
> `|δ| = L₃(1,2)`. This identification is **supplied, not derived**: it is the
> readout-identification content of Tier-A `AC_phi_lambda` sub-admission (ii);
> no retained readout theorem supplies it on the current surface, and the
> retained radian-bridge no-go covers the enumerated phase sources. Every claim
> in this note is conditional on this declared premise.

R-η is a dimensionless readout-class **identification** — the sibling of the
`(M)`/det-class readout atom — and it names no number; the number comes from
E1. The runner verifies this declaration mechanically and then checks the
conditional implication (declaration + E1 arithmetic ⟹ `|δ| = 2/9`); it does
not, and cannot, check R-η itself.

**Carrier class (supplied form, retained authority).** Throughout, the carrier
is the supplied charged-lepton circulant class: the three-parameter Hermitian
circulant family
`H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T` with `a` real, `B > 0`,
`delta` real, and `C` the cyclic 3-shift. The class form and its `K`-orbit
structure are consumed from the retained_bounded one-hop form authority
[`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
(the same wiring as the R-η narrowing note's formal layer).
The physical identification of this class as the charged-lepton carrier is carried
by the `AC_phi_lambda` admission itself, which supplies its own gate surface
(`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is context for where that
surface arises physically, not load-bearing here).

**E3 — the period fork, computed honestly.** The alternative standard packaging
(the density entering as a determinant-phase exponent, `δ = π·L = 2π/9`)
predicts a wildly wrong spectrum (computed: `m_τ` off by orders of magnitude).
The fork is physical, not conventional (see the radian-period context note named below).

**E8 — period-fork diagnostic.** The fork is not promoted into an extra hidden
admission. The runner records the following bounded diagnostics:

1. **The π is localized:** in any determinant reading, each negative eigenvalue
   contributes `e^{iπ}` to `arg det` — the π of the standard `e^{iπη}` packaging
   is exactly the det-sign mechanism, nothing else (computed witness).
2. **That det-class door is closed in this framework:** the multiplicative
   lemma (re-verified) forces the phase character `k = 0` for K-invariant
   det-class readouts, so the standard det-sign route does not supply a
   registrable `π·n₋` phase.
3. **Import accounting:** the direct reading `δ = L` consumes no additional
   dimensionless constant beyond R-η; `δ = π·L` consumes an unexplained
   dimensionless factor whose standard det-sign mechanism is unavailable by
   (2). Bounded claim only: no currently retained registrable π-source is
   supplied here. This does **not** prove that no future readout context could
   supply another dimensionless factor.
4. **Counterfactual boundary:** if the masses had matched the π-row, this
   chain would not have been allowed to absorb that result by convention. The
   comparator agreement supports the direct R-η reading but is not a
   derivation input.

**E4 — the comparator (labeled, never an input).** With `r = 1/2` (separate
comparator context, not landed by this note) and `|δ| = 2/9` **exact**, the charged-lepton
circulant predicts from `(m_e, m_μ)`:

```text
    m_μ  pred = 105.6594  vs PDG 105.6584     (1×10⁻⁵ relative)
    m_τ  pred = 1776.98   vs PDG 1776.86±0.12 (inside ~1σ)
    δ_fit − 2/9 = 7.4×10⁻⁶  with m_τ-induced 1σ band 8.3×10⁻⁶  (≈1σ)
```

**E5 — no-go boundary compliance.** The radian-bridge audit forecloses
*periodic* (`qπ`) sources — the rational density is outside its bins, and the
audit itself carries 2/9 as an unforeclosed witness (grep-verified). The
eigenline/cobordism no-gos police Wilson-*mark* selection on the rank-2 space —
this chain is a readout identification, not a mark selection; their scope is
not entered (line selection remains with the carrier gate and the unaudited
chirality-selector companion). The gated CP-odd vacuum route — circular on the
carrier gate — is **not used**: bypassed, not resolved.

**E6 — K-orbit consistency.** `conj(H(δ)) = H(−δ)` on the supplied circulant
class, and the registrable species surface is the unordered mass multiset
([`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md),
Consequence B): the registrable atom is `|δ|` — exactly what the chain supplies;
the sign stays frame content.

## Net

```text
|δ| = 2/9  =  THEOREM conditional on:
    R-η          (DECLARED supplied readout-identification premise — the
                  Tier-A sub-admission (ii) content; not derivable from
                  currently retained premises on this surface; number-free)
    carrier class (form from the retained_bounded K-orbit authority; the physical
                  carrier identification is carried by the AC_phi_lambda
                  admission)
    context      (landed circulant; r = 1/2 used only in the mass comparator
                  unless the separate occupancy-subsumption row lands)

new numbers consumed:  ZERO        new primitives consumed:  ZERO
```

If the separate occupancy-subsumption row for `r = 1/2` and the orientation
strip are both accepted, this supplies the `|δ|` component of the charged-
lepton mass pattern without adding a new number. This note does not retire the
AC_φλ admission or edit the Tier-A registry; it only prepares a candidate
retirement path for the `|δ|` numeric content, conditional on R-η and
independent audit.

## What this note does NOT claim

- **Not** an unconditional derivation of `|δ|`: R-η is the named conditional
  input (proposed; its ratification is an owner/audit decision exactly like the
  `(M)` atom's).
- **Not** a resolution of the gated CP-odd selector (bypassed), the rank-2
  line-selection question (remains with the carrier gate + the unaudited
  chirality-selector note), or the global `PL S³×R` bridge (named open in the
  retained fixed-locus note).
- **Not** a re-walk of refuted routes: no periodic/`qπ` source, no Wilson-mark
  selector, no CP-odd vacuum computation.
- The Callan–Harvey `2/N² = 2/9` is a **distinct** object (proven distinct
  in-repo; coincides only at `d = 3`) — recorded as consistency, never consumed.
- **Falsifier:** a tighter `m_τ` measurement pulling the fitted phase away from
  `2/9` (the current residual sits at 1σ of the `m_τ` band; the chain dies if it
  grows with precision).
- **No** comparator is a derivation input; sets no audit status.

## Negative-boundary discipline

This is a conditional positive chain with boundary checks, not a no-go against
all other phase-readout routes.

- Alternative routes left open: another retained readout context for a
  dimensionless phase factor; a future proof of R-η; a different carrier-gate
  realization; a direct derivation of `r = 1/2`; and a future selector theorem
  for the relevant line.
- Wall independence: R-η, carrier realization, occupancy-subsumption context,
  orientation/sign convention, and comparator agreement are independent.
- Hidden-wall scan: R-η, the carrier gate, `r = 1/2`, and the det-class
  multiplicative lemma are all explicit; none is silently converted into a
  repo axiom or primitive.
- Residual matching: the radian-bridge no-go is used only to show that this
  rational-density route is outside its enumerated periodic-source bins.
- Rhetoric resolution: "zero new number" means the numeric value comes from
  the cited fixed-locus arithmetic once R-η is assumed; it does not mean the
  readout identification is derived.
- Partial-closure scan: the period diagnostic removes the standard det-sign
  π route on the checked det-class surface but leaves other future readout
  contexts open.
- Steelman: a retained readout theorem could still justify a different
  dimensionless conversion factor. This note would then become a competing
  conditional chain, not an exclusion theorem.
- Cross-cycle echo: prior overbroad phase-source claims failed when they hid
  a readout or period convention; this note keeps R-η and the period diagnostic
  explicit.

## Dependencies

- [KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — the retained-bounded arithmetic (re-proven here; the chain's number source).
- [KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  — the enumeration no-go whose bins this route is outside (boundary cited, respected).
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the orientation strip consumed in E6 (registrable species surface = unordered
  multiset; the registrable atom is `|δ|`).
- [`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`](TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md)
  — the retained_bounded one-hop form authority for the supplied circulant class and its
  `K`-orbit structure (`conj(H(δ)) = H(−δ)`), re-verified symbolically in E6.

Context (not load-bearing: cited only to locate surfaces and corroborate
diagnostics; no content is consumed):

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — where the supplied
  circulant class arises physically as the charged-lepton carrier; the chain is
  stated on the supplied class above, and the physical identification rides with
  the `AC_phi_lambda` admission.
- `KOIDE_DELTA_RADIAN_PERIOD_PHYSICAL_NOT_VACUOUS_NARROW_THEOREM_NOTE_2026-06-04.md`
  — corroborating context for E3; the period-fork physicality used by this chain
  (the π-packaging mass prediction failing by a wide margin) is computed directly
  in this note's primary runner, and the note's own boundary states the period
  discussion is a bounded diagnostic.
- `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` — the open-gate
  row for the occupancy binary (real vs holomorphic doublet count); cited only to
  locate that binary. The circulant class is stipulated in-note; the orientation-strip
  and occupancy-subsumption rows remain context for downstream mass-pattern
  assembly, not load-bearing status claims made by this note.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
