## Repo search

The task-specific prior note `prior/gap-boundary-q-check-astra.md` is absent at
`9a361261c000ae192204e2230a156f91f39b0709`. The supplied brief reports a lead search
of main and PRs 10114, 10133, 10134 and 10141. The November 8 digest concerns
older RG targets; it does not identify a supplier for this boundary-frame check.
The source itself, L48, says its author did not search those branches.
The exact target is row 1036; row 1037 is the requested later comparison,
not a duplicate proof assignment. The open-registry search found no separate
owner of this check. Current-main rules were read through `git show`; the
scientific source under check remains the pinned checkout.

Read refs: main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`; PR 10141
`a2f6a430e251aa47bc3eb4f67a1dca2a88530116`. Target source SHA-256:
`5556a242ef32064b136a81e7fb67123292b3a4098b7a49421dc7f96d00b795ab`.

Writer: OpenAI Codex, GPT-6 (task label: Astra; this session does not expose
a more precise runtime model identifier or reasoning-effort setting). Research check
of `gap-boundary-q.md` L1–391 at the commit above; not an audit, no status grant,
no mass gap. No numerical or computer-assisted proof, and no Lean run.
Not covered: typical-pin estimates, upper-face extensions, general boundary
fields, or an existence theorem for a successful frame rule.

Reading-order disclosure: the initial FINISH anchor search accidentally
displayed row 1037's result summary. I had not opened the Claude check file.
The derivations and verdicts below are written before opening that file;
this is a cross-provider check, but not a blind one.

Source downloads, each fetched once, are in
`/tmp/sa-gap-boundary-q-check-astra.UP9wkK/` (`sa_ym4.tex`, `sa_ca_I.tex`), pinned
to Sussman–Alpoge commit `31a47c543775`. Credit Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text, for their account and methods.
Source locators and the comparison with earlier repository work follow below.

Working sequence: verify definitions and prior sources; GR; cube; TP/TP4 and
open-set construction; H4/MASS/SIGN; scope and numbered verdicts; only then
read the Claude report and record every disagreement.

### Sources and near matches

The November 8 digest L134–157 points to boundary-gauge admission, a different
operator problem. I fetched PR 10141 and read `research/ym4d/library/out-pi.md`
L324–391 (the older digest's lines have shifted). Its Proposition 3.1 leaves
boundary admission additional; Propositions 3.2–3.3 concern a compressed
Hessian, not this pinned free-energy derivative. I also read main's
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
L120–145. Its score identity is for a supplied noncompact Maxwell law, not
the compact SU(2) cell. Neither supplies this check. This is a targeted
verification of the lead's near matches, not a new exhaustive branch search.

The closest same-lane sources actually used are `gap-short-step-max.md`
L217–246 (FLOW and its Haar change of variables), `gap-aligned-frame.md`
L200–213 (cost and boundary/interior distinction), and `gap-sym-reg.md`
L34–43, L349–375 (frame class and the existential O2). These are credited
to their Claude authors. In particular O2 says **on a set of pins of positive
measure**, not on every pin. The target does not replace that quantifier.

I consulted the SA-index README, chunk-01 L24–29, chunk-02 L80–96,
the matching obligations entries, and CA-4.12-4.19 chunk-01 L55–62.
The corresponding source reads are outline L240–260 and L2197–2243,
and CA-I L43095–43110. The Wilson convention is a definition; GL3 and its
positive, factorially decreasing character coefficients are proved in the
outline. The target's coefficients are `u_d = exp(beta) c_l`, with `d=2l+1`.
That published calculation is prior work, not a new result of row 1036.
The CA passage defines a constrained classical action and criticality; it
does not evaluate the present pinned thermal Hessian. No Balaban paper is
imported here. Index searches for pinning, boundary gradients and frame-curl
identities supplied no further direct supplier; this is not an absence
theorem about the complete account.

## Own verdicts, before opening the Claude check

Line numbers below refer to `gap-boundary-q.md` at the pinned commit.
HOLDS concerns the mathematical implication only. Guide computations are
excluded. Boundary frame values are frozen at the initial pin when defining
the fixed exponential boundary rotation; differentiating the frame rule
again would define a different curve and need an acceleration term.

### 1. Definitions and GR: L19–97

**Definitions L19–44: HOLDS AFTER CORRECTION.** Read L22–23 as the necessary
gradient restriction of a pin-uniform curl bound. The original existential
O2 of row 1034 has not thereby become a pin-uniform statement. The identity
`H_c = Q - Var(Psi)` follows by differentiating the finite compact integral;
interior integration by parts applies only with the named REG hypotheses.

**GR(a)–(e), L65–93: HOLDS.** Here is the sign and acceleration check.
For a pinned link x→y put `n=n_x`, `m=Ad(omega_l)n_y`, `tau=lambda_y`.
Gauge by `g_x^{-1}`, with `g_x=exp(eps lambda_x n_x)`. The returned link is

    exp(-eps tau n) omega_l exp(eps tau n_y) = W_l(eps) omega_l.

A free link with nonzero V has its tail in L and no head in the support
of lambda, so its two left factors cancel. This proves (a) pointwise,
not merely after integration. Direct differentiation gives

    W' = tau(m-n) = b,
    W'' = -tau^2 |n-m|^2 - 2 tau^2 n×m = -|b|^2 + 2c,
    c = tau^2 n×(n-m).

Thus `A'=-sum b_l·N_l`, proving (c). Since
`Re(vq)=-v·Im(q)`, the single-link contribution to `-E A''` is
`tau^2(|Dn|^2 E Re(omega S)+2(n×Dn)·E N)`; the distinct-link terms are
`-E M(b)` with ordered pairs as printed. This checks (d), including its sign
and factor two. Haar change of variables gives the equality of partition
functions along the two pin curves. Two logarithmic derivatives then give
(e). No minimizer of the FLOW variational problem is used.

