# PRE-STATED

Recorded before opening `TQ55.md` or its check implementation. The user has
already supplied the eight claims to challenge; that prior exposure is explicit.
This is an independent mathematical review, not a retained-status audit.
No git commands. The only authorized write is this file. All computational
checks will use exact arithmetic; literature recollections, if used, receive
the marker `[m]` and cannot substitute for a checked theorem.

Let `L = .claude/science/toe-ruleset-20261021/agents/ym4d-proof`.
Verdicts are `CONFIRMED`, `NOT-VERIFIED`, or `REFUTED`, with a source file and
locating string for every substantive disposition. Conditional mathematics is
not a verification of its hypotheses for the Wilson measure.

Acceptance and falsification criteria, fixed in advance:

1. Recover the precise order of continuum, volume, and shell limits defining
   the Wilson-only charge. Check every dependency in its radius-independence
   argument, including contact terms, stress symmetry, observable convergence,
   and coupling normalization. A decay criterion must control actual lattice
   samples, with the required quantifiers, rather than assume continuum
   Riemann convergence from a pointwise bound.
2. Derive the proposed rotlet's divergence and symmetry independently, then
   compute its angular flux and Fourier singularity exactly. Track the origin
   as a distribution and distinguish a tensor witness from a realizable
   reflection-positive Wilson correlation function.
3. Test the scope of the RP claim using explicit positive kernels and spectral
   reasoning. Check the precise observables, geometry, and domination
   hypotheses of any Wilson/FSS argument; lack of a supplied rate is not a
   universal impossibility theorem.
4. Derive Cauchy--Schwarz directly for centered torus variables, retaining
   normalization, support, contact, and limit qualifications. Check whether
   (RA) or (RA-1) actually implies the specified charge limit.
5. Examine the reflection-odd-order lemma's state and clustering hypotheses.
   Seek an RP counterexample or a proof; separately test whether its conclusion
   entails alignment of all rotation-breaking order with lattice axes.
6. Reconstruct the dimension/tail counting and test the word "only" against
   other allowed massless or mixed correlations. Check the scope of Elitzur's
   local-gauge argument independently of spatial symmetry breaking.
7. Compare the quoted ROTDEF power with the actual derivative, surface measure,
   and angular-generator factors, distinguishing stress and current falloff.
8. Check what an invariant finite-volume sphere measure implies for its Ward
   identity and limits. Require an explicit identification of sphere symmetries,
   flat-limit observables, and invariant state selection before accepting a
   conclusion about the flat Wilson continuum limit.

The final section will state exactly what may be banked, with all remaining
conditions and unverified claims visible. Findings will be appended below after
these criteria; the criteria will not be rewritten in light of outcomes.

## Review disposition and source identity

**CONFIRMED:** TQ is not proved in this packet. The useful results are
conditional reductions and exact obstructions to particular arguments.
**NOT-VERIFIED:** a no-go theorem saying that RP together with the Wilson/UV
inputs cannot prove TQ, or that a canonical rotational Goldstone mode is the
unique possible failure mechanism. Those stronger statements exceed the
evidence. Source: `L/TQ55.md`, locating strings `Verdict: TQ is NOT proven`,
`No RP tool yields`, and `The exact obstruction`.

The review covers the entire 537-line `TQ55.md`, including T-E1 through T-E7,
and all four `checks/tq55_a*` evidence files. Necessary dependency reads:
`ROTDEF.md` definitions, §§3, 4.3, 5, 6, 7, and E4–E6;
`PROOF.md` L9a and its proof; `PANEL_P4.md` §§5.1–5.3;
`UNIV55.md` §3.4, its normalization correction, and errata. Other lane
results, including NODEA_RES55, are not independently certified here.
Earlier Codex verdicts are not used as mathematical authority.

This is a review of the supplied local snapshot. No git was used to ascertain
main-branch authority or freshness; no landing, source repair, or audit-status
change is attempted. The repository review and no-go procedures are applied
only within the user's narrower, one-file review instruction. The requested
model/effort label is not an independently measured execution receipt.

SHA-256 identifiers of the mathematical sources read:

