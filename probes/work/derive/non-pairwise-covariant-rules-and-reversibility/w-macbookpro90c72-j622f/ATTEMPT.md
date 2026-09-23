# J:derive:non-pairwise-covariant-rules-and-reversibility:a1: a formation rule gives a reversible level chain iff its log-law is two-body and exchange-symmetric; block 19's linear rule is one member; rules with three-body terms are irreversible

**Provenance.**
- Worker `w-macbookpro90c72-j622f`, model `claude-opus-5-5`, one session. Attempt 1 of 2; the claim printed no prior attempts.
- **Plan, formed before reading the notes in detail.**
  - The partition functions of a level chain cancel around cycles. So Kolmogorov's criterion is a linear condition on the log-law `F`, and exact linear algebra on small rings can solve it.
  - A mixed-difference argument should then force two-body structure.
- **Related earlier unit.** The same model did `J:derive:lro-of-level-ordered-formation-in-3plus1:a1` (issue #8714, unrefereed) on the level-ordered past; it is not used here.
- **Sources.** Block 93 (branch `physics-loop/admissibility-induced-law-block93-covariance-forces-a-reversible-formation-law-20260923`; no PR number yet):
  - the covariant pasts `{0, ±e_j}` with weights `(w₀, w₁)` (T1);
  - block 19's rule `p(s′|h) ∝ exp(βs′·h)`;
  - detailed balance with `π = Π_x Z(h_x)` (T2).
- **Comparator, named only.** The characterization of reversible probabilistic cellular automata (Kozlov–Vasilyev and later). It is re-proved here at the scope used.
- Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Setting.**
- Levels `s = (s_x)` of records, contents from a menu `M` (the sphere, or a finite subset such as the six axes).
- A record at `x` forms from its predecessors `η_x(s) = (s_{x+d})_{d∈D}` in the level below, with `p(s′|η) = exp F(s′; η)/Z(η)`, `F` real and finite.
- The level chain is `K(s → s′) = Π_x p(s′_x|η_x(s))`.
- The past `D` is symmetric (`d ∈ D ⟺ −d ∈ D`). By block 93 T1 every covariant past in the 3+1 reading is.

**(a) Theorem (PROVED; CHECKED N.null).** On a ring or torus large enough that distinct offsets are distinct sites, `K` is reversible iff

`F(s′; η) = Σ_{d∈D} φ_d(s′, η_d) + ψ(s′) + c(η)`, with `φ_{−d}(b, a) = φ_d(a, b) + α_d(a) + β_d(b)`.

- **Two-body:** the `s′`-dependence is a sum of two-body terms, one per predecessor.
- **Exchange-symmetric:** each term is symmetric under exchanging the two records with the offset reversed, modulo one-record terms.
- **The stationary law** is then `π(s) ∝ Π_x Z(η_x(s)) exp(Σ_x ψ̃(s_x))`, with `ψ̃` collecting the one-record terms.
- **Scope.** No symmetry beyond the symmetric past is needed. Covariance only restricts which `φ` are allowed.
- **CHECKED exactly** on rings with past `{x−1, x, x+1}` and every positive `F`: the space of reversible rules equals the two-body family.

  | menu | ring | constraints | unknowns | dimension (both) |
  |---|---|---|---|---|
  | 2 | 4 | 120 | 16 | 11 |
  | 3 | 4 | 3240 | 81 | 36 |
  | 2 | 5 | 496 | 16 | 11 |

**(b) Is pairwise the only reversible class?**
- **In the two-body sense, yes (a).**
- **Block 19's linear rule is not the only reversible covariant rule.**
  - **Counterexample** (CHECKED N.cube): the nematic rule `F = γ Σ_d w_d (s′·s_{x+d})²` is covariant under the 24 rotations, two-body and exchange-symmetric, hence reversible. Its cycle sums vanish exactly on the `3³` torus with the six-axes menu.
  - **Why it is not block 19's.** It is even in `s′`. Block 19's rule, with any `β ≠ 0` and any covariant `ψ` (constant, since the rotations are transitive on the axes), is not.
- **The task's two examples are covariant and irreversible** (CHECKED N.cube, exact cycle sums on the `3³` torus):
  - `βs′·h + γ(s′·h)²` has the three-body terms `γw_dw_{d′}(s′·s_d)(s′·s_{d′})`, and a cycle sum `−4γ`;
  - `βs′·h/|h|` has a cycle sum `β·(−19448√5 − 7480√13 − 2210√11 + 2145√17 + 24310√3 + 60775)/12155 ≈ 2.79β`.

## 2. Steps

**S1 (PROVED). Kolmogorov's criterion reduces to a gradient condition on `F`.**
- All transitions are positive, so `K` is reversible iff every cycle has equal products both ways, iff `log K(s→t) − log K(t→s) = A(t) − A(s)` for some `A`.
- `log K(s→t) = Φ(s,t) − Σ_x log Z(η_x(s))`, with `Φ(s,t) = Σ_x F(t_x; η_x(s))`. The `Z` terms form a gradient.
- So reversibility ⟺ `D(s,t) := Φ(s,t) − Φ(t,s) = B(t) − B(s)`, i.e. `D(s,t) = D(s₀,t) − D(s₀,s)` for all `s, t`.
- This is linear in the values of `F`. That makes the exact nullspace computation of N.null possible.

**S2 (PROVED). Necessity.**
- **The mixed difference.** Take a mixed second difference of `D(s,t) = B(t) − B(s)` in `t_x` (values `a, a′`) and `s_y` (values `b, b′`). The `B` terms drop out.
  - In `Φ(s,t)`, `t_x` appears only in the term at `x`. There `s_y` enters as the predecessor in slot `d = y − x`, if `y − x ∈ D`.
  - In `Φ(t,s)`, `s_y` appears only in the term at `y`, as the forming record, and `t_x` enters there as the predecessor in slot `−d`.
- **The consequence.** So `Δ_aΔ_b F(a; η_d = b, other slots = s at x's other predecessors)` equals `Δ_bΔ_a F(b; η_{−d} = a, other slots = t at y's other predecessors)`. These two "other slot" sets are values in different levels and can be varied independently. So both sides are independent of the other slots.
- **Two-body structure.** Fix references `r` for `s′` and `ρ` for the past, and define `φ_d(s′, b) := F(s′; ρ with slot d = b) − F(r; ρ with slot d = b) − F(s′; ρ) + F(r; ρ)`. Telescoping `F(s′; η) − F(r; η)` over the slots, changing one at a time from `ρ_k` to `η_k`, gives `F(s′; ρ) − F(r; ρ) + Σ_k φ_k(s′, η_k)`, because each step's mixed difference sees only its own slot. Hence `F = Σ_d φ_d + ψ + c` with `ψ(s′) = F(s′; ρ) − F(r; ρ)` and `c(η) = F(r; η)`.
- **Exchange symmetry.** The equality of mixed differences then says `φ_d(a, b) − φ_{−d}(b, a)` has vanishing mixed differences, i.e. it is `α_d(a) + β_d(b)`.
- **Size requirement.** The ring or torus must be large enough that `x + d` are distinct sites for distinct `d` (side ≥ 3).

**S3 (PROVED). Sufficiency.**
- With the stated form, reindex `Σ_{x,d} φ_d(s_x, t_{x+d}) = Σ_{y,d} φ_{−d}(s_{y+d}, t_y)` (using `D = −D`), which is `Σ_{y,d} [φ_d(t_y, s_{y+d}) + α_d(t_y) + β_d(s_{y+d})]`.
- So `D(s,t)` is a sum of terms depending on `t` alone minus terms depending on `s` alone: a gradient.
- Detailed balance then holds with the stated `π`. Block 93 T2 is the case `φ_d(a,b) = βw_d a·b`, `ψ = 0`.

**S4 (CHECKED N.null). Exact on rings.**
- **The constraint matrix.** For each pair `s < t`, the row is `D(s,t) − D(s₀,t) + D(s₀,s)` in the unknowns `F(s′; η_{−1}, η₀, η_{+1})`: all `m⁴` of them, no symmetry assumed.
- **Rank.** Computed by fraction-free integer elimination.
- **The family.** Its span (`c(η)`, `ψ(s′)`, and `[s′=a][η_d=b] + [s′=b][η_{−d}=a]`) lies in the nullspace, and its rank equals the nullity. So the two sets coincide on these systems.

**S5 (CHECKED N.cube). The covariant examples in 3+1.**
- **Setup.** `3³` torus, six-axes menu, past `{0, ±e_j}` with `w₀ = w₁ = 1`. Four random triples `(s, t, u)` of levels, with cycle sum `D(s,t) + D(t,u) + D(u,s)` in exact arithmetic (symbolic `β`, `γ`; exact surds).
- **Results:**
  - block 19's rule and the nematic rule: 0 on every triple;
  - `βs′·h + γ(s′·h)²`: no `β` part, and `−4γ` on a triple;
  - `βs′·h/|h|`: the surd sum above.
- **The oddness check** confirms the nematic rule is even in `s′`.

## 3. The first failing step

None for the claims made. The necessity argument needs positivity (all transitions positive) and a lattice where distinct offsets are distinct sites. On the sphere the same argument runs with densities and differences of values.

## 4. What would finish it

1. **Which two-body covariant rules** are admissible in the framework's vocabulary, for example whether the nematic term has a reading (contents as axes rather than directions).
2. **The long-time laws of the reversible two-body family** under block 93's three pasts. The six-neighbour past splits into two static laws for any exchange-symmetric `φ`, by block 93 T3's relabelling.

## 5. Running it

```
python3 probes/work/derive/non-pairwise-covariant-rules-and-reversibility/w-macbookpro90c72-j622f/check.py
```

The run takes about 1 s. It prints two exact checks, then the SUMMARY and HIT lines.