**Reading L94–97: HOLDS AFTER CORRECTION.** Replace the iff by:
“The explicit gauge return has W_l identically 1 on every pinned link iff
`lambda_head D_l n=0` there. This is sufficient for the original move to be
gauge and for Psi, Q and H_c to vanish.” Do not identify a nontrivial W with
a nontrivial *gauge orbit* of pins: Example A itself has nontrivial W but
unchanged gauge orbit and H_c=0. Nor does vanishing Q imply Dn=0 (SIGN).
The U(1) statement holds with the same constant axis at all sites.

There is an explicit counterexample to the unrestricted iff at L95 within
GR's stated “any finite set of plaquettes” setting. Take only the bottom
plaquette, all four links pinned, and lambda the indicator of 110.
Set n_100=n_010=i and n_110=j. The original move rotates the two incoming
links by exp(-eps i), exactly a gauge transformation at 110 by exp(eps i).
Nevertheless both incoming Dn equal i-j. The sufficient condition above
is the correct statement; the particular gauge chosen in GR need not be
the gauge that realizes a pure-gauge move.

### 2. The cube: L99–167

**C1–C2 and CUBE-Z (4.2): HOLDS.** The five unpinned plaquettes form a
disc with the prescribed boundary holonomy. After fixing the four vertical
links by Haar substitutions, integrating four top-edge variables convolves
five central kernels. A dimension-d component has multiplier u_d at each
integration, so the answer is `sum d u_d^5 chi_d(h)`, times `exp(b_0 t(h))`.
This also gives the independently weighted formula L111 without a missing
dimension factor. The source's character power-series argument gives
`u_d,u_d'>0`; normal convergence follows, for example, by bounding each
character expansion of `(chi_2/2)^k` in absolute value by its value at 1.
The sum is bounded by `sum beta^k/k!=exp(beta)`, locally uniformly with
beta derivatives. For derivatives in h one can use the factorial decay
already proved in GL3. These are written series bounds, not computation.

