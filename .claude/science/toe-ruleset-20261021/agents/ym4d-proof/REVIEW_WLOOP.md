# Independent hostile review of WLOOP

No binding defect was found in the frozen research note. The mathematical
claims survive at their printed finite-cutoff, Gaussian-model or conditional
scope. The full loop-only and combined physical targets remain **UNDECIDED**.
LAND here means acceptance of this bounded research note; it does not mean
that a continuum Yang–Mills theory, non-freeness in the full intended class,
confinement or a mass gap has been constructed.

## Review identity and evidence boundary

- Assignment: [briefs_q/WLOOP/REVIEW.md](briefs_q/WLOOP/REVIEW.md), checked
  against [AUTHOR.md](briefs_q/WLOOP/AUTHOR.md) and `PROCESS_LIGHT.md`.
  Only this review file was edited. No commit, source correction, audit or
  ledger mutation was made; no editable prompt file changed.
- Reviewer: fresh-context Codex, independent of authorship, **same-family**
  review of a Codex-authored note. The author log disclosed an earlier LAND
  result. I did not read that review body or use its verdict as evidence.
  The derivations and source checks below are this review's work.
- Target: [WLOOP.md](WLOOP.md), all **781 lines**, SHA-256
  `3fa6a797bab81e930d4d3f081b112da7ecb38a7073a248474731cd61314efa57`.
  All target line numbers below refer to these exact bytes.