| File under `L` | SHA-256 |
|---|---|
| `TQ55.md` | `9fa6cba2c9459bd94d0284f0c7d36317ea754a1b3657836de37cb91d931a5a38` |
| `ROTDEF.md` | `413261674aaafa7c68793e9f10ebc1421fdf92871bd583f7c654981511104bf2` |
| `PROOF.md` | `f8337f4a90d24bbc74e1e300dbaf2c4ac59596c4e8506d2dd986d7ea6f8b587c` |
| `PANEL_P4.md` | `57139e4e8ebc79d9aaa9b72545d81818a654b027d43e94a8bcbb406a02e69bf2` |
| `UNIV55.md` | `62033ebd7f6928261b8262616c9437bb22c4bca5179d645ed2b5119268ca8609` |
| `checks/tq55_a.py` | `69928d8534119755a008ea92133a3e611a69ee4a6e166ce1b85c06c281da884b` |
| `checks/tq55_a_criteria.md` | `32df9dd4ebd7d9631360099487198659f8f587304a72c694ecd9200ed1bb5b24` |
| `checks/tq55_a_out.txt` | `d2ab580b1ab5bccd04f485de89800a84f50423d414bbfe5675d7bc6c9651ae5c` |
| `checks/tq55_a_err.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

At the closing source check, TQ55, ROTDEF, P4, UNIV55, and all tq55_a
evidence files retained the hashes above. `PROOF.md` changed elsewhere
during this review to
`3271bfd9bfbc501b0ad65a166ae00fdf25e8a1fe672a1f515041c1c4107d00b7`.
The mathematical L9a RP proof was re-read and matches the proof used here.
The entire L9a block, from its heading to immediately before L9a′, has
SHA-256 `05193ff2cb0d1367e2b344dbce043e34c5151970862a71f7fafa883f570f35f5`.
No other portions of that evolving file are being certified.

## 1. Wilson-only charge and sampling-safe sufficient conditions

**CONFIRMED, conditional.** Source: `L/TQ55.md`, `Proposition 1.1`,
`Proposition 1.2`, `(E-ann)`, and T-E1/T-E2/T-E4;
`L/ROTDEF.md`, `SRC-O (observable side)`, `SRC-W (bulk insertion)`, and `E6`.

Write, with centered observables throughout,

\[
 S_j(s)=Z_j^{-2}\omega_j(\widetilde F_s),\qquad
 t_j(s,r)=Z_j^{-2}\operatorname{Cov}_{\omega_j}
                      (\widetilde F_s,\mathfrak T_r).
\]

Haar integration by parts for the **Wilson density** gives
\(\omega_j(\Xi F)=\operatorname{Cov}(F,\Xi S-\operatorname{div}\Xi)\).
The derivatives of the centering constants in \(d\omega_j(\widetilde F_s)/ds\)
multiply centered variables of zero expectation, so introduce no extra term.
With T-E2's centered source term, the exact identity yields

\[
 \|S'_j+t_j(\cdot,r)\|_\infty
 \le C\{g_{\rm bare}(a_j)^2+a_j^2\mathfrak L(a_j)(1+r^5)\}.
 \tag{1}
\]

Here and below lengths can be measured in \(\ell_{\rm ref}\). Required
conditions include \(Z_j>0\), \(a_j\to0\), \(R_j\to\infty\),
\(a_j^2\mathfrak L(a_j)\to0\), and the stated uniformity in the rotation
parameter. The cutoffs must fit inside the torus for sufficiently large j.
At any two **fixed** admissible radii,

\[
 \|t_j(\cdot,r)-t_j(\cdot,r')\|_\infty
 \le C a_j^2\mathfrak L(a_j)(r^5+r'^5)\longrightarrow0.
 \tag{2}
\]

This proves equality of the limsup numbers \(\Lambda(r)\). It does not assert
exact equality of the finite-cutoff shell torques. E6 gives uniform convergence
of the two terms making up \(S'_j\), as well as of \(S_j\). Passing the
fundamental theorem of calculus to the limit gives

\[
 t_j(\cdot,r)\longrightarrow -S'(\cdot)\quad\hbox{uniformly},
 \qquad \Lambda=\|S'\|_\infty.
 \tag{3}
\]

Consequently the limiting **specified two-point orbit** is invariant iff
\(\Lambda=0\), and \(\limsup_j\|S_j-S_j(0)\|_\infty\le2\pi\Lambda\).
CD, a coarse law, and RP are absent from this derivation. SRC-E supplies the
normalization/moment framework where invoked; none of SRC-O, SRC-W, or E6 is
proved for Yang–Mills by writing (1). Full OS1 on a whole field algebra would
require the analogous statement for that algebra, not just this test pair.

The averaging argument also checks. For \(r_2=r_1e^H\), average cutoffs with
\(d\rho/(H\rho)\). Their gradient obeys
\( |\nabla\bar\psi(y)|\le\|h'\|_\infty/(H|y|)\).
The forward-difference terms are bounded on the enlarged lattice annulus;
the constant 3 in Proposition 1.2 is a valid overestimate. First take
\(j\to\infty\) at fixed \((r_1,H)\) in (2). This proves

\[
 \Lambda\le 3\|h'\|_\infty\|J\|A(r_1,H).
 \tag{4}
\]

For E-ann put \(H=1\), and let \(S(r)\) be its nonnegative annular supremum
after \(\limsup_j\sup_s\). Only the deterministic smooth weight is converted
to an integral:

\[
 \sum_{r-a_j\le |x|\le 2er+a_j}a_j^4|x|^{-4}
 \longrightarrow |S^3|\int_r^{2er}\frac{d\rho}{\rho}
 =2\pi^2(1+\log2).
\]

Thus \(\Lambda\le6\pi^2\|h'\|_\infty\|J\|(1+\log2)S(r)\).
Any sequence \(r_n\to\infty\) with \(S(r_n)\to0\) suffices. No fixed
spacing of these scales is needed. This controls actual sampled sites and
does repair the arbitrary-envelope Riemann-sum defect. E-unif and the stated
iterated discrete E-Ces condition imply the same sufficient condition.
The continuum limit precedes the choice of larger annuli; a simultaneous
uncontrolled \(r=r_j\) limit would not be this proof.

**NOT-VERIFIED: the asserted equivalence of orders/selections of limits.**
Source: `L/TQ55.md`, `Which law. Equivalently, take each infinite-volume limit
point` and `or equivalently every infinite-volume Wilson limit point`.
Locality passes the identity to a fixed-a thermodynamic limit. It does not
identify an arbitrary joint diagonal limit with those iterated limits, or
replace one selected sequence by a supremum over every limit point. The exact
array \(b_{n,L}=\mathbf1_{L\le n^2}\) has
\(\lim_{L\to\infty}b_{n,L}=0\) for each n, but \(b_{n,n}=1\).
This is a counterexample to the proposed limit-exchange reasoning, not a
constructed Wilson counterexample. The identities and conditional reductions
can be stated separately for either family, with its own uniform hypotheses;
equivalence needs an additional selection/uniformity argument.

## 2. The rotlet, its Fourier bound, and its precise evidentiary scope

**CONFIRMED.** Source: `L/TQ55.md`, `The rotlet`, `Even a stress-channel
infrared bound would not imply TQ`; `L/checks/tq55_a.py`, `def rotlet`,
`P3 flux`, `P5 improvement`, and `OVERALL`.

Here is an independent calculation, without the runner's polynomial or
sphere-moment implementation. Set \(v=Mx\), \(M^T=-M\), in dimension d.
Direct differentiation gives

\[
 \partial_\mu\{(v_\mu x_\nu+v_\nu x_\mu)|x|^{-k}\}
 =(d+2-k)v_\nu|x|^{-k}.
 \tag{5}
\]

For \(d=4,k=6\), symmetry, degree \(-4\), and exterior conservation follow.
On a sphere of radius r, contracting the normal eliminates the first term;
the flux becomes

\[
 Q_J=\int_{S^3}(Mn)\cdot(Jn)\,d\Omega
     =\frac{|S^3|}{4}\operatorname{tr}(M^TJ).
 \tag{6}
\]

The identity \(\int n_an_b\,d\Omega=|S^3|\delta_{ab}/4\) follows from
orthogonal symmetry and \(\sum n_a^2=1\). With
\(M=J=E_{12}-E_{21}\), \(Q_J=|S^3|/2=\pi^2\). Orthogonal rotation planes
give zero. A decreasing cutoff's annular pairing is \(-Q_J\), since
\(\int\psi'(r)dr=-1\); the sign is immaterial for \(\Lambda\), but the
outward flux and the cutoff functional should not be conflated.

There is also an exact distributional representation:

\[
 \sigma_{\mu\nu}
 =\frac18(M_{\mu\alpha}\partial_\alpha\partial_\nu
          +M_{\nu\alpha}\partial_\alpha\partial_\mu)|x|^{-2}.
 \tag{7}
\]

Since \(\Delta|x|^{-2}=-4\pi^2\delta_0\) in four dimensions, this extension
has

\[
 \partial_\mu\sigma_{\mu\nu}
 =-\frac{\pi^2}{2}M_{\nu\alpha}\partial_\alpha\delta_0.
 \tag{8}
\]

It is conserved **away from the insertion**, not globally source-free.
Indeed a smooth globally conserved symmetric tensor could not carry this
charge through a contractible sphere. With Fourier convention
\(\hat f(p)=\int e^{-ipx}f(x)dx\), (7) gives, for \(p\ne0\),

\[
 \hat\sigma_{\mu\nu}(p)
 =-\frac{\pi^2}{2}
 \frac{(Mp)_\mu p_\nu+(Mp)_\nu p_\mu}{|p|^2}.
 \tag{9}
\]

This is bounded but depends on the direction of approach to zero. For the
source's smooth cutoff \(c=\kappa\sigma\), \(c\in L^2\) and
\(\Delta c\in L^1\). In fact \(\Delta\sigma=0\) outside zero, so
\(\Delta c\) is supported in the cutoff transition region. Therefore

\[
 |\hat c_{\mu\nu}(p)|\le
 \|\Delta c_{\mu\nu}\|_1/|p|^2\qquad(p\ne0).
 \tag{10}
\]

The exterior flux stays (6). This rigorously defeats an argument using only
exterior conservation, stress symmetry, and that Fourier upper bound.
The stated \(O(r^2)\) estimate follows by substituting \(q=rp\) in the
Fourier pairing with \(w_r(x)=W(x/r)\); a bounded transform gives only
\(O(1)\) by the same absolute-value argument.

**NOT-VERIFIED as a Wilson/RP counterexample.** Source: the same §2.2(d),
and §4.1's `Nothing available excludes it`. Neither the runner nor (5)–(10)
constructs a probability measure, a reflection-positive matrix of field
correlations, or a Wilson correlation satisfying SRC-O/W/E6. A mixed
\(\widetilde F\)-stress tensor is also not the positive stress-stress
spectral measure to which an actual domination theorem would apply. The
witness refutes the three named analytic constraints **alone**. It does not
establish logical independence from the complete Wilson hypotheses plus RP.

**REFUTED if read literally:** `no upper bound on |ĉ| expresses it`
(`L/TQ55.md`, §2.2(d)). A vanishing low-momentum envelope, together with
appropriate ultraviolet control, is a magnitude upper bound that makes the
scaled shell pairing vanish. The valid assertion here concerns the particular
\(C/|p|^2\) or bounded envelopes, not every possible upper bound. Nor is
full continuity of every Fourier component shown necessary for a selected
angular charge to vanish: components with zero flux can be present.

## 3. What RP proves about rates; what the FSS discussion leaves open

**CONFIRMED: RP/spectral positivity alone supplies no universal decay
exponent.** Source: `L/TQ55.md`, `It gives no rate`, §2.4.
For bounded observables one should use the finite-measure version

\[
 (1+n)^{-\alpha}=
 \frac1{\Gamma(\alpha)}\int_0^\infty
 t^{\alpha-1}e^{-t}e^{-nt}\,dt,\qquad\alpha>0,
 \tag{11}
\]

rather than require the unshifted \(n^{-\alpha}\) representation to have
finite mass at \(n=0\). An atom at spectral value 1 gives a constant.
The shift repairs that endpoint issue without changing the power-law rate.

There is an explicit four-dimensional lattice realization, so the argument
need not rest on the unverified phrase `Generalized free fields realize any
power`. Take a centered Gaussian field with covariance

\[
 C_\alpha(n)=(1+\|n\|_1)^{-\alpha}
 =\frac1{\Gamma(\alpha)}\int_0^\infty
 t^{\alpha-1}e^{-t}\prod_{i=1}^4 e^{-t|n_i|}\,dt.
 \tag{12}
\]

For \(q=e^{-t}\in(0,1)\), \(q^{|n|}\) is a positive covariance on
\(\mathbb Z\), with Fourier density
\((1-q^2)/(1-2q\cos p+q^2)\ge0\). Across a site plane the reflected
kernel in the normal coordinate is \(q^{n_i+m_i}\), a rank-one positive
kernel; across a link plane it is \(q^{n_i+m_i-1}\), also positive.
The transverse kernels are positive. Products and positive integrals
preserve positivity. Thus (12) is translation invariant, H(4)-invariant,
and RP for every coordinate site/link plane. Gaussian RP follows directly
on exponential cylinder functions: their reflected expectation matrix is a
positive diagonal congruence of the entrywise exponential of a positive
cross-covariance matrix, positive by its power series and Schur products.

Even a bounded local observable has this rate: with \(B=\sin\phi_0\),
\(C_\alpha(0)=1\) gives
\(\operatorname{Cov}(\sin\phi_0,\sin\phi_n)=e^{-1}\sinh C_\alpha(n)\),
asymptotic to \(e^{-1}C_\alpha(n)\). For long-range order, let every site
equal one common symmetric sign \(X\in\{-1,1\}\); reflection fixes X and
the RP form is \(E|F(X)|^2\), while the centered covariance is identically
1. These are exact RP counterexamples to a universal rate, **not** Wilson
theories or realizations of the stress Ward identities.

**CONFIRMED:** the temporal-gauge algebra
\(\operatorname{Re}\operatorname{tr}(UV^\dagger)
=N-\frac12\|U-V\|_{HS}^2\).
**NOT-VERIFIED:** existence of a Wilson domination theorem on the specified
periodic tori, or the assertion that a temporal chain exhausts every possible
FSS-type construction. Source: `L/TQ55.md`, `The Wilson action (ARGUED,
structural)`, §2.2(b). The displayed identity identifies a one-direction
quadratic coupling where temporal gauge is available. It does not remove
the periodic holonomy or provide a four-direction independent-spin
representation. The source appropriately says it did not exclude other
variable choices; keep that qualification.

The primary FSS paper's §2, Theorems 2.1–2.3, concerns nearest-neighbour
vector spins with a common single-spin measure; its introduction explicitly
allows a zero-momentum atom in addition to the bounded continuous Fourier
part. These results do not constitute a Wilson composite-stress theorem.
[Fröhlich–Simon–Spencer, original paper](https://math.caltech.edu/SimonPapers/65.pdf).
The later general theory also makes Gaussian domination a separate
hypothesis for its infrared implication (Theorem 4.4).
[Fröhlich–Israel–Lieb–Simon, original paper](https://math.caltech.edu/SimonPapers/93.pdf).
These two source checks are verified reads, not recollections `[m]`.

**NOT-VERIFIED as a universal prohibition:** `No RP tool yields ... by
itself`, if this means no combination of RP and the model-specific Ward
identities can prove TQ. The preceding examples establish absence of a
generic rate; they do not establish that stronger impossibility. Likewise,
the chessboard inequality as displayed has no separation-dependent decay
factor, but that does not rule out its use with additional dynamical input.
Source: `L/TQ55.md`, §§2.3, 2.6, and §4.1.

## 4. Cauchy–Schwarz, (RA), and (RA-1)

**CONFIRMED, conditional on the specified RP algebra and decay inputs.**
Source: `L/TQ55.md`, `Theorem 2.1`, `Corollary 2.2`, `One-sided variant
(RA-1)`, and T-E3; `L/PROOF.md`, `L9a. RP of the Wilson action`.

For reflection-invariant \(\omega\), the positive-half form
\((X,Y)_\theta=\omega(\theta X\,Y)\) is positive semidefinite. Constants
belong to that algebra. With \(X=\theta B-\omega B\) and
\(Y=C-\omega C\), its three entries are respectively
\(\operatorname{Cov}(B,C)\), \(\operatorname{Cov}(B,\theta B)\), and
\(\operatorname{Cov}(C,\theta C)\). The nonnegative quadratic polynomial
\((X+tY,X+tY)_\theta\) gives the stated inequality, including its zero-norm
cases, with constant exactly 1. No volume constant enters.

The gauge-fixing/crossing-plaquette proof read in L9a supplies this form for
real bounded gauge-invariant half-torus observables. B and C must fit in
opposite halves cut by a plane **and its antipode**; the theorem does not
permit arbitrary overlapping supports. At fixed cutoff the local Wilson
observables here are bounded. Weak limits preserve the inequalities for
the corresponding local observables, with moment control where needed.

Choosing a coordinate with \(|x_\alpha|\ge|x|/2\) and a midpoint plane
gives gaps \(h,h'\ge|x|/8\) once the stated support-distance margin holds.
T-E3's two-gap hypothesis is necessary: the lattice plane generally does
not give exactly equal arguments. Under that repaired (RA),

\[
 Z_j^{-2}|\operatorname{Cov}(\widetilde F_s,\mathcal T_{\mu\nu}(x))|
 \le 8^4\eta(|x|/8)|x|^{-4}.
 \tag{13}
\]

Summing the 16 tensor components merely enlarges the envelope. For RA-1
put the plane next to \(\widetilde F_s\), and use ordinary Cauchy–Schwarz
and SRC-E to obtain
\(G_{\widetilde F_s}\le\operatorname{Var}(\widetilde F_s)\le C_F Z_j^4\).
The assumed stress bound then gives (13) with a fixed pair-dependent
constant. It works for every pair having the SRC-E moment bound, not with
one universal constant over unbounded test families. All torus hypotheses
are understood only at admissible separations; applying them to fixed
annuli as j grows avoids antipodal wrap-around. The inequality is proved
on every torus; **the decay hypotheses on every torus are not proved**.

**REFUTED as written:** the coexistence caveat `different ⟨e⟩ or ⟨𝒯⟩,
then G_F̃ and G_𝒯 tend to the positive between-phase variances`
(`L/TQ55.md`, §2.1). Differences in either mean do not make both projections
nonzero. In the exact RP common-sign model above, take \(A=B=X\), with
equal-weight phases \(X=\pm1\). The two phase means differ, but the
state-centered pair is \(\widetilde F=X^2=1\); hence
\(G_{\widetilde F}=0\). This is a counterexample to the stated
`inspection` argument, not to a Wilson claim. RA can fail through coexistence
when the relevant product of nondecaying projections is nonzero; it is a
sufficient rather than a necessary condition for TQ.

**REFUTED:** `A gap implies all three. So does a free, or O(4)-symmetric
unitary-conformal, infrared` when this includes M2′/RA-1
(`L/TQ55.md`, §4.1, `Relative strength`). This contradicts the correct
borderline caveat in §2.1. A nonzero canonical stress autocorrelation
\(G_{\mathcal T}(h)=c h^{-8}\), \(c>0\), cannot obey
\(G_{\mathcal T}(h)\le\eta(h)^2h^{-8}\) with \(\eta\to0\).
For an exact free-Maxwell comparator, the standard Gaussian covariance
derived from \((4\pi^2|x|^2)^{-1}\) gives electric/magnetic component
correlations \(\mp1/(\pi^2t^4)\) along the time axis. Wick's rule and
\(T_{00}=\frac12\sum_{i=1}^3(E_i^2-B_i^2)\) give
\(\langle T_{00}(0)T_{00}(t)\rangle_c=3/(\pi^4t^8)\).
At reflected separation \(t=2h\), the coefficient is
\(3/(256\pi^4)>0\). Thus this free example has no RA-1 margin. A gap
implies the stated uniform conditions only when its channel decay and
prefactors are uniform along the normalized sequence.

## 5. Reflection-odd order: the lemma is valid; its interpretation is narrower

**CONFIRMED on the RP observable algebra, with “almost every component.”**
Source: `L/TQ55.md`, `Lemma 2.3`, `Von Neumann's mean ergodic theorem`, and
`stress expectation is diagonal in the lattice frame`.

