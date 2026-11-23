lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T10:47Z

# Row 1456: the Lean flow against the account's first passage

Started 2026-11-23T22:47Z (date -u) on Mac mini worker 2, commit f0ea65331. Port reading. Not checked by another model.

Credit: the Lean release `YM4 Lean` at 3932084a9b82 and the complete account (CA-I, CA-II, CA-III) and outline at 31a47c543775 are by Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text). Short attributed quotes only.

## Plan

1. Read check 1453 (`library/sa-ym4-lean-trajectory-check-astra62.md`) and the row 1451 note it checks; collect what is already established about FlowPassage, IsFirstPassageDatum, run_has_slope.
2. Read the Lean definitions (read only, never build): FlowPassage, IsFirstPassageDatum, run_has_slope, and the blocked Wilson density they read.
3. Read the account: 4.2:lem-first-passage and CA-I 56442-56510.
4. Compare: normalization of g, increments, window width, first-passage sets W_J(g) at matched lattice sizes.
5. Read rows 1332, 1353 and their checks: list the hypotheses of the first-passage seed reductions; decide whether they transfer.
6. Verdict: equal / first incompatible step. Next two rows.

## Repo search

(pending)

Prior on file: check 1453 (`library/sa-ym4-lean-trajectory-check-astra62.md`, lines 57-72) already matched the *form* of CA-I 4.2 (a), (c) with Lean's `passes`, found (b) absent from `IsFirstPassageDatum`, and left "identity of the flows or of their first-passage sets" open. Row 1451 (`prior/sa-ym4-lean-trajectory-opus.md`) and `port/p1-base.md` section 2.2 hold the CA arithmetic port. This row takes up only what check 1453 left open: the increments themselves.

Sources: CA-I and the outline fetched from raw.githubusercontent at 31a47c543775 into `/tmp/row1456.OKfxBS` (CA-I 166711 lines, outline 32992 lines). Lean release read in place at `~/ym4d-papers/sa-ym4-lean-full` (3932084a9b82), read only.

## Step 1. The account's side (CA-I)

Read: CA-I 606-675 (Definitions 1.2:def-couplings, 1.2:def-flow-constants), 3636-3721 (4.2:lem-first-passage and proof), 56342-56510 (Lemma 4.19:lem-flow-bounds, Proposition 4.19:prop-clause-zero).

