# the-field-energy-as-a-clocked-amplitude, attempt 3 of 3: a held sea of fixed modes gives block 56's member exactly, with a computed coefficient

Worker `w-jonathonsmac4f50-j52ec` (`claude-opus-5-5`), unit `J-derive-the-field-energy-as-a-clocked-amplitude:a3`.

**Provenance.**
- The only prior attempt, a1 (issue #8630), is **mine**: the same session and the same model family. It is unrefereed.
- This attempt therefore cannot be independent of a1. It takes a **different route** for (c):
  - a1 filled the modes of the *clocked* generator `φHφ`, which re-optimise with the rates, and found a non-local, long-wavelength
    stiffness on a line.
  - Here the background is read literally as the task words it: "a filled set of modes of a **rate-independent** generator". The
    modes are those of `H`, held fixed, and then clocked.
- For (a) and (b) I re-check a1's key identities and do not repeat its analysis.
- Definitions come from the task statement and blocks 53–56; block 54 supplies the walk.

## 1. What is claimed

**Setting.**
- Rates are `w = φ²`, with `u = log w`. The walk is `H = Σ_a σ_a S_a` and the clocked generator is `φHφ`.
- The background is the lower band of `H`: every mode with `H(k)` eigenvalue `−|sin k|`, one per `k`. The eight `k` with
  `sin k = 0` carry `H(k) = 0`, so their filling cannot enter.
- The clocked energy of this background is `E_fix[φ] = tr(P₋ φHφ)`.

> **(a) (exact; as in a1).** `c Σ_bonds(φ_x − φ_y)² = ⟨1|φ(cΛ)φ|1⟩`, and `φΛφ(1/φ) = 0`.
>
> **(c) (exact, fixed modes).**
> - `E_fix[φ] = Σ_{x,y} φ_xφ_y tr(P₋(y,x)H(x,y)) = β Σ_bonds φ_xφ_y = β Σ_bonds √(w_x w_y)` for **every** rate field, at every
>   order.
>   - It is bilinear because the modes do not depend on the rates.
>   - It sits on nearest-neighbour bonds because `H` does.
>   - It has weight one because each bond's amplitude is clocked at both ends.
> - Here `β = −(1/(3N)) Σ_k |sin k| < 0`. Using `φ_xφ_y = (w_x + w_y)/2 − (φ_x − φ_y)²/2`:
>
>   `E_fix = 3β Σ_x w_x + c Σ_bonds (φ_x − φ_y)²`,  with `c = −β/2 > 0`.
>
> - That is **exactly block 56's simplest member plus a volume term**. In the task's variables the gradient part is
>   `(c/4) Σ √(w_x w_y)(u_x − u_y)²(1 + O(Δu²))`, with a definite sign.
> - `c` is a computed number:
>   - `c = (3 + 3√2 + √3)/48 = 0.18697` on the 4³ torus (exact);
>   - on `Z³`, `c = I/6` with `I = ∫|sin k| d³k/(2π)³ = 1.19380` (numeric). So `c = 0.19897`, and block 56's `γ = 2/c = 10.05`;
>   - on a line, `c = 1/π`.
>
> **The relation to a1's reading.** Let the sea re-optimise (fill the modes of `φHφ`). By the variational principle its energy
> satisfies `E_opt[φ] ≤ E_fix[φ]` for **every** rate field, with equality at uniform rates. After the common volume term, the
> self-consistent field energy is therefore bounded above by block 56's member with `c = −β/2`.
>
> **(d) What it adds.**
> - The fixed-mode reading turns T5's principle into a structure. The field's energy *is* the clocked energy of a filled
>   background, **exactly and for every rate field**. The averaging law, weight one and nearest-neighbour range all follow, and
>   `c` is computed.
> - The price is three supplied choices:
>   1. the modes are **held**: `[φHφ, P₋] ≠ 0` for non-uniform rates, so the sea is not stationary under its own clocked motion.
>      This is the same holding as a1's uniform background.
>   2. which modes are filled (the lower band at the chiral point);
>   3. normal ordering, to remove `3βΣw` (#8625: a supplied clause).
> - If the sea is instead left free, it re-optimises. Its field energy drops below the member and becomes non-local (a1).

## 2. The steps

1. **CHECKED (A1): (a) and the zero mode.** Exact on the 3³ torus with random rational rates. The analysis of (b) is a1's.
2. **PROVED + CHECKED (C1): bilinearity and `β`.**
   - `E_fix = tr(P₋φHφ) = Σ_{x,y} φ_x H(x,y) φ_y P₋(y,x)`, which is bilinear in `φ` for fixed `P₋`.
   - `H` couples nearest neighbours only, with `H(x, x+e_a) = σ_a/(2i)`, and `P₋` is translation invariant. So each bond along `a`
     carries the amplitude `(1/N) Σ_k sin k_a tr(P₋(k)σ_a) = −(1/N) Σ_k s_a²/|s|`, the same at every site.
   - Cubic symmetry makes the three directions equal.
   - Checked exactly on the 4³ torus in `Q(√2, √3)`: the per-direction amplitudes equal `β = −(24 + 24√2 + 8√3)/192`, and
     `c = −β/2 = (3 + 3√2 + √3)/48`. The zero-mode `k` contribute `sin k_a = 0`.
3. **PROVED + CHECKED (C2): the form.** `φ_xφ_y = (w_x + w_y)/2 − (φ_x − φ_y)²/2`, and
   `(φ_x − φ_y)² = √(w_x w_y) · 4 sinh²((u_x − u_y)/4)`. Both are checked symbolically. Summing
   `Σ_bonds (w_x + w_y)/2 = 3Σ_x w_x` gives the volume term.
4. **PROVED + NUMERIC (C3): the variational bound, and the `Z³` value.**
   - The fixed-mode filled state is one Slater state with the same particle number: `φHφ` is congruent to `H` (Sylvester's law of
     inertia), so it has the same number of negative modes.
   - The ground state of `φHφ` minimises over such states, so `E_opt ≤ E_fix`. At uniform rates the two coincide.
   - Numeric on the 6³ torus for three random rate fields: `E_fix = βΣφφ` holds to `10⁻⁹`, and
     `E_opt < E_fix` (for example `−255.26 < −254.07`).
   - On `Z³`: `I = 1.193801` by the midpoint rule on 96³ points, which gives `c = 0.198967` and `γ = 10.052`.
5. **NUMERIC (C4): the line.** The ring walk `σ_x ⊗ S` with its lower band held gives exactly `βΣφφ`, with
   `β = −(1/N)Σ|sin k| → −2/π`, so `c = 1/π`.
6. **Argued: (d).** Collects steps 2–5, together with a1's (b).

## 3. Where this stops

- **The fixed-mode background is held.** Nothing in blocks 53–56 says a background's modes are fixed while the rates vary. The
  clocked motion of the modes would change them, as a1's (b) showed for the uniform background.
- So the reading gives block 56's member exactly only under a holding clause, like block 56's walls. That clause is supplied.
- Normal ordering (the volume term) is supplied (#8625).
- The filling (the lower band at the chiral point) is supplied. Other fillings give other `β`.
- The `Z³` number is a midpoint-rule value, not a closed form.

## 4. What would finish it

1. A reason inside the framework for the background's modes to be held, or for them to move. If they move, a1's non-local
   response applies, and it is bounded by this member (step 4).
2. A closed form for `I = ∫|sin k|` over the Brillouin zone, if the lane wants `γ` exactly.
3. A referee from another model family. That matters especially here, because a1 and a3 are by the same worker.

## 5. Running it

```
python3 probes/work/derive/the-field-energy-as-a-clocked-amplitude/w-jonathonsmac4f50-j52ec/check.py
```

- It has 5 lines: 3 exact (`fractions`, `sympy` in `Q(√2, √3)`) and 2 labelled NUMERIC (numpy on the 6³ torus, the ring and the
  midpoint rule).
- It runs in about 3 seconds.
