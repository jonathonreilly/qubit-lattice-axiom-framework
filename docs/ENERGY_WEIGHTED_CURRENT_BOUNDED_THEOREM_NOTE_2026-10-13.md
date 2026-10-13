---
claim_id: energy_weighted_current_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Conditional energy-weighted trace-ideal bounds, actual placed weighted-density transfer, and normalized-current mean comparison, with separate common-carrier, moment, placement, coefficient and hold-generator hypotheses."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: accepted_source_with_reviewable_publication_wrapper
runner: scripts/energy_weighted_current_identity_2026_10_13.py
scientific_execution: none_in_this_assembly
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: supplied-model conditional arguments with explicit provisional dependencies
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete separately scoped proof bodies preserved with accepted topology wording precisions
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: root publication review and integration; current-main landing checks and independent retained audit remain separate
upstream_dependencies:
  - energy_distribution_limit_bounded_theorem_note_2026-10-13
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
---

# Energy-weighted densities and normalized-current means

This publication candidate carries three complete root-accepted conditional bodies:
the 632-line weighted-trace independent derivation, the 155-line native
weighted-density addendum, and the 502-line normalized-current composition
check. The first two have narrowly recorded topology-wording precisions;
the complete current body is byte-exact. Their local notation, equation
labels and distinct hypotheses are preserved. These wrappers add scope,
chronology and provenance, not another proof or an independent check.

The first body treats positive normal states with one common nonnegative
Hamiltonian and spectral second moments, defining weighted products through
Hilbert--Schmidt factors and closures. The native body instead compares
actual energy-weighted positive operators under the specified Fock placement
and the actual commuting energy bridge. These operators need not have unit
trace. Form readouts require specified bounded coefficient operators and
their stated comparison; physical detector/current identification is extra.

The current body compares the supplied normalized current using low-density
trace error and actual free-energy second moments. Its later free-hold result
requires strong commutation with each true hold generator. The same body
gives a bounded even CAR interaction for which the current changes, so an
interacting hold does not acquire conservation from free conservation alone.
It retains the unscaled-current countercontrol as a state-class result,
without claiming realization by a fixed preparation and pulse.

Native half-energy weighted trace convergence and scalar Wasserstein
quadratic convergence have no unconditional ordering by strength. Scalar
energy laws miss coherences; weighted convergence alone does not supply
the separate second-moment/graph resources used for the scalar endpoint.
The continuum two-particle witness and the fixed-spacing growing-number
even witness are distinct. A compressed position example uses a specified
bounded one-particle map; it is an effect when that map is a contraction.
No particular physical embedding follows merely from writing a compression.

## Chronology and local notation

The independent weighted proof froze at 00:42:40 UTC on 2026-10-13, SHA-256
`7c9df64640d1296f2dc8a6d1a522652d0f766fdad769b14ec303f38dd8b6ff23`.
The full 584-line source-exposed comparison froze at 00:59:09 UTC, SHA-256
`202b44242e9f9b1d8ba8e93302745e3c91425aa4a63b6b599850cb8f12de02e7`,
and included all 155 native lines. Root's 01:01:28 acceptance and the
weighted precision record document conditional acceptance with scope
qualifications, not a second independent native derivation. The complete
502-line current check subsequently froze at 01:16:51 UTC, SHA-256
`3ed69527ba6177ae17a66eeabe45f98591cf60a1d2f9367bfacd95306fca52f6`,
and root's 01:24:32 record accepts its formulas, domain interpretation,
free-hold consequence and interacting countercontrol conditionally.

Thus older statements that a root was unexposed, an addendum unreviewed,
or the current check still active are preserved history, superseded for
review chronology by the later exact records just identified. This new
source assembly was accepted by root at 02:27:42 UTC with explicit reuse of
complete body coverage. The new publication wrappers remain subject to exact
root review. No model-diverse, formal, transitive
audit or retained-status conclusion follows. Current remains open_gate.

Equation prefixes W, N and C remain local to their bodies. J labels refer
to the historical 133-line current root, archived as evidence; the complete
current proof is the 502-line body below. The first body's energy scale,
the native body's unit convention, full placed trace error and reduced
low-density trace error must not be silently identified. Context-specific
symbols such as the interaction bound and current operator keep their
original meanings. The accompanying byte/line map identifies every piece.

## Preserved weighted-trace independent derivation

# Energy-sensitive trace ideals from full density convergence

Status: independent conditional mathematical derivation under the stated
state and moment hypotheses. This is a same-family text derivation, not a
formal proof, a model-diverse audit, or a transitive validation of its
physics parents. The new root argument remains unexposed before this
note's freeze. The original independent energy-law argument is unchanged.

The principal conclusion controls energy-relative forms and coherences
not determined by scalar energy laws. No unconditional ordering with scalar
Wasserstein W2 convergence is asserted. If two positive normal states approach in trace norm and have
uniformly bounded second moments of one common nonnegative Hamiltonian,
their density difference approaches zero in every symmetrically weighted
trace norm strictly below the full graph weight. In particular the
half-energy sandwich converges, uniformly controlling all bounded
energy-relative quadratic forms. The full graph sandwich and the
one-sided full energy weight need additional information. Actual even
free-Fock families test these boundaries below; their realization by a
fixed preparation and pulse is not asserted.

## 1. Carrier, moments, and precise weighted products

Let \(\mathcal H\) be a Hilbert space, \(H\ge0\) selfadjoint, and
\(\rho,\sigma\ge0\) trace-class with trace one. Write
\[
 X=\rho-\sigma,\qquad \delta=\|X\|_1\in[0,2],\qquad
 s_\tau^2=\int_0^\infty E^2\,d\operatorname{Tr}(\tau\mathbf1_{[0,E]}(H))
             =\|H\tau^{1/2}\|_2^2<\infty,\quad \tau=\rho,\sigma.
                                                               \tag{W1}
\]
The integral denotes the second spectral moment, more unambiguously
\(\int E^2\,d\mu_\tau(E)\), where
\(\mu_\tau(B)=\operatorname{Tr}\tau\mathbf1_B(H)\).
It does not require \(H^2\tau\) to be trace-class, vectors to lie in
\(D(H^2)\), or unbounded cyclic trace manipulations.

Fix an energy unit \(h_*>0\) and put
\[
 A=I+H/h_*,\qquad
 S_\tau=\|A\tau^{1/2}\|_2\le1+s_\tau/h_*,\qquad
 M^2=S_\rho^2+S_\sigma^2.                                      \tag{W2}
\]
This shift includes the vacuum and other zero-energy coherences in the
weighted norm. \(A\ge I\) and \(D(A)=D(H)\). In particular
\(M^2\le(1+s_\rho/h_*)^2+(1+s_\sigma/h_*)^2\).

Here and below \(\|\cdot\|_2\) is the Hilbert--Schmidt norm. To justify
the domain statement in W1, diagonalize a positive trace-class state as
\(\tau=\sum_j t_j|u_j\rangle\langle u_j|\). Monotone spectral cutoffs
give
\[
 \operatorname{Tr}\tau A^2=\sum_j t_j\|Au_j\|^2<\infty.           \tag{W3}
\]
Every positive-weight \(u_j\) therefore lies in \(D(A)\). The operator
with columns \(\sqrt{t_j}Au_j\) is Hilbert--Schmidt. For an arbitrary
vector, partial sums converge both before and after applying \(A\);
closedness of \(A\) proves that \(\tau^{1/2}\) maps all of
\(\mathcal H\) into \(D(A)\), and that this Hilbert--Schmidt operator
is exactly \(A\tau^{1/2}\). No commutation of \(A\) with \(\tau\)
was used. The same reasoning works for \(A^a\), \(0\le a\le1\).

For \(0\le a,b\le1\), define the trace-class operator
\[
 T_\tau(a,b)=(A^a\tau^{1/2})(A^b\tau^{1/2})^*,\qquad
 T_X(a,b)=T_\rho(a,b)-T_\sigma(a,b).                              \tag{W4}
\]
On \(D(A^b)\) it agrees with \(A^a\tau A^b\), respectively
\(A^a X A^b\). Thus W4 is their unique bounded closure from that dense
domain. Equivalently it represents, for
\(u\in D(A^a),v\in D(A^b)\), the form
\(\langle A^a u,\tau A^b v\rangle\). We use the sandwich notation
for these closures only. For balanced weights \(T_\tau(a,a)\ge0\),
\[
 \operatorname{Tr}T_\tau(a,a)=\operatorname{Tr}\tau A^{2a},\qquad
 \Gamma:=\|T_X(1,1)\|_1\le M^2.                                \tag{W5}
\]
The last bound is the triangle inequality for two positive trace-class
operators. It does not assert the generally false noncommutative
operator inequality \(|\rho-\sigma|\le\rho+\sigma\).

These constructions also hold for arbitrary positive finite-trace
densities with finite second moments. The balanced theorem below does
not use trace normalization; its \(\delta\) and \(M\) are simply the
corresponding unnormalized quantities. Normalization is used for the
moment simplifications in W2 and the asymmetric corollary.

## 2. Balanced interpolation, including its cutoff proof