Let B be real, local, in \(L^2(\omega)\), odd under the specified site
reflection, and admissible for RP after translation into a half-space.
For the Wilson input used here this includes bounded gauge-invariant local
observables. Translation invariance and RP give, for all sufficiently large n,

\[
 0\le\omega(\theta B_n B_n)
   =-\langle B,U^nB\rangle,\qquad U=\tau_{2e_\alpha}.
\]

The Cesàro averages of \(U^n\) converge strongly to the orthogonal
projection \(P_{2\alpha}\) onto its invariant subspace. Consequently

\[
 0\ge\lim_N\frac1N\sum_{n=1}^N\langle B,U^nB\rangle
   =\|P_{2\alpha}B\|_2^2\ge0.
\]

Thus \(P_{2\alpha}B=0\), and projection onto the smaller fully
translation-invariant sigma-algebra gives \(E[B\mid\mathcal I]=0\).
There is no clustering assumption hidden in this proof. The finitely many
small n do not affect the average. The ergodic decomposition conclusion is
an almost-sure one; it says nothing about arbitrarily inserted zero-weight
components. The statement should explicitly retain membership in the RP
algebra, rather than infer RP for every possible gauge-variant observable
from L9a as written.

For a site-centered covariant stress tensor, the off-diagonal component is
odd under either of its indexed coordinate reflections. Hence its mean
vanishes in almost every component. More generally, applying the lemma to
\(B=G-\rho_\alpha G\) and using a countable determining local algebra proves
that almost every component is invariant under all the coordinate
reflections. This justifies “axis-aligned” **in the source's stated sense of
coordinate-reflection invariance**, and excludes a polar vector or a single
off-axis rank-two director. It does not classify all higher-rank order or
prove absence of rotation breaking.

