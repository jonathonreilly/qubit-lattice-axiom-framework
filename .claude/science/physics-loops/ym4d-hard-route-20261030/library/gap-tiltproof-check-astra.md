## Repo search

The target-specific prior note is absent at `14d14ebf3a2db7e3e1b15845340f21e314b88267`.
The November 8 general digest concerns other RG and reconstruction targets.
It gives no prior proof of the pinned-sheet tilt bound. The present FINISH row
credits row 970's partial-pinning proposal; row 977 supplies the claimed bound.
Row 979 is a same-provider check. This requested cross-provider check is distinct.
The registry has no matching tilt-proof owner. Rebuilding the imported RP and
Gaussian-domination lemmas belongs to row 1000; this file checks their use only.
The bounded refresh searched `ZERO-CEIL`, `QUOT-CAP`, `TILT-COV`,
`Gaussian domination`, `pinned.sheet` and `partial.pinning`, outside this lane,
on main and PRs 10114, 10133, 10134 and 10141. No same-target result appeared.
Relevant source reads were:

| Source | Lines checked | Closeness |
|---|---|---|
| main, `docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md` | 75–155 | Same GD/infrared normalization method and self-inverse-mode treatment, for a supplied 3D sphere spin law. Its GD theorem is an import. No pinned 4D Wilson application. |
| PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/TQ55.md` | 227–272 | Temporal-gauge FSS discussion and its limits for an unpinned Wilson stress-channel problem. Different target and measure. |
| main, `research/mass-gap/library/gap-crux-fp.md` | 294–307 | Recalled gauge Gaussian-domination method, explicitly not proved there. No tilted-sheet bound. |
| this lane, `gap-direction2-max.md` | 294–323; row 977's own attribution at 323–330 | The existing quotient criterion and the earlier partial-pinning proposal; credited to row 970, Claude Fable 5.2. |
| this lane, `gap-d2-inputs.md` | 48–150 | The exact RP/GD supplier, already written by Claude Opus 5.5. Reused, not a new rebuild. |

Refs searched: main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`;
PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`;
PR 10133 `89faef229ff6e6bde42baad15ed8270c2f4087d8`;
PR 10134 `1e70c7211a2cdbc39001e619f1dd89db45e25851`;
PR 10141 `a2f6a430e251aa47bc3eb4f67a1dca2a88530116`.
The multi-ref fetch returned exit 1 without diagnostics. `ls-remote` verified
the first four refs and exposed a newer PR 10141 head; a successful separate
fetch and search covered that head. Search logs are in the scratch directory
below (`repo-hits.txt`, `pr10141-refreshed-hits.txt`). False-positive Gaussian
integrability and finite-clock matches were not treated as theorems here.

Account lookup followed `sa-index/README.md`, chunk 03's neighbouring rows,
and the corresponding `obligations.md` section before reading outline
2773–2883. AM2–AM5 are proved prior ingredients. The CA 4.12–4.19 index has
no match for the target or imported FSS step. The full-account index locates
ordinary RP statements in CA-II, not this CA-I file; no CA-II proof is claimed
read. The same targeted search of the downloaded CA-I text had no match.
This is a bounded search result, not an exhaustive novelty claim.

Provenance: OpenAI Codex, configured model and effort (not independently exposed
to this session); source commit `14d14ebf3a2db7e3e1b15845340f21e314b88267`.
Research check, not an audit; this file grants no status. No numeric proof step.

### Checkpoint

Completed: prior-source lookup; D2 reflection/GD hypotheses and Fourier
normalization; ZERO-CEIL and D1; CAP and QUOT-CAP; hand side-4/8 arithmetic.
Unresolved inputs: the finer ZERO-CEIL integral, side-12/16/120 lattice sums,
and `inf_b q_0(b)>=0.24`. No proof attack on those inputs was launched.

Sources downloaded once into the new empty directory
`/tmp/sa-gap-tiltproof-check-astra.lUCSck/`: `sa_ym4.tex` and `sa_ca_I.tex`,
both at Sussman–Alpoge commit `31a47c543775`. Credit Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text.

The full 446-line target was read. No source file was edited. The existing
row-979 verdict was exposed by the required FINISH lookup; its report was not
used as proof. The check below uses the raw construction, a graph-Laplacian
normalization calculation, and exact radical pairing for the arithmetic.

## D2: the two imported lemmas and their applications

Line numbers below refer to `library/gap-tiltproof-max.md` at the pinned commit.
The argument uses the abstract form of reflection positivity associated with
Osterwalder–Seiler and Fröhlich–Israel–Lieb–Simon, followed by the
Fröhlich–Simon–Spencer reflection-maximizer argument. Ordinary Wilson reflection
positivity alone is not the shifted partition-function inequality.

The existing supplier is `library/gap-d2-inputs.md:48–150` (row 1000).
That source already writes the full proofs, so this check does not create a
second rebuild. Its unrelated T3 discussion is outside this check.

**RP hypotheses as used.** The two halves have reflected product measures,
possibly including fixed identity links. At each fixed pair of source profiles
`f,g`, their finite action has the form

\[
a_f(U_+)+a_g(\theta U_-)
 +\sum_r c_r C_{f,r}(U_+)C_{g,r}(\theta U_-),\qquad c_r\ge0.
\]

The real features and half actions are bounded for each profile. Their number
and coefficients match on both sides. Then the integrated kernel in `f,g` is
positive semidefinite, giving Cauchy–Schwarz. The nonnegative exponential Gram
expansion is already in Sussman–Alpoge, outline 2773–2795 (AM2). Their
2834–2883 proves ordinary link-cut positivity and preservation under reflected
half actions. These are prior ingredients, not the pinned-sheet theorem.

**5.2 — HOLDS with this abstract input.** For either transverse direction,
crossing links at times 0 and 1 are pinned. The other crossing links are
disjoint matching edges. Each can be fixed by changing only its terminal site,
outside times 0 and 1. Conditional on the crossing links, all other changes
are left/right Haar translations; their Jacobian is one. The source reads
only time 0, so it is unchanged. Restoring temporal Haar links outside the
0–1 layer is essential here. After fixing, the reference measure is a product
on the two halves. Every nonconstant crossing plaquette is a scalar product
with coefficient `beta` or `beta/2`. The latter is positive at the temporal
ends. Crossing plaquettes in layer 0–1 are constants: all four links are
pinned. Thus `b` occurs only in reflected half actions or constants. All RP
hypotheses hold, even for real `b`; the later cross-slice covariance needs
`b >= 0`.

**GD hypotheses as used.** (G1) For every transverse bond-cut reflection,
`Z(h)^2 <= Z(R_+h) Z(R_-h)`, where `R_+` and `R_-` copy one half-profile.
(G2) Every shifted bond crosses one of these reflections. (G3) `Z` is positive,
continuous, invariant under constant shifts, and tends to zero as gradients
escape to infinity; hence it attains a maximum modulo constants. (G4) Copying
eliminates crossing gradients and doubles the gradients inside the copied
half. These imply `Z(h) <= Z(0)` by minimizing the number of nonzero gradients
among maximizers. No power-of-two assumption on the even side is needed.

**5.3 — HOLDS.** These hypotheses hold for shifts on the selected sheet alone.
For a crossing sheet bond, put `Q=P-h`. Its term splits as

\[
-\frac\beta2|Q_+-Q_-|^2
=-\frac\beta2|Q_+|^2-\frac\beta2|Q_-|^2+\beta Q_+\cdot Q_-.
\]

This verifies G1 using profile-dependent features in RP, while all other
crossing features remain unshifted. The sheet is connected and finite,
`|P|=1`, and `beta>0`, which verify G2–G4. The terse single-reflection lemma
cited at lines 203–205 must be consumed through this iteration, not as a
claim that one reflection removes every internal sheet shift.

For an independent normalization check, let `L` be the sheet graph Laplacian,
with eigenvalue `lambda(p)=4-2 cos p_2-2 cos p_3=2E(p)`. Twice differentiating
`Z(epsilon h)/Z(0) <= 1` gives

\[
\beta\,\mathbb E\langle P,Lh\rangle^2\le\langle h,Lh\rangle.
\]

Translation invariance diagonalizes this quadratic form. Thus the covariance
eigenvalue is at most `1/(beta lambda(p))`, exactly the factor in 5.3.

**5.1 — HOLDS.** Set `m_n=e^{-V/2} lambda_0^{-n} T_0^n 1`.
Its product with itself and `e^{b<x,w>}` has precisely the stated slab weights:
full spatial weights at the two central slices and half weights at the ends.
The strictly positive compact kernel gives uniform convergence of `m_n` to a
positive multiple of `m`. Restriction to the pinned set preserves this uniform
convergence; normalization then gives the claimed hard-pinned marginal.
Open temporal chains allow the stated restoration of Haar temporal links.

**5.4 — HOLDS.** Positive semidefiniteness of a covariance matrix, rather than
pointwise positivity of correlations, gives `Ghat(p)>=0`. Fourier inversion
and the sheet left/right SU(2) symmetry give `sum_p Ghat(p)=A/4`. Subtracting
the upper bounds outside `Low` gives exactly the stated maximum bound.

**5.5 — HOLDS AFTER CORRECTION.** At hard pinning the two restricted measures
are identical, independently of `s,s'`. For `b>=0`, the Gram expansion of
`e^{b<x,w>}` gives nonnegative *centered* cross covariance: apply its positive
quadratic form to `f-E f`. Hence both one-slice variances add as claimed.
However `sqrt(2/A) cos(p.y)e` is not a unit vector at the three nonzero
self-inverse momenta `p in {0,pi}^2`. Use `A^{-1/2} cos(p.y)e` there and at
zero; use `sqrt(2/A)` otherwise. With this repair, every momentum supplies
the stated unit-vector lower bound. The low-mode maximum and D2 are unchanged.

