## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
Its [record](prior/repo-search-2026-11-08.md), §§2 and 8, found no changed-boundary supplier.
[prior/hstep.md](prior/hstep.md), A1.3, A3.2 and W4, retains the boundary, domain and payment distinctions.
No `prior/leaf-cface.md` exists at this pin.

I fetched main at `43a1fcc374711ca50626eca667441d3ca575c7d1` and read its workflow and scoped-worker procedure.
I fetched the following two PR heads and checked the named passages.
The wider search remains the lead's work.

| Checked hit | Closeness to C-FACE; use |
|---|---|
| #10141, `c73ad7b177d94f89ff37b77386936e3d52b48b05`, `research/ym4d/library/out-mu.md` 8–32, 69–82, 180–189 | Admitted-window uniqueness and nesting. It excludes derivative decay and does not admit a changed exterior. |
| Same ref, `fp1.md` 142–168, 246–258 | Exact flat-fibre algebra and current-scale kernels. It expressly leaves the correcting gradient and fine-mesh pointwise bounds uncontrolled. Reused within that scope. |
| #10114, `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `SQ.md` 1401–1415, 1458–1467 | Exact action reflection and a curvature estimate requiring a controlled source. Neither supplies the joint boundary transfer. |
| Same ref, `OFFGLOB2_55.md` 847–866 | Free-boundary localization remains open there. It is not a supplier. |

The #10114 paths are under `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
Credit the Claude and Codex authors of these notes and their recorded checks.
The #10141 snapshot repeats this project's work; it is not independent evidence.

I read the CBR section of [hstep-tree3.md](hstep-tree3.md) and the three specified supplier notes in full.
I also read [pi-native.md](pi-native.md), §3.
The registry has no separate C-FACE or CBR owner; H-C-MARK remains open and unowned.
The matching searches of `open-core.md` and `l17c.md` supply no duplicate C-FACE proof.
FINISH row 581 assigns this leaf.

## 1. Scope and source record

Codex, 2026-11-08. Checkout `64be8397d0cbd948e6d68de25ad0473bf043e215`.
Research text, not an audit. This note grants no status.
New arguments have not been checked by another provider.
No numerical experiment or computer-assisted proof is used.

Result: stopping condition (c). Lemma CFW remains open after three routes.
The kill test yields a scalar cancellation estimate, but no admissible vector counterexample.

Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**, for every manuscript input below.
Credit **Tadeusz Bałaban** for the constrained-background, reflection and localization methods.

