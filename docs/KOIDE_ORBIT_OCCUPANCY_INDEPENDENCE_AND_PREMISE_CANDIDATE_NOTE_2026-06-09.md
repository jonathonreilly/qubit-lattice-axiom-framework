# The Koide Occupancy Atom (Doublet `r/Q`-Class) Is Independent of the Current Checked Premise Surface; the Per-Cell Equipartition-Granularity Premise Candidate

**Date:** 2026-06-09
**Review-loop update:** 2026-06-12 — the four fork cells and the `rho`-map
orientation are now derived in this note's runner from explicit per-cell
integrals. The landed table remains a consistency cross-check; the fork and
sharpening citations are context accordingly. (The `rho`-map orientation was
subsequently **withdrawn as contaminated** — see the Repair (2026-07-11)
section; the four partition integrals are retained only as a
normalization/determinant-power cross-check, decoupled from `r`.)
**Axiom-surface update:** 2026-07-05 — premises re-based from the superseded
`MINIMAL_AXIOMS_2026-06-05.md` (three-axiom memo) onto the current four-axiom
memo `MINIMAL_AXIOMS_2026-06-29.md`: the enumerated Record non-supply clause
is superseded by the Qualification's general non-supply clauses (checked live
by the runner; the 06-05 clause is kept as historical corroboration), and
outcomes-as-K/CPT-orbits is no longer axiom text — it is supplied-context
carried by the bridge [T1, KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md).
No claim is strengthened; the independence result and the premise candidate
are unchanged.
**Repair update:** 2026-07-11 — an independent audit (2026-07-10) failed the
prior version: the holomorphic Gaussian moment gives `r = 1`, not `1/2`, so the
prior runner's hard-coded per-slot quantum was an error. The moments are now
derived honestly as a diagnostic; both witnesses are recharacterized as
**realized-state equipartition laws differing only in granularity** (per real
mode ⟹ `r = 1`; per outcome cell, `E_s = E_d` ⟹ `r = 1/2`); the
independence-by-exhibition survives with exactly one differing named element.
See the **Repair (2026-07-11)** section below.
**Claim type:** bounded_theorem
**Type:** bounded_theorem + premise-candidate proposal (proposal NOT adopted)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt`](../logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt)
(SCORECARD: PASS=39, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2`, adoption of any premise, or a mass
> prediction. **Claimed:** the one residual atom behind the Koide `r`-gate — the
> `r/Q`-class of the generation doublet (equivalently the granularity of the
> realized-state equipartition law) — is **independent of the current checked
> premise surface** (shown by the current axiom-surface non-supply boundary plus
> two exhibited consistent witnesses), so the present derivation loop is
> closed at this atom without adding or deriving an equipartition granularity;
> and the principled premise candidate (**per-cell equipartition granularity:
> the equipartition law grained per record-outcome cell**) is stated with
> computed support, for owner decision — the `ξ=1` playbook.

---

## Repair (2026-07-11): honest orbit-witness moment; `r = 1/2` relabeled

An independent audit (2026-07-10; codex gpt-5.6-sol, xhigh, confidence high)
failed the prior version of this note and its runner. Verbatim finding:

> "The holomorphic Gaussian integral does not yield the claimed one-slot
> equipartition moment: with Z=pi/g and g=6 beta, it gives &lt;|b|^2&gt;=1/(6 beta),
> hence r=1, not 1/2. The runner obtains r=1/2 by hard-coding a per-slot quantum
> rather than deriving it from that integral."

The finding is correct and is accepted. What changed, and why the corrected
claim is weaker-but-honest:

1. **The finding is now a positive diagnostic (runner O3A).** The honest
   holomorphic one-complex-slot Gaussian moment of the channel energy
   `E = 3a² + 6|b|²` is `⟨|b|²⟩ = 1/(6β)` (with `g = 6β`: `Z_d = π/g` and
   `⟨|b|²⟩ = 1/g`), giving `r = ⟨|b|²⟩/⟨a²⟩ = 1`, not `1/2`. The realified
   two-real-slot bookkeeping of the same physical weight gives the same
   `⟨|b|²⟩` and the same `r = 1`: the Gaussian moment is
   **normalization-independent** — the partition normalization
   `Z_d ∈ {π/g, 2π/g}` cancels in the moment ratio. All moments are now
   computed by honest `sympy` integration; the hard-coded
   `per_slot_quantum = 1/(2β)` is removed. This computation is retained purely
   as the **diagnostic** that kills the old `ρ`-map/one-slot-moment story — it
   does not define `M_sector`. The diagnostic also explains itself: the
   Gaussian moments satisfy per-real-mode equipartition in expectation
   (`⟨3a²⟩ = ⟨6x²⟩ = ⟨6y²⟩ = 1/(2β)`), so the moment `r = 1` is per-mode
   graining realized on average — no Gaussian moment can give `r = 1/2`.

