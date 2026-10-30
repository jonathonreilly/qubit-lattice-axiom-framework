**Independent hostile review of TQ.md, 2026-10-29.**

The packet is ready as an **UNDECIDED research result**. Its conditional
reductions are sound at the stated scope. It proves neither the required
Wilson charge estimate nor a no-go for the flat route. No binding
mathematical correction is required. LAND below is permission to carry
this scoped note forward, not a finding that H_Euc, Yang–Mills existence,
or a mass gap has been established, and not an audit-status assignment.

This review follows `briefs_q/TQ/REVIEW.md`. The reviewed source is all
560 lines of `TQ.md`, SHA-256
`c184ec1ad4dfae8626676e99e4bc6ec2ec513c6230a6dc38b21ec00ba6d640aa`.
Working HEAD is `3bba91875672becadc0ab120204905d9f1f405a8`;
fetched `origin/main` is `01589af3faf806b736c42dc2f3bd625e9edead9f`;
the planning reference is `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
The scientific sources are the supplied working-tree proposals, not claims
of adopted main/audit status. All 13 entries in `checks/tq_sources.sha256`
matched both before the substantive checks and before writing this report.

This session did not author the note. The earlier `checks/tq_review.md`
and its verdict became visible during source inventory; this is therefore
not a blinded review. Its conclusions are not evidence for the judgments
below. This is another same-family Codex review, with independent written
calculations, not cross-family validation. No model change or delegation
was made.

| Item and target lines | Verdict | Fix or disposition |
|---|---|---|
| Precise pair statement and normalization, 28–118 | CONFIRMED, conditional | No fix. Preserve the selected sequence, normalization, corrected contacts and averaged CD hypothesis. |
| Ward identity and necessity, 117–172 | CONFIRMED, conditional | No fix. E6 is required for the derivative-norm converse, not the integrated sufficiency argument. |
| Annular criterion and RA repair, 174–198 | CONFIRMED | No fix. Actual reflected autocorrelation bounds remain an input; SRC-E′ cannot replace a fine-variance estimate by renaming it. |
| Fixed-volume comparison and truncation, 203–239 | CONFIRMED, conditional | No fix. Both comparison hypotheses and the tails for the actual approximants must be proved. |
| Slow diagonal, transport and orientation witness, 243–313 | CONFIRMED at the stated abstract scope; VQ OPEN | No fix. The witness does not falsify Wilson TQ or exclude a different volume-limit argument. |
| Feasibility and gapless comparators, 317–383 | CONFIRMED as logical compatibility; Wilson feasibility OPEN | No binding fix. An optional flux-sign clarification is given below. |
| All-observable settling lemma, 387–452 | CONFIRMED, conditional and target-equivalent | No fix. Neither U-all nor TQ-min is produced by the pair result. |
| Sphere comparison, 456–483 | CONFIRMED, conditional | No fix. Invariant sphere states, all-product control and the limiting bounds remain unconstructed here. |
| GO/NO-GO/UNDECIDED and scope discipline, 3–17, 446–452, 485–560 | UNDECIDED is supported | No fix. Do not promote the residuals, examples or review verdict into a Wilson theorem or audit status. |

For the first two items I reconstructed the finite-dimensional identity
directly. Write the Wilson density as exp(−S_W) times Haar measure. On the
compact configuration manifold,

    0 = integral div(F Xi exp(−S_W))
      = integral [Xi F + F div Xi − F Xi S_W] exp(−S_W).

Taking F=1 makes W=Xi S_W−div Xi mean zero. Thus
omega(Xi F)=Cov(F,W). For A=O(f_s), B=O(g_s), differentiating
omega[(A−omega A)(B−omega B)] gives

    Cov(A',B) + Cov(A,B').

The two differentiated means multiply variables with expectation zero.
With B_r=W_r+T_r and the note's definition of C_j, this gives exactly

    S'_j(s) + t_j(s,r)
      = Z_j^−2 [Cov(F_tilde,B_r) − C_j(s)].

The sign, centering, Haar divergence and powers of Z_j in (4) are correct.
The estimate of its right side is assumed in (2), not derived by defining
C_j or B_r. This distinction prevents the exact identity from becoming a
tautological success signal for the missing estimate.

The discrete shell statement also survives an explicit check. For a
forward difference,

    nabla_mu[psi(x)(Jx)^nu]
      = (nabla_mu psi)(Jx)^nu + psi(x+a e_mu) J_{nu mu}.

Pairing the second term against a symmetric tensor leaves
J_{nu mu}[psi(x+a e_mu)−psi(x+a e_nu)] for mu<nu. Both parts vanish where
the cutoff and its neighboring values are constant. Their coefficients
are bounded by C ||J|| ||h'|| on the enlarged shell, since |x|=O(r)
there and a/r is eventually small. A variable trace is not annihilated
exactly: for a radial cutoff locally proportional to |x|² and
Jx=(−x_2,x_1,0,0), its discrete contraction is proportional to
a(x_1−x_2). A spatially varying trace can retain this term. The no-wrap
margin in the note is sufficient.

Subtracting the two identities at fixed radii gives a vanishing difference
of fine charges. The allowed O(g_j²) contacts still tend to zero; one
must not copy the older contact-free finite-j radius estimate. Under E6,
the derivatives converge uniformly because they are the two derivative-test
correlations just displayed. If their sum tends to H, then

    S(s)−S(0) = integral_0^s H(u) du,

so H=S' and t_j(.,r) tends uniformly to −S'. In particular the fixed-r
limsup norm is ||S'||, independently of r. This establishes precisely
the necessity claimed at lines 157–160.

For the coarse charge, expand each observable into its conditional mean
and its mean-zero conditional remainder. The cross terms vanish after
conditioning, leaving

    t_j−q_j = Z_j^−2 E[Cov(F_tilde,T_r | U_K)].

Insert the actual finite shell sum and apply (3) term by term. Its physical
volume is O(r⁴), its coefficients are bounded, and its distance from the
test supports is at least r−rho_F−1. Therefore

    sup_s |t_j−q_j| <= C_F r⁴ exp[−mu(r−rho_F−1)].

Taking limsup_j and then r→infinity proves equivalence with TQ2. No
strict locality of E_K F, common random prefactor, or decay of the
unconditional coarse law was used. Conversely, without E6, integrating
(4) still proves sufficiency of (6) whenever the endpoint expectations
converge. S_j(s)=−sin(js)/j and t_j(s)=cos(js), with e_j=0, demonstrate
why endpoint invariance does not imply convergence of derivative suprema.

For the annular criterion, the same coefficient bound gives
||t_j(.,r)|| <= C times the actual sampled absolute covariance sum.
Hence ||S'|| <= C A_F(r) for every fixed admissible r. Its liminf along
any sequence of large radii suffices. If every sampled covariance is at
most C_F |x|^(−4−epsilon), the O(r⁴) physical-volume bound gives
A_F(r)<=C'_F r^(−epsilon). This is a conditional sufficient estimate,
not an inference from numerical samples or a continuum envelope defined
only almost everywhere.

The RA warning is justified independently of the older review. With a
coarse sigma algebra independent of a centered variable X of variance one,
Y_n=nX has E[Y_n|coarse]=0 but Var(Y_n)=n². Thus conditional-image L²
control cannot bound discarded fine variance. The total-variance identity
shows exactly which nonnegative term is missing. This is a probability
counterexample to that inference, not a Wilson counterexample. For RA,
positivity of the reflected 2-by-2 covariance Gram gives the product of
the two reflected autocorrelations. Those separated quantities can be
finite even when the repeated-support fine variance is not uniformly
bounded; their required bounds still have to be supplied. Finally,
c h^(−8)<=eta(h)² h^(−8), with c>0 and eta(h)→0, is impossible. The
canonical stress rate has no RA-1 little-o margin.

For (7), put d(V)=log Z_1−log Z_2−c and use the normalized second law
rho_2. The finite nonzero partition functions obey

    rho_1/rho_2 = exp(d)/E_(rho_2)[exp(d)],

which lies in [exp(−2 delta_d),exp(2 delta_d)]. Integrating h_1−h_2
against rho_1 and h_2 against rho_1−rho_2 yields exactly (7). This also
handles complex observables and the zero-error case. Summing the per-block
polymer norm bounds the whole log-weight error by N_b eta, independently
of susceptibility. The estimate supplies neither of its two suprema.
For unbounded approximants the expectation difference is at most the
truncated comparison error plus the two tail expectations. The final
text correctly requires comparison for each fixed truncation and uniform
tails, in the order a→0 followed by M→infinity. It makes no unjustified
transfer from bounded flowed loops to a collision-flat hierarchy.

The diagonal choice is valid on the compatible cofinal cutoff sets:
choose R_n to contain the first n compact test supports, and at that fixed
R_n choose a_n below their finitely many error thresholds and below 1/n.
No estimate uniform in R follows or is needed for this selection. This
does not supply compactness, a common trajectory satisfying other assembly
inputs, or a comparison along an already prescribed fast-growing volume.

For (8), change coordinates from x to y=Q^−1 x in the (Q,I) theory. Its
grid becomes aZ⁴ and its periods become RQ^−1 Z⁴. This bijects oriented
bonds and plaquettes, preserves product Haar measure and Wilson weights,
and carries F_Q back to F when all observable data are transported.
Adding and subtracting that transported expectation gives exactly the
two terms and signs printed in (8). For the chosen rational Q, R/a
divisible by 10 makes the transformed periods integral and even; it does
not make Q preserve the original period lattice. Likewise J(x+Rz)−Jx=RJz
shows why the linear rotation field does not descend to that torus.
The second difference is therefore a separate comparison unless another
argument is supplied. Under the first comparison it is target-equivalent
to Q-invariance, exactly as the note says.

The orientation example is a legitimate counterexample to the weaker
abstract inference. Each component has strictly positive Fourier covariance;
an equal mixture is a positive, translation-invariant law, although the
mixture itself need not be Gaussian. Its covariance difference in (9)
reduces to

    c² / [4 b(b+c)(2b+c)] > 0.

This also detects the note's particular rational Q, not just a 45-degree
rotation: replace the two interior denominators by b+alpha c and
b+(1−alpha)c, with alpha=9/25. The difference from the axis value is

    c² alpha(1−alpha)(2b+c)
    / [4 b(b+c)(b+alpha c)(b+(1−alpha)c)] > 0.

The Fourier covariance functions are continuous, so a nonzero difference
can be detected by smooth test functions; density then permits compact
tests. Fourier Riemann sums converge for these tests. Uniform domination
of the covariance operators by m^−2 I supplies local tightness as well:
after a compact spatial cutoff, expected negative Sobolev norms of order
s>2 are uniformly finite in four dimensions, and passing to a slightly
weaker norm gives compactness. None of this identifies the assignment
with a Wilson action or the matched stress/source hypotheses. The note
explicitly excludes that stronger interpretation.

The gapless scalar comparator can be constructed, rather than assumed
to have the desired symmetry. The map f -> f_hat/|p| takes real Schwartz
tests into the real momentum Hilbert space: its squared norm near zero
has radial measure proportional to r dr. Applying independent standard
Gaussian coordinates to an orthonormal expansion gives the centered
Gaussian family with the covariance displayed at lines 329–331.
Rotations act unitarily on this Hilbert
space, so every Gaussian moment is invariant. No Yang–Mills input enters.

Independently invert −d_t²+|k|². The decaying solution away from zero is
A exp(−|k||t|); its derivative jump fixes A=1/(2|k|). For positive-time
tests the reflected covariance is consequently

    integral d³k/[(2 pi)³ 2|k|]
      |integral_0^infinity exp(−|k|t) f_hat(t,k) dt|² >= 0.

Its exponential generating kernels are positive by expanding the
exponential in tensor powers of this Gram kernel, so the Gaussian
polynomial algebra is reflection positive. The one-particle energies
|k| have nonzero spectral measure arbitrarily close to zero. This verifies
gaplessness and avoids silently treating Euclidean symmetry as a gap.

For the separated stress insertion, subtraction of its internal Wick
contraction leaves the two ways of connecting its differentiated fields
to phi(f)phi(g). The trace subtraction gives exactly the three terms
at lines 351–355. The Green function normalization follows by integrating
−partial_r[c r^−2] over a small 3-sphere: the flux is 4 pi² c, so c=1/(4 pi²).
Each differentiated crossing to a fixed compact support is O(|x|^−3);
their product is O(|x|^−6), giving the stated O(r^−2) absolute annular
bound. This calculation needs only the separated insertion, not a
coincident stress variance or an ordinary composite random field.

The spectral-rate example is also exact: the stated probability measure
has Laplace transform (1+h)^−alpha. Its reflected kernel is an integral
of the rank-one positive kernels exp(−u s)exp(−u t). Thus spectral
positivity alone fixes no decay exponent. This does not test the full
Wilson Ward/RP package. For the exterior tensor, differentiate its two
summands separately; they give respectively (Mx)_nu/r^6 and
(d−5)(Mx)_nu/r^6. Their sum is zero at d=4. On a radius-r sphere,
n_mu sigma_(mu nu)=r^−4(Mn)_nu, and contraction with Jx and integration
give |S³| tr(M^T J)/4.

There is one optional clarity edit at `TQ.md:378–380`: call this the
**outward spherical flux**. For the decreasing radial cutoff used in (1),
the corresponding annular integral is its negative, because
integral_0^infinity h'(rho/r) d rho/r=−1. The note uses this example only
as a nonzero-flux witness and never substitutes its sign into a Ward
conclusion, so this is not a blocking error.

The settling lemma is the correct all-order obligation. Integrating (10)
over the one fixed angle gives

    integral_0^theta tau_j^F ds
      = S_j^F(0)−S_j^F(theta) + integral_0^theta e_j^F ds.

Both endpoint tests belong to D. Their limits exist on the same sequence,
and the last integral tends to zero. Hence TQ-min is equivalent to
S(F_Q)=S(F) on D without requiring convergence at intermediate angles
or E6. This verifies both directions, not only sufficiency.

I checked the angle by a different exact argument. If
z=(3+4i)/5 had finite order n, then (3+4i)^n=5^n. The map from Gaussian
integers to integers modulo 5 sending i to 2 is multiplicative, since
2²=−1 modulo 5. It sends the left side to (3+8)^n=1 and the right side
to 0, a contradiction. Pigeonholing powers on the circle then supplies
arbitrarily small nonzero angles; their integer multiples approximate
every angle. Conjugating the resulting plane circle by H(4) gives all
coordinate-plane circles. Successive plane rotations reduce an SO(4)
matrix to the identity; a coordinate reflection supplies the other
component of O(4). Group stability of D permits finite products, and
density plus continuity of both S and the motion action extends the
equalities to the actual domain. The separately supplied translation
continuity completes H_Euc. The same endpoint identity proves necessity.

This argument would be invalid if it quietly assumed a full observable
algebra or all-order insertion estimates. The current text instead names
them explicitly in lines 387–411. ASSEMBLY55 N4 consumes all compact test
polynomials, whereas N10's mixed insertion input ends at two additional
energy insertions. Pairwise invariance alone does not determine higher
joint moments. U-all remains a substantial source/contact producer, and
TQ-min is explicitly a target-equivalent residual. The word "minimal"
describes this endpoint test under the stated architecture, not a theorem
that all successful constructions must use it.

On the sphere, contraction of a symmetric continuum stress with
nabla_(mu v_nu) vanishes for a global Killing field. There is no radial
cutoff term on the closed manifold. This does not eliminate noninvariant
regulator or seam terms. Once continuum sphere states are invariant,
the explicit embedding

    exp_N(x) = (R sin(|x|/R) x/|x|, R cos(|x|/R))

commutes with diag(Q,1) for Q in SO(4). Every convergent pulled-back
correlation therefore preserves that invariance. A rotation in a tangent/
normal plane through angle b/R approaches tangent translation by b on
bounded patches; the local error tends to zero with its fixed-order
derivatives. Passing that error through the states requires the stated
uniform local continuity. Reflection invariance is an additional input.
The sphere paragraph correctly keeps these requirements and makes no
sphere/torus state identification.

The GO/NO-GO assessment follows from these calculations. A proof of U-all
and TQ-min, or the alternative all-observable comparison plus VQ on the
same sequence, would settle this H_Euc obligation under its other named
premises. No such estimate is established here. The gapless comparator
blocks a general inference from Euclidean invariance or the displayed
power count to a positive gap; it does not settle feasibility in Wilson
Yang–Mills. The exterior tensor, spectral kernels and orientation
assignment satisfy different premise sets and cannot supply a Wilson
NO-GO. An exponential-clustering shortcut is rejected under the author's
explicit task restriction, not converted into an obstruction theorem.
The N1–N8 discussion preserves these distinctions and claims no exhaustive
search or independent wall count. The kinetic-isotropy primitive has only
its registered structural scope and contributes no interacting symmetry
or selected-state theorem.

The relevant quotations, locators and interfaces were checked against
the following source passages, not accepted from their status labels:

| Source | Read passages used in this review |
|---|---|
| `ASSEMBLY55.md` | 128–292: N1F/N1S, H_reg, N4, the common algebra/sequence, N10–N14; in particular N4 at 183–197 and N12 at 279–281. |
| `ROTDEF.md` | 96–210, 278–439, 647–679: observable, exact Ward identity, shell, total covariance, I4/I5, theorem and centering/no-wrap/E6 corrections. |
| `TQ55.md` | 72–142, 184–218, 251–319, 508–537: pair reduction, reflected covariance, RA-1, rate caveats and errata. |
| `CODEX_REVIEW_TQ.md` | 98–196, 373–443, 513–545, 628–679: selected limits, RA assumptions, Goldstone limitation and conditional sphere transfer. |
| `SRCCD55.md` | 315–435, 921–956, 990–1017: source clauses, corrected moment scope, contacts and errata. |
| `CODEX_REVIEW_SRCCD.md` | 226–310: averaged CD, graph-distance conversion, product-image moment and insertion contact. |
| `UNIV55.md` | 63–198, 454–495: fixed-torus/sphere meanings, comparison implication, summability claim and sphere Ward proposal. |
| `CODEX_REVIEW_UNIV.md` | 26–114, 196–212, 319–366, 482–496: relative densities, cancellation counterexample, torus geometry and conditional sphere bounds. |
| `EUCLIDEAN_ROTATION_IMPORT_ASTRA.md` | 1–18, 102–140, 329–345, 390–419: import interface, cone scope and missing producers. |
| `REVIEW_EUCLIDEAN_ROTATION_IMPORT_ASTRA.md` | 1–18, 270–345, 448–457: same-state/global-source and full-theorem verification limits. |

In particular, the N4/N10 order mismatch, the insufficient fine-variance
substitution in N12/F19, the sufficient rather than necessary nature of
absolute covariance summability, and the unfinished reflection-to-rotation
import are accurately represented in TQ.md. The last import is used only
to keep an alternative open; its full external theorem was not verified
or used as a proof step here. No broad RG/source/tail producer has been
certified by this review.

I also checked the limited literature context recorded in `TQ_LOG.md`.
The abstract of [Gubinelli–Hofmanová, v4](https://arxiv.org/abs/1810.01700v4)
leaves rotation invariance and clustering outside its constructed
properties. The [Davoudi–Savage abstract](https://arxiv.org/abs/1204.4146)
describes perturbative restoration for smeared operators, not this
nonperturbative selected-state theorem. The direct v2 page returned a
cache error in this session; the arXiv search record and publisher
abstract supported the latter scope check. Neither paper supplied a
load-bearing lemma. Credit to Tadeusz Balaban and J. Dimock for the RG
programme is preserved; no claim of novelty is certified.

The complete author brief, review brief, PROCESS_LIGHT, TQ.md and TQ_LOG.md
were read. Repository methodology was checked against the fetched main
revision. The installed reviewer skill differed in model-label wording;
the current-main version and matching proof-search/primitive references
governed the review. Source/hash operations were deterministic bookkeeping.
Some combined displays were truncated; the relevant arguments were
retrieved again in smaller complete spans. Truncated search output and
older PASS lines were not counted as completed verification.

No numerical scientific check, old runner, symbolic program, or pool was
executed. The conclusions above rest on written derivations. The author's
reported nice failure was not bypassed. This review therefore makes no
claim to reproduce its resource observations or historical execution logs.

**Binding fixes: none.** The optional outward-flux wording at lines
378–380 does not affect the verdict. The unresolved scientific obligations
remain U-all plus TQ-min, or the all-observable UV comparison plus VQ,
on the common trajectory, normalization, selection and domain. A later
claim of GO must supply those producers; a claim of flat-route NO-GO
must quantify the selections/routes it actually excludes.

Only `REVIEW_TQ.md` was created. No source, editable prompt, axiom, audit,
ledger or other working-tree file was edited. No commit or landing action
was performed.

VERDICT: LAND
