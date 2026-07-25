# Worker A scout report — d-dim action-level transfer identity source scan

Bounded extraction. Verbatim quotes with relocation context. No code run.
Files read (exactly the spec set):

1. `docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md` (the **dispersion note**)
2. `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md` (the **RP note**)
3. `docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md` (the **corner note**, landed as block10)
4. `docs/MICROCAUSALITY_GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-20.md` — **ABSENT on this branch.** `find docs -iname "*GRAPH_METRIC*"` and `-iname "*D3_SECOND_QUANTIZATION*"` both return nothing. The newest microcausality notes on-branch are all dated `2026-07-18` (block10 corner note is the tip). Branch is `physics-loop/microcausality-many-body-lightcone-block10-discharge-...`. This block11 note does not yet exist; section (f) below records the consequence.
5. `scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py` — path confirmed from the dispersion note header line 8 (`**Primary runner:** scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py`); file present (10724 bytes).

---

## (a) Dispersion note — d-dimensional action, staggered phases, period + mass window

**Phase convention** (section "Cell Convention and Phase Bookkeeping", lines 76-91). "Use time coordinate `t` and spatial coordinate `x in Z^d`. The canonical staggered phases are"

```text
    eta_0(t,x) = 1,
    eta_mu(t,x) = (-1)^(t + x_1 + ... + x_{mu-1}),      mu = 1,...,d.
```

"Write"

```text
    xi_mu(x) = (-1)^(x_1 + ... + x_{mu-1}),
    H_hop = (1/2) sum_mu xi_mu(x) (tau_{+mu} - tau_{-mu}).
```

So: the **temporal** phase `eta_0 = 1`; the **spatial** phase on axis `mu` depends on `t` AND on the lower spatial coordinates `x_1,...,x_{mu-1}` (not on `x_mu` itself). `xi_mu` is the time-independent spatial part; the whole `t`-dependence of the spatial hop is the overall `(-1)^t`.

**Action / mode equation** (lines 93-106). "The spatial term on time slice `t` is `(-1)^t H_hop`, so the free mode equation has the same alternating form as the one-axis construction:"

```text
    psi_{t+1} = -2 (m I + (-1)^t H_hop) psi_t + psi_{t-1}.
```

"Thus"

```text
    T_even = [[-2(m I + H_hop), I], [I, 0]],
    T_odd  = [[-2(m I - H_hop), I], [I, 0]],
    T_2    = T_odd T_even.
```

**Even-periods sentence** (Statement, lines 38-40). "On the free `U = 1` staggered surface, with real `m > 0`, d spatial axes, **even spatial periods**, and the same two-step RP blocking in time, the action-derived two-step transfer is diagonal after the standard reduced momentum/two-site-cell transform." (Runner docstring for `spatial_hop`: "on an even periodic L^d torus".)

**Mass window.** The only mass hypothesis is "**real `m > 0`**" (Statement line 38; repeated as the domain of the contour bound "`0 < eta < arcsinh(m)`", lines 63-64). There is no upper mass bound in this note. (The runner exercises `m = 0.37` and `m = 0.3`; no mass sweep in the note itself.)

---

## (b) Dispersion note — fold / corner algebra and the per-k two-step block

**Reduced domain + corners** (lines 108-120). "Now fold the spatial lattice by translations through two sites in every spatial direction. A reduced momentum sector is labelled by `k in (-pi/2, pi/2]^d` and a cell/taste corner `r in {0,1}^d`, representing the full momentum `p_r = k + pi r`. Multiplication by `xi_mu(x)` shifts the corner by `s_mu = (1,...,1,0,...,0)` with ones in slots `< mu`, and the finite difference contributes `i sin(p_{r,mu}) = i (-1)^{r_mu} sin(k_mu)`. Therefore"

```text
    H_hop(k) = i sum_mu sin(k_mu) Gamma_mu,
    Gamma_mu |r> = (-1)^{r_mu} |r xor s_mu>.
```

**Corner-operator algebra** (lines 122-135). "A direct sign check gives"

```text
    Gamma_mu^2 = I,
    Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0,     mu != nu.
```

"Therefore"

```text
    H_hop(k)^2 = - (sum_mu sin^2 k_mu) I.
```