- **Normalization of g.** CA-I 606-616: $x_0:=g_0^{-2}$, $x_{k+1}:=x_k-\beta_{k+1}$, $g_k:=x_k^{-1/2}$. The bare weight is $\exp(-g_0^{-2}A(U))$ with $A(U)=\sum_p[1-\mathrm{Re}\,\mathrm{tr}\,U(\partial p)]$ and the normalized trace $\mathrm{tr}\,\mathbf 1=1$ (CA-I 657-662, Definition 1.3 uses the same $A$). So $x=2N/g_{\rm std}^2$ in the convention $\beta_{\rm std}=2N/g_{\rm std}^2$, $S=\beta_{\rm std}\sum(1-N^{-1}\mathrm{Re\,Tr}\,U)$.
- **One-loop constant.** CA-I 636: $c_0=\frac{11N^2}{12\pi^2}\log L$. Check by hand: $d(g_{\rm std}^{-2})/d\log\mu=2\beta_0=11N/(24\pi^2)$, times $2N$ gives $11N^2/(12\pi^2)$ per unit $\log$. For $N=2$, $c_0=\frac{11}{3\pi^2}\log L$.
- **Increment.** CA-I 618-623: $\beta_{k+1}$ is Balaban's coupling renormalization, CMP 109 (1.22), identified with CMP 119 (3.61); its construction is CA-I 4.2:def-increment (line 3765, "complete regular part of one step"). It is a function of $g_0,\dots,g_{k}$ only (CA-I 56476-56478) and is torus-independent by input (h).
- **Two-sided bounds.** Lemma 4.19:lem-flow-bounds (CA-I 56342-56368): from the one-loop sum bound $\sum_{i<l\le j}\beta^0_l\ge (j-i)c_0-2c_2$, $|\beta^{\mathfrak A}_l-\beta^0_l|\le c_0/2$, $|\beta^{\mathfrak A}_l|\le C_\beta$, $|\beta^{\mathfrak R}_l|\le\bar\varsigma\le\min(c_0/4,1)$, it gives $\lambda_\sharp(j-i)-c_5\le x_i-x_j\le B_\sharp(j-i)$ with $\lambda_\sharp=c_0/2-\bar\varsigma\ge c_0/4$, $B_\sharp=C_\beta+\bar\varsigma$, $c_5=2c_2$. Its inputs (the one-loop law 4.2:lem-one-loop and 4.2:lem-unmarked) are stated "with proof incomplete at the step marked $(\ast)$" (CA-I 56370-56385).
- **First passage.** $K(g_0,g)=\min\{k: x_k\le g^{-2}+B_\sharp\}$ (CA-I 662). Window: $g^{-2}\le x\le g^{-2}+B_\sharp$, width $B_\sharp$ in $x$ (CA-I 672-674). Bare range $0<g_0\le g_-(g)$. Lemma 4.2 (CA-I 3636-3664): from the two-sided bounds on every prefix with all earlier $x_i>g^{-2}$, (a) first crossing with $g^{-2}<x_K\le g^{-2}+B_\sharp$, (b) the two-sided bounds through $K$, (c) $\frac{t-g^{-2}}{B_\sharp}-1\le K\le1+\frac{t-g^{-2}-B_\sharp+c_5}{\lambda_\sharp}$. Proof read in full (CA-I 3666-3721): correct.
- **Lattice.** Bare spacing $L^{-K}$ on the torus $\mathbb T_m$; the step's block factor is $L$ (Balaban's $L$, odd and large in CMP 109). Torus exponent $m\ge m_{\mathbb T}(g_-(g))$.

What this side asserts about its own flow: Proposition 4.19 is conditional on inputs (a)-(h), among them Balaban CMP 109 Theorem 3 (cited) and two lemmas with proofs incomplete at one step. So $W_J(g)$ on the account's side is the set $\{g_0\in(0,g_-(g)]: K(g_0,g)=J\}$ for a flow whose increments are defined by Balaban's step, with the two-sided bounds conditional.

The increment itself, CA-I 3765-3830 (Definition 4.2:def-increment): $\beta_j=\sum_{u}\Pi^{(j)}_{\infty,\mu\nu}(u)\,u_\mu u_\nu$ ($\mu\ne\nu$), where $\Pi^{(j)}_\infty(x,y)=\sum_{\hat z}\sum_{\hat X\ni\hat z}\langle\partial^2E^{(j)}(\hat X;(\mathbf 1,0),\hat z);\mathfrak h_\infty\delta_x,\mathfrak h_\infty\delta_y\rangle$. Here $E^{(j)}$ are the *localised terms of the complete regular part* of Balaban's step $j$: (a) the Gaussian normaliser $\log Z^{(j-1)}(U_j)-\log Z^{(j-1)}(\mathbf 1)$ (CMP 119 (3.28), CMP 116) at the minimal configuration $U_j$, and (b) the log of the fluctuation integral built from $E_{j-1}$ including aged large-field remainders. $\mathfrak h_\infty$ is the free-boundary (infinite-lattice) linearisation of $B\mapsto(U_j,J_j)(e^{iB})$, Balaban's minimal-configuration map (CMP 109 (1.8), CMP 102). So the account's increment is a **whole-lattice second moment of the localised one-step regular part**, not a readout of a total density.

## Step 2. The Lean side (release 3932084a9b82, read only)

Files read in full: `YangMills/Construction/WindowOfTheParameters/FlowOfTheTotalDensities.lean`, `.../WindowOfTheParameters/FirstPassageOfASequenceForm.lean`, `.../RunningCouplingSlope/CoefficientOfATotal.lean`, `.../ClusterExpansionOfAStep/LumpsOnATorus.lean`, `.../ClusterExpansionOfAStep/WilsonWeightHasAnExpansion.lean`, `.../TotalDensitiesGiveASystem/TopStatementDefs.lean` lines 1-60, `FieldsOnATorus.lean` lines 80-95.