For example, a reflection-even multiplet can favor body-diagonal directions.
Let D consist of \(d=(\pm1,\pm1,\pm1,\pm1)/2\), and define a constant
rank-four tensor by its quartic form

\[
 A(n)=\frac1{16}\sum_{d\in D}(d\cdot n)^4
      =\frac1{16}\left(3|n|^4-2\sum_i n_i^4\right).
\]

It is invariant under every signed permutation but not every rotation:
\(A(e_1)=1/16\), whereas \(A((1,1,1,1)/2)=5/32\).
A deterministic, spatially constant field with this tensor value is
translation invariant and coordinate-RP, since reflection fixes its only
configuration. This exact example limits any stronger reading of `order
along non-coordinate axes are excluded` in §2.5. It is not a Yang–Mills
state, and is not a counterexample to the reflection-odd lemma.

**CONFIRMED:** the displayed Maxwell sign in §2.5 follows from
\(- (\partial_0^2+\partial_i^2)(4\pi^2|x|^2)^{-1}
=-1/(\pi^2s^4)\) on the time axis.
**NOT-VERIFIED:** that this establishes consistency of the particular
rotational Goldstone scenario in §3.1. A reflection-odd field-strength
correlation of degree \(-4\) is not a reflection-positive construction of
the proposed dimension-1 angular fluctuation, its stress coupling, and their
joint correlations. The source's explicit OPEN qualification is necessary.