The finite-group clause also holds. For Q_8, an endomorphism commuting with
all left quaternion units is right multiplication by a quaternion; commuting
also with the right units makes that quaternion real. The covariance is
therefore scalar. The group 2T contains Q_8. All other steps use only product
Haar measure (counting measure here), central flips, compactness and the same
nonnegative Gram expansion. Full continuous O(4) symmetry is not required
for these two finite-group conclusions.

## ZERO-CEIL and D1

**ZERO-CEIL, lines 54–72 — HOLDS AFTER CORRECTION.** The coarse ceiling holds.
Here `alpha_s^thm` means the reciprocal of the displayed POL-BR integral,
the rate certified by that formula. It is not the optimal log-Sobolev rate.
POL-BR itself gives a lower bound on the optimal rate; reversing that bound
would be invalid. With this meaning, the target's argument has the right sign.

Row 968, lines 148–167, supplies the exact zero-field covariance and the
formula. At zero field all directions are horizontal, so `kbar>=k00_s`.
The convexity argument for `tau_b>=0` applies for `b>=0`: the derivative of
the finite log partition function starts at zero and has nonnegative second
derivative. The elementary identities for `p=lambda(1-lambda)` and `r` are
correct. The logarithmic derivative of the integrand bound is

\[
\frac1r+\frac1{r+2}-\frac{\beta/2}{1-e^{-\beta r/2}}<\frac34-\frac\beta2.
\]

