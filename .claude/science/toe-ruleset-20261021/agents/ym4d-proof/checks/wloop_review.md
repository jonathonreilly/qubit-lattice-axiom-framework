# Independent WLOOP review

Recommend LAND for this bounded local research packet. I found no binding
mathematical correction in the frozen note. This recommendation accepts its
conditional lemmas and its UNDECIDED full-target verdict; it does not establish
continuum Yang–Mills existence, interaction, confinement, or a mass gap.

Reviewer: fresh-context Codex, with the inherited model/reasoning configuration.
This is same-family review of Codex work, not a different-family check or a
formal audit. The brief and source artifacts were shared inputs; the author's
conversation history was not supplied. No agents, model pools, numerical
experiments, commits, audit files, or ledger changes were used in this review.

## Frozen evidence and review boundary

- Complete `WLOOP.md`, all 781 lines, SHA-256
  `3fa6a797bab81e930d4d3f081b112da7ecb38a7073a248474731cd61314efa57`.
- Complete `WLOOP_LOG.md`, including the concurrent handoff additions, 103
  lines, SHA-256
  `8d29f5fbe5fa4c5fcb4f7192549eb9b479462182211edaa5cab2eadb644592d1`.
- `checks/wloop_sources.json`, SHA-256
  `ab026105675ba5ce80a605015aa761b9bb4f8ff5b757612d997c6d0670935e22`.
  All 19 recorded source hashes matched both initially and at the final source
  refresh, 2026-10-30T02:27:58 UTC. The log changed during review; its complete
  refreshed content was then read. The WLOOP argument did not change.
- HEAD `bb3e11fa4bf6e75e185bf5ba0950dfbef04e8727`; cached `origin/main`
  `01589af3faf806b736c42dc2f3bd625e9edead9f`. No remote refresh was attempted;
  this is an identified cached revision, not a freshness certification.
- Read local AGENTS, SCIENCE_WORKFLOW, PROCESS_LIGHT, and both WLOOP briefs.
  Applied `physics-claim-reviewer/SKILL.md` from that cached-main revision,
  SHA-256 `9a8c01717424c8c5c7b0420cd38a68c80179ae518b88591fe926dd21486096af`,
  with its same-revision freshness and proof-search-governance references.
  The installed skill was not substituted. Landing/audit workflow was outside
  the task. AUTHOR's allowlist supplies this review path instead of the
  template's `REVIEW_WLOOP.md`.

Line references below are to the frozen WLOOP source unless another file is
named. Necessary source definitions, theorem contracts, and cited interfaces
were inspected at their exact locators. This is not a recertification of the
complete upstream RG or REC_CONT proofs. Truncated search inventories were
used only to locate subsequently read source passages.

## Findings against each brief item

| Brief item | Verdict and evidence | Binding fix |
|---|---|---|
| 1. Loop OS axioms, continuum smearing/renormalization, reconstruction | Accept at the declared proposed/conditional scope. Lines 54–118 distinguish loop labels, actual support, convergence, covariance, and RP. W2–W3 give the exact cutoff/limit mechanism; W4–W5 establish only their stated model calculations. W6 gives a Hamiltonian semigroup; W7 gives a boundary module. Lines 363–399 correctly leave full loop/net reconstruction and local-field identification open. | None. The distinction between a Hamiltonian construction and a local Wightman reconstruction is essential and is already present. |
| 2. Existing estimates and new estimates | Accept the domain inventory, not a certification of all upstream results. Lines 411–440 separate exact positive-kernel identities and boundedness from local-source RG estimates. Lines 442–467 identify the missing contour limits, insertion representation, matching, mixed support/covariance, and dynamics. No beta-function bound is used as a holonomy estimate. | None. No listed source produces the needed loop-specific comparisons (15), and the note does not claim otherwise. |
| 3. Non-freeness | Accept W9–W10 as a restricted marked-comparator separation. The free loop cumulant warning at lines 478–492 is correct. Equations (11)–(13) hold for the defined commuting Gaussian/Cartan family, including its probability mixtures. The conditional YM margin follows from (14)–(15), not from boundedness. Lines 532–535, 560–564, and 583–590 explicitly retain broader free-class, localization, and physical-identification obligations. | None. This result must not be relabelled separation from every free physical theory, nor a nonzero excited-sector theorem. |
| 4. Mass gap and Polyakov/confinement routes | Accept. W11 is the correct common-rate, dense-family spectral criterion. Lines 616–622 preserve the sector-density issue. Lines 624–658 distinguish external-charge/string-tension limits and fixed-torus winding nontriviality from the physical vacuum gap. | None. The actual uniform infrared estimate remains absent and explicitly OPEN. |
| Overall comparison | Accept the UNDECIDED verdicts at lines 680–687. The EASIER entries at lines 668 and 671 are explicitly restricted to bounded moments/witness bookkeeping; the full reconstruction and dynamics are not declared easier or solved. Section 9 does not turn route sampling or an absent theorem into a universal no-go. | None. No GO or full-theory claim is justified by the packet, and none is made. |