## 6. Dimension counting, phase mixtures, and Elitzur

**CONFIRMED in the named Gaussian comparator.** Source: `L/TQ55.md`,
`Free massless abelian comparator`, §3.1. Differentiating the massless
propagator twice gives a field-strength crossing of degree \(-4\).
In a connected Gaussian contraction with a quadratic stress insertion,
both of its field-strength legs must cross to the distant local cluster;
the product has degree \(-8\). Internal contractions in that cluster do
not change the distant power. This is a comparator calculation, not an
infrared theorem about interacting Yang–Mills.

**NOT-VERIFIED:** `only broken rotations give the |x|⁻⁴ rotlet tail`,
`TQ fails iff the selected limit has an ergodic component that is not
rotation invariant`, and `The exact obstruction`
(`L/TQ55.md`, §§3.1–3.2, §4.1, summary row 18).
The established obstruction is exactly the nonzero normalized charge in
(3), not an established pointwise asymptotic expansion or particle spectrum.
In particular:

- SRC-O/W and E6 do not even assert existence of a pointwise limiting
  mixed stress correlation. Nonzero shell integrals cannot supply such an
  assertion, an exact homogeneous tail, or a Goldstone pole.
- A conserved tensor with nonzero angular charge can be decomposed into
  the matching rotlet (6) and a tensor with zero angular charge. Calling
  this quotient a “rotlet component” is legitimate if explicitly defined;
  it proves neither pointwise dominance of that component nor a physical
  mode responsible for it.
