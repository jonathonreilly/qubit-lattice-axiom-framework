# moving-records-and-the-balance-of-the-two-charges, attempt a2: records carry no fixed hop energy, and crossing at the member's factor cannot bind them

Worker `w-macbookpro9927a-j30ab` (`claude-opus-5-5`), unit `J-derive-moving-records-and-the-balance-of-the-two-charges-a2`.

**Sources, read as landed on origin/main `0e6ad8285096`.**
- Block 110 is landed; the task names it as open PR #8960. Its title as landed is "Around a body, the walk's rays match the comparator's at every order exactly when the body's two charges agree; the charges agree only when hop energy balances the slowed clocks".
- Block 60 (the curvature member) and block 59 (rates, lengths, the crossing factor).
- Block 95 as landed: "Detailed balance for fixed and configuration-following clocks". Its T1 and T2 give the laws for rates `exp[a u_x + (1−a)u_y] h/6`. Its pair law is the neutralized torus law.
- Block 97's leaving-site timing, as used by `probes/lib/clocked_gas.py`.
- No landed narrowing listed in the task changes what is used here. Block 95 is used only as landed, with its neutralized torus field.

**Provenance and independence.**
- **No prior attempt** at this problem was on ai/probes at claim time. The plan below is my own.
- **Block 110 T2 comes partly from my earlier units.** It credits:
  - #8649 (`bound-bodies-and-the-two-far-fields` a1: the `P − Q` formula);
  - #8732 (`internal-hop-energy-and-the-two-masses` a1: the per-site weight `(3w − 1)/w` and the dimer locus);
  - #8912 (`strong-field-turning-by-a-clump` a2).
- **Also related:** #9090 (`formation-timed-by-the-clock` a2), which uses the clocked gas's pair law.
- **None of these treats records as the member's content.** The question here, what a moving record contributes to `e` and `τ`, is new. I reuse only block 110's landed formulas.
- **Sibling search.** No attempt on ai/probes computes record-layer charges (a grep of `probes/work`).

## 1. What is attempted

**(a) Is the clause fixed?**
- **Setting.** Block 110 T2's sources are `e_x = ∂H/∂u_x` and `τ_x = −∂H/∂λ_x`, derivatives of a content energy `H(u, λ)`. Records are a Markov process, not an energy.
- **Claim A: a new clause is needed.** Take two energies for the same records, `ω` any even pair weight:
  - **rest only**, `H_R = Σ_{x∈C} m w_x`;
  - **activity at the crossing factor**, `H_A = H_R + μ Σ_{bonds with one end occupied} ½√(w_x w_y)/(χ_xχ_y)`. This is the expected transit rate, with the heat-bath factor `½`.

  Both have the homogeneity block 110 T2(e) needs: degree 1 in the rates, and for the hop part degree `−2` in the lengths. On the same records and fields they give `P − Q` of opposite signs. So block 60 T2's derivatives do not fix a record's `(e, τ)`.
- **Claim B: records crossing at the member's factor cannot bind.**
  - Records transit to an empty neighbour at `κ_xy h/6`, with `κ_xy = √(w_x w_y)/(χ_xχ_y)` and `h = W(C′)/(W(C) + W(C′))`.
  - Then the stationary law is `π(C) ∝ W(C)` for **every** fixed positive clock and length field. The fields drop out, as in block 95 T1 at `a = ½`, with the symmetric length factor added.
  - For fields that follow the records, `u = Σ U(z − r)` and `φ = χ − 1 = Σ Φ(z − r)` with even kernels, the same holds at first order.
  - So no clump of such records is held in its own field. A clump needs the leaving-site timing of block 97 (`a = 1`, rate `w_x h/6`), and that is not the member's crossing factor.

**(b) Is there a record-layer virial?** No, under the activity clause.
- **Claim C.** At weak field, block 110 T2(c) gives `P/Q = 1 + 2Στ/Σe`. With the activity clause, `Στ = μB/2`, where `B` is the number of bonds with exactly one end occupied. So

  `P/Q = 1 + μ⟨B⟩/(mN + μ⟨B⟩/2) > 1`

  for every stationary law in which a record can move (`⟨B⟩ > 0`). Nothing makes `P = Q` at weak field unless the gas is jammed.
- **Values.**
  - Exact on `3³` (`m = μ = 1`): the uniform law gives `251/101` (2 records) and `121/49` (3 records); the clocked gas's law gives `2.4290` and `2.3353`.
  - Simulated on `8³` (27 records): `2.48` at `g = 0`, and `2.16` for a bound clump at `g = 3`.

**(c) The smallest clause that would.**
- `P = Q` at leading weak-field order holds if and only if `Στ = o(Σe)`. So the records' hop energy must vanish with the field.
  - The rest-only clause is the smallest such. It gives `P/Q → 1`, but by block 110 T2(c) it has `P < Q` at every finite field.
  - A clause counting only the field's change of the crossing activity also vanishes with the field.
- Whether a record virial then balances the first-order difference is open.

## 2. Steps

