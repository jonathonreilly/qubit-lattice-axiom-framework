# Source-bound nonlinear stability review — 2026-10-11

**Finding:** I found no consequential mathematical defect in the complete draft or the publication version identified below. The uniform Sobolev estimate closes because the entire nonlinear collision difference is microscopic. The full five-moment correctors, residual, positivity bound and continuation argument are consistent at the stated preparation, fixed rates and supplied smooth lifetime. This is a selective independent research check, not an audit verdict or a claim of native physical dynamics.

## Exact identities and coverage

All paths in the first table are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/`.

| Source | Complete reading | SHA-256 |
|---|---:|---|
| `resume_20261011/NONLINEAR_STABILITY_DRAFT.md` | 231 lines | `90efaa08d5a2c2fefe9dc1f4114a37f32809fe169884cd6f01d1d826cc5ac1ae` |
| `worktree/docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md`, read with `git show 73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf:<path>` | 816 lines | `038e1ed6942d79720aa1dd7360d90f9fa1067016940ceb3554efeb99c21ed0c1` |
| `worktree/docs/D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md` | 326 lines | `ee06396528f616a96a236a2ba37ff246b255007ee4dda3c57ef97cdab3c381c0` |
| `worktree/scripts/d3q27_nonlinear_fluid_limit_2026_10_11.py` | 502 lines | `42428af72de054de764728f99e2f4446d1fc71cbe68e6aaaed2939032fb70a1a` |

The parent's working-tree bytes equal the specified `73a76d...` bytes. It is absent from current-main `a13caa4885f547c8d206265b031ba7649e539fd9`; the publication note correctly identifies it as a provisional branch dependency. I read the entire parent, including the kernel, all constitutive formulas, both linear proofs and quadratic moments. I did not rerun its historical runner or treat its status label as evidence.

The complete Sections 1–4 draft/publication diff is saved in `nonlinear_stability_packaging_diff.txt`, SHA-256 `429ed03b5802003399f940637b1c2a73ed56221bc4100cabe7eaf0bb296de9d2`. Its changes add definitions and regularity/justification; they do not change the corrector, residual or stability constants.

## Independent reconstruction of the delicate steps

**Collision structure and constants.** The five collision invariants annihilate every stoichiometric vector, hence `P Gamma(g,h)=0` for arbitrary fields, not just equilibria or the tested solution. The invariant sum identity gives `Gamma(U,U)=B(U^2/2)` with the sign and factor in the draft. Positive weights make the kernel the same for every strictly positive rate family. The parent's rectangle and axial-exchange argument supplies exactly five invariants; the independently reconstructed unit-rate `B+P` is also invertible.

For the Fourier shell with `|k|_infinity=n`, its cardinality is `24n^2+2` and `|k|>=n`. Thus its contribution is bounded by `26 n^(2-2s)` and the integral comparison gives the displayed bound, strictly below 36 at and above `s=3`. With normalized torus measure, no additional volume factor is missing. Splitting the product Fourier weight into its two convolution terms gives `2 * 6 * 2^(s-1)=6*2^s`. The per-reaction vector norm is at most `2/sqrt(m)`; four component products, their `1/2`, and the two component-weight bounds give exactly `4 C_s q_r/m^(3/2)`. The stated `E` and `G_s` are conservative valid constants.

**Full moments and residual.** The coordinates `H(r,J,E)` have precisely those five moments. `U` has energy moment zero, and `PTU=0` uses both that fact and `div j=0`. The quadratic microscopic stress is `j tensor j-|j|^2 I/3`, and its energy flux is `-(2/3)rho j`; the linear part contributes `-2nu D(j)` and `+(20/147) grad rho`. Consequently:

- Mass compatibility is `rho_t+div J1=0`.
- Momentum compatibility requires the entire `E1=3pi+|j|^2-mean(|j|^2)`. Its gradient cancels the trace-removal term and supplies the fluid pressure.
- Energy compatibility is `(5/3) div J1-(2/3)div(rho j)+(20/147)Delta rho=0`, using `(5/3)(4/49)=20/147` and the scalar coefficient `2/5`.

The spatial mean subtractions preserve these local equations while fixing the integrated corrector moments. `P Gamma(U,w)=0` then gives solvability of all 27 components for `z`, rather than merely the Leray-projected momentum equation. Direct expansion of the quadratic collision term gives, after the negative and zero powers cancel,

`delta [w_t+Tz-2Gamma(U,z)-Gamma(w,w)]`
`+ delta^2 [z_t-2Gamma(w,z)] - delta^3 Gamma(z,z)`.

There is no missing quadratic or cubic residual term.

**Uniform energy estimate.** Write `r=||e||_s`, `q=||Qe||_s`, and `A=G_s(2K0+1)`. On the bootstrap ball, the only singular nonlinear contribution is bounded by `A q r/delta`. The exact square inequality

`A q r/delta <= lambda q^2/(2delta^2)+A^2 r^2/(2lambda)`

leaves `(1/2)(r^2)' <= a0 r^2+delta S0 r` with **the displayed** `a0=A^2/(2lambda)`. Dividing through the regularized norm yields exponent `a0 t`, not `2a0 t`. The bound `delta C0<=1/2` starts strictly inside and prevents exit from the radius-one ball. The result does not assume the nonlinear kinetic semigroup itself is contractive; only the linear part is.

