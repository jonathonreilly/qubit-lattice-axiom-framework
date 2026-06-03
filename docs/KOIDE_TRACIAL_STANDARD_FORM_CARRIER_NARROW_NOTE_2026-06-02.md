# Koide r=1/2 from a tracial-standard-form carrier: does GNS rank the (1,N-1) partition?

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** conditional carrier lemma and Tier-A candidate source, **not**
a Tier-A admission and not a framework-axiom revision. This note does **not**
derive `r=1/2` from the current framework baseline plus retained inventory; it
derives the partition-ranking result **given** the proposed tracial-standard-form
carrier and still leaves a scoring residual. Any future Tier-A admission or
axiom-surface change requires explicit user approval and registry/source
process outside this note. Status authority = independent audit lane only; this
note does not set or predict an audit outcome.
**Primary runner:** [`scripts/koide_tracial_standard_form_carrier_2026_06_02.py`](../scripts/koide_tracial_standard_form_carrier_2026_06_02.py) (SCORECARD PASS=8).

## What this adds over the existing unaudited note

The on-main note
`FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md`
(claim_id `flavor_missing_axiom_carrier_measure_note_2026-05-30`, **unaudited**) states
the three-way fork and the HS-norm relation `r = 1/(N-1)`, but treats the fork as
**symmetric** -- "the same operator gives three different `r` under three partitions ... rep
theory ranks none." This note **breaks that symmetry rigorously**: it shows the tracial
standard form supplies a **distinguished cyclic vector** `Omega = e` that **ranks the (1,N-1)
group-element partition above the idempotent partition** -- and then it states, honestly,
the residual that survives even so. The fork is no longer "rep theory ranks none"; it is
"the cyclic vector ranks the (1,N-1) split first, and one scoring choice remains."

## Candidate carrier input (not admitted)

> **Candidate carrier input.** The on-site generation carrier is the group algebra `R[Z_3]`
> in its **tracial standard form**: `R[Z_3]` acting (by left multiplication) on its GNS
> Hilbert space `L^2(R[Z_3], tau)`, where `tau` is the normalized group trace
> (`tau(g^k) = delta_{k,0}`) and `<x, y> = tau(x* y)`. The distinguished cyclic and separating
> vector is the unit `Omega = e`; the canonical orthonormal basis is the group-element ONB
> `{e, g, g^2}`. The mass operator is the `C_3`-unbiased
> `H = a*e + b*(g + g^2) = a*I + b*(J - I)`. The identity/non-identity channel split is the
> carrier's canonical **cyclic-vector split**, and `r = |b|^2/a^2 = 1/(N-1) = 1/2` (at
> `N = 3`) is **inherited from the carrier**, not selected from a fixed `H`.

This paragraph is the conditional input being analyzed, not an accepted axiom.
It must not be cited downstream as admitted unless the user explicitly approves
the Tier-A/axiom-surface change and the registry/source surfaces are updated.

