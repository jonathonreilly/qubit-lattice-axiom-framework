# formation-response-kernel, attempt 6 (worker w-macbookpro90c72-jc53b, model grok-4.6)

Own plan, locked from the task and from `probes/lib/formation_levelplane.py` / block 35 (PR #8180) before reading the a2/a3 writeups in full: compute the linear response as a generating function, identify the point-source kernel with the trinomial walk on the event lattice, extract 3D decay along rays by Stirling, and classify the eight-corner average `R_8` by direction (axis vs. no-drift plane vs. body diagonal). After locking that route, the referee of a3 (`referee_w-jonathonsmac4f50-jceaa`, other model family) is used as a refereed partial: a3’s continuum Bessel off-axis and “no `1/r` / no `1/k²`” claims fail; the exact quadrant Green, the E-identity, and FDR-failure survive. This attempt proves the replacement those failures point to, with independent exact checks.

Objects: linearized sphere formation on the `L×L` level plane, `(Pf)(i,j)=(f(i,j)+f(i-1,j)+f(i,j-1))/3`, `φ(k)=(1+e^{ik_1}+e^{ik_2})/3` in the note’s sign (predecessor multiplier is `φ(-k)`). Event coordinates: level `t=x_1+x_2+x_3`, plane `(i,j)=(x_1,x_2)`. Comparator `E(k)=∑_{j=1}^3 2(1-\cos k_j)`.

## (1) The statement attempted

**Statement (PARTIAL).** For the linear formation law:

**(a)** From rest, `m_{t+1}=φ m_t + h_t` has generating function `R(k,z)=1/(1-φ(k) z)`. Static nonzero modes: `1/(1-φ)`. Zero mode: `m̄_t = t h̄`.

**(b)** Persistent source at the origin of every level: the static response on `Z^2` is supported on the forward quadrant `N^2` and equals
`G(n,m)=(3/2)\binom{n+m}{n}2^{-(n+m)}` there (0 off `N^2`). Downstream `G(n,n)∼3/(2\sqrt{π n})`. (Refereed; re-checked.)

**(c)** Replacement for `1/r`. None of the channels is an *isotropic* 3D Coulomb kernel.
- *Point source (one site, one level).* Exact kernel `T(x)=t!/(x_1! x_2! x_3!)\,3^{-t}` on `x∈N^3`, `t=x_1+x_2+x_3`, and 0 off the octant. Along the level axis `x=(n,n,n)`, with Euclidean `R=n\sqrt{3}`,
  `T(n,n,n)∼3/(2π R)`, i.e. a **directed** `1/R` with constant `3/(2π)`. Off the ray the large-deviation rate is strictly positive (exponential).
- *Eight-corner average* `R_8(k)=(1/8)∑_{ε∈{\pm1}^3} 1/(1-φ_ε(k))`, `φ_ε(k)=∑_j e^{-i ε_j k_j}/3`.
  - On a coordinate axis: `R_8(κ,0,0)=3/2` **identically** (no pole).
  - On the no-drift plane `k=(κ,-κ,0)`: `κ^2 R_8 → 3/2` and `κ^2/E → 1/2`, so `R_8 ∼ 3/E` (a `1/k^2` pole, not isotropic: the residue depends on direction).
  - Along the drift diagonal `k=(κ,κ,κ)`: `κ^2 R_8 → 0` (no `1/k^2`).
- *Persistent (line) source:* the 2D wake of (b), `1/\sqrt{r}` downstream, identically 0 upstream.

**(d)** Regression `C_s=C_0 φ^s` holds in the linear Gaussian model. Equilibrium FDR fails: `1/(1-φ)` is not a real multiple of `1/(1-|φ|^2)` whenever `φ` is not real. On `L=4`, mode `k=(π/2,0)` has `φ=(2+i)/3`, `1/(1-φ)=3(1+i)/2`, `1/(1-|φ|^2)=9/4`.

## (2) Steps

**Step 1 — generating function (PROVED; CHECKED F1).** `m_0=0`, `m_{t+1}=φ m_t+h_t`. The transform `∑_{t≥0} m_{t+1} z^t` equals `H/(1-φ z)`. Coefficients `φ^t`. Zero mode `φ=1`: `m̄_t=t h̄`.

**Step 2 — E-identity (PROVED; CHECKED F2).** Level wave `e^{i(q_1 i+q_2 j+w t)}` is a 3D wave with `k=(q_1+w,q_2+w,w)`. Then `φ(q)e^{iw}=(e^{ik_1}+e^{ik_2}+e^{ik_3})/3`, and `E=3(|1-φ e^{iw}|^2+1-|φ|^2)` identically.

**Step 3 — quadrant Green (PROVED; CHECKED F3; refereed).** Influence of `P` stays in `N^2`. On that quadrant `G=PG+δ` rearranges to `G(x)=(G(x-e_1)+G(x-e_2))/2+(3/2)δ(x)`. Pascal’s identity yields `G(n,m)=(3/2)\binom{n+m}{n}2^{-(n+m)}`. Equivalent: visits of the trinomial walk, `∑_p \binom{n+m+p}{n,m,p}3^{-(n+m+p)}`, evaluated by `∑_p \binom{k+p}{p}x^p=(1-x)^{-(k+1)}` at `x=1/3`, `k=n+m`.

**Step 4 — point source is the trinomial; directed `1/R` (PROVED; CHECKED F4).** One injection at the origin at level 0. Each step sends mass `1/3` along `+e_1,+e_2,+e_3`. After `t` steps the mass at `x` with `x_1+x_2+x_3=t` is `T(x)=t!/(x_1!x_2!x_3!)\,3^{-t}` (checked by exact iteration against multinomials through `t=8`). Along `(n,n,n)`:
`T(n,n,n)=(3n)!/(n!)^3\,27^{-n}`.
Stirling / `Γ`-limit:
```
n · T(n,n,n) → √3 / (2π).
```
The 3D Euclidean distance is `R=√(3n^2)=n√3`, so `T·R → 3/(2π)`. Algebra: `Γ(3n+1)/Γ(n+1)^3 / 27^n ∼ √3/(2π n)` by the standard `Γ(an)/Γ(n)^a` limit (CHECKED F4b,c). This is the local-CLT peak of a 3-nomial at its mean, which sits at 3D distance `t/√3` from the origin after `t=3n` steps.

**Step 5 — eight-corner classification (PROVED; CHECKED F5).** `φ_ε(κ,0,0)=(e^{-iε_1 κ}+2)/3`. Only `ε_1` enters; four copies of each sign. Then
```
1/(1-φ_+) + 1/(1-φ_-) = 3/(1-e^{-iκ}) + 3/(1-e^{iκ}) = 3,
```
because `(1-e^{iκ})+(1-e^{-iκ})=2-2\cosκ=(1-e^{iκ})(1-e^{-iκ})`. Hence `R_8(κ,0,0)=3/2` identically, not merely in the limit. On `k=(κ,-κ,0)` the four orders with `ε_1=ε_2` have vanishing in-plane drift; sympy gives `lim_{κ→0} κ^2 R_8=3/2` and `lim κ^2/E=1/2`, so `R_8∼3/E` along that ray. On `k=(κ,κ,κ)` one has `κ^2 R_8→0`: the `1/k^2` pole is directional, not isotropic.

**Step 6 — FDR (PROVED; CHECKED F6).** Linear Gaussian: `Cov(θ_t,θ_{t+s})=φ^s Var(θ_t)` (regression). Static objects `1/(1-φ)` and `1/(1-|φ|^2)` coincide (up to a real factor) only if `φ` is real. On `L=4`, `k=(π/2,0)`: `φ=(1+i+1)/3=(2+i)/3` (not `(1+i)/3`), `1-φ=(1-i)/3`, `1/(1-φ)=3(1+i)/2`, `|φ|^2=5/9`, `1/(1-|φ|^2)=9/4`. Ten of the fifteen nonzero modes have `Im φ≠0`.

## (3) Where the route stops

Linear response is solved, including the 3D point-source law a3 denied. Not done: the nonlinear sphere law’s response to a pin; a gravity-lane construction that *takes* this directed kernel as input; a remainder theorem for `T(n+a,n+b,n+c)` in the co-moving plane at scale `√n` (local CLT with explicit covariance of the multinomial); two-sided bounds converting Robbins’ inequalities into a rate for `T(n,n,n)·R - 3/(2π)`.

ASSUMED: Stirling/`Γ` asymptotics of `n!` at the scope of the `Γ(3n)/Γ(n)^3` limit (CHECKED by sympy’s `limit`, proved by the standard expansion `log Γ(n)=(n-1/2)log n - n + (1/2)log(2π)+o(1)`).

## (4) What would finish it

A local-CLT expansion `T(n+y_1√n, n+y_2√n, n+y_3√n) = 3/(2π R) · e^{-y^T Σ^{-1} y/2} (1+O(n^{-1/2}))` on `y_1+y_2+y_3=0`, with `Σ` the multinomial covariance `(1/3)I-11^T/9` restricted to that plane, giving the Gaussian profile of the directed `1/R` ray. And the same for the eight-octant average (superposition of eight directed rays).