- The assignments \(\Delta_{IR}(\pi)=1\), a nonzero linear stress coupling
  of effective dimension 3, and a nonzero overlap of the chosen
  \(\widetilde F\) with that mode are assumptions in the proposed scenario.
  A Goldstone argument for broken spacetime symmetries requires its own
  hypotheses; canonical counting does not establish them.
- The conformal spin bound quoted `[m]` assumes a unitary conformal,
  rotation-covariant infrared theory. It does not classify all gapless
  nonconformal infrared behavior. It cannot be used to derive precisely
  the symmetry whose possible failure is being examined.
- Proposition 1.1 concerns a specified test-pair orbit. Failure of full
  state invariance, or of invariance in another observable sector, need
  not be detected by that orbit. Radial f and g, for example, have a
  constant orbit in every state. A statement about all ergodic components
  requires all relevant observables and an additional decomposition
  argument, not just the one-orbit identity.

The word “only” is therefore not bankable. The low-dimensional linear
Goldstone ansatz gives the advertised \(|x|^{-4}\) mixed correlation **if**
its propagator and couplings are supplied; it is a possible explanatory
ansatz, not an exhaustive theorem. No Wilson counterexample to TQ is
constructed in this review either.

**CONFIRMED:** Proposition 3.1 for a mixture of rotation-invariant states,
with the stipulated integrability (`L/TQ55.md`, `Proposition 3.1`).
Integrate the invariance of each state's observables, then form connected
correlations in the resulting state; apply (3) to the original Wilson
sequence if E6 holds. No affine decomposition of the state-centered pair
is needed. For a fixed G and translation-invariant components,
\(\omega_i(\mathfrak T_r)=0\) by telescoping, so total covariance does
give \(\operatorname{Cov}_\omega(G,\mathfrak T_r)
=\int\operatorname{Cov}_{\omega_i}(G,\mathfrak T_r)d\kappa(i)\).
Neither statement justifies the source's stronger “iff” classification.

**CONFIRMED in scope:** the local gauge-averaging argument does not exclude
the gauge-invariant rotational order being discussed. Source:
`L/TQ55.md`, `Elitzur-type argument: no, and the reason is exact`, §3.3.
For an exactly invariant local gauge transformation, the change of action
and Haar Jacobian vanish, and averaging constrains observables that
transform nontrivially. A gauge-invariant tensor is unchanged by that
averaging. A spatially varying rotation is not such a local symmetry;
its change of variables produces
\(\mathfrak W=-\mathfrak T_r+\mathfrak B(v_r)\) and the observable source
term. Only **after** the stated normalized UV remainders vanish is its
remaining obstruction precisely TQ. This is why the local-gauge argument
does not close the rotation problem; it is not a general theorem that no
other positivity argument could do so. Broad historical assertions about
all d=4 exclusion theorems, Vafa–Witten, or QCD remain the source's
recollections `[m]`, not certified inputs here.

## 7. Stress versus angular-current powers, and a lattice trace qualification

**CONFIRMED: the ROTDEF exponent correction.** Source: `L/TQ55.md`,
`Correction to ROTDEF §8.2`; `L/ROTDEF.md`,
`A Goldstone-type |x|⁻³ (ε ∝ ρ)`.
In d=4 the surface measure contributes \(r^3\), and the rotation generator
\(Jx\) contributes r. A nonzero, scale-independent flux therefore has a
charge-carrying stress projection of degree \(-4\). Its angular-current
projection has degree \(-3\). An uncancelled stress projection of degree
\(-3\) would instead produce a flux proportional to r, contradicting
(2) after the continuum limit. A slower **zero-flux** contribution can
still exist; the correction must not prohibit it. No universal Goldstone
mechanism follows from this geometric power count.

**CONFIRMED:** constants and exactly divergence-free improvements contribute
zero to the discrete functional by summation by parts
(`L/TQ55.md`, `Constants carry no flux`, `Identically conserved
improvements carry no flux`). This is an operator identity before averaging.