"This is the only dimension-dependent algebraic step."

**Per-k block structure and DIMENSION.** Two nested layers:
- The corner/taste space is `2^d`-dimensional: `Gamma_mu` are `2^d × 2^d` matrices (Clifford module on `r in {0,1}^d`), and `H_hop(k)` is the `2^d × 2^d` matrix above. On this space `H_hop(k)` has scalar square `-(sum sin^2 k_mu) I`, so its eigenvalues are `± i·sqrt(sum sin^2 k_mu)`.
- **The per-k two-step block itself is 2×2, one per eigenline of `H_hop(k)`** (section "Two-Step Eigenvalue Algebra", lines 137-166). "Let `i lambda` be an eigenvalue of `H_hop(k)`, so `lambda^2 = sum_mu sin^2 k_mu`. On that eigenline the time recurrence is identical to the one-spatial-axis recurrence with `sin p` replaced by `lambda`:"

```text
    a = m + i lambda,
    T_even(lambda) = [[-2a, 1], [1, 0]],
    T_odd(lambda)  = [[-2conj(a), 1], [1, 0]].
```

"The two-step matrix is"

```text
    T_2(lambda) = T_odd(lambda) T_even(lambda)
                = [[4|a|^2 + 1, -2conj(a)], [-2a, 1]].
```

"It has determinant `1` and trace `2 + 4(m^2 + lambda^2)`."

**Eigenvalues of the per-k block** (lines 156-166). "With `R = m^2 + lambda^2` and `sinh E = sqrt(R)`,"

```text
    spec T_2(lambda)
      = { 1 + 2R + 2 sqrt(R(1+R)),
          1 + 2R - 2 sqrt(R(1+R)) }
      = { exp(+2E), exp(-2E) },
    E = arcsinh(sqrt(R)).
```

"Substituting `lambda^2 = sum_mu sin^2 k_mu` and unfolding `p = k + pi r` gives the displayed d-dimensional dispersion"

```text
    E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)).
```

Taste degeneracy (Statement, line 51): "The formula is taste-degenerate across the `2^d` two-site-cell corners because `sin^2(k_mu + pi r_mu) = sin^2 k_mu`."

---

## (c) Dispersion note — positivity / decaying-channel statements and one-particle-only boundaries

**Forward decaying eigenvalue** (Statement, lines 41-47). "For every full Brillouin-zone momentum `p in T^d`, the forward decaying one-particle eigenvalue is"

```text
    lambda_-(p) = exp(-2 E_d(p)),
    E_d(p) = arcsinh(sqrt(m^2 + sum_{mu=1}^d sin^2 p_mu)).
```

**Forward/backward channel language** (Two-Step Eigenvalue Algebra, lines 175-176). "The decaying forward channel is `exp(-2 E_d(p))`; the reciprocal growing channel is the backward-time solution, as in the one-axis construction."

**IMPORTANT NEGATIVE FINDINGS (dispersion note):**
- The dispersion note contains **NO `(0,1]` interval statement** for `e^{-2E_d}`. The explicit "`lambda_-(p) = e^{-2E(p)} in (0,1]`" line lives only in the RP note (see (d)); the dispersion note only says "forward decaying" and "reciprocal growing … backward-time solution."
- The dispersion note contains **NO projector construction** (no `P_-(p)`, `P_+(p)`), **no finite-norm forward-selection argument**, **no coherent-state kernel**, **no `Gamma`/second-quantization**, **no `B^dag B`**. It defers the channel selection by reference: "as in the one-axis construction." All of that machinery is 1+1d-only (RP note).

**ONE-PARTICLE-ONLY boundary sentences (all of them, dispersion note):**
- Statement (line 42): "the forward decaying **one-particle** eigenvalue is `lambda_-(p) = exp(-2 E_d(p))`".
- Boundaries (lines 221-223): "The theorem concerns the action-derived **one-particle** two-step transfer and the corresponding free log-transfer symbol. It does not prove gauged or interacting log-transfer locality."
- Boundaries (line 220): "Free `U = 1` staggered two-step sector only."
- Boundaries (lines 224-227): "The kernel is quasilocal, not finite-range. The even-offset rule is a parity support rule, not compact support." / "The all-direction statement is an explicit positive lower-bound rate. The sharp anisotropic rate away from coordinate axes remains an open target."

