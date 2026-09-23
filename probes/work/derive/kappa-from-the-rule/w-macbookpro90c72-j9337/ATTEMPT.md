# J:derive:kappa-from-the-rule:a2 — block 50's clock gives no κ with a far field, equal pulls trade κ for the record's energy, and nothing fixes γ

**Provenance.** Worker `w-macbookpro90c72-j9337`, model `claude-opus-5-5`, one session. The claim printed no prior attempts. Definitions come from the notes of four open PRs; every clause is supplied and none is adopted:
- block 53 (PR #8568): `u = log w`; a record enters as a source `log κ`, `u_x − (1/6)Σ_e u_{x+e} = (log κ) n_x`; `κ` is the record's rate over a degree-one covariant mean of its neighbours' rates, and the geometric mean makes the law exact;
- block 50 (PR #8562): the local clock, under which the event of the record at `x` runs at rate `1/π_x`, where `π_x` is the product of its pair weights `cω`;
- block 54 (PR #8570): the pull `−E∇u`;
- block 55 (PR #8571): the weak-field law `u_x − avg = −(γ/6)(e_x − μ)/w̄`, and action equals reaction iff source is proportional to energy.

## 1. Statement

The task asks three things:
- (a) Express block 50's clock as a `κ`: for an isolated record at `c₀ = 6/(p + q + 4r)`, and for a record with one or two record neighbours. Is it below one? Evaluate exactly at `(p, q, r) = (3, 1, 2)`.
- (b) If a record falls like block 54's packets, show that equal and opposite pulls between a record and a packet force `log κ = −γ·E_rec`, and say what replaces `κ` as the free number.
- (c) Say what would fix `γ`.

**Obtained:**
- **(a)** An isolated record has `κ = 1` exactly, so it has no source.
  - With neighbours, `κ` depends on their contents. With one neighbour it is `12/17`, `12/7` or `1` for equal, opposite or orthogonal contents. With two it runs from `1/2` (both equal) to `3` (both opposite).
  - It is below one only next to aligned contents. Its average over the partner's content is `382/357 > 1` uniformly but `352/357 < 1` under the stationary pair law.
  - **Read as block 53's rate field, block 50's clock is exactly `u = −log π`.** Its sources `log κ` sum to zero on every torus and vanish away from records that have neighbours. So it has no far field, and it cannot be the `κ` of block 53.
- **(b)** Equal and opposite pulls require `log κ = −(γ/6)E_rec`, with `γ` block 55's coupling; this is `−γ'E_rec` with `γ' = γ/6` in the task's normalization.
  - `κ` gives way to the record's energy in ambient ticks.
  - A block 54 walker at rest has none, so `κ = 1`, in agreement with (a)'s isolated record.
- **(c)** No present clause fixes `γ`. Every `γ > 0` satisfies blocks 53–55.

## 2. Steps

**Step 1 (CHECKED A.c0, A.neutral).**
- At `(3, 1, 2)`, `c₀ = 1/2`. The pair weights are `c₀p = 3/2`, `c₀q = 1/2` and `c₀r = 1`; `c₀r = 1` because `p + q = 2r` (block 50 T3).
- The mean pair weight over the partner's six contents is `1`.

**Step 2 (PROVED; CHECKED A.isolated, A.one, A.two, A.below). `κ` of the local clock.**
- *Rates.* A site's rate is `w = 1/π`, where `π` is the product of the pair weights of that site. An empty site or an isolated record has `π = 1`, the empty product. (ASSUMED: empty sites tick at the ambient rate 1. Block 50 defines events only for records.)
- *Isolated record.* `w_x = 1` and all six neighbours have `w = 1`, so `κ = 1` for any mean.
- *One neighbour* with pair weight `cω`, where that neighbour has no other pair:
  - arithmetic mean: `κ = (1/(cω)) / ((1/(cω) + 5)/6) = 6/(1 + 5cω)`;
  - geometric mean: `κ = (cω)^{−5/6}`.
- *Two neighbours,* not adjacent to each other: `κ = (1/(c²ω₁ω₂)) / ((1/(cω₁) + 1/(cω₂) + 4)/6)`. The values:

  | Neighbours' contents | `κ` |
  |---|---|
  | equal–equal | 1/2 |
  | equal–opposite | 6/5 |
  | equal–orthogonal | 12/17 |
  | opposite–opposite | 3 |
  | opposite–orthogonal | 12/7 |
  | orthogonal–orthogonal | 1 |
- In both means, `κ < 1` iff `π_x > 1`: the record's own pair weights are favoured.
- At `(3, 1, 2)`, `κ < 1` only next to equal contents, `κ = 1` next to orthogonal ones, and `κ > 1` next to opposite ones.

**Step 3 (CHECKED A.average). Averages depend on the averaging.** With one neighbour:

| Average over the partner's content | Arithmetic `κ` | Mean of `log κ` (geometric) |
|---|---|---|
| Uniform over its six contents | `382/357 > 1` | `+0.040` |
| Stationary pair law (weights `∝ cω`, block 50 T3) | `352/357 < 1` | `−0.036` |

So "is it below one" has no single answer.

**Step 4 (PROVED; CHECKED B.zero_total, B.local). Block 50's clock as a rate field has no far field.**
- Put `w = 1/π` at every site. Then `u = −log π`. Block 53's geometric-mean source is `log κ_x = u_x − (1/6)Σ_e u_{x+e} = −((1 − A)log π)_x`.
- *The total vanishes.* On a torus, `Σ_x ((1 − A)f)_x = 0` for every `f`. So the sources sum to zero.
- *The field is local.* The field is `u = −log π` itself: it vanishes wherever `π = 1`, with no tail. On the infinite lattice the same holds for finite clusters.
- Checked with formal logarithms on 40 random configurations on the `3³` torus.
- *The consequence.* Block 53's `κ` must be a source whose total is `n log κ` for `n` records. Block 50's clock supplies local sources of total zero. So it is not a candidate for block 53's `κ`; its records exert no long-range pull through the rates.

**Step 5 (PROVED; CHECKED C.sum). Equal and opposite pulls.**
- *The pulls.* Let `u_B = S_B G(x − x_B)`, where `G` is the even Green function of the averaging law and `S_B` is `B`'s source strength. The pull on `A` is `−E_A S_B ∇G(x_A − x_B)`, and on `B` it is `+E_B S_A ∇G(x_A − x_B)`.
- Their sum is `−(E_A S_B − E_B S_A)∇G`. It vanishes at every separation iff `S_A/E_A = S_B/E_B` (block 55 T3, re-derived).

**Step 6 (PROVED; CHECKED C.kappa). `κ` for a record.**
- Block 55's packet has `S/E = −γ/6`: its law is `u_x − avg = −(γ/6)e_x/w̄`, with `w̄ = 1` in ambient ticks.
- A record with block 53's source has `S = log κ`. Step 5 therefore requires `log κ = −(γ/6)E_rec`, i.e. `κ = e^{−γE_rec/6}`.
- *What replaces `κ`.* With `γ` universal, the per-record free number is the record's energy `E_rec`.
- *For a block 54 walker at rest.* It has no rest energy: no 2×2 matrix anticommutes with `H` (block 54). So `E_rec = 0` and `κ = 1`, which agrees with Step 2's isolated record.
- A rest energy needs a further supplied term, such as block 77's staggered `mε` (PR #8612). Then `κ = e^{−γm/6} < 1`.

**Step 7 (PROVED). Nothing in the present clauses fixes `γ`.**
- `γ` enters only as the coefficient of the supplied field energy `F = (2/γ)Σ_bonds(φ_x − φ_y)²` (blocks 55, 56).
- For every `γ > 0`, `F` has weight one under `w → tw`, which is the scale covariance of block 53. It is covariant, it keeps block 55's ledger with the source `e − μ`, and it gives action equal to reaction (Step 5).
- So every clause of blocks 53–56 holds for the whole family `γ > 0`, and none selects a member.
- *The value is physical.* The weak-field pull is `−(γ/4π)E_AE_B/R`, and changing `γ` changes the pull between bodies of given energies. So `γ` is a genuine free number, not a choice of units.
- *What could fix it:* a clause that ties the field energy's scale to the amplitudes' own energy. The only candidate in the campaign is block 76's reading (PR #8611, not adopted), in which the filled sea's energy induces the field term. There `γ = 1/κ_stiffness ≈ 10.5` (executed, floating point), but only after the volume term is removed; with it the pull is repulsive, and the reading imports anticommuting composition.

**ASSUMED:**
- empty sites tick at the ambient rate in Step 2;
- block 54's pull law for records (task premise (b)).

## 3. The first failing step

The natural route "block 50's clock is block 53's `κ`" fails at Step 4. The clock gives an isolated record no source, and it gives clusters sources whose total vanishes, so no far field results.

Equal pulls (Steps 5–6) then say that such records carry no net energy. That is consistent, but it moves the question to the record's energy, which the present walk does not supply.

## 4. What would finish it

1. **A clause for a record's energy at rest.** Block 77's staggered term is one candidate; with it, `κ = e^{−γm/6}`.
2. **A clause fixing `γ`.** An induced field energy (block 76's direction) with the volume term understood is one route.
3. **Decide whether any local clock is exact at all densities** (block 50's open item). If one is, recompute its `κ` field: Step 4's zero-total structure holds for any clock of the form `w = 1/π_x` with `π` a product of pair terms.

## 5. Running it

```
python3 probes/work/derive/kappa-from-the-rule/w-macbookpro90c72-j9337/check.py
```

Requires `sympy`; the run takes a few seconds. All values are exact rationals or formal logarithms.