Thus for `beta>=3/2`,
`alpha^thm <= 2 beta/(exp(beta)-1)`. At `beta=23/10` this is strictly below
`513/1000`. A hand certificate is `exp(2)>7.388`, from the Taylor polynomial
through degree 9, and `exp(0.3)>1.3498`, from degree 4. Their product is
`9.9723224>9.97`, and `460/897<513/1000`. Hence the stated `K_30=0.811`
cannot be reached. That seed value is a supplied input from row 974, lines
28–56; no check of its upstream transfer estimates is claimed here.

The correction is at lines 64–72: a trapezoid estimate supplies no upper bound
without a signed error estimate. The text acknowledges this, but then uses it
to say that the seed size **must** be at least 117. Delete that deduction.
This check does not promote `0.234`, nor check the quoted approximate seed
sizes 50, 117 or 830. The exact coarse formula is enough for the named seed.

**Lemma D1, lines 175–199 — HOLDS.** Parts (i)–(iv) use the actual gauge
action, not a change of variables on a guessed effective spin model. A
central flip at one endpoint plane kills the mean. For different planes,
one of the flips listed in the proof changes exactly one factor; `S>=4`
excludes coinciding neighbours. On one plane the two independent endpoint
groups act by the real irreducible left/right quaternion representation.
Its commuting covariance matrices are scalar, with scalar one quarter of
the trace. This proves all covariance and variance identities.

