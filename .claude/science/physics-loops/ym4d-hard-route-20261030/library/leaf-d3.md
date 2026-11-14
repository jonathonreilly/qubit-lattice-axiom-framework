## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
I read `prior/repo-search-2026-11-08.md` and the required local notes.
`prior/leaf-d3.md` is absent at the pinned checkout.

| Hit | What I checked | Distance from this leaf |
|---|---|---|
| `loc-3.md`, Theorem W; `loc-4.md`, §§6–7 | Both files in full; `r2-heal.md` and its check in full | Existing locality implication. D3 remains an input. No replay proof is repeated. |
| `fp1.md` | Fetched PR #10141 at `c73ad7b177d94f89ff37b77386936e3d52b48b05`; `research/ym4d/library/fp1.md`, 142–168, 246–258 | Flat fibre comparison and conditioning of a fixed precision. These do not identify a newly rebuilt nonflat regional operator. |
| `d3-local.md`, §§1–4; `regional-gauss.md`, §§2–3, 5 | Regional matrices, intrinsic meet, wall algebra, and full-core limitation | The finite determinant algebra and a sufficient axial-core construction already exist. |
| `inv-root.md` (10); `ur-gauge-check.md`, D2 | Native historical formula and its gauge obstruction | The outer term already uses the second lift. The raw absolute-gauge obstruction is known. It is not a counterexample to the later relative family. |
| **`hma.md`, D1–D4, Lemma 1, Theorem 2, D6 and Theorem 8** | 9–108, 279–390, 551–557, Amendment 1 | **Closest hit.** The adopted relative gauge, pivot second jet and candidate precision are already explicit. Physical identification retains PH1–PH4. |
| `descent.md`, Lemma 4 and Theorem B; `ol.md`, §11.3 | 184–196 and 226–237; 1770–1806 | Already treats the relative coefficient and complete reads at fixed geometry. OL also keeps both multiplier branches. |
| `open-registry.md` | D3-REGIONAL, G-ID-cov, HMA-BRANCH, HMA-DOM and HMA-FORM | Actual branch matching and whole-domain admission have existing HM-A ownership. |

The lead's other-branch hits do not supply the missing regional application.
This is a bounded search record, not an absence theorem.
Main was fetched at `43a1fcc374711ca50626eca667441d3ca575c7d1` for the workflow.
The requested research base is `0eac16d888e8af101c040cce1fdd6a1cbd0e5b20`.

# D3-MATRIX: existing dictionary and ownership stop

Codex, 2026-11-08. FINISH row 543. Research text, not an audit. Grants no status.
All calculations below are by hand. No numerical run supplies a conclusion.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the background, constraint and localization methods.
Credit Claude and Codex for the existing LOC, HMA, descent and FP1 work.

**SA** means `YM4_sketch_500.tex` at `31a47c543775`.
**I** means `theorem_0_complete_account_raw_I.tex` at that commit.
**Y** means `YM4_1400.tex` at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
Numbers following these abbreviations are source lines.
The requested `/tmp` copies were reused. None was fetched twice.
The SA index, neighbouring rows and obligations preceded the corresponding bounded source reads.

**Result.** The fixed-geometry formula dictionary is already present in HMA.
The remaining assertion that it is the actual birth, on all requested regional domains, retains existing owned inputs.
The task expressly requires stopping when it reaches another registered owner.
This is that stop, not a claimed proof or refutation of D3.

## 1. Kill test first

**Outcome:** the adopted relative family passes the following first-birth test.
The older absolute replacement fails, as already known.
At zero inner depth the two current lifts coincide, so this case cannot distinguish them at positive depth.

Take the first ordinary birth, with zero-depth inner hierarchy and level-zero units.
Use HMA's odd blocking integer $L\ge27$.
Retain complete read stock for adjacent blocks $B_0,B_1$, including their collars inside a larger finite lattice.
There is one outward outer coarse row from the centre of $B_0$ towards $B_1$.
Choose a length-one top input row $e$ crossing their face.
The outer coarse row and its input row $e$ are distinct objects.
This base case tests an outward input current; it does not realize the mixed-scale outward-row discriminator.