- **Bare weight.** `wilsonWeight β n W = exp(-β * wilsonAction univ W)`, `wilsonAction = Σ_{p, μ<ν} (1 - Re U_p)` with `Re` the real part of the unit quaternion, i.e. $\tfrac12\mathrm{Tr}$ of the SU(2) matrix, the normalized trace. So Lean's $\beta$ **equals** CA's $x_0=g_0^{-2}$ for $N=2$, plaquettes unoriented in both. Step 0 agrees.
- **Block step** (`kernelImage`, `LumpsOnATorus.lean`): $D_{t+1}(m,V)=\int_{W\in\text{field}(mL)} D_t(mL,W)\,\overline{K}_{x_t}(W,V)\,dW$ with
  $\overline K_x(W,V)=|\mathcal B(W)|^{-1}\sum_{b\in\mathcal B(W)}\prod_{c}\dfrac{\exp\bigl(a\,x\,\mathrm{Re}(\bar W_b(c)\,V(c)^{-1})\bigr)}{\mathcal Z(a\,x\,\|\bar W_b(c)\|)}$,
  $\mathcal Z(s)=\int_{SU(2)}e^{s\,\mathrm{Re}\,g}\,dg$, $a=$`ℓ.coupling`$=1$ (`IsUnitMeshStepParameters.coupling_eq_one`), $\bar W_b(c)$ the `contourMean` of the fine field over contours of block bond $c$, with the contour family chosen by a "base choice" $b$ adapted to the **hot lumps** of $W$ (`hotLumps p.grid p.threshold`), and $\mathcal B(W)$ the set of admissible base choices. So the Lean block kernel is a **Fisher (von Mises) kernel on $S^3$, linear in $V$ in the exponent, with stiffness $x_t\|\bar W\|$**, normalized to a probability density in $V$ for each $W$, and its averaging is field-dependent through the hot lumps.
