# Generation Prior Stability: Post-Record Equal-Letter vs Pre-Record Born Dial

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-05
**Claim type:** meta
**Status authority:** independent audit lane only. This source note does not set,
predict, or assert an audit verdict and does not claim "retained" or "promoted"
standing. No proposal language. Independent audit is required before any
authority-surface use.
**Primary runner:**
[`scripts/frontier_generation_prior_stability_2026_06_05.py`](../scripts/frontier_generation_prior_stability_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_generation_prior_stability_2026_06_05.txt`](../logs/runner-cache/frontier_generation_prior_stability_2026_06_05.txt)
(`PASS=23 FAIL=0`).

---

## What this note executes

This note executes the next trace action named by the Record classicalization
dynamics firewall:

> "The generation/Koide dial still needs a stability or selection argument for
> why one prior should be chosen in a given dynamical setting."
> — [`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md`](RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md).

The firewall sets a typed grammar for the generation dial:

| Surface | Object | Prior it suggests |
|---|---|---|
| pre-record | qubit state / readout context | dimension/Born prior `(1/3, 2/3)` |
| record event | instrument `{K_r}` | writes one realized letter `e_r` |
| post-record | additive count `c -> c + e_r` | (analyzed here) |

The firewall left **open** whether the post-record (equal-letter / count)
dynamics *selects* the dial `r = 1/2`, or merely clarifies that the dial is not a
category error. This note answers that question, honestly and adversarially.

## Verdict (one line)

**CLARIFIES-GRAMMAR-SELECTION-OPEN.** The post-record dynamics does **not** force
the equal-letter side. The firewall makes the equal-letter prior a *legitimate
post-record TYPE prior*, but the post-record *count dynamics* (token frequency)
actually points to the Born/dimension side `(1/3, 2/3) -> r = 1`. So `r = 1/2`
remains an **unforced stable setting**, not a value the dynamics selects.

This is consistent with — and sharpens — the two adjacent live surfaces:

- the retained-surface theorem
  [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md),
  which records the singlet/doublet weighting as **permitted-not-forced**;
- the retained-bounded separatrix result
  [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
  which shows `r = 1/2` is the **unstable separatrix** of the Lüders sharpening
  map `r -> 2r^2`.

## The supplied objects (none derived here)

1. **Two letters.** The generation readout context resolves exactly two K/CPT
   orbits — a singlet (dim 1) and a doublet (dim 2) — from
   [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)
   (on `main`).

2. **The operator dial.** The mass operator is the circulant Yukawa on the
   `C3` generation carrier,
   `lambda_j = a + 2|b| cos(theta + 2 pi j / 3)`, giving the
   theta-independent power split `Q = 1/3 + (2/3) r` with the operator dial
   `r = |b|^2 / a^2`. Then `r = 1/2 <=> a^2 = 2|b|^2 <=> Q = 2/3`;
   `r = 1 <=> Q = 1`; `r = 0 <=> Q = 1/3`. (Circulant-spectrum provenance:
   [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
   and the equipartition corpus.) Runner block `O1`–`O4`.

3. **The post-record dynamics.** The firewall's additive count update
   `c -> c + e_r`, with the realized letter `r` drawn from the predictive (Born)
   weights of the readout context.

The two-letter partition, the operator dial, and the Born predictive weights are
the **specified context**; this note neither re-derives them nor adds an axiom.

---

## Q1 — Token-counting vs type-counting (the precise distinction)

The post-record count vector `c` admits **two different normalizations**, and
they land on **opposite sides of the dial**:

- **Token frequency** `n_r / N` (normalize counts). Under `c -> c + e_r` with
  `r ~ Born`, the strong law gives `n_r / N -> (1/3, 2/3)`. In the 2-sector
  power model `p_s = 1/(1+2r)`, `p_d = 2r/(1+2r)`, the weight `(1/3, 2/3)` maps
  to **`r = 1` (`Q = 1`)**. Runner `T1`, `T4`, `T6`, seeded LLN
  (`N = 10^2, 10^4, 10^6`: doublet token freq `0.600 -> 0.665 -> 0.6656`,
  target `2/3`).

- **Type count** `#{ letters with count > 0 }` (normalize the realized
  **support**, not the counts). Once both letters have appeared this is the
  uniform `(1/2, 1/2)`, which maps to **`r = 1/2` (`Q = 2/3`)**. Runner `T2`,
  `T5`.