Let $T_1,T_2,T_3$ be the Pauli matrices, normalized by $\tfrac12\operatorname{tr}T_i^2=1$.
Put
\[
 W(e)=e^{i\alpha T_1},\quad W(b)=1\ (b\ne e),\qquad
 J(b)=\tau T_2\mathbf1_{b=e},                                \tag{1}
\]
with the usual transported negative values on reverse orientations.
Choose nonzero real $\alpha,\tau$, arbitrarily small.
A plaquette through $e$ has holonomy $e^{\pm i\alpha T_1}\ne1$.
Thus the transport is nonflat.
All within-block contours are one.
The current is independent of the Wilson current and is supported on the outward input row.

Choose a noncentral site $x\in B_0$, away from the face and the boundary of the read stock.
Set $g_\varepsilon(x)=e^{i\varepsilon T_3}$, and set $g_\varepsilon=1$ elsewhere.
Use $V=W^{g_\varepsilon}$, with $0<|\varepsilon|\ll1$.
The fixed real reference may be $W$; $V$ is a small potential perturbation of it.
At this finite base step all local small-chart inequalities hold for sufficiently small parameters.
No whole-domain admission theorem is inferred from this observation.

The curve $V(t)=W^{g_{\varepsilon-t}}$ has the exact form $V(t)=e^{itw}V$.
Here $w=-T_3$ on outgoing bonds at $x$, the transported $T_3$ on incoming bonds, and zero elsewhere.
All outer block centres are fixed by this gauge.
Gauge covariance of the actual plain average, SA 7178–7183, therefore gives
\[
 q_V(tw)=0.
\]
Let $u=w|_{\check X}$. Pivot uniqueness gives
\[
 \Phi_V(tu)=tw,\qquad C_Vu=w,\qquad q_V''(0)[w,w]=0.           \tag{2}
\]
The free vector $u$ is nonzero: otherwise the invertible pivot block would force $w=0$.
Its full incident star can be retained in the deep regional coordinates.

At zero inner depth, $Q=Q'=I$, $R=0$, and the inner nonlinear constraint jet vanishes.
Consequently
\[
 H=H_1=I,\qquad \omega_* =\omega_{1*}=J,
 \qquad E_V^{(2)}[\omega_*](w,w)
       =E_V^{(2)}[\omega_{1*}](w,w)=0.                        \tag{3}
\]
This follows directly from $H_{(1)}=G_{(1)}Q^\#(QG_{(1)}Q^\#)^{-1}$ and (2).
The row mass subtraction leaves the Wilson Hessian.
The Wilson action is constant on this exact gauge curve, so its second derivative is zero.
Each retained plaquette trace is separately invariant; fixed exterior links cause no boundary term on this interior star.

Only the contour ending at $x$ varies. Its absolute value is $e^{i(t-\varepsilon)T_3}$.
Its relative value is $e^{itT_3}$.
Thus, in canonical Gaussian normalization,
\[
 f_{\rm abs}''(0)=\left.\frac{d^2}{dt^2}[1-\cos(t-\varepsilon)]\right|_0
                 =\cos\varepsilon,
 \qquad
 \langle w,b_V^\#b_Vw\rangle=1.                              \tag{4}
\]
All gauge indicators stay one if $t,\varepsilon$ remain within their cutoff margin.
HMA D2 and Lemma 1 use the second expression, exactly as Y 92243–92251 does.
Therefore the actual adopted candidate and the source candidate give
\[
       \langle u,A_Y^{\rm HMA}u\rangle
       =\langle u,A_Y^{\rm source}u\rangle=1.                 \tag{5}
\]
The raw historical absolute formula gives $\cos\varepsilon$ instead.
That discrepancy is the prior example of `ur-gauge-check.md`, D2, and `regional-gauss.md`, §5.
It is excluded from the relative dictionary, not offered as a new counterexample.
No conclusion about $H_1^\#J-H^\#J$ at positive depth follows from (3).

