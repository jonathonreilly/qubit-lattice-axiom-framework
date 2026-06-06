# Record Production Kernel Boundary

**Date:** 2026-06-06
**Claim type:** no-go / exact-support boundary
**Status:** branch-local source note awaiting independent audit handling.
**Primary runner:**
[`scripts/frontier_record_production_kernel_boundary_2026_06_06.py`](../scripts/frontier_record_production_kernel_boundary_2026_06_06.py)
with cached output
[`logs/runner-cache/frontier_record_production_kernel_boundary_2026_06_06.txt`](../logs/runner-cache/frontier_record_production_kernel_boundary_2026_06_06.txt).

## Result

The finite post-record append/count layer consumes realized atoms. It does not
produce the next atom, assign probabilities, set transition rates, prove
frequency convergence, or select a dial attractor.

Formally, once a finite alphabet `O` is supplied, post-record dynamics gives:

```text
R_o(w) = w o
count(w o) = count(w) + e_o
```

for a supplied realized atom `o`. A production kernel is additional data:

```text
K(o | w, state, t, ...)
```

or, in a quantum interface, an instrument/selection rule that supplies
predictive weights and a realized outcome token. The append grammar has no slot
that determines `K`.

## Exact Boundary

The same finite post-record alphabet and append/count grammar admit many
distinct producers:

- fair IID;
- dimension-biased IID;
- reverse-biased IID;
- history-dependent Markov persistence;
- a supplied scripted producer for any named finite target word.

All feed the same post-record update once atoms are realized. They differ in
likelihoods, expected next counts, transition structure, and stationary/stable
priors. Therefore finite post-record dynamics underdetermines the production
kernel.

This is not a defect in the Record axiom. It is the typed interface:

```text
pre-record state / production kernel
  -> realized atom stream
  -> post-record append/count dynamics
```

The exact post-record layer is a consumer of produced atoms, not a producer of
atoms.

## Implications For Dynamics

1. **Record production remains a separate gate.** A physical Hamiltonian,
   instrument, stochastic kernel, Markov generator, decoherence model, or
   source/action law must be supplied or derived elsewhere.
2. **Born/frequency claims remain separate.** Counts and empirical frequencies
   are exact after a finite history is realized, but a law for future outcomes
   requires a production kernel and a probability/frequency bridge.
3. **Stable dial language is allowed, not forced.** A dial point can be stable
   under a named generator or entropy functional. The finite append grammar
   does not choose that generator.
4. **Audit lanes get a clean gate.** Rows that only consume realized record
   atoms can cite append/count support. Rows that predict atoms, rates, or
   stable distributions must expose the producer.

## Why This Builds On The Semigroup Boundary

[`RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md`](RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md)
showed that finite post-record algebra has only discrete reversible
automorphisms and zero derivations, while append/count updates are irreversible
information accumulation.

This note adds the producer boundary: even after that information-dynamics
surface is exact, the next-token law is not determined. The framework can now
say precisely where dynamics work lives:

```text
storage/update layer: exact append/count grammar
producer layer: open unless a kernel/instrument/generator is supplied
```

## Proof Sketch

Let the binary record alphabet be `O={0,1}` and fix a finite target word

```text
w = 1 0 1 1 0 1.
```

The post-record append/count layer records the same word and count vector no
matter how the atoms were produced:

```text
count(w) = (2,4).
```

Now compare five valid producers on the same alphabet:

- `P(1)=1/2`;
- `P(1)=2/3`;
- `P(1)=1/3`;
- a history-dependent persistence kernel;
- a scripted prefix kernel that writes `w` with probability one.

Each kernel is normalized and nonnegative at every prefix. Each assigns positive
likelihood to `w`; the scripted producer assigns likelihood one. The
likelihoods differ, and the expected next counts differ. Yet the realized
post-record update for a supplied next atom remains the same integral update:

```text
c -> c + e_0
or
c -> c + e_1.
```

Therefore the finite realized history and append/count grammar do not identify
a unique production law.

## Boundaries

- Does not derive record-production dynamics.
- Does not derive Born probabilities, IID trials, convergence, transition
  rates, or a clock metric.
- Does not derive a Markov generator or physical stochastic process.
- Does not derive measurement/decoherence dynamics.
- Does not select or force a Koide/generation dial location.
- Does not update repo-wide authority surfaces.

## Runner Summary

The runner verifies:

- suffix append and count projection remain exact and kernel-agnostic after
  atoms are supplied;
- five distinct kernels are valid on the same finite alphabet;
- the same finite word has positive likelihood under all five and likelihood
  one under a supplied scripted producer;
- different kernels give different likelihoods and expected next counts;
- realized count updates are integral, while expected next counts are ensemble
  objects;
- equal-letter, dimension-weighted, and reverse-weighted stable priors are all
  compatible with the same append/count grammar when supplied by different
  kernels.

Expected scorecard:

```text
PASS=29 FAIL=0
```
