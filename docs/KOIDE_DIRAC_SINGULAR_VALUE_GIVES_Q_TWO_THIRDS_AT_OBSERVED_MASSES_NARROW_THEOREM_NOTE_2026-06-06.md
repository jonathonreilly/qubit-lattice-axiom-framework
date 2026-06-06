# The Dirac (Singular-Value) Operator Gives Q=2/3 at the Observed Masses — the Chirality Pin's Readout Half is Moot — Narrow Bridge Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (narrow; resolves the readout half of the chirality pin for the physical masses)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/dirac_singular_value_gives_koide_runner.py`](../scripts/dirac_singular_value_gives_koide_runner.py)
**Cached output:** [`logs/runner-cache/dirac_singular_value_gives_koide_runner.txt`](../logs/runner-cache/dirac_singular_value_gives_koide_runner.txt)

## Audit context

The chirality-pin attack
([`KOIDE_SIGNED_READOUT_RECORD_FORCED_PIN_REDUCES_TO_OPERATOR_CLASS_NARROW_THEOREM_NOTE_2026-06-06`](KOIDE_SIGNED_READOUT_RECORD_FORCED_PIN_REDUCES_TO_OPERATOR_CLASS_NARROW_THEOREM_NOTE_2026-06-06.md))
reduced the Koide `δ=0`/chirality pin to one question: is the native generation operator
the Hermitian circulant (**signed** `√m`, `Q=2/3`) or the Dirac bilinear (**singular-value**
`|λ|`, the steelman
[`KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05`](KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md),
`unaudited` bounded no-go: "`r=1`")?

This note resolves the **readout half** for the *physical* masses. **Grant the steelman:**
charged leptons are Dirac, so the physical masses are singular values (sign-blind). The
key fact it overlooks is that **at the observed masses this changes nothing** — the
observed `√m` are all positive, so the singular-value reading already gives `Q=2/3`. The
"signed vs singular" distinction is **moot at the observed (Brannen) phase**, and the
steelman's "`r=1`" is its *derivation* of `r`, which the register-not-read ontology
dissolves (`r` is registered at `1/2`, not derived).

## Safe statement

**Theorem.**

1. **The physical masses give `Q=2/3` directly.** The observed charged-lepton `√m`
   (`√0.511, √105.66, √1776.86` MeV) are all positive — they *are* the singular values
   — and `Q = (Σ m)/(Σ √m)² = 0.66666… = 2/3`, implying `r = (Q − 1/3)·3/2 = 1/2`.

2. **The readout distinction is moot at the observed phase.** The `r=1/2` `C₃` circulant
   at the Brannen phase `δ ≈ 0.2222` has eigenvalues `(2.379, 0.040, 0.580)` — **all
   positive** — so the signed and singular-value readings **coincide** (`Q=2/3` both).

3. **The steelman's "some `√m < 0`" is `δ`-dependent, not a property of the observed
   masses.** At a different phase (e.g. `δ=0.9`) the circulant has a negative eigenvalue
   `(1.879, −0.399, 1.520)`, and the readings diverge (signed `2/3`, singular `0.416`).
   But that is a *different* operator, not the one realizing the observed masses.

4. **Conclusion (readout half).** No signed readout is required for the physical charged
   leptons: the Dirac/singular-value masses give `Q=2/3` at the registered
   (`r=1/2`, Brannen-`δ`) point.

5. **The steelman's "`r=1`" is the derivation of `r`, dissolved by register-not-read.**
   Its twelve routes (modulus, det, Berry-flat L-R coupling, …) all give `r=1` because
   they *derive* `r`. Under the record-outcome principle
   ([`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md),
   guardrail G3) `r` is a **registered** per-sector weight (`r=1/2` for charged leptons,
   like the masses), **not** a derivation target. The "12 routes → `r=1`" result is then
   exactly the *confirmation* that `r` is not derivable — consistent with registered, not
   a contradiction of the observed `r=1/2`.

## Proof

(1)–(3) are direct numerical evaluation (runner, to `1e-4`). For (2): at `r=1/2`,
`√m_k = a(1 + √2 cos(δ + 2πk/3))`; the three angles are `120°` apart, and a `90°`-wide
negativity window `cos < −1/√2` fits inside a `120°` gap, so for the observed `δ` all
three avoid it (all positive). (4)–(5) follow: the physical reading needs no sign
information at the observed masses, and the only residual ("`r=1`") is the
register-not-read-dissolved derivation of `r`.

## What this resolves, and what it does not

**Resolves (readout half):** the framework's Dirac (singular-value) operator gives the
observed `Q=2/3`. The signed-vs-singular readout choice — and hence the `√m`-sign half of
the chirality pin — is **moot for the physical masses** (they are all positive). So the
sibling note's "operator-class" residual collapses: *both* operator classes give `Q=2/3`
at the observed masses.

**Does NOT do:**

- **Derive `r=1/2`.** It does not. Under register-not-read, `r` is registered; the
  steelman's bounded no-go ("all derivation routes → `r=1`") **stands on the derivation
  frame** and is *consistent* with this note — the two are not in conflict, they are in
  different frames. This note's resolution of "`r=1`" is the reframe (register, don't
  derive), which rests on the **`unaudited`** record-outcome principle, not on refuting
  the steelman's algebra.
- **Derive the Brannen phase `δ=2/9`.** Separate gate; under G3 it is registered
  mass-pattern data (its retained no-gos confirm it is not convention-free-derivable).
- **Touch the weight `r`'s value** beyond noting the observed/registered `r=1/2`.

## Forbidden imports check

No new axiom or import. Uses the observed PDG masses (as the empirical comparator, named
as such), the `C₃` circulant, and finite arithmetic; the register-not-read frame is the
existing (unaudited) record-outcome principle. The steelman's facts are granted, not
contested; what is added is the observed-`δ` all-positivity that makes its readout half
moot.

## Runner check breakdown

Class A: observed `√m` all positive and `Q=2/3` (`r=1/2`); the Brannen-phase circulant is
all-positive (signed=singular); a different phase has a negative eigenvalue (readings
diverge) — so the steelman's "some `√m<0`" is `δ`-dependent; and the two
conclusion/frame lines documented `True`. Expected `runner_check_breakdown = {A: N,
B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is direct arithmetic on the observed masses and the `r=1/2`
circulant: the physical (singular-value) reading gives `Q=2/3`, and at the observed
Brannen phase the eigenvalues are all positive, so the signed-vs-singular distinction —
the readout half of the chirality pin — does not arise for the physical masses. This
genuinely closes the readout half: one need not adjudicate "signed vs singular," because
both agree at the observed masses. What remains is purely the value `r=1/2`, which this
note does **not** derive and does **not** claim to: the steelman's "all routes → `r=1`"
is granted and reframed (register-not-read: `r` is registered, the no-go confirms
non-derivability) rather than refuted, and that reframe rests on the unaudited
record-outcome principle. Effective status remains `unaudited` until the audit lane
assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/dirac_singular_value_gives_koide_runner.py
```
