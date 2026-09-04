# Qualitative Substrate Language And Exact-Law Selection

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a scoped finite non-entailment and language-design
probe. It does not select the universe's rule, amend an axiom, register a
premise, set an audit verdict, or claim that no exact uniqueness theorem can
exist.

**Runner:**
[`scripts/qualitative_substrate_exact_law_selection_probe_2026_07_14.py`](../../../../scripts/qualitative_substrate_exact_law_selection_probe_2026_07_14.py)

## Question

Could more fundamental-sounding substrate language derive the remaining TOE
interfaces and remove the need to identify an exact law, or is an exact-law
identity the minimum content that survives?

The question is deliberately sharper than whether words such as `causal`,
`reversible`, `covariant`, `local`, `minimal`, or `compute-limited` are useful.
It asks whether those conditions return one physical answer rather than a
family of inequivalent answers.

## Result

Qualitative structural conditions can remove many candidate axiom clauses,
but they do not by themselves identify an exact predictive law. Two exact
families demonstrate the residual:

1. positive normalized nearest-neighbor bit kernels can be local and covariant
   under global label exchange while predicting different record frequencies;
2. reversible two-qubit interactions can be unitary, exchange-covariant, and
   covariant under every common one-qubit basis change while retaining a
   continuous interaction angle with different measurable transition
   probabilities.

Therefore adding more structural adjectives to Admissibility is not a
substitute for an equation, exact rule table, exact generative object, or a
theorem proving that every remaining representative is physically equivalent.

This is not a universal no-go against derivation. A substrate principle can
close the gap if it is exact enough to yield a uniqueness theorem that fixes
all apparent parameters and every claimed observable. In that case the
principle itself is the exact law, or is a finite definition of it. The
constitutional minimum is still the identity of that exact object unless the
current four axioms uniquely derive it.

## 1. Convex Structural Conditions Leave A Family

For neighbor counts `(n_0,n_1)`, define

```text
q_lambda(0 | n_0,n_1)
  = lambda^n_0 / (lambda^n_0 + lambda^n_1),
q_lambda(1 | n_0,n_1)
  = lambda^n_1 / (lambda^n_0 + lambda^n_1).
```

For every positive `lambda`, the kernel is:

- nearest-neighbor local;
- strictly positive;
- normalized;
- homogeneous; and
- covariant when labels `0` and `1` and their neighbor counts are exchanged.

At `(n_0,n_1)=(2,1)`, `lambda=1` predicts `1/2` while `lambda=2` predicts
`2/3`. Convex mixtures preserve locality, positivity, normalization, and the
same covariance, while the displayed observable varies affinely.

The general scoped theorem is immediate. If a class of predictive laws is
closed under convex mixture, contains two operationally distinguishable
members, and a proposed substrate sentence asserts only properties shared by
that class, the sentence cannot identify the exact law value. Complete
positivity, trace preservation, no-signaling constraints, covariance, and
record preservation are commonly convex conditions. They can be essential
typing conditions without being a selector.

## 2. Reversibility And Extremality Do Not Repair The Gap

Convexity alone could be escaped by requiring a reversible or extremal law.
That escape is real but insufficient. On two neighboring qubits let `S` be
the swap and define

```text
U_theta = cos(theta) I + i sin(theta) S = exp(i theta S).
```

For every real `theta`, `U_theta` is unitary. It commutes with site exchange
and with `V tensor V` for every one-qubit unitary `V`; it therefore privileges
no one-qubit direction or presentation. Yet from `|01>` the probability that
the first qubit becomes `1` is `sin(theta)^2`.

The runner verifies unitarity, exchange covariance, representative common
`SU(2)` basis changes, and four distinct exact predictions. Reversibility and
basis neutrality narrow the rule to a physically important family without
fixing its interaction angle. A homogeneous cubic embedding can likewise use
one common exchange coupling on every edge; lattice symmetry does not choose
that coupling.

A possible objection is that one common angle only sets the clock unit. The
runner therefore adds an independent dimensionless control on a center qubit
and two equivalent neighbors. Both

```text
H_1 = SWAP_01 + SWAP_02,
H_2 = SWAP_01 SWAP_02 + SWAP_02 SWAP_01
```

are Hermitian, invariant under exchanging the two neighbors, and covariant
under every simultaneous one-qubit basis change. The family
`H_eta = H_1 + eta H_2` has three spectral levels. At `eta=0` its consecutive
gap ratio is `2`; at `eta=1/3` it is `1`. No overall clock rescaling or energy
shift changes that ratio. Thus the surviving freedom is not merely a units
convention.

The lesson is not that `theta` must be a new axiom sentence. The lesson is
that the final exact law or a uniqueness theorem must fix it, eliminate it as
a convention, or prove every value operationally equivalent.

## 3. Which Substrate Languages Could Actually Close The Gap

Four forms remain scientifically capable of yielding the missing pieces.
Each succeeds only if written as an exact mathematical object with a complete
interface, not as an architecture name.

### Exact local transition or QCA law

An explicit local instrument, reversible QCA, block rule, or finite gate table
can own the generated carrier, causal readiness, coherent propagation,
formation support, branch weights or deterministic continuation, concurrency,
record preservation, and renewal/export. Full-lattice consistency and the
record-only future-equivalence theorem must then be proved.

### Exact action or variational law