0. **ASSUMED (supplied).**
   - The curvature member, the rates and lengths, and the crossing factor (blocks 59 and 60).
   - Block 95's transit with the heat-bath factor and symmetric proposals.
   - The activity and rest-only clauses, which are supplied here as candidates.
   - Nothing is adopted.

1. **PROVED; CHECKED T1 (field-blind crossing).**
   - `κ_xy` is symmetric in `x ↔ y` for fixed fields. So `W(C)·κ_xy h(C,C′) = W(C′)·κ_yx h(C′,C)`, and detailed balance holds with `π ∝ W`.
   - For the contrast, leaving-site timing `w_x h/6` balances `π ∝ W(C)/Π_{z∈C} w_z` (block 95 T1 at `a = 1`).
   - Check T1: both on `3³` with 3 records, random rational `w = s²`, lengths `χ`, and a random even pair weight. That is 900 configurations and every move from them, exactly.

2. **PROVED; CHECKED T1b (fields that follow the records, first order).**
   - Write `C = D ∪ {x}` and `C′ = D ∪ {y}`. Then

     `u_x(C) + u_y(C) − u_y(C′) − u_x(C′) = U(y − x) − U(x − y) = 0`

     for an even `U`, and the same holds for `Φ`.
   - So `log κ_xy(C) = log κ_yx(C′)` at first order, and `π ∝ W` stays stationary.
   - Check T1b: every move from 400 configurations on `3³`, with `U` the mean-zero torus Green function (exact) and an even `Φ`.

3. **PROVED; CHECKED T2 (the clause is not fixed).**
   - Records have no `⟨H⟩`: block 60 T2 differentiates a content energy, and the record layer is a generator. `H_R` and `H_A` are both functions of `(u, χ)` with the required homogeneity (checked symbolically).
   - Block 110 T2(b)'s charges from each, on the records `{0, 1, 3}` of `3³` with clocks `(1 − 1/20)²` and lengths `1 + 1/40`:

     | clause | `P − Q` |
     |---|---|
     | rest only | `−117/3280 < 0` |
     | activity | `+3893397/2555120 > 0` |

   - **Scope.** The charges are evaluated from block 110's formulas at the prescribed fields. The self-consistent weak-field statement is step 4.

4. **PROVED; CHECKED T3 (no record virial under the activity clause).**
   - At weak field `κ = 1`. Each bond with one occupied end carries `μ/2`, a quarter at each end, so `Στ = μB/2` and `Σe = mN + μB/2`. Block 110 T2(c) then gives `P/Q = 1 + μB/(mN + μB/2)`, averaged over the stationary law.
   - **The uniform law.** `⟨B⟩ = 6N(V − N)/(V − 1)` (exact, checked).
   - **The clocked gas's law.**
     - It is `π ∝ exp(6g Σ_pairs G)`, with `G` the mean-zero torus Green function, exact over `ℚ` with common denominator 486.
     - With `q = e^{6g/486} = 3/2`: `⟨B⟩ = 10.0096` (`N = 2`) and `12.0536` (`N = 3`), both below the uniform values. The ratios are `2.4290` and `2.3353`.
   - **All above 1.**

5. **Floating control N1 (evidence).** Leaving-site timing on `8³` with 27 records started as a cube:
   - `⟨B⟩/N = 5.69`, `5.57` and `2.77` at `g = 0, 1, 3`;
   - `P/Q = 2.48`, `2.47` and `2.16`.

   The clump binds at `g = 3`, and `P/Q` stays above 1.

6. **PROVED ((c)).**
   - By step 4's formula, `P/Q → 1` at weak field if and only if `Στ/Σe → 0`.
   - The rest-only clause gives exactly that. Block 110 T2(c) then gives `P < Q` at every finite field.

**Mutation census.** Each mutation fails in its own family:
- an asymmetric crossing factor fails T1;
- an odd kernel fails T1b;
- dropping the activity term fails T2;
- a wrong bond count fails T3.

## 3. Where the route stops (not claimed)

- **The self-consistent member at finite field.** Solving the member's nonlinear equations with the records as sources is not done. Step 3 evaluates block 110's formulas at prescribed fields.
- **Configuration-following fields beyond first order.**
- **A first-order record virial** for a clause whose hop energy vanishes with the field.
- **Which clause is right.** That is a decision for the owner, not a result.

## 4. What would finish it

- **Supply the clause.** For example: records carry the crossing-factor activity, or only the field's change of it.
- **With a vanishing hop energy,** test the first-order balance `2Στ = Σe(1 − w)/w` through a stationarity identity. The candidate is `⟨L Σ|x|²⟩ = 0`: the relation between a gas's spreading activity and its drift virial.
- **Solve the member self-consistently** with record sources on small boxes.

## Checks (`check.py`, about 7 s)

| Family | What it checks |
|---|---|
| T1, T1b | Field-blind crossing, with fixed fields and with configuration-following fields (exact) |
| T2 | The two admissible clauses, with opposite signs (exact) |
| T3 | Weak-field ratios under the uniform and clocked-gas laws on `3³` (exact) |
| N1 | Float evidence on `8³` |
