# waves-need-signed-weights: derivation attempt 5 of 5

Worker `w-jonathonsmac4f50-j62b1` (claude-opus-5), unit `J-derive-waves-need-signed-weights-a5`.

**Provenance, stated because it bears on independence.** The one prior attempt, `a2`
(`w-jonathonsmac4f50-jafb3`), is by the same model family, machine and running worker. I do not
re-derive or re-check its (a), (b) or (c); those look complete and re-running them would tell a
referee nothing. I take the item `a2` itself files under "what remains open" and close it:

> "**The vector version of (a).** For nonnegative matrix weights (several record components,
> stochastic mixing), are the rules with a unimodular branch on an open set exactly the
> componentwise copies (permutation-type weights)? Not proved here. The chiral pair and the
> persistent walk are the two sides of it."

**The answer is no** — the exceptional class is strictly larger than componentwise copies — and
the correct characterization is below, with the physical conclusion the task cares about
unchanged and now proved in the vector setting.

## 1. The statement attempted

**The model.** Record components `θ_t(x) ∈ R^M` on `Z^d`, one level of memory, nonnegative
matrix weights:

`θ_{t+1}(x) = Σ_y w(y) θ_t(x − y)`, `w(y) ∈ R^{M×M}`, `w(y) ≥ 0` entrywise, finitely supported,

with **gain one**: `A := Σ_y w(y)` is row-stochastic. The symbol is `W(k) = Σ_y w(y)e^{−ik·y}`
and the branches are the eigenvalues of `W(k)`. Write the *support graph* for the edges `(m,n)`
with `A_{mn} > 0`, and assume `A` irreducible (otherwise apply the theorem to each class).

> **Theorem V.** The following are equivalent.
> 1. Some branch has `|λ(k)| = 1` on a set of `k` with nonempty interior.
> 2. Each block is a single site — `w_{mn}(y) = A_{mn}δ_{y, y_{mn}}` — and there are `v ∈ Q^d`
>    and vectors `g_m` with **`y_{mn} = v + g_m − g_n`** for every edge of the support graph.
> 3. `W(k) = e^{−ik·v} D(k) A D(k)^{−1}` with `D(k) = diag(e^{−ik·g_m})`.
>
> When they hold, `spec W(k) = e^{−ik·v} spec A` for **every** `k`: the unimodular branches are
> `e^{−ik·v}` times the unimodular spectrum of `A`, each with the constant group velocity `v`.

Equivalently (2) says: every directed cycle of the support graph has mean displacement `v`.

**What this settles.** `a2`'s guess is too narrow. Two kinds of rule satisfy (2) without being
componentwise copies or permutations:

- **stochastic mixing at a common velocity** — `w_{00} = w_{01} = ½` and `w_{10} = 1`, all at
  `y = +1`. `A = [[½,½],[1,0]]` is not a permutation, yet `W(k) = e^{−ik}A` and the Perron branch
  `e^{−ik}` is unimodular at every `k`;
- **gauge-shifted displacements** — `0 → 1` at `y = 0` and `1 → 0` at `y = 2`: the blocks sit at
  *different* sites, the cycle mean is `+1`, and `spec W(k) = ±e^{−ik}`. Here `g = (0, 1)`.
- The velocity need not be an integer vector: `0 → 1` at `y = 0`, `1 → 0` at `y = 3` gives
  `λ² = e^{−3ik}`, `v = 3/2`.

**The physical conclusion, unchanged and now proved for vectors.** A unimodular branch of a
nonnegative rule is `e^{−ik·v}` times a constant: **no dispersion**, one velocity per irreducible
class. Finitely many classes give finitely many velocities, so in `d ≥ 2` the set of fronts is a
finite set of points, never an isotropic cone. Nonnegative weights — probabilities of records —
buy transport, never waves. To get a cone one still has to leave the nonnegative cone, which is
the task's (c).

## 2. Steps

**S1 (PROVED). `|λ| ≤ 1`, and the Perron equality.**
`|W(k)| ≤ A` entrywise in modulus, so for `W(k)u = λu`, taking moduli row by row gives
`|λ||u| ≤ A|u|` entrywise. Let `π > 0` be the left Perron vector of the irreducible stochastic
`A` (`πA = π`). Pairing: `|λ| π·|u| ≤ π A |u| = π·|u|`, and `π·|u| > 0`, so `|λ| ≤ 1`. If
`|λ| = 1` the inequality is an equality, so `A|u| = |u|` and **every triangle inequality used is
tight**.

**S2 (PROVED; CHECKED `G4`). What tightness says.**
Tightness in row `m` means all the terms `w_{mn}(y)e^{−ik·y}u_n` over the support of that row
share one argument `ψ_m`. Since `A|u| = |u|` with `A` irreducible stochastic, `|u|` is the Perron
vector, so `|u_n| > 0` for all `n` and `u_n = |u_n|e^{iφ_n}` is well defined. Writing the
eigenvalue equation's phase, `λ u_m = e^{iψ_m}|λ||u_m|`, hence `ψ_m = arg λ + φ_m`. Substituting:

> for every support edge `(m,n)` and every `y` in that block: `φ_n − k·y = arg λ + φ_m`.   (★)

**S3 (PROVED; CHECKED `G5`). Each block is a single site.**
Apply (★) to two sites `y ≠ y'` of the same block `(m,n)`: subtracting gives
`k·(y − y') ∈ 2πZ`. For fixed `y ≠ y'` the set of `k` with `k·(y − y') ∈ 2πZ` is a union of
hyperplanes, closed with empty interior — `G5` counts them in `d = 1`: for `y − y' = m ≠ 0` there
are exactly `m` solutions in `[0, 2π)`. An open set of `k` therefore forces `y = y'`.

**S4 (PROVED). The displacement is a velocity plus a gauge.**
With single sites, (★) reads `k·y_{mn} = φ_n − φ_m − arg λ` for every edge. Summing around a
directed cycle of length `L` and total displacement `Y`, the `φ` telescope: `k·Y = −L arg λ`. For
two cycles `(Y₁,L₁)`, `(Y₂,L₂)` this gives `k·(Y₁/L₁ − Y₂/L₂) = 0` on an open set of `k`, hence
`Y₁/L₁ = Y₂/L₂ =: v`. Fix a spanning tree of the support graph and define `g` along it by
`g_m − g_n = y_{mn} − v`; the cycle condition makes this consistent on the non-tree edges. That
is (2), and `arg λ = −k·v`.

**S5 (PROVED; CHECKED `G1`). (2) ⟹ (3) ⟹ (1), with equality everywhere.**
With `D(k) = diag(e^{−ik·g_m})`,
`(D A D^{−1})_{mn} = e^{−ik·(g_m − g_n)}A_{mn} = e^{ik·v}e^{−ik·y_{mn}}A_{mn}`, so
`W(k) = e^{−ik·v}DAD^{−1}`. A similarity preserves the spectrum, so
`spec W(k) = e^{−ik·v} spec A`, which contains the unimodular `e^{−ik·v}` at **every** `k` — far
more than an open set. `G1` verifies the identity symbolically for five rules, including the two
that are not permutations and the one with `v = 3/2`.

**S6 (CHECKED `G2`, `G3`). The two sides, executed.**
- Rules satisfying (2): `A` is row-stochastic with `1 ∈ spec A`, and `e^{ik·v}W(k)` has the trace
  and determinant of `A`, hence its spectrum. Unimodular at all 61 of 61 grid points.
- Rules breaking either half: a two-site block, two cycles of means `+1` and `0`, and the
  persistent walk (`|C_{ij}|²` with `cos²θ = 9/25`) are unimodular on `1/61` of the grid — the
  single point `k = 0` — as the theorem requires.

**S7 (PROVED; CHECKED `G6`). `d ≥ 2`.**
The group velocity of the unimodular branch `e^{−ik·v}` is `∇_k(k·v) = v`, a constant: no
dispersion. Four chiral copies on `Z²` give the four branches `e^{∓ik₁}, e^{∓ik₂}` — four
velocities, four points of the front. Adding components adds points; by the theorem each
irreducible class contributes exactly one velocity, so a finite-component nonnegative rule can
never produce the continuum of velocities an isotropic cone needs.

## 3. Where the route stops

- **Irreducibility is assumed** for the class the branch lives on. For reducible `A` the theorem
  applies class by class (the chiral pair is two classes), but I have not written out the
  bookkeeping for a branch that is unimodular because of a *non-trivial* interaction between two
  classes — for triangular `A` the spectrum is the union of the classes' spectra, so I believe
  nothing new appears, and I have not proved it.
- **One level of memory only.** `a2`'s scalar theorem covers `J` levels; the vector version here
  is `J = 1`. The `J`-level vector case should follow by the companion-matrix trick, applied to a
  nonnegative block companion matrix, but that matrix is not stochastic in the same way and I did
  not do it.
- **Gain one is used twice** — for `ρ(A) = 1` and for the Perron vector. With gain `< 1` every
  branch is strictly inside the disc (`|λ| ≤ ρ(A) < 1`), so the statement is vacuous, which is the
  uninteresting case.
- The theorem says nothing about **signed** matrix weights; that is `a2`'s (b) and (c).

## 4. What would finish it

1. The `J`-level vector statement, by the block companion matrix.
2. The reducible bookkeeping, which is routine but unwritten.
3. The question this raises for the axiom: the exceptional class is exactly the rules that are a
   **gauge** away from a single rigid transport. A record rule of that kind carries information at
   one velocity and mixes components while doing so — it is a transport with an internal state,
   not a wave. If the axiom's formation law is ever to carry a cone, the departure has to be in
   the weights' signs or in an amplitude, and the size of that departure is what `a2`'s (b) and
   (c) measure.

## 5. Running it

```
python3 probes/work/derive/waves-need-signed-weights/w-jonathonsmac4f50-j62b1/check.py
```
from the repository root. `sympy` for the symbolic parts, `numpy` for the two grid scans in `G3`.
Under a minute.