So the "equal-letter post-record prior" is the **type/support-cardinality**
reading. It is a *different functional of the same count vector* than the token
frequency (`T3`), and it **discards** the frequency information. The token
frequency — the genuine count dynamics — flows to Born, **not** to equal-letter
(`T6`: `|token doublet freq - 1/2| = 0.166` at `N = 10^6`).

**Clean alignment found:** the **pre-record dimension prior** `(1/3, 2/3)` and
the **post-record token-frequency limit** *coincide* at `(1/3, 2/3) -> r = 1`
(`X3`). The equal-letter `(1/2, 1/2) -> r = 1/2` is **neither** of these; it is
only the support count.

## Q2 — Which surface governs the mass-operator sector weighting? (the crux)

The dial `r = |b|^2 / a^2` is a property of the **mass operator** (the circulant
Yukawa): it is a function of the operator parameters `a, b` **only**, independent
of which eigenvalue/index `j` is realized in any record (`O2`). A realized record
atom `e_r` is a one-hot label naming **which eigenvalue/event** was registered;
it does **not** encode the ratio `r` and is neither prior distribution (`X1`).

Therefore the dial is a **pre-record** object. The chain
"masses are post-record records `->` equal-letter `->` `r = 1/2`" would require
**imposing** the equal-letter weight on the operator's sector power, i.e. setting
`a^2 = 2|b|^2` by hand (`X2`). That is a pre-record **operator stipulation**, not
a consequence of any record being written. Reading the operator ratio off the
post-record letter is thus a **type error / circular** for the purpose of
*selecting* the dial:

> the records grammar tells you which letter was *realized*; it does not tell you
> how the operator *weights its sectors* — and the dial is the latter.

This is the honest answer to the crux the trace action posed: the
sector-power-balance `a^2 = 2|b|^2 <=> r = 1/2` is a **pre-record (operator)**
property, so "masses are post-record records `->` `r = 1/2`" does **not** select
the dial.

## Q3 — Is equal-letter a stable fixed point of the post-record dynamics?

Equal-letter is a fixed point **only in a degenerate sense**: the *set* of
realized letters stops changing once both letters appear (`V1`). That is
support-stability, not value-selection — it throws away the frequency the count
dynamics actually evolves.

Adversarial check (does **any** non-circular post-record dynamics flow to
equal-letter?). All four candidates fail or smuggle equal-letter in:

| Candidate dynamics | Limit | Selects equal-letter? |
|---|---|---|
| additive count `c -> c + e_r` (the firewall's own) | token freq `-> (1/3, 2/3)` | **No** — flows to Born / `r = 1` (`additive-count candidate`) |
| Lüders state-sharpening `p -> p^2/Z` `=` `r -> 2r^2` | `r = 1/2` repels both sides | **No** — `r = 1/2` is the *unstable* separatrix (`B1`, `B2`) |
| max-entropy on the 2 letters, **unconstrained** | uniform `(1/2, 1/2)` | **Circular** — imposes the type/support as the state space (`C1`) |
| max-entropy **constrained to the observed token mean** | Born `(1/3, 2/3)` | **No** — returns Born (`C2`) |
| Pólya / self-reinforcing urn | random, prior-dependent limit | **Circular** — hits `1/2` only under a symmetric seed = equal-letter by hand (`E1`, `E2`) |

So **no non-circular post-record dynamics selects equal-letter**, and the
firewall's own count dynamics favors Born / `r = 1` (`V2`, `V3`). Equal-letter
survives only as a non-dynamical *type prior*.

---

## What this buys (and what it does not)

**Buys (bounded):**

1. A precise **token-vs-type** statement: the firewall's count dynamics
   (token frequency) `-> Born (1/3, 2/3) -> r = 1`; the equal-letter
   `(1/2, 1/2) -> r = 1/2` is the **type/support count**, a dynamics-free prior.
2. A clean **crux resolution**: the dial `r = |b|^2/a^2` is a **pre-record
   operator** property, so "masses are post-record `->` `r = 1/2`" is circular
   for selecting the dial.
3. A confirmation that the dial is **not a category error** (the firewall's
   stated win): equal-letter is a coherent post-record *type* prior, comparable
   to the pre-record dimension prior as a dial setting.
4. An alignment note: the **pre-record dimension prior** and the **post-record
   token limit** coincide at `(1/3, 2/3) -> r = 1`; both point away from
   `r = 1/2`, consistent with the retained pieces.

**Does NOT (honest non-claims):**

- does **not** derive the equal-letter prior;
- does **not** force the dial to either side;
- does **not** derive a Koide value;
- does **not** identify the physical record-production dynamics, an arrow of
  time, a decoherence model, or an operational Born-frequency mechanism;
- does **not** assert any audit status (the audit lane sets status).

## What remains open

- A **stabilizer** for the 2-sector (singlet/doublet) partition as the physical
  record basis is still missing — the same open object the separatrix note
  isolates (einselection / predictability sieve on the commutant of a `C3`-
  invariant interaction). If such a stabilizer existed, equal-letter could be
  promoted from a type prior to a selected setting; this note does not supply it.
- The Born **operational-frequency** identification remains separate from the
  algebraic probability functional (consistent with the adjacent
  `BORN_QUANTUM_RECORD_UNCONDITIONAL_FORM_VS_OPERATIONAL_RESIDUAL` branch).
- Whether the operator weights its two sectors by **block-count** (`-> r = 1/2`)
  or by **dimension/trace** (`-> r = 1`) is exactly the
  `permitted-not-forced` slot in
  [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md);
  this note does not close it, and shows the post-record dynamics does not close
  it either (it leans token/Born).

## Verification

```bash
python3 scripts/frontier_generation_prior_stability_2026_06_05.py
# PASS=23 FAIL=0
python3 -m py_compile scripts/frontier_generation_prior_stability_2026_06_05.py
git diff --check
```

| Block | Content |
|---|---|
| O1–O4 | operator dial `r = |b|^2/a^2`, `Q = 1/3 + (2/3) r`, `r=1/2 <=> a^2=2|b|^2`; `r` index-independent |
| T1–T6 | token frequency `-> Born / r=1` (seeded LLN) vs type count `-> uniform / r=1/2`; distinct functionals |
| X1–X3 | record atom is one-hot, not the ratio; `r=1/2`-from-records is circular; pre-record dim prior `=` post-record token limit |
| additive-count, Lüders, maxent, Pólya candidates | adversarial: none non-circularly select equal-letter |
| V1–V3 | synthesis: equal-letter stable only as support count; dynamics favors Born; verdict CLARIFIES-GRAMMAR-SELECTION-OPEN |

## Provenance

- **Upstream support:**
  [`RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md`](RECORD_CLASSICALIZATION_DYNAMICS_FIREWALL_2026-06-05.md) — the typed
  pre-record / record / post-record grammar and the `c -> c + e_r` count
  dynamics whose stability this note analyzes.
- **Two-letter partition (on `main`):**
  [`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)
  (singlet + doublet; weighting recorded as permitted-not-forced).
- **Separatrix prior art (on `main`):**
  [`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md)
  (`r -> 2r^2`; `r = 1/2` unstable separatrix; `S2` peaks at `1/2`, `S3` at `1`).
- **Operator dial / circulant spectrum (on `main`):**
  [`KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md`](KOIDE_Q23_K0_REAL_BLOCK_EQUIVALENCE_NOTE_2026-05-30.md)
  and the equipartition corpus (`Q = 1/3 + (2/3)|b|^2/a^2`, theta-independent).
- **Axioms:** [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) (Record).

## Admitted-context mathematical inputs

The strong law of large numbers for i.i.d. Bernoulli draws; one-dimensional
fixed-point stability (`|f'| <=> 1`); Shannon entropy and Lagrange max-entropy on
a finite alphabet (the unique distribution on `{0,1}` with mean `t` is `(1-t, t)`);
the Pólya urn limit law (martingale convergence to a Beta-distributed random
limit). Universal mathematics; not framework-derived. No PDG value, fitted
constant, literature comparator, or unit convention is consumed.
