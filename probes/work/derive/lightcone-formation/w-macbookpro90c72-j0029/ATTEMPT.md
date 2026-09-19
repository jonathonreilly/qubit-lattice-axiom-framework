# lightcone-formation, attempt 6 (worker w-macbookpro90c72-j0029, model grok-4.6)

Plan formed before reading other attempts. Objects are those of the LEAD in
`probes/lib/formation_levelplane.py` (symmetric flag: `dim=3s`) and block 19
(PR #8153) as the static comparator, not as authority for this law.

**The law.** Event lattice `Z^{3+1}` with time `t ∈ Z` and space `x ∈ Z^3`. The
record `s_{t+1,x}` is drawn from the covariant weight `exp(β s · S_{t,x})` on the
menu (sphere, or a finite unit-vector menu), given the seven records of the
*symmetric* past

```
S_{t,x} = s_{t,x} + Σ_{j=1}^3 (s_{t, x+e_j} + s_{t, x−e_j}).
```

Records are permanent. Read as a synchronous PCA on `Z^3`: `s'_x ∼ exp(β s'_x · S_x(s)) / Z(β |S_x(s)|)`,
independently across `x` given `s`. Write `N = {0, ±e_1, ±e_2, ±e_3}` (`|N|=7`),
`N = −N`. The *backward* 4-stencil `{0, −e_j}` is used only as a no-go.

`Z(κ)` is the menu's partition function at field strength `κ`. For the sphere,
`Z(κ) = 4π sinh(κ)/κ` (`κ = β |S|`). For a finite menu `M`,
`Z(S) = Σ_{m∈M} exp(β m·S)`.

## (1) The statement attempted

**(a)** The 7-stencil PCA is reversible with respect to
`π(ds) ∝ ∏_x Z(β |S_x(s)|) ∏_x λ(ds_x)` (`λ` the menu measure). Equivalently
`π(s) P(s'|s) = π(s') P(s|s')` as measures. The identity used is
`Σ_x s'_x · S_x(s) = Σ_x s_x · S_x(s')`. This fails for the backward 4-stencil
(exact integer counterexample on the `L=3` torus).

**(b)** `π` is the `s`-marginal of the classical Heisenberg ferromagnet on the
*doubled graph* `Γ`: two copies of `Z^3` with an edge between `(x,0)` and
`(x+z,1)` for each `z ∈ N`. The graph Laplacian at crystal momentum `k` has
spectrum `{E(k), 14 − E(k)}` with `E(k) = 2 Σ_j (1 − cos k_j)`. Long-range order
via FSS on `Γ` is **not** claimed (the classical RP/FSS theorem is named, not
re-proved).

**(c)** Linear gain-one model: `φ(k) = 1 − E(k)/7`, and
`σ²/(1 − φ(k)²) = 7 σ² / (2 E(k) (1 − E(k)/14))` identically (the Green-function
kernel `1/E` times a bounded factor `7 / (2(1 − E/14)) ∈ [7/4, 7/2]` on
`E ∈ (0, 12]`).

**(d)** The vMF mean map `S ↦ A(β|S|) Ŝ` has Jacobian `(β/3) Id` at `S = 0`.
The linearised Dobrushin coefficient of the PCA is `7β/3`; the threshold
`7β/3 < 1` is `β < 3/7`. Global Lipschitz `≤ β/3` is **ASSUMED** (sampled
`A'(κ) ≤ 1/3` and `A(κ)/κ ≤ 1/3`; covariance of vMF is standard).

**(e)** The static comparator of block 19 has pair Hamiltonian `−β Σ_{⟨xy⟩} s_x·s_y`
(coordination 6). This law's equilibrium weight is `∏_x Z(β |S_x|)`, i.e.
`−Σ_x log Z(β |S_x|)`. For the sphere, `log(sinh κ / κ) = κ²/6 − κ⁴/180 + O(κ⁶)`,
so the leading small-`β` interaction is `(β²/6) |S_x|²` (a 7-stencil quartic in
the spins at higher order), not the static pair.

## (2) Steps

**Step 1 — bilinear identity (PROVED; CHECKED as E1, E3).**
```
Σ_x s'_x · S_x(s) = Σ_x Σ_{z∈N} s'_x · s_{x+z} = Σ_z Σ_u s'_{u−z} · s_u
  = Σ_u s_u · Σ_{w∈N} s'_{u+w}     (w = −z, N = −N)
  = Σ_u s_u · S_u(s').
```
Checked with integer 3-vector configurations on periodic `L=2` and `L=3`, and
for all `256` Ising configurations on `L=2` against four partners (`1024/1024`).

**Step 2 — reversibility (PROVED from Step 1).**
The kernel is `P(ds'|s) = ∏_x [exp(β s'_x · S_x(s)) / Z(β |S_x(s)|)] λ(ds'_x)`.
The weight `π(ds) ∝ ∏_x Z(β |S_x(s)|) λ(ds_x)` cancels the denominators, leaving
```
π(ds) P(ds'|s) ∝ exp(β Σ_x s'_x · S_x(s)) ∏ λ(ds_x) λ(ds'_x),
```
symmetric in `(s, s')` by Step 1. Hence detailed balance. On a finite torus the
normaliser is finite for every compact menu; the infinite-volume Gibbs statement
is the DLR version of the same specification (the 7-star of `x` is finite-range).

**Step 3 — backward no-go (CHECKED as E2; PROVED by the same expansion).**
If `N` is replaced by `N⁻ = {0, −e_j}`, then `N⁻ ≠ −N⁻`. On the `L=3` torus,
`s = 1_{x=0} e_1`, `s' = 1_{x=e_1} e_1`: the 7-stencil pairing is `1=1`; the
backward pairing is `left=1`, `right=0`. So the product-form `∏ Z(S⁻_x)` cannot
be a reversible weight for the backward automaton.

**Step 4 — doubled graph (PROVED; CHECKED as E0b–E0d, E6).**
`∏_x Z(β |S_x(s)|) = ∫ ∏_x exp(β s'_x · S_x(s)) λ(ds'_x)` (definition of `Z`).
The exponent is `β` times the bilinear form of Step 1, i.e. `β Σ_{z∈N} Σ_x s'_x · s_{x+z}`:
Heisenberg ferromagnet on `Γ` (bipartite, parts the two copies, degree 7).
Bloch adjacency between copies: `Σ_{z∈N} e^{ik·z} = 1 + 2 Σ_j cos k_j = 7 − E(k)`.
Laplacian eigenvalues `7 ± (7 − E(k)) = E(k)` and `14 − E(k)`. Checked at
`k=(π,0,0)`: `E=4`, `7−E=3`.

**Step 5 — linear kernel identity (CHECKED as E0a).**
`φ(k) = (1 + 2 Σ_j cos k_j)/7 = 1 − E/7`. Then
`1 − φ² = (E/7)(2 − E/7) = E(14−E)/49`, so
`1/(1−φ²) = 49/(E(14−E)) = 7 / (2 E (1 − E/14))`. Sympy simplifies the difference
to `0`. The prefactor `7 / (2(1−E/14))` is bounded on the torus minus the zero
mode (`E ∈ (0, 12]`, value in `[7/4, 7/2]`).

**Step 6 — linearised Dobrushin threshold `β = 3/7` (CHECKED as E4; global Lip ASSUMED).**
Sphere: mean of vMF(`β S`) is `A(β|S|) Ŝ` with `A(κ) = coth κ − 1/κ`.
`A'(0) = 1/3` and `A(κ)/κ → 1/3` (sympy limits). Samples at
`κ ∈ {1/10, 1/5, 1/2, 1, 2, 5, 10}` have `A'(κ) ≤ 1/3` and `A(κ)/κ ≤ 1/3`.
The Jacobian at `S=0` is `(β/3) Id`. One past site enters seven stars, so the
linearised influence is `7β/3`. The identity `7·(3/7)/3 = 1` is exact.
**ASSUMED** for a uniqueness theorem: `‖Cov_{vMF(κ)}‖ ≤ 1/3` for all `κ` (so the
Lipschitz is globally `β/3`). Under that assumption the PCA is unique for
`β < 3/7`.

**Step 7 — static vs this law (CHECKED as E5).**
`log(sinh κ / κ) = κ²/6 − κ⁴/180 + O(κ⁶)` (sympy series). The static law of
block 19 is pair-weight `exp(β s·s')` on six nearest-neighbour bonds. The two
Hamiltonians agree neither at small `β` (quadratic in `β` vs linear) nor in
range (7-star vs edge). Block 19's infrared/Bogoliubov constants therefore do
not transfer; the doubled-graph spectrum of Step 4 is the replacement if FSS
is applied to `Γ`.

**Step 8 — FSS/LRO (ASSUMED, not claimed).**
Fröhlich–Simon–Spencer infrared bound for the classical Heisenberg ferromagnet
on a reflection-positive graph would give a transverse bound of the form
`(1/β) times a linear combination of 1/E(k)` and `1/(14−E(k))`. Reflection
positivity of `Γ` through a plane is not re-proved here. No long-range-order
threshold is stated.

## (3) First failing step of routes not taken

- *Backward / one-sided past as a reversible PCA:* fails at Step 3 (exact).
- *Transfer of block 19's constants to this law:* fails at Step 7 (different
  Hamiltonian, different graph).
- *Unconditional uniqueness for all `β < 3/7`:* fails at the global Lipschitz
  of vMF (Step 6, ASSUMED). A proof that `A'(κ) ≤ 1/3` for all `κ > 0` would
  close it.
- *LRO at large `β`:* not attempted beyond naming FSS on `Γ` (Step 8).

## (4) What would finish it

- Prove `A'(κ) ≤ 1/3` (equivalently `sinh² κ ≥ 3κ²/(κ²+3)` for `κ² < 3`, and the
  complementary range by `csch² κ ≥ 1/κ² − 1/3`) to make `β < 3/7` a theorem.
- Prove reflection positivity of the Heisenberg ferromagnet on `Γ` through a
  site or bond plane, then run FSS with the spectrum of Step 4, for an explicit
  `β` threshold.
- Two-sided kernel bound for the *nonlinear* sphere PCA (cluster expansion at
  small `β` around the linear kernel of Step 5; infrared bound at large `β`
  after RP).

Nothing here edits notes or runners.