For every \(0\le\theta\le1\),
\[
 \boxed{\quad
 \|A^\theta X A^\theta\|_1
       \le \delta^{1-\theta}\Gamma^\theta
       \le \delta^{1-\theta}M^{2\theta}.
 \quad}                                                        \tag{W6}
\]
The endpoint conventions are \(\delta\) at zero and \(\Gamma\) at
one. If \(\delta=0\), all these operators vanish. Consequently,
\(\delta_n\to0\) and uniformly bounded \(s_{\rho_n},s_{\sigma_n}\)
imply weighted trace convergence for every fixed \(\theta<1\).
For varying exponents \(\theta_n\uparrow1\), the same bound suffices
if \((1-\theta_n)\log(1/\delta_n)\to\infty\), with uniformly bounded
\(M_n\) and eventually \(0<\delta_n<1\). A fixed-exponent conclusion
does not silently include all approaches to the endpoint.

Here is a direct proof, including the noncommuting cutoff passage. Set
\(A_N=\min(A,N)\), \(N\ge1\), by spectral calculus. It is bounded
and strictly positive. For a bounded contraction \(U\), define
\[
 F(z)=\operatorname{Tr}\bigl(U A_N^z X A_N^z\bigr),
                    \qquad0\le\operatorname{Re}z\le1.          \tag{W7}
\]
Bounded \(\log A_N\) makes this analytic in the open strip and
continuous on its closure. Its absolute value is bounded on the strip.
Imaginary powers are unitary, so the two boundary estimates are
\[
 |F(it)|\le\delta,\qquad
 |F(1+it)|\le\Gamma_N:=\|A_N X A_N\|_1.                         \tag{W8}
\]
The unitaries occur on both sides of \(X\); they need not be adjoints
for trace-norm invariance under left and right unitary multiplication.
On the right boundary they similarly flank \(A_N X A_N\).

For completeness the scalar strip estimate used here follows from the
maximum principle. Given positive boundary bounds \(b_0,b_1\), divide
\(F(z)\) by \(b_0^{1-z}b_1^z\) and multiply by
\(\exp(\eta z(z-1))\), \(\eta>0\). On either vertical edge the
modulus is at most one. On the horizontal edges of taller rectangles it
tends uniformly to zero: the normalized function is bounded on the
strip, while the extra modulus contains \(e^{-\eta t^2}\).
The maximum principle, followed by height tending to infinity and
\(\eta\downarrow0\), gives
\(|F(\theta)|\le b_0^{1-\theta}b_1^\theta\).
Zero boundary bounds follow by replacing them by positive upper bounds
and decreasing those bounds to zero. Trace duality
\(\|Y\|_1=\sup_{\|U\|\le1}|\operatorname{Tr}UY|\) now gives
\[
 \|A_N^\theta X A_N^\theta\|_1
                     \le\delta^{1-\theta}\Gamma_N^\theta.      \tag{W9}
\]
Trace duality follows from the polar decomposition, and
\(\|RS^*\|_1\le\|R\|_2\|S\|_2\) is the Hilbert--Schmidt
Cauchy--Schwarz inequality; these apply to all products used here.

For \(0\le a\le1\), scalar spectral dominated convergence gives
\[
 \|(A_N^a-A^a)\tau^{1/2}\|_2^2
     =\int |\min(x,N)^a-x^a|^2\,d\mu_\tau^A(x)\longrightarrow0.
                                                               \tag{W10}
\]
The dominating function is \(x^{2a}\le x^2\) on the spectrum of
\(A\). The scalar measure here is \(\operatorname{Tr}\tau E_A\);
\(\tau\) need not commute with the spectral projections.
Applying the Hilbert--Schmidt product inequality to the difference of
the two products in W4 proves convergence in trace norm for every
\((a,b)\in[0,1]^2\). In particular
\(\Gamma_N\to\Gamma\). Taking the limit in W9 proves W6.

There is also a useful homogeneous version with no vacuum shift:
\[
 \boxed{\quad
 \|H^\theta X H^\theta\|_1
       \le\delta^{1-\theta}\|H X H\|_1^\theta
       \le\delta^{1-\theta}(s_\rho^2+s_\sigma^2)^\theta,
       \qquad0<\theta\le1.
 \quad}                                                        \tag{W11}
\]
To prove it, apply exactly W7--W10 first to
\(\min(H,N)+\varepsilon I\), with \(\varepsilon>0\). No lower
bound of one is needed in the bounded strip argument, only strict
positivity. Let \(N\to\infty\), then \(\varepsilon\downarrow0\).
The required Hilbert--Schmidt limits follow from dominated convergence
with a constant multiple of \(1+E^2\). This also defines each
homogeneous sandwich without a formal product-domain assumption.
The case \(\theta=0\) is the ordinary trace norm separately.
W11 deliberately ignores coherences with \(\ker H\) when both
weights are positive; W6 includes them and is useful for the larger
class of forms relative to \(I+H/h_*\).

## 3. Asymmetric trace ideals and the actual threshold

For normal states one obtains a second explicit family of estimates.
Let \(0\le a,b\le1\), \(r=\max(a,b)>0\), and put
\(\alpha=a/r,\beta=b/r\). Then
\[
 \|A^a X A^b\|_1
 \le\delta^{1-r}\|A^\alpha X A^\beta\|_1^r
 \le\delta^{1-r}
       \left(S_\rho^{(a+b)/r}+S_\sigma^{(a+b)/r}\right)^r.       \tag{W12}
\]
Indeed repeat the strip proof with
\(A_N^{\alpha z}X A_N^{\beta z}\) and evaluate at \(z=r\).
The endpoint estimate follows from W4 and the scalar moment bound
\[
 \|A^t\tau^{1/2}\|_2
       =(\operatorname{Tr}\tau A^{2t})^{1/2}\le S_\tau^t,
                                      \quad0\le t\le1,          \tag{W13}
\]
which is Hölder/Jensen for the probability measure \(\mu_\tau^A\).
The cutoff convergence is exactly W10. For positive densities of trace
\(m_\tau\ne1\), replace the right side of W13 by
\(m_\tau^{(1-t)/2}S_\tau^t\); this is the appropriate unnormalized
extension.

Thus \(\max(a,b)<1\) suffices for convergence, including
\[
 \|A^a X\|_1\le\delta^{1-a}(S_\rho+S_\sigma)^a,
                                      \qquad0<a<1.              \tag{W14}
\]
The symmetric half-energy sandwich is therefore a convergence result
under these hypotheses, while a one-sided full \(A X\) is an endpoint.
They are different trace ideals. An exponent exceeding one is not even
guaranteed to define a finite weighted state, as section 6.4 shows.

## 4. Exactly which forms and readouts are controlled

For a bounded operator \(B\) and \(0\le\theta\le1\), define on
\(D(A^\theta)\) the sesquilinear form
\[
 q_B(u,v)=\langle A^\theta u,B A^\theta v\rangle,
 \qquad \langle q_B\rangle_\tau=
                     \operatorname{Tr}B T_\tau(\theta,\theta).
                                                               \tag{W15}
\]
For a positive ensemble decomposition this expectation equals
\(\sum_j t_j q_B(u_j,u_j)\). The sum is absolutely convergent,
bounded by \(\|B\|\operatorname{Tr}\tau A^{2\theta}\), and independent
of the decomposition by W4. This establishes the definition for mixed
states, including states which do not commute with \(H\).
No trace-distance estimate alone was applied to an unbounded observable.

For \(\theta<1\), W6 implies
\[
 |\langle q_B\rangle_\rho-\langle q_B\rangle_\sigma|
            \le\|B\|\delta^{1-\theta}M^{2\theta}.               \tag{W16}
\]
For selfadjoint \(B\), these are real quadratic forms. Because the
balanced weighted difference is selfadjoint, the supremum of the left
side over selfadjoint contractions \(B\) equals its trace norm.
Consequently W16 is a uniform assertion about this entire relative-form
class, including noncommuting forms, rather than only functions of
\(H\). It is also uniform for state-dependent or index-dependent
\(B\)'s with a common norm bound.

An arbitrary bounded \(B\) defines a continuous form in the
\(A^\theta\) graph norm. It need not, without further hypotheses,
define a closed semibounded form or a particular selfadjoint measurement
operator. W15 is a form expectation. Whenever a specified selfadjoint
observable has this form representation and its absolute form
expectation is finite, W15 agrees with its usual expectation. No
measurement implementation is inferred solely from the relative bound.

In particular, an energy-relative form
\(q(u,v)=\langle A^{1/2}u,B A^{1/2}v\rangle\) obeys
\[
 |\langle q\rangle_\rho-\langle q\rangle_\sigma|
                      \le\|B\|M\sqrt\delta.                    \tag{W17}
\]
For a selfadjoint form dominated in absolute value by \(C H\), its
bounded relative representative on \(\overline{\operatorname{Ran}H^{1/2}}\)
has norm at most \(C\), with zero extension on \(\ker H\).
This follows by completing that range in its Hilbert norm: the form
bound descends through the kernel, and the bounded selfadjoint form
representation has norm equal to its numerical radius. Hence W11 gives
the sharper homogeneous bound
\[
 |\langle q\rangle_\rho-\langle q\rangle_\sigma|
                  \le C\sqrt{\delta(s_\rho^2+s_\sigma^2)}.      \tag{W18}
\]

### 4.1 Number and second-quantized current-type observables

