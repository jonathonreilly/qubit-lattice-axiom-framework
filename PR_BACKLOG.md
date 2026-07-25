
## Cycle 702 — law pinned by scale and coherence — BACKLOGGED, with a real error

Branch: `physics-loop/law-pinned-by-scale-and-coherence-20260725` (pushed).
Runner 8 PASS / 0 FAIL, cold-run isolated, pin verified. **No PR opened.**

Built in response to owner direction: take Planck as given, adopt no counting
convention, aim at identifying the law. The cluster-cap evaluator returned
`BACKLOG` and found two substantive problems and one mathematical error.

### The mathematical error (verified independently, evaluator correct)

Part I's P1 claimed "the response is long-ranged precisely when `A = 0`",
inferring a global statement from the symbol's value at `k = 0` alone. That does
not follow. The lattice symbol is `A + B·Dhat(k)` with `Dhat ∈ [-12, 0]`, so for
`0 < A/B <= 12` the symbol **vanishes at nonzero `k`** — zero modes exist away
from the origin, and the behaviour is oscillatory rather than exponentially
screened. Checked directly:

```text
A=1,  B=1: symbol range [-11, 1]   zero mode away from k=0: yes
A=6,  B=1: symbol range [-6, 6]    zero mode away from k=0: yes
A=11, B=1: symbol range [-1, 11]   zero mode away from k=0: yes
A=13, B=1: symbol range [1, 13]    no zero mode
```

The Yukawa mass and screening-length reading additionally require a sign
restriction that the note did not state, and absorbing `B` into a source
normalization presumes a source equation the classified operator family does not
supply.

### The load-bearing objection

Part I's selector does not work, and the reason is worth keeping:

> "Zero dimensionless content" means the primitive supplies **no value** of
> `A/B`. It does **not** supply zero preferentially. Choosing zero because it is
> writable without naming a nonzero number is a simplicity or naturalness
> principle absent from the framework. Using the clause as a blocker elsewhere
> but as a selector here is inconsistent.

That is correct. The scale primitive is a ruler, not a selector, and the attempt
to read it as one was the cycle's central move.

### Part II

The antitone/monotone characterisation of the two closures is correct only under
a **revalidation semantics** — that a locked possibility must remain admissible
when the surrounding configuration is deleted or enlarged. Record permanence and
additivity do not impose that; additivity can instead quantify only over
collections already in its domain. So the "equivalences" are not framework
consequences, and under the chosen semantics the constancy result is elementary.
Substantively it sharpens backlogged cycle 700 by one lemma and reaches the same
fork.

### Disposition

Target stopped. This is the third consecutive backlog in this campaign (700,
701 twice, 702), and this one contained a false mathematical claim that the gate
caught. The negative result is recorded in `HANDOFF.md` because it is genuinely
informative for planning; the branch is kept for recovery.
