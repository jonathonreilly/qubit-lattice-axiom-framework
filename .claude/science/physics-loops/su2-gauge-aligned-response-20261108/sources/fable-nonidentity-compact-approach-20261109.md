# Fable 5.2 approach consultation: nonidentity compact control

Requested tool-free approach advice, not a mathematical certification or
audit. The call used local Claude CLI 2.1.321, requested model `fable` and
`--effort max`, and observed `claude-fable-5-2` in its initialization.
Session: `efe9a75d-fbca-4170-b7b7-71ec73ebeb3e`. Started
2026-11-10 03:14:25 UTC; successful final result observed before the owned
35-minute deadline. No tool, browser or MCP access was enabled. Stdin was
closed; prompt, public final answer, launch metadata and full local stream
are retained under `logs/su2-nonidentity-compact-20261109/`.
Only public answer text is reproduced below; internal reasoning is not an
artifact of this record.

The prompt supplied five COMPLETE existing texts and an explicitly
unproved candidate route, including questions about terminal forcing,
regional tangent compensation, broken mean-zero symmetry, frozen centers
and possible source-power losses. It did not supply any new author proof,
new Gaussian producer, new primary, or the independent checker report.
It did not supply the abstract density-forest proof. Thus shared route
content limits independence, and the advice is not a check of the new files.
The host checker froze its derivation before any candidate or Fable advice,
then completed its candidate verdict before this advice was shared.

## Input identities

| Existing source under this pack | SHA-256 |
|---|---|
| parts/marginal-normalized-regional-coercivity.md | bd3fa8b5eb989c7718ad5d760a913e33166f3e9edcf52b9f17f82cbd809ca255 |
| parts/marginal-regional-moments-and-ratios.md | b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f |
| parts/marginal-nonlinear-chart-estimates.md | b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7 |
| parts/marginal-source-marked-compact-decomposition.md | 4a30c12ef9c58eaf3d6ca1c82bab94137f088ee59cba73304fe30da9e04dcdd3 |
| parts/marginal-connected-density-expansion.md | 79d6f2d98f058180d98f576b1840681a42e504186e1be4975bbbaf47a5121d98 |

Prompt SHA-256: `ed5495b0772682c192e08a21a0ab8959985cba275393915811d00203e54d640a`. Public final SHA-256: `041c9154dd9dd655e3fcd779a7c50ba00562ccd514d48e09bf7bf9cbabe1d9d6`.

## Supervising disposition

The advice supports the proposed complete-energy mode and factorwise
compensation route. Those implications were separately proved and checked
in the new files; its affirmative wording does not supply their evidence.
All its implementation conditions are explicit there: a common right-tangent
frame, the actual u-dependent Haar mode, one frozen global center through the
regional tower, full surviving normalizers, and no exact coordinate mean zero.
The exact shifted minimum appears in the Gaussian prefactor.

Its compact-forest conclusion is conditional because two required producer/
forest texts were outside its read set. The new Gaussian producer and the
full fixed-reference forest were separately read and checked by the host
checker, whose report gives that scope. We do not call the Fable consultation
a producer audit.

Its source-power caution agrees with the published candidate's actual
bounds: C(epsilon^2+u^-1) for the quotient fourth cumulant and the retained
C(1+epsilon sqrt(u)) original-orbit allowance. Neither is claimed optimal.
The stronger-cumulant integration-by-parts lemma and proposed tree-level
asymptotics in the advice are NOT imported as proved statements. Its own
scaling table distinguishes C3 from C2 observables; the opening assertion
that the true orders are unchanged is stronger than the proof supplied.
A regularity-specific compact integration-by-parts argument would be a
separate research task. The current theorem needs no such strengthening.

Gauge-orbit extension, strict terminal-parameter locality of activities and
probability of the small-background class are likewise suggestions, not
new theorem clauses. The current conditional-density corollary already
requires the restored J terminal values to lie in the small neighborhood
and uses the restored law's own mode. The next principal consumer remains
the actual third-transition geometry and rough-terminal integration class.

## Complete public answer (verbatim)

Advice from the five texts only, with no tools; this is reasoning, not certification.

## Verdict

- **Background theorem: yes.** Your candidate route closes and I found no defect in it: unique Haar-energy mode `a*(V)`, compact coercivity around it, and exact regional compensation.
- **Regional moments, buffered ratios, source-marked decomposition: yes.** They transport verbatim in the shifted frame, with no extensive comparison.
- **Compact-versus-chart expansion (D5)–(D10): conditional.** It depends on `marginal-frozen-gaussian-producers.md` and `zero-shift-marked-density-forest.md`, which were not among the five texts.
- **Chart response (D11)–(D16): not as written.** The existing cut method gives `C(eps^2 + 1/u)` for the quotient fourth cumulant, as you guessed. For the orbit third cumulant it gives `C(1 + eps*sqrt(u))`, which is unbounded at fixed `eps`. The true orders are unchanged (`1/u` and `1`), but recovering them needs one new lemma.