- Working HEAD: `bb3e11fa4bf6e75e185bf5ba0950dfbef04e8727`.
  Fetch of `main` and `ai/execution` succeeded. `origin/main` remained
  `01589af3faf806b736c42dc2f3bd625e9edead9f`; the planning ref was
  `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. Planning supplied no proof.
- The 19 input files in [checks/wloop_sources.json](checks/wloop_sources.json)
  matched their recorded hashes at intake and again after source review.
  The manifest hash is
  `ab026105675ba5ce80a605015aa761b9bb4f8ff5b757612d997c6d0670935e22`.
  The note hash, HEAD and main ref also remained unchanged.
- Methodology: the repository `physics-claim-reviewer` skill and its relevant
  freshness, proof-governance, review-depth and no-go instructions were checked
  against the fetched main revision. The installed reviewer skill differs;
  the matching repository/main version governed this review. The explicit
  one-file/no-commit brief controls over broader workflow delivery rules.
- Existing JSON validation receipts are document bookkeeping, not proof.
  No numerical experiment, simulation, formal proof-assistant build or
  upstream whole-theorem recertification is claimed. Numerical resource gates
  were not bypassed. The author's reported `nice` rejection is not a numerical
  result and was not treated as one.

## Verdict per requested item

| Author item | Target lines | Verdict | Fix |
|---|---|---|---|
| 1. OS axioms, continuum renormalization/smearing and reconstruction | 28–118, 120–404 | **ACCEPT at the stated scope.** The loop-label proposal is separated from a constructed continuum law. Actual support determines the RP cone. W6 gives a Hamiltonian; W7 gives a boundary extension. Neither is misidentified with a local Wightman reconstruction. The REC library mismatch is real. | None. Preserve the OPEN status of the loop test completion, renormalization, mixed hierarchy, localization and reconstruction interfaces. |
| 2. Existing RG and source producers | 406–474 | **ACCEPT.** The exact bounded-source identity is available, while the quantitative local-composite source theorems do not supply a general holonomy insertion estimate. Coupling RG and Wilson gradient flow are correctly distinguished. | None. Loop-specific source transport, geometry control and fine-to-coarse matching remain new estimates. |
| 3. Non-freeness and comparison with a free theory | 476–590 | **ACCEPT as a conditional marked-comparator separation.** W9's monotonicity and W10's margin are correct. Equation (15), the common realization and the wider physical free-class identification are explicitly unsupplied. Nonzero loop cumulants alone are correctly rejected as an interaction test. | None. Do not promote the conclusion beyond the canonical Abelian/Cartan comparator of (12). |
| 4. Mass gap, confinement and Polyakov route | 592–658 | **ACCEPT.** The dense-family criterion has the right spectral quantifiers. The cited Polyakov result concerns spatial winding loops in a fixed spatial box. Neither a boundary mean nor a nonzero OS norm establishes positive-energy excitations or a gap. | None. Retain the full-sector density, infinite-volume and uniform physical decay obligations. |
| Comparison and GO/NO-GO/UNDECIDED judgment | 4–15, 660–697 | **ACCEPT UNDECIDED** for both full targets. The easier/harder table is explicitly an assessment of obligations, with bounded-moment bookkeeping distinguished from unsupplied dynamics. There is no hidden affirmative construction verdict. | None. |
| Negative-claim discipline and audit status | 699–781 | **ACCEPT as scoped boundary analysis.** The counterexample refutes automatic RP inheritance, not every flowed Yang–Mills loop theory. No universal loop no-go, packet PASS or retained/audit status is asserted. | None. This review confers no formal audit status. |

## Mathematical items and re-derivations

**W1, lines 28–38 and 120–145 — ACCEPT. Fix: none.** A product of SU(N)
matrices is unitary, so the normalized trace has modulus at most one.
Reversal gives the complex conjugate; gauge transformations conjugate the
closed holonomy. These statements survive repeated edges. For SU(N), N>2,
discarding imaginary parts can discard observable information, as the note
warns. Retracing can give the constant observable and hence no signal.

For every monomial, its expectation lies in the unit disk. Enumerate the
countably many coordinate/conjugate monomials, extract a subsequence for each,
and diagonalize. For every cylinder polynomial P the limiting functional obeys
`|L(P)| <= ||P||_infinity`, `L(1)=1` and `L(P*P)>=0`. It therefore extends to
the uniform closure; products of unit disks supply the compact coordinate
space. Integrating a joint test gives `|S_n(F)|<=||F||_1` directly, and centering
costs at most `2^n`. Conditioning under a positive law changes none of these
bounds. This establishes neither contour continuity nor the physical identity
of the limiting coordinates. The note expressly excludes both inferences.

**W2, lines 147–175 — ACCEPT. Fix: none.** Re-classifying plaquettes with
respect to a site plane gives exactly three classes: boundary plaquettes,
positive-half plaquettes and their reflected negative-half partners. Keep
the two temporal edges distinct when the temporal extent is two. Once the
spatial links on both fixed planes are conditioned upon, the remaining two
halves factor, and reflecting the negative variables gives the absolute
square in (4). Boundary coefficients need not be nonnegative; they enter
a positive real exponential. This is a site-reflection proof. The separate
link-reflection argument has the crossing-coupling sign restriction.

For a reflected open path, expanding
`Tr(Hol(theta gamma)^* Hol(gamma))` into matrix entries gives the sum of
their reflected quadratic forms. Gauge variance of individual entries is
harmless because the underlying RP theorem covers all half-measurable
functions. It does not make an arbitrary crossing loop a half-observable.

**W3, lines 177–188 — ACCEPT conditional implication. Fix: none.** If the
renormalized functions themselves have matching half-support and conjugation,
their Gram matrix is positive. A change of basis gives `Z*QZ`, irrespective
of the size of Z. Entrywise convergence of every required finite matrix
preserves positivity. Extension to other tests needs the printed continuous
bound. A separately chosen subtraction of kernel/contact terms need not be
an observable-level congruence, so the caution at lines 186–188 is justified.

**W4 and the color contraction, lines 195–242 — ACCEPT in the displayed
model. Fix: none.** The regulator is a valid positive Gaussian covariance:
`1/(|z|^2+epsilon^2)` is a positive superposition of the positive-definite
kernels `exp(-t|z|^2)`. The characteristic function of the real Gaussian flux
is `exp(-q^2 Q/2)`. Along a smooth arclength arc, the leading diagonal
integral is

```text
(4 pi^2)^(-1) (2/epsilon) arctan(delta/epsilon)
    = 1/(4 pi epsilon) + O(1).
