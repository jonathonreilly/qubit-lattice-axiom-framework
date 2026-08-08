# The No-Diagonal Axiom + Staggered-Dirac Hopping Make the Generation Coupling K-Real to All Orders: the 2-Sector Partition is Dynamically Einselected and r=0 is Structurally Excluded — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (derives K-reality / the 2-sector partition from the axioms; the value r=1/2 vs r=1 left open)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/no_diagonal_staggered_dirac_einselects_2sector_runner.py`](../scripts/no_diagonal_staggered_dirac_einselects_2sector_runner.py)
**Cached output:** [`logs/runner-cache/no_diagonal_staggered_dirac_einselects_2sector_runner.txt`](../logs/runner-cache/no_diagonal_staggered_dirac_einselects_2sector_runner.txt)

## Audit context

The retained einselection sieve
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
(`bounded_theorem`) shows: a `C3`-invariant **K-real** (time-reversal-real) generation coupling
lies in `span_R{I, C+C^2}` and resolves only the two real-irreducible blocks (singlet ⊕ doublet)
— the **2-sector partition**; resolving `omega` from `omega^2` (the **3-mode / r=0** partition)
*strictly requires* the **K-odd** observable `i(C − C^2)`. The sieve **posits** K-reality (its
GAP A: "K-reality is posited, not derived"). This note **derives** it from the axioms — so the
2-sector partition is dynamically einselected, not assumed.

The emergent generation coupling is the second-order (and higher) effective operator built from
the native single-flip hopping; it is the `C3`-coupling the predictability sieve compares against
the sector mass. Generations are the `hw=1` sector
([`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
`retained`). The hopping is the retained staggered-Dirac form (off-diagonal `−0.5j`, real diagonal
mass) of
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md).

## Safe statement

**Theorem.** Let the emergent generation coupling be the effective operator on `hw=1` built from
the native single-flip hopping through the `hw=0`/`hw=2` virtual sectors, with the staggered-Dirac
form: off-diagonal hopping **purely imaginary** `V = iA` (`A` real, the `−0.5j` hops), diagonal
(mass) real. Then:

1. **Odd perturbative orders vanish.** The **no-diagonal** axiom makes the hop a single bit-flip,
   so returning to `hw=1` requires an **even** number of hops (Hamming parity). Every odd order
   (3rd, 5th, …) vanishes identically on `hw=1`.

2. **Even orders are real.** An even number of purely-imaginary hops has amplitude
   `i^{even} · (real) = real`. So every non-vanishing (even) order of the effective coupling is a
   **real** matrix (verified 2nd and 4th order; robust across uniform and staggered sign
   patterns).

3. **Hence K-real to all orders.** The `K`-odd generator `i(C − C^2)` is intrinsically imaginary,
   so a real coupling has **zero** overlap with it at every order. The emergent generation
   coupling is therefore **K-real to all orders** — it lies in the sieve's cone
   `span_R{I, C+C^2}`.

4. **The 2-sector partition is einselected; r=0 is structurally excluded.** `eig(C+C^2) =
   {2, −1, −1}` (singlet isolated, doublet degenerate), so the K-real coupling resolves only the
   2-sector (singlet ⊕ doublet) partition. The K-odd coupling needed for the 3-mode / `r=0`
   partition is **structurally forbidden**: it would require either a **diagonal** hop (odd-order
   return, forbidden by the no-diagonal axiom) or a **non-native mixed** real+imaginary hop (a
   mixed `V = (1+i)A` *does* produce a K-odd part — verified — but the framework's hop is purely
   imaginary).

So the no-diagonal axiom and the staggered-Dirac form together **discharge the sieve's posited
K-reality from the axioms**, dynamically einselecting the 2-sector partition and excluding the
`r=0` (democratic, `Q=1/3`) setting.

## The genuine open piece (and what this opens)

This derives the **partition** half (2-sector) of the gate; it does **not** decide the **value**
within it. The dial is narrowed from `{r=0, r=1/2, r=1}` to the 2-sector `{r=1/2, r=1}`. The
remaining `r=1/2`-vs-`r=1` choice is the separate **block-count-vs-dimension measure** on
`R[Z_3] = R ⊕ C` (block-count → `r=1/2` → `Q=2/3`; dimension/Plancherel → `r=1` → `Q=1`) — the
standing measure question, **not decided here**. So this note narrows the dial without forcing a
value; it opens the measure question as the single remaining input for the charged-lepton value.

## Boundary (honest)

- **Partition, not value.** It derives K-reality (the 2-sector partition) and excludes `r=0`; it
  does **not** force `r=1/2` (or `r=1`). No value is reverse-engineered.
- **Load-bearing identification (flagged).** It treats the emergent `C3` coupling (the effective
  mass-operator `C3` part) as the operator the predictability sieve compares against the sector
  mass — i.e. the pointer-selecting coupling. This is the sieve's own setup (pointer = eigenbasis
  of the dominant of `{coupling, mass}`), flagged here for the auditor.
- **Purity is load-bearing.** K-reality requires the hop to be purely imaginary (or purely real),
  not mixed. The framework's staggered-Dirac hop is purely imaginary off-diagonal with a real
  diagonal mass; a non-native mixed hop would reintroduce a K-odd part.
- **Symbol note.** The sieve's "`δ=0`" (the Brannen phase / time-reversal-reality) is the
  *predicate* derived here; it is distinct from the energy-asymmetry `δ` of the companion
  amplitude notes.

## Forbidden imports check

No new axiom/import. The single-flip hopping + Hamming-graded diagonal + purely-imaginary
staggered-Dirac form are the retained native dynamics; the order-parity (odd orders vanish) and
the realness of even orders are exact arithmetic. The sieve (`retained_bounded`) supplies the
K-real ⇒ 2-sector reduction. No value `r` is asserted.

## Runner check breakdown

Class A: (1) odd orders (3,5) vanish on `hw=1` for uniform and staggered sign patterns; (2) even
orders (2,4) are real and nonzero; (3) the 2nd-order coupling has zero overlap with the K-odd
generator `i(C−C^2)`; (4) a non-native mixed hop introduces a K-odd part (purity is load-bearing);
(5) `eig(C+C^2) = {−1,−1,2}` (2-sector, singlet+doublet). Expected `runner_check_breakdown = {A:
N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact: the no-diagonal axiom forces returns to `hw=1` to be even-order
(odd orders vanish), and even-order products of the purely-imaginary staggered-Dirac hop are real,
so the emergent generation coupling is K-real to all orders (zero overlap with `i(C−C^2)`),
robust across sign patterns; a non-native mixed hop is what would introduce a K-odd part. By the
retained sieve, a K-real coupling resolves only the 2-sector (singlet+doublet) partition, so the
2-sector partition is dynamically einselected and the `r=0` (3-mode) setting is structurally
excluded. The result discharges the sieve's posited K-reality (its GAP A) from the axioms and
narrows the dial to `{r=1/2, r=1}`; it does **not** decide the value within (the block-count vs
dimension measure), and forces no `r`. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/no_diagonal_staggered_dirac_einselects_2sector_runner.py
```