## Route: one global compensated normal form

Work in the frame `a_e = a*_e q_e`, with `b(q) = Im q`, `beta_e = 1 - w(q_e)`, and `T_x` the owned sum of `beta_e`.

**Mode.** With `H` the identity Hessian (9) of the regional-coercivity note, solve in logs:

```
x = -H^{-1}[ f(V) + N(x;V) ],    f(V) = -kappa Q1^T Im(V_O),    N(0;V) = 0
```

- `f` is exact: non-terminal factors have zero differential at identity, and `<I, dM> = 0`.
- Use the `alpha = 0` block-sup norm; the Neumann-series bound `A` already covers it.
- The forcing is everywhere but `|f|_inf <= B eps`, and (13) holds with the same `K(s + eps)`.
- Result: `sup_e |log a*_e| <= 2AB eps`, with no decay, and `x* = kappa H^{-1} Q1^T Im(V_O) + O(eps^2)`.

**Coercivity.** (14)–(15) go through with `V_c` as one more frozen slot. The only inputs are the `kappa|V_c - I|` term of (5) and the mixed hidden/output third-derivative rows of the chart note's (7), (9).

**Compensated factors.** Let `S_f` be all hidden readers of `f`, interior and exterior.

```
l_{f,e} = d/dx h_f(a* exp(i x.sigma), V) at x = 0,      sum_{f reads e} l_{f,e} = 0
g_f(q)  = h_f(a*q,V) - h_f(a*,V) - sum_{e in S_f} l_{f,e}.Im(q_e)
|g_f(q) - h_f(q,I)| <= K0 eps sum_{e in S_f} d(q_e,I)^2      (all compact q, all u >= 1)
sum_f g_f(q) = Ehat_V(a*q) - Ehat_V(a*) =: Ghat(q)
```

**Regional law.** For any cell set `A`, collar `B = N_1(A)\A`, and any compact exterior:

```
law(q_A | q_ext)  ∝  exp(-u G_A) dHaar,     G_A = sum_{f in sel(A)} g_f        (exact)
(c_J - 2 D K0 eps) T_A - (K_E + 2 D K0 eps) T_B  <=  G_A  <=  (K_E + K_r + 2 D K0 eps)(T_A + T_B)
```

- Exactness holds because every reader of an interior link is selected, so interior linear terms cancel; exterior linear terms are constants.
- The inequalities are (7), (8) of the moments note and (3), plus the per-factor error.
- The moments note (9)–(32) and the source-marked note (M2)–(M7), (S1)–(S24) use only these two inequalities, positive weights, Haar invariance and the cap. They hold with `c_J -> c_J/2` and no `H(kappa u)^k` left to cancel.

**Chart.** Center the cube at the mode, `q_e = exp(i z_e.sigma)`:

```
S_V(z) = u Ghat(exp(i z.sigma)) - sum_e log j(z_e)
grad S_V(0) = 0,    D^2 S_V(0) = u H_V + (2/3) Id,    ||H_V - H||_row <= C eps
```

Zero shift is exact because `j` is even and `a*` is the Haar mode of the complete energy.

## Hard points

1. **Uniform `u`, zero means: passes.** Off the cap only (5) is used. One caution: k-th derivatives of `u*Phi_u` are `O(u^k)` near `M = 0`, so any globally differentiated source has a polynomial-in-`u` sup norm.
2. **Stationarity and compensation: passes, on three conditions.**
   - `l_{f,e}` and `Im(q_e)` use the same right-multiplication frame.
   - `a*` is the mode of the complete energy at the actual `u`; the leading-energy minimizer leaves an `O(eps)` linear term in `S`.
   - Compensate once with the global mode and never re-center regionally inside the tower.
3. **Moments without symmetry: passes.** (13)–(18) hold on the product cube since the cap sits inside it when `(pi/2) d0 < p`. That gives `||z_i||_s <= C_s/sqrt(u)` with no centering; `E z_i = 0` is lost and not needed.
4. **Sources and orbit term: passes.** `M1,c` is root-fixed-orbit invariant for any `V`, so the scores `A_c = kappa u <V_c i v.sigma, M1,c>` are quotient functions and (23), (D15) hold verbatim.
   - Free regression test: block-constant terminal gauge covariance gives `a*(V^g) = a*(V)^g`. For pure gauge `V = I^g`, every `l_{f,e}` must vanish and `g_f(q) = h_f(Ad q, I)`.
5. **Frozen center: correct and sufficient.** The compact cumulants are intrinsic functions of `V`; the chart at base `V` is only a proof device on a fixed domain. A bound uniform over the ball integrates to finite differences.
   - Not covered: strict `V`-locality of activities. The mode map is exponentially local, `|D_c a*_e| <= C exp(-alpha d(e,c))`, but turning that into local activities is unbuilt.
6. **Scaling: see next section.**

## Scaling and the missing lemma

At the mode, `DF(a*) = D^2 F(I)[x*] + O(eps^2)` is generically nonzero. Split each source as `Y = Y(a*) + l_Y.b + Ytilde`.