### Empty and separated subsets

Use the intrinsic meet and deep-coordinate convention of `d3-local.md`, §2, and `regional-gauss.md` (4)–(5).
There is no intermediate inner layer in this test.
Choose the localization blocks large enough to contain the one-step pivot and plaquette read collars.
Let $Y_1,Y_2$ each retain one outer block, with a zero wall wider than all these finite stencils.
Their complete read collars and integrated coordinates are disjoint.
At this depth the row Schur inverse cancels its defining inverse because $Q=I$.
Every remaining precision coefficient is local to one of these two stocks.
Thus the input to the existing wall-factorization argument holds:
\[
 A_{Y_1\cup Y_2}=A_{Y_1}\oplus A_{Y_2}.                       \tag{6}
\]

FP1 supplies the positive flat free-coordinate form.
The retained deep collars include all its stencils, so zero extension supplies positivity for these test matrices.
Finite-dimensional continuity gives a common small parameter neighborhood.
Continue each logarithm from that positive reference.
Writing $F(Y)=-\tfrac12\operatorname{Tr}\log A_Y$ and $Z(Y)=e^{F(Y)}$, the existing determinant algebra gives
\[
 F(\varnothing)=0,\quad Z(\varnothing)=1,\qquad
 F(Y_1\cup Y_2)=F(Y_1)+F(Y_2),\quad Z(Y_1\cup Y_2)=Z(Y_1)Z(Y_2). \tag{7}
\]
Here the unnormalized Gaussian uses $du/(2\pi)^{d_Y/2}$.
The normalized Gaussian evaluates one to one, including in empty dimension.
The assigned pivot scalar products also factor on these disjoint complete reads; their empty product is one.
Their logarithms retain the signs in `r2-heal.md`, §7.
This verifies the scalar edge cases for the test family, not all regional-history admission.

## 2. The dictionary that is already available