2. **Both witnesses are recharacterized as realized-state equipartition laws
   differing only in granularity (runner O3B).** `M_sector` is the
   **per-real-mode** equipartition law — one quantum `ε` per real mode
   (`a; x; y`), componentwise `3a² = 6x² = 6y²`, invariantly `E_s = ε`,
   `E_d = 2ε` — solved exactly to `|b|² = a²`, `r = 1`. `M_orbit` is the
   **per-outcome-cell** equipartition law — one quantum `ε` per outcome cell
   (`{e₀}; {e₁,e₂}`), i.e. `E_s = E_d` (`3a² = 6|b|²`) — solved exactly to
   `|b|² = a²/2`, `r = 1/2`, and `Q = 2/3` via the landed dictionary
   `Q = (1+2r)/3`. Both are exact constraints on the *realized* configuration
   (not moment identities); the quantum `ε` cancels in `r` for both, so
   nothing is hard-coded. In particular `r = 1/2` is **not** a Gaussian-moment
   consequence of one-slot occupancy bookkeeping.

3. **Independence-by-exhibition survives, relabeled (runner O3C).** The two
   witnesses share one checked premise surface (carrier, Gaussian measure
   family, normalization convention, outcome dictionary, K-reality
   restriction, and the equipartition-law *type*: a realized-state law
   assigning one quantum per counting unit) and differ in **exactly one named
   element** — the **granularity** of the realized-state equipartition law
   (per real mode → `r = 1`; per outcome cell → `r = 1/2`). The parity table
   exhibits the two decisive toggles: toggling the normalization convention
   leaves `r` unchanged, while toggling the granularity flips `r` between `1`
   and `1/2`. The witnesses' distinguishing content is therefore relabeled
   from "one-slot occupancy counting" to the "granularity of the
   realized-state equipartition law."

4. **Withdrawn as contaminated.** The `ρ`-map `r = 1/(2ρ)` with
   `ρ = (π/g)/Z_d`, and every statement that the partition-normalization ratio
   `Z_sector/Z_orbit = 2` *sets* the `r`-ratio, are withdrawn: they encode the
   same arithmetic error the audit caught (that `Z_d` fixes `r`). The four
   landed partition integrals (`2π/g`, `π/g`, and their Berezin forms) remain
   true facts, but are **normalization / determinant-power facts only** and are
   decoupled from `r`.

