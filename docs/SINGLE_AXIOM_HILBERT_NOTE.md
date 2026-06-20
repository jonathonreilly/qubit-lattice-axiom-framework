# Local Tensor Product Hilbert Space + Local Hamiltonian + Born Readout: Operational Reduction Note

**Date:** 2026-04-12 (originally); 2026-05-10 (audit-narrowing refresh:
explicit class-E definitional-compression framing under named admitted
inputs); 2026-06-17 (runner/source drift repair for Test 4 and synthesis).
**Status:** scope-narrowed bounded operational note. The runner numerically
verifies four consequences (Hamiltonian-support graph recovery, Born-rule
`I_3 = 0` at machine precision, unitarity-vs-Lindblad behaviour, tensor-
product locality) **after** the named inputs `(local d, local Hermitian H,
Born readout)` are supplied. The "single axiom" framing is a definitional
compression of those inputs into the phrase "local tensor product Hilbert
space"; this note **does not** derive the local-Hamiltonian, the locality
restriction, or the Born readout from the bare tensor-product Hilbert
space alone.
**Claim type (in-note framing):** bounded operational note —
`(local d, local Hermitian H, Born readout, "support = edges"
extraction rule)` ⇒ four runner-verified numerical consequences.
The prior audit ledger recorded `claim_type: bounded_theorem` (audited,
2026-05-11) with verdict `audited_renaming`; this in-note framing is
aligned with that historical `bounded_theorem` row and the renaming verdict,
and does not propose any further audit-side `claim_type` revision. The
earlier 2026-05-05 audit row recorded `claim_type: positive_theorem`; the
2026-05-11 re-audit moved the row to `bounded_theorem`, matching this note's
scope-narrowed framing. After this source refresh, independent re-audit owns
the current status.
**Status authority:** independent audit lane only.
**Authority role:** records that the four numerical consequences follow
from `(H = ⊗_i H_i, local Hermitian H, Born readout)` as a class-E
definitional substitution. **Does not** propose retained, positive-
theorem, or framework-reduction promotion. The accepted-input ledger
for the current paper package remains the Lattice + Quantum + Record
front-door surface in `docs/MINIMAL_AXIOMS_2026-06-05.md`.
**Runner:** `scripts/frontier_single_axiom_hilbert.py`

**2026-06-17 runner/source drift repair:** the executable runner and this
source note now agree that Test 4 does **not** prove monotone distance-decay
with graph distance. The current fixed-seed Test 4 output reports
`Locality gradient (near > far): False`; the bounded support is only the
spread/localization contrast between the supplied tensor-product local
Hamiltonian and an unfactored random Hamiltonian of the same dimension. The
runner synthesis has therefore been demoted from the old "single axiom
reduction" language to the admitted-input operational-support boundary already
stated in this note.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this Hilbert-surface wrapper is a non-chain-closing
alias/decorative handle, the current framework parent candidate is
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

**Scope note:** this is an operational support note for Hilbert-surface
scoping. It is not the load-bearing accepted-input ledger for the current
paper package, whose framework statement is the Lattice + Quantum + Record
front-door surface recorded in `docs/MINIMAL_AXIOMS_2026-06-05.md`.

## Source boundary (2026-06-12)

**Boundary:** renaming / definitional-compression support only. Effective
status is audit-derived; this source records only the claim boundary.

The four numerical checks are valid after the local dimension, local
Hermitian Hamiltonian, Born readout, and graph-extraction rule are stipulated.
This note may be cited only for those operational consequences under the
stated inputs. It may not be cited as a derivation of the Hamiltonian,
Hermiticity/locality restriction, Born rule, graph support extraction, or the
current accepted-input ledger.

Promotion beyond renaming support requires deriving those inputs from a
strictly smaller retained framework surface, and repairing the Test 4
source/runner drift before any stronger use.

## Audit boundary (2026-05-10 refresh of 2026-05-05 verdict; prior 2026-05-11 re-audit confirmed `audited_renaming` and updated `claim_type` to `bounded_theorem`)

The 2026-05-05 audit recorded the verdict `audited_renaming` (load-
bearing-step class E, criticality `critical`). The 2026-05-11 re-audit
confirmed `audited_renaming` and updated the ledger `claim_type` from
`positive_theorem` to `bounded_theorem`, matching the scope-narrowed
operational framing adopted here. The 2026-05-05 audit's
`chain_closure_explanation`:

> *The chain does not close from the single axiom alone because the
> Hamiltonian, its Hermiticity, its local support restriction, and the
> rule for reading interaction support as graph topology are additional
> inputs. The note itself acknowledges that H and the local-interaction
> qualifier do real load-bearing work beyond the tensor-product Hilbert
> space.*