## Independent derivations and adversarial checks

**W1 and the observable definitions, lines 28–81 and 120–145.** A product
of SU(N) links is unitary, so normalized trace modulus is at most one;
reversal gives the adjoint trace. Products, positive conditional averages,
and chart integrals therefore have the displayed bounds. A diagonal limit
of cylinder monomial expectations defines a bounded positive functional:
for each polynomial P, the cutoff inequality
`|E P| <= sup_(product disks) |P|` survives, as does `E P*P >= 0`.
This gives the stated state on the uniform closure, without any geometric
continuity conclusion. Centering costs at most `2^n`. None of this controls
unbounded renormalized traces or mixed e-moments. The note makes those
restrictions explicit; the N>2 complex-trace and retracing edge cases are
handled correctly.

**W2–W3, lines 147–188.** I classified the site-reflection plaquettes by
their time interval: spatial plaquettes are on a slice; temporal plaquettes
span one neighboring interval. With even temporal extent and distinct
geometric periodic edges, each belongs to one closed half or a fixed plane.
Conditioning on both planes therefore produces an actual squared conditional
amplitude. No positivity of a crossing character expansion is being silently
assumed in the site proof. For the reflected open path,
`Tr(M(theta U)^* M(U)) = sum_ij conjugate(M_ij(theta U)) M_ij(U)`;
the stronger RP statement for nongauge-invariant half-functions covers each
entry. Arbitrary crossing contours are correctly excluded from A_+.
Linear observable renormalization is a Gram congruence, and finite-entry
limits preserve its positive cone. Independent kernel subtractions are a
different operation. HRP lines 230–258 and 272–355 match these uses.

**W4 and color completeness, lines 195–234.** Completing the square in the
one-dimensional Gaussian integral yields (5). On a smooth arclength arc,
the leading near-diagonal integral is
`(4 pi^2)^(-1) * 2 epsilon^(-1) arctan(delta/epsilon)`;
its leading coefficient is `1/(4 pi epsilon)` per unit length.
Two noncollinear rays give a radial `rho d rho / rho^2` integral; the
angle/smooth-continuation qualification is needed and supplied. The Fierz
identity follows by adding the identity matrix to a Hilbert–Schmidt
orthonormal traceless basis and subtracting its rank-one projection.
It provides two color routings, not a nonperturbative renormalization
theorem. The latter remains OPEN. Whole-contour translation averaging
does not change the same-contour diagonal divergence.

**W5 and (8), lines 255–302.** The heat-smoothed covariance has negative
second derivative at zero. Direct expansion gives
`C(2e)C(4e)-C(3e)^2 = a*b*e^2 + O(e^4)`, with `a>0`, `b<0`.
An independent bounded-observable check is the exact Gaussian identity
`E sin(lambda Y(-t_i)) sin(lambda Y(t_j))
 = exp(-lambda^2 a) sinh(lambda^2 C_s(t_i+t_j))`.
Its leading matrix is `lambda^2 C_s`, so the negative determinant survives
at fixed small e and then sufficiently small lambda. This really defeats
automatic RP inheritance even for bounded functions; it is not an SU(N)
Wilson-loop counterexample. For (8), expand `F=G+E`; reflection is an L2
isometry, so the two mixed errors cost at most `2 delta ||G||_2` and the
last at most `delta^2`. A fixed positive tail bound is not a vanishing
cutoff error. The source's X-FLOW-NL/X-ARP limitations are preserved.

**W6, lines 306–334.** Set `a(t)^2=q(T_tF,T_tF)=q(F,T_(2t)F)`.
RP Cauchy–Schwarz implies `a(t)^2<=a(0)a(2t)`. The ordinary state and
isometric action bound a(t) uniformly by the supremum norm of F. Dyadic
iteration yields contractivity; if a(0)=0, the first inequality already
preserves the null class. Reflection covariance makes the induced maps
self-adjoint and positive, and the printed continuity identity gives a
strongly continuous semigroup. A vector in ker P_1 is in ker P_(2^-j)
for every j and hence is zero by strong continuity. The spectral logarithm
therefore gives H>=0. Spatial motions preserve the form and have inverses.
These premises concern the continuum half-space/action, not arbitrarily
long positive translations inside a finite torus. The note's R4 target
and support-defined continuum premise supply that context. No Lorentz
or locality conclusion follows from this calculation alone.