---

## (d) RP note — Steps 3b and 4 verbatim (1+1d)

**Step 3b — projectors** (lines 143-164). "For `m>0`, the two eigenvalues of `T2cl(p)` are reciprocal positive real numbers"

```text
    lambda_-(p) = e^{-2E(p)} in (0,1],
    lambda_+(p) = e^{+2E(p)} >= 1.
```

"Their spectral projectors are explicit:"

```text
    P_-(p) = (T2cl(p) - lambda_+(p) I) / (lambda_-(p) - lambda_+(p)),
    P_+(p) = (T2cl(p) - lambda_-(p) I) / (lambda_+(p) - lambda_-(p)),
```

"with `P_-^2=P_-`, `P_+^2=P_+`, `P_-P_+=0`, `P_-+P_+=I`, and `T2cl P_- = lambda_- P_-`."

**Finite-norm forward-selection sentence** (lines 159-164). "The positive-time coherent-state transfer is the stable half-line channel on `P_-`: a forward solution with any `P_+` component grows like `lambda_+^N` over `N` two-step blocks, so finite-action / finite-norm positive-time propagation sets that coefficient to zero. In the diagonal one-particle basis the forward kernel is therefore `K_2(p)=lambda_-(p)`. The growing reciprocal channel is the inverse backward-time solution, not the forward transfer kernel."

**One-mode coherent-state kernel + induced exterior operator** (lines 166-174). "For a one-mode coherent-state kernel `<bar z'|T_2|z> = exp(bar z' lambda_- z)`, the induced operator on the finite exterior algebra is exactly `diag(1,lambda_-)`; across momenta this is the wedge product `Gamma(K_2)`. The runner verifies the projector identities, the residual `T2cl P_- - lambda_- P_-`, the projector split/orthogonality, the finite exterior construction, the creation-operator intertwiner, and the `B^dag B` factorization at machine precision (C6). Thus `t1^(2)(p)=e^{-2E(p)}` is the action-derived decaying spectral channel, not a separate convention."

**Step 4 — defining intertwiner** (lines 196-199). "The defining property of the second-quantization functor `Gamma` is that it carries a one-particle operator `K` (here diagonal, `K e_p = lambda_p e_p`) to the many-body operator `Gamma(K)` on the Fock space `H = tensor_p {|0>, |1>}` that fixes the vacuum and intertwines the creation operators,"

```text
    Gamma(K) |vac> = |vac>,    Gamma(K) a_p^dag = lambda_p a_p^dag Gamma(K).
```

**Assembly display** (lines 205-208 and 226-229). "For a diagonal kernel these two requirements have a unique, explicit finite-dimensional solution: the per-mode tensor product … "

```text
    Gamma(t1^(2)) = tensor_p diag( 1, lambda_p )
                  = exp( -2 a_tau H_hat ),    H_hat = sum_p E(p) a_p^dag a_p,
```

and

```text
    T_hat^2 = Gamma( t1^(2) ) = tensor_p diag( 1, e^{-2 E(p)} )
            = exp( -2 a_tau H_hat ),     H_hat = sum_p E(p) a_p^dag a_p.
```

**`B^dag B` display** (lines 234-236). "Since `E(p) >= 0` for all `p`, `H_hat >= 0`, hence `T_hat^2` is positive Hermitian with `||T_hat^2|| = 1` (vacuum) and admits the explicit factorization"

```text
    T_hat^2 = B^dag B,    B = exp( -a_tau H_hat ) = tensor_p diag( 1, e^{-E(p)} ).
```

"This is exactly the 2-step reflection-positivity statement: `H_hat = -log(T_hat^2) / (2 a_tau)` is self-adjoint and bounded below by `0`." (lines 238-239)