For the supplied massive free Fock Hamiltonian
\(H=d\Gamma(e)\), \(e\ge m>0\), the particle number
\(N=d\Gamma(I)\) satisfies \(H\ge mN\). These are strongly
commuting direct-sum operators; their forms have the same inequality.
Thus all states under consideration have finite number mean, and
\[
 |\operatorname{Tr}N(\rho-\sigma)|
             \le \frac1m\sqrt{\delta(s_\rho^2+s_\sigma^2)}.      \tag{W19}
\]
For a bounded selfadjoint one-particle operator \(j\), with
\(\|j\|\le u\), the sectorwise selfadjoint operator
\(J=d\Gamma(j)\) obeys \(|J|\le uN\). On the \(n\)-particle
sector its norm is at most \(un\); it preserves that sector. This
argument does not need \([j,e]=0\). Its quadratic form extends to
\(D(H^{1/2})\) with absolute diagonal bound \((u/m)H\), so
\[
 |\langle J\rangle_\rho-\langle J\rangle_\sigma|
              \le \frac{u}{m}\sqrt{\delta(s_\rho^2+s_\sigma^2)}. \tag{W20}
\]
The observable's spectral absolute expectation is finite because
\(|J|\le uN\). The form expectation above is therefore its ordinary
mean. More general unbounded one-particle forms require an explicit
relative-energy form bound; their inclusion is not automatic.