**W7, lines 336–361.** At cutoff, regard the conditional integral of F
in (4) as a vector in boundary L2 with weight `exp(-S_boundary)/Z`.
Boundary b is literally multiplication in that space. Thus domination
(9) holds for every finite sum `sum b_i F_i`, not just for a pure e-word.
Mixed Cauchy–Schwarz and the assumed uniform e-test bounds give bounded
entries on a countable dense test/module family. Diagonal extraction,
continuous extension in each e-test slot, and the same domination define
bounded multiplication on the limit quotient and preserve the e-core
isometrically. On boundary-only words the form is the ordinary joint
moment, giving the claimed norm and vacuum pairing. No coincident e-square
or delta time test is inserted. The strong translated sharp-time limit,
full mixed action, compact locality, and sector equality do not follow;
lines 354–359 explicitly retain them. W_T0 lines 155–214 make the same
boundary limitation, while its unbounded variable needs additional moments.

**W8, lines 424–440.** With r=`sum |z_i|`, bounded coordinates give
`|exp(sum z_i X_i)-1|<=exp(r)-1`; positive conditional averaging preserves
this bound. For r<log 2, M remains in the unit disk about 1 and has the
analytic logarithm normalized at zero. The Markov chain's level property,
not an inclusion of the individual sigma-fields, gives
`E[E(exp(z.X)|U_k)|U_(k+1)]=E(exp(z.X)|U_(k+1))`.
The exact recursion and derivatives follow. On a coordinate polydisc the
sufficient radius is `log(2)/n`; it supplies neither the local uniform
source radius nor a holonomy/coarse-field matching estimate.

**W9 and the cumulant control, lines 478–535.** For `x=q^2 v`,
`kappa_3(exp(iqX))=exp(-3x/2)[exp(-3x)-3exp(-x)+2]`;
the bracket equals `(exp(-x)-1)^2(exp(-x)+2)` and is positive for x>0.
Thus the proposed non-Gaussianity shortcut would fail. For (11), closedness
gives `k.J_C(k)=0` and `J_C(0)=0`. Integrating time momentum gives
`1/(2 sqrt(p^2+m^2))`. Under p=k/ell, the Jacobian, the squared-current
factor, and the denominator contribute `ell^-3 * ell^2 * ell=1`.
At zero momentum `J_C(k)=O(|k|)`, and positive eta controls infinity.
The resulting integrand decreases with ell for m>0 and is unchanged for
m=0. Gaussian characteristic functions of the diagonal color components
then give (12), (13), and their mixture extension. These steps use commuting
H_a; substituting noncommuting path ordering would invalidate the proof,
and lines 532–535 explicitly disallow that substitution.

As a sign/scaling discriminator independent of the claimed inequality, direct
differentiation of the independently rescaled covariance gives
`d V_m/d ell = -(c*m^2*ell/2) integral d^3k/(2pi)^3
 exp(-2 eta k^2)|J_C(k)|^2/(k^2+m^2 ell^2)^(3/2) <= 0` for m>0.
For m=0 the rescaled Gaussian current law has no ell parameter at all.
Thus an extra power of ell, a growing massive variance, or a positive
coarse-minus-fine comparator witness would fail this check. This argument
does not assume a numerical value or fitted normalization for the flux.

**W10, lines 537–590.** The coarse lower bound is at least
`A=c_-/U_+(m_0)>0`. Since `U_-(m)` diverges and `vartheta-1<0`, the fine
upper bound can be made at most A/2 by a fixed m_1, chosen before removing
the cutoff. For a marked comparator, `D_G(ell_m0)-D_G(ell_m1)<=0` because
`ell_m0>ell_m1`. The limit YM difference is at least A/2, so its difference
from any comparator difference is at least A/2; the triangle inequality
forces at least one coordinate discrepancy of A/4. W7 justifies the
boundary vacuum pairing under the specified common realization. The source
coupling convention `u=2N/g_std^2=1/g^2` is consistent with FLOW lines 24–26
and W_T0 lines 24–49. Bounds (15), their original-law uniformity, and the
physical observable identification are substantial unproved premises,
explicitly presented that way. The deterministic-assignment warning at
lines 587–590 correctly prevents interpreting the witness alone as physics.
For an explicit challenge to that stronger inference, in a one-dimensional
vacuum Hilbert space assign two SU(2) holonomies
`diag(exp(i theta_j),exp(-i theta_j))` with `0<theta_1<theta_0<pi`.
Their deterministic normalized traces give `D_0-D_1>0` while H=0 and
there is no excited space. This does not satisfy the actual YM-law
hypotheses; it disproves the inference from a two-moment margin alone to
interaction or a nonzero physical spectrum. W10 avoids that inference.

