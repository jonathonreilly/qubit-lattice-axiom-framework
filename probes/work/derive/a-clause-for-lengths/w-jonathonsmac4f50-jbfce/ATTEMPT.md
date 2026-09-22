# a-clause-for-lengths, attempt 1 of 3: one exact ray law for the two-function family; scale covariance keeps an algebraic length clause at ratio 1

Worker `w-jonathonsmac4f50-jbfce` (`claude-opus-5-5`), unit `J-derive-a-clause-for-lengths:a1`.

**Provenance.**
- There were no prior attempts. The definitions come from blocks 53 and 54, as the task states them.
- Block 59 (PR #8581) is a later block of the same campaign, by the same model family as me, unrefereed, and not named in the
  task. It already contains most of what this task asks:
  - T4: the two ray limits;
  - T5: an algebraic local length clause depends only on the ratio of rates, whereas a local *law* can give `l = (w̄/w)^β`;
  - an executed bending ratio of 1.966.
- I read its claim scope after forming my plan (Hamilton's equations for the family, then scale covariance).
- New here:
  - the exact ray law at **every** speed and direction, which contains block 59's two limits as special cases;
  - an independent re-derivation of T5(a) from block 53's scale covariance;
  - an independent execution of the test on a slab.

## 1. What is claimed

> **(a) The ray law (exact).** The lattice family is `E² = a(x)²m² + c(x)² Σ_j sin²k_j`: `a` times the rest energy, and
> `c = ab` times the hops. The continuum `E = a√(m² + b²k²)` is its small-`k` form. For this family,
>
> `dv_j/dt = −c² cos(2k_j) [a²m² ∂_j log a + c²S ∂_j log c]/E² + 2v_j (v·∇log c)`,  with `S = Σ sin²k`.
>
> - The pull is the energy-weighted mixture of `∇log a` (weighted by the rest share `a²m²/E²`) and `∇log c` (weighted by the hop
>   share `c²S/E²`).
> - With `a = c = w` this is block 54's law.
> - A slow body falls at `−c²∇log a`. A massless ray crossing the gradient bends at `−c²∇log c`. So bending over fall is
>   `dlog c/dlog a = 1 + dlog b/dlog a`:
>   - 1 when hops are timed like sites (lengths locked);
>   - 2 for lengths `l = ā/a`;
>   - `1 + β` for `l = (ā/a)^β`.
>
> **(b) What could play the role of `b`**, judged by block 53's premise that only ratios of rates mean anything.
> - *A rate for bonds distinct from the rate for sites:* **allowed**, as a supplied field (block 59's clause). Blocks 53–54 do not
>   force it.
> - *Block 53's scale covariance applied to bond rates:* **forces** any bond rate built from the two site rates to be
>   `√(w_x w_y) g(w_x/w_y)`. The length `√(w_x w_y)/c_b = 1/g(w_x/w_y)` then depends only on the local ratio and never on the depth
>   of the rate, so in a uniform gradient the ratio is exactly 1. This **excludes** the factor 2 by this route (block 59 T5(a)).
> - *The second-order term of block 53's law:* it fixes how sources set `u` at second order. It does not change how hops are timed,
>   so it cannot supply `b`. It is **excluded** as a mechanism.
> - So a factor other than 1 needs lengths tied to the **depth** of the rate. That takes either a law (block 59 T5(b): a cross term
>   in the field's energy, with held walls giving `l = (w̄/w)^β`) or a supplied reference rate.
>
> **(c) The executed test (numeric).** A walker with no rest energy crosses a uniform rate gradient on a 40×64 slab. After
> subtracting the free walk's own drift, its transverse displacement is 1.98 with locked lengths and 3.83 with `l = w̄/w`, a
> **ratio of 1.934**. Block 59 gets 1.966 in three dimensions.
>
> The slow-body side of the test needs an on-site rest energy, which block 54's walk does not have. With one, a slow packet's fall
> (`−c²∇log a`) is the same under both clauses.

## 2. The steps

1. **PROVED + CHECKED (A1).** Hamilton's equations: `v_j = c² sin(2k_j)/(2E)` and `k̇ = −∇E`, with
   `∇E = (a∇a m² + c∇c S)/E`.
   - `dv_j/dt = Σ_l (∂v_j/∂x_l)v_l + Σ_l (∂v_j/∂k_l)k̇_l`.
   - The terms that come from the `x`-dependence of `1/E` cancel against those that come from `∂E/∂k`.
   - What remains is `−(c² cos 2k_j/E)∂_jE + (sin 2k_j/2E)(v·∇c²)`, which is the stated law.
   - Checked symbolically for arbitrary `a(x)`, `c(x)`.
2. **CHECKED, exact (A2).** Uniform gradients: `a = (5/4)(1 + 3x/10)`, `c = (2/3)(1 − 7x/20)`. At 36 wave vectors with rational
   sines and cosines (Pythagorean), with rest energies 0, ½ and 2, Hamilton's equations agree with the closed law.
3. **PROVED + CHECKED (A3): the limits.**
   - `k → 0`: `S → 0` and `cos → 1`, so `dv/dt → −c²∇log a`.
   - `m = 0` with `k` along the direction of motion and the gradient transverse: `cos(2·0) = 1`, and the transverse `v` is 0, so the
     acceleration is `−c²∂ log c`.
   - The ratios are checked for `c = w` (ratio 1) and `c = w²/w̄` (ratio 2).
4. **PROVED + CHECKED (B1): scale covariance.**
   - If `c_b(tw) = t·c_b(w)` for all `t`, write `c_b = √(w_x w_y) · F(w_x, w_y)`. Then `F` is homogeneous of degree 0, so it is a
     function of `w_x/w_y` alone.
   - Checked symbolically: the length is independent of the depth `u`, and `c_b` scales with degree 1.
5. **NUMERIC (C1).** A 2-component walk on a 40×64 slab, open in the gradient direction and periodic along the motion; rates
   `w = e^{−0.004(x − 20)}`; a packet with `k = 0.5` and width 3; sparse `expm_multiply` to `t = 40`. The displacement of `⟨x⟩` is
   measured relative to a zero-gradient run.

## 3. Where this stops

- **(a)** is complete for the two-function family, on the lattice and in the continuum.
- **(b):** the factor 2 is not available from blocks 53–54 plus scale covariance. It needs a supplied object:
  - an independent bond field together with a law tying it to the depth of the rate, as in block 59 T5(b), with `β` free; or
  - a reference rate.

  Which one, if any, is the owner's choice.
- **(c)** is executed for the ray side only. The slow-body side needs a rest-energy clause.
- No gravitational claim is made. The comparator's factor 2 is a comparator.

## 4. What would finish it

1. A reason inside the framework for lengths to follow the depth of the rate, with `β = 1`. Later blocks (60, 64: the
   curvature member forced by blindness) propose one. That is a separate question.
2. A rest-energy clause, so the full `a = b` versus `b = 1` test can be run on one walker.
3. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/a-clause-for-lengths/w-jonathonsmac4f50-jbfce/check.py
```

- It has 5 lines: A1–B1 exact (sympy; Pythagorean points) and C1 labelled NUMERIC (scipy).
- It runs in about 3 seconds.
