# Repo search

**READ.** The checkout is pinned at `85e07067c7100fa735ff885d93cf2267c16960f6`.
`prior/gap-tomboulis-read.md` does not exist. The lead's
`prior/repo-search-2026-11-08.md` covers earlier ultraviolet tasks, not this
argument. Row 797 contains no separate list of repository hits.
The current registry search finds no other owner for this reading task.

**READ.** A fresh search of `origin/main` and PR heads 10114, 10133, 10134
and 10141 finds an older soft-route Migdal–Kadanoff toy calculation and
`checks/review_massgap_block_literature.md`. These are prior diagnostics,
not a reconstruction or repair of Tomboulis's proof. The earlier
literature note already isolates flow and common matching; that
diagnosis is credited and reused. Exact references and the
hard-route precedents are recorded in §6.

# Tomboulis 2007: reading and diagnosis

Author: Codex, gpt-6-astra, max; 2026-11-12; FINISH row 797.
Research text, not an audit; this grants no status. No numerical computation
discharges any statement. `PROVED` below means a written argument in this
note, not an independent check or retained standing.

Labels: **READ** gives a source page, equation or repository line;
**PROVED** gives the present author's argument; **ARGUED** gives a supported
diagnosis without a full theorem; **GUIDE** names a possible route;
**OPEN** names an obligation still lacking proof. The separate labels
PROVED IN THE TEXT, SKETCHED and ASSERTED describe the source's treatment.

