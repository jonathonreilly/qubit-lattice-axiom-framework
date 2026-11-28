## Repo search

The lead's [search](prior/repo-search-2026-11-08.md), §§2 and 8, found no changed-boundary supplier.
I reuse that search and [prior/hstep](prior/hstep.md), A1.3, A3.2 and W4.
`prior/leaf-creflect.md` is absent at the requested pin.
I read the assigned supplier section of [hstep-tree4](hstep-tree4.md) and both preceding leaf notes.
The registry has no separate CFW or C-REFLECT owner.
Its H-C-MARK row remains open and unowned.
The separate tower-localization and stage-admission problems are not taken over here.

I fetched main at `1e0d3b58dcda7f83152b0bb51729260247454d65` and read its workflow and worker procedure.
I fetched the two PRs containing the closest recorded hits.
The lead's negative searches of #10133 and #10134 are reused.

| Primary hit checked | Closeness and use |
|---|---|
| #10114, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `SQ.md` 1401–1415, 1458–1467 | Exact action reflection; curvature regularity with a controlled source. Neither identifies the reflected hard rows or prescribed nodes. |
| Same head, `OFFGLOB2_55.md` 847–866 | The relevant free-boundary application remains open. |
| #10141, `fb99b4dddc7254e6124ac124887d58eeb3a77802`, `research/ym4d/library/fp1.md` 142–168, 246–258 | Exact flat-fibre algebra and current-scale kernels. No estimate for the correcting gradient or fine-mesh density is supplied. |
| Same head, `out-mu.md` 8–32, 69–82, 180–189 | Uniqueness and nesting on admitted windows with literal averages. Changed-boundary admission is still required. |

The #10114 paths have prefix `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Credit their Claude and Codex contributors.
The #10141 snapshot is this project's prior work, not an independent check.

## 1. Scope and ports

Codex, 2026-11-08. FINISH row 591. Research base `fef8cebc000e98ab1a69a6b63d41b43ed754ce50`.
Research text, not an audit. This note grants no status.
No computation discharges a mathematical step.
New arguments here have not been checked by another provider.

Result: stopping condition (c). CFW remains open after the three routes in §§3–5.
The kill test refutes a direct-reflection shortcut, not CFW.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, for every manuscript input.
Credit **Tadeusz Bałaban** for the averaging, constrained-background and localization methods.