An action can generate dynamics only when its carrier, coefficients, boundary
class, quantization/history rule, and observable map are exact. Symmetry alone
does not fix allowed invariant terms or their coefficients. An action that
leaves a family of couplings is a law family, not the missing law identity.

### Exact rewrite or multiway law

A Wolfram-style rewrite rule plus a causal-invariance theorem can prove that
different admissible update orders describe the same causal history. It still
needs the exact rewrite rule. For quantum or branching claims it also needs an
exact branch algebra/measure and an observer-independent link to the one
record-valued history. Causal invariance removes schedule presentation; it
does not select rule, weight, or actual branch.

### Exact whole-history constraint

A global consistency condition can close actuality if the supplied physical
boundary has a unique extension. A uniquely ergodic deterministic system can
also derive long-run frequencies after its exact law, decoder, preparation,
and corpus are fixed. If several global solutions or invariant measures
remain, the constraint has moved rather than removed the selection input.

These routes may prove most of the current TOE lane interfaces as theorems.
None licenses a generic sentence such as “the universe computes only what it
needs,” because `compute`, `need`, resource accounting, and the exact update
remain undefined there.

## 4. What Bare-Metal Resource Language Can And Cannot Do

The storage/compute intuition has one promising physical reading: commits
consume or displace a locally conserved resource, and local conservation can
generate a long-range Green response after repeated local transport. The
Cycle-9 resource probe derives a `1/r` stationary profile from a local cubic
update and a balanced commit/export current; it does not place `1/r` in the
microscopic rule.

That success does not make “compute-limited” constitutional content. An exact
model must still identify:

- the conserved quantity;
- the commit current and its relation to matter or mass;
- the renewal/export or return cycle;
- the arrow or nonequilibrium affinity sustaining the current;
- the common coupling to every matter carrier; and
- the spatial transport response required for lensing, not only an onsite
  clock slowdown.

These are fields of the exact law and downstream theorems. They become axiom
content only if the project intentionally adopts a resource principle as the
law rather than deriving it.

## 5. Constitutional Consequence

The tested universal residue is not a witness count, a clock-lock sentence, a
possibility-counting convention, a Born clause, a tensor-product clause, or a
storage slogan. It is:

> an exact predictive law identity, or an exactly defined physical-
> equivalence class of representatives, unless uniquely derived from the
> present foundation.

One-history language is additionally required for a genuinely branching
measure-only law unless it is bundled into a sampled-law definition, derived
from unique deterministic/global continuation, or already fixed by an
explicit physical boundary interface. It is not a universal second atom
because deterministic exact laws need no sampling rule.

The public axiom need not print the law. A stable exact reference from
Admissibility can keep the constitution short while the referenced document
holds the equations and theorem obligations. A placeholder such as
`[CANONICAL-LAW]`, `causal computation`, `QCA`, or `multiway evolution` cannot
serve as the reference.

No Record addition follows from this probe. Exact preservation may be a law
theorem; site-tethered permanence versus migrated/re-encoded record identity
cannot be decided before the exact carrier and record lineage are known.

## 6. No-Go Discipline Gate

**Gate result:** `PASS` for the narrow finite claim that the displayed
structural conditions do not select the displayed stochastic or unitary law
value. No exhaustive claim is made against stronger exact principles.

### N1 — alternative routes

The probe tests stochastic kernels, convex mixtures, reversible unitary laws,
exact actions, rewrite/multiway laws, whole-history constraints, and resource
laws. Exact uniqueness and exact operational-equivalence theorems remain live.

### N2 — wall independence

The stochastic family defeats a convex structural selector. The unitary
partial-swap family independently defeats the claim that reversibility or
extremality alone repairs it. The deterministic control separately shows that
actuality need not be a universal additional atom.

### N3 — hidden-wall scan

`Exact`, `minimal`, `causal`, `covariant`, `reversible`, `compute`,
`equivalent`, and `physical` require mathematical definitions. No such word is
counted as filling a completeness-contract field by itself.

### N4 — residual matching

The exact-law identity fixes predictions. A schedule-equivalence theorem fixes
only schedule presentation. A record-preservation theorem fixes only record
lineage. A probability representation theorem fixes weights only under its
stated premises. The probe does not substitute one for another.

### N5 — rhetoric audit

The conclusion is `these displayed conditions do not select`, not `a law
cannot be derived`. The finite two-qubit interaction is an exact separation,
not a model of the complete universe.

### N6 — partial-closure paths

Every structural condition remains usable as a theorem hypothesis or a field
of a complete law. The result removes only the inference that their conjunction
automatically fixes the law's numerical value.

### N7 — steelman

The strongest counterposition is an exact finite principle whose uniqueness
proof fixes carrier, coefficients, histories, records, and observables. Such a
result would derive the referent and could reduce the constitutional update to
zero. No tested candidate currently supplies that theorem, but this probe does
not close the route.

### N8 — cross-cycle echo

Earlier work repeatedly promoted structural classifications into physical
selection. The paired complete sampled laws, QCA classification audit, cubic
covariance tournament, and this independent reversible family all reproduce
the same correction: classification is not selection.

## Verification

```bash
python3 scripts/qualitative_substrate_exact_law_selection_probe_2026_07_14.py
python3 -m py_compile scripts/qualitative_substrate_exact_law_selection_probe_2026_07_14.py
python3 scripts/vocab_lint.py docs/work_history/repo/review_feedback/QUALITATIVE_SUBSTRATE_EXACT_LAW_SELECTION_NOTE_2026-07-14.md
git diff --check
```