**Energy justification and continuation.** For each fixed delta, the finite Fourier projections commute with streaming and `B`. Applying them to the actual mild solution, rather than to a different nonlinear Galerkin problem, gives a finite differentiable energy identity. On a compact local interval, the projections of the solution and its continuous `H^s` forcing converge uniformly in `H^s`. The bounded collision matrix and the forcing terms therefore pass to the integrated identity; the streaming contribution is already zero. No hidden `H^(s+1)` hypothesis on the kinetic initial family is required.

At a finite proposed maximal time, the established `H^s` bound makes the fixed-delta nonlinear forcing bounded and Bochner integrable. In the mild formula, strong continuity of the contraction semigroup plus dominated convergence handles the earlier-time integral, and its remaining time tail is bounded by its length times the forcing bound. An `H^s` endpoint limit follows and the local Lipschitz/Picard construction restarts there. This supplies actual continuation to L. Finally the equation is continuous in `H^(s-1)`, giving the stated time regularity.

**Positivity.** The bootstrap gives `||g_delta||_s<=K0+1`. Therefore `delta |g_delta,v(x)|<=delta E(K0+1)<=1/2`, so `f_delta,v>=M_v/2` for the continuous spatial representatives throughout the interval, including the initial datum. This argument needs neither an unproved entropy inequality nor an extra global positivity theorem.

## Publication additions

The added population equation has the correct scaling after `f=M(1+delta g)`. The geometric nine-reaction definition agrees with the collision enumeration. The explicit `PTU=0`, moment definitions and provisional-parent identification close useful presentation gaps without adding an unsupported premise.

The pressure equation has the correct sign: taking divergence of the incompressible momentum equation gives `-Delta pi=partial_a partial_b(j_a j_b)`. Its mean-zero Fourier multiplier is order zero. Under the published sufficient hypotheses, products give

`pi in C H^(s+4) intersect C^1 H^(s+2) intersect C^2 H^s`.

Counting the derivatives in the actual definitions then yields `w in C H^(s+3)`, `w_t in C H^(s+1)`, `z in C H^(s+2)` and

`z_t=R[2Gamma(U_t,w)+2Gamma(U,w_t)-U_tt-Tw_t] in C H^s`.

Thus `K0,S0` are finite and all residual terms are continuous in the norm used by the proof. No global three-dimensional fluid existence assertion is being smuggled into this hypothesis. The note's prepared, fixed-lifetime convergence and physical-scope boundaries are appropriate.

## Independent finite evidence and primary-runner coverage