**W11 and infrared distinctions, lines 592–658.** For each centered vector,
spectral positivity yields
`exp(-bt)||E_H([0,b])v||^2 <= A_v exp(-m_*t)` for every b<m_*.
Taking t to infinity kills each low-energy projection. Density, bounded
projections, and a countable b increasing to m_* give the stated gap and
exclude extra vacuum vectors. The same m_* must work for the entire dense
family. The note keeps cutoff/volume limits before large t and separately
requires a nonzero excited sector. Both the direct-sum gapless extension
and the H=0 two-dimensional example are valid counterexamples to the
broader inferences they target. A static-charge energy and the vacuum
Hamiltonian spectrum are different spectral questions; no identity between
string tension and a glueball mass is used.

## Exact source-interface and attribution checks

- ASSEMBLY55 lines 134–152, 167–225, and 249–270 agree with the N0/N6,
  common-sequence, reconstruction, and physical-identification reading.
  OSLEAF55 lines 158–222 confirm the flat/ordered domain and the absence of
  an ordinary e(f)^2 claim. REC_LIB lines 112–146, 203–263, 782–822,
  824–889 and REC_CONT lines 17–70, 955–1018 confirm the finite Cartesian
  point-field contract and gap consumer. The point-tube theorem is not
  applied to extended loops merely by assigning them centers.
- SRCCD55 lines 329–403 and 588–608, SRCAN55 lines 129–154, and SRC2_55
  lines 138–163, 306–343, and 526–540 support the table's distinction
  between exact tower identities, coupling sources, and strictly local
  rooted insertions. FLOW lines 418–455 are conditional real-trajectory
  statements. FLOWPOS55 is a target-only draft, not a supplied estimate;
  WLOOP makes no contrary claim.
- EXISTENCE lines 220–228, 353–375, 427–455, 581–642 and 2384–2443
  support the bounded block/flow scope, raw-loop caveat, support issue and
  conditional continuity reduction. Its lines 3437–3452 define spatial
  winding loops. Lines 3523–3539, 3570–3578 and 3598–3620 contain the
  quoted SU(2) 3/8 result and its box-dependent sufficient condition.
  Lines 3652–3680 explicitly distinguish OS norm from positive-energy
  spectral weight. The WLOOP summary preserves these qualifiers.
- Primary method references were checked, not imported as proof:
  [Brandt–Neri–Sato](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.24.879)
  for perturbative cusp/intersection renormalization;
  [Lüscher](https://arxiv.org/abs/1006.4518),
  [Lüscher–Weisz](https://arxiv.org/abs/1101.0963), and
  [Lohmayer–Neuberger](https://arxiv.org/abs/1110.3522) for flow/smearing;
  [Schlingemann](https://arxiv.org/html/hep-th/9802035v1), Definition 2.3
  and (TZ), for regularity and the additional time-zero condition;
  [Ashtekar et al.](https://arxiv.org/abs/hep-th/9605128) for the stated
  two-dimensional precedent; and [Dimock](https://arxiv.org/abs/1304.0705)
  for the three-dimensional scalar Balaban-method account. Their described
  scopes agree with the note. Balaban and Dimock receive explicit credit.
  The DOI resolver failed for the first reference, but the primary APS
  abstract was accessible. No paper proof or PDF was used to fill a gap.

## Binding fixes and remaining limits

Binding fixes: none on the frozen WLOOP argument.

The unresolved work remains real science: loop-specific bounds (15), a
common covariant/local continuum realization, the chosen physical free-class
identification, and a dense-family uniform infrared estimate. These are not
minor technical remainders, and this review does not discharge them. The
source comparison and section 9 leave alternative loop constructions open;
W5 only rules out automatic inheritance, not a Yang–Mills loop program.

No numerical verification was performed because the reported nice guard was
blocked; the guard was not weakened. Hash checks are deterministic
bookkeeping, not physics evidence. I independently checked the written
load-bearing mathematics above, but neither rebuilt every upstream theorem
nor performed a formal proof-assistant verification. The review edited only
this file and grants no retained or audit status.

VERDICT: LAND