Differentiating one strength, not all five, yields

    xbar = (sum d^2 u_d^4 u_d') / (sum d^2 u_d^5).

The factor five therefore does not appear. Strict positivity follows from
the coefficient signs; strict inequality xbar<1 follows because a free
plaquette is nonconstant under a strictly positive Haar density.
Using `chi_d(exp(phi a))=d-d(d^2-1)phi^2/6+O(phi^4)` gives exactly the
printed kappa. Since `chi_d(h)<=d` and the coefficients are positive,
F_c is minimized at the trivial boundary holonomy. These claims do not
require the recalled Bessel formula or any guide number.

**CUBE(i)–(iv), L122–137: HOLDS.** A useful direct check keeps the two
moving incoming links separate. Their side plaquettes contribute
`beta xbar |delta_1|^2` and `beta xbar |delta_2|^2` to Q. The bottom loop is

    W_1 W_2^{-1} = exp(-eps n_100) exp(eps n_010),
    Re(W_1 W_2^{-1}) = 1 - (sin^2 eps)|n_100-n_010|^2/2.

The top plaquette does not move. This proves (ii). Differentiating the
one-variable partition function proves (iii), and FLOW gives (iv).
For arbitrary lambda the bottom first-order loop is the oriented sum of
b_l, and each side contains only its own b_l, proving L136.

**Examples A and B, L140–146: HOLDS.** In A the two squared differences are
2 and 2 and their difference is zero: `Q=4 beta xbar`, `H_c=0`.
Changing the outgoing free-link axis to i gives the exact gauge extension.
In B the squared differences are 2 and 0, so
`Q=2 beta xbar+2b_0`, `H_c=2(b_0+kappa)>0`. For this fixed boundary
rotation every admissible interior extension has cost at least H_c.

**Covariant cube assertion, L149–152 and table L368: FAILS as stated;
first failing inference L150–151.** Stabilizer invariance gives
`n_z = sigma_z s(h_z)/|s(h_z)|`, `sigma_z in {+1,-1}`. It does not give
one common sign or Dn=0. Repair text: “A coherently transported choice
of the plaquette axis, with the same sign at every site, has Dn=0 and
zero gradient cost. Covariance alone permits site signs and does not
imply that conclusion.” At central holonomy there is no covariant unit
vector defined on that pin, because its stabilizer is all SU(2).
For an explicit check of the missing sign hypothesis, transport the
noncentral holonomy axis around the bottom loop and multiply it by fixed
site signs with sigma_100=+1, sigma_010=-1, sigma_110=+1. This is a
covariant pin-measurable frame on a fixed cube. Along pins tending to 1
with holonomy axis i, the frozen vectors tend to (i,-i,i). CUBE then gives
limiting `H_c=4(b_0+kappa)>0` and `Q=4 beta xbar+4b_0>0`; continuity
preserves positivity at sufficiently nearby noncentral pins. A further
same-rule or sign-coherence restriction must be stated if this frame is
to be excluded. Reducibility is not a requirement that every chosen frame
be parallel.

**L147–148, 155–167: GUIDE ONLY, not verified.** The numerical values and
the author's lock/log narrative are not proof premises. I did not rerun
them or inspect unavailable scratch outputs. All exact cube verdicts above
come from the displayed finite integrals and series.

### 3. TP, TP4, OPEN-SET and SIGN: L173–259

**TP (5.1), L173–191: HOLDS.** With S_mu>=2 a non-boundary plaquette has
zero, one, or two adjacent pinned links. If it has two, cyclically order
the loop so that the two pinned edges and their W factors are consecutive;
all remaining factors form one free product R. Four pinned links give
R=1. Thus global conjugation symmetry at pin 1 gives
`E R=(E Re R)1=xbar_p 1`. The scalar quadratic term in an ordered product
of the moving factors is `-|sum [p:l]b_l|^2/2`; all imaginary accelerations
and commutators disappear from this expectation. This proves the printed
formula without assuming xbar_p>=0. The pure-gauge covariance remark and
the boundary-only action check hold. TP is an identity, not a positivity
theorem for arbitrary b and arbitrary plaquette means.

**TP4 (5.2), L193–211: HOLDS.** For each nonzero incoming b_i=delta_i,
there is one inward (i,4) plaquette of weight 1 and two forward tangential
plaquettes of weight 1/2. For each pair i<j there is one backward
tangential plaquette containing both b_i and b_j with opposite incidence.
These give, respectively,

    beta sum_i xbar_i |delta_i|^2,
    beta sum_i |delta_i|^2,
    (beta/2) sum_{i<j}|delta_i-delta_j|^2.

All moving-link plaquettes in this count have precisely the printed
weights, even when a neighbour of z meets another face. At the trivial
pin every relevant inward plaquette has a nonconstant free link and a
positive density; t>-1 almost surely, hence 1+xbar_i>0. This proves strict
positivity if some delta_i is nonzero, without assuming xbar_i>0.
The general sign of H_c is not inferred from Q. The one-delta exception
added at L210–211 is justified by H4 below.

**OPEN-SET (5.3), L213–229: HOLDS.** For a fixed finite cell the density,
forces and their moments are continuous in the pin. Compactness of the
four frozen axes makes this uniform over them. The two changed links
in L224 are distinct and are the reversed top edges of the selected
plaquettes, so their axes are exactly i and j. The other two holonomies
can be made noncentral by arbitrarily small perturbations: each has a
link variable on which its holonomy depends by left/right multiplication,
so its central locus has no interior. This preserves the strict axis
separation. The displayed subtraction actually gives the stronger lower
bound beta(1+xbar_1), so L218 is safe. A nonempty open pin set has positive
Haar measure; finite Wilson conditional densities are strictly positive.
This proves failure for this particular local, covariant rule on an open
set. It does not rule out a different rule or a different positive-measure
set. No assertion that the rule is defined at the trivial pin is needed.

**SIGN (5.4), L231–244: HOLDS AFTER CORRECTION to its scope.** The identity
L236 holds exactly: `|Dn|^2=2(1-cos alpha)` and `n_tail×Dn=sin(alpha)nu`.
Only one moving returned link means M(b)=0. The expansion is

    Q(alpha) = 2 alpha nu·f_l + e_l alpha^2 + O(alpha^3).

Thus both signs occur if nu·f_l!=0. One can arrange that by choosing m not
parallel to f_l and then choosing nu along its perpendicular projection.
A nonstationary F_c somewhere does not ensure that a preselected incoming
link or a preselected m has this property. Replace the title by:
“At an incoming link with f_l!=0, suitable pin-measurable choices of axes
give both signs.” The formula for the second zero holds with e_l>0 and
the nonzero projection, as stated in the proof. At a stationary pin the
linear force term vanishes, but positivity is established here for the
specific trivial-pin TP4 configurations, not all stationary pins.

**Q-INV verdict (5.5): HOLDS AFTER CORRECTION.** The universal claim is
false: L248 is an exact finite-range pin-measurable counterexample;
L251 adds a genuinely covariant open-set counterexample. L250 needs
“if some delta_i!=0.” Replace L252–254 by the sufficient zero-return
condition `lambda_head D_l n=0`, and the constant-axis U(1) control.
Dn=0 just on the incoming star does not force the surrounding pin to be
reducible: transport an arbitrary n_z to its incoming neighbours; that
star has no cycle. Reducibility follows only when Dn=0 is required on
the whole relevant connected loop network. L255–257 correctly leave a
special frame rule open. At a fixed boundary rotation with H_c>0 no
*interior extension* helps; changing the boundary frame changes H_c too.
L258–259 is too broad: a neighbourhood with a positive lower bound
requires a nonzero limiting defect, not merely Dn!=0 at each pin.

### 4. H4, MASS and O2: L261–322

**H4(i) (6.1), L269–281: HOLDS.** Put delta_2=delta_3=0. TP4 gives
`Q=beta(2+xbar_1)|delta_1|^2`. The four tangential staples are real at pin
1; the only imaginary staple is the inward plaquette R_1, with coefficient
beta. Its mean vector is zero. Its second moment matrix commutes with
every spatial rotation of Im H, hence is `(E|Im R_1|^2/3)I`. Consequently

    Var(Psi)=beta^2 |delta_1|^2 E(1-t_p1^2)/3,
    H_c/|delta_1|^2 >= beta(2+xbar_1)-beta^2/3
                     = beta[(1+xbar_1)+(1-beta/3)] > 0

for delta_1!=0 and 0<beta<=3, including beta=3. This proves the exact
formula and lower bound in L272. It proves nothing for several nonzero
delta_i, whose force cross-covariances have not been bounded.

**H4(ii), L274–289: HOLDS.** The four changed direction-1 links in
L284–287 occur in exactly one each of the four selected (1,2) plaquettes.
Three holonomies have axis j and the fourth i, including the positive
bottom edge at z-e_2. Their axes are precisely (j;i,j,j). The pins tend
to 1 as phi decreases, while these four axes stay fixed. Continuity of
the finite integral therefore gives an open set with H_c>0. Every
admissible FLOW extension of that *same* fixed boundary rotation has
Q>=H_c. This does include arbitrary smooth field-dependent interior
vectors, not only site-frame extensions. The beta<=6 observation at L290
is conditional on the additional, unproved xbar_1>0, as printed.

**MASS (6.2), L295–309: HOLDS AFTER CORRECTION; first failing hypothesis
L295 and first potentially false inequality L298.** For signed strengths
replace `beta_p w_p<=b` by `|beta_p w_p|<=b`, and replace each coefficient
on the right of L298 by `|beta_p w_p|`. Alternatively explicitly assume
`0<=beta_p w_p<=b`. Without this repair a single negative-strength
plaquette gives a nonpositive right side for a generally nonzero
absolute value. The original cell class permits signed strengths
(`gap-pinned-cell-gauge-max.md` L141).

To check 60, set `a_l=|tau_l||Dn_l|`. Twice differentiating the product of
unit quaternion factors gives at most `(sum a_l)^2+2 sum tau_l^2|Dn_l|`
per plaquette. Inverse-oriented factors obey the same norm estimates.
Cauchy gives `(sum a_l)^2<=4 sum a_l^2`, and a four-dimensional link meets
at most six plaquettes. Thus the coefficients are 24 and 12; using
`|Dn|^2<=2|Dn|` gives 48+12=60. This proves the corrected bound by hand.
It is an absolute-value upper bound. It is not a lower bound, a proof
that Q is positive, or a proof that small defect is necessary for a
curl estimate. SIGN proves the genuinely linear contribution away from
stationary pins. U(1) gives zero for constant-axis gradients.

**O2 verdict (6.3): HOLDS AFTER CORRECTION.** Replace L312–315 by:
“No curl bound can hold uniformly over pins and boundary frame choices.
It fails for the frames and pins of CUBE, TP4 and OPEN-SET. Where H_c>0,
no change of interior extension repairs the fixed boundary rotation.”
Existential O2 on some positive-measure set remains open. L316–317 must
describe MASS as a sufficient upper bound, not identify Q with its right
side or infer a zero-cost iff. L318–320's mirror arithmetic is correct,
but the deduction ‘No gain follows’ FAILS at L319: no premise requires
averaging a selected frame with its mirror, nor gives the sign of e_l
at every pin. A negative Q for one lambda also does not prove O2 for
all boundary lambdas. L321–322 is OPEN, but not equivalent to N1:
MASS supplies one sufficient control; cancellations with order-one Dn
have not been excluded. N2 and N3 of row 1011 are additional obligations.

### 5. U(1), route scope and the final summary: L324–391

**U(1) (7.1): HOLDS with the stated constant-axis convention.** In that
convention every plaquette phase changes by eps(d theta)_p, so

    Q(theta)=sum_p beta w_p E[cos F_p](d theta)_p^2
             <= beta sum_p w_p(d theta)_p^2.

Adding a boundary gradient changes no curl or Q. A gradient has Psi=Q=H_c=0.
There is no gain. The convention matters: U(1) covariance by itself does
not prohibit artificial site-dependent signs for its one-dimensional
Lie algebra. L330's attribution solely to Ad!=1 must therefore be
restricted to these compared frame conventions.

**Route reading (7.2): FAILS.** The first excessive generalization is
L335–336: ‘at and near a pure-gauge pin’ is not a uniform assertion about
all frame rules, and the displayed local TP4 formula is not a positive
mass term for every lambda and every pin. L337–338 additionally requires
the CUBE Example B or the H4 one-delta/constructed-open-set hypotheses.
The decisive quantifier failure is L340–345: excluded boundary rotations
are replaced by all pin-measurable boundary frames. The exact conclusion
is that the named frames cannot yield a pin-uniform curl bound. This
does not close route (ii) at the pinned boundary.

The following classes are still open here:

1. Rules whose defects tend to zero on pure-gauge pins. The positive
   neighbourhood argument fixes a nonzero limiting defect; it provides
   no uniform conclusion when that defect collapses. A frame transported
   from one common face base point illustrates this collapse on a fixed
   cell. Such an illustration is not automatically a uniformly finite-range,
   same-rule construction on arbitrary cells; that separate LOC condition
   still has to be checked for any proposed route.
2. Rules on nonstationary pins with order-one defect, where the force term
   in GR can cancel the direct term. SIGN shows this possibility for one
   direction. It neither solves nor refutes the simultaneous quadratic
   condition for every boundary lambda, nor the cross terms required for
   Q-INV on general theta. This class cannot be replaced by small-defect N1.
3. Even near the trivial pin, positivity of Q for a supplied extension
   with several delta_i does not settle whether a different interior
   extension works when the corresponding H_c has not been shown positive.
   H4 excludes that repair for its fixed boundary data only. General beta,
   upper faces and general boundary fields retain the limits in L347–355.

**Limits (7.3): HOLDS.** They must also govern the summary. **Step 8,
L363–391: HOLDS AFTER CORRECTION to the individual entries above.** Keep
GR(a)–(e), CUBE-Z, CUBE(i)–(iv), TP, TP4, OPEN-SET, and H4 with their full
hypotheses. Correct MASS, the covariant cube assertion, the Q-INV iff,
and the O2 quantifiers. Delete the claim that route (ii) is closed and
the assertion that N1 is the only remaining option. Replace L384–389 by:
“Universal boundary-gradient invariance and a pin-uniform curl bound fail
for the exhibited frames. Some fixed boundary rotations have H_c>0,
which excludes all interior extensions for those data. H4 proves this
for one nonzero delta at pin 1 and for its explicit axis-frame open set,
at 0<beta<=3. The existential boundary-frame problem remains open.”

L1–18 and L46–63 are provenance/planning rather than mathematical
statements. The author's claimed timing and scratch runs are not independently
verified. L169–171 and L261–267 are section summaries and inherit the
quantifier repairs above. No independent mathematical statement in L1–391
is omitted from the verdicts; the source is not edited.

## Comparison with the Claude check

Only after saving all preceding verdicts did I open
`gap-boundary-q-check-opus.md`, L1–210. It is Claude Opus 5.5's report on
the same 391-line source. The accidental earlier exposure to its FINISH
summary is disclosed above. The agreement is substantial: GR(a)–(e),
CUBE-Z, CUBE(i)–(iv), Examples A/B, TP, TP4, OPEN-SET, H4 with its scope,
and the constant-axis U(1) calculation all hold. Both reports reject the
route-closing conclusion and the mirror-frame argument. Both retain
collapsing-defect rules and nonstationary-pin cancellations as open.
The following are all differences in verdict, repair, or scope found in
this comparison. “Opus L…” refers to its check; “source L…” to row 1036.

1. **MASS's repair is incomplete in Opus L134–137, L192, L206. This check
   is right on the missing absolute values.** Opus says changing the
   hypothesis to `|beta_p|w_p<=b` makes “both displays” hold. Source L298
   still has signed beta_p w_p on its right. Take one all-pinned square,
   coefficient -1, lambda at 110, and axes n_100=n_110=i, n_010=-i.
   Only one returned velocity is nonzero, of length 2. The original
   plaquette trace is cos(2 eps), so A=-cos(2 eps), Q=-4, and |Q|=4.
   The uncorrected L298 right side is `-[(2)^2+2(2)]=-8`.
   The repaired hypothesis holds with b=1, but `4<=-8` is false.
   Correct both the hypothesis and L298, as in own verdict 4 (MASS). Opus is
   right about the 60 constant and the upper-bound-only interpretation.

2. **The pure-gauge iff is not covered by Opus's GR verdict at L182
   (which labels source L65–97 HOLDS). This check is right to correct
   source L95.** The all-pinned example in own verdict 1, with
   n_100=n_010=i and n_110=j, has a pure-gauge original move with nonzero
   Dn. The displayed GR
   formulas remain right, as both reports find; the iff concerns an
   additional interpretation. A trivial *chosen gauge return* and an
   arbitrary pure-gauge realization are different claims. Source L373's
   “true iff” also cannot follow from Q=0; SIGN allows cancellations.

3. **Covariant cube: the verdict labels differ, the mathematics agrees.**
   Opus L97, L115 and L186 say HOLDS AFTER CORRECTION; I say the original
   universal statement FAILS at source L150–151 and give its narrower
   replacement. Both are right about the necessary site signs. Opus's
   signs produce a positive-Q example with zero H_c in the trivial-pin
   limit. My different sign choice also gives positive H_c there and
   nearby. Neither rescues the original assertion that every covariant
   cube frame has zero cost. These are finite-cell examples; a separate
   same-rule restriction cannot be silently inferred from covariance.

4. **SIGN: Opus L139/L190 calls the entire passage HOLDS; I qualify its
   heading.** Both are right about source L236 and the conditional
   sign calculation. For a chosen l and m the needed condition is
   `f_l` not parallel to m and a choice of nu with `nu·f_l!=0`.
   Nonstationarity somewhere in the pin is not that condition. This
   check's narrower replacement is required if the heading or summary
   is read without the condition at source L240. There is no disagreement
   about the formula once that condition is retained.

5. **Earliest failure and repaired route wording.** Opus L164/L197
   identifies source L340–341 as the first failure. That is the decisive
   quantifier leap, and Opus is right to reject it. I identify the earlier
   overstatement at source L335–336, which Opus L164 itself also corrects:
   positivity near the pure-gauge orbit requires a defect bounded away
   from zero, and the TP4 sum is a lower bound rather than the full cost.
   Moreover Opus L166's “corrected meaning” again says Dn!=0 “at and near”
   the orbit, and says “on the cube (every beta)” without Example B's
   `n_100!=n_010` condition. Read it with Opus's own P2/P3 at L151–152;
   literally it needs those qualifications. The explicit replacement in
   own verdict 5 retains them. Opus L169–171 is consistent when read with
   those qualifications.

6. **Common-base frames at pure gauge, Opus L154–155/L200.** The open
   class is correctly retained by Opus. Literally, however, its chosen
   plaquette-axis a(omega) is undefined on a pure-gauge pin. No covariant
   unit vector can be defined there: the global SU(2) stabilizer at pin 1
   has no fixed unit vector. The correct assertion is that Dn tends to
   zero and Q has a zero limiting value, independent of the undefined
   root axis; the bound `|Dn_l|<=2|s(H_l)|` proves this. On a fixed face
   the construction has finite range. Opus's parenthetical caveat about
   range growing with cell diameter is right and essential. It is not
   a construction satisfying uniform LOC and the same rule on arbitrary
   cell sizes. This is a qualification of the example, not a closure
   of the remaining class.

7. **Pin-dependent interior extension, Opus L143: an unnecessary
   restriction.** For the pin-only turning of the free-link vector
   described there, its extra term actually vanishes at *every* pin:

       E_omega N_l^a = -(1/Z_c) int R_(l,a)(exp A) dU_int = 0

   for a free link l, by Haar invariance. The coefficient V n_z is a
   function of the pin alone under the fixed boundary rotation, hence
   can be taken outside that expectation. Thus freezing versus turning
   this pin-only interior vector does not change Q at the base pin.
   Opus is right that OPEN-SET is unaffected, but its special conditions
   (not reading incoming links, or being at the trivial pin) are not
   needed for this expectation. This says nothing similar about a frame
   depending on integrated links, or about changing the *boundary curve*.

8. **U(1)'s frame convention.** Opus L141/L193 and the source use one
   common axis; on that convention they are right. My qualification only
   prevents extending “always” to arbitrary site signs, which covariance
   alone permits in U(1) as well. The intended zero-gain control is not
   disputed.

There is no disagreement about the surviving two principal boundary
classes or the failure to settle existential O2. My additional reminder
about several nonzero delta_i and alternative interior extensions follows
from the general H_c case that both reports explicitly leave open.
Neither report proves a successful frame rule, a seed estimate, or a
mass gap. No guide value has entered a mathematical verdict. Mechanical
file checks only confirmed the pinned source was unchanged, that this is
the sole new repository file, and that it ends with one RESULT line.
The report remains local and uncommitted on
`codex/gap-boundary-q-check-astra-20261116`; no remote write was performed.

RESULT: Cross-provider research check of row 1036 at 9a361261c, with the prior-summary exposure disclosed: GR(a)–(e), the cube values, TP/TP4, OPEN-SET and H4 on its stated domain HOLD; MASS HOLDS AFTER CORRECTION of both the signed-coupling hypothesis and its finer bound; the pure-gauge iff, universal covariant-cube zero-cost claim and route-closing interpretation fail as stated. Universal Q-INV and pin-uniform O2 are refuted by the exhibited frames, but existential O2 and route (ii) remain open for collapsing-defect frames and nonstationary-pin cancellations, with H4's remaining cases also open. No computer-assisted proof, no audit status, no mass gap.
