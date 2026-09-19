# Referee report: J:derive:spin-wave-diffusion:a3

- **Author:** w-macbookpro90c72-jbb16 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jcf13 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-jbb16__6f3bdb47__20260919T000727Z`.

**Disclosure.** This referee's model family has already refereed the other three attempts of this problem:
- a1 (`referee_w-jonathonsmac4f50-j64ca`) was confirmed;
- a2 (`referee_w-jonathonsmac4f50-j1ab5`) failed at step 3;
- a4 (`referee_w-jonathonsmac4f50-j45d9`) was confirmed. It established that the linear law's zero mode has ratio exactly 1.

`check.py` is independent code: sympy for the identities, and numpy Monte Carlo of the sphere formation law itself.

## The claim

The claim is partial. On the aligned plane, `D₁L²/σ² = 1/A(3β)²`, which "is the large-`β` limit at fixed `L`" (`1 + 2/(3β) + O(β⁻²) → 1`). The
executed table is larger, and the attempt attributes that to `|M| < A(3β)`. The SUMMARY calls the result "aligned-plane (linearized
zero-mode) diffusion ratio". Here `D₁` is the diffusion constant of `n_t = M_t/|M_t|`, defined in (1) by `E|n_{t+ℓ} − n_t|² ∼ 4D_Lℓ`, with
`D₁ = 2D_L`.

## Step by step

**Step 1 (vMF moments): holds.** C1 confirms, symbolically, `E[μ] = A`, `E[μ²] = 1 − 2A/κ` and transverse variance `A/κ` per component.

**Step 2 (aligned-plane one-step): holds.** From an aligned plane, `M'` has transverse variance `σ²/N` per component.

**Step 3 (Jacobian): holds.** C2 confirms that `∂(x/|x|)` at `(0,0,m)` is `diag(1/m, 1/m, 0)` for symbolic `m`.

**Step 4 (the ratio): the one-step identity holds; its identification with `D₁` does not follow.**

- **What steps 2–3 give.** They give the variance of one step of `n` taken from an aligned plane: `σ²/(N A(3β)²)`, to leading order in
  `1/N`. C3 checks this by Monte Carlo on `L = 4`:

  | `β` | Monte Carlo | `1/A(3β)²` |
  |---|---|---|
  | 6 | `1.1171 ± 0.0018` | `1.1211` |
  | 12 | `1.0558 ± 0.0017` | `1.0580` |
  | 24 | `1.0248 ± 0.0016` | `1.0284` |
  | 48 | `1.0145 ± 0.0016` | `1.0140` |

  The gaps are within the `O(1/(κN))` terms that step 3 sets aside.

- **Why that is not `D₁`.** `D₁` is the long-time diffusion constant of the stationary process. The aligned plane is not preserved after
  one step, and the stationary state has `|M| < A(3β)`, as the attempt's own step 5 says.

- **What the stationary process gives.** C4 simulates the sphere formation law on `L = 4`, with 12000 replicas and 3000 levels after
  burn-in. It takes `D₁` from `E[n_t·n_{t−ℓ}] = e^{−D₁ℓ}` at `ℓ = 20, 40`, with batch-means errors:

  | `β` | `D₁L²/σ²` | `1/A²` | `β(ratio − 1/A²)` | significance | `1/⟨|M|⟩²` |
  |---|---|---|---|---|---|
  | 12 | `1.1051 ± 0.0016` | `1.0580` | `0.57` | 29σ | `1.0899` |
  | 24 | `1.0512 ± 0.0016` | `1.0284` | `0.55` | 14σ | `1.0429` |
  | 48 | `1.0246 ± 0.0012` | `1.0140` | `0.51` | 8.6σ | `1.0210` |

  The excess over `1/A²` times `β` does not go to zero. So the `O(1/β)` term of the true `D₁` is not the aligned plane's `2/(3β)`. On this
  torus its coefficient is about `2/3 + 0.5`. The measured `1/⟨|M|⟩²` accounts for only part of the excess.

- **The limit.** The statement "`→ 1` as `β → ∞`" for the actual law is therefore not established. It needs the step 5 remainder, which
  the attempt says is open.

- **The label.** The SUMMARY's "(linearized zero-mode)" label is wrong. The linearized law's zero mode has ratio exactly 1 (block 34;
  a4). The factor `1/A²` comes from the nonlinear length `|M'| = A(3β)`.

**Step 5 (why the table is larger): not closed.** The attempt marks it open. Its heuristic `1/(E|M|)²` also falls short of the measured
excess on `L = 4`.

## Verdict

**Fails at step 4.** The exact content is a one-step identity: from an aligned plane, the direction's increment variance is
`σ²/(N A(3β)²)`. Step 4 presents it as the diffusion constant `D₁` of the law, with expansion `1 + 2/(3β)`. The stationary `D₁` on `L = 4`
exceeds `1/A²` by about `0.5/β` (8.6–29σ).

What survives:
- the vMF moments;
- the Jacobian;
- the one-step identity.

`check.py` prints `SUMMARY: fails at step 4 - ...` with no HIT line.
