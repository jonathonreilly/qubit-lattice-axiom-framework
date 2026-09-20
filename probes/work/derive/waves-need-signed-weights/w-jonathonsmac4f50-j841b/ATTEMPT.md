# waves-need-signed-weights, attempt 3 of 5 — (a) with many levels *and* many components

Worker `w-jonathonsmac4f50-j841b` (`claude-opus-5`), unit `J-derive-waves-need-signed-weights:a3`.

**Provenance.** Three prior attempts exist. Two — `w-jonathonsmac4f50-j62b1` and
`w-jonathonsmac4f50-jafb3` — are by the same model family, machine and running worker as this one.
The third, `w-macbookpro90c72-jf9e6`, is from a different machine and is the only prior here that
might be independent; I have not verified what produced it, and its conclusions are treated as
claims, not as confirmation. I re-run none of their routes.

I chose the target by reading what all three say they did *not* do, and they name the same corner:

- `j62b1` proves the **vector** theorem at **one** level; its §4 item 1 is "the `J`-level vector
  statement, by the block companion matrix".
- `jafb3` proves the **scalar** theorem at **`J`** levels; its §3 item 3 is "the vector version of
  (a)".
- `w-macbookpro90c72-jf9e6` says "(a) is closed as stated" but lists "multi-component rules in
  `d ≥ 2` are not classified" as its item 2.

So the two halves are each done separately and the intersection — **nonnegative matrix weights
over finitely many levels** — is done by none of them. That is this attempt.

## 1. The statement attempted

`θ_{t+1}(x) = Σ_{j<J} Σ_y w_j(y) θ_{t−j}(x − y)` on `Z^d`, with `θ_t(x) ∈ R^M`, each `w_j(y)` an
`M×M` matrix that is **entrywise nonnegative** and finitely supported, and **gain one**:
`A = Σ_{j,y} w_j(y)` is row-stochastic. `W_j(k) = Σ_y w_j(y)e^{−ik·y}`, and the branches are the
`MJ` eigenvalues of the block companion matrix `C(k)` (first block row `(W_0,…,W_{J−1})`,
identities on the subdiagonal).

> **Theorem.** Every branch satisfies `|λ(k)| ≤ 1`. A branch has `|λ(k)| = 1` on a set with
> nonempty interior **only if** every entry of every `w_j` is carried by a single displacement and
> the resulting phases form a diagonal conjugation times a global phase — that is, only if the
> rule is **rigid transport**. In particular no such rule disperses, in any dimension and at any
> number of levels.

Two things the vector case adds over both prior halves, both with exact witnesses:

- **Single-site entries are necessary but not sufficient.** A two-component rule whose every entry
  is a single displacement, but whose first row *mixes* the two components, has every branch
  strictly inside the circle. In the scalar case condition (i) is almost the whole story; in the
  vector case the second condition is about mixing, not about displacements.
- **The transport velocity is rational, not integral.** `θ_{t+1} = θ_{t−1}(x − 1)` has dispersion
  polynomial `λ² − e^{−ik}` and branches `±e^{−ik/2}`: unimodular at every `k`, at velocity `1/2`.
  Any statement of the exception that puts the velocity in `Z^d` is wrong; `j62b1`'s Theorem V
  says `Q^d`, and this is a witness it does not give.

## 2. The steps

1. **PROVED (`W1`, checked).** The branches are `C(k)`'s eigenvalues; verified that the
   companion's characteristic polynomial is the dispersion polynomial on a two-level example.
2. **PROVED (`W2`, checked).** `|W_j(k)_{mn}| ≤ (A_j)_{mn}` entrywise, **because the weights are
   nonnegative** — this triangle inequality is the only place the sign hypothesis is used. Hence
   `|C(k)| ≤ C(0)` entrywise, `C(0) ≥ 0`, and gain one gives `ρ(C(0)) = 1` (checked exactly for a
   one- and a two-component rule). Perron–Frobenius comparison then gives `|λ(k)| ≤ 1` for every
   branch.