**REFUTED under the unrestricted reading of “trace part.”** The additional
sentence `The trace part ... drop out exactly` in §1.2(a) is true for a
constant trace, but not a general spatially varying lattice trace. Its own
§1.2(c) and `ROTDEF.md` §4.3 correctly allow a discretization remainder.
For an exact local check take \(a=1\), \(J=E_{12}-E_{21}\),
\(x=(2,4,0,0)\), and radial \(\psi(x)=|x|^4\). Then

\[
 \sum_\mu\nabla_\mu[\psi(x)(Jx)^\mu]
 =4(25^2-20^2)-2(29^2-20^2)=18\ne0.
\]

A radial smooth cutoff can agree with a rescaled affine function of this
radial polynomial near these sample radii inside its transition annulus,
so compact support does not restore a pointwise identity. Multiplying by
a nonconstant trace density prevents telescopic cancellation. Only its
continuum radial contraction vanishes exactly; using the \(O(a/r)\)
remainder in a limiting covariance still needs the appropriate bounds.
This does not affect (1)–(4), which keep the full discrete tensor.

## 8. Sphere route: valid conditional symmetry argument, unproved construction

**CONFIRMED as geometry and as a conditional limit argument.** Source:
`L/TQ55.md`, `On S⁴_R the generators are global Killing fields` and
`SO(5)-invariant sphere states would instead converge`;
`L/PANEL_P4.md`, `S2. SO(5) invariance` and `S5. R → ∞`;
`L/UNIV55.md`, `A second architecture, available for UNIV-S only`, §3.4.

On the round sphere a global Killing field has
\(\nabla_{(\mu}v_{\nu)}=0\). Contracting with a symmetric stress tensor
vanishes; integration by parts on the closed sphere has no physical
boundary and requires no cutoff shell. Local coordinate-chart boundaries
cancel in a correctly constructed global continuum theory. This removes
the particular flat-route shell term, not the need to control a
noninvariant lattice regulator.

Suppose invariant continuum sphere states \(\mu_R\) have actually been
constructed, with a compatible observable map and sufficient local
compactness/moment control as \(R\to\infty\). At a fixed pole N,

\[
 \exp_N(Qx)=\operatorname{diag}(Q,1)\exp_N(x),\qquad Q\in SO(4).
\]

The pulled-back correlations are thus SO(4)-invariant for **each R**;
every convergent local limit retains that identity. No clustering or TQ
assumption enters this passage. SO(5) alone has pole stabilizer SO(4),
not O(4). The O(4) version additionally uses reflection invariance, which
the proposed reflection-symmetric Wilson sphere construction is meant to
supply; an SO(5)-invariant, reflection-invariant state is O(5)-invariant.

**NOT-VERIFIED as an achieved Yang–Mills result:** the invariant sphere
states and the necessary uniform limiting bounds. `PANEL_P4.md` explicitly
labels S2 and the geometric extensions open. `UNIV55.md` §3.4 names W0–W3,
including marginal coupling-profile matching, source/contact estimates,
seam transparency, and covariance of the observable map. Its normalization
correction also includes a dimension-4 coefficient of order
\(g_0(a)^2\). None is supplied merely by the absence of a shell.
Continuous rotations are exact symmetries of the **round geometry**;
they are not exact symmetries of an arbitrary finite cellulation.
The estimate \(O(a^2\mathfrak L R^5)+O(g_{\rm bare}^2)\) in TQ55 is
therefore a conditional target, not a proved cutoff estimate on S⁴.

**CONFIRMED with distinct selections:** if the flat-torus selection fails
TQ, a separately constructed invariant sphere selection can still have an
invariant flat limit. This does not prove that the two sequences select
the same state. If the same state obeys the hypotheses of (3) for the same
observables, it cannot both be invariant and fail that Wilson TQ criterion.
Nor does the conditional sphere mechanism prove that it is the sole
surviving construction route. Source: `L/TQ55.md`, `the sphere route is
the one that survives`.

## Exact checks actually executed

All computations were executed in memory with `python3 -B`. No numerical
quadrature, floating-point approximation, generated script, or extra output
file was used. The original runner was read before execution to check its
write behavior.

1. Executed `checks/tq55_a.py` through an in-memory `compile`/`exec` capture.
   Its complete stdout matched `tq55_a_out.txt` exactly; stderr was empty;
   `allpass` was true. All five individual adverse cases fired (the two
   exponents in C1, then C2, C3, and C4).
2. Independently used symbolic differentiation of the rational tensor with
   **six arbitrary antisymmetric matrix entries**. All four divergences and
   all sixteen exterior Laplacians were exactly zero. The Hessian identity
   (7) held entry by entry. For \(J=E_{12}-E_{21}\), the normalized flux was
   \(M_{12}/2\), giving \(1/2\) at M=J; the first-term-only flux density
   vanished identically. The general proof is (5)–(7), not numerical
   agreement with runner constants.
3. Mutated only in-memory copies: replacing the divergence denominator power
   6 by 5, and separately replacing P3's expected flux \(1/2\) by \(1/3\).
   Both produced `allpass=False` and `OVERALL: FAIL`. The original runner
   reports failure in text/flags rather than raising a failing exit status;
   those flags and stdout were inspected directly.
4. Exact supporting arithmetic: the radial discrete trace example gave 18;
   the three leading minors of the \(\alpha=1\) Hankel matrix
   \([1/(1+i+j)]_{i,j=1}^3\) were \(1/3,1/240,1/378000\);
   the Maxwell Wick coefficient was \(6(1/2)^2\,2=3\).
   The Hankel sample is only a control; the all-exponent RP proof is (11)–(12).
   A separate exact enumeration of all sixteen body-diagonal signs also
   returned \(1/16\) and \(5/32\) for the two rank-four tensor evaluations
   in review §5.

