# Local Tensor Product Hilbert Space + Local Hamiltonian + Born Readout: Operational Reduction Note

**Date:** 2026-04-12 (originally); 2026-05-10 (audit-narrowing refresh:
explicit class-E definitional-compression framing under named conditional
inputs); 2026-06-17 (runner/source drift repair for Test 4 and synthesis);
2026-07-17 (Test 4 common-outcome-space and Hamiltonian-scale repair).
**Type:** bounded_theorem
**Status:** scope-narrowed bounded operational note. The runner numerically
verifies four consequences (Hamiltonian-support graph recovery, Born-rule
`I_3 = 0` at machine precision, fixed unitary/strong-dephasing toy behaviour,
and a
matched-scale local-H localization contrast) **after** the named inputs
`(local d, local Hermitian H, Born readout)` are supplied. The "single axiom"
framing is a definitional compression of those inputs into the phrase
"local tensor product Hilbert space"; this note **does not** derive the
local-Hamiltonian, the locality
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
**Audit-status authority:** independent audit lane only.
**Authority role:** records that the four numerical consequences follow
from `(\mathcal H = ⊗_i \mathcal H_i, local Hermitian H, Born readout,
"support = edges" rule)` as a class-E
definitional substitution. **Does not** propose retained, positive-
theorem, or framework-reduction promotion. The current framework baseline
remains Lattice + Qubit + Admissibility + Record in
`docs/MINIMAL_AXIOMS_2026-06-29.md`.
**Runner:** `scripts/frontier_single_axiom_hilbert.py`

**2026-07-17 Test 4 repair:** the executable runner and this source note compare
both propagators on the same 64 mutually exclusive computational-basis
outcomes. Both probability distributions are normalized. Before propagation,
the mean energy `Tr(H)/64` is subtracted from each Hamiltonian (which changes
only a global phase) and the result is rescaled to centered RMS energy
`sqrt(Tr(H_c^\dagger H_c)/64) = 1`. The fixed seed, initial state `|000000>`,
dimensionless time `t=1`, and existing twofold spread-contrast criterion are
unchanged. The control is now described accurately as a dense nonlocal
Hamiltonian on the same factorized Hilbert space, rather than as an
"unfactored" space. Test 4 remains a fixed-seed bounded localization contrast;
it does not prove monotone distance decay or a general localization theorem.

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this Hilbert-surface wrapper is a non-chain-closing
alias/decorative handle, the current framework parent candidate is
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

**Scope note:** this is an operational support note for Hilbert-surface
scoping. It is not the load-bearing framework baseline for the current paper
package, whose framework statement is the Lattice + Qubit + Admissibility +
Record surface recorded in `docs/MINIMAL_AXIOMS_2026-06-29.md`.

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
strictly smaller retained framework surface. The repaired Test 4 remains only
a common-space, matched-scale fixed-seed contrast and supplies no stronger use.

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
The four named conditional inputs are listed in §"Explicit conditional
inputs" below; each is a real upstream gap, not an import-redirect. The
load-bearing step is `(local d, local H, Born readout) ⇒ four numerical
consequences`, evaluated mechanically by the runner.

**Explicit conditional inputs (not derived in this note):**

1. The local Hilbert dimension `d` for each tensor factor `\mathcal H_i`.
2. A Hermitian, local-support Hamiltonian `H` on
   `\mathcal H = ⊗_i \mathcal H_i` (the
   restriction to neighbour-only support is part of the input, not a
   consequence of the tensor-product structure).
3. The Born readout convention `P(outcome) = |<outcome | psi>|^2`
   (chosen, not derived; replaced by the three tested `p`-norm controls in
   Test 2, which give nonzero sampled `I_3`).
4. The rule "interaction support of `H` on tensor factors **defines**
   the graph edges" (a graph-extraction convention used by Test 1).

**Cited authorities (cited as related, not as authority closure):**

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — the current
  Lattice + Qubit + Admissibility + Record framework baseline. Cited as related,
  not as authority closure for the local-Hamiltonian or Born-readout inputs
  specified above.

## Question (scope-narrowed)

Given the named conditional inputs `(local d, local Hermitian H, Born
readout, "support = edges" extraction rule)`, do the four numerical
consequences (graph recovery, `I_3 = 0`, fixed unitary/strong-dephasing toy
behaviour,
matched-scale local-H localization) follow mechanically?

**Definitional compression (class-E):** packaging the four conditional
inputs together gives the phrase "a finite Hilbert space with local
tensor product structure,
`\mathcal H = \mathcal H_1 ⊗ \mathcal H_2 ⊗ ... ⊗ \mathcal H_N`". The
load-bearing step is the mechanical evaluation of the four consequences
under those conditional inputs. **This is not** a first-principles
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

Recovery rate: 100% **under the supplied "support = edges" extraction
rule (input 4 above)**. The graph in this test is the support of the
supplied local `H` on the tensor factors, read out under the supplied
extraction convention. The graph is not derived from the bare tensor-
product Hilbert space; it is the runner-verified consequence of the
supplied local `H` and the supplied extraction rule.

### Test 2: Supplied Born readout gives `I_3 = 0`

Third-order interference I_3 computed for 200 random state pairs in
dimension-8 Hilbert space.

| Framework         | mean |I_3|   | max |I_3|    |
|-------------------|--------------|---------------|
| Hilbert (p=2)     | 1.3 x 10^-17 | 2.6 x 10^-16 |
| p-norm p=1.5      | 7.0 x 10^-3  | 5.3 x 10^-2  |
| p-norm p=3.0      | 2.0 x 10^-3  | 2.9 x 10^-2  |
| p-norm p=4.0      | 1.0 x 10^-3  | 3.6 x 10^-2  |