3. **ASSUMED (`W3`) — Wielandt's lemma**, stated at the scope used: if `|B| ≤ C` entrywise with
   `C` nonnegative irreducible, then `ρ(B) ≤ ρ(C)`, with equality only if
   `B = e^{iφ} D C D^{−1}` for a unimodular diagonal `D`. **This is the one imported theorem and
   it is not re-proved here.** Everything in §1 after `|λ| ≤ 1` rests on it.
4. **PROVED (given 3).** Equality forces (i) `|W_j(k)_{mn}| = (A_j)_{mn}` for every entry, which
   for nonnegative weights forces single-displacement support per entry; and (ii) the phase
   relation. Condition (i) alone confines `k` to a proper closed subgroup — empty interior —
   unless every entry is already single-site.
5. **CHECKED (`W4`) — the exception is real, and it is real in the vector case.** Three exact
   symbolic verifications, in `k`, not sampled: `θ_{t+1} = θ_{t−1}(x−1)` has `P = λ² − e^{−ik}`
   with roots `±e^{−ik/2}`; the chain `w_0 = ½δ_1, w_1 = ½δ_2` has the exact factorization
   `(λ − e^{−ik})(λ + e^{−ik}/2)`, one branch of modulus 1 and one of modulus exactly `1/2`; and
   the **two-component, two-level** rule `w_1(+1) = [[0,1],[0,0]]`, `w_1(−1) = [[0,0],[1,0]]` has
   dispersion polynomial **`λ⁴ − 1` identically in `k`** — four flat bands of modulus exactly one.
6. **CHECKED (`W5`) — mixing rules are strictly inside.** Tested exactly at `k = π, π/2, 2π/3` by
   a resultant certificate: if `|z| = 1` and `P(z) = 0` then the reversed-conjugated polynomial
   `P*` also vanishes at `z`, so a **nonzero resultant of `P` and `P*` certifies no root on the
   unit circle**. (Roots at the origin are stripped first, since they are not on the circle and
   make the reversal degenerate.) Three examples: single-site entries with the wrong displacement
   relation; the diffusive rule `w_0(0) = w_0(1) = ½`; and the two-component mixing rule of §1.
7. **CHECKED (`W6`).** `λ = ±e^{−ik/2}` has phase velocity `−1/2`.

## 3. Where this stops

- **Wielandt is assumed, not proved.** It is the whole engine of the equality case. The `|λ| ≤ 1`
  half is self-contained; the classification half is not. A referee should treat step 4 as
  conditional.
- **Irreducibility is assumed**, as in `j62b1`. For reducible `A` the statement applies class by
  class and the bookkeeping is unwritten — the same gap that attempt lists.
- **The converse is not proved.** I show rigid transport is *forced*, and exhibit rigid-transport
  rules that are unimodular, but I do not prove that *every* rule satisfying (i) and (ii) is
  unimodular on an open set. §1's theorem is stated as a one-way implication for that reason.
- **The examples are `d = 1`.** The argument never uses `d`, but every exact witness is
  one-dimensional, so the `d ≥ 2` multi-component classification that the third attempt lists as
  open is still open.
- **Nothing here touches (b) or (c).** Those are the other attempts' territory and I did not
  re-check their results — in particular I have not verified the third attempt's `J = 3` lossless
  region or cone radii, which are the strongest unrefereed numbers in this problem.

## 4. What would finish it

1. Re-prove Wielandt's equality case at this scope, or replace it with a direct argument on the
   companion matrix. Until then the classification half of (a) is conditional in all three
   multi-level or multi-component treatments, since `jafb3`'s and `j62b1`'s routes lean on the
   same equality case in scalar and one-level form.
2. The converse: show (i) + (ii) ⟹ unimodular on an open set, which would make the exception an
   exact characterization rather than a necessary condition.
3. The `d ≥ 2` multi-component classification, with an exact witness in two dimensions.
4. Independent re-derivation by another model family: two of the three priors and this attempt are
   the same family, so the only possibly-independent input here is one attempt from one other
   machine.

## 5. Running it

```
python3 probes/work/derive/waves-need-signed-weights/w-jonathonsmac4f50-j841b/check.py
```

Standard library plus `sympy`; 20 checks. Symbolic identities are verified in `k`; the
"no root on the circle" claims are exact resultant certificates at `k` a rational multiple of `π`,
where the coefficients lie in a cyclotomic field. No floating point anywhere.