I wrote `nonlinear_stability_review_checks.py` before reading the primary runner. It uses only the Python standard library and no repository imports. It independently enumerates four-element velocity subsets and their three pairings; checks all 729 coordinate-basis bilinear conservation pairs, all 15 kernel polarization pairs and all ten slow quadratic field coefficients; solves the full rational 27-dimensional heat and off-diagonal Poisson systems; and derives the diagonal isotropy equation from a computed rational Krylov plane. The derived outputs are:

`288 reactions; 9 axial; chi=40/441; mu_off=67/1083;`
`536 alpha^2+4579 alpha-22183=0; nu=67/361; D=4/49; advection=2/5`.

It rejects unit-rate isotropy and a reversed quadratic collision sign. A separate periodic shear `j=(sin y+cos y,0,0)` at `y=0` gives the **computed** momentum defect `-2/3` when the `|j|^2` pressure correction is omitted, and zero after restoring it. The script is not an analytic convergence proof.

After that independent check, I read all 502 lines of the primary runner and replayed it successfully. Its exact number field represents the supplied positive root and verifies all 64 responses of eight complete stress/heat sources; its candidate Krylov inverses are checked in every velocity component and against every invariant. Its Fourier/time jets are obtained from an explicit advected-shear/thermal solution, rather than defined by the kinetic hierarchy they subsequently test. It evaluates the actual nonlinear operator at three rational deltas, with 77 nonzero Fourier modes, and rejects omitted pressure, incorrect thermal coefficient and omitted `Gamma(w,w)` controls.

The runner's constitutive and residual checks have different scopes. The constitutive check uses `alpha_*`; the residual fixture uses `alpha=1`. This is valid for the displayed shear, whose strain is off-diagonal and whose relevant coefficients are independent of the axial rate. The publication note says so explicitly. This example does not test arbitrary tuned nonlinear flows, prove Sobolev estimates, or integrate the kinetic equation in time.

**Independence limit:** both implementations use the same declared finite model, and their four-subset enumeration and Krylov ideas overlap. My heat/off-diagonal solves use full rational elimination; my isotropy polynomial comes from rational affine blocks, while the author's tuned check operates directly in `Q(alpha_*)`. The analytic energy reconstruction necessarily uses the same microscopic orthogonality/Young mechanism. This is independently written/checkable evidence, not an independent mathematical model or a different proof of every parent theorem. Expected constants were known from the draft; none were fitted into a response computation. Replaying the author's runner is explicitly author-evidence replay.

| External evidence file in `resume_20261011/` | SHA-256 |
|---|---|
| `nonlinear_stability_review_checks.py` | `80454e196faf6753cb7557ffce4b48588e520e7665a7b5563266db6335e94f5a` |
| `nonlinear_stability_review_checks.log` | `0075cbfcb89a4f4371e220a8e39449c9825443f8235e2dbbd97fe7957c11ef37` |
| `nonlinear_stability_author_replay.log` | `8f75ebe801cd3f92be9fc322700eb9a3d71aec3bfbed08444189923249eb7832` |

Both executed scripts exited zero; the author replay took about 28 seconds and reported its final source hash. No external paper, empirical interpretation, finite-particle/mesh extension, quantum composition, global fluid regularity, or long-time bound was newly verified. The earlier opportunities report is a distinct source-map task, not evidence for this theorem. No repository source, prompt, model setting, commit or PR was changed by this review.

## Narrow definition refresh

The final note now has 327 lines and SHA-256 `c81c0029fb70d1cea0ecf41ee893caf357747bcda138af5d1bef5ed5848a114a`. Its sole change from the reviewed `ee063965...` bytes is to define `D(j)=(grad j+grad j^T)/2-(div j)I/3` immediately before the microscopic flux list. Reversing that exact two-line replacement reproduces the previous complete source hash. The definition is the trace-free symmetric strain used by the parent and the reviewed flux calculation, so it changes no argument or estimate. The primary runner remains byte-identical at `42428af72...`; no proof reread or runner replay was needed for this definition-only change. Original review identities above are preserved.
