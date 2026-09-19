# Referee report: J:derive:two-source-interaction:a4

- **Author:** w-macbookpro90c72-j8f4d (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jf286 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j8f4d__c60ee525__20260919T012521Z`.

**Disclosure.** This referee's model family has already refereed three other attempts of this problem:

| Attempt | Referee directory | Finding |
|---|---|---|
| a1 | `referee_w-jonathonsmac4f50-j714a` | — |
| a2 | `referee_w-jonathonsmac4f50-jc66e` | equal-time conditioning is not a persistent pin |
| a5 | `referee_w-jonathonsmac4f50-jf209` | — |

`check.py` is independent code: sympy and Fractions for the finite facts, numpy for the tori.

## The claim

The model is linear, with `φ = 1 − E/7` and `C = 1/(1 − φ²) = 49/(E(14−E))`. The attempt claims:

- **(a)** The naive fluctuation-response fails: `χ/C = 1 + φ`.
- **(b–c)** Two pins have energies `a²/(C₀ ± C_r)`, like pins are attractive when `C(r) > 0`, and the unlike energy on `L = 4` is
  `128a²/147`.
- **Step 5.** Like pins are "IR-divergent on the massless torus". This is "the massless 3D Newton signature".
- **(d)** Mass is the pinned amplitude, and superposition holds at linear order.

## Step by step

**Step 1 (kernel identities): holds.** T1 confirms `1/(1−φ²) = 49/(E(14−E)) = 7/(2E(1−E/14))`, `χ = 7/E` and `χ/C = 1+φ`.

**Step 2 (naive FDR fails): holds.** A persistent field in the dynamics gives the resolvent `χ`, not `C`.

The correct statement for this reversible PCA, derived here, is as follows. The perturbed automaton is reversible with respect to
`π_h = π · e^{h·s₀} Z(|βS₀ + h|)/Z(β|S₀|)`. So the field enters the stationary log-weight as `h(s₀ + E[s'₀ | S₀])`, and the response is
`C(1 + P) = χ`. T2 checks the identity exactly on every mode of `L = 4`.

**Step 3 (two-pin Gaussian energies): the formulas hold; the sign sentence is reversed.** T3 confirms `a²/(C₀ + C_r)` for like pins and
`a²/(C₀ − C_r)` for unlike pins.
- The displayed difference `2a²C_r/(C₀² − C_r²)` is unlike minus like.
- So the sign of `C_r` is the sign of unlike minus like. The text says like minus unlike.
- The conclusion in (1), "like is cheaper if `C(r) > 0`", is correct.

**Step 4 (L = 4): holds.** T4 gives, exactly:

| `r` | `C(0) − C(r)` |
|---|---|
| `e₁`, `e₁+e₂`, `2e₁` | `147/128` (the degeneracy the attempt reports) |
| `(1,1,1)`, `(2,1,0)`, `(2,2,0)` | `49/40` |
| `(2,2,2)` | `2401/1920` |

**Step 5 (IR of like pins): fails.**
- **`C₀` is finite.** `C(k) ~ 7/(2k²)` is integrable in 3D.
- **Tori (T5).** On mean-zero tori, `C₀(L)` for `L = 8, 16, 32, 64` is `1.2789, 1.3284, 1.3531, 1.3655`. The increments halve exactly
  (ratio `0.500`), and the extrapolation gives `1.3778`.
- **Infinite volume.** Independently, `C₀ = (7/2)(W + I₁₄) = 3.5(0.2527310 + 0.140931) = 1.3778`, where `W` is Watson's integral over 2 and
  `I₁₄ = (2π)⁻³∫1/(14−E)`.
- **Like pins have finite energy.** At `L = 64`, `a²/(C₀ + C(e₁)) = 0.633a²`, against `0.869a²` for unlike pins.
- **The only divergence is the torus zero mode.** It is not stationary on any torus of any dimension, so it is not a 3D signature. If it is
  kept, `C₀ = ∞`, and the like-pin energy is 0 for every `r`. That contradicts the attempt's own "like pins attractive when `C(r) > 0`".
- **The regularisation.** "`C₀` diverges as `m → 0` in `E(E+m)`" concerns a kernel of order `1/E²`, which is not this model's `C` (of order
  `1/E`).

**Step 6 (sphere): ASSUMED, as the attempt says.**

**What the task asks and the attempt does not supply:**
- **The 1/r coefficient.** It is `C(r) ≈ 7/(8πr)`. T6 checks `(C(r) − C(2r))·16πr/7` on `128³` along `(1,0,0)`, `(1,1,0)` and `(1,1,1)`:
  it gives `0.983–1.021`. So the like-minus-unlike energy difference is `≈ −(7/(4πC₀²))a²/r` with `C₀ = 1.3778`.
- **The requested checks on `L = 8..32`.** The attempt stops at `L = 4`.
- **Persistent pins.** The task defines a source as pinned at every level. The attempt's energies condition the unpinned stationary law at
  one time. T7 compares the two on `L = 8`, with unlike pins `±1` at 0 and `2e₁`:

  | Site | Stationary mean of the pinned recursion | Equal-time conditional mean |
  |---|---|---|
  | `−e₁` | `0.265` | `0.100` |
  | `e₂` | `0.234` | `0.084` |

  The largest difference over the torus is `0.165`. The same gap was found in a2.

## Verdict

**Fails at step 5.** Like pins are not IR-divergent in 3D. `C₀` is finite at `1.3778`. The torus zero mode would remove the like-pin
interaction altogether, not make it attractive.

What survives:
- steps 1, 2 and 4;
- step 3's formulas, with its sign sentence reversed.

Not supplied:
- the `1/r` coefficient (`7/(8πr)` in `C`);
- the checks on `L = 8..32`;
- the persistent-pin reading of a source.

`check.py` prints `SUMMARY: fails at step 5 - ...` with no HIT line.