**1+1d-only scope sentences (RP note):**
- Claim (lines 24-26): "On the free staggered-only action surface (`U = 1`, one Grassmann component per site, **`1+1d`**, `L_s` spatial sites, periodic, real mass `m > 0`), with the canonical staggered phases `eta_0 = 1` and `eta_1(t) = (-1)^t`:"
- Step 1 (lines 90-92): "For free staggered fermions in **`1+1d`** (one Grassmann component per site, `L_s` spatial sites, periodic) at fixed spatial momentum `p`, the staggered action's banded-in-time mode equation is"
- Step 3 (lines 128-131): "`E(p) = arcsinh( sqrt( m^2 + sin^2 p ) )` … the exact free staggered **`1+1d`** dispersion."
- Note the RP note works at the **full** spatial momentum `p` (`alpha_even = m + i sin(p)`, `alpha_odd = m - i sin(p)`, lines 104-106); it does **not** perform the reduced-`k`/taste-corner fold of the dispersion note.

---

## (e) Corner note — finite-mode theorem items 1-5 verbatim + open problems

**Finite-mode theorem** (lines 44-72). Setup: "`F(H) = direct_sum_(q=0)^n wedge^q H` … `Gamma(A) = direct_sum_(q=0)^n wedge^q A`." "let `dGamma(X)` denote the infinitesimal exterior action: on `wedge^q H`, it is the sum of `X` acting in each occupied slot."

1. "**Functoriality.** For arbitrary linear maps `A` and `B`, `Gamma(A) Gamma(B) = Gamma(AB)`. No commutativity hypothesis is needed for this algebraic identity."
2. "**Canonical intertwiner.** With `a^dag(f)` denoting exterior multiplication by `f`, `Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)`, and `Gamma(A)` fixes the vacuum. These relations determine `Gamma(A)` on decomposable occupation vectors."
3. "**Positive logarithm.** If `t` is strictly positive, then `Gamma(t) = exp(dGamma(log t))` and `-log Gamma(t) = dGamma(-log t)`."
4. "**Trace identity.** `Tr_F Gamma(A) = det_H(1 + A)`. In particular this holds for positive `t` without choosing an eigenbasis in the statement."
5. "**Direct sums.** Under the canonical exterior-algebra identification, `Gamma(direct_sum_k A_k) = tensor_k Gamma(A_k)`."

**Why trace data do not identify the functor** (lines 94-107, load-bearing pin — this is the block10 discharge lens counterexample cited in memory). "Let `W` be a fixed number-preserving unitary which acts nontrivially inside a two-particle sector and define `Gamma_tilde(A) = W Gamma(A) W^dag`. It preserves traces and functoriality and maps positive `A` to positive operators, but it need not satisfy the canonical creation intertwiner. For `t = diag(2,3,5)`, swapping the occupation states with eigenvalues `6` and `10` changes the corresponding entries of `-log Gamma_tilde(t)` relative to the standard `dGamma(-log t)`. Thus the exterior action or, equivalently, the canonical creation intertwiner is the pin. The trace/determinant correspondence by itself is not a Gaussian-factorization theorem."

**Composition on the free corner surface** (lines 109-140). The cited `CORNER_AXIS_FREE_TRANSFER_EXTENSION_...` "supplies, on its free finite-mode `1+1d` surface and positive-mass domain, `t_k = exp(-2 E_k)`, `T_k^2 = Gamma(t_k)` for each of the three decoupled generation channels." Then: "`-1/2 log T_k^2 = dGamma(E_k)`" and "`T_corner^2 = tensor_k T_k^2 = Gamma(direct_sum_k t_k)`", hence "`-1/2 log T_corner^2 = sum_k dGamma(E_k)` under the canonical tensor-factor identification." Key caveat: "The factorized form has no additional scalar there because the cited source supplies the operator equality itself. This does not determine any background-dependent scalar or normalization beyond that free source surface." And: "This is an algebraic logarithmic-generator identification. It does not select physical time or derive dynamics from the framework axioms."

**Open problems and non-claims** (lines 142-156, verbatim):
- "**Fixed gauge backgrounds:** no current source identifies the classical fixed-background recurrence matrix with a Fock-space `Gamma(t[U])`."
- "**Gauge integration:** no measure over backgrounds or interacting transfer is supplied."
- "**Locality and Lieb-Robinson bounds:** this note proves no spatial kernel envelope and makes no open-chain or periodic-chain activity claim. A one-particle locality estimate cannot be fed into a many-body bound until the operator identification and boundary convention are both supplied."
- "**Matrix fibers:** if a future one-dimensional open-chain bridge supplies a block-operator-norm envelope with fixed fiber dimension `n_f`, the coarse activity expression carries the factor `n_f`; scalar-fiber constants do not transfer to a non-Abelian block kernel."
- "**Physical interpretation:** no species choice, occupancy choice, physical velocity, infinite-volume dynamics, or retained-grade status follows."