- **Readout** (`nextCoupling`, `HasNextCoupling`, `HasSlopeCoefficient`): $x_{t+1}$ is the $x'$ for which the log ratio $\log D_{t+1}(n,V)-\log D_{t+1}(n,\mathbf 1)$ is a local gauge total along the torus sides $n=2L^q\to\infty$ whose Hessian kernel at the trivial field converges to $\langle X,X'\rangle K(c,c')$ with exponential decay, and $\sum_z -\tfrac12K((0,e_1),(z,e_1))\,z_0^2=-x'$. If no such $x'$ exists the recursion returns the old value $x_t$ (`nextCoupling` fallback), and `IsDefinedUpTo` records the prefix on which the readout exists.
- **Window.** `passageThreshold B g = g^{-2}+B`; `IsFirstPassageIndex B g x K`: $x_K\le g^{-2}+B$ and $x_k>g^{-2}+B$ for $k<K$; `definedPassageWindow` adds $\beta\ge g^{-2}+B$ and `IsDefinedUpTo ℓ β K`. This is CA's $W_K(g)$ **in form**, with Lean's own $B=B_s$.
- **Lattice.** `meshSize L K = L^{-K}`, `torusSide L m = 2L^m`, block side $L$ odd, $L\ge2^{40}$ (`IsUnitMeshStepParameters`). `asymptoticFreedomSlope = 11·2^2/(12π^2) = 11/(3π^2)`.

**Normalization check of the readout (PROVED here by hand).** Let a gauge-invariant quadratic form have Fourier kernel $\hat Q_{\mu\nu}(k)=x\,(k^2\delta_{\mu\nu}-k_\mu k_\nu)+O(k^4)$ in plaquette units, so that $x$ is the coefficient of $\sum_p(1-\mathrm{Re}\,U_p)$ at quadratic order. With $\sum_u Q(u)u_\rho u_\sigma=-\partial_\rho\partial_\sigma\hat Q(0)$:
  - CA (μ≠ν, ρ=μ, σ=ν): $\sum_u\Pi_{\mu\nu}(u)u_\mu u_\nu=-\partial_\mu\partial_\nu\hat\Pi_{\mu\nu}(0)=-x\cdot(-1)=x$.
  - Lean (μ=ν=1, ρ=σ=0): the Hessian of $\log D=-x'Q+\dots$ is $K=-x'Q$, so $\sum_z K_{11}(z)z_0^2=-x'\cdot(-\partial_0^2\hat Q_{11}(0))=-x'\cdot(-2)=2x'$, and $-\tfrac12\cdot 2x'=-x'$. ✓
  Both read **the same coefficient** (the $F^2$, i.e. $k^2$-transverse, coefficient) with the same normalization, given that the Lie-algebra normalizations agree. The Lean Hessian uses directions $X\in\mathrm{Im}\,\mathbb H$ with the quaternion inner product; CA's directions are Lie-algebra fields with its own trace normalization. At the bare level both give $x_0=\beta$, so any constant factor between the two direction normalizations would show as $x_0\ne\beta$; Lean's `run`/slope theorems state the bare readout is $\beta$ (not re-read here; GUIDE until read).
- **One-loop constant.** CA $c_0=\frac{11N^2}{12\pi^2}\log L$ at $N=2$ equals Lean `oneLoopShift L = asymptoticFreedomSlope * log L` $=\frac{11}{3\pi^2}\log L$. **Equal.**
- **Monotonicity in β** (`ContinuumLimit/SlopeOfTheRun.lean` L194-226, `run_has_slope`, read): on the run domain (open, upper set, nonempty) the expansion flow `runFlow T y k` is differentiable in the bare β with derivative `runSlope ∈ [3/4, 5/4]`; check 1453 L32 records the agreement of this expansion flow with `TotalDensityFlow.coupling` above the floor. "Slope" in `run_has_slope` is $\partial x_k/\partial\beta$, not the running-coupling slope.
- **Where FlowPassage is proved** (`ContinuumLimit/TunedLimitsAtTheTop.lean` L47-65, `TunedTop.Statement`, `tuned_top`): there are $\vartheta_0,J,L_*$ such that for every odd $L\ge L_*$ there are step parameters ℓ (side $L$, unit mesh), $B_s=2\,T.B\ge2$, $c_5\ge0$, $\gamma\in(0,1)$, … with, **for every $g\in(0,\gamma]$**, `CouplingConditions ℓ Bs c₅ (3/4 * oneLoopShift L) Nw CT g`, whose field `passage` is `FlowPassage ℓ Bs c₅ lam Nw g` with $\mathrm{lam}=\tfrac34c_0$. It also gives a unique tuned root per cutoff (`∀ K, ∃! β, IsTunedAt …`). Kernel replay of the release is row 1455 (lead), not read here.

## Step 3. Comparison, item by item (PROVED by reading both sources, unless labelled)

| Item | Account (CA-I) | Lean release | Equal? |
|---|---|---|---|
| Bare weight, normalization of $g$ | $e^{-g_0^{-2}A(U)}$, $A=\sum_p(1-\mathrm{Re\,tr}U_p)$, tr normalized (CA-I 447-481) | $e^{-\beta\,\mathrm{wilsonAction}}$, $\sum_{\mu<\nu}(1-\mathrm{Re}\,U_p)$, quaternion real part | **yes**: $x_0=g_0^{-2}=\beta$ |
| Readout normalization | $\sum_u\Pi_{\mu\nu}(u)u_\mu u_\nu$, $\mu\ne\nu$ (CA-I 3826-3829) | $-\tfrac12\sum_z K_{11}(z)z_0^2$ (`secondMomentTerm`) | **same coefficient** (transverse $k^2$ term), computation in Step 2 |
| One-loop constant | $c_0=\frac{11N^2}{12\pi^2}\log L$ (CA-I 636) | `oneLoopShift L` $=\frac{11}{3\pi^2}\log L$ | **yes** at $N=2$ |
| Lattice, torus, block factor | spacing $L^{-K}$, torus $2L^m$, $L$ odd large (CA-I 790-794) | `meshSize L K`$=L^{-K}$, `torusSide`$=2L^m$, $L$ odd $\ge2^{40}$ | **yes** for any common odd $L$ above both floors |
| **Block step** | exact push-forward $\mathbf T\rho(V)=\int dU\,\delta(\mathcal M(U)V^{-1})\rho(U)$ under Balaban's averaging map $\mathcal M$ (CMP 109 (0.10)-(0.12) on $\mathcal S_c$, (0.4) off it), a **hard constraint** (CA-I 862-866); then Balaban's small/large-field decomposition and gauge fixing (CA-I 870-876) | soft kernel $\prod_c e^{x_t\mathrm{Re}(\bar W_b(c)V(c)^{-1})}/\mathcal Z(x_t\|\bar W_b(c)\|)$, linear quaternion contour mean, averaged over hot-lump base choices; no field split | **no — first incompatible step** |
| Increment / readout | $\beta_{k+1}$ = whole-lattice second moment of the *localised regular part* of step $k+1$ composed with Balaban's linearised minimal-configuration map $\mathfrak h_\infty$, plus a bounded large-field part $\beta^{\mathfrak R}$ (CA-I 3765-3830, 56342-56385) | $x_{t+1}$ = second moment of the Hessian at $V=\mathbf 1$ of $\log$ of the **whole** exactly blocked density, infinite-volume limit along sides $2L^q$; fallback $x_{t+1}=x_t$ off the defined prefix | **no** (different objects, even for equal densities) |
| Status of the two-sided bounds | conditional: inputs (a)-(h) of Prop. 4.19, two lemmas with proof incomplete at $(\ast)$, Balaban CMP 109 Thm 3 cited (CA-I 56442-56470) | `FlowPassage.passes` and `run_has_slope` proved in the release (kernel replay: row 1455) | different standing |
| Window | $(g^{-2},g^{-2}+B_\sharp]$, $B_\sharp$ no value (CA-I 662-674) | `passageThreshold Bs g`, $B_s=2T.B\ge2$, no value | same form, constants unrelated |
| Passage speed | $\lambda_\sharp\ge c_0/4$ | `lam` $=\tfrac34c_0$ | different constants |
| $\beta\mapsto x_k$ | no continuity in $g_0$ used or claimed (CA-I 3620-3622) | $C^1$, slope in $[3/4,5/4]$ on the run domain | Lean has more |

**First incompatible step: the block step from level 0 to level 1.** Both flows start at $x_0=\beta$. The account's $\rho_1$ is the push-forward of the Wilson density under Balaban's map $\mathcal M$ (a delta constraint). Lean's $D_1$ is its integral against a soft Fisher kernel of stiffness $\beta\|\bar W\|$ centred on a linear contour mean chosen by hot lumps. These are different functions of the block field $V$, and the readouts are different functionals of them. So $x_1^{\rm Lean}(\beta)$ and $x_1^{\rm CA}(\beta)$ are different numbers in general, and no statement in either source, or on file, relates them.

**What the difference is expected to be (GUIDE only; no proof step uses it).** Both schemes have the universal one-loop step $c_0$. They differ in the scheme-dependent finite part of the step (the account's $c_2$ is that part for its scheme). At weak coupling one expects $x_k^{\rm Lean}(\beta)-x_k^{\rm CA}(\beta)\to d$ for a fixed finite renormalization $d=O(1)$, so the first-passage indices at the same $(\beta,g)$ would differ by a bounded shift, and $W_J^{\rm Lean}(g)$, $W_J^{\rm CA}(g)$ would be different intervals of comparable width. Nothing in either source proves this. The proved two-sided bounds alone give only $|K^{\rm Lean}(\beta)-K^{\rm CA}(\beta)|\le\beta\,|1/\lambda-1/B|+O(1)$, growing with $\beta$.

**Verdict on equality: NOT EQUAL.** The flows are not the same sequence, and the first-passage sets $W_J(g)$ at matched lattice sizes are not shown equal (and are not expected to be equal). The match of check 1453 is a match of the *arithmetic* (CA-I 4.2 (a), (c) against `passes`), not of the flows.