```

The tangent and chord corrections are lower order. At a genuine corner,
the two-ray cross integral has radial measure `rho d rho` and a degree-two
denominator, producing the possible logarithm described in the note.
Center/rotation smearing retains this self-diagonal. For (6), add the
normalized identity matrix to the traceless Hermitian basis, use matrix
completeness, and subtract its contribution. This yields the printed two
color routings. It motivates intersection mixing; it does not prove the
nonperturbative renormalization program. That program remains OPEN.

**Finite-cutoff flow, W5 and localization, lines 244–302 — ACCEPT. Fix:
none.** The finite-link flow is an equivariant smooth ODE on a compact
manifold, preserving unitarity and therefore bounded traces. Compactness
does not establish continuum flow existence.

I checked W5 without relying on its determinant calculation. The original
Gaussian covariance is reflection positive: condition on its value at time
zero, and realize its positive and negative OU halves as independent
copies with common boundary value. Conditional expectation then expresses
the reflected form as a square. After time smoothing let
`a=C_s(0)>0`, `b=C_s''(0)<0`. For the explicit coefficients `(1,-1)` at
positive times `epsilon, 2 epsilon`,

```text
q = C_s(2 epsilon) + C_s(4 epsilon) - 2 C_s(3 epsilon)
  = b epsilon^2 + O(epsilon^4) < 0.
```

The note's determinant also expands to `a b epsilon^2+O(epsilon^4)`.
For bounded probes the exact joint-Gaussian identity is

```text
E[sin(lambda Y(-t_i)) sin(lambda Y(t_j))]
  = exp(-lambda^2 a) sinh(lambda^2 C_s(t_i+t_j)).
```

Fix a sufficiently small epsilon first, then take lambda small. The same
negative direction survives. This is a concrete counterexample to a general
inheritance rule, not a result about every nonabelian holonomy.

Writing `F=G+h`, reflection invariance gives
`|q(h,G)|,|q(G,h)|<=||h||_2||G||_2` and `|q(h,h)|<=||h||_2^2`.
Thus (8) is correct. Fixed physical flow time and fixed distance give only
a fixed localization error; cutoff removal alone does not make it vanish.
Spatial flow preserves the aligned temporal half-support, but its tilted
full slices cannot be put inside that same cone by moving their centers.

**W6, lines 306–334 — ACCEPT conditional implication. Fix: none.** State
positivity supplies the uniform ordinary-norm bound, while RP supplies the
different OS norm. These two uses of positivity are legitimate for the
bounded-loop state assumed here; they are not imported into the singular
e-test algebra. Translation/reflection covariance gives
`||[T_t F]||^2=q(F,T_(2t)F)`. OS Cauchy–Schwarz and iteration yield the
printed inequality. The far-translate norm is uniformly bounded, hence
translations preserve null vectors and induce contractions. Half-time
translation proves positivity; symmetry gives self-adjointness. Continuity
of the actual pairings, which is an explicit premise, yields strong
continuity. Trivial kernel of P_1 follows by its successive positive square
roots and continuity at zero, so the logarithm construction of H is valid.
Spatial motions preserve the same form. No Lorentz/local-field conclusion
is drawn from these steps alone.

**W7, lines 336–361 — ACCEPT conditional boundary extension. Fix: none.**
Conditioning as in W2 represents each cutoff OS norm by an L2 norm of a
conditional half-amplitude. A boundary multiplier b multiplies that
amplitude pointwise, giving (9) for a general finite sum as well as for a
single e-test. For a sum `sum_i b_i F_i`, Cauchy–Schwarz bounds its norm by
`sum_i M_(b_i) sqrt(q_a(F_i,F_i))`. The assumed convergent, uniformly
continuous e-core forms therefore bound every mixed Gram entry needed for
the countable extraction. Their positive limits retain the original e-core
form and extend in its test topology. The same multiplier inequality on
arbitrary sums proves null-space preservation and a bounded operator.
On boundary-only words reflection acts as conjugation, giving exactly the
norm and vacuum pairing at lines 350–352.

No ordinary `e(f)^2`, delta-function time test, unbounded moment convergence,
e-cyclic completeness or strong sharp-time translation limit has been
inserted. The exclusions at lines 354–361 are substantive and sufficient.

**W8, lines 424–440 — ACCEPT. Fix: none.** The exponential bound follows
from `|X_i|<=1`; expanding `exp(sum z_i X_i)-1` gives the stated disk about
one. Inside `sum |z_i|<log 2`, that disk excludes zero and supplies the log
branch. The same majorant justifies differentiation. The tower identity
uses the Markov property of the specified soft chain, not a generally false
tower identity for arbitrary nonnested conditioning variables. Its
strictly positive kernels also give a canonical conditional law for each
coarse configuration. This elementary complex radius depends on the number
of coordinates in a coordinatewise polydisc. No geometric decay, continuum
renormalization or comparison with coarse holonomy follows.

**Nonlinear free-loop warning and W9, lines 478–535 — ACCEPT. Fix: none.**
With `r=exp(-q^2 v)`, the third cumulant in (10) factors as
`r^(3/2)(r-1)^2(r+2)`, nonzero for `0<r<1`. A free Gaussian connection can
therefore give non-Gaussian loop coordinates.

For (11), `k.J_C(k)=0` follows by integrating a total derivative around
the closed contour. The p_0 integral gives `1/(2 sqrt(|p|^2+m^2))`.
Under `k=ell p`, the measure contributes `ell^(-3)`, the two currents
contribute `ell^2`, and the inverse energy contributes `ell`; they cancel.
The two spatial heat factors become `exp(-2 eta |k|^2)`. Closure gives
`J_C(k)=O(|k|)` at the origin, and eta>0 controls large momenta. For m>0,

```text
dV_m/dell = -(c m^2 ell/2) integral d^3k/(2 pi)^3
  exp(-2 eta |k|^2) |J_C(k)|^2 / (|k|^2+(m ell)^2)^(3/2) <= 0.
