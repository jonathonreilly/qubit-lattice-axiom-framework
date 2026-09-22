# inertia-with-the-rules-weights, attempt 1 of 4: a clause exact for pairs, record-by-record balance impossible beyond them, and local global balance not excluded

Worker `w-jonathonsmac4f50-jbc35` (`claude-opus-5-5`), unit `J-derive-inertia-with-the-rules-weights:a1`.

**Provenance.** There were no prior attempts. Block 44's clause, block 39's law with vacancies and block 40's pinned scale come
from open PRs #8550, #8530 and #8546, all by the same model family as me. My stationarity code generalises block 44's runner
(`stationarity`) and reproduces its two-record count of 12636 configurations.

## 1. What is claimed

**Setting.** Six-axis menu. The law with vacancies is `μ(c) ∝ z^n Π_{adjacent pairs} W(s_x, s_y)`, with `W = c₀ω` and
`c₀ = 6/(p+q+4r)`. Block 44's streaming, exchange and scattering events are unchanged. All numbers are at
`(p,q,r) = (5,1,2)` unless stated.

> **(a) The departure clause.** Every streaming event of the record at `x`, whether a move or an exchange, has rate
> `1/Ŵ(x)`, where `Ŵ(x)` is the product of that record's pair weights with its current neighbours. Scattering is the heat bath on
> the momentum class with weights `μ`. The clause is covariant and conserves number and momentum event by event.
>
> **Theorem 1 (two records).** The departure clause keeps the law with vacancies stationary, exactly, for every weight triple and
> with or without scattering. **CHECKED** on every configuration of the `3³` and `4³` tori at four triples. Block 44's plain
> clause does not do this (5832 of 12636 configurations unbalanced).
>
> **Theorem 2 (no record-by-record balance beyond two records).** Suppose a clause has local rates, streams isolated records at
> rate 1, and balances each record's streaming inflow against its outflow. If it keeps `μ` stationary, then `W ≡ 1`: all three
> weights are equal, which at `c₀` means `p = q = r`. The reason is that an exchange displaces the passed record by one step, and
> that changes its bond with a third record, which the carried flux cannot pay for.
>
> **What is not excluded.** Global balance with local rates. On the `4³` torus with three records, a linear program over move and
> exchange rates (630 covariant classes; rates may depend on the contents within distance 1 of the event's two sites) finds
> strictly positive rates that make `μ` stationary. Its optimal minimum rate is `0.217778 = 49/225 = 1/W_eq²` (**NUMERIC**). At
> constant weights the optimum is `1`, which is block 44's clause. So impossibility cannot be shown at the three-record,
> range-1 level. Whether a single local clause works for **every** number of records is open.
>
> **(b)** Not done: no clause has been established for all numbers of records, so there are no currents or pressure to expand.
>
> **(c) The closest clause.** It is the departure clause, exact for pairs. On `3³`, the stationarity defect of `μ`
> (`Σ|inflow − outflow| / Σ outflow`) is:
>
> | records | block 44's plain clause | departure clause |
> |---|---|---|
> | 2 | `32/273` (11.7 %) | `0` |
> | 3 | `192896/1003977` (19.2 %) | `176/20475` (0.86 %) |
>
> The task's example, weights acting only in the scattering step, changes nothing. Heat-bath scattering is balanced on its own,
> so it leaves the plain clause's defect as it is.

## 2. The steps

1. **PROVED + CHECKED (T0): conservation and covariance.**
   - A move carries a record and its content. An exchange permutes two contents. A heat-bath re-draw stays inside the momentum
     class.
   - Rates are functions of pair weights, which are rotation invariant, and of momentum classes. So the clause commutes with the
     24 proper rotations, as block 44's does. Conservation is checked on sample configurations.
2. **PROVED + CHECKED (T1): Theorem 1.**
   - Block 44's T2 gives every record `r` of a configuration `c` exactly one streaming preimage: either `r` moved in from behind,
     or the record behind triggered an exchange.
   - With two records, every bond involves the mover, so `μ(pre) = Ŵ_mover(pre)` (in units of `z²`). The inflow through `r`'s
     preimage is therefore `μ(pre)/Ŵ_mover(pre) = 1`.
   - `r`'s outflow is `μ(c)/Ŵ_r(c) = 1` for the same reason.
   - Heat-bath scattering satisfies detailed balance. So every configuration balances. ∎
   - **CHECKED** exactly: all 12636 (`3³`) and 72576 (`4³`) configurations, at `(5,1,2), (3,1,2), (7,2,1), (2,1,1)`, with
     `γ = 0, 1, 1/3`.
3. **PROVED: Theorem 2.**
   - Let `Φ(c)` be the outflow flux, `μ(c)·rate`, of the record carrying a given content `d`. Record-by-record balance says the
     inflow into `c` through that content's preimage equals `Φ(c)`. That inflow is `Φ(pre)`, so `Φ` is constant along the
     content's chain.
   - Where the carrier is isolated (no record within the rates' range), its rate is 1 and `Φ(c) = μ(c)`, the weight of the
     other records' bonds.
   - Now place records on `Z³`:
     - `B` at the origin with content `d_B`;
     - `C` at `−e_x + e_z` with content `d_C` (not adjacent to `B`);
     - `A` with content `+x` far to the left on the `x`-axis.
   - Follow `A`'s content. It streams in, is exchanged at the origin (the record at `−e_x` now carries `d_B`: `B` has been
     displaced by `−e_x`), and streams away to the right.
   - Before, `Φ = Π_{others} = 1`, since `B` and `C` are not adjacent. After, `Φ = W(d_B, d_C)`, since the displaced `d_B` is
     adjacent to `C`. Constancy forces `W(d_B, d_C) = 1` for all pairs.
   - **CHECKED** in its finite form (T2). On `3³` with three records the departure clause fails at 34344 of 631800
     configurations. In the witness (`+x` at 000, `+x` at 001, `+y` at 010), the inflow is `1 + W_orth + 1 = 20/7` and the outflow
     `1 + W_orth + W_eq = 4`. The exchange that brought `+y` to 010 turned the third record's bond from `W_orth` to `W_eq`.
4. **CHECKED, exact (T3): the defects** in the table above.
5. **NUMERIC (N1): global balance is feasible.**
   - Method: reduce the `4³` torus by translations (140616 classes). The unknowns are move and exchange rates per covariant
     environment (630 classes), with an isolated move pinned at rate 1. Maximise the smallest rate subject to exact balance
     (HiGHS).
   - Optimum `49/225 = 1/W_eq²` at `(5,1,2)` and `1` at constant weights. The same optimum appears on `3³`.
   - An earlier least-squares test is consistent with this: fixing move rates at the departure rule and freeing only exchange
     rates left a residual of 88 against `|b| = 541` on `3³`. The move rates must adjust too.
   - The LP optimum is not unique, and I did not extract a closed-form rule from it.

## 3. Where this stops

- **(a) is decided only in part.**
  - Proved: record-by-record balance is impossible beyond pairs.
  - Found: global balance with range-1 local rates is feasible for three records on two windows.
  - Not decided: whether one covariant local clause keeps `μ` stationary for every number of records. Four records at range 1
    were not tested, since the `4³` window with four records is 12.9 million translation classes.
- **The LP solutions have no closed form yet.** Their minimum `1/W_eq²` suggests the departure rates survive where a record
  leaves two aligned neighbours.
- **(b) is not attempted.**
- **Only the six-axis menu is treated.** The sphere menu's clause has non-deterministic stepping (`max(0, s·e_k)/√3`), and the
  same pairwise analysis applies to it with the step kernel in place of the unit step. Not done.

## 4. What would finish it

1. A closed-form reading of the LP's three-record solution, for example by fixing the departure move rates wherever the LP
   allows and solving for the rest. Then test it with four records on a window where range 1 is local.
2. Or: a four-record infeasibility certificate at range 1 (a vector `y` with `yᵀA = 0`, `yᵀb ≠ 0`, restricted to `r ≥ 0` by
   Farkas), which would turn Theorem 2 into a full no-go.
3. With a clause in hand: its product-state currents and pressure to first order in `ω − const` (block 44's T3 method), and the
   wind law.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/inertia-with-the-rules-weights/w-jonathonsmac4f50-jbc35/check.py
```

Requires `scipy` for N1. There are 6 checks, and the run takes about 3 minutes, most of it the exact three-record
enumerations. `inertial_weights.py` is the stationarity machinery (a generalisation of block 44's `stationarity`), and
`lp_feasibility.py` is the translation-reduced linear program.
