# J:derive:su2-bond-links-exact-blindness-and-the-species:a3 — SU(2) links make the frame walk exactly gauge covariant; the species are a flat ℤ₂ connection, so a connection cannot serve them at first order

**Provenance.** Worker `w-macbookpro90c72-j5d78`, model `claude-opus-5-5`, one session. The claim printed no prior attempts, and there are no `a1`/`a2` directories on `ai/probes`. Definitions come from blocks 54, 62, 65, 70 and 74 (PRs #8570, #8592, #8596, #8602, #8607). The fork probe's setting is taken as stated in the task. Every clause is supplied and nothing is adopted.

## 1. Statement

**The operator.**
- `H[E, U] = ½ Σ_j {A_j, S_j^U}`, with `A_j(x) = Σ_a E_a^j(x) σ_a`.
- `(S_j^U ψ)(x) = (1/2i)[U_{x,x+e_j} ψ(x+e_j) − U_{x,x−e_j} ψ(x−e_j)]`, with `U_{y,x} = U_{x,y}† ∈ SU(2)`.
- `E = 1`, `U = 1` is block 54's walk.

**Obtained (PARTIAL; the task's HIT condition is not met):**
- **(a)** `H[E, U]` is hermitian and exactly gauge covariant: `H[g E g†, g_x U g_y†] = g H[E, U] g†` for every site-dependent `g ∈ SU(2)`. The frame's coin index turns by the SO(3) image of `g_x`.
- **(b)** The pure-gauge links `U_{x,y} = g_x g_y†` with `g = exp(−iθ·σ/2)` give, at first order, exactly block 65's twist hop `½ Σ_a C_a[d_aθ_a]`. Together with the rotated frame they give block 65's `−(i/2)[θ·σ, H]`. With the task's `exp(+iθ·σ/2)` the sign of `θ` flips.
- **(c)** Block 70's species maps are gauge transformations, `g_x = (−1)^{n·x} iσ_c`: a centre element times a half turn.
  - Species `n` of `(E, U = 1)` is species `000` of `(ρ_c E, U' = (−1)^{n_j}` on the bonds along `j)`.
  - `U'` is a flat ℤ₂ connection: every plaquette holonomy is `1`.
- **(d)** Consider a gauge-invariant, coin-blind field energy, built from `E^T E` and plaquette holonomies.
  - *At fixed links*, the served-species count of block 74 (two of eight) is unchanged.
  - *With a dynamical SU(2) connection* it is still unchanged at first order. The connection enters the relabelling identity only through plaquette curvature, and the species backgrounds are flat. The curvature the content induces is of first order in the content, so its force is of second order. The missing `2 × shear` of block 74 is of first order.

## 2. Steps

**Step 1 (PROVED; CHECKED A.hermitian).**
- `S_j^U` is hermitian. Its matrix elements are `(S_j^U)_{x,x+e} = U_{x,x+e}/(2i)` and `(S_j^U)_{x+e,x} = −U_{x+e,x}/(2i) = ((S_j^U)_{x,x+e})†`.
- `A_j` is hermitian, so `{A_j, S_j^U}` is hermitian.
- Checked for a random rational frame, random Gaussian-rational SU(2) links, and random states on the `4³` torus.

**Step 2 (PROVED; CHECKED A.su2, A.covariant, D.so3). Gauge covariance.**
- Under `ψ → gψ`, `U_{x,y} → g_x U_{x,y} g_y†`, `A → g A g†`, each hop picks up `g_x` on the left and `g_y†` on the right: `(S_j^{U'} A' ψ')(x) = g_x (S_j^U A ψ)(x)`. Hence `H' ψ' = g Hψ`.
- The exact check uses SU(2) elements with rational entries: rational points of `S³` by inverse stereographic projection. It verifies `g g† = 1`, `det g = 1`, and `g σ_b g† = Σ_a R_ab σ_a` with `R` rational, orthogonal and of determinant `1`.

**Step 3 (PROVED; CHECKED B.link, B.total). The pure-gauge link is the twist hop.**
- With `g = exp(−iθ·σ/2)`, `U_{x,x+e} = 1 + (i/2)(d_eθ)(x)·σ + O(θ²)`.
- The first-order change of `S_j^U` is the hop `¼[(d_jθ(x)·σ)ψ(x + e_j) + (d_jθ(x − e_j)·σ)ψ(x − e_j)]`.
- In the anticommutator with `σ_j`, only the component along `j` survives, since `{σ_j, v·σ} = 2v_j`. So the link term is `½ C_j[d_jθ_j]` for each `j`: block 65's scalar twist hop.
- The frame part is `g σ_j g† = σ_j + (θ × e_j)·σ + O(θ²)`, which gives `½ Σ_j {(θ × e_j)·σ, S_j}`.
- Their sum equals `−(i/2)[θ·σ, H]`, block 65 T1. Checked exactly for a random rational `θ` on the `4³` torus.
- So block 65's twist hop, which it needed to make the walk blind to local coin rotations at first order, is the first-order trace of the gauge link. Exact blindness at all orders is Step 2.

**Step 4 (PROVED; CHECKED C.gauge, C.flat, C.species). The species maps are a flat ℤ₂ connection.**
- `g_x = (−1)^{n·x} iσ_c` has `det(iσ_c) = 1`, so `g_x ∈ SU(2)`.
- It sends `σ_j → σ_c σ_j σ_c`: `+σ_j` for `j = c`, `−σ_j` otherwise. That is the half turn `ρ_c`, and the centre sign cancels in the frame.
- It sends `U = 1 → U' = g_x g_{x+e_j}† = (−1)^{n_j}`.
- Every plaquette holonomy of `U'` is `1`: the connection is flat.
- A zero mode of species `n`, `(−1)^{n·x}u`, maps to the constant spinor `iσ_c u`. That is a species-`000` zero mode of `H[ρ_c E, U']`, checked for all `n`, `c`.
- The `(−1)^{n·x}` part alone, with `c` absent, already maps species `n` of `(E, 1)` to species `000` of `(E, U')`. The half turn is what relates it to block 70's `V_n`, which maps the walk to `±` itself.
- On `Z³` every such `U'` is pure gauge. On a torus of even side it is too: `(−1)^{n·x}` is single-valued there.

**Step 5 (PROVED; CHECKED D.covariant). At fixed links the count is gauge invariant.**
- The frame's response `Θ_a^j = Re ψ† σ_a S_j^U ψ = ∂⟨H[E, U]⟩/∂E_a^j` turns as `Θ → R(g_x)Θ` (checked exactly).
- A coin-blind field energy depends on `E` through `g = E^T E`, and its derivative turns the same way. So the frame's field equations map to field equations.
- The served-species criterion is covariant as well: the balance of block 66's relabelling identity against the weight `e∇u`, per block 74. Relabellings act on labels, gauge maps on the coin, and the flat links `(−1)^{n_j}` are translation invariant.
- So by Step 4 the eight species are the eight flat ℤ₂ backgrounds of one species. The frame serves species `n` exactly when it serves species `000` in the background `(ρ_c E, (−1)^{n_j})`.
- Block 74's count therefore stands at fixed links: `000` and `111` are served, and the other six miss `2 × shear`.

**Step 6 (PROVED at the order stated; the lattice transport of links ASSUMED). A dynamical connection.**
- *The fourth equation.* With `F = F_E[g] + F_U[holonomies]` gauge invariant, stationarity in the link `U_b = e^{iε·σ/2} U_b` gives, on every bond `b` and for each `c`:

  `∂F_U/∂ε_b^c + j_b^c = 0`, where `j_b^c = ∂⟨H[E, U]⟩/∂ε_b^c`

  is the content's spin current on the bond. This is a lattice Yang–Mills-type equation sourced by the spin current.
- *The identity's new terms.* Under a relabelling the frame is transported as a frame, and the link as a connection. The covariant transport of a connection along `ξ` is `ι_ξ F + D(ι_ξ A)`: a curvature term plus a gauge transformation. The gauge part drops out of the gauge-invariant `F`.
- So block 66's identity acquires only terms of the form `(curvature) × ∂F/∂U`. On shell these are `−(curvature) × (spin current)`, a Lorentz-type force.
- *Order counting.* The species backgrounds of Step 4 are flat. The curvature induced by the content's spin current is of first order in the content, so the new term in the momentum balance is of **second** order. The frame's response `Θ` depends on `U` through `S_j^U`, so a first-order change of `U` also changes `Θ` only at second order.
- Block 74's deficit, `2 Σ d_a K_a^j` over the axes with `D_a ≠ D_j`, is **linear** in the content. So no connection term supplies it, and the count stays two of eight at first order.

**ASSUMED:**
- the lattice form of the covariant transport of links under a relabelling. Step 6 uses only its structure: curvature plus a gauge part;
- the fork probe's setting as stated in the task.

## 3. The first failing step for the HIT

The HIT asks whether, with a dynamical SU(2) connection, the nearest-neighbour frame serves all eight species. It fails at Step 6's order counting:
- the species are related by flat ℤ₂ gauge transformations (Step 4);
- the only connection terms are curvature × current;
- the shear deficit is of first order, the connection terms of second.

## 4. What would finish it

1. **Second order.** Compute the Lorentz-type term's size for a species-`n` packet. Its sign and whether it acts like a shear are open.
2. **An exact lattice relabelling for links.** Write the relabelling identity with its plaquette-curvature term exactly (the ASSUMED step), for instance for integer relabellings as site permutations with link transport.
3. **A nontrivial holonomy.** On a torus, a ℤ₂ holonomy around the torus distinguishes backgrounds that are locally flat. This would be a global, topological distinction between species rather than a local one.

## 5. Running it

```
python3 probes/work/derive/su2-bond-links-exact-blindness-and-the-species/w-macbookpro90c72-j5d78/check.py
```

The run takes about 2 s and uses Gaussian rationals throughout: Fractions only, no floats.