- **SA:** [outline, `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
- **I:** [complete account I, `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
- **Y:** [YM4_1400, `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).

The three requested `/tmp` copies already existed and were reused without refetching.
The SA README, relevant index rows, neighbouring rows and obligations guided the excerpts.
The CA 4.12–4.19 index guided its boundary and minimizer excerpts.
The named scratch paper directory is absent.
I used the separately specified `~/ym4d-papers/cmp*.txt` copies, in bounded ranges.
Paper equation numbers identify the Bałaban results; text line numbers are retrieval aids.

| Port or scope check | Exact source and limit |
|---|---|
| Literal flat row and endpoint covariance | SA 8467–8517; Bałaban CMP 98, (14)–(15), text 126–148. Reuse the corner-rooted composition in `leaf-tbflat`, §2. |
| Original inputs and full saddle | SA 5665–5727, 11718–11805. Keep independent-current matching and every hereditary condition. |
| Boundary subtraction | SA 12226–12266. Its decay implication assumes the correct weighted inverse and complete force. |
| Prescribed comparison readouts | Y 13223–13427. The potential, first difference and contracted second readout are distinct from an arbitrary fine-site gauge. |
| Native boundary estimates | Y 27666–27729, 31944–31980 use bare fine-scale boundary rows. They do not cover the retained top-row rim. |
| Account's local minimizer | I 43098–43155 cites the block-scale theorem. I 45135–45160 retains a different boundary compatibility obligation. |
| Meaning of a free response | I 58835–58855 is an infinite-volume walk limit. Bałaban CMP 109, (4.35), text 2107–2129, compares inset reads. |
| Bałaban boundary method | CMP 96, p.229, text 274–322 distinguishes graded boundary conditions from sharp Neumann boundaries. CMP 122a, (1.56)–(1.59), text 664–693, uses an already controlled localized response. |

These checked passages do not supply the exact CFW statement.
This is a bounded source comparison, not a claim that every page was searched.
The existing finite transfer, scalar cancellation, null-space proof and failed shortcuts are reused.
They are not re-proved below.

## 2. Kill test first

**Outcome: direct row reflection fails; no admissible CFW counterexample is obtained.**
Here is the failed identity, with its exact size.
It concerns the proposed unfolding, not the original common input domain.

Put $`h=1/n`$, $`K\ge2`$, $`M=Kn`$, and use slab sites $`r=0,\ldots,M-1`$.
Double to the normal circle of $`2M`$ sites.
Reflect across the two fine-bond midplanes.
Let $`E_0`$ copy scalars evenly.
Let $`E_1`$ copy tangential components evenly and normal components oddly, with zero crossing normal links.
This is the linear action reflection of #10114, `SQ.md` 1401–1415.
Let $`E_{c,0},E_{c,1}`$ be the corresponding extensions on top blocks and top bonds.
The top roots are their prescribed corners.

Take the scalar $`\phi(r)=hr`$ on the slab, constant in tangential directions.
Then $`a=D\phi`$ has $`a_1=1`$, zero other components, zero curl and zero first differences.
For the coarse row crossing the right mirror, endpoint covariance gives

```math
 (Q_{\rm per}E_1a)_{K-1,K}
 =(r_{\rm per}E_0\phi)_K-(r_{\rm per}E_0\phi)_{K-1}
 =(K-h)-(K-1)=1-h.
 \tag{1}
```

Direct odd reflection would assign this row zero.
Thus $`Q_{\rm per}E_1=E_{c,1}Q_X`$ is false for every $`n>1`$.
This calculation uses the literal endpoints. It is independent of the internal path choices.

A stronger attempted repair also fails.
Suppose $`E_1a+D\psi`$ keeps every slab bond unchanged and gives the reflected crossing row zero.
Fix $`\psi=0`$ at one original root.
The unchanged bonds make $`\psi=0`$ on the connected slab.
Equation (1) then forces $`\psi(K)=-(1-h)`$.
The first crossing fine bond consequently has correction

```math
 D\psi(M-1,M)=-(1-h)/h=-(n-1).
 \tag{2}
```

So this correction cannot have a mesh-independent potential bound.
It fails because it demands exact restriction, the zero reflected row, and a bounded crossing potential simultaneously.
Allowing a bounded residual gauge inside a top collar removes this particular obstruction.
Section 3 constructs that correction.

The field in (1) has not been identified with the prescribed saddle representative.
Its gauge equations and original hereditary input record have not been supplied.
Therefore (1)–(2) refute those operator shortcuts, not C-REFLECT in its full form or CFW.
The earlier logarithmic surface packet remains excluded in the scalar sector of `leaf-cface`, §2.
It is not repeated as a candidate input.

## 3. Route 1: literal reflection, including the node defect

Write the already ported literal rows as

```math
 Q_X=S_X-d_c\sigma_X,\qquad
 Q_{\rm per}=S_{\rm per}-d_c\sigma_{\rm per}.
 \tag{3}
```

Here $`\sigma`$ is the actual composed path primitive, including its path multiplicities.
The identities come from SA 8467–8517 and Bałaban CMP 98, (14)–(15), as ported in `leaf-tbflat`, §2.
We keep the corner roots.

The straight rows obey

```math
 S_{\rm per}E_1=E_{c,1}S_X,\qquad
 d_cE_{c,0}=E_{c,1}d_c.
 \tag{4}
```

For a tangential row, reflection permutes its starting sites and leaves the straight segment tangential.
For a noncrossing normal row, it reverses the segment and exchanges its endpoint blocks.
For a crossing normal row, pair each starting site with its reflected endpoint.
Their straight path sums have opposite signs. Crossing fine links contribute zero.
These pairings preserve the averaging weights and prove (4), including the crossing rows.
They also apply when there is only one normal top block.

Define the **literal row defect at the nodes**

```math
 T_h=E_{c,0}\sigma_X-\sigma_{\rm per}E_1.
 \tag{5}
```

Substituting (3) into (4) gives the exact row identity

```math
 Q_{\rm per}E_1=E_{c,1}Q_X+d_cT_h.
 \tag{6}
```

No extra boundary datum was introduced.
The defect vanishes at original block roots because the internal path constructions agree there.
For a gradient, endpoint telescoping gives the sharper identity

```math
 T_hD\phi=r_{\rm per}E_0\phi-E_{c,0}r_X\phi.
 \tag{7}
```

Indeed $`\sigma D=q_s-r`$ and $`q_{s,\rm per}E_0=E_{c,0}q_{s,X}`$.
Equation (1) is one instance of (7).

The composed path estimate already proved in `leaf-tbflat`, §2, gives
$`\|\sigma_X\|_{\infty\to\infty},\|\sigma_{\rm per}\|_{\infty\to\infty}\le C_L`$.
It is an absolute row bound, uniform in $`m`$.
Thus $`\|T_h\|_{\infty\to\infty}\le2C_L`$.

Choose a fixed smooth bump at each top root, with disjoint supports of radius less than $`1/3`$.
Sampling their linear combination on the fine lattice defines $`I_h`$ with

```math
 r_{\rm per}I_h=1,\qquad
 \|D^j I_h\|_{\infty\to\infty}\le C_j\quad(0\le j\le3).
 \tag{8}
```

For small tangential periods, periodize the same bumps.
Top roots still have distance at least one in each noncollapsed direction.
Finite differences are integrals of derivatives, which proves the uniform bounds.
This is the existing smooth interpolation device from `leaf-tbflat`, now applied to (5).
It is an auxiliary gauge, not the prescribed slice.

Put

```math
 \widetilde E_1=E_1-DI_hT_h.
 \tag{9}
```

Then

```math
 Q_{\rm per}\widetilde E_1=E_{c,1}Q_X,
 \qquad d\widetilde E_1=dE_1,
 \qquad R\widetilde E_1a=a-D_XRI_hT_ha.
 \tag{10}
```

The last correction fixes every original top root.
Its restriction is supported in a fixed top collar of the mirrors.
Its potential, first differences and contracted second differences are bounded by $`C\|a\|_\infty`$.
These claims concern the correction alone; they do not assert a full derivative bound for $`E_1a`$ across the mirror.
Unlike (2), this construction allows a residual gauge in that collar.

There is also an exact unforced consequence on the physical quotient.
Take the free curvature minimizer with straight rows $`S_Xa=d`$.
Its reflected field has rows $`E_{c,1}d`$ by (4).
For any periodic zero-row variation, average it with its reflection.
The antisymmetric part pairs to zero with the reflected curvature.
The symmetric part restricts to a zero-row slab variation.
The doubled first variation is therefore twice the vanishing slab first variation.
This proves periodic stationarity; positivity of the quadratic form proves minimality.
FP1's existing equality of straight and literal curvature minima transfers this conclusion to the literal fibres.
Thus the **unforced physical curvature minimizer reflects exactly**, modulo gauge.
This conclusion does not identify the prescribed potential representative.

### The remaining full-system equation

The required C-REFLECT identity acts on the original input $`z`$, not on a freely supplied solution $`a`$.
In (9) the correction contains $`T_ha_X(z)`$, where $`a_X`$ is the unknown free-face response.
Putting that quantity into the input lift would use the response whose estimate is being sought.

For the actual prescribed gauge block, the row defect is explicitly

```math
 G_{\rm per}\widetilde E_1a_X-E_gs_X
 =G_{\rm per}E_1a_X-E_gs_X
       -G_{\rm per}DI_hT_ha_X,
 \qquad G_Xa_X=s_X.
 \tag{11}
```

No chosen $`E_g`$ has yet converted (11) into bounded coefficients on $`\mathcal J_hz`$.
The transformed force has the companion transpose term.
For any periodic force $`j`$ and slab test field $`v`$,

```math
 \langle j,\widetilde E_1v\rangle
 =\langle j,E_1v\rangle
   -\langle D^*j,I_hT_hv\rangle.
 \tag{12}
```

All adjoints here use the actual physical pairings.
The last term vanishes for a compatible divergence-free physical force.
The original independent-current and gauge equations do not permit declaring it zero.
SA 11798–11805 requires their complete matching; Y 30405–30475 specifies the native straightened convention.
The latter uses site means, not literal root evaluation.

**Route 1 fails to close at (11)–(12).**
Equations (6)–(10) solve the literal row defect modulo a bounded auxiliary gauge.
They do not supply $`E_h,N_h`$ in C1 on the original input record.
The physical quotient argument is insufficient for that stronger identity.

## 4. Route 2: C-BAND by physical-space Fourier bounds

The scalar cancellation in `leaf-cface`, (2), already identifies the correct source difference.
We keep that difference before taking absolute values.
The following extends its high-frequency estimate to all three tangential directions.
It avoids the divergent Fourier-orthogonality bound in that note's Route A.
It does not replace the vector saddle by scalar equations.

Let $`\theta\in[-\pi,\pi]^3`$ be the fine tangential frequency and put

```math
 \lambda_h(\theta)=\frac2h
       \left(\sum_{j=2}^4\sin^2(\theta_j/2)\right)^{1/2},\qquad
 \alpha_h(\theta)=2\operatorname{arsinh}(h\lambda_h(\theta)/2).
 \tag{13}
```

Choose a smooth dyadic partition in $`\lambda_h`$ above frequency one.
Write $`P_\rho`$ for a band with $`\rho=2^\nu\ge1`$ and
$`\rho/2\le\lambda_h\le2\rho`$.
The last bands may meet the edge of the fine Brillouin torus.
Use periodic multipliers there. Bands above the spectrum are zero.

We first give the coefficient estimate used below.
For a smooth periodic multiplier $`m`$ in three variables, suppose

```math
 \operatorname{vol}(\operatorname{supp}m)\le C\delta^3,
 \qquad
 \|\partial^\beta m\|_\infty\le A\delta^{-|\beta|}
       \quad(|\beta|\le4),\qquad 0<\delta\le1.
 \tag{14}
```

Its infinite-lattice coefficients satisfy

```math
 |\check m(l)|\le C A\delta^3(1+\delta|l|)^{-4},
 \qquad \sum_{l\in\mathbb Z^3}|\check m(l)|\le C A.
 \tag{15}
```

For $`\delta|l|\le1`$, integrate $`|m|`$ over its support.
Otherwise choose a coordinate with $`|l_j|\ge|l|/\sqrt3`$ and integrate four times by parts.
Periodicity removes boundary terms; the derivative integral is at most $`CA\delta^{-1}`$.
This proves the first bound, after increasing its constant.
Counting lattice shells proves the second: the tail is bounded by a constant times $`\int_1^\infty t^{-2}dt`$.
On any finite tangential torus, the sampled multiplier has the periodized coefficients.
Absolute summation therefore gives the same bound, independently of its periods.
All frequency aliases are present in this assertion.

For the scalar complete bulk source $`F`$, the reflected source-to-face multiplier at normal source depth $`s`$ is

```math
 m_{r,s}(\theta)
 =P_\rho(\theta)\,\frac{h^2}{2\sinh\alpha_h(\theta)}
                    e^{-(r+s+1)\alpha_h(\theta)}.
 \tag{16}
```

It acts on $`F_s-F_{-s-1}`$.
This is the existing scalar transfer with the tangential Laplacian eigenvalue in (13).
The same one-dimensional normal recurrence applies to that eigenvalue.

On the band, $`\alpha_h\asymp h\rho`$ and $`\sinh\alpha_h\asymp h\rho`$.
The comparison constants are uniform because $`h\lambda_h\le2\sqrt3`$.
Use $`\delta=\min(h\rho,1)`$ in (14).
Differentiating the smooth band symbol up to four times gives

```math
 \|\partial^\beta m_{r,s}\|_\infty
 \le C_\beta\frac h\rho\delta^{-|\beta|}
                 e^{-a\rho h(r+s+1)}.
 \tag{17}
```

Here and below a fixed smaller $`a>0`$ absorbs the derivative polynomials.
To check the scaling, on the band
$`|\partial^\beta\alpha_h|\le C_\beta\delta^{1-|\beta|}`$ for $`1\le|\beta|\le4`$.
For the reciprocal prefactor, each derivative costs $`C\delta^{-1}`$ relative to its size $`h/\rho`$.
Differentiating the exponential adds powers of $`\rho h(r+s+1)`$.
For each of the finitely many powers, $`t^j e^{-bt}\le C_{j,b}e^{-bt/2}`$.
This proves (17) by the product rule.
When $`h\rho`$ is bounded below, the same calculation takes place on the whole compact frequency torus.

A tangential first difference multiplies (16) by $`(e^{i\theta_j}-1)/h`$.
A normal first difference multiplies it by $`(e^{-\alpha_h}-1)/h`$.
Each costs at most $`C\rho`$, with the same derivative scaling.
Equations (15)–(17) thus bound a single normal-source row by

```math
 \|m_{r,s}^{\vee}\|_1\le C(h/\rho)e^{-a\rho h(r+s+1)},
 \qquad
 \|(D m_{r,s})^{\vee}\|_1\le Ch e^{-a\rho h(r+s+1)}.
 \tag{18}
```

Sum over $`s\ge0`$ using $`e^t-1\ge t`$.
The two original source halves cost a factor two.
For any fixed $`0<c<a`$, this yields

```math
 \sup_r e^{crh}
       \|K^{\rm scalar}_{\rho,\,\mathrm{potential}}(r,\cdot)\|_1
       \le C\rho^{-2},
 \qquad
 \sup_r e^{crh}
       \|K^{\rm scalar}_{\rho,\,\mathrm{first}}(r,\cdot)\|_1
       \le C\rho^{-1}.
 \tag{19}
```

On a slab, use the images already displayed in `leaf-cface`, (7).
Their additional distances are multiples of $`2K`$ in top units.
Since $`K\ge1`$ and $`\rho\ge1`$, their bounds sum geometrically with a uniform constant.
Replace $`rh`$ by distance to the nearer changed face.
The scalar contracted Laplacian is zero on every full interior stencil.
Thus (19) is a genuine summable high-band result for that scalar combined transfer.
It makes no claim about the low band or a missing boundary stencil.

### Where the vector application fails

The original transfer is `leaf-cface`, (11), with its row and frame blocks.
It is not diagonal in the fine aliases
$`\theta_{j,q}=(\kappa_j+2\pi q)/n`$.
Those blocks must be eliminated before applying (15).

On the actual finite slice, reuse the exact Schur inverse from `leaf-tbflat`, (18).
Its coarse factor is $`W=qA^{-1}q^*`$, with $`A=H+q^*q`$.
Its frequency derivatives contain

```math
 \partial W^{-1}=-W^{-1}(\partial W)W^{-1}.
 \tag{20}
```

The fine band does not commute with $`q^*W^{-1}q`$.
Even the straight-row filter couples aliases at a nonzero coarse phase; see `leaf-cface`, (9).
The prescribed frame contributes additional blocks.

The attempted use of (17) therefore stops at a specific missing estimate:
four scaled tangential derivatives, with summed fine-channel coefficients, of the **combined** Schur response.
Bounds for the scalar diagonal entries do not bound (20) with those channel sums.
The existing current-scale Gram estimate does not assert this fine-scale estimate.
Taking absolute values before the two responses are subtracted would also discard the cancellation in (16).

**Route 2 supplies (19), but does not prove C-BAND for the original vector inputs.**
No low mode or row channel has been dropped from the requested statement.

## 5. Route 3: sum the literal paths before taking the band bound

This route keeps the literal path operators instead of estimating the Schur inverse first.
It uses their scale decomposition to test whether the node correction supplies the missing smoothing.
The primitive's unweighted bound was already proved in `leaf-tbflat`.
The new estimate here is its bound on a high tangential band.

Put $`s_r=L^rh`$, for $`0\le r<m`$.
Let $`S_{s_r}`$ be the raw straight average along a path of physical length $`s_r`$.
Let $`R_{r+1,m}`$ restrict site values to their prescribed later roots.
Iteration of the existing primitive recursion gives

```math
 \sigma_m=\sum_{r=0}^{m-1}R_{r+1,m}\sigma_L S_{s_r}.
 \tag{21}
```

The row norm of $`R_{r+1,m}`$ is one.
In raw coarse bond coordinates, $`\sigma_L`$ has row norm at most $`C_L`$.
The physical length is included in $`S_{s_r}`$.

Split a band $`P_\rho`$ into three smooth pieces.
On piece $`j`$, require $`|e^{i\theta_j}-1|/h\ge c_0\rho`$.
Such a partition exists because the sum of their squared magnitudes is $`\lambda_h^2`$.
Apply (14)–(15) to its multiplier divided by $`(e^{i\theta_j}-1)/h`$.
The resulting operator $`B_{\rho,j}`$ satisfies

```math
 D_jB_{\rho,j}=P_{\rho,j},\qquad
 \|B_{\rho,j}\|_{\infty\to\infty}\le C/\rho.
 \tag{22}
```

Let $`A_{N,j}=N^{-1}\sum_{t=0}^{N-1}\tau_j^t`$ be a fine site mean, with $`N=s_r/h`$.
The finite sum telescopes:

```math
 A_{N,j}D_j=(\tau_j^N-1)/s_r.
 \tag{23}
```

The straight average contains this site mean in every tangential direction.
Its other means have row norm one; its raw longitudinal path contributes length $`s_r`$.
Equations (22)–(23), followed by sampling at the coarse sites, give

```math
 \|S_{s_r}P_\rho\|_{\infty\to\infty}
       \le C\min(s_r,\rho^{-1}).
 \tag{24}
```

Sampling cannot increase a row norm.
The same proof works for every tangential period and every component of the one-form.
It does not choose a central alias.

Sum (24) in (21).
The terms with $`s_r\rho\le1`$ form a geometric sum bounded by $`C_L/\rho`$.
There are at most $`1+\log_L\rho`$ remaining terms since $`s_r<1`$.
Consequently

```math
 \|\sigma_mP_\rho\|_{\infty\to\infty}
       \le C_L\frac{1+\log\rho}{\rho}
       \le C_L'\rho^{-1/2}.
 \tag{25}
```

For the last inequality use $`\log\rho=\int_1^\rho t^{-1}dt\le2\sqrt\rho`$.
All constants are independent of mesh and depth.
Normal reflection commutes with the tangential filter, so (25) also bounds $`T_hP_\rho`$.
Together with (8), it gives

```math
 \|RDI_hT_hP_\rho\|_{c,1;\,\mathrm{field}\to\mathrm{reads}}
       \le C_{L,c}\rho^{-1/2}.
 \tag{26}
```

The reads in (26) are the potential correction and its first and contracted second differences.
The output lies in a fixed top collar; its normal exponential weight costs a fixed factor.
The input columns in (26) are fine field values.
They are **not** the original normalized input record $`\mathcal J_hz`$.
This distinction prevents using (26) as the desired $`N_h`$ bound.

### Attempt to close the equations with (25)

The exact first saddle row contains

```math
 Q^*\lambda=S^*\lambda-\sigma_m^*d_c^*\lambda.
 \tag{27}
```

An absolute row estimate for $`\sigma_m`$ does not give a bounded volume-force estimate for its adjoint.
The physical weights are essential.
A path term with coefficient $`wh`$, where $`w>0`$ is its fixed averaging weight,
has adjoint coefficient $`wh^{-3}`$ under fine pairing $`h^4\sum`$ and counting node pairing.
Thus even a bounded primitive row can yield an unbounded density if its node load is treated independently.
This calculation concerns a primitive term, not the combined compatible force.

The physical Ward cancellation in `leaf-cbr`, (7)–(9), already removes the last term of (27) when applicable.
For the full saddle, the identity to use instead is

```math
 r^*d_c^*\lambda+D^*G^*\gamma=D^*j.
 \tag{28}
```

It is the original gauge/current compatibility equation, not an optional condition.
The actual new-boundary gauge block and the prescribed restoration must enter its solution.
The native independent-current convention does not assume $`D^*J=0`$; see Y 30475–30501.
Here $`j`$ is the saddle force and $`J`$ is the separate current coordinate.
Their relation must come from the actual defining map.
No independent divergence-free source is substituted for that convention here.

For an unforced physical solution, the known cancellation applies and the quotient reflection of §3 survives.
For the complete requested record, (25) only controls a primitive acting on an already known field band.
It neither bounds the multiplier combination in (27)–(28) nor shows that the saddle preserves that band.
Low-frequency original data may produce several fine aliases through the hard rows.
The required cancellation must therefore be proved after substituting the same original $`z`$ in all three saddle rows.

**Route 3 stops at that combined substitution.**
It proves the summable path estimate (25) and the auxiliary collar estimate (26).
Estimating the adjoint path terms independently fails by the explicit physical-weight calculation above.
Dropping them by the unforced Ward identity would change the input problem.

## 6. The one remaining lemma and result

**Stopping condition (c): CFW remains open after three distinct routes.**
They were complete reflection with literal re-rooting, bandwise Schur elimination, and scale-summed path cancellation.
The failed steps are (11)–(12), the required combined estimate following (20), and (27)–(28).
These are failures of the attempted proofs. They are not an impossibility theorem.

The remaining lemma is exactly CFW, not a new independently forced boundary problem.
For every $`h=L^{-m}`$, normal depth $`K\ge1`$ and tangential top periods $`T_2,T_3,T_4\ge1`$,
retain `leaf-cface`, (8)–(11), its original constrained space $`\mathcal Z_h`$,
its normalized input record $`\mathcal J_h`$, and its complete prescribed readout $`\mathcal A_h`$.
The physical potential, first differences, contracted second readout, nodes and full-stencil currents are all retained.
Find fixed $`c,C>0`$ and matrices $`\mathcal K_h`$ such that

```math
 \mathcal K_h\mathcal J_hz=\mathcal A_hz\quad(z\in\mathcal Z_h),
 \qquad
 \sup_x e^{c\,d(x,\partial_{\rm changed}X)}
           \sum_i|\mathcal K_h(x,i)|\le C.
 \tag{CFW}
```

The coefficients may be extended off the constrained input image.
They must agree with the original response on that image.
Neither an independent surface trace nor the unknown $`a_X`$ may become a new input.
The zero and low bands remain part of CFW.
No new proof or counterexample for them is claimed here.

The kill test refutes exact unchanged-restriction reflection with zero crossing coarse rows and bounded crossing potential.
It does not supply bounded original inputs with an unbounded CFW output.
The correction (9) explains why that route failure does not refute the physical comparison.

The note supplies literal row/node defect identities, a physical quotient reflection, and two summable high-band estimates.
It supplies no complete C-REFLECT or C-BAND estimate on the original input record.
CFW, C-FACE, CBR, TB-BC and renewed-mark payment receive no closure from this note.
After CFW is proved, the next downstream leaf is C-SEAM-LIFT for corners and mixed grades.
That work is not started here.

The author check revisited the endpoint signs, physical adjoint weights, finite-period sums and derivative orders.
It is not an independent check. No numerical proof or numerical kill test was used.

| Item | Status in this research note | Exact limit |
|---|---|---|
| Existing finite transfer and scalar cancellation | Reused with credit | Original domains and prescribed frame retained. |
| Kill test (1)–(2) | Explicit counterexample to the stated direct-reflection shortcut | Not an admitted CFW input or a refutation of CFW. |
| Literal defect and corrected rows (5)–(10) | Written proof; not independently checked | Correction uses the free field and an auxiliary gauge. |
| Unforced physical curvature reflection | Written proof using the existing fibre identity; not independently checked | Quotient statement; no prescribed potential or independent-current estimate. |
| Scalar high-band estimate (19) | Written proof; not independently checked | Complete scalar bulk source, all tangential frequencies in each high band; low band excluded. |
| Composed path and collar bounds (25)–(26) | Written proof; not independently checked | Field-input coefficients; not yet coefficients on the original input record. |
| C-REFLECT | Open | Match (11)–(12) to the actual original current, row and node inputs. |
| C-BAND and CFW | Open after three routes | Uniform combined coefficients after all actual constraints and the frame are eliminated. |
| Corners, mixed grades and nonlinear admission | Unchanged | C-SEAM-LIFT follows a successful CFW supply. |

**First open input: CFW's uniform combined row bound on $`\mathcal J_h\mathcal Z_h`$, including the actual node/current compensation.**
