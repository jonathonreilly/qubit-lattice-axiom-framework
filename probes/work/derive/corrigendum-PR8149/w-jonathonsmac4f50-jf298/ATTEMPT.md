# corrigendum-PR8149: derivation attempt 1 of 2

Worker `w-jonathonsmac4f50-jf298` (claude-opus-5), unit `J-derive-corrigendum-PR8149-a1`.

**Provenance, stated because it bears on independence.** The other attempt, `a2`
(`w-jonathonsmac4f50-j90fb`), is by the same model family, machine and running worker. Its
corrected `U2′`/`U4′`, its verdict table for (b) and its line list for (c) look complete and I do
not re-derive or contest them. I take the item it files under "what remains open":

> "**The number of centre-first star environments that agree.** At the level of value multisets,
> 24880 ordered matches of two factor-triples give a constant product at `(3,1,2)` (an exploratory
> count, not in `check.py`, and not a count of realizable environments). The 216 equivariant ones
> are exhibited."

## 1. The statements attempted

The star is the centre `0` with its six neighbours; centre first, so every leaf has `I = {centre}`
and `E =` its outside neighbours, and `U2′(c)` says sequential equals joint iff
`Φ_c(a) = Π_{leaves}(K H_x)(a)` is constant in `a`.

> **(i) The geometry.** The star has **18** outside sites, not 30: each leaf has five, but the
> **twelve corner sites are shared by exactly two leaves each**. So the environment space is
> `6¹⁸ = 101 559 956 668 416`, and the six leaf factors are **coupled**. Any count that treats the
> six leaves as independent — a factor-by-factor or pairing count over 30 free values — counts
> configurations that do not exist.
>
> **(ii) The mechanism.** If a cubic symmetry `M` acts on the six values as a single **6-cycle**
> and the environment is `M`-equivariant, then `Φ_c(Ma) = Φ_c(a)`, and a 6-cycle is transitive, so
> `Φ_c` is constant — **for every rule `(p,q,r)`**. This is why `a2`'s family agrees at every
> non-constant rule.
>
> **(iii) The count.** Exactly **8** of the 48 cubic symmetries act on the values as a 6-cycle;
> they generate exactly **4** distinct cyclic subgroups; each has **three orbits of six** on the 18
> outside sites, hence exactly `6³ = 216` equivariant environments. That is `a2`'s 216, identified.
>
> **(iv) The union.** The four families overlap in 8 environments apiece; their union is
> **exactly 840** distinct agreeing environments — `216 + 3 × 208`, a factor `3.89` more than the
> exhibited 216.
>
> **(v) No smaller cancellation at `(3,1,2)`.** Among the 252 possible leaf value-multisets there
> are 234 distinct factors up to scale; **none is constant** and **no two are inverse**. So no
> single leaf and no pair of leaves can produce agreement: every agreeing environment at `(3,1,2)`
> is an irreducible cancellation among at least three leaves. At `(4,1,2)`, where `pq = r²`, there
> are 146 distinct factors, none constant but **eight with inverse partners** — pairwise
> cancellation becomes available. The structure is rule-dependent.

## 2. Steps

**S1 (PROVED; CHECKED `P1`). The geometry.** Computed from the stencil: six leaves, five outside
neighbours each, 18 distinct outside sites, twelve of them in exactly two leaves' lists.

**S2 (PROVED; CHECKED `P2`, `P4`). The symmetry argument.** For `M`-equivariant `env`,
`H_{Mx}(Ms) = H_x(s)` and `K(Ma, Ms) = K(a,s)`, so `(K H_{Mx})(Ma) = (K H_x)(a)`; the product over
leaves is over an `M`-orbit of leaves, so `Φ_c(Ma) = Φ_c(a)`. If `M`'s value action is a 6-cycle
this forces `Φ_c` constant. `P4` verifies it exactly in 160 sampled environments at `(3,1,2)` and
20 each at `(4,1,2)` and `(7,2,3)` — the rule never enters the argument, and the checks confirm it.

**S3 (PROVED; CHECKED `P2`, `P3`). The four subgroups.** Enumerating the 48 signed permutation
matrices: 8 have a 6-cycle value action, generating 4 cyclic subgroups of order 6. Each acts on
the 18 outside sites with orbit profile `[6,6,6]`, so each equivariant family is `6³ = 216`.

**S4 (CHECKED `P4`). The union is 840.** Enumerated exactly as sets of `18`-tuples.

**S5 (CHECKED `P5`). The leaf factors.** Exact rational enumeration over all
`C(10,5) = 252` multisets at two rules, with the counts above.

## 3. Where the route stops

- **The full count is not settled.** `6¹⁸ ≈ 1.0 × 10¹⁴` environments, and by S1 the factors are
  coupled, so the natural meet-in-the-middle over leaf multisets is invalid — this attempt's first
  contribution is to show that the obvious approach counts non-existent configurations. 840 is a
  **lower bound**, and the only mechanism I can prove is the symmetric one.
- **Whether 840 is everything** is open. A non-symmetric agreeing environment would have to be an
  irreducible three-or-more-leaf cancellation (S5), which is exactly what a search would have to
  find; I did not search the `10¹⁴`.
- **`a2`'s exploratory 24880** is a multiset-level number and, by S1, is not a count of
  environments. This attempt neither confirms nor uses it.
- Nothing here revisits `a2`'s `U2′`, `U4′`, its (b) table or its (c) line list.

## 4. What would finish it

1. A search for agreeing environments outside the 840 — best posed as: does `Φ_c` constant force
   `M`-equivariance for some 6-cycle `M`? The `(4,1,2)` pairwise family shows the answer is rule
   dependent, so the question is about `(3,1,2)` specifically.
2. If the packet wants a number in the note, **840** is the defensible one with today's argument,
   with "at least" in front of it.
3. The rule-dependence in S5 — inverse partners appearing exactly at `pq = r²` — looks like a
   statement about the kernel's spectrum and is worth its own line; `a2`'s `(f3)` witness lives at
   that same rule.

## 5. Running it

```
python3 probes/work/derive/corrigendum-PR8149/w-jonathonsmac4f50-jf298/check.py
```
from the repository root. Standard library plus `fractions`; about two minutes, most of it in the
exact enumeration of the 252 leaf multisets at two rules.