For (v), normalize each transverse factor `exp(Lambda x^0/s)` separately.
Their product converges to identity pins. The remaining density is continuous
and strictly positive on a compact space, so the normalized expectations of
the observable and its square converge. This proves the required lower bound
on every admissible `kbar`; no infinite-volume limit is involved.

The generic-point remark is not needed for the literal supremum hypothesis,
which includes the singular tilt itself. A sufficient implementation of its
limiting argument is to choose the perturbation only on the free links, with
zero `cos(p.y)`-weighted sum on the tested plane and enough other free-link
values to break the continuous plane stabilizers. The pinned-link tangent
space is orthogonal to the free-link space. Projection onto the remaining
orbit directions then gives horizontal vectors converging to the tested
mode. Mere trivial stabilizer without the weighted cancellation is insufficient.

## Hand arithmetic and CAP

**Side 4, line 243 — HOLDS AFTER CORRECTION of rounding.** The one-dimensional
eigenvalues are `0,2,4`, with multiplicities `1,2,1`. Thus

\[
16G_4=2+\frac12+1+\frac23+\frac18=\frac{103}{24},\qquad
\lambda_4=16-\frac{103}{6\beta}.
\]

At `beta=23/10`, the proved lower bound is exactly `589/69`. It is **less**
than `8.54`, since `29450<29463`. Use `lambda_*>=589/69>8.53`, or write
`lambda_4 approximately 8.54`. Rounding upward does not prove the printed
inequality `lambda_*>=8.54`. Positivity requires exactly `beta>103/96`.

**Side 8, lines 423–427 — HOLDS AFTER CORRECTION of the decimal certificate.**
The eigenvalues and multiplicities are correct. Pairing conjugate radicals
in the fourteen summands gives an exact, shorter hand sum:

\[
64G_8=17+\frac{31}{24}+\frac{32}{7}+\frac{24}{17}
     =\frac{69329}{2856},\qquad G_8=\frac{69329}{182784}.
\]

Here the pairs involving `2-sqrt(2)` and `2+sqrt(2)` contribute, respectively,
`8` against zero, `4` on their diagonals, `32/7` against eigenvalue 2,
and `24/17` against eigenvalue 4. Their mutual pair contributes 2.
The remaining terms are `2,1/2,1,2/3,1/8`. This accounts for every term.
Consequently

\[
\lambda_8=\frac{178859}{8211}>\frac{1089}{50}=21.78,
\]

because `178859*50-8211*1089=1171>0`. Thus the claimed `21.78` is valid.
The displayed rounded summands are approximations, not an exact identity;
in particular their `24.274857` must not be used as an exact sum. The earlier
`>=21.8` is only a rounded description, not the lower bound just proved.

**Corollary CAP, lines 259–266 — HOLDS AFTER CORRECTION of scope and input
labels.** Put `ell=lambda_*` and `x=ell beta`. The integral bound gives the
first inequality for `alpha_s^thm` exactly. Its reduction to the midpoint
uses `x>=3/2`, by the same derivative calculation as ZERO-CEIL. This condition
holds at `beta=2.3`: allowing all momenta in `Low` gives `ell>=1`.
Include that condition if CAP is stated at arbitrary beta. It yields

\[
\alpha^{\rm thm}\le\frac{2x}{e^x-1}.
\]

The side-4 ceiling `<1.2*10^{-7}` survives the corrected `x=589/30`.
For a hand bound, `e^3>20` (Taylor polynomial through degree 8),
`e^{8/5}>99/20` (through degree 7), and `e^{1/30}>31/30` imply
`e^{589/30}>327360000`. Then
`(589/15)/(327360000-1)<1.2*10^{-7}`.