**Why the law framing (and not a moment framing) — hygiene note.** Beyond being
arithmetically wrong for `r = 1/2`, the moment/ensemble framing is additionally
in tension with the realized-state primitive: derivations evaluate at the
realized state pointwise, and an ensemble moment ("no averaging over
alternatives") is not a realized-state law. The law framing is therefore both
the honest and the primitive-compliant reading of the two witnesses; the
Gaussian-moment computation is kept only as the diagnostic above. This is
hygiene only — the primitive is not cited as deriving anything.

**Weaker-but-honest.** The prior note presented `r = 1/2` as a *derived* moment
of holomorphic one-slot bookkeeping; that derivation was false. The corrected
note derives `r = 1/2` only *conditionally* on a supplied per-outcome-cell
equipartition granularity — which is exactly the atom the independence result
says is **not** supplied by the current checked surface. The strong reading
(holomorphic bookkeeping forces `r = 1/2`) is gone; the surviving claim is the
honest one: two lawful witnesses, one differing supplied element (the law's
granularity), so the `r/Q`-class is independent of the current checked premise
surface, with the per-cell equipartition granularity offered as an
owner-decision premise candidate. Runner after repair:
`SCORECARD: PASS=39, FAIL=0`. This note sets no audit status; the audit lane
owns the re-check.

## Role

The orbit-quotient sharpening
`KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md`
reduced the Koide `r`-gate
to one residual atom: the doublet **`r/Q`-class**, `r ∈ {1, 1/2} ⟺ Q ∈ {1,
2/3}`. (The prior version tied this to a per-doublet measure-weight class
`Z_d ∈ {2π/g, π/g}`; the 2026-07-10 audit showed `Z_d` does not fix `r` — see
**Repair (2026-07-11)** — so the atom is stated directly as the `r/Q`-class,
carried by the granularity of the realized-state equipartition law.) This note
settles the **status** of that atom.

## Result 1: the atom is not supplied by the current axiom surface

The current four-axiom memo
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)) states:
*"These axioms state only their named primitive content. Further physical
structure requires derivation, bridge, explicit admission, or approved
primitive registration before use as a premise."* It also states: *"In
particular, a law may not depend on a choice not fixed by the supplied
structure, unless that choice is admitted."* and *"A law privileges no states.
Its domain is a supplied condition, and at every state where the condition holds
it gives exactly one answer."* The realized-state primitive adds: *"The laws do
not pick the state; the world does, among the states the laws permit."* and
*"Nothing more is supplied: no averaging over alternatives, no typical or
generic claim, and no quoting a number that would differ had another
law-admissible state been realized."* Historically, the superseded 2026-06-05
Record wording corroborated the same boundary by saying that a record
*"supplies no readout context, decomposition, K/CPT structure, sector-generation
rule, **weighting, normalization, probability**, measurement/decoherence
dynamics, time metric, within-sector data, **or occupancy rule**."* The doublet
`r/Q`-class — equivalently the granularity of the realized-state equipartition
law (per real mode vs per outcome cell) — is precisely such a state-privileging
weighting rule (a choice not fixed by the supplied structure, and one that would
privilege the equipartition states of its graining). The runner checks the 06-29
Qualification clauses and primitive mechanically, with the 06-05 clause kept as
historical corroboration. So the current axiom surface **declines to supply this
atom**.

## Result 2: independence by exhibition

Two explicit witnesses on the generation configuration `(a, b) ∈ R × C`, both
satisfying the checked constraints supplied by the current Record/Koide
bookkeeping surface — `Z₃`-equivariance, K-invariance/orbit-definedness of the
weight, with outcomes-as-K/CPT-orbits supplied by [T1, KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md),
positivity, normalizability, and finite additivity of the induced readout on
the two-orbit outcome algebra. Both carry the same channel energy
`E = 3a² + 6|b|²` (the landed circulant lever), and both are **realized-state
equipartition laws** — exact constraints assigning one energy quantum `ε` per
counting unit — differing only in the **granularity** of the counting unit:

```text
M_sector : per-REAL-MODE law (three modes a; x; y):  E_s = ε, E_d = 2ε
           componentwise 3a² = 6x² = 6y²  ⟹  |b|² = a²   (exact)  →  r = 1
M_orbit  : per-OUTCOME-CELL law (two cells {e₀}; {e₁,e₂}):  E_s = E_d = ε
           3a² = 6|b|²  ⟹  |b|² = a²/2                   (exact)  →  r = 1/2
```