**SA** denotes [the outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
**I** denotes [complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
**Y** denotes [YM4_1400](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).
The three requested `/tmp` copies already existed and were reused.
The SA index, neighbouring rows and obligations guided bounded source reads.
The CA 4.12–4.19 index guided its minimizer and localization reads.

| Source | What is available; exact limit |
|---|---|
| SA 5663–5727, R4–R6 | Original potential, derivative, independent-current and hereditary conditions. Keep all of them. |
| SA 11725–11815, BGR1–BGR6 | Exact stationarity and differentiated equations. The independent-current normal form “must be matched” at 11798–11805. |
| SA 12226–12292, BGR28–BGR30 | Complete boundary force and conditional decay. The estimate starts: “Suppose the inverse has weighted row bound”. |
| I 43098–43155 | Free inner action and constrained criticality. The block-scale theorem is “used here by statement”. This is a cited input, not a proof of C-FACE. |
| I 45135–45160 | Proposed tower localization. Crossing-constraint compatibility “is not proved here”. This separately owned problem is not attacked below. |
| Y 27666–27729, 31944–31980 | The native proof uses bare boundary rows and the equality of fine and boundary scales. TB deletes those rows. |
| Y 13223–13427 | Comparison potential, first differences, contracted second readout and prescribed node identity. No bound on the gauge at every fine site is asserted. |
| I 58835–58855 | The “free boundary conditions” response here is the infinite-volume walk limit. It is not a new finite top-rim theorem. |

The native inverse chain recorded in `pi-native.md`, §3, is already available.
It is not rederived here.
The targeted searches found no exact C-FACE proof in Y or I.
This is a bounded source-search conclusion, not a claim about all literature.
The authorized scratch paper directory is absent.
Bałaban's equation locators are therefore reused from `hcm-tb.md` and `leaf-tbflat.md`; no new paper verification is claimed.

The target is the flat-face restriction of CBR, with top spacing one and $`h=L^{-m}`$.
Use a normal slab of whole top blocks and periodic tangential directions.
Keep the exact force of `leaf-tbflat.md`, (11), its literal corner-rooted rows, and its prescribed node frame.
Include every tangential frequency, every required output and the exponential normal-distance weight.
A surface-force estimate with independently chosen data would be a different statement.

## 2. Kill test first: test all realizations with a bounded scalar bulk equation

**Outcome: no admissible counterexample.**
The logarithmic packet remains a counterexample to the separate surface estimate only.
The following calculation excludes every bounded-bulk-source realization in its transverse scalar sector.
It does not exclude every original vector input.

Use one color, $`a_3=a(r,l)`$, and independence of coordinates 3 and 4.
Let $`r\in\mathbb Z`$ and $`l\in\mathbb Z/n\mathbb Z`$, with $`h=1/n`$.
Impose zero mean in $`l`$ on each normal slice.
Suppose the actual equation in this sector is $`H_o a=F`$, where $`H_o=-\Delta_h`$.
Require $`a`$ and $`F`$ bounded on the two-sided normal lattice.
Here $`F`$ means this equation's complete source, not the independent-current coordinate.

First cut at $`r=0`$ and keep $`r\ge0`$.
Let $`u`$ be the bounded zero-mean solution of $`H_Nu=F|_{r\ge0}`$ with the free-end Laplacian.
The reflected Green function below constructs this solution.
Then $`w=u-a|_{r\ge0}`$ solves exactly

```math
 (H_Nw)_{r,l}=1_{\{r=0\}}\frac{a_{0,l}-a_{-1,l}}{h^2}.
 \tag{1}
```

Every straight top row of $`w`$ vanishes by its tangential mean.
The literal correction in `leaf-tbflat.md`, (1a), restores the literal zero rows without changing curvature.
Its prescribed-frame identification remains outside this scalar calculation.

For $`1\le j<n`$, define

```math
 \theta_j=\frac{2\pi j}{n},\qquad
 \alpha_j=2\operatorname{arsinh}|\sin(\theta_j/2)|,\qquad
 \lambda_j=e^{-\alpha_j}.
```

The full-line Green function of this mode is $`h^2\lambda_j^{|r-s|}/(2\sinh\alpha_j)`$.
Substitution verifies its homogeneous recurrence away from $`r=s`$.
At $`r=s`$, the recurrence gives one.
The two homogeneous solutions are $`\lambda_j^r`$ and $`\lambda_j^{-r}`$.
No nonzero combination is bounded at both ends, so this inverse is unique on bounded sequences.

Reflecting its source across $`-1/2`$ gives the free-end Green function.
Subtract the full-line solution before taking absolute values. The result is

```math
 \widehat w_r(j)=\frac{h^2}{2\sinh\alpha_j}
   \sum_{s\ge0}\lambda_j^{r+s+1}
       \bigl(\widehat F_s(j)-\widehat F_{-s-1}(j)\bigr).
 \tag{2}
```

This is the combined transfer from the original source.
It is not the transfer from an independently specified normal trace.
The normal trace has acquired one extra smoothing factor through the original equation.

Here are absolute row bounds for (2), including every tangential frequency in this sector.
Put $`q_j=\min(j,n-j)`$.
The inequalities $`\sin(\pi q/n)\ge2q/n`$ and $`\operatorname{arsinh}s\ge s/2`$, for $`0\le s\le1`$, imply
$`\alpha_j\ge2q_jh`$.
Also

```math
 \frac{|e^{i\theta_j}-1|}{2\sinh\alpha_j}\le\frac12,
 \qquad
 \frac{1-\lambda_j}{2\sinh\alpha_j}\le\frac12.
 \tag{3}
```

For a multiplier $`m_j`$ on this circle, its convolution kernel satisfies

```math
 \sum_{l=0}^{n-1}\left|\frac1n\sum_{j=1}^{n-1}m_j e^{i\theta_jl}\right|
 \le\left(\sum_{j=1}^{n-1}|m_j|^2\right)^{1/2}.
 \tag{4}
```

This follows from Cauchy–Schwarz and finite Fourier orthogonality.
No computed Fourier sum is used.
For either first difference of (2), (3) bounds $`|m_j|`$ by $`(h/2)\lambda_j^{r+s+1}`$.
Sum the geometric series in $`q_j`$ in (4). Its square root is at most

```math
 C h\,e^{-h(r+s+1)}\bigl(h(s+1)\bigr)^{-1/2}.
 \tag{5}
```

For example, after extracting $`e^{-2h(r+s+1)}`$, the remaining squared sum is bounded by
$`2/(e^{2h(r+s+1)}-1)\le1/[h(r+s+1)]`$.
The sum of (5) over $`s\ge0`$ is at most $`Ce^{-hr}`$.
Indeed, compare its decreasing summand with the integral of $`e^{-t}t^{-1/2}`$.
That integral is finite by splitting at one.

For the potential, use $`h^2/(2\sinh\alpha_j)\le h/(4q_j)`$ in (4).
The inequality $`\sum_{q\ge1}q^{-2}\le2`$ gives a row bound $`Ch e^{-h(r+s+1)}`$.
Sum over $`s`$ again. The two source halves in (2) cost a factor two.
Thus

```math
 \sup_{r\ge0}e^{hr}
   \bigl(\|w_r\|_\infty+\|D_1w_r\|_\infty+\|D_2w_r\|_\infty\bigr)
 \le C\|F\|_\infty.
 \tag{6}
```

On every full interior stencil, $`-\Delta_hw=0`$.
No current claim is made on an incomplete stencil.
For $`n=1`$, the zero-mean sector is zero.

The estimate also holds on a slab of $`K`$ whole blocks, uniformly in $`K\ge1`$.
Write $`M=Kn`$. The left boundary solution for one mode has normal factor

```math
 \frac{\lambda_j^r+\lambda_j^{2M-1-r}}
 {(\lambda_j^{-1}-1)(1-\lambda_j^{2M})},
 \qquad 0\le r<M.
 \tag{7}
```

Multiplying (7) by $`a_0-a_{-1}`$ solves the left term of (1) and has zero right boundary force.
Substitution at the two endpoints verifies this assertion.
Reflect (7) for the right boundary force $`a_{M-1}-a_M`$.
Insert the full-line Green formula for both traces.
Expand $`(1-\lambda_j^{2M})^{-1}=\sum_{p\ge0}\lambda_j^{2pM}`$ before estimating.
Each term is a kernel already bounded in (5), at an image distance.
Since $`\lambda_j^M\le e^{-2K}`$, those image estimates sum uniformly in $`K`$.
Equation (6) follows with $`hr`$ replaced by $`h\min(r,M-1-r)`$ and a fixed smaller rate.
Only existing normal differences are read on the slab.

Now reuse the packet of `leaf-tbflat.md`, (19)–(21), without rebuilding it.
Its boundary curvature is at least $`\frac14\sum_{j\le\lfloor n/16\rfloor}j^{-1}`$.
If it came from (2), (6) would force $`\|F\|_\infty`$ to grow at least logarithmically.
This rules out every uniformly bounded $`F`$ realization in the stated sector.
It strengthens the earlier test, which rejected only one realization with source of order $`1/h`$.

The missing transfer to C-FACE is explicit.
The original vector equation contains row multipliers and a prescribed gauge.
Its independent current is not automatically $`F`$.
Neither (6) nor the original R4 bounds identify those terms with a bounded scalar source.
The hereditary tests also remain mandatory.
No face failure has been produced, so there is no failure to transfer to an actual stage.

## 3. The joint Fourier problem and the one remaining lemma

Use $`K`$ normal top blocks and tangential top periods $`T_2,T_3,T_4`$.
Decompose under translations by whole top blocks in the three tangential directions.
For each coarse phase $`\kappa_\nu=2\pi k_\nu/T_\nu`$, retain all fine aliases

```math
 \theta_{\nu,q}=\frac{\kappa_\nu+2\pi q}{n},
 \qquad 0\le q<n,\quad \nu=2,3,4.
 \tag{8}
```

Thus each coarse phase has $`n^3`$ fine tangential modes, for each normal coordinate and vector component.
Keeping only the central alias would change the problem.

The exact straight-row filter helps locate the coupling.
Define $`b_n(\theta)=n^{-1}\sum_{v=0}^{n-1}e^{iv\theta}`$.
For a bulk fine plane wave in the corner-rooted convention, the physical length-one straight row has filter

```math
 s_\mu(\theta)=b_n(\theta_\mu)\prod_{\nu=1}^4b_n(\theta_\nu),
 \qquad
 b_n(\theta_{\nu,q})=
 \frac{1-e^{i\kappa_\nu}}{n(1-e^{i\theta_{\nu,q}})}.
 \tag{9}
```

At a removable zero, use the defining finite sum.
The first formula follows by summing the $`n^4`$ starting sites and the $`n`$ bonds of each straight segment.
The factor $`h=1/n`$ converts the fine potential to its path integral.
Normal rows in the slab use those finite sums only on complete retained carriers.
No missing exterior bond is inserted through a normal Fourier transform.

The literal rows are still

```math
 Q=S-d_c\sigma,\qquad QD=d_c r,\qquad SD=d_c q_s,
 \qquad \sigma D=q_s-r.
 \tag{10}
```

Here $`r`$ evaluates at prescribed roots and $`q_s`$ is the site block mean.
The path primitive $`\sigma`$ is the composed literal primitive of `leaf-tbflat.md`, §2.
Equation (10) is the already ported FP1 fibre algebra, with that note's corner-root correction.
Credit Sussman and Alpoge, with Claude and Codex, for SA 8467–8517's centered-grid identities.
The corner-root realization and composed path bound are reused from `leaf-tbflat.md`, §2.
It preserves its actual path multiplicities.
It is not permission to discard the last term of $`Q`$.

At $`\kappa=0`$, a nonzero tangential alias makes the appropriate block mean vanish.
This explains why §2 is tractable.
At general $`\kappa`$, (9) is nonzero for many aliases.
The hard rows therefore couple fine frequencies, even at a flat background.

For completeness, the exact finite transfer can be organized without separating the surface force.
Write $`\Psi_o=(a_o,\lambda_o,\gamma_o)`$ and retain the saddle of `leaf-tbflat.md`, (9).
Use $`\mathcal E_o z`$ and $`\mathcal E_X z`$ for the two original right sides.
Let $`\mathscr R=\operatorname{diag}(R,P,P_g)`$ use that note's restriction maps.
On independent compatible rows, the Fourier blocks satisfy

```math
 \widehat{\delta\Psi}(\kappa)=\mathcal T_h(\kappa)\widehat z(\kappa),
 \qquad
 \mathcal T_h=
  (\mathcal S_X^N)^{-1}\mathcal E_X
   -\mathscr R\mathcal S_o^{-1}\mathcal E_o.
 \tag{11}
```

Indeed, multiplying (11) by $`\mathcal S_X^N`$ gives
$`\mathcal E_Xz-\mathcal S_X^N\mathscr R\Psi_o`$.
Expanding this expression gives precisely the three rows of the original force (11).
Old multipliers are the responses to the same $`z`$; they are not extra bounded inputs.
Equation (11) is an exact finite symbol representation.
It does not evaluate or bound its inverse entries.

Finite solvability uses the earlier constrained-minimum argument.
There is one addition for periodic tangential directions.
A curl-free zero-row field has zero period on each of the three fundamental cycles.
Sum its literal rows around the corresponding coarse cycle; internal paths telescope to that fine period.
The existing path proof then makes the field a gradient with constant root values.
The prescribed residual gauge removes it.
This establishes finite physical uniqueness on the compatible quotient, not a uniform estimate.

Here is the precise unresolved lemma, called **CFW** in this note.
It is the uniform row-sum part of C-FACE after (8)–(11).

Let $`\mathcal Z_h`$ be the original linearized common input space restricted to this face geometry.
Let $`\mathcal J_hz`$ list its original normalized input reads, so
$`\|\mathcal J_hz\|_\infty=\|z\|_{\rm original}`$.
Retain the linearized hereditary and frame relations in this record.
It does not acquire a new scalar-source or trace bound.
Let $`\mathcal A_hz`$ be the required readouts of (11), including the original node restoration.
Use the exact derivative of that restoration; any direct datum contribution remains in $`\mathcal A_h`$.
The output rows include the potential, first differences, contracted second readout and the specified full-stencil currents.

**Lemma CFW.** For every original input, construct its compatible row lift and prescribed node restoration.
There are $`c,C>0`$, independent of $`n,K,T_2,T_3,T_4`$, and coefficient matrices $`\mathcal K_h`$ such that

```math
 \mathcal K_h\mathcal J_hz=\mathcal A_hz
       \quad(z\in\mathcal Z_h),\qquad
 \sup_{x\ {m read}}e^{c d(x,\partial_{\rm changed}X)}
       \sum_i|\mathcal K_h(x,i)|\le C.
 \tag{CFW}
```

All physical weights are included in these normalized coefficients.
The sum is over original input reads, including their component labels.
It is not a sum against independently variable force, multiplier and gauge data.
Different coefficient rows may represent the same functional on the constrained input record.
Such freedom may encode the required cancellation; it must not change that functional.

CFW would give C-FACE by the triangle inequality, on exactly the original inputs.
Conversely, no bound for a different surface-input space is used as a substitute below.
The next three routes attack this same lemma.

## 4. Route A: convert exact mode estimates by Fourier orthogonality

The calculation in §2 suggests applying (4) to every alias block of (11).
This keeps the original source coupling.
It differs from estimating the omitted-plaquette force as independent surface data.

The attempted conversion already loses uniformity in a larger transverse scalar sector.
Let $`a_3`$ depend on the normal coordinate and on coordinates 2 and 4.
Both tangential periods are one; the field remains divergence-free.
Remove the joint tangential mean.
Equation (2) holds with

```math
 \alpha_{j,k}=2\operatorname{arsinh}
       \sqrt{\sin^2(\pi j/n)+\sin^2(\pi k/n)}.
```

For the direction-2 derivative at the boundary, the normal-source row at depth $`s`$ has multiplier

```math
 m_{j,k,s}=
  \frac{h(e^{2\pi i j/n}-1)}{2\sinh\alpha_{j,k}}
          e^{-(s+1)\alpha_{j,k}}.
 \tag{12}
```

Set $`m_{0,0,s}=0`$, consistently with the removed mean.

Fourier orthogonality would bound the whole absolute row by
$`\sum_{s\ge0}(\sum_{(j,k)\ne(0,0)}|m_{j,k,s}|^2)^{1/2}`$.
That proposed upper bound itself diverges with refinement.

Here is a hand lower bound on this *upper-bound expression*.
Put $`t=s+1`$, with $`1\le t\le\lfloor n/64\rfloor`$.
Keep integers $`j,k`$ between $`\lceil n/(16t)\rceil`$ and $`\lfloor n/(8t)\rfloor`$.
There are at least $`n/(32t)`$ choices in each direction.
On this square, $`\alpha_{j,k}\le2/t`$.
The ratio $`|e^{2\pi i j/n}-1|/(2\sinh\alpha_{j,k})`$ has a fixed positive lower bound.
Indeed, its numerator is at least $`1/(4t)`$, while its denominator is at most $`4\cosh(2)/t`$.
Also $`e^{-t\alpha_{j,k}}\ge e^{-2}`$.
Consequently

```math
 \left(\sum_{j,k}|m_{j,k,s}|^2\right)^{1/2}\ge\frac{c_0}{t},
 \qquad
 \sum_{s\ge0}\left(\sum_{j,k}|m_{j,k,s}|^2\right)^{1/2}
 \ge c_0\sum_{t=1}^{\lfloor n/64\rfloor}\frac1t.
 \tag{13}
```

The harmonic sum diverges by grouping consecutive powers of two.
This is not a lower bound on the actual convolution row sum.
Fourier phases were discarded in forming (13).
It therefore supplies no counterexample to CFW.

The route fails at this conversion, even before adding the vector row and frame blocks.
A bounded multiplier, or its Hilbert-space coercivity bound, cannot complete the proposed proof.
One must use physical-space cancellation or additional frequency regularity of the combined matrix.
The one-tangential-direction success in §2 does not justify this higher-dimensional conversion.

## 5. Route B: use the Ward identity, then restore the prescribed frame

The second route tries to convert the original vector equation into a bounded volume-source problem.
It would then use the scalar regularity machinery already ported in `leaf-cbr.md`, §3.
It estimates the equation before applying the boundary inverse.

Reuse the homogeneous physical Ward cancellation from that note, (7)–(9).
For an unforced physical solution, (10) and stationarity give $`d_c^*\lambda=0`$.
Hence $`Q^*\lambda=S^*\lambda`$.
The literal path adjoints must cancel before taking absolute values.
This is prior work, not a new closure here.

For a general explicit forcing, the same calculation instead gives

```math
 r^*d_c^*\lambda+D^*G^*\gamma=D^*j.
 \tag{14}
```

This follows by applying $`D^*`$ to the first row of the original saddle.
The curl Hessian annihilates gradients.
Equation (14) records the required compatibility; it does not assert that an actual current violates it.
The independent-current operator cannot be replaced by a convenient divergence-free source without its defining match.
SA 11798–11805 explicitly requires that match.

There is a second, exact obstruction to the proposed shortcut.
The native Landau projection preserves the *straightened* rows.
It need not preserve the literal rows before their node factors are removed.
SA 10587–10603 and Y 30405–30432 distinguish these maps.
Their site average is $`q_s`$, not the root evaluation $`r`$.

This distinction can be tested without an estimate.
On the finite flat graph, define the source's algebraic site operators

```math
 G_s=(D^*D+q_s^*q_s)^{-1},\qquad
 R_s=I-G_sq_s^*(q_sG_s^2q_s^*)^{-1}q_sG_s,\qquad
 \Pi=I-DG_sR_sD^*.
 \tag{15}
```

All site blocks are complete, and residual constants are treated through the mean term.
These inverses exist at finite mesh.
The identities $`q_sG_sR_s=0`$ and $`D^*DG_sR_s=R_s`$ are the source's projection algebra.

Choose a scalar $`\phi`$ with $`q_s\phi=0`$ and nonconstant root values.
For example, put one at a root, minus one at another site in its block, and zero elsewhere.
Use a block having a neighbouring top block.
Since $`G_sD^*D\phi=\phi`$, the vector $`D^*D\phi`$ lies in $`\ker(q_sG_s)`$.
Thus $`R_sD^*D\phi=D^*D\phi`$, and (15) gives

```math
 \Pi D\phi=0,\qquad
 QD\phi=d_cr\phi\ne0.
 \tag{16}
```

Therefore $`Q\Pi=Q`$ is false for the *literal* $`Q`$ in (10).
This does not contradict the source identity for its straightened field-row map.
The example tests an operator identity only; it is not an admitted C-FACE input.

More explicitly, the discarded literal-row defect would be

```math
 Q\Pi a-Qa=-d_crG_sR_sD^*a.
 \tag{17}
```

The exact C-FACE system retains this defect through its row and node equations.
A smooth correction chosen only to restore root values does not automatically satisfy its prescribed slice.
The previous fibre lemma deliberately made no such claim.
Applying $`\Pi`$ again would also change those corrected literal rows through (17).

Thus the route cannot identify (11) with independent scalar Neumann responses.
It still owes the uniform combined coefficient bound after the actual row and node correction.
That bound is CFW, on the same input record.
Equations (14)–(17) locate the failed reduction; they do not refute CFW.

## 6. Route C: remove the native bare-boundary mass by a resolvent comparison

The third route starts from the existing native inverse.
It tries to replace its bare boundary control by the retained top rows.
This uses the source's positive-operator comparison method, rather than scalarizing the equation or applying Fourier orthogonality.

Y 27698–27716 controls the outer collar through its bare determining rows.
Y 31948–31963 pays boundary commutators at the fine scale.
Those are exactly the terms removed by TB.
There is no small curvature parameter in this change at the flat background.

The needed uniform contraction fails even in the corresponding scalar mass-removal comparison.
Take a unit normal slab with $`n`$ sites, and three tangential unit circles.
Let $`H_N`$ be its physical scalar graph Laplacian and $`q`$ the whole-block mean.
Let $`P_\partial`$ be the orthogonal projection onto the first normal site layer.
Set

```math
 A_t=H_N+q^*q,\qquad
 B=h^{-2}P_\partial,\qquad
 A_b=A_t+B.
 \tag{18}
```

This is a diagnostic scalar comparison, not an identification of the vector native operator.
It isolates the cost of replacing a fine-scale boundary mass by top-scale control.
Both matrices are positive definite: zero graph energy means a constant, and the mean controls that constant.

For odd $`n\ge3`$, take $`v(r,l_2,l_3,l_4)=\sin(2\pi l_2/n)`$.
Use the physical pairing $`h^4\sum`$.
Finite geometric sums give

```math
 qv=0,\qquad \|v\|_2^2=\frac12,\qquad
 \langle v,Bv\rangle=\frac1{2h},\qquad
 \langle v,A_tv\rangle
   =4h^{-2}\sin^2(\pi/n)\|v\|_2^2\le2\pi^2.
 \tag{19}
```

The normal energy vanishes because $`v`$ is constant in that direction.
The boundary layer occupies the fraction $`h`$ of the volume.
No numerical eigenvalue calculation is used.

Test the symmetric relative perturbation on $`A_b^{1/2}v`$.
Equation (19) gives

```math
 \|A_b^{-1/2}BA_b^{-1/2}\|
 \ge\frac{\langle v,Bv\rangle}{\langle v,A_bv\rangle}
 \ge\frac1{1+4\pi^2h}\longrightarrow1.
 \tag{20}
```

Thus this comparison has no contraction constant below one that is uniform in the mesh.
The resulting Neumann-series estimate loses at least a factor of order $`1/h`$.
A uniform gap for a different native boundary does not repair that estimate.
This is a failed perturbative proof, not a lower bound on the desired response.

I next kept the boundary correction exact.
At each finite mesh, elimination gives

```math
 A_t^{-1}=A_b^{-1}
 +A_b^{-1}B^{1/2}
    (I-B^{1/2}A_b^{-1}B^{1/2})^{-1}
     B^{1/2}A_b^{-1}.
 \tag{21}
```

To verify (21), put $`C_b=B^{1/2}A_b^{-1}B^{1/2}`$.
Then $`(A_b-B)A_b^{-1}B^{1/2}=B^{1/2}(I-C_b)`$.
Multiplying the right side of (21) on the left by $`A_b-B`$ gives
$`I-BA_b^{-1}+B^{1/2}(I-C_b)(I-C_b)^{-1}B^{1/2}A_b^{-1}=I`$.
The inverse is taken on the boundary range; positivity of $`A_t`$ makes it invertible there.
Equation (20) shows why bounding its middle factor separately cannot give the required uniform estimate.
The exterior factors and the joint input must be retained before estimating the product.
Section 2 supplies that cancellation in its scalar sector.
For the vector problem, the corresponding boundary elimination also carries the row and frame blocks of (11).
Neither the native theorem nor (21) estimates that combined matrix on the original input record.
This returns exactly to CFW, without a new domain or an independent surface-force norm.

## 7. Result

**Stopping condition (c): CFW remains open after three distinct routes.**
The routes were Fourier orthogonality, Ward reduction with frame restoration, and native boundary-mass removal.
Their failed steps are (13), (16)–(17), and (20)–(21), respectively.
They are failures of the specified arguments, not an impossibility theorem.

The kill test obtained no admissible counterexample.
Its new result is the source-to-face estimate (6), including all frequencies in the stated transverse scalar sector.
It excludes bounded complete-bulk-source realizations of the old logarithmic packet in that sector.
It does not identify a free independent-current coordinate with that source.

C-FACE is not proved.
CBR, TB-BC and the renewed-mark payment therefore receive no closure from this note.
If CFW is proved, the next tree work treats corners and mixed-grade interfaces, beginning with C-SEAM-LIFT.
Those tasks are not started here.
Only this output file was changed.

| Item | Status in this research note | Scope or first missing step |
|---|---|---|
| Native inverse, flat-fibre algebra, old packet | Reused | Their original boundaries, gauges and input spaces remain in force. |
| Coupled scalar transfer (2), (6), (7) | Written proof; not independently checked | One active tangential direction, zero top mean, bounded complete scalar bulk source; uniform finite slab extension. |
| Kill test on the original vector domain | No admissible counterexample obtained | The scalar source and frame must come from one actual original input. |
| Full alias bookkeeping and finite transfer (8)–(11) | Exact finite representation | No uniform inverse-entry or prescribed-frame estimate is inferred. |
| Fourier conversion in Route A | Insufficient | Its own bound grows logarithmically, (13). |
| Literal-row preservation by the native projection | False as an operator identity | Counterexample (16); the actual node correction remains mandatory. |
| Uniform contraction for bare-mass removal | False for the diagnostic comparison | Rayleigh quotient (20); this does not refute the combined response. |
| CFW, hence C-FACE | Open after three routes | Uniform combined absolute row sums on the original input record, with the prescribed frame. |
| CBR, TB-BC and H-C-MARK payment | Unchanged | Corners, mixed grades, nonlinear admission and ownership remain separate. |

**First open input: Lemma CFW, with all aliases and the literal row/node compensation retained on the original common domain.**