The side-8 ceiling `<1.8*10^{-20}` also survives. The function
`2x/(e^x-1)` decreases for `x>0`; use `x>=25047/500=50.094`.
The finite Taylor bounds `e^3>502/25` (degree 11) and `e^2>369/50`
(degree 7), together with `e^{0.09}>109/100`, give

\[
e^{50.094}>20^{16}\left(1+\frac{16}{250}\right)
             \frac{369}{50}\frac{109}{100}>5.6\,10^{21}.
\]

Since `2*50.094=100.188<100.8`, the claimed cap follows. These are hand
inequalities, not values discharged by a run.

The side-120 cap remains conditional on an unproved lattice-sum bound.
The source labels that arithmetic ARGUED, but later calls the resulting
24-order exclusion proved. Keep the source's limitation in every use.
The independently proved ZERO-CEIL already excludes the named side-120 seed.

## Proposition QUOT-CAP

**Lines 390–412 — HOLDS AFTER CORRECTION, conditionally.** The correct
conditional conclusion is the spectral formula below. Neither its one-link
hypothesis nor its side-120 numerical input is proved by this check.

At every finite `Lambda>0`, removing just the selected plane's direction-1
links leaves a connected pinned-link graph. Its stabilizer is constant
conjugation. The real vector `z_l=a(y)1` is horizontal and fixed by that
stabilizer. Thus it meets both side conditions in row 970's Theorem QUOT
(lines 294–323, read here). For one colour, the orbit norm is
`Lambda^2 xi^T L_pin xi`. Taking its inverse on constants' orthogonal
complement gives `R_eff/Lambda^2` for the squared endpoint difference.
The three colours give exactly

\[
Q_{\phi''}(z)=\frac3{\Lambda^2}\sum_y a(y)^2R_{\rm eff}(y)
 \le\frac{3(S-1)}{\Lambda^2}.
\]

This proves the disappearing gain without treating a rigid frame mode as an
admissible quotient direction.

The centre flip of the free plane is a global centre-sheet symmetry, not a
gauge transformation on the connected pinned graph. Extend that sheet flip
through every time slice in the slab: each affected plaquette has two flipped
links. It preserves the action, all fixed links and the two end weights.
Hence the means vanish, including in the limit. Constant conjugation makes
the imaginary covariance scalar but does not force `q_0=1/4`.

Additional identity pins on other direction-1 planes preserve every transverse
reflection and remain unchanged by the exterior gauge fixing. All RP and GD
hypotheses above still hold. Replace the sum rule `A/4` by `A q_0(b)`.
Swap symmetry and positive type still apply. Therefore the exact conclusion is

\[
\bar k_{s,t}\ge
4k_{00,s}\max_{L\ni0}
\frac{Aq_0(b_t)-\sum_{p\notin L}(\beta\lambda(p))^{-1}}{|L|}.
\]

This establishes the proposition's mechanism. To assert its constants at
**every** `s,t`, or insert one constant throughout CAP's time integral, its
hypothesis must read
`inf_{0<=b<=beta} q_0(b)>=0.24` for each box in question. A value measured
only at `b=beta` does not meet it. The hard-pinned law has no remaining
dependence on `s`, but it does depend on `b`.

The numerical consequences need these corrections:

- Side 8: the exact formula at `q_0=6/25` gives
  `178859/8211-64/25>19`. This lower bound follows by hand.
- Side 16: using the source's decimal `G_16=0.48992` gives
  `4*256*(0.24-0.48992/2.3)=27.639095...`, not 28. The formula supports a
  conservative 27.6 only if an appropriate upper bound on `G_16` is supplied.
- Side 120: the claimed 19.8/19.9 needs the still unproved high-mode sum.
  The arithmetic in 10.3, taken literally, is `4*(3456-3052)/81=1616/81`,
  approximately 19.95. It permits the smaller 19.9, but only if 3052 is a
  proved **upper** bound on the excluded-mode sum. No such bound is printed.
  The ceiling derived from an assumed factor 19.8 should remain the exact
  expression `91.08/(exp(45.54)-1)`; its rounded `1.5*10^{-18}` is not a
  certified upper bound here.