Scope front-matter (lines 4): "Finite-dimensional number-conserving fermionic second quantization and its logarithmic-generator identity, with composition only on the supplied free U=1 corner surface. Fixed-background factorization, gauge integration, locality envelopes, Lieb-Robinson bounds, and physical-time selection are not claimed." Scope §, lines 30-41: "It does not infer a many-body transfer operator from a one-particle kernel." / "The current source tree does not supply `T_MB^2[U] = Gamma(t[U])` at a general fixed gauge background." / "Fixed-background factorization therefore remains open."

---

## (f) Block11 note (file 4) — ABSENT; consequence

`MICROCAUSALITY_GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-20.md` does **not exist on this branch** (confirmed by two `find` name-globs and the fact the tip note is block10, `2026-07-18`). Therefore I cannot quote its "construction-status sentences" or its "scalar-ambiguity caveat."

What CAN be said from the allowed sources about the caveat this block would discharge: the corner note (file 3) already names the target — the "**Gaussian-factorization hypothesis**" — and states the residual scalar freedom explicitly (lines 130-140): the free-corner composition "**has no additional scalar there because the cited source supplies the operator equality itself. This does not determine any background-dependent scalar or normalization beyond that free source surface**." The corner note credits that hypothesis to `MICROCAUSALITY_GAUGED_KERNEL_WEIGHTED_ACTIVITY_FEED_BOUNDED_THEOREM_NOTE_2026-07-18.md` (line 132) — which is NOT in my allowed read set, so I did not open it. **Flag for supervisor:** any plan step that quotes or "updates" the block11 note is quoting a file that is not present; the plan's ground-truth must either create block11 fresh or re-point to the corner note + gauged-kernel-feed note as the actual on-branch anchors for the scalar-ambiguity caveat.

---

## (g) Dispersion note runner — construction pipeline (for a native rebuild)

`scripts/free_staggered_two_step_dispersion_d_dimensional_2026_06_12.py`, numpy only, deterministic (no RNG). The per-block object is built in **position space over the full torus**, not per-k:

1. `spatial_hop(d, L)` builds the `V×V` complex hop, `V = L**d`, on an even periodic `L^d` torus. Per site `x`, per axis `mu`: `eta = (-1)**sum(x[:mu])` (this is `xi_mu(x)`), then `hop[site, +mu neighbor] += 0.5*eta` and `hop[site, -mu neighbor] -= 0.5*eta`. This is `H_hop`; the `(-1)^t` slice sign is applied in `T_even/T_odd`, not here.
2. `two_step_decays_from_blocking(d, L, m)` assembles the doubled classical transfer exactly as the note's display: `T_even = block([[-2*(m*I + H), I],[I, Z]])`, `T_odd = block([[-2*(m*I - H), I],[I, Z]])`, `T2 = T_odd @ T_even`; then `eig = eigvals(T2)`, selects the decaying branch `eig[abs(eig) < 1.0 + 1e-8]`, returns `sort(decaying.real)` and `max|imag|`.
3. `predicted_decays(d, L, m)` is the independent target: over every momentum `p = 2*pi*n/L`, `exp(-2*dispersion(m,p))`, with `dispersion = arcsinh(sqrt(m*m + sum sin(component)**2))`.
4. `gamma_matrices(d)` builds the corner matrices directly: `mask = (1<<mu)-1`, `gamma[r ^ mask, r] = -1.0 if ((r>>mu)&1) else 1.0` — i.e. `Gamma_mu|r> = (-1)^{r_mu}|r xor s_mu>`.
5. `kernel_d(d,m,N)` = `ifftn(E).real` where `E = arcsinh(sqrt(m*m + sum_mu sin(grid_mu)**2))` on an `N^d` momentum grid — the position-space log-kernel.