HMA D3 already defines
\[
 \mathsf A^{\rm HMA}=C_V^\#
 \left[\iota^\#\{(QG_1Q^\#)^{-1}-\mathsf a\}\iota
       +\mathsf G_V^Y
       -E_{\rm amb}[\iota^\#H_1^\#J]\right]C_V.              \tag{8}
\]
Its notation $Y$ on the gauge denotes the chosen relative gauge, not a conditioning subset.
Below, $Y$ denotes a conditioning subset.
The physical interpretation of (8) is conditional on HMA PH1–PH4.

| Required entry | Existing specification |
|---|---|
| Physical coordinate map | HMA D3 and D6: $u\mapsto\Phi_V(u)\mapsto U_k(e^{i\Phi_V(u)}V)$. The outer average is plain; the inner rows are straightened. PH3 identifies the actual critical branch. |
| Eliminated subspace | The inner constrained Landau problem and outer pivot coordinates. HMA PH1, PH4 and Lemma 7 keep the physical fine pairing and raw row normalization. |
| Boundary action and unchanged rows | HMA D1 retains the longer sequence, inner plaquettes, boundary spaces and omitted inward rows. PH2 retains stored unchanged rows. Matching a newly cut problem remains additional. |
| Independent current | HMA (3) and OL §11.3 retain $H^\#J$ inside $G_1$ and $H_1^\#J$ in the outer second jet. No physical substitution is made. |
| Relative gauge | HMA (2), Lemma 1: zero gradient and $\mathsf G_V^Y=b_V^\#b_V$, including after pivot substitution. |
| Conditioning | Zero extension $e_Y$ on the free coordinates of the specified regional problem. It is not an inverse taken before conditioning. |

On the *same specified regional problem*, the displayed formulas agree:
$q_V''=2C_V^{(2)}$, so
\[
 E_{\rm amb}[\iota^\#H_1^\#J](w,z)
   =2\langle H_1^\#J,\iota h_VC_V^{(2)}(w,z)\rangle.
\]
Also $\iota^\#\mathsf a\iota=a_{\rm top}$ on the active length-one rows.
These are the existing HMA/OL conventions, and give precisely Y 92253–92285 after applying $e_Y^\#$ and $e_Y$.
This is a formula comparison, not a new proof that two differently constructed regional problems coincide.

HMA Lemma 1 already proves the gauge identity used here.
HMA Theorem 8 already proves the physical Hessian implication under PH1–PH4.
HMA Theorem 2 and descent Lemma 4 already preserve full-read coefficients at fixed geometry.
Their proofs must not be repeated as closure of the missing regional application.

The source supplies the subsequent analysis on its admitted class:
Y 92397–92440 gives the proper covariance bound and continuation.
Y 92441–92574 gives the local inverse, logarithm and Gaussian construction.
Y 92576–92598 gives its physical critical-pair identification.
Y 48051–48090 retains the local-functional and hereditary premises of the uniform comparison.
These source results are credited inputs with their stated conditions; this note does not independently check their full proofs.

## 3. Where the assigned task reaches an existing owner

The task asks for an *actual birth* on its *original domain*, including newly cut boundaries.
Neither selecting (8) nor recognizing its source formula establishes that application.
The exact existing boundaries are:

| Needed assertion | Existing location and owner |
|---|---|
| The step's critical branch is the chart branch, with stored unchanged rows | HMA PH2–PH3, 283–286; registry **HMA-BRANCH**, owner **HM-A**. |
| Every complete regional read remains in the required complex class with the original radii | HMA 108, 557; registry **HMA-DOM**, owner **HM-A**. Intrinsic regional construction itself also remains with **D3-REGIONAL / DR**. |
| Replacing a gauge convention actually preserves the stored operation and its tests | HMA 182–186; registry **HMA-FORM**, owner **HM-A**. This is unnecessary for a new adopted candidate but cannot be assumed for an older stored birth. |

The first row is a prerequisite before calling the candidate an actual birth.
It is not supplied by the algebraic current readout or by the relative gauge identity.
The complete account likewise leaves application gauge membership outside its operator theorem (I 49495–49516).
No claim of impossibility follows from these open inputs.

**Stop:** the formula-level task is already covered, and its actual-birth prerequisite is registered to HM-A.
I stop under the user's prior-work and ownership instruction.
I do not relaunch HMA-BRANCH or HMA-DOM under a new D3 name.
The mixed-scale outward-row lift discriminator has not been computed here; the base-case test above is not a substitute for it.
No new counterexample to the adopted family, and no three-route failure of a new lemma, is claimed.
This is the explicit prior-work/ownership stop allowed by the task.

D3-SECTOR should not be selected merely because the obsolete absolute substitution fails.
The relative dictionary survives the test actually evaluated.
The next action is to use the existing HMA dictionary and resolve its owned application before extending it to the intrinsic meet.

## Status

| Item | Outcome |
|---|---|
| Relative gauge and two-current formula | Already present in HMA and OL; reused, not rederived. |
| Nonflat independent-current base-case test | Relative matrices both give (5). It does not test positive-depth lift separation. |
| Empty subset and wall-separated union | Exact normalization and branch factorization for the test family, (6)–(7). |
| Raw absolute replacement | Prior counterexample only; not a failure of the adopted relative family. |
| Actual birth and all newly cut regional domains | Not established here; existing HMA-BRANCH/HMA-DOM and D3-REGIONAL inputs remain. |
| D3-MATRIX / Theorem W supplier | No new closure or status. Stopped at prior coverage and registered ownership. |

**First open input:** **HMA-BRANCH**, specifically HMA PH3's equality of the actual step branch and the chart branch, with PH2's unchanged rows, on the regional problems used by this birth. Owner: **HM-A**. Whole-domain regional admission is still required afterward.