Downloads and extracted reading copies are confined to the newly created
directory `/tmp/sa-gap-tomboulis-read.x7PT9F`. The outline and CA-I were
fetched once at `31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text, for their material. Their text
is not a proof of the infrared claim examined here.

## Checkpoint

**READ / OPEN.** All versions of the six named arXiv works were read
in full. Relevant later continuations and the lane consumers were
read as recorded below. The 2009 MPLA body remains unavailable.
The new local counterchecks in §§2.4 and 4 are author arguments,
not independently checked results. The next scientific obligation
is a group-sensitive ratio comparison with the actual Wilson
normalizers; local interpolation and a strong-coupling endpoint
do not supply it. No crux is closed.

## 1. What the original argument actually does

**READ.** Here `T` means [Tomboulis, 0707.2179v1](https://arxiv.org/pdf/0707.2179v1).
Page numbers are printed PDF pages. Set
\(f(U)=1+\sum_{j>0}d_jc_j\chi_j(U)\), with normalized Haar measure.
For Wilson SU(2), \(c_j=I_{2j+1}(\beta)/I_1(\beta)\), and
\(\beta=4/g^2\). Let \(Z^+=(Z+Z^-)/2\), where the minus sign denotes
one nontrivial center twist. This average, rather than \(Z^-\) alone,
is essential to the reflection-positivity argument.
In the bulk factors below, \(N_m\) counts coarse plaquettes;
the inconsistent use of lattice cardinality in the lower bound
is addressed separately in §2.4.

| Step and source | Reconstruction | Treatment in T |
|---|---|---|
| **READ**, (2.1)–(2.11), pp. 4–5 | Expand the positive Wilson plaquette weight in characters; normalize its trivial coefficient. Nonnegative Fourier coefficients give reflection positivity. | PROVED IN THE TEXT, with standard character identities used. |
| **READ**, II.1, (2.12)–(2.14), Appendix A §§1,3 | Obtain monotonicity of the periodic partition function in the nonnegative coefficients; claim a quantitative lower bound from removing crossing terms and keeping elementary cube contributions. | PROVED IN THE TEXT as presented; the plaquette-count normalization of the quantitative bound is false (§2.4). The reflection construction uses compatible dyadic tori. |
| **READ**, (2.18)–(2.22), pp. 7–8 | Put \(\widehat F_j=\int f^\zeta\chi_j/d_j\), \(\widehat c_j=\widehat F_j/\widehat F_0\), \(c'_j=\widehat c_j^{b^2r}\), \(F'_0=\widehat F_0^{b^2}\). This is a specified approximate transformation, not exact blocking of the measure. | PROVED IN THE TEXT for the integer convolution construction; arbitrary real powers require separate care. |
| **READ**, III.1, (3.1)–(3.4), (A.14)–(A.19) | With \(\zeta=b^{d-2}\), moving potentials gives \(Z_{m-1}\le (F^U_0)^{N_m}Z_m(c^U(r))\). The proof first takes \(r=1\), then increases coefficients by taking \(r\le1\). | PROVED IN THE TEXT on its admissible positive-weight, reflection-positive domain. |
| **READ**, III.2, (3.5)–(3.11), (A.11)–(A.13) | A proposed lower bound uses \(F^L_0=1\) and \(c^L_j=c_j^6\). The zero-coefficient lower endpoint suffices for interpolation. The alternative \(c_j^{b^2}\) is stated but its proof is omitted. | PROVED IN THE TEXT as presented for \(c^6\), but its cited quantitative proof has the defect in §2.4; SKETCHED for (3.10). Only the independently available zero endpoint is used here. |
| **READ**, (3.12)–(3.24), pp. 12–14 | Interpolate \(c^L\le\widetilde c(\alpha)\le c^U\), and use a bulk factor \((F^U_0)^{N_mh(\alpha,t)}\). Endpoint bounds and strict increase give a unique \(\alpha(t,r)\in(0,1)\) reproducing one partition function. | PROVED IN THE TEXT. This intermediate-value step is not the disputed final matching. |
| **READ**, (3.25)–(3.32), Appendix B | With \(A=(N_m\log F^U_0)^{-1}\partial_\alpha\log Z_m\), obtain \(\alpha_t=-h_t/(h_\alpha+A)\). Move \(r\) below one to keep \(\alpha\) away from one, and obtain local derivative bounds on suitable parameter intervals. | PROVED IN THE TEXT as local calculus; the unrestricted continuation use needs more than these bounds. |
| **READ**, (3.33)–(3.38), pp. 16–17 | Iterate the representation. In (3.38), the upper coefficients evolve on their own, independent of the chosen intermediate \(\alpha\)'s. | PROVED IN THE TEXT, conditional on each admissible step. |
| **READ**, (3.42)–(3.43), p. 19 and footnote 8 | If the upper coefficients enter a strong-coupling norm ball, so do the interpolated coefficients. T says ordinary MK reaches it by explicit evaluation, and says this persists under fixed small \(1-r\) for SU(2), unlike U(1). | The squeeze is PROVED IN THE TEXT. The all-coupling modified-flow and structural-stability claims are ASSERTED, not proved there. |
| **READ**, (4.1)–(4.8), (A.6)–(A.10), (A.23)–(A.25) | A center change of link variables moves a closed twist sheet. \(Z^-\le Z\); averaging the two sectors restores the reflection positivity needed in every direction. | PROVED IN THE TEXT. |
| **READ**, IV.2–IV.5, (4.9)–(4.19), Appendix A | Apply the bounds and interpolation to \(Z^+\), obtaining its own \(\alpha^+(t,r)\). The same coefficient endpoints can be used. | PROVED IN THE TEXT as presented; use the zero lower endpoint to avoid the inherited quantitative normalization defect. Geometry and admissibility conditions remain. |
| **READ**, (A.20)–(A.22), pp. 38–39 | Potential moving also gives a raw upper bound for \(Z^-\) at \(r=1\). Extending to \(r<1\) uses monotonicity of \(Z^+\), not an asserted monotonicity of \(Z^-\). | PROVED IN THE TEXT. |
| **READ**, (5.1)–(5.6), pp. 24–25 | Separate exact representations give an exact ratio with a residual bulk factor. \(\alpha^+-\alpha=O(N_m^{-1})\) on a controlled interval; this does not make that bulk factor tend to one. | PROVED IN THE TEXT locally; T explicitly warns against discarding the factor. |
| **READ**, (5.7)–(5.12) | Shift \(t\) separately in numerator and denominator to cancel the explicit bulk factors, leaving different coarse coefficients. Repeat while the upper coefficients flow. | SKETCHED as an iteration: local shifts follow under uniform derivative and range control; compatibility over the required run is not supplied. |
| **READ**, (5.14)–(5.20), Appendix C | At a late scale seek one \(t_*\) with \(\alpha(t_*)=\alpha^+(t_*)\). Invoke \(A\ge A^+\), (5.15), and continue a solution of \(\Psi(\lambda,t)=0\) from \(\lambda=0\) to one. | ASSERTED at the decisive global continuation in (C.8)–(C.10); the local implicit-function calculation does not prove it. |
| **READ**, p. 27, (5.15)–(5.16) | The derivative comparison is invoked only after entry into strong coupling, where T calls it an exercise in the convergent expansion. | SKETCHED; no written uniform expansion proof is given. It is not invoked at the original large \(\beta\). |
| **READ**, V.1–V.2, (5.17)–(5.24) | Once common matching exists, obtain the same-action coarse ratio and its one-sided bound \(Z^-_\Lambda/Z_\Lambda\ge Z^-_{\Lambda_n}(c^U_n)/Z_{\Lambda_n}(c^U_n)\). | PROVED IN THE TEXT as a conditional implication; its antecedent is unproved. |
| **READ**, II.2, (2.31)–(2.36), Appendix D | Once the coefficient norm is small enough, a displayed elementary recursion forces further decay. Appendix D extends the norm estimate to \(b^2r>2\). | PROVED IN THE TEXT. This proves stability of a strong-coupling region, not entry from arbitrary \(\beta\). |
| **READ**, (6.6)–(6.14), pp. 30–31 | In the logarithmic expansion, contractible clusters cancel between twisted and untwisted theories. Wrapping surfaces have minimum area \(L_1L_2/b^{2n}\). Convergence gives a vortex free energy with exponential area suppression. | Cancellation is PROVED IN THE TEXT; full convergence and exponentiation are SKETCHED with citations. |
| **READ**, (6.1)–(6.5), pp. 28–29 | Insert the claimed matching into the strong-coupling expansion, then use the Tomboulis–Yaffe inequality to infer a Wilson area law. | SKETCHED conditional on matching, flow and the cited inequality. The all-coupling conclusion is not established. |

**ARGUED.** After the elementary bounds and separate interpolants,
the modified all-coupling flow claim on p. 19 is unsupported. Even granting that
claim, the ratio argument has a second, logically independent gap in
Appendix C. Neither is repaired merely by knowing a strong-coupling seed.

**READ / ARGUED, the intended endpoint.** For a blocking depth
\(n=n(\beta)\) independent of the large box, the intended bound
from (6.6)–(6.14) is of the form
\[
 F_v(\Lambda;\beta)\le
 C\,\frac{L_3L_4}{b^{2n}}\,
     \exp\!\left(-\kappa\,\frac{L_1L_2}{b^{2n}}\right).
\]
The one-sided ratio comparison would transfer this coarse
strong-coupling estimate to the original model. Its constants
must be controlled on the coupling interval of an application.
The bound is a claimed fixed-lattice vortex conclusion; the
paper's later qualitative discussion of \(g(a)\to0\) is not
a construction of a continuum theory with a physical mass gap.

## 2. The criticisms and the reply

**READ.** [Ito–Seiler 0711.4930v1](https://arxiv.org/pdf/0711.4930v1),
pp. 5–9, Claim 2.1 and (3.2)–(3.11), simplify to \(r=1\) and a
one-step matching problem. They correctly identify common matching as
essential. They also say the derivative inequality must be proved at large
\(\beta\). This does not faithfully describe T's late-scale use of (5.15).

**ARGUED.** [Tomboulis's reply](https://arxiv.org/pdf/0712.2620v1),
pp. 3–6, (2.5)–(2.9), is adequate on that narrow point. T pp. 26–27
explicitly postpone (5.15) until the coarse coefficients are small.
The reply correctly objects that setting \(r=1\) removes a parameter his
construction uses. It gives no proof of the modified all-coupling flow,
and repeats the claim that (5.15) implies common matching. It therefore
does not answer the two actual missing obligations.

**READ.** [Ito–Seiler 0803.3019v1](https://arxiv.org/pdf/0803.3019v1),
§3.2, p. 12, list the separate shifts, common matching, and global
implicit-function continuation as Problems 1–3. Section 3.3, pp. 13–16,
explains the conflict between taking \(r<1\) and preserving flow to strong
coupling. Their Gaussian example is exact for a noncompact Gaussian map;
their SU(2) bifurcation is numerical evidence, not a proof under this lane's
rules. Their demand for a contraction is sufficient, not necessary:
compact continuation or a direct endpoint bracket could also suffice.

**READ.** [0901.4246v1](https://arxiv.org/pdf/0901.4246v1) is authored
by **Keiichi R. Ito and Erhard Seiler**, with Seiler the speaker. Pages 3–5,
(4.2)–(4.8), repeat the flow and continuation issues. The prose on p. 4
reverses the two numerical flow assignments relative to 0803.3019 p. 14;
no numerical claim is used here. The sign and endpoint arguments below
do not depend on those runs.

### 2.1 The continuation inference is false

**PROVED (following Kanazawa's counterexample, credited by Ito–Seiler).**
Take \(\Psi(\lambda,t)=e^{-t}-1+2\lambda\). It is smooth and
\(\Psi_t=-e^{-t}<0\) at every finite point. At \((0,0)\) it vanishes.
The unique zero for \(0\le\lambda<1/2\) is
\(t(\lambda)=-\log(1-2\lambda)\). It tends to infinity as
\(\lambda\uparrow1/2\); no finite real zero exists for
\(\lambda\ge1/2\). This refutes T's general continuation inference after
(C.8). It does **not** exhibit a counterexample to his particular SU(2)
matching equation. That equation remains OPEN.

**PROVED.** Write \(B=N\log F^U_0>0\),
\(\Phi=B^{-1}\log Z_c\), \(\Phi^+=B^{-1}\log Z_c^+\), and
\(k=B^{-1}\log Z_f,\ k^+=B^{-1}\log Z_f^+\).
For a fixed reference \(t_I\), the homotopy in Appendix C is
\[
 \Psi(\lambda,t)=h(\alpha(t),t)
 +(1-\lambda)\Phi^+(\alpha^+(t_I))
 +\lambda\Phi^+(\alpha(t))-k^+.
\]
The untwisted level equation is
\(h(\alpha(t),t)+\Phi(\alpha(t))=k\). Put
\(A=\Phi'\) and \(A^+=(\Phi^+)'\).
Thus at the disputed endpoint,
\[
 \Psi(1,t)=k-k^++\Phi^+(\alpha(t))-\Phi(\alpha(t)).
\]
Consequently \(\Psi(1,t)=0\) is exactly
\(Z_c^+(\alpha(t))/Z_c(\alpha(t))=Z_f^+/Z_f\).
Changing \(h\) can change which coefficient values the level curve
reaches. It does not establish that the fine ratio lies in the
attainable range of the coarse ratio.

**PROVED.** On the same level curve,
\[
 \Psi_t(\lambda,t)
 =h_t\,\frac{A-\lambda A^+}{h_\alpha+A}.
\]
The sign in (C.9) follows when \(A>A^+\). But nonvanishing is not a
lower bound on its magnitude. At \(\lambda=1\) the numerator contains
the small difference \(A-A^+\), which is precisely a twist response.
A local lower bound for \(\alpha_t\) does not bound this difference.
T supplies no compact region trapping the branch through \(\lambda=1\).

**PROVED.** A derivative bound \(\alpha_t\ge\eta>0\) cannot hold on
an unbounded interval while \(0<\alpha<1\): integration gives
\(\alpha(T)\ge\alpha(t_0)+\eta(T-t_0)\). The useful version is a
bound on a specified finite interval, with sufficient room for the required
shift. Ito–Seiler's broad objection to global bounds is right in this
sense; it does not invalidate an individual small shift in (5.7).

### 2.2 Flow: the criticism needs its qualifications

**READ.** Ito–Seiler 0803.3019, §3.3, p. 13, in the unnumbered
Gaussian iteration following their reference to (2.2a), obtain
\(f_n(\theta)=\exp[-\beta\theta^2/(2r^n)]\) for their Gaussian
version of the transformation. For \(r<1\) its width shrinks.
This is a rigorous calculation for that noncompact model, and a GUIDE
to the compact-group weak-coupling regime. Their plotted compact SU(2)
flows do not establish a counterexample theorem. T's p. 19
structural-stability assertion is therefore **OPEN for the stated
all-coupling fixed-parameter prescription**, rather than refuted here
by those plots. Ordinary MK convergence cannot simply be cited for a
different map.

**READ.** Kanazawa's [v3](https://arxiv.org/pdf/0805.2742v3),
Appendix A.1, pp. 10–14, distinguishes four issues: global continuation;
the modified flow; the location of the abelian/nonabelian distinction;
and whether \(r<1\) was necessary in the first place. His proposed
strict thermodynamic slack at \(r=1\) is a possibility, not a proved
replacement for T's volume-uniform estimates.

**READ, PROVED IN THE TEXT conditional on the cited convergence theorem.**
Kanazawa v3 Appendix A.2, Theorem 4, pp. 15–16, (40)–(48), supplies an
important positive result absent from v1 and v2. For each initial smooth
strictly positive weight on a compact **connected** Lie group, one may
choose a sufficiently large integer blocking factor \(b\) and
\(r=1-b^{-2}\) so that the modified map converges to the constant
weight. This includes both SU(2) **and U(1)**. It is not a fixed
\(b=2\), fixed-\(r<1\), all-initial-couplings result.

**READ.** The imported Müller–Schiemann functional obeys
\[
 \operatorname{osc}(-\log f)\le W[f]/2,\qquad
 W[Tf]\le(q/s)(1-e^{-W[f]})W[f],
 \quad Tf=(f^q)^{*s}/(f^q)^{*s}(1).
\]
Here \(q,s\) are integers, \(s\ge2\). Set \(q=b^2\),
\(s=b^2-1\), so \(q/s=1/r\). Choosing \(b^2>e^{W[f_0]}\)
gives \(\rho=(1-e^{-W[f_0]})/r<1\). The displayed estimate
then inductively gives \(W[f_n]\le\rho^nW[f_0]\), hence uniform
convergence to one. This is Kanazawa's argument, credited to him;
the underlying 1988 functional theorem was not independently read
or reproved in this task. Integer convolution also avoids an
unjustified assumption of positivity under fractional Fourier powers.

**PROVED, conditional normalization check.** For the positive
Fourier coefficients generated from the Wilson weight, normalize
the identity-normalized iterate \(f_n\) instead by Haar integral:
\(g_n=f_n/\int f_n\). Then
\(\sum_{j>0}d_j^2c_{j,n}=g_n(1)-1\).
Uniform convergence \(f_n\to1\) therefore forces this sum to
zero. Thus, subject to the cited functional theorem, this
flow reaches the coefficient-norm basin used in T; it gives
more than convergence of each fixed character coefficient.

**ARGUED.** This repairs one possible *choice of bounding flow*,
not the partition-function-ratio comparison. The choice must still
fit T's interpolation hypotheses, available lattice divisibility,
and uniformity on the coupling interval being used. It also shows
why the whole objection cannot be summarized as “MK cannot reach
strong coupling”: there is a mathematical way to make it do so
even for U(1). Something else must prevent the false conclusion
about the actual U(1) theory.

### 2.3 What survives in all three Kanazawa versions

**READ.** [v1](https://arxiv.org/pdf/0805.2742v1), Theorems 1 and 3,
pp. 3–4 and 6, (5), (32), already give an exact representation
with two slightly different coarse parameters. Its confinement
discussion, (15)–(17), requires an intersection of two bulk-factor
functions and does not prove the intersection.
[v2](https://arxiv.org/pdf/0805.2742v2), §2, pp. 4–5,
(14)–(19), makes the residual extensive error explicit.
V3 retains this discussion and adds the critical appendix and
Theorem 4. No version supplies common matching.

**READ.** V3 Theorem 1, (5), treats SU(N) and U(N), a finite
subgroup \(H\) of the center, and a positive combination
\(\mathcal Z=\sum_{g\in H}A_g Z^g\). For sufficiently large
volume, a small prescribed coarse coefficient family can represent
\[
 \frac{\mathcal Z_f}{Z_f}
   =\frac{\mathcal Z_c(\alpha c')}
           {Z_c(\alpha_\Lambda c')},
 \qquad |\alpha_\Lambda-\alpha|\le C/|\Lambda_c|.
\]
This is a finite-volume theorem with a mismatched denominator,
not an exact renormalization-group map preserving the ratio
at one coarse action. His proof uses small-coefficient analyticity
and pressure derivatives; it is not an all-temperature expansion
in the original bare coupling.

**PROVED (the error mechanism already identified by Kanazawa).**
For \(p_N(u)=N^{-1}\log Z_c(u)\) and
\(\alpha_N=\alpha+\gamma_N/N\), the mean-value theorem gives
\[
 \log\frac{Z_c(\alpha)}{Z_c(\alpha_N)}
       =-\gamma_N p_N'(\xi_N).
\]
Thus an \(O(N^{-1})\) mismatch generically leaves an \(O(1)\)
logarithmic ratio error. If \(\gamma_N\to\gamma\) and the pressure
derivatives converge near \(\alpha\), its limit is
\(-\gamma p'(\alpha)\). No asymptotic equality of the ratios follows
from equality of limiting bulk free energies. T recognizes this
problem in (5.6); his attempted repair, not the warning, fails.

**ARGUED.** For the lane's area-small vortex target, even an
uncontrolled \(o(1)\) residual would be insufficient. A usable
approximate matching theorem would need an error on the same
scale as the required twist deficit. Kanazawa's exact mismatched
formula usefully isolates the missing information in a scalar
function, but does not bound that information.

### 2.4 An additional normalization defect in the printed lower bound

**READ.** T (2.13), (A.4)–(A.5), pp. 5, 35–36, uses
\[
 Z_\Lambda(c)\ge(1+\sum_{j>0}d_j^2c_j^6)^{|\Lambda|},
\]
and Appendix A §3 explicitly takes \(|\Lambda|\) to count
plaquettes. The PDF, not merely its extracted text, says after
(A.5) that there are more bonds than plaquettes. In four dimensions
there are \(4V\) bonds and \(6V\) plaquettes on a periodic lattice
with \(V\) sites. That stated counting justification is false.

**PROVED, counterexample to the plaquette-count normalization.**
Take a periodic torus with each side at least eight and the
positive SU(2) weight \(f=1+2c\chi_{1/2}\), \(0<c<1/4\).
In its finite polynomial partition function, a nonempty contribution
must have an even number of incident selected plaquettes at every
link: multiplication of that link by the center element changes
the sign otherwise. The smallest such surfaces have six plaquettes
and are elementary cube boundaries. Each has weight \(4c^6\),
by character orthogonality (the sphere contributes
\(d^{\,\#F-\#E+\#V}=d^2\), with \(d=2\)).
There are \(\binom43 V=4V\) elementary cubes. Equivalently this is
the leading coefficient counted in Kanazawa v3 (12), with
\(a_4=2/3\) per plaquette. Consequently
\[
 Z_\Lambda=1+16V c^6+O(c^7),\qquad
 (1+4c^6)^{6V}=1+24V c^6+O(c^{12}).
\]
For sufficiently small positive \(c\), the printed lower bound
with exponent \(6V\) is false. This finite expansion is an analytic
coefficient comparison, not an enumeration or numerical test.

**ARGUED.** This defect is distinct from the global matching gap.
It does not disprove every lower decimation bound: a weaker,
correctly counted lower bound may suffice, and the endpoint
\(c^L=0,\ F_0^L=1\) follows from monotonicity and \(Z(0)=1\).
That trivial lower endpoint is sufficient for the separate
intermediate-value constructions. I therefore salvage that
endpoint, not the uncorrected numerical strength of (2.13)/(4.10)
or its printed proof of the \(c^6\) choice. The source labels in
the reconstruction table describe a presented proof, not acceptance
of this erroneous normalization.

## 3. Where the group enters, and the comparison-model tests

**READ / ARGUED.** The following comparison separates group algebra from
the unproved physical comparison. It does not infer a mass gap from
a Wilson-loop law.

| Step | SU(2) versus U(1) and finite groups |
|---|---|
| Haar integration, character expansion, convolution | **READ**, T §2; Kanazawa v3 §§2–3. These have compact-group counterparts. Character dimensions and fusion rules change; positivity is not unique to SU(2). |
| Movable center sheet and positive sector average | **READ**, T §4 and Appendix A.2. U(1) contains the two-element subgroup \(\{1,-1\}\); Z₂ has exactly this center operation. The same projection construction is available. A finite subgroup needs the relevant nontrivial center element for this particular test. |
| Convex upper bound, trivial lower bound, separate interpolation | **ARGUED**, from the displayed proofs. These use positivity, reflection/translation symmetry and calculus, not a distinction between SU(2) and U(1). Domain and geometry restrictions still matter. The erroneous plaquette normalization in §2.4 is not needed. |
| Flow into the small-coefficient region | **READ**, Kanazawa v3 Theorem 4. Connectedness matters: the theorem includes U(1), excludes finite groups, and allows a sufficiently large \(b\) chosen from the initial weight. T's fixed-\(r\) structural-stability distinction is unproved. |
| Late strong-coupling expansion | **READ**, T §6; Ito–Seiler 0803.3019 Theorem 2.2(1). Small-coefficient confinement occurs for abelian as well as nonabelian groups. This is not the missing distinction. |
| Same-action ratio comparison through all scales | **OPEN** for SU(2), T V.1/(5.17), and its useful one-sided consequence V.2/(5.23). This is the first asserted *physical comparison* that cannot be universal once an admissible flow to strong coupling has been supplied for U(1). |

**ARGUED, precise U(1) conclusion.** Grant a bounding flow that really
reaches the small-coefficient region. If the full matching construction
also applied to U(1) at large \(\beta\), it would pass the small-coefficient
vortex estimate to that theory and yield an area law in the boundary/state
class to which the comparison applies. This conflicts with the abelian
Coulomb-phase result. The false logical inference in T is already
identified without using that result: nonzero \(\Psi_t\) does not imply
global continuation. The *SU(2) matching statement* is not thereby
disproved. A correct SU(2) proof must supply a group-sensitive global
ratio bracket/continuation estimate, or a comparably substantive
group-sensitive compatibility condition elsewhere in the iteration.
Merely distinguishing the coefficients of the two groups is insufficient.

**READ, boundary qualification.** Ito–Seiler 0803.3019, pp. 6–7,
Theorem 2.2(2), state for U(1) at large \(\beta\) a periodic-twist
bound
\[
 \lim_{L_3L_4\to\infty}F_v/(L_3L_4)
       \ge c/(L_1L_2),
\]
incompatible with the claimed area-exponential upper bound. They
attribute the adaptation to their reference [13], an in-preparation
preprint, rather than prove it there. I record this as a READ
statement, not a newly checked torus theorem.
The lane's row-784 source, section 0 and table row 3, correctly
distinguishes the established Villain infinite-volume area-law
countertest from the unproved bridge to its periodic thermal seed.
The Wilson-weight extension is not silently substituted for the
Villain theorem, and no numerical transition coupling is used.
If one insists on literal T with fixed \(b,r<1\), even its flow
can fail before matching; there is no justified claim that every
earlier hypothesis holds for U(1). The location above concerns
the proposed transfer of a *valid* bounding flow to the exact theory.

### 3.1 A hand check: finite groups do not share the connected-group flow

**PROVED.** For Z₂ write \(f(u)=1+cu\), \(c=\tanh\beta\), and
put \(q=b^2\), \(s=b^2r\ge1\). The four-dimensional recursion is
\[
 c'=\{\tanh(q\,\operatorname{atanh}c)\}^{s}.
\]
For \(c=1-\delta\), \(0<\delta\le1\),
\[
 1-\widehat c
 =\frac{2\delta^q}{(2-\delta)^q+\delta^q}
 \le2\delta^q,\qquad
 1-c'\le s(1-\widehat c)\le2s\delta^q.
\]
The middle inequality follows from the mean-value bound for \(x^s\)
on \([0,1]\). Choose a positive \(\delta_0\) with
\(2s\delta_0^{q-1}\le1/2\). Then \(0<\delta\le\delta_0\)
implies \(1-c'\le\delta/2\); iteration gives \(c_n\to1\),
not zero. This includes ordinary MK (\(r=1\)).
Thus applying the purported all-coupling strong-flow step to Z₂
would already be false. It is not a counterexample to Kanazawa's
connected-group theorem.

**PROVED, extension to a finite subgroup.** Normalize a positive
weight on a finite group \(G\) by \(f(1)=1\), and assume
\(\max_{g\ne1}f(g)\le\epsilon<1\). Raising it to an integer
\(q>1\) and normalizing to a probability measure leaves
off-identity mass at most \(K\epsilon^q\), \(K=|G|-1\).
After \(s\) independent convolution factors, the probability of
a nonidentity product is at most \(sK\epsilon^q\), since at
least one factor must be nonidentity. Dividing the resulting
weight by its value at identity gives
\[
 \epsilon'\le\frac{sK\epsilon^q}{1-sK\epsilon^q}.
\]
For small enough \(\epsilon\), this is at most \(\epsilon/2\).
The SU(2) fundamental Wilson weight restricted to any finite
subgroup has a unique maximum at identity; its normalized
off-identity maximum tends to zero as \(\beta\to\infty\).
It therefore enters this weak-coupling basin for every fixed
integer \(q>1,s\). The argument concerns the approximate map,
not a proof of the finite group's phase diagram.

**ARGUED.** The useful distinctions are consequently separate.
Connectedness defeats this finite-group concentration mechanism
but does not distinguish U(1). Noncommutativity distinguishes
the commutator average from U(1), but does not exclude finite
nonabelian subgroups. The lane's (LC) combines small continuous
deformations with noncommuting generators; it passes both
algebraic tests. None of these algebraic facts alone is the
missing Wilson-measure inequality.

## 4. Later continuations: an attempted repair, not just silence

**READ.** [Tomboulis 0710.1894v1](https://arxiv.org/pdf/0710.1894v1),
pp. 4–7, (2.14)–(2.16), (4.3)–(4.5), is a conference summary.
It repeats separate interpolation, common matching and the flow
claim without a new matching proof.

**READ.** [Tomboulis, PoS Confinement8 (2008) 020](https://pos.sissa.it/077/020/pdf),
pp. 6–8, contains a material change. Equations (4.5)–(4.6) propose
the adaptive choice \(r_m=1-\varepsilon/(1+\beta_{\rm eff}(m-1))\).
On p. 7 the proposed endpoint bracket is supported by numerical
string-tension comparisons. That is GUIDE here. On p. 8,
(4.9)–(4.11), he replaces the one-variable continuation with
a two-variable monotone iteration attributed to G. Meyer:
\[
 x=(t,\alpha),\qquad
 x_k'=-(I+\lambda F_x(x_k))^{-1}F(x_k).
\]
He requires \(F(x_0)<0\), entrywise nonnegativity of the inverse,
and a bounded invariant domain with a suitable boundary sign.
He then asserts that the hypotheses hold for sufficiently late
blocking and an appropriate \(h\). No domain, boundary estimates
or proof of that assertion is supplied. Thus the application
is **ASSERTED**, even though its stated aim addresses the
global-continuation problem.

**PROVED, a problem with the displayed residuals.** Read (4.9)
in its printed order, with \(f_2\) the untwisted residual and
coordinates \(x_1=t,x_2=\alpha\), as specified on p. 8.
Correcting the apparent missing logarithm on the bulk factor
only for this check, it has the form
\[
 f_2(t,\alpha)
   =-\log\widetilde F_0(t,\alpha)
      -N^{-1}\log Z_c(\alpha)+\text{constant}.
\]
The coarse coefficients have no explicit \(t\) dependence.
For the parametrizations used in the paper,
\(h_t<0\) and \(F_0^U>1\), so
\(u=\partial_t f_2=-(\log F_0^U)h_t>0\).
At any fixed interior point,
\[
 [(I+\lambda F_x)^{-1}]_{21}
       =-\lambda u/\det(I+\lambda F_x)<0
\]
for all sufficiently small positive \(\lambda\), because the
determinant tends to one. This contradicts condition (ii)
as printed. Reading the bulk term literally as
\(-\widetilde F_0\) gives the same sign. Different residual
signs or a different order cone might permit another construction;
they would need a new verification and a genuine trapping domain.
This is a countercheck of the presented repair, not a theorem
that the actual simultaneous equations have no solution.

**READ / ARGUED.** The same proceedings paper, p. 9, says
that its adaptive flow (4.5) reaches a weak-coupling U(1)
fixed point; it gives no analytic proof of that distinction.
Its mass-gap discussion, (4.15)–(4.16), concerns Wilson-line
correlators and vanishing center magnetization. It supplies
no estimate of the lane's full thermal sum or of all
neutral physical excitations. The discussion of a coarse
center theory also depends on the unproved exact representation.

**READ, access limit.** The INSPIRE citation list also identifies
Tomboulis, *Long distance dynamics and confinement via RG decimations*,
Mod. Phys. Lett. A **24** (2009), 2717–2730,
[DOI 10.1142/S0217732309032307](https://doi.org/10.1142/S0217732309032307).
Its metadata and first-page preview were available; its body was
not read. The publisher request returned 403, and the specified
local paper folder is absent on this machine. I did not bypass
the refusal. Therefore this note does not claim to have ruled
out a repair inside that unread article.

**READ.** [Ogilvie 1010.1942v1](https://arxiv.org/pdf/1010.1942v1),
§IV, pp. 12–15, discusses both 2008 and 2009 continuations and
still describes the construction as lacking a complete
demonstration or implementation. His U(1) discussion distinguishes
an extremely slow approximate flow from a true fixed point.
It is a contemporaneous assessment, not a substitute for reading
the unavailable article.

**READ.** Cheng–Tomboulis
[1206.3816v1](https://arxiv.org/pdf/1206.3816v1), pp. 2, 7,
and [1211.5845v1](https://arxiv.org/pdf/1211.5845v1), p. 2,
develop practical two-lattice matching of approximate decimations.
They calibrate using Monte Carlo data and compare critical
couplings/string tensions. They do not present those calculations
as a proof of the exact common-parameter statement. They supply
GUIDE only under the present no-computer-discharge rule.

**READ, screened rather than adopted.** Grady
[1210.1794v1](https://arxiv.org/pdf/1210.1794v1), pp. 1–3,
and [v2](https://arxiv.org/pdf/1210.1794v2), pp. 1–2,
cite Tomboulis and pursue an opposing long-range-order claim via
an anisotropic theory and Coulomb gauge. The revised title says
“Toward a proof.” This is not a repair or a new analysis of
T's matching equations. Its separate argument was not validated
here, and its claimed nonconfinement is not used.

**READ, search boundary.** INSPIRE record 755847 returned 18
citing records, all inventoried. Searches on arXiv by original
identifier, author, decimation, matching and confinement found
the continuations above. A 2026 title hit,
[Schierholz, EPJC 86, 646](https://link.springer.com/article/10.1140/epjc/s10052-026-15857-z),
§§1–2, concerns gradient flow and a gluon condensate, not a repair
of T's interpolation. Other citing records concern numerical
density-of-states methods, entanglement, center vortices, or
different theories; no matching proof was inferred from their
citations. This is a bounded search as of 2026-11-12, not evidence
that no later repair exists anywhere.

## 5. Salvage for this lane

### 5.1 Fix the consumer before importing a theorem

**READ.** [gap-ext-astra.md](gap-ext-astra.md), §1, (E1)–(E2),
uses periodic shapes \((a,a,c,d)\), \(a\ge3\),
\(c,d\in\{a,2a\}\), and
\[
 R_m(v)=\frac{Z_{m+v}}{Z_m}
       =\mathbb E_{\mu_m}e^{-X_\Sigma^m},\qquad
 F_m(v)=-\log R_m(v).
\]
For the designated \((0,v_{34})\) pair this is precisely the
weighted exterior mean in (26), with its original normalizer.
The identity itself is proved in the lane; its small-deficit
estimate is the open issue. (V) requires all specified twist
free energies to be bounded by \(Ca^p e^{-\sigma a^2}\),
uniformly on a fixed compact coupling interval \(I\).

**READ.** [gap-trf-astra.md](gap-trf-astra.md), §1, (T1)–(T2),
retains the weaker consumer
\[
 Q_F=\max_{m_2=0,\ i=3,4}\frac{1-R_m(v_{1i})}{2},
 \quad 8Q_F\le K(a)\sqrt{S_{\rm ev}},
 \quad Q_F<1/192,\quad K(a)\le C_1a^{p_1}.
\]
It does not demand an area exponent. The witness
\(S_{\rm ev}\ge\eta_*^a\) makes a bound with scale
\(\min\{1/96,K(a)\eta_*^{a/2}/4\}\) on the full transport
cost sufficient.
An approximate decimation error must be compared to the consumer
actually chosen, not merely shown to vanish per unit volume.

### 5.2 Inventory of reusable steps and their limits

**READ / ARGUED.** This is an inventory of the mathematical
ingredients in the proposed argument, not a grant of repository
status. “Conditional” means the displayed antecedents still
have to be established in the actual application.

| Reusable statement | Precise scope / evidence | Use for (V), (26), (FQ) |
|---|---|---|
| Positive character expansion; integer multiplication and convolution preserve the required positivity | T (2.2)–(2.9), (2.18)–(2.28); positive weights, normalized Haar measure, integer convolution. A fractional coefficient power is not automatically a positive density. | Supplies admissible auxiliary actions. Does not compare twist normalizers. |
| Movability of a closed center sheet; \(0<Z^-\le Z\); \(Z^+\) reflection positivity | T (4.2), IV.1–IV.2, (A.6)–(A.10), (A.23)–(A.25), for the stated single twist and reflection geometry. | Exact sign/cohomology facts; useful prerequisites. The bound \(R\le1\) is the opposite endpoint from the needed \(R\approx1\). |
| Coefficient monotonicity of \(Z\) and \(Z^+\), and the trivial lower endpoint \(Z,Z^+\ge1\) | T (2.12), (4.9), with the reflection-positive construction. Do not use the erroneous plaquette-count strength of (2.13)/(4.10). | Permits a sound lower endpoint for separate interpolation; no ratio estimate. |
| Potential-moving upper partition-function bound | T III.1, IV.3, (A.14)–(A.22). At \(r=1\) the convexity proof includes a raw single-twist bound. At \(r<1\), the coefficient-monotonicity extension is for \(Z,Z^+\). | A rigorous control of individual extensive free energies. Dividing two upper bounds is not a bound on their ratio. |
| Separate exact interpolants and local derivatives | T (3.24)–(3.29), IV.5; calculus on a positive admissible path, with its endpoint bracket and finite parameter interval. | Can represent \(Z\) and \(Z^+\) individually. Does not provide one common \(\alpha\) or a global trapping interval. |
| Exact mismatched-ratio representation | Kanazawa v3 Theorems 1 and 3, (5), (38); small prescribed coarse coefficients, sufficiently large volume, numerator and denominator parameters differing by \(O(1/N)\). | The most useful diagnostic salvage: it locates the unresolved twist information instead of losing it in bulk normalization. Alone it proves none of the three consumers. |
| Small-norm basin for the coefficient recursion | T II.2, Appendix D. With \(x=\sum d_j^2c_j\), \(p=b^2r>2\), the estimate has the form \(x'\le(\zeta x)^p(1+x)^{(\zeta-1)p}\). | Once a sufficiently small endpoint is reached, subsequent upper coefficients remain controlled. It says nothing about the exact fine-theory ratio. |
| A convergent connected-group bounding flow with sufficiently large \(b\) | Kanazawa v3 Theorem 4, conditional on the cited Müller–Schiemann functional theorem; see §2.2. | Removes one possible flow obstruction but still works for U(1). No SU(2) confinement follows without the comparison. |
| Wrapping-cluster cancellation and small-coefficient vortex estimate | T (6.6)–(6.14); the full convergence theorem is imported, not proved in detail there. Contractible terms cancel and wrapping supports cost the transverse area. | A suitable coarse endpoint for a **proved** ratio comparison, including appropriate uniformity. It is not a comparison between fine and coarse theories. |
| V.2 as an implication from common matching and a controlled derivative sign | T (5.17)–(5.24). At a shared coefficient path, the derivative of the ratio is the difference of the logarithmic derivatives. | A one-sided ratio bound is already enough for (V); exact equality is stronger than necessary. The antecedent is the open crux, not a salvaged unconditional theorem. |
| Vortex-to-Wilson-loop inequality | Kanazawa v3 Theorem 2, (20), quotes the proof in its reference [17]; Ogilvie (24) agrees. For normalized fundamental SU(2), the safe stated form is \(\lvert\langle W(C)\rangle\rvert\le2[(1-R)/2]^{A_C/(L_\mu L_\nu)}\), where \(A_C\) is the minimal enclosed area. | Converts a vortex bound into an area law. It cannot upper-bound \(1-R\) from an upper bound on a different loop observable. |

**ARGUED, normalization caution.** T (6.4) prints no leading
factor two and describes a spin-\(1/2\) character observable.
The lane's earlier gap-skeleton-max §2.3 copied that convention.
For a new application use the explicit normalized-loop form
above; do not silently equate the two formulas. This issue
does not repair matching, and no argument here depends on
optimizing that prefactor.

### 5.3 Do the bounds cover our twisted boxes?

**READ.** T Appendix A §1 actually takes side lengths
\(2^{m_\mu}\); the source PDF confirms the exponent.
A blocking step also requires compatible side lengths.
Thus dyadic instances of \((a,a,c,d)\) with sufficient room
for the requested blockings fit its geometry. A statement
for every integer \(a\ge3\), or for an arbitrary \(b\) selected
by Kanazawa's theorem, needs a compatible geometry argument;
it does not follow by suppressing the divisibility condition.

**ARGUED.** For a compatible torus with background \(m=0\)
and one temporal center twist, the upper bounds and
\(Z^+=(Z+Z^v)/2\) construction are useful exactly as stated.
For the lane's crossed magnetic backgrounds, the required
object is \((Z^m+Z^{m+v})/2\) relative to \(Z^m\), not
\((Z^0+Z^v)/2\) relative to \(Z^0\).
The proof restoring reflection positivity for one sheet does
not establish all-direction reflection positivity with the
other magnetic sheets left fixed. The lane already exhibits
a negative fundamental eigenvalue for a temporal-twist
crossing kernel: gap-ext-astra §3.2, (E10).
An average over additional center sectors changes the object.
An extension covering those fixed-background pairs remains
**OPEN**, rather than disproved by this observation.

**ARGUED.** Conditioning on exterior links also destroys the
translation symmetry used in the potential-moving proof unless
that boundary data is transformed and accounted for. Neither
an individual partition-function upper bound nor a bound on
each normalized conditional law supplies the common
\(B_0\,d\xi/Z^0\) weight required by (26).
Even the single-twist, compatible-torus bounds therefore
do not discharge the lane's exact weighted mean.

### 5.4 Can the checked \(\beta<2/9\) seed be the endpoint?

**READ.** [gap-vmf-lip.md](gap-vmf-lip.md), §§3–4, (14)–(21),
proves a background-uniform layer comparison for
\(\beta<2/3\), and a full Wilson thermal seed for
\(0<\beta<2/9\). The latter uses \(q=9\beta/2<1\) and,
for sufficiently large \(a\),
\[
 S(a;(2a)^3;\beta)<1/1650,\qquad
 m(L^3;\beta)\ge3/(50a)\quad(L\ge64a).
\]
It includes the nonzero electric sectors.
[The row-790 check](gap-vmf-lip-check-opus.md), §§6–8,
accepts these statements with the inherited transfer/shape
inputs; its one wording correction concerns a single
transverse coordinate in the vMF variance. Those accepted
proofs are reused, not redone.

**ARGUED.** This is a valid endpoint for a comparison that
actually lands on the Wilson family at such a coupling.
T's map instead produces
\(1+\sum_j d_jc_j\chi_j\), usually with infinitely many
effective couplings in its logarithm. A small leading
coefficient, or an effective curvature named
\(\beta_{\rm eff}\), does not identify that action with
\(\exp(\beta\chi_{1/2}/2)\) at \(\beta<2/9\).
The source's strong-coupling cluster expansion is naturally
adapted to this multi-character endpoint; the lane's explicit
Wilson threshold cannot simply replace its hypotheses.

**OPEN / GUIDE.** To use the checked seed after this decimation,
one would need either an exact/comparison landing on that
Wilson family, or a proved small-interaction extension of the
single-link influence bounds and the required transfer/shape
comparisons to the resulting action. Neither is supplied here.
Moreover a scalar thermal seed and an area-small all-twist
free energy are different outputs. The seed does not itself
prove T's claimed exact ratio identity, nor does this method
give a cutoff-uniform physical gap.

### 5.5 Do (LC), Theorem R, or commutator averaging fill the gap?

**READ.** Theorem R in gap-ext-astra §3.3, (E11)–(E12),
controls a four-element light subgroup **given** small spectral
quantities \(S,\Delta\), with
\(\theta=1-e^{-\Delta}(1+S)^{-2}\).
A lower bound \(Z^{v_{34}}/Z^0>64\theta\), under the stated
small-\(\theta\) hypotheses, would select the magnetic
alternative. It does not establish those hypotheses or
the needed twist estimate. The theorem is a conditional
sector-selection tool, not an unconditional SU(2)-specific
replacement for (5.17). Invoking the desired small twist
deficit to select the subgroup, then using that selection
as its proof, would be circular.

**READ.** (LC), gap-ext-astra §4.2, constructs exact small
commutators \(C_N=[A_N,B_N]=e^{i\pi\sigma_3/N}\) with
\(C_N^N=-1\), generator trace deficits \(O(N^{-1})\),
and \(N(1-\operatorname{tr}C_N/2)=O(N^{-1})\).
It fails algebraically for U(1) and for every fixed finite
subgroup. It is a **GUIDE** to what an SU(2)-specific
comparison could use.

**READ / ARGUED.** The same source §4.3, (E18)–(E20), already
shows that independent conjugated small increments do not
produce the needed mixing. Its §5 and the later
gap-trf-astra §3, (T7), retain the full action/information
cost
\[
 \mathcal C
  =\sum_j\pi_j\mathbb E_{\mu_m}
       [S_{m+v}(T_jU)-S_m(U)]-I_\pi
  =F_m(v)+D\!\left(\sum_j\pi_j(T_j)_*\mu_m
                    \,\middle\|\,\mu_{m+v}\right).
\]
For its specified small-displacement families, (T7) gives
an area-sized lower bound on this cost; Corollary 4 covers
bounded-word use of LC with word length divided by \(\sqrt N\)
tending to zero. It does not exclude all correlated maps.
These already-written results block the inexpensive
“spread the flux and ignore the rest of the action” repair.
No LC family satisfying (TR-F) is constructed here.

**READ.** [gap-vortex-astra.md](gap-vortex-astra.md), §§4–7,
(5)–(15), proves the commutator convolution norm \(1/4\)
on center-odd SU(2) functions, its conditional finite-\(\beta\)
version, and the explicit product-word bound. Its (12)–(13)
even permits arbitrary nonnegative endpoint data **with a
common exterior weight**. Its own (15) identifies the
missing factors \(C_k(\xi)\prod_xz_{k,x}(\xi)\) in exact
Wilson integration. The proposed common factorization (CF)
is not proved.

**ARGUED, using the checked scope.** The commutator word is
invariant under every link-center change, not merely closed
ones; the row-780 check corrects this wording. Its exponent
counts independent factors rather than a forced minimal
electric surface. U(1) fails its strict commutator contraction,
but the finite quaternion group shares the center-odd
representation contraction. The row-780 finite-group phase
claim is explicitly ARGUED, not used here as a torus theorem.
In any event, the exact normalization identity (15) already
blocks inference of (V). Adding T's separate interpolation
formulas cannot remove those unknown factors. A theorem
identifying the actual flux ratio with the contracted object,
with all normalizers retained, is still **OPEN**.

**GUIDE, the useful reduced task.** A repair need not reproduce
T's exact equality. A uniform one-sided estimate
\[
 R_{\rm fine}\ge R_{\rm coarse}-\varepsilon_a
\]
with a controlled small-coefficient coarse action and an
error of the appropriate (V) or (FQ) scale would suffice,
after verifying the required background pairs and geometries.
This is the content to seek in a Wilson-measure use of LC
or the common-factorization route. It is not furnished by
separate upper/lower bounds, small coefficient mismatches,
or the local implicit-function theorem.

**PROVED, conditional error budget.** If
\(R_{\rm coarse}\ge1-\delta_a\) and
\(\delta_a+\varepsilon_a\le1/2\), the proposed one-sided
comparison gives
\(F_{\rm fine}\le2(\delta_a+\varepsilon_a)\).
This follows by integrating \(1/(1-x)\le2\) for
\(0\le x\le1/2\). It makes explicit why an unbounded
bulk-normalizer error cannot be discarded.

## 6. Source record, prior credit, and remaining limits

**READ, repository revisions.** Main was read at
bb4ec020d5ada57c630dd89acc98a68397ade423; PRs 10114, 10133,
10134 and 10141 at f76f6c649cff7dffbab664d8976e680e8f287fe9,
89faef229ff6e6bde42baad15ed8270c2f4087d8,
1e70c7211a2cdbc39001e619f1dd89db45e25851, and
fb99b4dddc7254e6124ac124887d58eeb3a77802.
The target-name search outside this lane found the following
relevant passages under
.claude/science/toe-ruleset-20261021/agents/ym4d-proof/
on PRs 10114 and 10133; their file blobs agree across those
two heads, so one copy was read:

- **READ**, checks/review_massgap_block_literature.md,
  lines 112–121: the full reading of Ito–Seiler 0901.4246
  already separates flow from common matching and warns
  against local-to-global continuation. This is the closest
  prior diagnosis, but explicitly does not examine the
  original Tomboulis construction.
- **READ**, REVIEW_S2.md, lines 112–121: a finite
  Migdal–Kadanoff toy does not test locality, large-field
  regions or the four-dimensional interface. No numerical
  result from it is used.
- **READ**, PROOF.md, lines 5755–5773: the corresponding
  toy is an approximate four-dimensional map; an exact
  hierarchical interpretation is not established there.
  It supplies neither the missing ratio theorem nor a
  duplicate of the present reading.

**READ, lane precedents.** Credit and scope of the four
specifically requested predecessors:

- [prior/gap-lit-grok-paths.md](prior/gap-lit-grok-paths.md),
  D.2, lines 355–378, records the controversy from abstract
  and excerpt reading. Its broad statement about no later
  repairs is replaced here by the bounded search and explicit
  unread-2009 limitation; the 2008 attempted repair matters.
- [gap-skeleton-max.md](gap-skeleton-max.md), §2.3,
  lines 355–361 within the requested 336–361 range, locates
  the missing passage from partition functions to the ratio.
  Its quoted TY prefactor needs the convention caution in §5.2.
- [gap-crux-fp.md](gap-crux-fp.md), table line 234
  (read with lines 218–242), gives the same warning in brief.
  “The inequality is only proved at strong coupling” does
  not by itself explain the failure: T deliberately postpones
  that inequality; global matching and the bounding flow
  are separate obligations.
- [gap-u1-audit-opus.md](gap-u1-audit-opus.md),
  §0 and table row 3, supplies the boundary/observable
  qualification retained in §3. No audit verdict is changed
  or applied by this research note.

**READ, Sussman–Alpoge source scope.** The README, neighbouring
rows in chunk-01 (58–74), chunk-29 (68–80), and obligations
(18–30, 1493–1501) were read before outline lines 581–602
and 31860–31885. Those passages explicitly separate spectral
support away from zero from existence/clustering; clustering
alone is not a mass-gap theorem. Searches of the outline
index and the CA-I 4.12–4.19 index found no entry for
Tomboulis, Migdal–Kadanoff or Kanazawa supplying this target.
No claim of absence from every line of CA-I is made, and
no unindexed CA-I proof is imported. Credit again Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. No Balaban estimate is used.

**READ, version coverage.** ArXiv histories list only v1
for 0707.2179, 0711.4930, 0712.2620, 0803.3019 and
0901.4246. Those PDFs were read in full: respectively
48, 10, 6, 18 and 5 PDF pages. All three versions of
0805.2742 were read in full: 7, 8 and 19 pages.
Later-source reading ranges are stated in §4; they are
not represented as full readings of every later paper.
The PoS 2008 argument was read through its conclusion,
with the formulas on pp. 7–8 also checked visually.
T Appendix A p. 35 was likewise checked visually.
No downloaded source was executed.

**READ, local evidence record.** The scratch directory contains
the once-fetched PDFs and two pinned SA TeX sources, their
text extractions, rendered formula pages,
inspire-record.json, inspire-citations.json,
repo-source-refs.json, and download-manifest.json
(file sizes and SHA-256 hashes).
The manuscript is the only checkout file created.
No simulations, numerical coefficient iterations or
computer-assisted proof certificates were used.

**OPEN.** Neither the original nor the later argument read
here supplies a valid global same-action ratio comparison
for the lane's full set of twisted boxes. The unread
2009 article remains a literature-access limitation.
The mathematical open obligations are (26)'s weighted
estimate, (V), and order-one (FQ); the new hand diagnoses
in this note require checking, and establish no physical
mass gap or continuum identification.

RESULT: OPEN — the decisive failure is the inference of global common-parameter matching from local continuation, T Appendix C (C.8)–(C.10) to V.1/(5.17), with an additional unproved modified-flow assertion and a failed sign condition in the 2008 attempted repair; the most useful salvage is Kanazawa's exact mismatched-ratio representation, supported by partition-function bounds and a convergent connected-group bounding flow, which isolates rather than removes the missing twist-normalizer comparison.