| Term | Existing cut method, fixed `eps` | Tree-level order | With the lemma |
|---|---|---|---|
| `kappa4(f,g,A_c,A_d)` | `eps^2 + eps/sqrt(u) + 1/u` | `1/u` | `1/u` for C3 sources; `1/u + eps/sqrt(u)` for C2 |
| `kappa3(C_FG,A_c,A_d)` | `1 + eps*sqrt(u)` | `1` | `1` |

The cut bound cannot see that Gaussian cumulants of linear functions vanish. It is sharp only when at most two legs carry a linear part. Tree-level cross-checks:

```
kappa4 -> (1/u) D_c D_d <grad F, C_V grad G>(a*(V)),      kappa3 -> D_c D_d [C_FG(a*(V))]
```

**Repair: integration by parts on the compact group.** There is no boundary term and no Jacobian. Let `X_i` be the left-invariant derivative along `a_e -> a_e exp(i t sigma_k)` and `C_V = H_V^{-1}`.

```
E[Phi X_i(u Ghat)] = E[X_i Phi]
X_i(u Ghat) = u sum_j H_V,ij b_j + R_i,     |R_i| <= C u sum_{e near i} beta_e   (globally)
kappa(b_i, Y_2..Y_n) = (1/u) sum_j C_V,ij [ sum_a kappa(Y_2,..,X_j Y_a,..,Y_n) - kappa(R_j, Y_2..Y_n) ]
```

The `n = 1` case gives `|E b_i| <= C/u`.

**Lemma to prove.** For `n <= 4` local quotient functions `Y_a = c_a y_a` with bounded chart derivatives:

```
|kappa_n(Y_1..Y_n)| <= C prod_a c_a * u^{1-n} * exp(-mu tau_n)
```

- Scores have `c = u`, which gives `1/u` and `1`.
- Proof plan: induct on (number of legs, number of legs with a linear part). With at most two linear legs the cut bound already suffices.
- Otherwise reduce one linear leg; each new term has fewer legs, or the same number with one fewer linear leg.
- Each compact cumulant passes to its chart cumulant by (D10), where the polynomial sup norms are absorbed by `exp(-c_r p^2)`.

## Potential defects

1. **Orbit term.** This is the only place the existing method fails outright; it keeps the old orders only while `eps <= C/sqrt(u)`.
2. **Unsupplied producers.** Audit them for:
   - use of the identity Hessian formula rather than gap, range and row bounds;
   - any use of color pi-rotation or `E a_i = 0`;
   - the prefactor, which now contains the extensive `exp(-u Ehat_V(a*))` and must cancel in every ratio.
3. **Factor nonnegativity is lost.** `g_f` can be negative. In the supplied texts I found only two uses of dropped nonnegative factors, and both survive.
4. **Restored law in (D17).** It has its own mode `a*_full(V_O, V_J)`, so `V_J` must also lie in the ball.
5. **Score at the center.** `A_c(a*) = O(u eps)`, not zero. This is harmless for cumulants of order two and up, but check that nothing uses `A_c(0) = 0`.
6. **Hypothesis is not gauge-covariant.** It extends for free to the block-gauge orbit of the ball. Whether actual terminal fields land there is a separate large-field question.
7. **Size of `eps*`.** It is `u`-independent but tiny: `2 D K0 eps* <= c_J/2` with `K0 ~ K_Lip/rho_cap^2`, plus the contraction and chart margins.

## Next decisive calculation

Do it at `V = I`, where all five texts apply. A pure-gauge nonidentity `V` with singlet `F` equals identity `V` with the non-singlet `F∘g`, so the identity case decides the nonidentity consumer. By SO(3) equivariance,

```
kappa3(b_i^a, A_c[v_c], A_d[v_d]) = k_i(c,d) (v_c x v_d)^a
k_i(c,d) = (1/u) sum_j C_ij [ Cov(X_j A_c, A_d) + Cov(A_c, X_j A_d) - kappa3(R_j, A_c, A_d) ]
```

- **Pass:** each bracket term is `O(u)` with tree decay, so `|k_i(c,d)| <= C exp(-mu tau_3)` uniformly in `u`. The cut method alone gives `sqrt(u)`.
- **Cross-check:** the tree value is `D_c D_d a*_i` at `V = I`, which should be generically nonzero. With `A_c = u[alpha_c.z + m_c(z,z)/2 + ...]` and `T3 = D^3 Ghat(I)`:

```
sum_j C_ij [ m_c(e_j, C alpha_d) + m_d(e_j, C alpha_c) - T3(e_j, C alpha_c, C alpha_d) ]
```

- **Fail:** if `kappa3(R_j, A_c, A_d)` cannot be brought to `O(u)`, the nonidentity response is limited to the cut-method column. The orbit term then has no `u`-uniform bound at fixed `eps`.

Still open either way: the two producer audits, strict `V`-locality, repeated-link jets, and the probability of the `eps*` ball.
