# the-reach-three-coupling-beyond-first-order, attempt 1 of 3: completions exist; the sea sees one only through a single trace, and block 76's lengths' stiffness depends on it

Worker `w-jonathonsmac4f50-j5453` (`claude-opus-5-5`), unit `J:derive:the-reach-three-coupling-beyond-first-order:a1`.

**Provenance.**
- There were no prior attempts.
- Definitions come from:
  - block 69 (PR #8601): `H3[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], P_j}` with `P_j = S_jC_j`;
  - block 70 (#8602): the species maps `V_n`;
  - block 76 (#8611): the free sea `E_sea = Σ_{E<0} E`, its strain polarisations, and N1.2.
- All three are by the same model family as me and unrefereed.
- I reproduce block 76's W2 numbers from its own control script's conventions. I read that script to match them.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a) Completions exist, so the task's HIT condition is not met.**
> - Take any function `f` applied to the bond field, with `f(B) = B + O(B²)`. Then `H3[f(B)]` is hermitian and equals `H3[B]` at first order.
> - It is **species-blind to all orders**, because `V_n H3[E] V_n† = s_n H3[E]` holds for *every* bond field `E`. This is checked exactly on a `6³` torus with independent dyadic values on all 1944 components.
> - The linear `H3[B]` is itself such a completion.
> - The natural exponential one for stretches is `f(b) = e^b − 1`, applied bond by bond. It is rotation-covariant within the diagonal strains.
> - For general strains, rotation covariance needs a matrix function assembled at the sites. That assembly is a choice the axioms do not make.
>
> **(b) The geometry, exactly.** At uniform strain every species sees the inverse metric `(1 + E)ᵀ(1 + E)`, exactly in `E`. So a completion shows every species `(1 + f(B))ᵀ(1 + f(B))`:
> - the exponential stretch completion gives `e^{2b}`;
> - the linear one gives `(1 + b)²`;
> - they differ at second order.
>
> **(b) The sea (proved, and executed).** Two completions that agree at first order change the sea's second variation only by `tr(P_sea H″)`. For a completion applied to the bond field this is `Σ_a κ_a Σ_bonds (second-order bond field)`, where `κ_a` is the sea's uniform expectation of the bond coupling: `κ = −0.10761` per bond on `8³`.
> - **In the bond field itself** the term is local, so it shifts only the local part of the sea's second variation, never the gradient stiffness. Executed: a constant `−0.161415` per site at three wave vectors, as predicted.
> - **Where the bond value is built from a site field by averaging**, as block 76 does, the term is non-local. The gradient stiffness then changes, exactly by `−κ sin²(q/2)/(4q²)`.
>
> **Block 76's W2, recomputed** with its conventions (`8³`, `q = 2π/8` along `x`):
>
> | Mode | Linear completion (block 76's numbers) | Exponential completion |
> |---|---|---|
> | TT cross | `+0.0035` | not computed (needs a site-assembled matrix function) |
> | TT plus | `+0.0021` | `+0.0021` (unchanged: its bonds are transverse to `q`) |
> | isotropic stretch | `+0.0004` | `+0.0068` |
>
> - The isotropic stretch's change is `+0.006387` exactly, as predicted. Its local part shifts by `3κ/4`.
> - So **block 76's "the lengths' stiffness is ten to sixty times below the clocks'" depends on the completion.** With the exponential completion the isotropic stretch is only about 3.5 times below the clocks' `+0.0236`.
>
> **(c) The response and block 72.**
> - For a completion applied bond by bond, `∂⟨H3[f(B)]⟩/∂B_b = f′(B_b)K_b` exactly, where `K` is block 69's conserved current.
> - The stress entering the static balance is therefore `K` at first order (so block 72's leading-order requirement is unchanged) and `K + f″(0)BK` at second order.
> - The second-order terms of block 66's rate-dependent force density `fP` at finite strain are **not** derived here.

## 2. The steps

1. **CHECKED (A1).**
   - Block 70's maps `V_n = R_nU_n` act on `H3[E]` through `U_n` (the site signs), which turns `C_a[v]` into `D_aC_a[v]` and leaves `P_j` unchanged, and through `R_n` on `σ_a`.
   - Nothing depends on how `E` depends on `B`. So `V_nH3[E]V_n† = s_nH3[E]` for any bond field.
   - Verified exactly (dyadic arithmetic is exact in binary floating point) for all eight `n`, together with hermiticity.

2. **PROVED + CHECKED (A2).**
   - Uniform `E` has symbol `Σ_aσ_a[sin k_a + cos k_a Σ_jE_a^j sin k_j cos k_j]`.
   - At `k = πn` it vanishes, and its `q`-gradient is `D_a(δ_{aj} + E_a^j)`.
   - So `H² = |(1 + E)q|² + O(q³)`, and the inverse metric is `(1 + E)ᵀ(1 + E)` for every `n`, exactly in `E`.

3. **PROVED (B1): the sea's second variation.**
   - `d²E_sea/dε² = tr(P_sea H″) + 2Σ_{occupied, empty}|⟨m|H′|n⟩|²/(E_n − E_m)`.
   - The second term uses only `H′`, which is the same for all completions.
   - The free sea is translation-invariant, so `tr(P_sea · coupling_a[v]) = κ_a Σ_bonds v`.
   - **Checked** at `L = 8` with the isotropic stretch mode placed directly on bonds: the exponential-minus-linear difference is `−0.161415` per site at `q = (100), (001), (110)`, against the predicted `−0.161415`. The two completions' gradient parts agree.

4. **CHECKED (B2): mixing completions.** A covariant assembly of a general strain at the sites (for instance, half the mean over a bond's ends of the site-average squared) gives a second-order bond field that mixes neighbouring bonds. `κ` times that carries a `|q|²` part: `+0.0135` per `|q|²_lat` in the example.

5. **NUMERIC + EXACT IDENTITY (B3): block 76's W2.**
   - Its conventions are taken from its control script: bond value `(B(x) + B(x + e_a))/2`; second order `E″/2` from two amplitudes; local part the uniform mode's times the mean square `½`; gradient over the continuum `q²`.
   - With them the linear completion reproduces block 76's numbers to the digits quoted.
   - Under `f(v) = e^v − 1`:
     - the `y`- and `z`-bonds see an `x`-mode without averaging, so TT plus is unchanged;
     - the `x`-bonds' `v²` averages `cos²(q/2)/2`, which gives the stated `−κ sin²(q/2)/(4q²)` for the isotropic stretch.

6. **PROVED (C1).** The chain rule, bond by bond, with the response identity of block 69 T3.

## 3. Where this stops

- **(a)** is answered: completions exist, and there are many. The axioms fix none of them: neither `f`, nor, for general strains, the assembly that covariance needs.
- **(b)** The sea's gradient stiffness is completion-independent only for completions local in the bond field. Block 76's lengths' stiffness is not a number of the reading alone: its size moves by a factor of about 18 between two natural completions.
- **(c)** The rate-dependent force density `fP` of blocks 66 and 72 at finite strain is not derived.

## 4. What would finish it

1. **A principle that fixes the completion.** For example, exact covariance under relabellings up to second order, `H^c[B + dξ] = H^c[B] + i[H^c[B], G_ξ] + O(ξ²)`. This condition constrains the second-order term. Whether any local completion satisfies it is open.
2. **The TT cross mode** under a site-assembled matrix exponential.
3. **`fP`'s second-order terms** from `i[φH3[f(B)]φ, G^P_ξ]`.
4. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/the-reach-three-coupling-beyond-first-order/w-jonathonsmac4f50-j5453/check.py
```

- It has 6 lines:
  - A1 and A2 are exact (dyadic arithmetic; sympy);
  - B1–B3 are NUMERIC, each with an exact identity checked against it;
  - C1 is a proof.
- It runs in about 18 seconds.
- **No HIT line:** a completion exists, so the task's HIT condition is not met.