The auxiliary claim `q_0>=A_4(6 beta)/(6 beta)` uses a single-link conditional
law in the slab, not a single-link conditional law of the already integrated
`m`. In the slab, six staples have total vector norm at most `5 beta+b<=6 beta`.
The rotational single-spin second-moment bound can then be averaged before
taking the slab limit. The source does not write that von Mises–Fisher bound
or a hand bound on its Bessel ratio. Its decimal `0.064` is not promoted by
this check; in any event it does not supply the needed `0.24`.

## Numerical scope and verdicts

No simulation or floating-point sum was run here. The GUIDE results belong
only to their stated finite models. The target's proposed P1/P3 tests are not
proof inputs. In particular P3 tests `b=beta`; its criterion C2 uses 0.22,
whereas QUOT-CAP's printed numerical conclusion assumes 0.24 throughout `b`.
Even a passing C2 cannot establish that conclusion. Finite-size growth also
does not refute existence of some finite box-uniform bound without a proved
continuation to arbitrarily large sides.

| Statement in the pinned source | Verdict | Exact limit or correction |
|---|---|---|
| 2.0 ZERO-CEIL, lines 54–72 | HOLDS AFTER CORRECTION | Exact coarse cap holds for the formula's output; remove the unproved 0.234/117 deduction. |
| D1(i)–(v), lines 175–199 | HOLDS | Finite-box gauge symmetry and hard-pin convergence; no spectral-gap input. |
| D2 5.1, lines 209–214 | HOLDS | Uniform transfer-kernel limit with the stated end weights. |
| D2 5.2, lines 216–222 | HOLDS | Abstract parameter-dependent RP, with crossing gauge fixing and restored temporal links. |
| D2 5.3, lines 224–229 | HOLDS | Sheet-only GD meets G1–G4; coefficient `1/(2 beta E(p))` is correct. |
| D2 5.4, lines 231–233 | HOLDS | Nonnegative Fourier spectrum and exact sum rule. |
| D2 5.5 / D2, lines 235–247 | HOLDS AFTER CORRECTION | Normalize self-inverse modes; use exact or downward-rounded constants. The spectral theorem itself holds. |
| CAP, lines 259–266 | HOLDS AFTER CORRECTION | State `beta lambda_*>=3/2`; side-4/8 caps hold; side-120 number remains conditional. |
| QUOT-CAP, lines 390–412 | HOLDS AFTER CORRECTION | Uniform-in-`b` hypothesis; replace side-16 28 by its actual bound; retain lattice-sum inputs. |
| Hand arithmetic 5.5 and 10.1 | HOLDS AFTER CORRECTION | Exact fractions above prove `589/69` and `178859/8211`; decimal sums are not exact certificates. |

No failing structural step was found in the pinned-sheet mechanism. This is
not an unconditional proof of every number in the source. The generic
box-uniform bound remains open. The finite seed is excluded by ZERO-CEIL,
conditional on the stated POL-BR output formula and the supplied seed target.

Source SHA-256: target `7a1fae3602debd631c8d042f99bd7ceb140629a1c709e440f8950f617f474e40`;
RP/GD supplier `d15113a6ad7527e19e4edb2e81d08cc7fd1a02b313b99794053271c5aaab3de1`.
Only this check file was written in the checkout. No audit, simulation, source
edit, registry update, commit, push or external post was performed.

RESULT: Row 977 cross-provider research check: D1 HOLDS; D2 HOLDS AFTER CORRECTION of exceptional-mode normalization and numerical labels, with its RP and sheet-only GD hypotheses met; ZERO-CEIL, CAP, QUOT-CAP and the 5.5/10.1 arithmetic HOLD AFTER CORRECTION as detailed above. Exact side-4 and side-8 bounds are 589/69 and 178859/8211; the stated side-4/8 CAP ceilings follow by hand. ZERO-CEIL excludes the supplied a=30 seed through the POL-BR formula. Side-120 numerical claims and the uniform-in-b q_0 hypothesis remain unproved; no GUIDE run discharges them, no structural failure was found, and this file grants no status.