**Seven checks** (all deterministic): (1) note guardrails/links; (2) `Gamma_mu^2=I` + anticommutation in `d=2,3`; (3) `A(k)^2 = -(sum sin^2 k_mu) I` for `A(k)=sum 1j*sin(k_mu)*Gamma_mu` (residual `<1e-14`); (4) blocked `T_odd T_even` decaying spectrum equals `exp(-2E_d(p))` on `(d,L) in {(2,4),(2,6),(3,4)}`, `m=0.37`, residual `<1e-12`, `max imag <1e-12`; (5) kernel vanishes on odd offsets; (6) axis decay rate fit `≈ arcsinh(m)`; (7) all-direction contour ratio `<= 1` giving `l1` rate `arcsinh(m)/(2d)`. Expected final line `TOTAL: PASS=7, FAIL=0`.

**What the runner does NOT build:** no Fock space, no `Gamma(t)` second quantization, no spectral projectors `P_±`, no forward-channel selection, no `B^dag B`, no OS Gram, no many-body operator. It is a one-particle classical-monodromy spectrum check plus dispersion match plus kernel-decay bounds. (Contrast the RP-note runner `axiom_first_rp_two_step_transfer_matrix_positivity.py`, which does build `Gamma`, `B^dag B`, and the OS Gram — but only in 1+1d.)

---

## (h) GAP LIST — what a d-dim many-body action-level derivation needs that is NOT in any source

Adversarial. A "d-dim many-body action-level transfer identity" (the analogue of RP-note Steps 3b+4 at general d) requires the following, none of which exists on-branch:

1. **No many-body object at general d anywhere.** The dispersion note stops at the one-particle classical monodromy: it derives the per-k 2×2 block `T_2(lambda)` as a **transfer recursion in time** (yes, a genuine time-transfer, lines 137-155) but only reads off its **eigenvalues** (a dispersion relation). It never forms `Gamma(t)`, `T_hat^2`, or any Fock-space operator in `d>1`. The only many-body `T_hat^2 = Gamma(t1^(2)) = tensor_p diag(1,e^{-2E(p)})` display (RP note Step 4) is explicitly `1+1d`.

2. **No forward-channel selection at general d.** The projectors `P_-(p), P_+(p)`, the finite-norm "sets that coefficient to zero" argument, and `K_2(p)=lambda_-(p)` exist **only in the RP note (1+1d)**. The dispersion note defers this entirely ("as in the one-axis construction," line 176). A d-dim derivation must rebuild `P_±(p)` from the d-dim `T2cl` and re-run the growth/finite-norm selection — nobody has.

3. **No d-dim coherent-state / induced-exterior step.** `<bar z'|T_2|z> = exp(bar z' lambda_- z) → diag(1,lambda_-)` is RP-note 1+1d only.

4. **The d-dim assembly is unwritten.** The object the plan must produce, `T_hat^2 = tensor_{p in T^d} diag(1, e^{-2E_d(p)}) = exp(-2 a_tau H_hat)` with `H_hat = sum_{p in T^d} E_d(p) a_p^dag a_p >= 0`, and its `B^dag B = tensor_p diag(1,e^{-E_d(p)})`, appears **nowhere**. The corner note supplies the *abstract* functor that would license it (items 1-5, arbitrary finite `H`) but applies it only to a 1+1d three-generation surface, and states outright it "does not infer a many-body transfer operator from a one-particle kernel."

5. **Mode-set / corner bookkeeping is unresolved for the many-body fold.** The dispersion note's `2^d` taste corners `r in {0,1}^d` are spatial-fold bookkeeping (a Clifford module), not extra particle species. A d-dim second quantization needs one creation operator per full-BZ mode `p in T^d` (Fock dim `2^{L^d}`), with the `2^d` corners collapsing into the momentum label via `p_r = k + pi r`. This map (corners → BZ modes, avoiding double-counting) is not written in any source. The corner note's "matrix fibers" open problem warns that here the fibers must be **scalar** (`n_f = 1`) for the free case, else "scalar-fiber constants do not transfer to a non-Abelian block kernel."