The retained upstream surface supplies the algebra this builds on: the `C_3` character-norm
recasting and the closed-form Brannen/Rivero ratio
([`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
`retained`;
[`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md`](KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md),
`retained_bounded`) give `Q = 1/3 + (2/3)*r`, so `Q = 2/3 <=> r = 1/2`. This note does **not**
re-derive that algebra; it addresses the **selection of the partition** that fixes `r`.

Load-bearing markdown-linked authorities: the two retained Koide ratio/block
weight anchors and the retained-bounded chirality no-go named below. The
unaudited carrier-measure note is context only and intentionally not a
citation-graph dependency.

## The crux: does the standard form canonically single out the (1,N-1) partition?

### What the GNS standard form genuinely forces

The tracial GNS triple `(L^2(R[Z_3], tau), pi, Omega)` is well-defined and reproduces the state:
`<Omega, pi(g^k) Omega> = tau(g^k)`. The unit `Omega = e` is **cyclic** (`{pi(g^k)Omega}` spans) and
**separating**, and `{e, g, g^2}` is the GNS ONB. Crucially, `Omega = e` is **itself one of the
ONB vectors**, and the other two are its group orbit `g.Omega, g^2.Omega`.

This makes one orthogonal decomposition **a function of `(Omega, <.,.>)` alone**, with **no
diagonalization**:

```
  L^2 = C.Omega  (+)  Omega^perp  =  span{e}  (+)  span{g, g^2}      -- dims (1, N-1) = (1, 2).
```

`C.Omega` is the **vacuum line** of the cyclic/separating vector; `Omega^perp` is its orthocomplement.
This is exactly the **identity vs non-identity** group-element partition. Measuring `H`'s
energy in this split is the GNS metric on the **operator's coefficient vector** `(a, b, b)`:
identity-channel energy `||a*e||^2 = a^2*1`, non-identity-channel energy `||b(g+g^2)||^2 = b^2*2`.
Equal energy across the two channels (`a^2*1 = b^2*2`, i.e. `3a^2 = 6b^2`) gives **`r = 1/2`**.

### Why this **ranks** the (1,N-1) split above the idempotent split

The idempotent / Fourier split (`r ~ 0.0147`) is **also** a canonical decomposition of
`R[Z_3]` -- the central-idempotent / spectral split of the canonical generator `S`. But its
distinguished singlet line is the **democratic element**
`p_0 = (e + g + g^2)/3 -> (1,1,1)/sqrt(3)`, which is **not** `Omega = e` (overlap `<Omega, (1,1,1)/sqrt(3)> =
1/sqrt(3)`, strictly between 0 and 1). So the idempotent singlet is **invisible from `(Omega, <.,.>)`
alone**: recovering it requires **also** importing the Fourier/spectral resolution of `S`.
The cyclic vector therefore acts as a **tie-breaker** the bare fork lacks:

- the **(1,N-1) group-element split** is built from `(Omega, <.,.>)` only (a fixed rank-1
  projection `P_id = |e><e|`);
- the **idempotent split** needs the extra spectral structure and its distinguished line is
  misaligned with `Omega`.

**Group-basis/Hopf automorphism invariance** confirms the (1,N-1) split is basis-independent up to the
carrier symmetry actually checked here: the `Z_3` group automorphisms `Aut(Z_3)` (`g -> g^u`,
`u in {1,2}`) fix `e` (the **unique order-1 group element**) and permute `{g, g^2}` among themselves.
So `{e}` is a singleton orbit and the (1,2) split is canonical under the checked group-basis/Hopf
symmetry. This is intentionally narrower than a classification of every trace-preserving `*`-automorphism
of the real algebra. Symmetry alone does **not** separate the two splits -- the democratic line is
Aut-invariant too -- which is exactly why the **cyclic vector** is the load-bearing tie-breaker, not the
symmetry.

### The honest residual (what the standard form does **not** force)

Granting that `(Omega, <.,.>)` distinguishes the **(1,N-1) split**, one commitment survives:
the **scoring rule on that split**. Two `C_3`- and `(g<->g^2)`-invariant rules live in the same
GNS metric:

| scoring on the (1,N-1) split | condition | `r` | `Q` |
|---|---|---:|---:|
| equal energy **per channel** (2 channels: `{e}`-line, `{g,g^2}`-plane) | `a^2*1 = b^2*2` | **1/2** | **2/3** |
| equal energy **per basis direction** (3 directions; Plancherel/dimension) | `a^2 = b^2` | 1 | 1 |

The first counts **isotypic channels** (treat each subspace as one unit); the second is
genuine per-degree-of-freedom equipartition over `{e, g, g^2}` (which gives `r=1`, **not**
`r=1/2`). The carrier makes the two channels `{e-line}, {g,g^2-plane}` canonical objects, and
equal-weighting **them** is the `(1, N-1)` rule -- but the standard form does **not by itself
adjudicate channel-counting vs direction-counting**. That choice is the residual the carrier
carries. (The idempotent equal-**power** rule on the spectrum, giving `r = 17/2 - 6*sqrt(2) ~
0.0147`, is the third option; it is now demoted by the cyclic vector but not logically
eliminated as an algebra decomposition.)

### Verdict on the crux

**The tracial standard form substantially relocates this carrier-selection problem; it does not close it.** The fork is
no longer the symmetric "rep theory ranks none" of the unaudited note: the cyclic vector
`Omega = e` **ranks the (1,N-1) group-element split first** (the idempotent split's distinguished
line is misaligned with `Omega` and needs extra spectral structure). The live residual shrinks
from "three coequal partitions" to "the channel-count (`->1/2`) vs basis-direction-count
(`->1`, Plancherel) weighting on the now-distinguished (1,N-1) split." `r = 1/2` is forced
**given** the candidate carrier input **plus** the channel-counting scoring on the cyclic-vector
split; the scoring posit is the one thing not delivered by GNS uniqueness alone.

## Falsifiable content (kept)

1. **`r = 1/(N-1)` ties `r = 1/2` to the derived generation count.** With a `Z_N` carrier,
   `||I_N||^2 = N`, `||J_N - I_N||^2 = N(N-1)`, so equal channel energy gives `r = 1/(N-1)`:
   `N=2 -> 1`, `N=3 -> 1/2` (`Q = 2/3`), `N=4 -> 1/3`, `N=6 -> 1/5`. `r=1/2` is **forced by
   `n_gen=3`**, not tuned.
2. **Kahler/Dirac corroborator -> Majorana neutrinos off `2/3`.** A structurally distinct
   computation (rank-weighted phase-averaged moments `1*(a^2+4b^2) = 2*(a^2+b^2) -> r=1/2`)
   reaches the same point and predicts `Q = 2/3 <=> complex b <=> Dirac/U(1)-gauged sector`; so
   **Majorana neutrinos (real `b`, frozen Brannen phase) must depart from `2/3`** -- a
   structural prediction, and it explains the derived `delta`-independence as the gauge direction
   of the quotient.
3. **Coheres with the signed/Hermitian (Dirac `H = iD`) readout.** The `tau`/HS form is the
   invariant of the comparator-compatible signed-eigenvalue (Brannen) readout class, not the
   singular-value/Yukawa class. (Relation to readout class noted qualitatively only;
   the signed-vs-singular-readout note is `audited_failed` and is **not** load-bearing here.)

## Decoupling from the chirality no-go

`r = 1/2` is an **interior point of the commuting circulant family**: `[H, S] = 0` at
`r = 1/2`, and `H` does **not** anticommute with the `C_3` chiral grading
`Gamma_chi = (2/3)J - I`. So this candidate carrier input introduces **no** chiral/anticommuting operator
and therefore does **not** trip the generation-chirality obstruction
`comm(S) cap anticomm(Gamma_chi) = {0}`
([`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
`retained_bounded`). **The VALUE lane is clean and structurally decoupled from the chirality
gate** -- a separate, more tractable question.

## What it costs / does not break

As a candidate input, the tracial-standard-form carrier is compatible with the retained derivations it touches (3 generations, `C_3` regular rep,
signature `(3,1)`/emergent time, the Koide identity). The price is the right kind of debt:
**re-deriving the qubit / `Cl(3)` structure as an operator *on* this carrier**, which pushes
the question to foundations rather than papering over it with a bolted-on selection principle.
The residual cost is the **channel-counting scoring** on the (1,N-1) split (now the *only*
undetermined input, vs the unaudited note's full three-way fork).

## Honest bottom line

> The tracial standard form makes the **(1,N-1) identity/non-identity partition** a carrier
> property -- the cyclic vector `Omega = e` distinguishes it from the idempotent partition, which
> the bare fork could not rank. `r = 1/(N-1) = 1/2` is then **inherited** rather than freely
> selected, **given** the candidate carrier input **and** the channel-counting scoring on that
> split. What remains undetermined is that one scoring posit (channel-count `-> 1/2` vs
> direction-count `-> 1`). This carrier-selection problem is **substantially relocated and
> narrowed**, not closed. The note is a Tier-A candidate source, **not** an
> admission and not a derivation from the current framework baseline plus retained inventory.

## Tiers verified on `origin/main` (`.rows[claim_id].effective_status`)

| claim_id | effective_status | role here |
|---|---|---|
| `flavor_missing_axiom_carrier_measure_note_2026-05-30` | `unaudited` | the note this strengthens |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | `retained_bounded` | block-weight algebra anchor |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | `retained` | Brannen ratio `Q=1/3+(2/3)r` |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | `retained_bounded` | chirality decoupling |

## 2026-06-03 wording repair

The automorphism paragraph has been narrowed to the `Z_3` group-basis/Hopf automorphisms actually checked
by the runner. It no longer claims a classification of all trace-preserving `*`-automorphisms of `R[Z_N]`.
The missing carrier/scoring bridge remains open.
