# kernel-normalization-in-3plus1, attempt 3 (worker w-macbookpro90c72-j2171, model grok-4.6)

Independent route, locked before any prior attempt on this problem: expand the vMF one-step map of the transverse field to cubic order about the aligned configuration, close at Gaussian order on the linear covariance, and read the infrared ratio of `S(k)(1-|φ|^2)/σ²` from the resulting multiplier `K(k)`. (No prior `probes/work/derive/kernel-normalization-in-3plus1/` artifacts were present in this worktree.)

Definitions from `probes/lib/formation_levelplane.py` and block 35 (PR #8180): backward 3+1 level-order formation, `n=4` predecessors (the site and its three backward neighbours), sphere menu a vMF draw about `S/|S|` with concentration `β|S|`, `φ(k)=(1+∑_j e^{-i k_j})/4` (predecessor multiplier; the note’s `e^{+ik}` is `φ(-k)`), linear kernel `σ²/(1-|φ|²)` with `σ²=A(nβ)/(nβ)`, `A(κ)=coth κ - 1/κ`. The executed first look (this worktree’s `X:formation-3plus1-sphere-memory` log) is `|m|=0.9242`, low-`k` ratio `0.9719` at `β=6`, `L=32`.

## (1) The statement attempted

**Statement (PARTIAL).** Let `θ∈R²` be the lab-frame transverse components of the unit-vector record about `e_z`. Write `Q(x)=∑_{α=1}^n |θ(x-δ_α)|²` and `(Pθ)(x)=(1/n)∑_α θ(x-δ_α)`, so `widehat{Pθ}(k)=φ(k)widehat{θ}(k)`. Truncate the vMF conditional mean at cubic order in `θ` and at `O(1/β)` in the concentration, using `A(κ)=1-1/κ` (the remainder `2/(e^{2κ}-1)` is exponentially small). Close the cubic map at Gaussian order on a translation-invariant isotropic two-component covariance `C`, and insert the linear covariance `S_{\mathrm{lin}}(k)=σ²/(1-|φ(k)|²)` off the zero mode.

Then the effective one-step multiplier is exactly proportional to `φ`:

```
K(k) = g φ(k),
g = 1 - 1/(n β) + σ² (1 - V^{-1})     (finite torus, V=L^3)
g = 1 - 1/(n² β²) + 2 / (n β (e^{2 n β}-1))     (V=∞).
```

In particular, for `n=4` in infinite volume, `1-g = 1/(16 β²) - 1/(2 β (e^{8β}-1))`: there is **no power-law `O(1/β)` term**. The mean-map contribution to

```
R(k) := S(k) (1-|φ(k)|²) / σ²
```

is therefore `1+O(1/β²)` at every fixed `k≠0` as `β→∞`, and the infrared stiffness ratio obtained by stripping the `O(1/β²)` Goldstone mass is `1+O(1/β²)`. The return sum `G_3=(2π)^{-3}∫ 1/(1-|φ|²)` **does not enter** this truncation. The suggested leading correction `R(k→0)=1-a/β+O(1/β²)` with `a` built from `|m|²` and `G_3` cannot arise from cubic Wick closure of the mean map.

(The identity `K=gφ` is a consequence of A3 symmetry of the predecessor tetrahedron, not of a further approximation: every pair of predecessors is equivalent under an automorphism of `1-|φ|²`, so the Hartree kernel cannot acquire a `k`-dependent form factor relative to `φ`.)

## (2) Steps

**Step 1 — vMF moments (PROVED; CHECKED T1).** Density `∝ e^{κ u·s}` on `S²` has partition function `Z=4π sinh(κ)/κ`. Then `E[s]=A(κ) u` with `A=∂_κ log Z=coth κ-1/κ`; `E[(s·u)²]=Z''/Z=1-2A/κ`; each lab-frame transverse component in the `u`-frame has variance `A/κ`. Exact identity `A(x)=1-1/x+2/(e^{2x}-1)` (from `coth x=(e^{2x}+1)/(e^{2x}-1)`). The power-law large-`κ` truncation is `A=1-1/κ`; the error is `O(e^{-2κ})`.

**Step 2 — `1-|φ|²` is the A3 root cosine (PROVED; CHECKED T2).** Expanding `|1+∑_j e^{-ik_j}|²/16` gives

```
1-|φ(k)|² = 3/4 - (1/8) [cos k_1 + cos k_2 + cos k_3 + cos(k_1-k_2) + cos(k_1-k_3) + cos(k_2-k_3)].
```

The six arguments are the positive roots of A3 in the backward coordinates. Consequently `1-|φ|²` (and any scalar function of it) is invariant under the Weyl group of A3.

**Step 3 — finite-torus return sum (CHECKED T3).** On `L=4`, `k_j=n_j π/2`, each cosine is in `{1,0,-1}`, and `G_4 := V^{-1} ∑_{k≠0} 1/(1-|φ|²) = 1913/1344` exactly (`V=64`, 63 nonzero modes).

**Step 4 — `e_1` and `e_1-e_2` are in one A3 orbit (PROVED; CHECKED T4).** The integer matrices with entries in `{-1,0,1}` and `|det|=1` that permute the signed A3 roots form a group of order 48 (`W(A3)≅S_4` of order 24, times inversion `k↦-k`). Four of them send `e_1` to `e_1-e_2`; one is

```
M = [[1,0,0], [-1,-1,-1], [0,0,1]],    M e_1 = (1,-1,0).
```

If `f(k)=1-|φ(k)|²` then `f(M^T k)=f(k)`, so the Green function `C(x)=V^{-1}∑_k S(k) e^{ik·x}` with `S` a function of `f` satisfies `C(Mx)=C(x)`. In particular `C(e_1)=C(e_1-e_2)`.

**Step 5 — tetrahedron gram is `c I + d J`; hence `H(k)=C_v φ(k)` (PROVED; CHECKED T5).** The four predecessor offsets `{0,e_1,e_2,e_3}` have six pairwise differences, all A3-root vectors. Step 4 puts them in one orbit, so `C(δ_α-δ_β)=C(0)` on the diagonal and a single off-diagonal value `C_1` off it. The exchange sum in the Wick contraction of `Q·Pθ` is then

```
H(k) := V^{-1} ∑_p φ(-p) φ(p+k) S(p) = Γ φ(k),
```

with `Γ=(C(0)+(n-1)C_1)/n`. For `S=σ²/(1-|φ|²)` off zero one has the elementary identity `|φ|²/(1-|φ|²)=1/(1-|φ|²)-1`, so `Γ=C_v:=V^{-1}∑_k |φ|² S(k)=σ²(G_V-1+V^{-1})`. On `L=4` with `σ²=1` this is exact in `Q(i)`: `C(e_1)=C(e_1-e_2)=149/1344`, `C_v=295/672`, and `H(k)=C_v φ(k)` on every tested mode (including `k=0` and a generic `(3,1,2)`).

**Step 6 — cubic jet of the mean map (PROVED; CHECKED T6).** Lab-frame `E[s_⊥'|S]=A(β|S|) S_⊥/|S|`. With `A=1-1/κ` and `|S|=n-Q/2+|S_⊥|²/(2n)+O(θ^4)`,

```
E[θ'] = [1 - 1/(nβ)] Pθ + (Q/(2n)) Pθ - (1/2) |Pθ|² Pθ + O(θ^5, θ³/β).
```

Checked on the two-site slice `θ_0=(ε,0)`, `θ_1=(δ,0)`, others aligned: the degree-`≤3` jet in `(ε,δ)` together with the `O(1/β)` linear term matches the polynomial; the discarded remainder is `O(θ^4)` and `O(θ³/β)` (the latter is `O(β^{-2})` under the spin-wave counting `θ=O(β^{-1/2})`).

**Step 7 — Wick closure produces `K=g φ` (PROVED from 5–6; CHECKED T5, T7).** The linear piece contributes `[1-1/(nβ)]φ`. The tadpole of `Q Pθ` contributes `C(0) φ`. The tadpole of `|Pθ|² Pθ` contributes `-2 C_v φ`. The exchange of `Q Pθ` is exactly `H(k)=C_v φ(k)` by Step 5. Altogether

```
K(k) = [1 - 1/(nβ) + C(0) - C_v] φ(k).
```

On `S_{\mathrm{lin}}`, `C(0)-C_v=σ²(1-V^{-1})`, hence `K=gφ` with the `g` of the statement. Goldstone at this order: `g-1=O(1/β²)`, not `O(1/β)`.

**Step 8 — no `O(1/β)` mean-map stiffness (PROVED; CHECKED T7).** Infinite-volume identity (exact, not truncated)

```
g = 1 - 1/(n² β²) + 2/(n β (e^{2nβ}-1)).
```

For `n=4`, `1-g=1/(16β²)-1/(2β(e^{8β}-1))`. The second term satisfies `β e^{8β}(1-g-1/(16β²))→-1/2`, so it is `O(e^{-8β}/β)`, smaller than every power of `1/β`. The first power-law correction to `g` is `O(1/β²)`. Therefore:

- at fixed `k≠0`, `|K(k)|²=g²|φ(k)|²` and `R_{\mathrm{mean}}(k)=(1-|φ|²)/(1-g²|φ|²)=1+O(1/β²)`;
- `k→0` at finite `β` sees a Goldstone mass `1-g²=O(1/β²)`, so `R(k)∼k²/(k²+m²)→0`, an artefact of not taking `β→∞` first;
- the stiffness ratio (equivalently `K(k)/g`, or `k→0` after `β→∞`) is identically `1` at this order.

`G_3` cancels in `C(0)-C_v` and never appears in `g`.

## (3) Where the route stops

The cubic-Gaussian **mean map** is solved. It does not produce a nontrivial `a` involving `G_3` or `|m|²`.

What this truncation does *not* contain:

1. The innovation variance `⟨A(β|S|)/(β|S|)⟩` relative to `σ²=A(nβ)/(nβ)`. Under the same Gaussian, `⟨|S|⟩=n-nσ²(1-V^{-1})`, so `⟨1/(β|S|)⟩=1/(nβ)+O(1/β²)` and `⟨A/κ⟩/σ²=1+O(1/β)` **greater than 1** (wrong sign versus the executed ratio `0.97<1` at `β=6`). A k-independent noise factor cannot make `R` dip in the infrared and sit near 1 in the ultraviolet, which is the executed shell pattern.

2. Expansion about the magnetized saddle `m=A(nβ m)` rather than about the aligned configuration. Mean-field self-consistency already makes the linear gain equal to 1; the cubic A3 argument still forces `K∝φ`.

3. Non-Gaussian four-point vertices, `O(θ^5)`, and the `O(θ³/β)` terms dropped in Step 6. Those are `O(1/β²)` in the spin-wave counting and cannot supply a leading `1/β`.

4. The kinematic identification `R=(1-σ² G_V)/A(nβ)` (spin-wave plateau over the aligned Langevin factor). At the executed point `β=6`, `L=32`, `σ²=A(24)/24`, `G_{32}=1.74726448…`, this number is `0.9707` against the log’s low-`k` ratio `0.9719`. It **does** involve `G_3` and the plateau, but it is not a consequence of the cubic-Gaussian map; it is listed under (4), not claimed.

ASSUMED throughout: the linearized field’s two-point controls the Wick contraction (the route’s Gaussian closure); records remain in the ordered phase so that `A=1-1/κ` is the right large-`κ` truncation.

## (4) What would finish it

A derivation of the **noise / kinematic** factor that survives after `K=gφ` has been used, producing an explicit `a` with `G_3` in it, or a proof that no such `O(1/β)` exists in the full (untruncated) law. The candidate `a=(G_3-1)/n` (infinite-volume limit of `1-R=σ²(G_V-1)/A(nβ)+O(σ⁴)`) matches the one executed low-`k` shell to three digits and is the natural object to confirm or kill against `formation_levelplane.py` at `β=3,6,12,24` on a lattice large enough that `2π/L` is not mass-contaminated by `1-g²`. That comparison is a computation, not this attempt’s HIT.

Finite exact numbers used above, all in `check.py`: `G_4=1913/1344`, `C(e_1)=149/1344`, `C_v=295/672` on `L=4`; 48 automorphisms; `g=1-1/(16β²)+2/(4β(e^{8β}-1))`.