The quantum `ε` cancels in `r` for both laws — nothing is hard-coded. The two
witnesses share one checked premise surface — carrier, Gaussian measure family,
normalization convention (the doublet partition `Z_d ∈ {2π/g, π/g}`, which is
**`r`-invariant**; see the Repair section), outcome dictionary `Q = (1+2r)/3`,
K-reality restriction, and the equipartition-law *type* (a realized-state law,
one quantum per counting unit) — and differ in **exactly one named element**:
the **granularity** of the equipartition law (per real mode in `M_sector`, per
outcome cell in `M_orbit`). The runner's parity table shows the decisive
toggles: swapping the normalization convention leaves `r` unchanged, while
swapping the granularity flips `r` between `1` and `1/2`. Both witnesses
consistent + the live axiom-surface non-supply boundary ⟹ **the equipartition
granularity (equivalently the `r/Q`-class) is not supplied by the current
checked premise surface.** This also mechanizes the refuted-attempt history:
every prior derivation route in this loop smuggled an equipartition-granularity
/occupancy law (the CW/fluctuation-modulus route is a per-mode-side choice —
supplied, never retained; refs #2624/#2688). Derivation attempts from this
surface cannot settle `r` without adding or deriving an equipartition
granularity; an explicit owner-approved premise is one possible resolution.

## Consequence map — at the landed bookkeeping level only

No new microscopic bridge is invented (the #3138 lesson). The `r`-values are
fixed by the two witnesses' single differing element — the law's granularity —
**not** by the partition normalization:

```text
M_sector  (per-real-mode equipartition)     →  r = 1    →  Q = 1
M_orbit   (per-outcome-cell equipartition)  →  r = 1/2  →  Q = 2/3
```

The four landed partition integrals (`2π/g` and `π/g`, in their Gaussian and
Berezin forms) remain true facts and are kept only as a normalization /
determinant-power cross-check; they are **decoupled from `r`**. The prior
`ρ`-map `r = 1/(2ρ)` with `ρ = (π/g)/Z_d`, and any reading in which the
normalization ratio `Z_sector/Z_orbit = 2` *sets* the `r`-ratio, are withdrawn
as contaminated (see Repair). Labeled comparison: `r_mode/r_cell = 2` is the
doublet's modes-per-cell count (two real modes in one outcome cell); the
partition normalizations also differ by `2`, but `Z_d` does not set `r` — the
granularity does (the 2026-07-10 finding). Connection to the landed
count-once/count-twice binary (stated only, no new claim): per-real-mode
graining is the count-twice/sector/`det_R = |det_C|²` horn (the doublet counted
as two real modes), and per-outcome-cell graining is the
count-once/orbit/`det_C` horn (the doublet counted as one cell) — the
granularity fork is that binary in realized-state law form.

## The premise candidate: per-cell equipartition granularity (proposal; NOT adopted)

> **Per-cell equipartition granularity:** the realized-state equipartition law
> is grained per record-**outcome cell** (K/CPT orbit) — one energy quantum per
> cell, so the singlet and doublet channels carry equal energy, `E_s = E_d` —
> rather than per real fluctuation mode.

Computed support:

- **Granularity matching (unique among the two exhibited witnesses):** the
  per-cell law grains one equal energy quantum per record-outcome cell
  (2 outcome cells ⟷ 2 equal channel energies `E_s = E_d`); the per-mode law
  instead grains at the 3 real fluctuation modes (`a; x; y`) and mismatches the
  2 outcomes. "The equipartition law grained at the granularity of outcomes" is
  the readout-side analogue of the approved `kinetic_isotropy_primitive`'s
  "tick grained like edge" — dimensionless, structural, binary, no fitted
  number.
- **Comparator (labeled, never an input):** the empirical charged-lepton Koide
  ratio `Q_PDG = 0.666661` sits on the per-cell-granularity cell (`2/3`) to
  `6×10⁻⁶`; the per-mode cell (`Q = 1`) is excluded empirically by ~50%.
- **Payoff if approved (stated as the proposal's consequence, not a result):**
  with the per-cell equipartition granularity, `r = 1/2` and `Q = 2/3` follow
  from the landed `Q = (1+2r)/3` lever — the Koide relation becomes the
  statement that nature's record statistics equipartitions energy per outcome
  cell rather than per real mode. The phase `δ` remains a separate admission
  (the radian-period note).

Per the independence result, this is **owner-decision territory** — exactly the
`ξ=1` situation: the premise is not supplied by the current checked premise
surface, both horns are consistent, and one honest resolution is an explicit
structural law rather than an eighth derivation attempt.

## No-go discipline gate

- **N1 Route enumeration:** Record non-supply is ATTEMPTED and stops at the
  current Qualification/realized-state non-supply boundary, with the
  superseded 06-05 "no occupancy rule" clause only historical corroboration;
  the sector witness (per-real-mode equipartition law) is ATTEMPTED and gives a
  consistent `r = 1` horn; the orbit witness (per-outcome-cell equipartition
  law `E_s = E_d`) is ATTEMPTED and gives a consistent `r = 1/2` horn but
  remains proposed, not adopted; the prior CW/fluctuation-modulus route is
  RULED OUT BY PRIOR as supplied per-mode-side context; the honest Gaussian
  moment (both bookkeepings give `r = 1`) is ATTEMPTED as a diagnostic and
  shows the normalization does not select a horn; the PDG comparator is
  ATTEMPTED only as labeled non-input support; the future-larger-premise route
  is left OPEN.
- **N2 Wall independence:** the common wall is the unsupplied equipartition
  granularity; the two exhibited witnesses agree on the checked constraints and
  differ only at that wall.
- **N3 Hidden-wall scan:** no readout context, weighting, probability,
  normalization, dynamics, phase, mass input, or empirical value is introduced as
  a premise.
- **N4 Residual matching:** the residual atom is exactly the granularity of the
  realized-state equipartition law — per real mode vs per outcome cell
  (`r ∈ {1, 1/2}`).
- **N5 Rhetoric audit:** the claim is current-surface independence, not a
  universal future no-go and not a derivation of `r = 1/2`.
- **N6 Partial closure:** the live continuation is either an owner-approved
  per-cell equipartition-granularity premise or a later derivation from
  additional theory.
- **N7 Steelman:** a larger retained premise surface could still derive the
  equipartition granularity; this note does not block that route.
- **N8 Cross-cycle echo:** prior failed Koide `r` routes are treated only as
  refuted-route context, not as evidence that the proposed premise is adopted.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2`; **not** adoption of the per-cell
  equipartition-granularity premise; **not** a charged-lepton mass prediction.
- **Not** a universal route-closure claim: no claim is made that a future
  larger premise surface cannot derive the equipartition granularity. The
  independence is relative to the **current checked** Record/Koide bookkeeping
  surface, witnessed by the exhibited witnesses, the live Qualification/primitive
  non-supply boundary, and the historical 06-05 corroboration.
- **Not** a new microscopic moment-bridge: the Gaussian moments are computed by
  honest integration and give `r = 1` for both bookkeepings (diagnostic only);
  the `r = 1/2` endpoint follows only from the supplied per-outcome-cell
  equipartition granularity `E_s = E_d`. The landed partition integrals are kept
  only as a normalization/determinant-power cross-check, decoupled from `r`.
- **No** PDG/fitted input in any derivation step (PDG `Q` is a labeled
  comparator); **no** new axiom, primitive, vocabulary, or class tag is added by
  this note (the candidate is *proposed*, with approval routed through
  `AXIOM_MINIMALITY_POLICY.md` §6 exactly as for the kinetic-isotropy primitive).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, `PASS=39`): the orbit partition (`K(e₁)=e₂`); the
  `Q`-lever (100 draws); the honest Gaussian moments `⟨a²⟩ = ⟨|b|²⟩ = 1/(6β)`
  giving `r = 1` for BOTH the holomorphic one-complex-slot and the realified
  two-real-slot bookkeeping (the 2026-07-10 audit finding, reproduced as a
  diagnostic), the normalization-independence of the moment `r`, and the
  diagnostic's explanation (the Gaussian moments satisfy per-mode equipartition
  in expectation, `⟨3a²⟩ = ⟨6x²⟩ = ⟨6y²⟩ = 1/(2β)`); the per-real-mode law
  solved exactly (componentwise and invariant forms) to `|b|² = a²`, `r = 1`;
  the per-outcome-cell law `E_s = E_d` solved exactly to `|b|² = a²/2`,
  `r = 1/2`, `Q = 2/3` (the quantum `ε` cancels in both); the parity table (one
  differing named element — the law's granularity — with both toggles); the two
  witnesses' checked constraint-consistency; the four landed partition
  integrals `2π/g` and `π/g` (Gaussian and Berezin) kept as a
  normalization/determinant-power cross-check decoupled from `r`; the
  mechanical live axiom-surface and primitive text checks; the
  granularity/outcome counting; the PDG comparator arithmetic.
- **Cited:** [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  (the `E_s = 3a^2`, `E_d = 6|b|^2` lever used by the equipartition
  derivation); [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  (current Qualification non-supply clauses);
  [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  (state-side non-supply);
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (historical corroboration only for the superseded non-supply clause);
  [`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md)
  (T1 supplied ORBIT-INDEXING for outcomes-as-K/CPT-orbits);
  [`AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md) §6 (the
  approval mechanism the proposal would route through); the refuted-route corpus
  (#2624, #2688, #3138) as non-re-walk boundaries.

**Context (not load-bearing: backticked names are context, not dependency
edges):**

- `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` — where the
  four-cell mechanism landed (open-gate row); the cells are recomputed from
  explicit per-cell actions in this note's runner, and the landed table is
  consumed only as a consistency cross-check.
- `KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md` —
  the reduction history (how the r-gate narrowed to this atom); framing only, no
  content consumed.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