For example on the continuum scalar positive-polarization carrier,
\(e(p)=\sqrt{m^2+v^2p^2}\). The velocity multiplier
\(j(p)=e'(p)=v^2p/e(p)\) is bounded by \(v\), and W20 applies.
This is a velocity-type example, not an identification of velocity with
the supplied normalized microscopic energy-current generator.

That supplied normalized current can be treated directly. Current C2--C3
give the scalar coefficient symbol
\(k_c(q)=\sin(cq)/c\), with
\(e_c(q)^2=m^2+4v^2\sin^2(cq/2)/c^2\). Therefore
\[
 v^2 k_c(q)^2
  =\frac{4v^2}{c^2}\sin^2(cq/2)\cos^2(cq/2)
  \le e_c(q)^2-m^2\le e_c(q)^2.                                \tag{W21}
\]
The current commutes with the chosen polarization and is scalar on its
positive subspace. Its vacuum-normalized Fock implementation is
\(\mathcal K_c=d\Gamma(k_c)\): second quantization of
\(e^{is k_c}\) implements the real-CAR current group and fixes the
vacuum, which fixes the additive constant. This is compatible with
the current branches in Current C4--C12, where \(k_c=p\).
On each particle sector the triangle inequality in the joint multiplier
representation gives \(|\mathcal K_c|\le H_c/v\). Hence, for two
states compared using that same actual \(H_c\),
\[
 |\langle\mathcal K_c\rangle_\rho-
       \langle\mathcal K_c\rangle_\sigma|
             \le \frac1v\sqrt{\delta(s_\rho^2+s_\sigma^2)}.      \tag{W22}
\]
The continuum low-copy current \(d\Gamma(p)\) obeys the same bound
because \(v|p|\le e(p)\). The unnormalized microscopic current in
Current C3, with the same vacuum normalization, is
\((v^2/c)\mathcal K_c\), so its bound has coefficient
\(v/c\). W22 does not supply a uniform unscaled-current continuum
limit. It also does not transport a state between two different
Hamiltonians without a separate common-carrier comparison.

Fixed finite CAR polynomials, including bounded even local readouts,
already satisfy \(|\operatorname{Tr}OX|\le\|O\|\delta\).
Their norm/dynamical comparisons are separate from the unbounded Fock
number and current means above. Neither type of CAR comparison alone
establishes the full-density trace convergence assumed in W1.

## 5. A sufficient route to the missing endpoint

Bounded second moments alone do not guarantee \(\|A X A\|_1\to0\).
A concrete additional sufficient resource is uniform integrability of
the squared-energy tails of both states. Let
\(P_R=\mathbf1_{[1,R]}(A)\), \(R\ge1\), and define
\[
 t_\tau(R)^2=\operatorname{Tr}\tau A^2\mathbf1_{(R,\infty)}(A).
\]
Factoring \(T_\tau(1,1)=R_\tau R_\tau^*\),
\(R_\tau=A\tau^{1/2}\), gives
\[
 \|T_\tau(1,1)-P_R T_\tau(1,1)P_R\|_1
             \le2S_\tau t_\tau(R).
\]
Indeed subtract the products in two terms, one with
\((I-P_R)R_\tau\) on the left and one on the right, and use the
Hilbert--Schmidt product inequality. The low block is bounded by
\(\|A P_R\|^2\delta\le R^2\delta\). Thus
\[
 \|A X A\|_1\le R^2\delta
                  +2S_\rho t_\rho(R)+2S_\sigma t_\sigma(R).     \tag{W23}
\]
If the two \(S\)'s are uniformly bounded and the two tail suprema
vanish as \(R\to\infty\), first send the density error to zero at
fixed \(R\), then send \(R\to\infty\). The endpoint follows.
Multiplication by the bounded \(A^{-1}\) then also gives the
one-sided endpoint. This tail condition is sufficient, not a necessary
condition for every pair: identical moving states have zero difference
whether or not their tails are uniformly integrable.

For a fixed target \(\sigma\), trace convergence plus
\(\operatorname{Tr}\rho_n A^2\to\operatorname{Tr}\sigma A^2<\infty\)
is another sufficient formulation. For \(R\ge\sqrt2\),
\[
 t_{\rho_n}(R)^2\le
 2\left[\operatorname{Tr}\rho_n A^2-
          \operatorname{Tr}\rho_n\min(A^2,R^2/2)\right].         \tag{W24}
\]
The truncated term converges by ordinary trace duality. Take the
limsup, then \(R\to\infty\), to obtain uniform tails for all
sufficiently late indices. Finitely many earlier states also have
vanishing tails, so W23 applies. Matching second moments of two moving
targets is weaker and does not suffice; section 6.2 has exactly matching
moments and a nonzero endpoint. Common-weight graph convergence of pure
vectors is a further sufficient resource, since
\[
 \bigl\||Au_n\rangle\langle Au_n|-|Au\rangle\langle Au|\bigr\|_1
       \le(\|Au_n\|+\|Au\|)\|A(u_n-u)\|.                      \tag{W25}
\]
No such resource is assumed in the basic theorem.

## 6. Actual even free-Fock controls

### 6.1 Narrow energy packets on one fixed supplied carrier

These are actual normal states in the supplied free-Fock representation,
not finite-dimensional Hamiltonians invented to fit the estimate.
One can fix the continuum \(H=d\Gamma(e)\), or one actual lattice
spacing \(c>0\) with its full-zone free Hamiltonian. In either case
the positive one-particle multiplier is continuous near zero momentum,
has minimum \(m>0\), and every small nonempty momentum interval has an
infinite-dimensional positive-polarization \(L^2\) subspace.

Choose \(\eta_n\downarrow0\) and \(2n\) orthonormal one-particle
modes supported where \(m\le e\le m+\eta_n\). Their normalized
wedge \(\chi_n\) lies in the even \(2n\)-particle sector and has
spectral support for \(H\) in
\([2nm,2n(m+\eta_n)]\). Each such vector lies in every power domain.
The shrinking support does not obstruct orthonormal choices: each
nonempty interval still gives infinitely many \(L^2\) modes.

Let \(\Omega\) be the free vacuum and set
\(E_n=\|A\chi_n\|\to\infty\). Then \(A\Omega=\Omega\),
\(\chi_n\perp\Omega\), and the relative width of the \(A\)-spectral
interval tends to zero. For every fixed \(t\ge0\),
\[
 \frac{\|A^t\chi_n\|}{E_n^t}\longrightarrow1.                  \tag{W26}
\]
This follows by bounding numerator and denominator between the
corresponding powers of the interval endpoints; their ratio tends to
one. No exact eigenvector in continuous momentum spectrum is presumed.

### 6.2 Coherent pairs: optimal interpolation and one-sided failure

Put \(\varepsilon_n=E_n^{-1}\), and define even unit vectors and
their normal pure states by
\[
 \psi_n^\pm=\frac{\Omega\pm\varepsilon_n\chi_n}
                         {\sqrt{1+\varepsilon_n^2}},\qquad
 \rho_n=|\psi_n^+\rangle\langle\psi_n^+|,\quad
 \sigma_n=|\psi_n^-\rangle\langle\psi_n^-|.                      \tag{W27}
\]
Both states are supported in the even sector; mere parity invariance
is not being substituted for even-sector support. A direct rank-two
calculation gives
\[
 X_n=\frac{2\varepsilon_n}{1+\varepsilon_n^2}
       (|\Omega\rangle\langle\chi_n|+|\chi_n\rangle\langle\Omega|),
 \qquad \delta_n=\frac{4\varepsilon_n}{1+\varepsilon_n^2},       \tag{W28}
\]
and
\[
 S_{\rho_n}^2=S_{\sigma_n}^2=\frac2{1+\varepsilon_n^2},\qquad
 M_n^2=\frac4{1+\varepsilon_n^2},\qquad
 \|A X_n A\|_1=M_n^2\longrightarrow4.                          \tag{W29}
\]
The two singular values of a balanced sandwich are each
\(2\varepsilon_n\|A^\theta\chi_n\|/(1+\varepsilon_n^2)\), since
\(A^\theta\chi_n\) is orthogonal to the vacuum. Consequently
\[
 \frac{\|A^\theta X_n A^\theta\|_1}
             {\delta_n^{1-\theta}M_n^{2\theta}}
          =\frac{\|A^\theta\chi_n\|}{E_n^\theta}\longrightarrow1.
                                                               \tag{W30}
\]
For every fixed \(0\le\theta\le1\), the universal constant one
in W6 is asymptotically attained. For \(\theta<1\), its power
\(\delta^{1-\theta}\) cannot be uniformly improved with only the
same bounded second-moment resource. At \(\theta=1\), convergence
fails. Both states have vanishing first free energy:
\[
 \operatorname{Tr}\rho_n H=\operatorname{Tr}\sigma_n H
   \le h_*/E_n\longrightarrow0,\qquad
 s_{\rho_n}^2=s_{\sigma_n}^2\le h_*^2.                          \tag{W31}
\]
Thus these are also actual near-free-ground families, though they are
not asserted to be outputs of the specified ramp and pulse.

The packet estimate W26 is uniform for \(t\in[0,1]\), since the ratio
of its spectral endpoints tends to one. Therefore if
\((1-\theta_n)\log E_n\to\ell<\infty\), the norm in W30's numerator
tends to \(4e^{-\ell}\), not zero. This tests the joint approach to
the endpoint as well. Sharpness here is for the whole bounded relative-
form ball in W16, and does not say that each fixed number or current
observable attains that rate.

For asymmetric exponents the two singular values are instead
proportional to \(\|A^a\chi_n\|\) and \(\|A^b\chi_n\|\):
\[
 \|A^a X_n A^b\|_1=
 \frac{2\varepsilon_n}{1+\varepsilon_n^2}
         (\|A^a\chi_n\|+\|A^b\chi_n\|).                       \tag{W32}
\]
If \(\max(a,b)=1\), this does not tend to zero; if only one
exponent is one the limit is two, and if both are one it is four.
In particular \(\|A X_n\|_1\to2\). For the unshifted one-sided
product \(\|H X_n\|_1\to2h_*\): the vacuum-side term is killed,
and the other term has norm
\(2\varepsilon_n\|H\chi_n\|/(1+\varepsilon_n^2)\), with
\(\|H\chi_n\|/E_n\to h_*\). This is a genuine one-sided energy
endpoint obstruction.

All scalar \(H\)-energy laws of \(\rho_n\) and \(\sigma_n\) are
exactly identical. A spectral function of \(H\) has no matrix element
between the vacuum and a strictly positive \(2n\)-particle energy
packet, so the two coherence signs are invisible to every such law.
Indeed all scalar spectral moments, when finite, agree. Yet W29 is
nonzero. The homogeneous *balanced* sandwich \(H X_n H\) vanishes
for this particular coherent pair, because both weights kill the
vacuum. The next control supplies its separate endpoint failure.

### 6.3 Fixed vacuum target and a homogeneous endpoint failure

Fix an energy scale \(d>0\), set \(L_n=\|H\chi_n\|\), and, for
large \(n\), let \(p_n=d^2/L_n^2\le1\). Define
\[
 \widetilde\rho_n=(1-p_n)|\Omega\rangle\langle\Omega|
                         +p_n|\chi_n\rangle\langle\chi_n|,
 \qquad \widetilde\sigma=|\Omega\rangle\langle\Omega|.          \tag{W33}
\]
They are actual even normal states with
\[
 \|\widetilde\rho_n-\widetilde\sigma\|_1=2p_n\to0,\quad
 \operatorname{Tr}\widetilde\rho_n H^2=d^2,\quad
 \operatorname{Tr}\widetilde\rho_n H\le d^2/L_n\to0,
 \quad \|H(\widetilde\rho_n-\widetilde\sigma)H\|_1=d^2.        \tag{W34}
\]
The shifted endpoint also stays nonzero, asymptotically
\(d^2/h_*^2\). Thus its failure is possible with a fixed target,
not only two moving targets. The high-energy probability disappears
but its second-moment weight does not. At any \(0<\theta<1\), the
homogeneous balanced norm has order \(L_n^{2\theta-2}\), the same
power \(\delta_n^{1-\theta}\) as W11. This supplies sharpness of
that exponent on the same physical state class.

If only a uniform *first* energy mean were assumed, choose instead
\(p_n=d/L_n\) (with consistent energy units). Then the trace error
still vanishes and the first mean is bounded, but the half-energy
balanced norm tends to \(d\), by the narrow-packet property.
This explicitly identifies the role of the second-moment assumption
in W17--W18; a first-mean cap alone cannot replace it.

### 6.4 Higher weights can lack a domain

Fix a nonempty momentum interval on which \(m\le e\le M_0<\infty\).
Choose even normalized \(2n\)-particle wedges \(\zeta_n\) in that
interval. They are mutually orthogonal because their particle numbers
differ, and their total energy lies in \([2nm,2nM_0]\).
Choose positive \(w_n=C/(n^3(\log n)^2)\), \(n\ge2\), with
\(C\) small enough that \(\sum w_n<1\), and form
\[
 \psi=\sqrt{1-\sum_{n\ge2}w_n}\,\Omega+
                               \sum_{n\ge2}\sqrt{w_n}\,\zeta_n.
                                                               \tag{W35}
\]
This is an even unit vector. Particle-sector orthogonality shows
\(\|H\psi\|^2\) is finite, since it is bounded by a constant
times \(\sum 1/(n(\log n)^2)\). For every \(t>1\), however,
\(\|A^t\psi\|^2\) is bounded below by a positive multiple of
\(\sum n^{2t-3}/(\log n)^2=\infty\). Therefore
\(\psi\in D(H)\) but \(\psi\notin D(A^t)\) for every \(t>1\).
The positive density \(|\psi\rangle\langle\psi|\) has a finite
second energy moment but no finite balanced trace-class sandwich at
such a higher exponent. This is a domain failure, not merely a bad
convergence rate.

## 7. Scope, boundary checks, and remaining obligations

The result assumes full density trace convergence on a common carrier
and common nonnegative free Hamiltonian. It neither derives that
topology from convergence of bounded CAR tests nor transfers moments
between unrelated Hamiltonians. If an embedding compares actual
\(H_c\) with a target \(H_0\), the common-weight moment bound must
first be justified in that embedding. The previous energy-law theorem
uses such branch comparisons for scalar energy laws; it is not, by
itself, a proof of every noncommuting weighted density comparison.
An index-dependent common weight for each pair can be used in W6, with
uniform constants, but comparing different readout operators adds its
own operator/form comparison obligation.

The distinction from scalar energy laws is operationally precise:
functions of \(H\) are one commuting class of readouts, while W15
allows all bounded relative matrices \(B\), including off-diagonal
energy coherences. W27 has identical scalar laws but nonzero weighted
coherence. W6 nevertheless yields the stated convergence for every
strictly smaller weight because full trace convergence is also given.
There is no claim that the weighted trace norm itself is a probability
metric or a prescribed single measurement.

The negative statements are confined to the displayed state classes
and hypotheses. The following checks make their scope explicit.

| Boundary check | Outcome in this derivation |
|---|---|
| Alternative routes | Cutoff interpolation proves every strict subendpoint; squared-energy uniform tails, fixed-target second-moment convergence, or graph convergence recover the endpoint. |
| Independence of walls | One-sided failure, shifted balanced failure, homogeneous balanced failure, and higher-weight domain failure are computed separately; the coherent pair is not misused for its vanishing homogeneous sandwich. |
| Hidden assumptions | Positivity, full trace convergence, common weight, uniform second moments, and a fixed exponent are explicit; no commutation of the states with the energy is assumed. |
| Residual matching | The exact coherent rank-two singular values saturate the stated W6 constant and exponent; the rare mixture tests W11's exponent and fixed-target endpoint. |
| Rhetoric check | These are insufficiency results for a bounded state class, not a global dynamical no-go, a failure of every preparation, or a physical prediction. |
| Partial closure | Energy-relative form means, number means, normalized-current means and all strict weighted trace ideals are positively controlled. |
| Strongest competing case | Endpoint resources are displayed in W23--W25; a fixed pulse with stronger graph preparation can satisfy them and evade the counterfamilies. |
| Repetition/independence | Reuse of the same supplied Fock carrier and the same selected model is disclosed; no extra independent vote or formal proof status is claimed. |

Every constructed state is supported on the actual even Fock sector.
Allowing increasingly many particles or increasingly fine momentum
profiles is part of the broad normal-state class. Those resources are
not claimed to arise from a fixed finite-hull local preparation or a
fixed finite pulse. Establishing or excluding such a protocol is an
additional, unperformed task. Likewise W21--W22 use the supplied current
normalization; no unscaled uniform-current limit is smuggled into them.

## 8. Source and exposure record

The neutral source scope was sealed before any new source reads at
`energy_weighted_trace_independent/PLAN_SEAL.json`. The seal candidly
records that interpolation/cutoff and even-Fock routes were considered
before the written scope seal without new scientific-source exposure;
it is not claimed to be pristine method preregistration. The only
scientific source files admitted for this task are:

| Exact source | SHA-256 | Role and coverage |
|---|---|---|
| `ENERGY_DISTRIBUTION_LIMIT_INDEPENDENT.md` | `4ab02757ff0be403b15d41779a04ca596436bc62240dbc027c01ac6d0fb78abc` | Prior complete 944-line author read reused; refreshed lines 19--79 and 688--774 for moments/carrier and distinction from protocol controls. |
| `LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa` | Scoped prior coverage reused; fresh exact reads 102--140, 184--235, 339--378 for bounded fields, massive multiplier, and positive Fock Hamiltonian. |
| `CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff` | Fresh exact read 94--233 for actual dispersion/current normalization, branch coordinates, polarization and current implementation. No unrelated conclusions imported. |

An initial targeted `rg` extract over these three exact snapshots is
recorded separately; it is not represented as a complete read of either
Current or Local. Governing workflow/skill instructions previously read
in full are reused at unchanged identities. The checkout `AGENTS.md`
was a pointer to a Git-only instruction body; that body was not fetched,
consistent with the no-Git scope, and the prior caveat remains explicit.

The analytic argument above is self-contained; no external mathematical
source, Lean file, scientific program, solver, or numerical experiment
was needed. File scripts perform only manifests, source hashes, copies,
line counts and freeze bookkeeping. No root probe or seal for this
weighted task, checkpoint, new candidate, publication package, other
chat, repository mutation, or delegation was used. Complete author
coverage, exact source/snapshot checks and the final frozen copy are in
`energy_weighted_trace_independent/`. Source-exposed comparison remains
an outstanding independent step after this freeze; no outcome of it is
presumed here.

## Preserved native weighted-density composition

The following is the complete 155-line root addendum, originally SHA-256
`62d98c8f61c8bb842daa3713e6fc46b08c795224073656295d517e7aa280a004`.
Its opening review status is historical. Its later source-exposed comparison
uses the separately frozen weighted derivation and the energy-law bridge.
Only its scalar-W2 comparison wording is qualified; N1--N8 are untouched.
No second independent native theorem is claimed.

# Actual energy-weighted density transfer

Unreviewed root addendum. It uses the proposed interpolation statement in
ENERGY_WEIGHTED_TRACE_ROOT_PROBE.md (7d52417c) and the already independently
compared actual commuting energy bridge in the energy-law sources
4ab02757/92a80fb5. The interpolation statement is still undergoing an
independent derivation; neither it nor this composition is formally verified.

This addresses an observable class that scalar energy laws do not describe:
bounded coefficients between square-root energy weights, including energy
coherences. It is a conditional mathematical observable class, not a claim
that every native current or laboratory detector has that representation
with a converging bounded coefficient.

## 1. Actual placement and hypotheses

Let rho_c be an actual normal density, placed on the common carrier by the
physical Fock isometry iota_c. Let rho_0 be a low continuum density with high
vacuum, placed as rho_0 tensor |Omega_H><Omega_H|. Assume the full placed
trace error alpha_c tends to zero and

    S_c^2=Tr rho_c H_c^2,  S_0^2=Tr rho_0 H_0^2

are finite. Convergence will use uniform bounds on these quantities. All
moments are spectral moments; no D(H_c^2) assumption on state vectors is
made. On the actual physical range define L=H_0 tensor I_H. It strongly
commutes with H_c and satisfies the checked inequalities

    0<=L<=H_c,
    0<=H_c-L<=kappa_c H_c^2,
    kappa_c=c/(2v)+1/Lambda_c.                                    (N1)

Thus M_c=Tr rho_c H_c<=S_c and M_L=Tr rho_c L<=M_c. Put
delta_E=Tr rho_c(H_c-L)<=min(M_c,kappa_c S_c^2).

Define the positive trace-class weighted density by a Hilbert-Schmidt
factorization, not by an unjustified unbounded trace cycle:

    Gamma_c=iota_c[(1+H_c)^(1/2)rho_c^(1/2)]
                    [(1+H_c)^(1/2)rho_c^(1/2)]*iota_c*,
    Gamma_0=[(1+H_0)^(1/2)rho_0^(1/2)]
                    [(1+H_0)^(1/2)rho_0^(1/2)]* tensor P_H.       (N2)

Their traces are 1+M_c and 1+M_0. These are weighted positive operators,
not normalized density matrices. No Hamiltonian value on an artificial
outside-band extension is used in Gamma_c.

## 2. Separating native energy from the common low weight

On the actual joint spectrum x>=y>=0,

    (sqrt(1+x)-sqrt(1+y))^2<=x-y.                                  (N3)

Apply this to the Hilbert-Schmidt columns A=(1+H_c)^(1/2)rho_c^(1/2) and
B=(1+L)^(1/2)rho_c^(1/2), with their common isometric placement. N3 and
monotone spectral cutoff limits give

    ||A-B||_HS<=sqrt(delta_E),
    ||A||_HS=sqrt(1+M_c),  ||B||_HS=sqrt(1+M_L).

The trace-ideal product estimate and the identity
AA*-BB*=(A-B)A*+B(A*-B*) give

    ||Gamma_c-(1+L)^(1/2)rhohat_c(1+L)^(1/2)||_1
       <=[sqrt(1+M_c)+sqrt(1+M_L)]sqrt(delta_E).                    (N4)

The middle expression is again defined by its positive factorization.
Strong commutation is needed in N3; no square-root Lipschitz claim is made
for arbitrary noncommuting Hamiltonians.

On the full common carrier put W=1+L. The proposed interpolation lemma at
theta=1/2, applied to rhohat_c and rhohat_0, gives

    ||W^(1/2)(rhohat_c-rhohat_0)W^(1/2)||_1<=sqrt(alpha_c B_c),
    B_c=Tr rhohat_c W^2+Tr rhohat_0 W^2
       <=(1+S_c)^2+(1+S_0)^2.                                    (N5)

Here L^2<=H_c^2 follows from the actual joint multiplication calculus,
not from squaring a general noncommuting operator inequality. Combining
N4-N5 produces the conditional estimate

    ||Gamma_c-Gamma_0||_1
      <=[sqrt(1+M_c)+sqrt(1+M_L)]sqrt(delta_E)
                      +sqrt(alpha_c B_c)
      <=2 S_c sqrt((1+S_c)kappa_c)
           +sqrt(alpha_c[(1+S_c)^2+(1+S_0)^2]).                    (N6)

Thus uniform second moments and the full trace limit would imply convergence
of these actual energy-weighted positive operators in trace norm. Actual
second-moment convergence is not asserted. The W2 endpoint for scalar energy
laws is a separately justified conclusion under the stated moment/graph
resources. There is no unconditional strength ordering between these
topologies. N6 is consistent with the known counterexamples to that endpoint.

## 3. What form readouts follow

Let C_c,C_0 be specified bounded common-carrier coefficient operators with
||C_0||<=a and ||C_c-C_0||<=epsilon_c. They may be selfadjoint when real-valued
readouts are intended. The actual quadratic form on D(H_c^(1/2)) is

    q_c[psi]=<iota_c(1+H_c)^(1/2)psi,
                        C_c iota_c(1+H_c)^(1/2)psi>.

Its normal-state expectation is Tr C_c Gamma_c, and the target is defined
with H_0 and C_0. This definition needs no choice of a selfadjoint operator
representing an indefinite form. From N6,

    |Tr C_c Gamma_c-Tr C_0 Gamma_0|
       <=a ||Gamma_c-Gamma_0||_1+epsilon_c(1+M_c).                  (N7)

For common C this is uniform on the bounded coefficient unit ball, including
off-diagonal energy coherences. C=I gives total first-energy convergence.
Native one-particle currents, spatial energy densities and inserted histories
still require an explicit coefficient representation and its comparison;
neither boundedness of the source nor its name supplies epsilon_c->0.
An energy-weighted norm limit is not a claim about quadratic energy readouts.

## 4. Actual even-state diagnostic for the square-root loss

For small c choose two orthonormal positive-polarization high modes with
compact current-momentum support in fixed bounded intervals, and let chi_c
be their normalized two-particle wedge. It is an actual even vector with
no low particles. The exact high-branch dispersion gives constants
0<a<b<infinity independent of c with

    a/c <= H_c <= b/c

on its joint spectral support. Let E2_c=||H_c chi_c|| and r_c=1/E2_c, which
is less than one eventually, and put

    psi_c=sqrt(1-r_c^2)Omega+r_c chi_c.

This pure density has actual second moment exactly one and full trace
distance 2r_c=Theta(c) from vacuum. Its low partial density is exactly the
vacuum. Its actual mean energy tends to zero at order c.

The off-diagonal vacuum-to-pair block of Gamma_c is
r_c sqrt(1-r_c^2)|Omega><(1+H_c)^(1/2)chi_c|, plus its adjoint. Testing
Gamma_c-P_Omega against the norm-one even operator that swaps Omega with
the normalized vector (1+H_c)^(1/2)chi_c gives the lower bound

    ||Gamma_c-P_Omega||_1
      >=2r_c sqrt(1-r_c^2)||(1+H_c)^(1/2)chi_c||=Theta(sqrt(c)).     (N8)

The diagonal remainder is only O(c), so factorization also gives a matching
O(sqrt(c)) upper bound. This is an actual spacing-dependent state family and
a spacing-dependent bounded test in a uniform norm claim. It is not a fixed
ordinary-cell pulse protocol, nor a counterexample for every fixed readout.
The common low-weighted difference for this family is only Theta(c), since
L is zero on both vacuum and the high pair. Thus the native energy weight
in N4 contributes a real additional coherence cost.

No formal analytic certificate or independent check of this new addendum has
yet been supplied. Pending obligations are the interpolation premise, actual
carrier/trace-ideal composition and witness normalization. Frozen parents and
the original weighted-trace root remain unchanged.

## Preserved complete normalized-current proof and composition check

The following complete 502-line body is byte-exact. It contains the actual
low/high estimates, bounded spectral-ratio interpretation, the free-hold
consequence, and the interacting countercontrol. The older 133-line root
and matching seal are historical evidence, not a replacement for this body.

# Normalized-current transfer: source-exposed composition check

This checks all 133 lines of the authorized normalized-current root addendum
129a1af7 against the unchanged named parents. It is a source-exposed
composition check, not a new pre-exposure independent derivation, a
model-diverse review, a formal verification, or a retained-status audit.
The source scope was sealed before the new addendum and its seal were read.

**Disposition.** No formula repair is required in J1--J9. The root's
conditional normalized-current mean comparison, its order-\(c\) high-sector
control, and its scoped unscaled-current counterexample are valid with the
actual supplied Fock placement and moment conventions. The inverse-energy
notation in J6 denotes a bounded spectral ratio/closure, as detailed below;
it need not be a raw everywhere-defined product of unbounded operators.
The high-sector example proves the order, not optimality of J4's coefficient.

There is also a valid additional consequence: after a finite comparison
stage, subsequent genuinely free holds preserve each of the two current
means exactly, for arbitrary different finite hold durations. Consequently
the already established mean comparison survives durations growing without
bound along a spacing sequence. This needs strong commutation with each
actual hold generator; it does not imply growing-time density convergence
or apply automatically to a hold generated by an interacting Hamiltonian.
Section 7 gives a bounded even CAR interaction for which the current changes.

## 1. Exact sources and correspondence

The new scientific source is
NORMALIZED_CURRENT_TRANSFER_ROOT_ADDENDUM.md, SHA256
129a1af703261521627e56786fa2bed2a31d494940a13a8d29dd672a1c63f472,
133 lines, 6593 bytes. Its matching .seal.json is SHA256
1fc4a374f6903dfe183747196ae57f6271ae0ed43b4e8eb61e834b69a2a2bb9e,
15 lines, 664 bytes. Both were read completely; the seal's body identity
matches. A matching identity records provenance, not truth of the argument.

The unchanged scientific parents used here are:

- ENERGY_WEIGHTED_TRACE_INDEPENDENT.md, 7c9df64640d1296f2dc8a6d1a522652d0f766fdad769b14ec303f38dd8b6ff23, 632 lines.
- ENERGY_WEIGHTED_TRACE_CROSSCHECK.md, 202b44242e9f9b1d8ba8e93302745e3c91425aa4a63b6b599850cb8f12de02e7, 584 lines.
- ENERGY_DISTRIBUTION_LIMIT_INDEPENDENT.md, 4ab02757ff0be403b15d41779a04ca596436bc62240dbc027c01ac6d0fb78abc, 944 lines.
- Current: CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md, 763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff, 601 lines.
- Local: LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md, b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa, 731 lines.

The three earlier complete derivations/comparisons retain their prior full
coverage. Current and Local retain their prior scoped premise coverage;
this check does not claim an independent audit of their entire notes.
Current section 6's reflection convention was also read directly again.
Exact coverage, chronology, byte identities, immutable input snapshots and
the final seal are in the accompanying evidence directory.

| Root lines | Assertion checked | Check below |
| --- | --- | --- |
| 1--8 | Conditional source-exposed status and readout scope | Sections 1, 8 |
| 10--29 | Actual C3/C12 current, polarization, normalization, reflection | Section 2 |
| 31--43 | State placement, moments and low-density premise | Sections 2--4 |
| 45--62 | J3/J4 high-sector spectral inequalities and coefficient | Section 3 |
| 64--83 | J5/J6 partial trace, domains and relative form | Section 4 |
| 85--94 | J7 convergence and time-window qualification | Sections 5--6 |
| 96--123 | J8/J9 actual even witness and unscaled boundary | Section 5 |
| 125--133 | Imported lemmas and conditional scope | Sections 1, 8 |

No kinetic/potential/finite-order candidate, Lean or symbolic result,
publication package, checkpoint, queue, or other newly forbidden source was
read. This document changes no parent note, original freeze, canonical
repository file, instruction or prompt. All calculations below are symbolic.

## 2. Actual current, Fock normalization and carrier

Fix \(m,v,c>0\). On the positive-polarization one-particle spaces in
Current C8, both copies have momentum coordinate
\(p\in I_c=(-1/c,1/c)\). Write their actual positive free energies as
\(e_{c,L}(p)\) and \(e_{c,H}(p)\), and put
\[
 E(p)=\sqrt{m^2+v^2p^2},\quad
 \Lambda_c=\sqrt{m^2+2v^2/c^2},\quad
 U_c=\sqrt{m^2+4v^2/c^2}.
\]
The branch change of variables in C4 gives
\[
 e_{c,L/H}(p)^2
 =m^2+\frac{2v^2}{c^2}\left(1\mp\sqrt{1-c^2p^2}\right).
 \tag{C1}
\]
In particular
\[
 E\le e_{c,L},\qquad \Lambda_c\le e_{c,H}\le U_c.
 \tag{C2}
\]
For the first inequality use
\(2(1-\sqrt{1-x})\ge x\), \(0\le x<1\).
These are actual multiplication operators, not a dispersion assigned
arbitrarily to the complement of the physical range.

Current C3 normalizes the actual current coefficient to
\(k_c(q)=\sin(cq)/c\). Current C4 and C12 take this symbol to \(p\) on
both branches. It commutes with the positive polarization. Its real-CAR
group is implemented on the positive Fock space by
\(\Gamma(e^{is k_c})\), whose vacuum is fixed. The selfadjoint Fock
generator is consequently
\[
 K_c=d\Gamma(p_L\oplus p_H)=K_L+K_H,\qquad
 P_{\mathrm{actual},c}=\frac{v^2}{c}K_c.
 \tag{C3}
\]
The vacuum convention fixes the additive constant to zero. This is the
current generator selected in C3, not the geometric lattice momentum \(q\).
The sign here is the sign of the supplied coefficient group and its Fock
implementation; changing a Schrödinger/Heisenberg evolution convention
does not change this operator identification.

The one-particle estimate
\[
 v^2 k_c(q)^2
 =\frac{4v^2}{c^2}\sin^2(cq/2)\cos^2(cq/2)
 \le e_c(q)^2
\]
and the sectorwise triangle inequality imply
\[
 |K_c|\le H_c/v,\qquad H_c=d\Gamma(e_{c,L}\oplus e_{c,H}).
 \tag{C4}
\]
All these comparisons are spectral comparisons of strongly commuting
multiplication operators. They need no commutation of the density with
those operators.

The physical envelope convention in Current section 6 reflects the high
coordinate. It writes the same current as \(p\oplus(-p)\) and also
reflects the high state. Its absolute estimates are unchanged. The signed
positive-current example below is in C8 coordinates throughout; one must
not reflect its operator without reflecting its state.

The standard Fock splitting identifies the physical space with low and
high Fock factors. Its isometric placement \(\iota_c\) into the two full
continuum factors places both missing momentum bands in vacuum. The
fermionic graded convention has no effect on the even, number-preserving
Hamiltonians or currents here. Given a positive normal density \(\rho_c\),
let
\[
 \widehat\rho_c=\iota_c\rho_c\iota_c^*,\qquad
 \lambda_c=\operatorname{Tr}_{H}\widehat\rho_c .
 \tag{C5}
\]
These are positive trace-one operators. No parity restriction is needed.
On the physical range define
\[
 L=H_0\otimes I_H,\qquad H_0=d\Gamma(E),\qquad K_0=d\Gamma(p).
\]
The band subspaces reduce \(H_0\) and \(K_0\). On that range \(L\)
strongly commutes with the placed \(H_c\), \(0\le L\le H_c\), and
\(K_0\otimes I_H\) restricts exactly to the placed \(K_L\).
This exact low-current identity is stronger than convergence of some
relative-current coefficients; the latter is not needed for J7.

## 3. High-current bound with all moment domains

For any positive normal density \(\rho\), the convention
\(\operatorname{Tr}\rho H^2<\infty\) means its nonnegative spectral
integral. Equivalently \(H\rho^{1/2}\) has a Hilbert-Schmidt extension
with squared norm equal to that integral. A pure vector therefore needs
to be in \(D(H)\), not \(D(H^2)\). The statements extend to arbitrary
normal mixed states by their positive spectral decompositions or,
equivalently, monotone spectral truncation. No trace-distance estimate
alone is used to control these moments.

Set
\[
 S_c^2=\operatorname{Tr}\rho_c H_c^2,\qquad
 S_0^2=\operatorname{Tr}\rho_0 H_0^2,\qquad
 \alpha_c=\|\lambda_c-\rho_0\|_1.
 \tag{C6}
\]
First moments are finite, with
\(\operatorname{Tr}\rho_c H_c\le S_c\) and similarly for \(\rho_0\).
Thus (C4) already makes the entire actual current mean absolutely
defined.

In the joint particle/momentum representation, the integer high particle
number \(N_H\) obeys
\[
 |K_H|\le N_H/c,\quad H_c\ge\Lambda_c N_H,\quad N_H^2\ge N_H.
\]
Squaring is permissible here because the first energy inequality is a
pointwise joint spectral inequality. It is not the invalid operation of
squaring a general noncommuting operator inequality. Consequently
\[
 H_c^2\ge\Lambda_c^2 N_H^2\ge\Lambda_c^2 N_H,
\]
so positivity and monotone integration against \(\rho_c\) give
\[
 |\operatorname{Tr}\rho_c K_H|
 \le\operatorname{Tr}\rho_c|K_H|
 \le \frac{S_c^2}{c\Lambda_c^2}
 =\frac{c S_c^2}{m^2c^2+2v^2}.
 \tag{C7}
\]
This proves J4 with its stated constant for all such normal densities.
No step assumes that \(\rho_c\) is diagonal in energy or particle number.
The estimate bounds the absolute spectral mean, including for coherences.

For completeness, \(H_H\le H_c^2/\Lambda_c\): on the high vacuum both
sides have the appropriate inequality; off it \(H_H\ge\Lambda_c\),
so \(H_H\le H_H^2/\Lambda_c\le H_c^2/\Lambda_c\).
Together with \(|K_H|\le H_H/v\) this gives the root's coarser coefficient
\(1/(v\Lambda_c)\). The ratio of the sharper coefficient to this one is
\(v/(c\Lambda_c)\le1/\sqrt2\). Neither statement needs even support.

## 4. Partial trace and the low relative form

Because \(L\) and the actual \(H_c\) strongly commute on the physical
range, \(L^2\le H_c^2\). To pass to the partial trace, use the bounded
positive low operators
\[
 b_R=\min(H_0^2,R).
\]
By the defining bounded-operator identity for partial trace,
\[
 \operatorname{Tr}\lambda_c b_R
 =\operatorname{Tr}\widehat\rho_c(b_R\otimes I_H)
 \le S_c^2.
\]
Monotone convergence as \(R\to\infty\) yields
\[
 s_{\lambda_c}^2:=\operatorname{Tr}\lambda_c H_0^2\le S_c^2.
 \tag{C8}
\]
This proves J5 without cycling an unbounded operator through a trace.
It also shows that the full low density has the moment needed by W18.
The physical-range restriction is essential for the comparison with
\(H_c\); no Hamiltonian on the unused complement has been introduced.

On a low occupation configuration with total energy \(h\) and total
current \(k\),
\[
 |k|\le\sum_j|p_j|\le h/v.
\]
Let \(B\) be multiplication by \(k/h\) on the nonvacuum configurations
and zero on the vacuum. It is a bounded selfadjoint operator of norm
at most \(1/v\). Thus on \(D(H_0^{1/2})\),
\[
 q_{K_0}(u,w)=\langle H_0^{1/2}u,BH_0^{1/2}w\rangle.
 \tag{C9}
\]
It agrees with the spectral quadratic form of \(K_0\). Although that
spectral form may have a larger natural domain, the displayed domain
is sufficient. The notation \(H_0^{-1/2}K_0H_0^{-1/2}\) in J6 is
this bounded ratio, or the closure of that product from a joint spectral
core. The spectral gap makes the inverse square root bounded off the
vacuum, but does not by itself make every raw unbounded product
everywhere defined. This domain interpretation, rather than an additional
scientific hypothesis, is the necessary reading of J6.

For \(X=\lambda_c-\rho_0\), the homogeneous half-weight consequence
W11/W18 of the frozen weighted proof states
\[
 \|H_0^{1/2}XH_0^{1/2}\|_1
 \le \sqrt{\alpha_c(s_{\lambda_c}^2+S_0^2)}.
 \tag{C10}
\]
Here the sandwich is the difference of the positive trace-class
operators defined by the Hilbert-Schmidt factors
\(H_0^{1/2}\lambda_c^{1/2}\) and \(H_0^{1/2}\rho_0^{1/2}\);
it is not assumed to be a naive everywhere-defined algebraic product.
The already checked interpolation proof allows noncommuting densities.
Finite second moments supply its endpoint resource, while trace
distance supplies its unweighted endpoint. This does not assert that
trace convergence controls unbounded energy without that resource.

Trace duality with bounded \(B\), (C8) and (C10) now give
\[
 |\operatorname{Tr}K_0(\lambda_c-\rho_0)|
 \le\frac1v\sqrt{\alpha_c(S_c^2+S_0^2)} .
 \tag{C11}
\]
Both separate means are absolutely defined because \(|K_0|\le H_0/v\).
Their spectral means equal their form means in (C9): apply bounded
spectral cutoffs and dominated convergence using the finite absolute
means. The same procedure for the exact restriction \(K_0\otimes I=K_L\)
proves
\(\operatorname{Tr}\rho_c K_L=\operatorname{Tr}\lambda_c K_0\).
Thus J6 has no hidden unbounded cyclic-trace step and no pure-state
restriction. It is the homogeneous relative-energy form theorem, not
the shifted-weight native transfer estimate, that supplies its constant.

## 5. J7, convergence, and the actual high-pair test

Adding (C7) and (C11) proves exactly the root result
\[
 |\operatorname{Tr}\rho_cK_c-\operatorname{Tr}\rho_0K_0|
 \le
 \frac{cS_c^2}{m^2c^2+2v^2}
 +\frac1v\sqrt{\alpha_c(S_c^2+S_0^2)} .
 \tag{C12}
\]
Uniform boundedness of \(S_c,S_0\) and \(\alpha_c\to0\) imply convergence.
For families with varying moment resources the displayed two terms
themselves give a more general sufficient condition. Uniform versions
over a specified time window require uniform versions of these same
hypotheses there. J7 does not produce a density or moment theorem.

A full placed-density trace-convergence assumption is unnecessary for
this proof. A stronger full comparison implies low convergence by
contractivity of partial trace, but CAR-word convergence alone does not
imply the \(\alpha_c\) premise. Scalar energy-law convergence is also
not a substitute: it can lose current-sign information, coherences and
placement information. The distinction is logical, not a claim that
the supplied protocol cannot establish the necessary premises.

To check sharpness of the high-sector order, fix \(0<a<b<1\).
Choose orthonormal smooth high positive-polarization packets
\(u_c,w_c\) with disjoint momentum supports in \((a/c,b/c)\).
The nonzero positive-polarization high space admits these packets.
Their normalized wedge \(\chi_c=u_c\wedge w_c\) is an actual even
two-particle vector with low vacuum. Its momentum support gives
\[
 2a/c\le K_H\le2b/c,\qquad 2\Lambda_c\le H_c\le2U_c
 \quad\hbox{on that support}.                              \tag{C13}
\]
The energy assertion follows from (C1), not from a hypothetical state
in the unused momentum complement. For each \(c\), the vector is in
every free-energy power domain, since its particle number is two
and its momentum support is compact.

For fixed \(s_*>0\), take sufficiently small \(c\) and define
\[
 p_c=\frac{s_*^2}{\|H_c\chi_c\|^2},\quad
 \rho_c=(1-p_c)P_\Omega+p_cP_{\chi_c},\quad \rho_0=P_{\Omega_L}.
 \tag{C14}
\]
Then \(0<p_c<1\), \(S_c^2=s_*^2\), \(S_0=0\), and \(\alpha_c=0\).
The state is supported in the even sector. Explicit bounds are
\[
 \frac{s_*^2}{4U_c^2}\le p_c\le\frac{s_*^2}{4\Lambda_c^2},
\]
\[
 \frac{a s_*^2 c}{2(m^2c^2+4v^2)}
 \le\operatorname{Tr}\rho_cK_c
 \le\frac{b s_*^2 c}{2(m^2c^2+2v^2)} .                       \tag{C15}
\]
Thus its positive current is \(\Theta(c)\). This verifies J8/J9 and
rules out an \(o(c)\) high-sector bound from these state-class premises
alone, even with an exact low vacuum. It does not prove the numerical
constant in J4 optimal, and does not assert sharpness of every term
for every fixed preparation.

Multiplying (C15) by \(v^2/c\) gives
\[
 \liminf_{c\to0}\operatorname{Tr}\rho_cP_{\mathrm{actual},c}
 \ge a s_*^2/8>0,\qquad
 \limsup_{c\to0}\operatorname{Tr}\rho_cP_{\mathrm{actual},c}
 \le b s_*^2/4.                                             \tag{C16}
\]
The target vacuum has zero current. A unique nonzero limit is not
needed for this counterexample. In fact the actual full trace distance
to vacuum is \(2p_c=\Theta(c^2)\), and the actual first free energy is
\(\Theta(c)\). Even those stronger near-vacuum properties do not repair
the unscaled-current inference under the same bounded second moment.

This is a spacing-dependent actual Fock state family. No realization by
a fixed local ramp, finite pulse or insertion is asserted. It refutes
only a state-class implication and leaves stronger preparation rates,
fixed-protocol constraints, and direct unscaled-current theorems open.

## 6. Additional consequence: arbitrary free holds preserve the comparison

Suppose the finite preparation/comparison stage supplies densities
\(\eta_c,\eta_0\) for which (C6) and (C12) hold, with constants evaluated
at that stage. Subsequently suppose that their exact generators are
respectively the free \(H_c,H_0\). Both supplied currents strongly
commute with their own free Hamiltonians: they are sectorwise joint
multipliers in the same occupation representation.

More generally, if selfadjoint \(K,H\) strongly commute, then for every
Borel set \(A\),
\[
 e^{itH}E_K(A)e^{-itH}=E_K(A).
\]
For any normal density \(\eta\) and any real finite \(t\), bounded trace
cyclicity therefore gives
\[
 \operatorname{Tr}\bigl(e^{-itH}\eta e^{itH}E_K(A)\bigr)
 =\operatorname{Tr}\eta E_K(A).                              \tag{C17}
\]
The whole current spectral measure is unchanged. If its absolute first
moment is finite at the start, it remains finite and its mean is exactly
unchanged. This reasoning avoids cycling an unbounded current through a
trace, works for noncommuting mixed densities, and preserves its domain
requirements. Here finiteness follows from (C4) or \(|K_0|\le H_0/v\).
Free-energy second moments are conserved as well.

Consequently, for arbitrary different finite durations \(t_c,t_0\),
\[
 \begin{split}
 &\operatorname{Tr}\bigl(e^{-it_cH_c}\eta_c e^{it_cH_c}K_c\bigr)
 -\operatorname{Tr}\bigl(e^{-it_0H_0}\eta_0 e^{it_0H_0}K_0\bigr)\\
 &=\operatorname{Tr}\eta_cK_c-\operatorname{Tr}\eta_0K_0 .
 \end{split}                                                \tag{C18}
\]
The absolute value is bounded by (C12), with the initial comparison-stage
\(\alpha_c,S_c,S_0\). The durations may depend independently on \(c\),
on a weak-source parameter, or on a preparation parameter; they may
diverge along a sequence. There is no need to compare densities at the
later times or to establish a growing-time propagator approximation.
Each duration is a real finite number; this does not postulate a unitary
at time infinity.

The same conclusion holds after arbitrary finite starting times once
the two free holds begin. In a joint weak-source limit it preserves
whatever initial mean estimate has actually been proved. Conservation
does not improve that initial rate: for example, an \(o(g^2)\) initial
mean error remains \(o(g^2)\), while mere \(o(1)\) is not thereby upgraded.
For the normalized-current convergence proved here, the initial
right-hand side of (C12) tending to zero suffices.

This is conservation of one observable (indeed its own spectral law)
under separate evolutions. It asserts neither full-density convergence
at the two later times nor convergence of their current distributions
to each other unless a separate initial distribution comparison exists.
A formal commutator on an unspecified common core is insufficient:
strong commutation, or another proved conservation theorem with adequate
domains, is the hypothesis used in (C17).

## 7. Why an interacting hold needs an additional argument

If the full hold generator is \(G=H+V\), commutation of \(K\) with the
free part \(H\) alone does not prove conservation under \(G\). One
would need commutation with \(G\), or an independently controlled
current variation. Even bounded, parity-preserving, domain-regular
CAR interactions can change this current.

Here is a concrete check on the supplied continuum free Fock carrier.
Choose orthonormal smooth positive-polarization packets \(u,w\) with
compact disjoint supports in a positive momentum interval. Put
\[
 \chi=a^*(u)a^*(w)\Omega,\quad
 A=a^*(u)a^*(w),\quad V=\gamma(A+A^*),\quad \gamma\in\mathbb R\setminus\{0\}.
\]
Then \(\|\chi\|=1\), \(k=\langle\chi,K_0\chi\rangle>0\);
\(V\) is a bounded selfadjoint even CAR polynomial, with
\(V\Omega=\gamma\chi\) and \(V\chi=\gamma\Omega\).
The compact momentum supports make \(\chi\) belong to every power
domain of \(H_0\) and \(K_0\). Moreover the finite-particle core formulas
\[
 [K_0,A]=a^*(pu)a^*(w)+a^*(u)a^*(pw),\qquad
 [H_0,A]=a^*(Eu)a^*(w)+a^*(u)a^*(Ew)
\]
have bounded right-hand sides. Closure gives the usual operator-domain
preservation and bounded commutators; no singular source is being used.

The bounded perturbation \(G=H_0+V\) is selfadjoint on \(D(H_0)\).
Take the even initial unit vector
\(\psi=(\Omega+i\chi)/\sqrt2\). It lies in \(D(G^2)\):
\(H_0\psi\) and \(V\psi\) both lie in \(D(H_0)\).
Since \(|K_0|\le H_0/v\), differentiability of \(e^{-itG}\psi\)
in the graph norm of \(G\) implies the needed differentiability in
the \(K_0\) graph norm at zero. With the inner product linear in its
second entry, direct differentiation gives
\[
 \left.\frac{d}{dt}
 \langle e^{-itG}\psi,K_0e^{-itG}\psi\rangle\right|_{t=0}
 =i\langle\psi,[G,K_0]\psi\rangle
 =-\gamma k\ne0.                                             \tag{C19}
\]
The free contribution vanishes by strong commutation. For the remaining
term,
\(\langle\psi,VK_0\psi\rangle=i\gamma k/2\) and
\(\langle\psi,K_0V\psi\rangle=-i\gamma k/2\).
These quantities are defined on the just specified domains, so (C19)
is not a formal manipulation.

This example shows precisely why a generic interacting-baseline hold
cannot inherit (C18) merely because its free current is conserved by
the free Hamiltonian. It does not say every interaction changes current:
a genuinely conserved current for the full generator would still be
constant. Nor is this example claimed to be a particular fixed local
preparation from another note; it is an actual bounded even CAR
state/generator countercontrol on the allowed carrier.

## 8. Scope, repairs and remaining obligations

All J1--J9 formulas survive this source-exposed check. The bounded
spectral-ratio interpretation of J6 supplies its rigorous form meaning;
the explicit constants in (C15)--(C16) substantiate the root's rate and
unscaled boundary. The extra free-hold result is (C18), conditional on
the actual subsequent generators and strong commutation. Equation (C19)
prevents extending it to an interacting baseline without a new argument.

The report imports the frozen weighted interpolation theorem with its
checked hypotheses. It does not establish an additional independent
pre-exposure weighted proof, certify every Current/Local parent claim,
or convert their conditional/open_gate status into retained status.
No claim follows from matching hashes alone.

For an actual preparation or finite-pulse application, the remaining
obligations are to supply the precise low-density trace comparison and
actual free-energy second-moment bounds at the comparison stage, and to
identify the true generators of any later holds. A bounded-orbit CAR
comparison alone does not discharge the density premise. Interacting
holds need a full-generator conservation or variation estimate.
Unscaled-current convergence needs stronger hypotheses than the
state-class assumptions checked here; fixed-protocol possibilities
remain open. None of these obligations requires altering the checked
formulas or any preserved original.

## Assembly source and dependency crosswalk

The original weighted, native and current bodies and all matching selected
comparison/evidence records are preserved in the content-addressed archive.
The two accepted topology-wording edits are authorized by
ENERGY_WEIGHTED_POSTCOMPARISON_PRECISIONS.md
(`12d9aa4e7acd40c2a62fa5b7595234f6221b726078051c818869538acd28a64c`).
Every original formula, domain argument and counterexample is retained.
Exact before/after edits, complete diffs and source/assembled byte maps
are separate packet records, not new scientific validation.

| Parent or earlier body | Used role and limit |
|---|---|
| [Energy-distribution limit](ENERGY_DISTRIBUTION_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-13.md) | Original E3 actual commuting-energy bridge and actual carrier/moment conventions; protocol applications inherit their distinct resources. Its scalar endpoint is not inferred from weighted trace convergence. |
| [Current refinement](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Actual dispersion/current normalization, branch coordinates and the high-coordinate reflection convention. It remains open_gate. |
| [Local even continuum](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Supplied positive free-Fock Hamiltonian, bounded fields and continuum CAR carrier used for actual state/control constructions. |
| Weighted body above | Common-Hamiltonian interpolation and homogeneous half-energy estimate used in the later compositions; no extra independent vote is created by reuse. |
| Native and current bodies above | Distinct source-exposed compositions with full placed versus reduced low-density trace hypotheses and their specified observables. |

The source archive retains the 584-line comparison and its three accepted
scope qualifications. The old precision record's statement that the current
check was still active is a historical timestamp, superseded by the later
502-line freeze and root acceptance. Parent canonical hashes, exact roles,
read coverage and evidence chronology are separately bound. This assembly
does not recertify their transitive premises or promote their status.

Common-carrier coefficient convergence, the actual density/moment resources
at a preparation stage, fixed-protocol realization of counterexamples, and
the true generators of subsequent holds remain application obligations.
No unscaled-current limit, arbitrary interacting-hold conservation,
growing-time density comparison or detector realization is added here.

The negative controls keep their literal state/protocol classes. Existing
scoped stress checks are preserved; N1/N5 global-packet obligations remain
pending, and no completed no-go packet or packet PASS is assigned.

No scientific/formal runner, publication driver or audit was executed for
this source assembly. The new canonical identity-only runner sources remain
unexecuted by the preparation worker. Their later root-owned execution checks
source bytes and reconstruction, with zero mathematical predicates.

The [publication packet](../.claude/science/physics-loops/toe-energy-observables-20261013/README.md) binds exact archives,
complete publication diffs, parent identities, review chronology and pending
obligations. The [identity-only runner](../scripts/energy_weighted_current_identity_2026_10_13.py) verifies bytes and
reconstruction only; it supplies no mathematical proof, independent audit or
retained status. Original pending/exposure statements within the body remain
historical. The exact source acceptance retains its false fresh-full-note and
fresh-full-context-diff read fields.