6. **`a_tau` / normalization is not fixed at general d.** The dispersion note gives `E_d(p)` "up to the already declared blocked-time normalization convention" (line 50) and never names `a_tau`. A d-dim `H_hat = -log(T_hat^2)/(2 a_tau)` identity needs `a_tau` pinned; the three sources use three different conventions (see (i)).

7. **No d-dim OS-Gram / positivity cross-check.** RP-note route R2 (`G = <vac|F_I^dag T_hat^2 F_J|vac>`, PSD) is 1+1d only.

Net: the dispersion note gives **one-particle spectral data at general d** (`E_d`, `lambda_-`, taste degeneracy, kernel decay). Everything many-body/positive/functorial is either 1+1d (RP note) or abstract-and-1+1d-applied (corner note). The d-dim many-body action-level identity is exactly the un-built bridge.

---

## (i) LIMITS — mismatches that would block or rescope the plan

1. **"Corner" is overloaded across sources — high collision risk for the plan's ground truth.** In the **dispersion note**, "corner" = taste corner `r in {0,1}^d`, the `2^d` spatial-fold sectors (`p_r = k + pi r`). In the **corner note**, "corner" = the free `1+1d` **three-generation** channel surface, and `T_corner^2 = tensor_k T_k^2` runs `k` over **generation channels** (`t_k = exp(-2E_k)`, three of them), NOT over taste corners or momenta. Any plan step that reads the corner note's `-1/2 log T_corner^2 = sum_k dGamma(E_k)` as a *d-dim taste-corner* statement is wrong. Flag: if the plan's ground-truth item 3 equates these two "corners," it is mistaken.

2. **Phase-convention shape differs (reconcilable in d=1, but the plan must state it).** RP note: `eta_1(t) = (-1)^t` (spatial phase depends on `t` only). Dispersion note: `eta_mu(t,x) = (-1)^(t + x_1+...+x_{mu-1})` (depends on `t` AND lower spatial coords). They agree in `d=1` (`xi_1 = (-1)^{empty} = 1`, so the spatial hop is `(-1)^t · (1/2)(tau_+ - tau_-)`, matching `alpha_t = m + i(-1)^t sin p`), but a d-dim derivation must use the dispersion note's convention and cannot silently inherit the RP note's simpler form.

3. **Momentum-domain / fold mismatch.** RP note operates at the **full** spatial momentum `p` with no fold (Fock modes = the `L_s` chain momenta). Dispersion note folds to reduced `k in (-pi/2,pi/2]^d` + corners. A d-dim many-body assembly must choose one labelling and keep the mode count consistent (`2^{L^d}` Fock space over full-BZ `p`, with `2^d`-degenerate `E_d`), reconciling the fold before tensoring.

4. **`a_tau` normalization is three-valued across the sources.** RP note: explicit `a_tau`, `H_hat = -log(T_hat^2)/(2 a_tau)`, `B = exp(-a_tau H_hat)`. Dispersion note: unspecified ("declared blocked-time normalization convention"). Corner note: dimensionless, `-1/2 log T_corner^2 = dGamma(E)` (effectively `a_tau = 1`, factor `-1/2`). The plan must pick one; a native runner should follow the corner note's dimensionless `-1/2 log` to match the landed block10 identity, or explicitly carry `a_tau`.

5. **Positivity interval `(0,1]` is asserted only in 1+1d.** `e^{-2E_d} in (0,1]` at general d is *true* (since `E_d(p) = arcsinh(sqrt(m^2 + …)) > 0` for `m>0`) but is **not stated** in the dispersion note; the plan cannot cite the dispersion note for it and must rederive it (trivially) from `E_d > 0`.

6. **Even-period assumption is load-bearing and must be preserved.** Dispersion note requires "even spatial periods"; the RP note flags `p=π` on even lattices as an exceptional real-spectrum mode. A d-dim many-body run must keep even `L` (runner uses `L in {4,6}` for `d=2`, `L=4` for `d=3`).

7. **Block11 target file is absent (repeat of (f)).** Any plan whose ground truth points at `...GRAPH_METRIC_CLASS_AND_D3_SECOND_QUANTIZATION..._2026-07-20.md` is pointing at a non-existent file on this branch; re-anchor to the corner note (block10) + the gauged-kernel-feed note as the live scalar-ambiguity authorities.