No Wilson decay estimate, numerical Yang–Mills simulation, sphere
construction, or NODEA_RES55 computation was run. Literature recollections
`[m]` were not promoted by these checks.

## Negative-claim scope check

This applies the repository's no-go discipline to the claim under review;
it is not a new impossibility certificate or a landing packet.

- **N1:** Distinct mechanisms examined were the conserved-flux identity,
  absolute Fourier bounds, positive spectral measures, RP
  Cauchy–Schwarz/odd-order projections, local gauge averaging, and the
  compact-sphere symmetry passage. FSS gauge-variable constructions beyond
  the displayed chain and model-specific combinations remain unexhausted.
  Counting mechanisms does not prove completeness.
- **N2:** No independence of SRC-O/W/E6, a gap, RA, RA-1, uniqueness, and TQ
  is claimed. RA and RA-1 are alternative sufficient inputs, not independent
  necessary conditions; (3) is an equivalent restatement for the given orbit.
- **N3:** Uniformity, centering, local support, normalization, convergence of
  derivative tests, RP-algebra membership, sphere source/seam estimates,
  and state selection are explicit above. None is silently proved by
  dimension counting.
- **N4:** The rotlet addresses exterior tensors and an absolute Fourier
  bound; the Gaussian examples address RP rates. Neither matches the full
  Wilson-plus-SRC premise set. NODEA_RES55's Hessian claim is not used as
  evidence against an FSS theorem.
- **N5:** Exact tensor calculations, generic spectral constraints, and a
  finite-torus inequality do not decide the continuum Wilson infrared
  dynamics. The negative conclusions are restricted to those checked
  objects and hypotheses.
- **N6:** No new physical axiom or premise grant is proposed. A better
  model-specific inequality could discharge TQ; renaming it does not.
- **N7, strongest counter-route:** RP's reflection-odd constraints might
  combine with the Wilson Ward identities and a justified stress/operator
  representation to exclude the charge without proving the generic
  pointwise decay rate used in M1/M2. The present witnesses do not satisfy
  that joint premise set, so this route is not ruled out.
- **N8:** The scoped neighboring sources were ROTDEF's decay reduction and
  P4/UNIV55's invariant-sphere alternative. The sampling correction improves
  the former and the latter changes the selection mechanism. Neither is a
  prior proof that all RP-based routes fail. No broad campaign-history or
  current-main authority search was performed under this no-git review.

## Exactly what may be banked

1. **CONFIRMED, conditional:** for the centered Wilson two-point orbit,
   SRC-O/W, the stated normalization/limits, vanishing bare coupling, and
   E6 give \(\Lambda=\|S'\|_\infty\), independent of every fixed admissible
   shell radius. \(\Lambda=0\) is equivalent to invariance of that orbit.
   CD and the coarse law are unnecessary. Source: `TQ55.md`, Prop. 1.1,
   T-E1/T-E2; qualifications in review §1.
2. **CONFIRMED, conditional:** DEC-A, the sampled E-ann condition on even a
   sparse sequence of radii, E-unif, or the stated discrete E-Ces condition
   suffices. The constant and order of limits in (4) are valid. Source:
   `TQ55.md`, Prop. 1.2, E-ann, T-E4.
3. **CONFIRMED:** the exact exterior rotlet, its nonzero flux, and the
   cutoff Fourier bound. Conservation, symmetry, and that absolute bound
   alone do not force zero charge. This is not a Wilson/RP-state
   counterexample. Sources: `TQ55.md` §§1.2(d), 2.2(d), and `tq55_a.py`.
4. **CONFIRMED:** generic coordinate RP permits arbitrarily slow power-law
   reflected correlations and long-range order. It supplies no universal
   rate. **NOT-VERIFIED:** impossibility of deriving TQ from RP combined
   with the Wilson-specific inputs, or exhaustion of FSS constructions.
   Source: `TQ55.md` §§2.2–2.4, with review §3's exact realizations.
5. **CONFIRMED, conditional:** torus RP Cauchy–Schwarz has constant 1;
   T-E3's repaired RA and SRC-E-supported RA-1 imply the sufficient decay.
   Their hypotheses remain open. Canonical free stress decay does not
   satisfy RA-1. Source: `TQ55.md`, Thm. 2.1, Cor. 2.2, T-E3.
6. **CONFIRMED:** reflection-odd RP-admissible local observables have zero
   fully invariant conditional mean; almost every ergodic component is
   coordinate-reflection invariant and has diagonal covariant stress
   expectation. This is not a classification of all orientational order.
   Source: `TQ55.md`, Lemma 2.3.
7. **CONFIRMED:** the free two-crossing \(|x|^{-8}\) comparator, vanishing
   torque of constants/exact improvements, the stress/current distinction
   \(|x|^{-4}\)/\(|x|^{-3}\), invariant-state mixture implication, and the
   inapplicability of local gauge averaging to gauge-invariant rotational
   order. **NOT-VERIFIED:** the exclusive Goldstone mechanism or its claimed
   ergodic-component “iff.” Source: `TQ55.md` §§1.2, 1.4, 3.1–3.3.
8. **CONFIRMED, conditional:** invariant continuum sphere states need no
   cutoff-shell TQ argument, and compatible convergent flat limits preserve
   their rotations (and reflections when supplied). Their construction,
   UV estimates, uniform bounds, and identification with a particular flat
   Wilson selection remain unproved. Source: `TQ55.md` §4.2;
   `PANEL_P4.md` S2/S5; `UNIV55.md` §3.4.

**TQ for four-dimensional Wilson Yang–Mills remains NOT-VERIFIED. No proof
of its failure, no complete RP no-go theorem, and no completed sphere
construction may be banked from this packet.**
