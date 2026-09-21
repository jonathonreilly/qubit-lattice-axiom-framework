# isotropic-streaming-clause, attempt 2 of 3 — the anisotropy was never about the axes

Worker `w-jonathonsmac4f50-j1e60` (`claude-opus-5`), unit `J-derive-isotropic-streaming-clause:a2`.

**Provenance.** No prior attempt existed on this problem at claim time. Block 51 is taken as the
unit states it, except that I **recompute its three sphere moments** rather than take them on
trust (they check out). Block 51 is same-family campaign work.

## 1. What is claimed

> **(a) Such rates exist.** And the cubic viscous term is **not** a consequence of hops being
> along lattice axes — it is a consequence of the rate `|s_k|` being **one-way**.
>
> **The reduction.** Write `M_kl(s) = Σ_d a(s,d) d_k d_l`. If `M(s) = m(s)·I` with `m`
> cubic-invariant, then `T_ijkl = ⟨s_i s_j m(s)⟩δ_kl`, and cubic symmetry alone gives
> `⟨s_i s_j m⟩ = (⟨m⟩/3)δ_ij`, so `T = (⟨m⟩/3)δ_ij δ_kl` — isotropic. It therefore suffices to
> make the hop second moment a multiple of the identity at each content.
>
> **Forward hops on the axes alone cannot.** At `s = e₁` the only forward axis neighbour is
> `(1,0,0)`, so `M = diag(a,0,0)`, a multiple of `I` only if `a = 0`.
>
> **Two-way axis hops can, in closed form.** Take
>
> ```
> a(s, ±e_k) = λ (1 ± κ s_k),      non-negative for every unit s when κ ≤ 1.
> ```
>
> Then exactly, and with no diagonal neighbours at all:
>
> ```
> mean displacement = 2λκ s          (∝ s, as required)
> second moment     = 2λ I           (a multiple of I, INDEPENDENT of s)
> total rate        = 6λ             (independent of s)
> ```
>
> **Forward-only rules exist too, on the 26 neighbours.** Exact rational witnesses, symmetrised
> over the stabiliser of `s` and normalised to `m = 1`:
>
> | `s` | rates | mean | `M` |
> |---|---|---|---|
> | `(1,0,0)` | `1/4` on each of `(1,±1,±1)` | `(1,0,0)` | `I` |
> | `(1,1,0)` | `1/2` on `(0,1,0)`,`(1,0,0)`; `1/4` on `(0,1,±1)`,`(1,0,±1)` | `(1,1,0)` | `I` |
> | `(1,1,1)` | `1/5` on six neighbours | `(3/5)(1,1,1)` | `I` |
>
> The `(1,0,0)` witness is the clean one: each body diagonal has `d_k² = 1` in every coordinate,
> so the second moment is `I`, and the signs cancel pairwise so the mean is along `e₁`. Generic
> directions `(3,2,1)` and `(5,1,1)` are feasible too (exact rational programming; those rates are
> not symmetric and are not reproduced in the script).

> **(b)** The two constructions differ in what they preserve. The two-way axis rule has total rate
> `6λ` at **every** content, so it keeps a single event clock. The forward-only witnesses do not —
> their total rates are `1`, `2`, `6/5` at the three directions above — so "one event per record"
> does not come for free there and the uniform product measure's stationarity must be re-argued
> rather than inherited from block 44. Under the two-way rule the capture count becomes
> **affine** in `s` (`6λ − 2λκ s·n`) rather than block 48's `|s|₁`.
>
> **(c)** Three prices: the two-way axis rule costs the reading (a record steps *backwards*
> against its content at positive rate); the forward-only rule costs the geometry (diagonal
> neighbours, so adjacency is no longer the nearest-neighbour graph the other clauses use) and the
> single event clock; keeping the present clause costs the isotropy, which is block 51's finding.

## 2. The steps

1. **CHECKED (`S1`).** `T_1111 = 1/(4√3)`, `T_1122 = 1/(8√3)`, `T_1212 = 0`; an isotropic tensor
   forces `B = T_1212 = 0` hence `T_1111 = T_1122`, which fails.
2. **PROVED + CHECKED (`S2`).** The reduction, plus **independent recomputation of block 51's
   moments** by symbolic sphere integration: `⟨|s_k|⟩ = 1/2`, `⟨s_i²|s_i|⟩ = 1/4`,
   `⟨s_i²|s_k|⟩ = 1/8` — all three agree. The cubic-invariance step is checked on the non-constant
   invariant `m = s_1⁴+s_2⁴+s_3⁴`: `⟨s_1s_2 m⟩ = 0` and `⟨s_1²m⟩ = ⟨s_3²m⟩ = 1/5`.
3. **PROVED (`S3`).** The forward-axis-only impossibility, one line at `s = e₁`.
4. **PROVED + CHECKED (`S4`).** The two-way closed form, verified symbolically in `s, λ, κ`.
5. **CHECKED (`S5`).** The three exact rational witnesses: parallel, isotropic, non-negative and
   forward, all verified in exact arithmetic.
6. **CHECKED (`S6`).** The total rates.

## 3. Where this stops

- **(a) is answered pointwise, not as a closed-form rule, in the forward-only case.** I exhibit
  exact witnesses at five directions and verify them; I do **not** give a formula `a(s,d)` valid
  for all `s`, nor prove one exists. A continuity argument is needed and I did not make it — as
  `s` crosses a plane `s·d = 0` the support changes, and whether a *continuous* forward-only rule
  exists is open.
- **(b) is barely started.** Stationarity of the uniform product measure is **not** proved for
  either construction; I only observe that the two-way rule keeps the total rate constant, which
  is a necessary bookkeeping condition, not stationarity. The capture law is stated by
  substitution, **not verified against a simulator**. The collisionless shadow is **not computed
  at all** — and since the two-way rule makes every record diffuse as well as stream, I expect the
  shadow to soften, which is exactly the kind of expectation that should be measured rather than
  asserted.
- **The two-way rule changes the physics, not just the tensor.** Its second moment is `2λI`
  regardless of `κ`, so the diffusion is isotropic *and content-independent*; the streaming is
  carried entirely by the first moment. Whether that is still an "inertial record gas" in the
  sense blocks 45–48 mean is a question about the reading, not about this algebra.
- Nothing here re-runs the executed wind-by-direction numbers, and nothing here touches the
  two-body forces that blocks 45 and 47 measured along a lattice axis only.

## 4. What would finish it

1. A closed-form forward-only rule, or a proof that no continuous one exists. The obvious ansatz
   to test is `a(s,d) ∝ (s·d)_+ w(|d|)` with shell weights chosen to make `M ∝ I`; I did not test
   whether any `(w_1,w_2,w_3)` achieves it for all `s`.
2. Stationarity of the uniform product measure under each construction, which is what (b) actually
   asks.
3. The shadow, measured with `probes/lib/inertial_wind_by_direction.py`, under the two-way rule —
   the cheapest decisive experiment here.
4. Another model family: block 51 and this attempt are the same family.

## 5. Running it

```
python3 probes/work/derive/isotropic-streaming-clause/w-jonathonsmac4f50-j1e60/check.py
```

`sympy` only; 13 checks, exact symbolic and exact rational arithmetic throughout, including the
sphere integrals. Runs in about a minute.