The audit's `verdict_rationale`:

> *The runner numerically demonstrates consequences after constructing
> Hamiltonians with selected support, choosing Born-rule probabilities,
> and comparing unitary/Lindblad examples, but it does not derive those
> structures from the single Hilbert-space axiom. The conclusion mainly
> repackages several specifications into the phrase "local tensor product
> Hilbert space" and then reads graph/locality/unitarity back out of the
> added Hamiltonian data. This is a definitional compression rather than
> a first-principles derivation from the stated axiom.*

This note adopts the explicit class-E definitional-compression framing.
The four named admitted inputs are listed in §"Admitted-context inputs"
below; each is a real upstream gap, not an import-redirect. The
load-bearing step is `(local d, local H, Born readout) ⇒ four numerical
consequences`, evaluated mechanically by the runner.

**Admitted-context inputs (not derived in this note):**

1. The local Hilbert dimension `d` for each tensor factor `H_i`.
2. A Hermitian, local-support Hamiltonian `H` on `⊗_i H_i` (the
   restriction to neighbour-only support is part of the input, not a
   consequence of the tensor-product structure).
3. The Born readout convention `P(outcome) = |<outcome | psi>|^2`
   (chosen, not derived; replaced by `p`-norm in Test 2 to confirm
   `I_3 ≠ 0` for `p ≠ 2`).
4. The rule "interaction support of `H` on tensor factors **defines**
   the graph edges" (a graph-extraction convention used by Test 1).

**Cited authorities (cited as related, not as authority closure):**

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the
  current Lattice + Quantum + Record front-door surface. Cited as related,
  not as authority closure for the local-Hamiltonian or Born-readout inputs
  imported above.

## Question (scope-narrowed)

Given the named admitted inputs `(local d, local Hermitian H, Born
readout, "support = edges" extraction rule)`, do the four numerical
consequences (graph recovery, `I_3 = 0`, unitarity vs. Lindblad,
tensor-product locality) follow mechanically?

**Definitional compression (class-E):** packaging the four admitted
inputs together gives the phrase "a finite Hilbert space with local
tensor product structure, `H = H_1 ⊗ H_2 ⊗ ... ⊗ H_N`". The
load-bearing step is the mechanical evaluation of the four consequences
under those admitted inputs. **This is not** a first-principles
derivation of the inputs themselves from a strictly smaller axiom set.

## Tests and Results

### Test 1: Graph support recovered from supplied Hamiltonian support

Built random local Hamiltonians on 5-qubit systems with random interaction
graphs (3--10 edges per trial). Extracted the interaction graph by decomposing
H into a product operator basis and checking for non-trivial 2-site
components.

| Trial | Input edges | Recovered edges | Match |
|-------|------------|-----------------|-------|
| 1     | 3          | 3               | yes   |
| 2     | 8          | 8               | yes   |
| 3     | 4          | 4               | yes   |
| 4     | 8          | 8               | yes   |
| 5     | 5          | 5               | yes   |

Recovery rate: 100% **under the admitted "support = edges" extraction
rule (input 4 above)**. The graph in this test is the support of the
admitted local `H` on the tensor factors, read out under the admitted
extraction convention. The graph is not derived from the bare tensor-
product Hilbert space; it is the runner-verified consequence of the
admitted local `H` and the admitted extraction rule.

### Test 2: Admitted Born readout gives `I_3 = 0`

Third-order interference I_3 computed for 200 random state pairs in
dimension-8 Hilbert space.

| Framework         | mean |I_3|   | max |I_3|    |
|-------------------|--------------|---------------|
| Hilbert (p=2)     | 1.3 x 10^-17 | 2.6 x 10^-16 |
| p-norm p=1.5      | 7.0 x 10^-3  | 5.3 x 10^-2  |
| p-norm p=3.0      | 2.0 x 10^-3  | 2.9 x 10^-2  |
| p-norm p=4.0      | 1.0 x 10^-3  | 3.6 x 10^-2  |

Under the admitted Born readout `P = |<·|·>|^2` (input 3 above),
`I_3 = 0` to machine precision. Replacing the admitted Born readout
with any `p`-norm at `p ≠ 2` gives `I_3 ≠ 0`. This confirms the Born
readout is a real admitted input: the bare Hilbert tensor-product
structure does not by itself force `p = 2`. The standard reading
"the inner product forces the Born rule" is a definitional
substitution: choosing the inner-product convention for readout is
equivalent to choosing the `p = 2` norm.

### Test 3: Hermitian generator gives unitary toy evolution; Lindblad control breaks it

8-site chain with 1/r gravitational potential. Unitary evolution concentrates
probability at the gravitational center. Lindblad (non-unitary) evolution with
increasing dephasing rate gamma:

| gamma | Center excess | Behavior                        |
|-------|---------------|---------------------------------|
| 0.0   | +0.104        | Probability at center (toy attraction profile) |
| 0.1   | +0.078        | Weakened attraction              |
| 0.5   | -0.005        | Attraction destroyed             |
| 1.0   | -0.078        | Stuck near source                |
| 2.0   | -0.167        | Localized at source              |

Unitarity follows from the admitted Hermitian Hamiltonian (input 2
above). Non-unitary evolution (open systems, Lindblad channels)
destroys gravitational attraction — particles freeze at their source
instead of migrating toward the potential minimum. The Hermiticity
restriction is therefore a real admitted input: replacing it with
non-Hermitian Lindblad dynamics changes the consequence.

### Test 4: Tensor-product/local-H packet gives bounded localization support

Compared a 6-qubit chain (tensor product, local Hamiltonian) to a random
64x64 Hamiltonian (same dimension, no factorization).

| Metric               | Tensor product | Unfactored |
|----------------------|---------------|------------|
| Participation ratio  | 1.0 / 6 sites | 30.2 / 64 states |
| Distance dependence  | No monotone decay claim; fixed-seed gradient check is false | No graph-distance notion |
| Spread ratio         | 29x more localized | baseline |

Without the admitted tensor-product factorization, there is no notion
of locality, distance, or spatial structure: the propagator spreads
uniformly rather than respecting any supplied factorization. The runner's
valid Test 4 support is the participation-ratio/spread contrast. It does not
establish that the fixed-seed amplitudes decay monotonically with graph
distance; the runner prints that monotone-gradient diagnostic as false.
The tensor-product factorization plus the admitted local Hamiltonian
(inputs 1+2) jointly give the bounded localization contrast. Neither input
alone suffices: an unfactored same-dimension Hamiltonian gives much broader
spread.

## Conclusion (scope-narrowed)

Under the four named admitted inputs (local `d`, local Hermitian `H`,
Born readout, "support = edges" extraction rule), the four numerical
consequences follow mechanically as evaluated by the runner:

- The graph **is recovered** as the interaction support of the
  admitted local `H` under the admitted "support = edges" extraction
  rule (Test 1).
- The Born rule `I_3 = 0` **holds** at machine precision under the
  admitted Born readout (Test 2). Replacing the readout with a
  `p`-norm for `p ≠ 2` gives `I_3 ≠ 0`, confirming the readout is a
  real input.
- Unitary toy evolution follows from the admitted Hermitian generator
  (Test 3); a non-Hermitian Lindblad replacement breaks the toy attraction
  profile, confirming the Hermiticity restriction is a real input.
- The admitted tensor-product factorization gives a bounded localization
  contrast by participation ratio; an unfactored same-dimension Hamiltonian
  is much broader. The runner does not claim monotone distance-decay in the
  fixed Test 4 sample (Test 4).

**Definitional-compression framing.** The four admitted inputs
`(local d, local H, Born readout, "support = edges" rule)` can be
packaged together under the phrase "a finite Hilbert space with local
tensor product structure". This packaging is a class-E definitional
compression, not a derivation: replacing the package with the four
itemized inputs makes explicit that the local Hamiltonian and the
locality restriction do real load-bearing work, as the audit verdict
recorded.

## Honest scope limits (explicit, not import-redirect)

1. **The local Hermitian `H` and its locality restriction are real
   admitted inputs**, not consequences of the bare tensor-product
   Hilbert space. A tensor-product space with all-to-all interactions
   would not give spatial locality; the restriction is part of the
   admitted package.

2. **The Born readout is a real admitted input.** Test 2 confirms this
   by demonstrating `I_3 ≠ 0` under any `p`-norm with `p ≠ 2`. The
   tensor-product structure does not by itself force `p = 2`.

3. **The "support = edges" graph-extraction rule is a real admitted
   input.** Without it, Test 1's recovery procedure is not defined.
   The graph is not a consequence of the tensor-product structure
   alone; it is the support of the admitted local `H` under the
   admitted extraction rule.

4. **These are small-system demonstrations (5--8 sites).** The
   argument is structural and holds at any scale, but large-scale
   gravitational physics tests (distance law, etc.) use the 3D
   lattice infrastructure in other frontier scripts.

5. **Authority surface unchanged.** The accepted-input ledger for the
   current paper package remains the Lattice + Quantum + Record front-door
   surface in `docs/MINIMAL_AXIOMS_2026-06-05.md`. This note is a Hilbert-surface
   operational support note; it does not propose framework-reduction
   promotion, nor does it claim to be a smaller axiom set than the
   recorded minimal-axioms surface.