```

For m=0 the variance is constant. Applying the Gaussian characteristic
function to each diagonal entry of the commuting traceless Hermitian
matrices proves (12). Each exponential is nondecreasing in ell, so D_G
is nonincreasing. The zero-amplitude and zero-flux cases give equality.
Fixed probability mixtures preserve the inequality. Noncommuting color
Gaussian holonomies and arbitrary unmarked free theories are outside this
calculation, precisely as lines 532–535 state.

**W10, lines 537–590 — ACCEPT conditional separation. Fix: none.**
The sign of the negative exponent in (15) is handled correctly:

```text
D(ell_(m_0)) >= c_-/u_(K-m_0) >= c_-/U_+(m_0) = A,
D(ell_(m_1)) <= C_+ u_(K-m_1)^(vartheta-1)
              <= C_+ U_-(m_1)^(vartheta-1) <= A/2.
```

The fixed m_1 exists because beta_->0 and vartheta<1. It is chosen before
the cutoff/volume passage. The signed difference of these two moments is
at least A/2 in the proposed YM family and at most zero for every comparator.
Consequently their maximum coordinate discrepancy is at least A/4.
Bounded-coordinate convergence passes this margin to the limit. W7 identifies
the vacuum pairing only within the assumed common realization.

The Wilson-coupling conversion is also correct:
`u=1/g^2=2N/g_std^2` implies `g_std^2=2N g^2`. Nothing here produces the
two dynamical inequalities (15). The text expressly allows a deterministic
marked assignment to pass this two-number test; it therefore does not
mistake this test for an unconditional interacting-QFT construction.

**W11 and the sector examples, lines 594–622 and 650–658 — ACCEPT
conditional spectral criterion. Fix: none.** For the spectral measure of
each v_F, positivity yields
`exp(-bt)||E_H([0,b])v_F||^2 <= A_F exp(-m_*t)` for `b<m_*`.
Taking large t kills that projection. The bounded projection then vanishes
on the dense linear span and on its closure. A countable sequence b rising
to m_* removes all spectrum below m_* in Omega-perp, including extra
vacuum vectors. Density is required in the intended sector, not merely
the e-sector. Nonzero excited space remains separate; once it exists,
strong convergence of `E_H([0,R])` to the identity ensures a finite excited
spectral infimum. The cutoff/volume prescription is a valid sufficient way
to pass the decay estimate: first take each fixed physical t, then large t.

Appending multiplication by x on `L2((0,1))` leaves the old sector gapped
but introduces spectrum down to zero. The printed two-dimensional H=0
example has a unit centered vector with constant reflected correlation.
Both are genuine counterexamples to the broader inferences being rejected.
The invariant-mass interpretation additionally requires the Poincare
representation; W6 alone does not provide it.

## Source and locator checks

The following were checked against the pinned local bytes, including the
necessary definitions and qualifications. They establish that WLOOP uses
the cited interfaces honestly; they do not recertify every upstream RG or
analytic-continuation proof.

| WLOOP locator | Checked source lines | Result |
|---|---|---|
| 19–26, ASSEMBLY55 N0/N6 | `ASSEMBLY55.md:134–152, 219–225`; `MASS_GAP_TARGET.md` in full | Target and common-system requirement match. The expanded physical mass-gap target has not been weakened. |
| 85–118, 333, 363–373 | `OSLEAF55.md:134–330`, especially definitions D2/D5/D6 and E0′–E3 | Correct ordered/flat-test formulation and OS naming. In particular the e-test space does not admit arbitrary coincident polynomial moments. |
| 363–399, 772–774 | `REC_LIB.md:112–145, 824–958, 1080–1120`; `REC_CONT.md:17–70, 955–1018` | The current sources state an E0′ continuation producer for finite real scalar/Cartesian tensor point fields. Infinite loop-shape labels, support overlap and loop intersections are outside that printed theorem. The note does not repeat the obsolete claim that the point-field continuation producer is absent. |
| 147–175, table row 413 | `HRP.md:46–78, 200–258, 280–351` | Both fixed planes, geometric edge identity, site/link distinction, bare marginal and clover support match. Normalized auxiliary kernels do not reweight the bare law. |
| 336–361, 419, 583–586, 737–743 | `W_T0.md:86–215, 336–415, 454–491, 566–709` | Boundary extension, unbounded magnetic moment task, spatial tails, normal-label action and additional common-system obligations match. The B transport estimates are not loop estimates. |
| Table rows 414–417 and W8 | `SRCCD55.md:315–402, 588–623`; `SRC2_55.md:138–168, 306–343, 526–541`; `SRCAN55.md:129–154, 440–458` | Exact source identities generalize to bounded loops. The quantitative producer hypotheses concern e-coupling sources or strictly local insertions and remain conditional. The Markov hypothesis is present. |
| 51–52, 418, 541–558 | `FLOW.md:418–453`; `FLOW55.md:147–166`; `FLOWPOS55.md` in full | The cumulative coupling brackets and their indexing match. They supply no Wilson-gradient-flow transport theorem. FLOWPOS55 is a proposed task, not an established producer smuggled into W8 or W10. |
| 141–145, 280–295, 420–421 | `EXISTENCE.md:220–228, 353–455, 617–649, 2384–2443`; X-RAW heading at 581 | Compactness, flow-support caveat, approximate RP and the conditional single-loop continuity reduction have the stated scopes. X-RAW remains ARGUED. Finite-graph orbit separation is not a continuum local-field completeness theorem. |
| 637–658 | `EXISTENCE.md:3437–3619, 3652–3721` | The named loops are spatial winding observables of the soft law. The SU(2) constant and both fixed-box and infinite-time/fixed-space qualifications match. |
| 594–614 | `REC_LIB.md:782–822`; `MASS_GAP_TARGET.md` §§1–3 | Full-sector density, unique-vacuum requirement, physical decay scale and separate nonzero excited space match. |

The author's requested path `../ym4d-existence/E/EXISTENCE.md` is absent;
the actual source used above is
[../ym4d-existence/EXISTENCE.md](../ym4d-existence/EXISTENCE.md), as the author
log discloses. This is a locator correction, not a substituted theorem.

For the Polyakov constant I also checked the elementary mechanism, rather
than merely matching the numeral. Center charges annihilate the mean and
the cross terms between `e1`, `e2`, `e1+e2`. Quaternion multiplication gives
the SU(2) squared-trace sum at least `3/4` for commuting holonomies, with
loss at most their commutator norm otherwise. Telescoping plaquettes across
the spatial square bounds that norm; telescoping across the reflection
ribbons bounds the change of each trace. Cauchy–Schwarz then gives

```text
Cov(theta F_2,F_2) >= 3/4 - (n_s^2+4 n_s d_t) sqrt(eta).
```

Thus the cited `3/8` requires the stated smallness inequality. SMALL supplies
eta only conditionally on (O1)–(O3), H-coer and H-up, including the latter's
torus interpretation; the fixed-space/infinite-time version instead consumes
its printed ASSEMBLY (III) and K9-req assumptions. WLOOP does not claim these
assumptions have been proved. The growing n_s factor prevents reading this
estimate as a uniform infinite-spatial-volume signal at fixed coupling.

Primary literature checks were limited to the attributions actually made:

- Lines 232–234 accurately attribute perimeter/cusp/intersection
  renormalization to the perturbative program of Brandt, Neri and Sato.
  The DOI resolver failed through the browser tool, but the publisher's
  [article abstract](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.24.879)
  was retrieved and explicitly describes cusp factors and intersection
  mixing. No nonperturbative theorem is imported.
- Lines 248–253 match the scopes stated by
  [Luscher](https://arxiv.org/abs/1006.4518),
  [Luscher–Weisz](https://arxiv.org/abs/1101.0963) and
  [Lohmayer–Neuberger](https://arxiv.org/abs/1110.3522).
  Their primary abstracts support the smoothing/method attribution, not
  construction of this particular continuum law.
- Lines 377–389 accurately identify Schlingemann's extended-observable
  setting. I read [Definitions 2.1–2.3 and (TZ)](https://arxiv.org/html/hep-th/9802035v1):
  the three-factor group-continuity requirement and the nontrivial
  reflection-fixed time-zero algebra are distinct conditions. W6–W7 do
  not purport to reproduce the subsequent analytic rotation/locality proof.
- Lines 401–404 match the two-dimensional scope and proposed gauge-theory
  OS axioms in [Ashtekar et al.](https://arxiv.org/abs/hep-th/9605128).
  Lines 469–474 correctly identify [Dimock's convergence paper](https://arxiv.org/abs/1304.0705)
  as a treatment of three-dimensional scalar phi^4 using Balaban's methods.
  Neither attribution is used as four-dimensional nonabelian existence evidence.

No recalled literature assertion, prior review verdict, numerical PASS count
or imported expected coefficient was needed for the re-derivations above.

## Negative-claim and hidden-import disposition

The N1–N8 discussion is acceptable at its declared non-packet scope.
N1 retains materially different contour, flow, block, net and shrinking-loop
routes rather than declaring them exhausted. N2 does not invent independence
of reconstruction, marked separation and spectral decay. N3 prints the
Wilson/Haar, Gaussian, Markov, continuity, comparison and density premises.
N4 matches the actual support and theorem-domain residuals. N5 distinguishes
cutoff/model statements from continuum implications. N6 permits mathematical
reconstruction without inventing a new physical axiom. N7 gives a viable
net/time-zero alternative. N8 checks the relevant predecessor interfaces
and recognizes the updated point-field continuation producer.

The strongest attempts to invalidate the note's conclusions therefore do
not produce a defect: a direct RP proof for a particular flowed YM family
would evade W5's general warning, but W5 explicitly leaves it possible;
a noncommuting Gaussian comparator might evade W9, but it is explicitly
outside W9; extra low-energy states can appear after adjoining loops, and
W11 explicitly requires density in that larger sector. These are preserved
scope boundaries, not hidden assumptions or universal obstruction claims.

## Binding fixes and final checkpoint

**Binding fixes: none.** No source edit is required for acceptance of the
present note. The OPEN estimates are scientific tasks, not editorial fixes
that this review has silently discharged:

- a physically identified common continuum loop/local hierarchy with the
  required continuity, support, covariance and sharp-time realization;
- the loop-specific original-law comparisons (15), and an appropriate
  identification of the intended free comparison class;
- a dense-family uniform physical decay estimate and a surviving nonzero
  excited sector for the full mass-gap target.

The next discriminating task at lines 689–697 follows from the evidence.
Repeating boundedness would not supply those missing estimates. This file
is the completed review and sole reviewer checkpoint. Final source refresh
found zero changes among the 19 pinned inputs, the target retained its
frozen hash, and Git showed no tracked or staged source changes. Only
`REVIEW_WLOOP.md` was authored by this reviewer. The verdict does not
authorize a commit, merge or audit-status change.

VERDICT: LAND