Under the supplied Born readout `P = |<·|·>|^2` (input 3 above),
`I_3 = 0` to machine precision. In the same fixed-seed packet, the tested
controls `p ∈ {1.5, 3, 4}` give nonzero sampled `I_3`. This confirms the Born
readout is a real conditional input to this packet: the bare Hilbert
tensor-product structure does not by itself force `p = 2`. The standard reading
"the inner product forces the Born rule" is a definitional
substitution: choosing the inner-product convention for readout is
equivalent to choosing the `p = 2` norm.

### Test 3: Hermitian generator gives unitary toy evolution; fixed strong-dephasing control changes the profile

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

Unitarity follows from the supplied Hermitian Hamiltonian (input 2 above).
For this fixed Euler-integrated toy control, adding computational-basis
dephasing at `gamma = 2` leaves more probability at the source than at the toy
potential center. This establishes only the stated unitary-versus-strong-
dephasing profile contrast; it is not a general claim about Lindblad dynamics
or gravitational attraction.

### Test 4: Matched-scale local-H packet gives bounded localization support

Compared a 6-qubit chain-local Hamiltonian with a dense nonlocal random
Hamiltonian on the same 64-dimensional factorized Hilbert space. Both start
from `|000000>` and are read in the same mutually exclusive computational
basis. For each raw Hamiltonian `H`, the runner removes the energy origin and
matches the generator scale by

`H_c = H - Tr(H) I / 64`,

`sigma_H = sqrt(Tr(H_c^2) / 64)`, and `H_matched = H_c / sigma_H`.

Thus both evolutions use `sigma_H = 1` at the same dimensionless time `t=1`.
The shift has no observable effect because it contributes only a global phase;
the RMS normalization matches the mean-square spectral generator scale. This
is an explicit comparison convention, not a derived physical energy scale. It
does not match bandwidths, higher spectral moments, or entrywise matrix scales.

| Metric | Chain-local Hamiltonian | Dense nonlocal control |
|---|---:|---:|
| Outcome space | 64 basis outcomes | same 64 basis outcomes |
| Probability sum | 1.000000 | 1.000000 |
| Centered RMS energy after matching | 1.000000 | 1.000000 |
| Participation ratio `1/sum_z p(z)^2` | 3.2706 / 64 outcomes | 13.1853 / 64 outcomes |
| Spread ratio | 4.0314x more localized | baseline |

The participation ratios are now like-for-like: each is computed from one
normalized distribution over the same 64 mutually exclusive outcomes. Within
this fixed construction, the comparison holds the factorization, readout
basis, initial state, evolution time, and centered RMS energy fixed while
changing the Hamiltonian support class. The dense control does not respect the
chain-local support restriction and is broader in this fixed sample. Test 4
does not establish monotone decay with graph distance. The result is not an
ensemble statement and does not show that tensor-product factorization alone
causes localization.

## Conclusion (scope-narrowed)

Under the four named conditional inputs (local `d`, local Hermitian `H`,
Born readout, "support = edges" extraction rule), the four numerical
consequences follow mechanically as evaluated by the runner:

- The graph **is recovered** as the interaction support of the
  supplied local `H` under the supplied "support = edges" extraction
  rule (Test 1).
- The Born rule `I_3 = 0` **holds** at machine precision under the
  supplied Born readout (Test 2). The three tested nonquadratic controls give
  nonzero sampled `I_3`, confirming the readout is a real conditional input.
- Unitary toy evolution follows from the supplied Hermitian generator
  (Test 3); the fixed `gamma = 2` dephasing control leaves more probability at
  the source than at the toy center. No broader Lindblad claim is made.
- On the supplied factorized Hilbert space, the chain-local Hamiltonian gives a
  bounded fixed-seed localization contrast against a dense nonlocal control.
  Both participation ratios use the same normalized 64-outcome space and
  matched centered RMS energy. The runner does not claim monotone
  distance-decay or an ensemble theorem (Test 4).

**Definitional-compression framing.** The four conditional inputs
`(local d, local H, Born readout, "support = edges" rule)` can be
packaged together under the phrase "a finite Hilbert space with local
tensor product structure". This packaging is a class-E definitional
compression, not a derivation: replacing the package with the four
itemized inputs makes explicit that the local Hamiltonian and the
locality restriction do real load-bearing work, as the audit verdict
recorded.

## Honest scope limits (explicit, not import-redirect)

1. **The local Hermitian `H` and its locality restriction are real
   conditional inputs**, not consequences of the bare tensor-product
   Hilbert space. A tensor-product space with all-to-all interactions
   would not give spatial locality; the restriction is part of the
   supplied packet.

2. **The Born readout is a real conditional input.** Test 2 shows nonzero
   sampled `I_3` for `p ∈ {1.5, 3, 4}`; it does not test every `p ≠ 2`. The
   tensor-product structure does not by itself force `p = 2`.

3. **The "support = edges" graph-extraction rule is a real conditional
   input.** Without it, Test 1's recovery procedure is not defined.
   The graph is not a consequence of the tensor-product structure
   alone; it is the support of the supplied local `H` under the
   supplied extraction rule.

4. **These are fixed-seed small-system demonstrations (5--8 sites).** They do
   not establish large-system scaling, an ensemble result, or a distance law.

5. **Authority surface unchanged.** The current framework baseline remains the
   Lattice + Qubit + Admissibility + Record surface in
   `docs/MINIMAL_AXIOMS_2026-06-29.md`. This note is a Hilbert-surface
   operational support note; it does not propose framework-reduction
   promotion, nor does it claim to be a smaller axiom set than the
   recorded minimal-axioms surface.
