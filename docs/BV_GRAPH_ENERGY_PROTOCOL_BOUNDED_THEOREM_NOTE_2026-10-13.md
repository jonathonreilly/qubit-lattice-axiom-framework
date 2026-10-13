---
claim_id: bv_graph_energy_protocol_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Compact real scalar BV work and domain preservation; slow-preparation and finite-BV graph moments, actual high-sector bounds and finite-word comparisons under the original hypotheses."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: source_accepted_publication_scope_separately_gated
runner: scripts/bv_graph_energy_protocol_identity_2026_10_13.py
scientific_execution: no_mathematical_predicates_in_identity_tools
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: supplied-model conditional arguments with explicit provisional dependencies
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete conditional proof bodies preserved with two specifically authorized wording corrections across this source assembly
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: exact publication review and source integration, cumulative stack checks, then independent retained audit
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
  - excitation_pulse_response_bounded_theorem_note_2026-10-12
  - energy_transfer_correlation_bounded_theorem_note_2026-10-12
  - time_averaged_energy_transfer_bounded_theorem_note_2026-10-12
---

# BV work and graph-energy protocol sources

**Type:** bounded_theorem

Status: conditional-support. Root accepted the pinned source assembly for
publication preparation. Exact publication-wrapper and program acceptance is
recorded separately in the installed evidence packet; source acceptance alone
authorizes no execution. The filename date is not evidence of publication.

The two complete arguments below retain their own local notation, equation
labels, premises, controls and historical status/exposure statements. Each
source was frozen before its later source-exposed comparison. The assembly
does not create a new combined theorem by concatenating them. All original
bytes are recoverable from the content-addressed source archive.

The selected sources are `BV_PULSE_WORK_INDEPENDENT.md` and `GRAPH_ENERGY_INDEPENDENT.md`. Original phrases saying
that comparisons or root reads are pending describe their earlier freezes.
The later complete comparison reports are archived separately, and root reports
complete reads of the four independent bodies and four comparison reports.
This worker read those eight complete bodies during source assembly. Root
reused its complete body/comparison reads at unchanged hashes, read the six
new source wrappers and changed surrounding arguments, and mechanically
reconstructed all twelve complete diffs and 211 original aliases. Root did not
claim to manually reread every assembled unchanged line or complete diff.
The exact source acceptance record preserves those coverage limits. Publication
wrapper/program review is a separate gate. This chronology is not a new proof.

The derivation/comparison lineage is separate-context reasoning within the same
selected model family with shared parents, followed by source-exposed checks.
It is neither model-diverse checking, analytic Lean verification nor retained
audit. Current remains `open_gate`; every inherited conditional/open premise
remains explicit. No N1/N5 packet PASS or global no-go is assigned.

## First complete source body

# General scalar BV pulses: exact form work and domain preservation

Status: conditional ordinary mathematical derivation, frozen before exposure
to the root BV or prepared-pulse robustness candidates. The exact allowed
pulse and finite-energy parents were already exposed and are reused at their
pinned identities. The proof below reconstructs the new BV passage directly.
It does not claim minimal temporal regularity, generic novelty, formal
verification, an audit, or transitive certification of those parents.

## 1. Source, representative, and endpoint conventions

Let H>=0 be selfadjoint on a separable Hilbert space, V=V* bounded with
||V||<=K, G=H+V, and A=A* bounded with ||A||<=a. Write

    D=D(H)=D(G), Q=D(H^(1/2)),
    G_j(t)=G-epsilon j(t)A, epsilon in R.                  (B1)

All instantaneous operators have domain D and closed form domain Q. A
semibounded expectation always means its closed-form/spectral expectation.
For example E_G(rho)=E_H(rho)+Tr(rho V) when E_H(rho)<infinity. No mass gap,
smallness of epsilon, or A D subset D or A Q subset Q is needed in sections
1-6. In the supplied model H is the actual full-Fock free Hamiltonian,
V,A are even, and the same theorem applies at every c and to the low target.
There is no outside-band zero-mode replacement of H_c.

Let j be a real compactly supported BV function as an almost-everywhere
class on R, with distributional derivative the finite signed measure

    nu=Dj, TV=|nu|(R)<infinity.                           (B2)

Use its canonical right-continuous representative, still denoted j. Then
j(t)=j(t+), both one-sided limits exist, and
nu({t})=j(t)-j(t-). Isolated changes of a representative do not change the
propagator or nu; such point values must not be inserted as fictitious
source impulses. TV denotes distributional variation, equivalently the
variation of this representative. Compact support implies nu(R)=0.

The propagator U(t,r) is determined by the almost-everywhere coefficient
j in the usual bounded interaction equation over the reference G:

    S_r(t)=exp(i(t-r)G)U(t,r),
    S_r'(t)=i epsilon j(t) beta_(t-r)(A) S_r(t),
    beta_s(A)=exp(isG)Aexp(-isG).                         (B3)

Strong integrals on vectors define its Dyson series. The scalar L1
majorant makes the series converge, gives uniqueness, unitarity, strong
continuity, and composition. For two real integrable sources on [r,t],

    sup_(r<=s<=t)||U_jn(s,r)-U_j(s,r)||
         <=|epsilon|a integral_r^t |j_n-j|.              (B4)

The same bound holds for propagators with final time t and varying starting
time s. It follows by variation of constants for bounded interaction
generators and unitarity. It contains no exponential and makes no domain
or energy-continuity assertion.

Default endpoint energies below use G_j(r)=G-epsilon j(r)A and G_j(t)
with right traces. Their work interval is (r,t], excluding a jump at r and
including a jump at t. For a cyclic pulse supported in [0,T], the initial
base energy is at 0- and the final base energy is at T+: the work interval
is [0,T], including both possible endpoint jumps. The state itself is
continuous at every jump, and the point-value convention never changes U.

## 2. Finite-step approximants with controlled variation

Fix r<t. On [r,t], write

    j(s)=j(r)+nu((r,s]),
    F_+(s)=nu_+((r,s]), F_-(s)=nu_-((r,s]),               (B5)

where nu_+,nu_- are the Jordan measures. These two functions are bounded,
nondecreasing and right continuous. For delta_n down to zero define

    k_n(s)=j(r)+delta_n floor(F_+(s)/delta_n)
                     -delta_n floor(F_-(s)/delta_n).    (B6)

Each quantized monotone function has finitely many levels and finitely
many jumps, including a possible jump at t. Right continuity ensures its
level-crossing value is the post-jump value. Thus k_n is a finite step
function. Its uniform error is at most 2delta_n and its total variation
on (r,t] is at most nu_+((r,t])+nu_-((r,t]). Clip k_n to
[-||j||_infinity,||j||_infinity], calling the result j_n. Scalar clipping
is 1-Lipschitz, cannot increase variation, and cannot increase its error
from the values of j. Consequently

    j_n(r)=j(r), ||j_n-j||_infinity,[r,t]->0,
    ||j_n||_infinity<=||j||_infinity,
    |Dj_n|((r,t])<=|nu|((r,t]).                          (B7)

This construction does not require finitely many jumps in j, absolute
continuity, or absence of singular-continuous variation.

For a cyclic approximation take r strictly before the compact support and
t strictly after it. Then j(r)=0 and the two Jordan measures have equal
total mass, so their quantized final values coincide. Hence j_n returns
exactly to zero, is zero outside the same support interval, and its whole
variation is at most TV. In particular endpoint jumps are included in
this cyclic approximation, rather than repaired afterward by extra jumps.

Let nu_n be the Stieltjes derivative of j_n on (r,t], extended as a measure
on [r,t] with zero mass at r. For f in C1([r,t]), integration by parts gives

    integral_(r,t] f dnu_n
      =f(t)j_n(t)-f(r)j_n(r)-integral_r^t j_n(s)f'(s)ds.  (B8)

Uniform convergence proves convergence of this expression to its j version.
The uniform total-variation bound and uniform density of C1 tests in
C([r,t]) extend this to every continuous test. Thus nu_n converges weakly
as a finite signed measure on this exact interval to nu restricted to
(r,t]. Endpoint atoms are not lost or silently moved across the boundary.

For any fixed continuous f, the stronger uniform primitive statement also
holds:

    sup_(r<=s<=t)|integral_(r,s] f d(nu_n-nu)|->0.         (B9)

Indeed approximate f uniformly by a C1 function p. The residual integral
is at most 2 TV ||f-p||_infinity. Formula B8 on every [r,s] bounds the
p integral uniformly by
[2||p||_infinity+integral_r^t |p'|]||j_n-j||_infinity.
First take n large, then improve the approximation. This proof handles
atoms and singular measures; no convergence of derivative densities is
claimed or needed.

## 3. Exact work from two-sided lower semicontinuity

For a finite step j_n, each constant segment is generated by one
selfadjoint H plus a bounded perturbation. Spectral calculus for a positive
constant shift of that operator proves preservation of Q and conservation
of its form energy on that segment. At a jump the state is continuous and
the form energy changes by exactly -epsilon Delta j_n <A>. Concatenating
the finitely many segments gives, for x in Q and u_n(s)=U_jn(s,r)x,

    q_Gjn(t)(u_n(t))-q_Gjn(r)(x)
       =-epsilon integral_(r,t] <u_n(s),A u_n(s)>dnu_n(s). (B10)

This finite-step proof uses no A Q inclusion and no differentiability of an
unbounded expectation. It agrees with the allowed finite-jump parent.

Let u(s)=U_j(s,r)x. By B4, u_n->u uniformly in Hilbert norm on [r,t].
The continuous scalar functions a_n(s)=<u_n(s),A u_n(s)> therefore converge
uniformly to a(s)=<u(s),A u(s)>. B7-B8 show

    integral_(r,t] a_n dnu_n -> integral_(r,t] a dnu.      (B11)

For the part a_n-a use the bounded variations; for the part a use weak
measure convergence against this continuous function. The initial form
in B10 converges because only a bounded scalar coefficient changes.
The final forms in B10 consequently have a finite limit. Lower
semicontinuity of q_H, with the bounded final potential treated separately,
proves u(t) in Q and only the forward inequality

    q_Gj(t)(u(t)) <= q_Gj(r)(x)
                       -epsilon integral_(r,t] a(s)dnu(s). (B12)

Stopping here would leave a possible energy defect. Norm convergence of
the propagators does not supply the reverse inequality.

Apply exactly the same approximation and lower-semicontinuity argument to
backward propagation from an arbitrary y in Q at t. The finite-step
identity, rearranged with v_n(s)=U_jn(s,t)y, yields in the limit

    U_j(r,t)y in Q,
    q_Gj(r)(U_j(r,t)y) <= q_Gj(t)(y)
        +epsilon integral_(r,t]
             <U_j(s,t)y,A U_j(s,t)y>dnu(s).               (B13)

Forward B12 and backward B13 prove U_j(t,r)Q=Q. Now take y=u(t), which
belongs to Q by B12. Composition gives U_j(s,t)y=u(s), so B13 is the exact
reverse of B12. Therefore the complete vector identity is

    q_Gj(t)(U(t,r)x)-q_Gj(r)(x)
       =-epsilon integral_(r,t]
                <U(s,r)x,A U(s,r)x>dnu(s), x in Q.       (B14)

This is the decisive passage. It proves energy equality before making any
claim of energy convergence of the approximants. Having proved B14, B10-
B11 now imply that their actual form energies do converge. That conclusion
is a consequence of the two-sided argument, not of B4 alone.

## 4. Operator domain, a bounded work operator, and time regularity

Define the strong operator integral

    W(t,r)=-epsilon integral_(r,t]
                    U(s,r)* A U(s,r)dnu(s),
    W(t,r)=W(t,r)*, ||W(t,r)||<=|epsilon|a|nu|((r,t]).     (B15)

It is defined first on each vector; boundedness of the integrand, finite
variation and strong continuity make it a bounded selfadjoint operator.
B14 is an identity of quadratic forms on Q. Polarization makes it an
identity of their sesquilinear forms. It also proves the operator statement

    U(t,r)D=D,
    G_j(t)U(t,r)x=U(t,r)(G_j(r)+W(t,r))x, x in D.         (B16)

Here is the domain step explicitly. For x in D and every z in D(G_j(t)),
write z=U(t,r)y with y in Q, using the already established onto-Q property.
The polarized identity gives

    <G_j(t)z,U(t,r)x>
       =<z,U(t,r)(G_j(r)+W(t,r))x>.

The definition of the adjoint and selfadjointness of G_j(t) put U(t,r)x
in D(G_j(t)) and give B16. Apply the reversed form identity for the
onto-D statement. This argument proves operator-domain preservation from
the exact form identity; it does not assume it in the approximation limit.

In particular, if Y_s=G_j(s)+b>=delta>0 for a fixed shift b, then

    ||Y_t U(t,r)x||<=||Y_r x||+|epsilon|a|nu|((r,t])||x||,
    ||Y_t U(t,r)Y_r^(-1)||
       <=1+|epsilon|a|nu|((r,t])/delta.                  (B17)

One may take b=K+|epsilon|a||j||_infinity+delta, uniformly over the
actual spacings when K,a,j are uniformly specified.
This sufficient linear graph bound is stronger than the exponential
Gronwall bound used in the earlier AC construction. It follows from B16
and the bounded work operator, with no instantaneous pulse gap assumption.

For x in D, the path U(t,r)x is graph-continuous for H. To see this directly,
W(t,r) is norm càdlàg, since its increments have norm at most
|epsilon|a|nu| on the corresponding intervals. At a jump s its increment is
-epsilon Delta j(s) U(s,r)*A U(s,r). Formula B16 then gives the càdlàg
vector G_j(t)U(t,r)x. In

    H U(t,r)x=G_j(t)U(t,r)x-V U(t,r)x
                                      +epsilon j(t)A U(t,r)x,           (B18)

the two jump increments cancel. Right continuity and equality of each
left limit therefore prove ordinary strong continuity of H U(t,r)x.

The bounded interaction equation has the fixed-D-test weak Schrödinger
equation. By B18 its operator-domain vector path has a bounded, strongly
measurable G_j(t)U(t,r)x on compact intervals. Integrating the weak equation
against the dense D tests gives the strong vector integral equation. Thus
U(t,r)x is locally absolutely continuous in Hilbert space and solves
i u'(t)=G_j(t)u(t) almost everywhere. At every continuity point of j it is
strongly differentiable with that derivative; at a jump its right/left
derivatives use G_j(t) and G_j(t-), respectively. A continuous singular-BV
source has a Hilbert-C1 path on D, although its energy work measure need
not be absolutely continuous. No derivative of j is needed for this claim.

For x merely in Q, the free form energy is continuous in t. Indeed B14
makes the driven form energy càdlàg with jump -epsilon Delta j <A>.
Adding epsilon j(t)<A> and subtracting <V> cancels those jumps; the bounded
expectations are continuous. Weak continuity of H^(1/2)u(t) follows from
Hilbert continuity, a locally uniform form bound, and tests in D(H^(1/2)).
Continuity of its squared norm then gives strong form-norm continuity.
No operator-domain membership is asserted for a vector initially only in Q.

## 5. Endpoint variants and normal densities

Denote the endpoint form using the left or right trace by q_Gj(s-) or
q_Gj(s+). For r<t, B14 has the following exact variants:

| Initial trace at r | Final trace at t | Work measure interval |
| --- | --- | --- |
| right | right | (r,t] |
| left | right | [r,t] |
| right | left | (r,t) |
| left | left | [r,t) |

They follow by adding or subtracting the bounded endpoint jump energy.
The continuous expectation at the jump makes the measure integral
unambiguous. The corresponding bounded operator identity and domain result
also follow by adding or subtracting these bounded endpoint terms.

For a normal density rho with E_H(rho)<infinity, take its spectral
decomposition with positive weights. Every such vector is in Q, and B14
gives a finite final energy sum, bounded by the initial free energy plus
bounded potential/source terms. Sum B14: shifted/free positive energies
are summable, and boundedness of A permits the integral to pass through
the weights against the finite measure. For a cyclic source in [0,T] this
gives, exactly,

    W_rho:=E_G(rho_T)-E_G(rho)
       =-epsilon integral_[0,T] a_rho,epsilon(s)dnu(s),
    a_rho,epsilon(s)=Tr(rho_s A),
    |W_rho|<=|epsilon|a TV.                              (B19)

At an intermediate time t in [0,T], with the right source trace,

    E_G(rho_t)-epsilon j(t)a_rho,epsilon(t)
       =E_G(rho)-epsilon integral_[0,t]a_rho,epsilon dnu,
    E_H(rho_t)<=E_H(rho)+2K
                    +|epsilon|a[|nu|([0,t])+|j(t)|].     (B20)

At T and during every later autonomous G hold the last bound has j=0 and
|nu|([0,t])=TV. The exact stronger final bound is
E_H(rho_(T+w))<=E_G(rho)+W_rho+K. No repeated 2K is accumulated.
Normality is preserved by the unitary; the result concerns full Fock and
does not impose parity on the input. Even observables and controls preserve
the earlier parity qualifications. The finite-c high-occupation estimate
follows from the same actual H_c>=Lambda_c N_H premise and this energy cap.

The bounded expectations in B19-B20 are continuous in t. This follows by
finite-rank trace approximation and strong unitary continuity, or by the
uniformly dominated spectral decomposition. The cancellation argument of
section 4 also makes E_H(rho_t) continuous; it is not claimed to be
absolutely continuous for every initially finite-form-energy density.

The structured step approximation now also gives convergence of these
normal-density energy trajectories. The driven expectations converge
uniformly by B4, the measure primitives converge by B9, and the bounded
potential terms converge. Thus exact work proves their energy convergence.
It would be incorrect to infer that conclusion merely from trace-norm
convergence of U_jn rho U_jn*.

For a cyclic source, B16 can be written as a bounded global energy-transfer
commutator on D:

    W_cyc=-epsilon integral_[0,T] U(s,0)*A U(s,0)dnu(s),
    [G,U(T,0)]=U(T,0)W_cyc,
    ||[G,U(T,0)]||<=|epsilon|a TV.                       (B21)

Here W_cyc includes both endpoint masses as in B19 and is distinct from
the default half-open W(T,0) in B15. The norm refers to the
bounded extension of this initially D-defined commutator. This is a global
G statement derived from the work theorem; it is not a bound for any
unbounded regional energy observable. For H, adding [V,U] gives the
sufficient bound 2K+|epsilon|a TV.

## 6. Work sign and bounded-response statements

Set J(t)=integral_0^t|j(s)|ds for 0<=t<=T, J=J(T), and

    B_j=integral_[0,T] J(t)|nu|(dt),
    C_j=integral_[0,T] J(t)^2|nu|(dt).                    (B22)

These are finite, J is continuous, and no choice of a left/right J value at
an atom is needed. The bounded source/readout identity of the allowed
finite-energy core uses only L1 time dependence, so it applies unchanged:
its finite-strength norm bound and its native/continuum spatial statements
need no new BV regularity argument. In particular, for A as its own readout,

    a_rho,epsilon(t)=a_rho,0(t)+epsilon r_rho,j(t)+R_A(t),
    r_rho,j(t)=i integral_0^t j(s)
             Tr(rho[beta_t(A),beta_s(A)])ds,
    |R_A(t)|<=2 epsilon^2 a^3 J(t)^2.                    (B23)

This remainder follows by subtracting the unconjugated commutator in the
exact interaction-picture integral and using ||S(s)-I||<=|epsilon|aJ(s).
It is valid at every finite strength and does not have a source-strength
exponential. Integrating the exact work identity gives

    W_rho=epsilon w_1+epsilon^2 w_2+R_E,
    w_1=-integral_[0,T] a_rho,0(t)dnu(t),
    w_2=-integral_[0,T] r_rho,j(t)dnu(t),
    |R_E|<=2|epsilon|^3 a^3 C_j.                         (B24)

Also |W_rho-epsilon w_1|<=2 epsilon^2 a^2 B_j. For a stationary input,
the baseline is constant and nu([0,T])=0, hence w_1=0. Work is still signed;
neither stationarity nor the BV theorem establishes passivity. The earlier
coherent linear-work, stationary excited-state extraction, and actual-chain
U*Omega controls remain valid members of this larger temporal class.

## 7. Ground absorption, temporal coefficient, and remainder

Now add the supplied actual ground premises: G Omega=E_g Omega, F=G-E_g>=0,
and the relevant excited spectral sector for the even source has gap
Delta=2m-2K>0 in the stated small-K model. The full ground gap remains
m-2K. Set a_g=<Omega,A Omega>, xi=(A-a_g)Omega, and

    mu(S)=<xi,1_S(F)xi>, mu(R)<=a^2,
    supp mu subset [Delta,infinity).                    (B25)

No positive spectral moment is assumed. Ground stationarity, B19 and B23
give at every finite amplitude

    D(epsilon,j)=<U(T)Omega,F U(T)Omega>, D>=0,
    D<=min(|epsilon|a TV,2 epsilon^2 a^2 B_j),
    D=epsilon^2 Q(j)+R_E,
    |R_E|<=2|epsilon|^3 a^3 C_j.                         (B26)

The first line means the scalar expectation is nonnegative. The sign comes
from the starting ground and final nonnegative F, not from the work
integrand. The BV extension does not require an instantaneous driven gap.

There is a further sufficient finite-strength bound from B21. The ground
belongs to D(G)=D(H), B16 preserves this domain, and

    ||F U(T)Omega||<=|epsilon|a TV.

Since the even final vector has spectral support at zero or above Delta,

    D<=epsilon^2 a^2 TV^2/Delta.                        (B27)

Thus B27 can be included in the minimum in B26. This is a consequence of
the bounded global energy-transfer identity, not a bound obtained by
pairing a state norm error with F. If the pulse does not preserve the even
sector, the same ground-initial-state argument uses the full ground gap
instead; without a gap omit B27.

Define jhat(omega)=integral_0^T j(t)exp(i omega t)dt. Then

    Q(j)=integral omega |jhat(omega)|^2 mu(domega)>=0,
    |jhat(omega)|<=min(J,TV/|omega|),
    Q(j)<=a^2 min(J TV,TV^2/Delta).                      (B28)

Here is the measure-level verification. The ground response is
r_g,j(t)=2 integral mu(domega) F_omega(t), where
F_omega(t)=integral_0^t j(s)sin(omega(t-s))ds. Fubini through the finite
nu integral uses |F_omega|<=J and the finite mass of mu. For each fixed
omega, F_omega is C1, even for integrable j, with
F_omega'(t)=omega integral_0^t j(s)cos(omega(t-s))ds.
Stieltjes integration by parts, including the endpoint masses, gives

    -2 integral_[0,T] F_omega(t)dnu(t)
      =2omega integral_(0<=s<t<=T)
                   j(t)j(s)cos(omega(t-s))dsdt
      =omega |jhat(omega)|^2.                            (B29)

Symmetry of the square gives the last equality; its diagonal has Lebesgue
measure zero. Distributional integration by parts on the zero extension
also gives integral exp(i omega t)dnu(t)=-i omega jhat(omega), proving
the inverse-frequency bound in B28. All these manipulations are justified
before requiring an excitation-energy moment. In fact the spectral factor
jhat(F)xi of the first-order excited vector is in D(F), since
integral omega^2|jhat(omega)|^2 dmu<=a^2 TV^2. The energy expansion B26
was nonetheless derived through bounded work, not an assumed unbounded
Taylor expansion of the state.

For V_c bounded by K in the supplied ground model, the final actual free
energy remains at most 2K+D_c, and the corresponding high-occupation bound
is (2K+D_c)/Lambda_c. These are global bounds; a fixed energy cap is still
not a state selector or a local-energy estimate.

## 8. Which spacing-limit statements survive

Fix one BV profile j, its duration T, and finite epsilon. All resources
J,TV,B_j,C_j are then finite and independent of c. Use the same explicitly
conditional common-CAR norm-orbit premises as the allowed pulse sources.
Write d_A,c(T) for the source orbit error and ||P_g,c-P_g,0||_1<=2p_c.
The unital observable extension and actual band density embedding remain
distinct. The bounded source-unitary stability estimate is unchanged, and
the stationary subtraction in the ground work identity gives

    |D_c-D_0|<=4 epsilon^2 a B_j[d_A,c(T)+a p_c].          (B30)

For general normal inputs whose low partial states converge on low CAR,
the compact target readout family gives the same state error e_c->0 as in
the allowed finite-energy comparison. Its exact work estimate becomes

    |W_c-W_0|<=|epsilon|TV
                [(1+2|epsilon|aJ)d_A,c(T)+e_c].          (B31)

Both proofs integrate bounded expectation differences against |nu|.
No total initial/final energy equality follows without the additional
initial-energy premise. The preceding exact work identity preserves the
already stated scalar energy-defect accounting along such a subsequence.
The massive normal-CAR compactness lemma is the same inherited conditional
dependency when energy caps are used to obtain subsequences; it is not
reproved or newly certified here.

The coefficient weight omega|jhat(omega)|^2 is continuous, tends to zero
at omega=0 and at positive infinity by B28, and extends by zero below zero
to a C0 function. The previously checked ground spectral convergence
therefore gives Q_c(j)->Q_0(j) without positive unfiltered moments. Its
time-domain quantitative version also survives:

    |Q_c-Q_0|<=2 TV J d_C,c(T),                           (B32)

where d_C,c(T) is the parent connected ground-correlation modulus. Finally
B26's uniform cubic remainder proves D_c(epsilon(c),j)/epsilon(c)^2->Q_0(j)
for nonzero epsilon(c)->0 under that static coefficient convergence.
Finite-strength B30 needs the stated orbit comparisons. Varying profiles,
shrinking impulses, unbounded source translations and growing observation
windows require their displayed resource-weighted errors to be controlled;
being individually BV is not enough for a uniform joint limit.

## 9. Genuine controls and invalid shortcuts

There is no obstruction for compact scalar BV in this theorem. Two invalid
proof shortcuts and the earlier temporal limit obstruction remain important.

First, norm-convergent domain-preserving unitaries need not have convergent
energies. On fermionic Fock with one-particle energies mn, take a normalized
two-particle occupation chi_n of modes n,n+1, of energy E_n=m(2n+1), and
rotate the vacuum toward it with sin(theta_n)=sqrt(M/E_n). Let U_n be that
two-dimensional rotation and the identity off its span. Then U_n preserves
D(H), ||U_n-I||->0, and

    q_H(U_n Omega)=M, while q_H(Omega)=0.                 (B33)

This is an explicit even finite-rank control disproving a norm-limit-only
energy passage. It is not claimed to arise from the fixed BV source family.
B12 alone would leave precisely this kind of defect; B13 removes it for
the structured source approximation by comparing the reverse work as well.

Second, using only j'(t)dt discards singular work. For example let C be the
Cantor distribution function on [0,1] and set j(t)=C(t) on [0,1],
j(t)=C(2-t) on [1,2], and zero outside. This is a nonzero continuous BV
cyclic source with TV=2 and purely singular-continuous derivative; its
ordinary derivative is zero almost everywhere. Compress its duration by
j_sigma(t)=j(t/sigma). In the two-mode vacuum model H=m(N_1+N_2), A equal
to the normalized even pairing, choose sigma so 4m sigma<pi/2. Then
Re jhat_sigma(2m)>0 because j_sigma is nonnegative and nonzero. Hence
Q=2m|jhat_sigma(2m)|^2>0, and B26 proves strictly positive actual work for
sufficiently small nonzero epsilon. The false derivative-density formula
would predict zero. This is a finite-Fock control of the need for the full
Stieltjes measure, not an additional continuum physical claim.

An explicit infinitely jumping source is

    j(t)=sum_(n>=1) 2^(-n) 1_[2^(-n),3*2^(-n-1))(t).    (B34)

Its intervals are disjoint, the jumps accumulate at zero with vanishing
heights, TV=2, and integral |j|=1/6. It belongs to the new class with its
canonical value zero at zero, and all identities apply with both endpoint
masses of every component included. No finite truncation is asserted to
equal it exactly.

The allowed rough-cell impulse counterexample is unchanged. A normalized
compact rough field f=1_[0,1]e_1, a separated smooth g, and
A=i gamma(f)gamma(g) can make exp(i theta A)Omega lie outside the free
form domain for theta not in pi Z. Smooth fixed-area pulses approaching
that kick are each BV but have diverging TV and can have diverging actual
energies. Thus the BV theorem does not give a uniform impulse theorem.
Exceptional amplitudes and smoother observables remain exceptions to that
specific counterexample. No necessity or optimality of BV is established;
some profiles beyond BV may have finite work under additional hypotheses.

## 10. Exact exposure and retained status

The neutral plan was sealed at 2026-10-12T21:10:01.126443+00:00, before this
new BV proof was developed. Five exact allowed previously fully read sources
were rebound: the finite-energy independent core
2ee8752599c8f5ec9280fca737ca2c3e71efb198e042a3d28074092a210826f2, its
comparison dac8b44d02b124e22968c3e7e005704bc604543787ba54246aa6615d4ec19394,
the pulse core 3be0730d252ce52280e50fb629e369b062b10a5b77cc036eac1bba9b65e001e6,
its comparison ce644c7d6f8e71aa07821e41d2a076599015c62ee6c5e172e62be0fcdb8abcf4,
and ground synthesis b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9.
Their actual identities, immutable copies and prior read coverage are in the
assigned provenance directory. Existing governing instruction identities
and selected model/effort are unchanged.

No root BV addendum, prepared-pulse robustness candidate, either seal,
other new candidate, or checkpoint was read. No mathematical program,
numerical/formal execution, external theorem import, delegation, Git,
canonical edit, installation, publication, audit, prompt or axiom change
occurred. Only this note and its assigned evidence were written. The final
source seal precedes disclosure of its mathematical outcome. Shared exact
parents and same-family separate reasoning are not independent audit or
formal verification.


## Second complete source body

The following graph-energy argument is preserved in full. Its one tracked edit
replaces the unqualified "already sharper" wording by the exact qualified
minimum-of-bounds wording in the archived correction record. No displayed
formula or constant is changed. The graph comparison's additional X18 remains
archived comparison material and is not added here as a new theorem.

# Graph energy after slow preparation and finite BV control

Status: independently developed conditional ordinary proof from the six pinned
shared parents. The separate graph-energy root candidates and their seals have
not been read. Same-family separate reasoning with shared parents is not a
model-diverse check, formal verification, transitive audit, or retained status.
The selected inherited model and reasoning effort were unchanged.

The linear ramp from the exact free vacuum has a uniform **second free-energy
moment**, not only a first moment. A finite BV control budget adds linearly to
its square root. Autonomous final holding contributes no duration factor. The
actual high expected number is then O(c^2), and full-state normalized
high-vacuum compression is O(c) in trace norm. With bounded commutators on
both sides of each observable insertion, the scalar finite-word compression
error is O(c^2). Shrinking BV time averages give a sufficient squared-resource
bound O((c/epsilon)^2) for a fixed finite word. These rates concern the named
sector comparison; complete continuum correlations have additional state and
orbit hypotheses.

No optimum constant or necessary shrinking scale is claimed. First-moment
caps on arbitrary states do not supply the extra moment used here. None of
the arguments derive the supplied Hamiltonian, exact initial vacuum, control
schedule, observable prescription, or physical identification.

## 1. Exact hypotheses and imported mathematical facts

Let H>=0 be selfadjoint on a separable Hilbert space, D=D(H), and let Omega be
a normalized simple zero-energy vector with H>=m(1-|Omega><Omega|), m>0.
Let V=V* be bounded, ||V||<=K<m/2. Set

    H_s=H+sV, 0<=s<=1;  G=H+V;  delta=m-2K>0.
    i partial_s U_tau(s,r)=tau H_s U_tau(s,r), tau>0.
    psi_tau(s)=U_tau(s,0)Omega.

All these operators have domain D. Let E_s and P_s be the simple ground
energy and projection of H_s, F_s=H_s-E_s>=0, and F=F_1=G-E_g. The full gap
above the final ground is at least delta. If V and the controls commute with
parity in the supplied full-Fock model, even initial vectors stay even, and the excited even
sector gap can instead be taken as Delta=2m-2K. A division by Delta below is
made only under that parity restriction; otherwise use delta.

After the ramp and any autonomous G pre-hold, permit finitely many bounded
selfadjoint controls A_l, ||A_l||<=a_l, with real compact whole-line BV
profiles j_l and strengths epsilon_l. They may overlap. Their generator is

    G+Z(t),  Z(t)=-sum_l epsilon_l j_l(t) A_l,
    B=sum_l |epsilon_l| a_l |D j_l|(R).                    (1)

The derivative is the distributional measure of the zero extension. Both
endpoint jumps and any singular-continuous part count. The initial and final
times are outside all supports, so Z=0 there. A finite sequence with intervening
G holds is included. No pulse-time gap, small amplitude, bounded [H,V], or
invariance A_l D subset D or V D subset D is assumed.

The allowed preparation parent supplies, with all domain details reproduced
there, common-domain unitary evolution, graph continuity, the ground branch,
and the exact adiabatic identity

    xi_s=psi_tau(s)-phi_s
      =(1/(i tau))[U_tau(s,0)X_0 Omega-X_s phi_s
                         + integral_0^s U_tau(s,r) T_r phi_r dr],       (2)
    phi_s in ran P_s, ||phi_s||=1,
    A_s=[P_s',P_s], X_s=R_s P_s' P_s+P_s P_s' R_s,
    T_s=X_s'+X_s A_s, [H_s,X_s]=A_s.

A_s in (2) is the adiabatic auxiliary operator, not one of the pulse controls.
R_s is the reduced inverse of F_s, extended by zero on P_s. Useful exact
identities and sufficient bounds from that parent are

    F_s X_s=P_s' P_s,
    F_s X_s'=P_s''P_s+(P_s')^2+(E_s'-V)X_s,              (3)
    |E_s|<=sK, |E_s'|<=K,
    ||P_s'||<=K/delta, ||P_s''||<=10K^2/delta^2,
    ||X_s||<=K/delta^2, ||X_s'||<=30K^2/delta^3,
    ||A_s||<=K/delta, ||T_s||<=31K^2/delta^3.             (4)

X_s and X_s' map the Hilbert space into D; they are continuous as maps into
the fixed graph space. Equation (2) is a graph-space integral, not a merely
formal application of an unbounded operator to a Hilbert integral. Its proof
and these identities are in preparation synthesis sections 2-7, fully read.
The previous sufficient graph constant is also available:

    kappa=K/(m-K), g=exp(kappa),
    u=K(2m-K)/delta^2, v_*=K^2(43m+4K)/delta^3,
    C_old=(1+g)u+g(v_*+Ku/delta),
    ||(H_s+m)xi_s||<=C_old/tau.                          (5)

For the optional earlier amplitude and first-excess estimates quoted below,
their explicit constants are

    C_ad=2K/delta^2+31K^2/delta^3,
    M_form=sqrt(m/(m-K)), a_*=K sqrt(2m-K)/delta^2,
    b_*=K^2[ sqrt(30(43m+4K))+sqrt(2m-K) ]/delta^3,
    D_*=(1+M_form)a_*+M_form b_*.

The actual model premises used below are explicit in both allowed syntheses:

    H_c=dGamma(e_c,L direct-sum e_c,H),
    e_c,L(p)^2=m^2+2v^2 p^2/(1+sqrt(1-c^2p^2)),
    e_c,H(p)^2=m^2+(2v^2/c^2)(1+sqrt(1-c^2p^2)), |p|<1/c,
    Lambda_c=sqrt(m^2+2v^2/c^2), v>0.                    (6)

The actual Hilbert space is the physical in-band full fermionic Fock space.
Under its isometry into F_L tensor F_H, P=I_L tensor |Omega_H><Omega_H| is
the high-vacuum projection, Q=1-P, and N_H counts high particles. The free
operators H_c, N_H, P, and H_0 tensor I_H strongly commute on that range,
where H_0=dGamma(E), E(p)=sqrt(m^2+v^2p^2) acts on the low factor. In particular

    H_c>=Lambda_c N_H,  H_c>=H_0 tensor I_H.              (7)

Strong commutation follows from their common momentum/occupation
multiplication representation in (6); it is more information than a lone
form inequality. No outside-band zero modes enter any energy assertion.
Potentials and observables have unital extensions for CAR norm comparison;
physical densities and compressed resolvents have their different, zero-
extended placements. P need not reduce G_c and is not an interacting ground
projection or the actual full Fock-band projection.

## 2. Exact graph work, including the ramp and general normal densities

First consider the ramp. Its domain theorem makes U_tau(s,r)x Hilbert C1
and graph continuous for x in D. For the quadratic expectation of H_s,
the finite-difference product rule pairs Hilbert differences of the vector
with graph-continuous H_s-vector values. The two tau H_s contributions
cancel, so its derivative is <U_tau(s,r)x,V U_tau(s,r)x>. No D(H^2) assumption
or derivative of H_s U_tau(s,r)x is needed. Polarize and test on the dense
image U_tau(s,r)D to obtain the exact operator identity on D:

    H_s U_tau(s,r)=U_tau(s,r)(H_r+W_s,r),
    W_s,r=integral_r^s U_tau(u,r)* V U_tau(u,r)du,
    ||W_s,r||<=K|s-r|.                                  (8)

Strong vector integration suffices. The reversed time identity has the same
absolute bound. In particular, for Y_s=H_s+m,

    ||Y_s U_tau(s,r)x||<=||Y_r x||+K|s-r| ||x||,
    ||Y_s U_tau(s,r)Y_r^-1||<=1+K|s-r|/(m-rK).            (9)

The denominator is positive throughout the ramp. For forward r<=s, the last
ratio is at most 1+Ks/m, since (s-r)/(m-rK)<=s/m. This is a useful tighter
transport estimate than an exponential Gronwall factor. The claim is an
operator graph bound, not an order obtained by squaring positive operators.

For completeness the same work mechanism extends the scalar BV parent to
the finite sum in (1). Approximate every right-continuous j_l uniformly by
finite step functions with no larger variation, using quantized positive
and negative Jordan primitives as in the allowed BV parent. Choose common
subdivisions. Propagators converge uniformly in operator norm on compact
time intervals, by the sum of their L1 perturbation errors. Each finite
step preserves the common operator and form domains, and its form energy
changes at a jump by exactly <state, Delta Z state>. Summing gives the
step work identity. The bounded expectations converge uniformly and each
derivative measure converges weakly against continuous tests, so the work
integrals converge.

Lower semicontinuity of the shifted positive H form gives forward form
invariance and a forward inequality. Apply the same argument backwards from
the **fixed limiting final vector**, which is already in the form domain.
Composition gives the reverse inequality, hence equality and onto-form
invariance. Polarization and the selfadjoint adjoint-domain characterization
then give operator-domain invariance and

    U_p D=D,   G U_p=U_p(G+W_p) on D,
    W_p=-sum_l epsilon_l integral U_p(t,t0)* A_l U_p(t,t0) d(Dj_l)(t),
    W_p=W_p*, ||W_p||<=B.                                (10)

This passage uses neither norm-limit continuity of unbounded energies nor
A_l-domain invariance. It includes simultaneous pulses and endpoint atoms.
It is precisely the two-sided form argument of the shared BV source applied
to a finite sum of signed measures. For each vector the integrands are
continuous and uniformly bounded; the integrals define bounded operators.
An arbitrary G hold preserves D and commutes with G and F. Thus (8)-(10)
compose with no extra term depending on the number or duration of holds.
At an intermediate pulse time, the same formula uses the partial variation
and the instantaneous G+Z(t), with consistent left/right traces.

For a normal density rho, define its second moment spectrally:

    M_2(H;rho)=Tr rho H^2=||H rho^(1/2)||_HS^2.            (11)

It is finite exactly when every positive-weight vector in a spectral
expansion rho=sum lambda_r |x_r><x_r| lies in D(H), and
sum lambda_r ||H x_r||^2 is finite. The notation does not assume x_r in
D(H^2), the existence of an everywhere-defined H^2 rho, or a cyclic trace
identity involving unbounded factors. Monotone bounded spectral cutoffs and
Tonelli give the displayed nonnegative spectral sum. Finite spectral sums
of rho, followed by closedness of H and the Hilbert-Schmidt bound, show that
rho^(1/2) maps the Hilbert space into D and that its H-composition has exactly
that Hilbert-Schmidt norm. The same definition applies to any selfadjoint
G, even when G is not positive.

If initial free root-second-moment is S=||H rho^(1/2)||_HS, (8), (10),
Minkowski in Hilbert-Schmidt norm, and ||T rho^(1/2)||_HS<=||T|| give

    after ramp, pulses, and any final hold:
    ||H rho_final^(1/2)||_HS <= S+2K+B.                   (12)

One can use the unitarily transported columns U rho^(1/2) to evaluate the
final sum; multiplying on the right by U* identifies the usual positive
square root. The ramp first costs K in the G graph norm, the pulses cost B,
and returning from G to H costs K. The two K terms are not charged again
at every hold. For a state initially specified at the G stage, its sharper
bound is ||G rho^(1/2)||_HS+B+K, or at most S+2K+B if only S is known.
These statements extend to subnormalized positive trace-class inputs with
all bounded terms multiplied by sqrt(Tr rho).

## 3. Preparation-specific second moments and an excitation graph bound

Apply (8) to the exact free vacuum. Since H Omega=0,

    ||H_s psi_tau(s)||<=sK,  ||H psi_tau(s)||<=2sK.        (13)

Thus the entire ramp has Tr rho_tau(s) H^2<=4s^2 K^2, independently of its
speed. This supplies more than the earlier first-energy cap. At s=1, a G
hold conserves ||G psi|| and ||F psi||, so (13)'s final free bound 2K
survives every autonomous hold even though H itself is not conserved.

The inherited graph estimate (5) already proves ||F_s psi_tau(s)||<=C_old/tau:
F_s phi_s=0 and F_s(H_s+m)^-1 is a positive contraction by spectral calculus.
There is also a direct excitation-graph coefficient that avoids that shift.
From (3)-(4),

    ||F_s X_s||<=K/delta,
    ||F_s X_s'||<=13K^2/delta^2,
    ||F_s T_s||<=14K^2/delta^2.                          (14)

The 13 is 10+1+2, using ||E_s'-V||<=2K; the extra 1 in the last line comes
from F_s X_s A_s. Subtract E_s from (8) and use |E_s-E_r|<=K|s-r|:

    ||F_s U_tau(s,r)x||
       <=||F_r x||+2K|s-r| ||x||, x in D.               (15)

Apply this directly to each term of the graph integral (2). Its graph
continuity, already proved by the parent, justifies carrying the fixed F_s
through the integral. For 0<=s<=1 the resulting coefficient is

    ||F_s psi_tau(s)||=||F_s xi_s||<=C_F(s)/tau,
    C_F(s)=2K/delta+16s K^2/delta^2+31s^2 K^3/delta^3.    (16)

Indeed the initial endpoint costs K/delta+2Ks K/delta^2, the final endpoint
costs K/delta, and the integral costs
14s K^2/delta^2+31s^2 K^3/delta^3. This calculation retains both endpoints
of the linear schedule. All constants vanish when K=0.
Define the sufficient final coefficient and root-second-moment bound

    C_*=min(C_old, C_F(1)),
    eta_tau=min(K+|E_g|, C_*/tau) <= min(2K,C_*/tau).      (17)

The first entry follows from ||G psi_tau(1)||<=K. It is optional to replace
K+|E_g| by the coarser 2K when E_g is not separately known.
For the prepared vector after all the controls and final holding, (10) gives

    ||G psi_final||<=K+B,
    ||F psi_final||<=eta_tau+B,
    ||H psi_final||<=2K+B.                              (18)

A second sufficient free root-second-moment coefficient is
eta_tau+B+K+|E_g|; take the smaller one if useful. In particular

    Tr rho_final H^2 <= (2K+B)^2,
    Tr rho_final F^2 <= (eta_tau+B)^2.                   (19)

The first moment cap is also 2K+B: the ramp's exact mean G-energy is at most
K, work changes it by at most B, and |<V>|<=K. These are actual unbounded
moments on the physical space, uniform in every final hold time. At an
intermediate pulse time replace B by partial variation and add ||Z(t)||
to the free root-second-moment bound.

Let gamma=delta in the unrestricted case, or gamma=Delta for the preserved
even sector. The spectral inequalities F^2>=gamma F and F^2>=gamma^2(1-P_g)
on that sector yield

    <F>_final <= (eta_tau+B)^2/gamma,
    ||rho_final-P_g||_1 <= 2 min(1,(eta_tau+B)/gamma).      (20)

One may also retain the independent first-work bound <F>_final<=d_tau+B,
where d_tau is the parent ramp excess (at most D_*^2/tau^2). The smaller
bound is valid. For B=0 the parent amplitude estimate 2 min(1,C_ad/tau) also remains
available; take the minimum with the bound in (20). The displayed constants
cross; there is no uniform ordering of those older bounds. Finite controls need not leave a state
close to the ground. If B(c)->0 and tau(c)->infinity, (20) and the parent
static ground comparison do give a ground-state limit uniformly over every
final hold; fixed nonzero B alone does not imply that conclusion.

## 4. Actual high number, vacuum compression, and the low target moment

Now let rho_c be any actual normal density with

    S_c^2=Tr rho_c H_c^2<infinity, M_c=Tr rho_c H_c<=S_c.  (21)

This includes the protocol with S_c<=2K+B, but is a separately stated
second-moment class. In each joint free occupation configuration h>=Lambda_c n_H,
and n_H is a nonnegative integer. Hence, as spectral/form statements,

    H_c^2>=Lambda_c^2 N_H^2>=Lambda_c^2 N_H,
    Tr rho_c N_H <= Tr rho_c N_H^2 <= S_c^2/Lambda_c^2,
    q_c:=Tr rho_c Q <= min(1,M_c/Lambda_c,S_c^2/Lambda_c^2). (22)

The first inequality in (22) uses actual strong commutation. Squaring a
generic positive form inequality between noncommuting operators would not
justify it. Finite second moment also places each positive-weight vector
in D(N_H). None of this asserts conservation of N_H under V_c or the pulses.
Uniform S_c therefore gives an O(c^2) actual expected high particle number,
not merely a probability bound.

Let p_c=1-q_c and, when p_c>0, let

    sigma_hat_c=P rho_hat_c P/p_c                        (23)

be the normalized full-carrier high-vacuum density. It identifies with a
trace-one low density sigma_c tensor the high vacuum, supported in the
actual low band. A purification Phi of rho_hat_c has normalized projected
purification (P tensor I)Phi/sqrt(p_c), whose overlap with Phi is sqrt(p_c).
The rank-two pure-state trace formula followed by contractivity of partial
trace proves

    ||rho_hat_c-sigma_hat_c||_1<=2 sqrt(q_c)
                         <=2 min(1,S_c/Lambda_c).         (24)

No spurious additional normalization term is needed in this trace-distance
estimate. A sufficient condition for p_c>0 is S_c<Lambda_c. If p_c=0 the
normalized compression is undefined, although all unnormalized bounds hold.

There is an even stronger relation to the trace-one low partial state
lambda_c=Tr_H rho_hat_c. The partial trace of the P-Q off-diagonal blocks
vanishes, so

    lambda_c=p_c sigma_c+chi_c,
    chi_c=Tr_H(Q rho_hat_c Q)>=0, Tr chi_c=q_c,
    ||lambda_c-sigma_c||_1<=2q_c<=2S_c^2/Lambda_c^2.       (25)

This comparison is different from (24), which detects low-high coherences.
Finally the commuting free comparison in (7) gives

    Tr lambda_c H_0^2<=S_c^2,
    Tr sigma_c H_0^2<=S_c^2/p_c.                         (26)

These are statements about the actual embedded density at each c. No
normality or second-moment conclusion for an unspecified CAR subsequential
limit is inferred merely by citing them.

## 5. Energy windows, transfer profiles, and actual mean-energy comparison

For any nonnegative selfadjoint H and normal density of second moment S^2,
let E_R=1_[0,R](H), R>0. Spectral calculus gives

    Tr rho(1-E_R)<=S^2/R^2,
    Tr rho H(1-E_R)<=S^2/R.                              (27)

If rho_R=E_R rho E_R/Tr(rho E_R) exists, the same purification proof gives
||rho-rho_R||_1<=2 min(1,S/R). For the unnormalized corner, on a purification
the difference from its unnormalized projected rank-one operator has trace
norm sqrt(q^2+4q(1-q))<=2 sqrt(q), where q is the discarded probability.
Partial-trace contraction therefore also gives
||rho-E_R rho E_R||_1<=2 min(1,S/R).
Consequently a bounded operator error D with
||E_R D E_R||<=d_R satisfies

    |Tr rho D|<=d_R+2||D|| min(1,S/R).                   (28)

This converts an energy-window norm comparison into a state expectation
comparison. It improves the first-moment tail sqrt(M/R) to S/R; it does not
supply d_R without a dynamical/operator comparison premise.

A complementary formulation concerns energy transferred by a bounded
insertion A, ||A||<=a. Define its window profile

    t_A(L,R)=||(1-E_L) A E_R||, L>R>0.                  (29)

Splitting rho^(1/2) into E_R and its complement gives a Hilbert-Schmidt
estimate, valid without an A-domain assumption:

    ||(1-E_L) A rho^(1/2)||_HS
        <=t_A(L,R)+a min(1,S/R).                        (30)

The square is the unnormalized output tail probability. Normalizing the
output A rho A* divides that probability by Tr rho A*A, if it is positive.
The profile in (29) is genuine extra data for a general bounded A.

If A D(H) subset D(H) and C=[H,A] on D(H) extends boundedly with ||C||<=d,
then the adjoint also preserves D(H) and [H,A*]=-C*. Indeed test the identity
H A y=A H y+C y against any x in D(H), for y in D(H), and use the adjoint-domain
characterization for A*x. In particular,

    ||H A x||<=a||Hx||+d||x||,
    ||H A rho^(1/2)||_HS<=a S+d,                        (31)
    t_A(L,R)<=min(a,(aR+d)/L,d/(L-R)).                   (32)

Here is the domain justification for the last, gap-separated term. On
ran E_R the restricted H_R is bounded by R; on ran(1-E_L) the restricted
H_L is at least L. Set X=(1-E_L)AE_R and C_LR=(1-E_L)CE_R. The domain
inclusion makes H_L X bounded, and
H_L X-X H_R=C_LR. Differentiate
exp(-u H_L)X exp(u H_R) for u>0 and integrate. The positive semigroup is
norm differentiable there; bounded H_L X makes the limit at u=0 equal X
in norm. The expression vanishes in norm at infinity, so

    X=integral_0^infinity exp(-u H_L) C_LR exp(u H_R)du,
    ||X||<=d/(L-R).

All integrals converge in norm; no inverse of a nonexistent spectral gap
on the entire Hilbert space is used. Equations (31) and (7) also give the
more direct output tail bound (aS+d)^2/L^2, and the corresponding actual
high-sector bound (aS+d)^2/Lambda_c^2.

Window transfer is stable under a finite word. For T=A_r ... A_1 choose
R_0<...<R_r. Insert E_Rk after each factor, starting with E_R0. The truncated
recursion differs from the untruncated word by the sum of each first
leakage, propagated through later bounded factors. Therefore

    ||(1-E_Rr) T E_R0||
       <=sum_{k=1}^r t_Ak(R_k,R_(k-1)) product_{i!=k} a_i. (33)

A high-vacuum projection P commutes with H, contracts graph norms and has
zero upward window-transfer profile; it can be inserted in this recursion
at no additional cost. This states the energy-window transfer mechanism
without replacing product compression by the product of compressions.

There is also a useful mean-energy bridge specific to the actual branches.
The branch formula (6) gives, for every allowed p,

    0<=e_c,L-E<=c E^2/(2v).

Indeed 1-sqrt(1-c^2p^2)<=c|p| and e_c,L+E>=2v|p| give that bound by
difference of squares; p=0 has zero difference. Summing low energies uses
sum E_i^2<=(sum E_i)^2. The high energy H_c,H is at most H_c Q, and
H_c Q<=H_c^2/Lambda_c in the common occupation representation. Thus

    0<=Tr rho_c H_c-Tr lambda_c H_0
       <=S_c^2 [c/(2v)+1/Lambda_c].                     (34)

This is an actual finite-spacing bound, including high particles. It uses
second moments and commuting free multipliers; it does not use a false
inequality for squares of interacting operators.

If, additionally, the low densities converge in trace norm,
||lambda_c-rho_0||_1=alpha_c->0, and the S_c are uniformly bounded, then
rho_0 has the corresponding finite H_0 second-moment bound by bounded
spectral cutoffs and lower semicontinuity. For any R>0,

    |Tr lambda_c H_0-Tr rho_0 H_0|
       <=R alpha_c+(S_c^2+S_0^2)/R.                    (35)

Equations (34)-(35) give actual mean free-energy convergence. For preparation
without pulses, the allowed parent already supplies the needed trace-norm
convergence to the target ground, uniformly over every final hold, and
S_c,S_0<=2K. Thus this particular joint preparation limit also converges in
actual mean free energy. The same implication holds for controlled families
whenever their final trace-norm state comparison is separately established.

Uniform second moments and CAR state convergence alone do not imply the
trace-norm hypothesis or energy convergence in (35). A translated smooth
finite-energy particle packet can escape every fixed CAR test while retaining
its energy. Section 8 gives this control explicitly. Second moments suppress
large-energy tails, not spatial escape at fixed energy.

## 6. Finite observable words with bounded commutators

Fix an actual c, put Lambda=Lambda_c, and let rho have root-second-moment S.
Let A_1,...,A_n be bounded blocks with norms at most a_i, preserving D(H),
and bounded commutators with H of norms at most d_i. The adjoint conclusion
following (30) supplies the same bounds for A_i*. More generally separate
d_i^+ and d_i^- may be used if those forward/adjoint data are stated directly.
No selfadjointness of the blocks or chronological product order is required.
Set

    W=A_1 ... A_n, C=P A_1 P A_2 P ... P A_n P,
    a_[r,s]=product_{i=r}^s a_i,
    d_[r,s]^+=sum_{k=r}^s d_k^+ product_{r<=i<=s,i!=k} a_i,
    d_[r,s]^-=sum_{k=r}^s d_k^- product_{r<=i<=s,i!=k} a_i. (36)

Empty products equal one and empty sums zero. These polynomial definitions
also cover a zero factor, with no division by its norm.
Leibniz on D proves the graph bounds for each word and its adjoint.
Every inserted P preserves D and has zero commutator. Telescoping the n+1
projection slots gives the exact identity

    W-C=sum_{j=0}^n L_j Q R_j,
    L_0=I, L_j=P A_1 P ... P A_j (j>=1),
    R_j=A_(j+1) ... A_n, R_n=I.                          (37)

Both endpoint slots are present. Since ||Qx||<=||Hx||/Lambda for x in D,
(31), applied to the normal-density columns, gives

    ||Q L_j* rho^(1/2)||_HS
                  <=(a_[1,j] S+d_[1,j]^-)/Lambda,
    ||Q R_j rho^(1/2)||_HS
                  <=(a_[j+1,n] S+d_[j+1,n]^+)/Lambda.

The bounded trace in each slot equals the Hilbert-Schmidt pairing of those
two columns. Cauchy-Schwarz, followed by the finite slot sum, proves

    |Tr rho(W-C)|<=G_2,
    G_2=Lambda^-2 sum_{j=0}^n
          (a_[1,j] S+d_[1,j]^-)
          (a_[j+1,n] S+d_[j+1,n]^+).                    (38)

This is the complete density argument. It does not assume H rho is trace
class, move H through a trace, or assign an energy bound after an insertion
without proving it. All insertions are controlled by their actual graph
estimates. The original traces contain only bounded operators.

Writing a=product a_i and q=Tr rho Q, the normalized high-vacuum comparison is

    |Tr rho W-Tr sigma(C restricted to ran P)|
       <=G_2+a q <=G_2+a S^2/Lambda^2, p=1-q>0.          (39)

The second term is the exact normalization cost |1-p| times a bound on the
corner word. At fixed n,a_i,d_i,S, both (38) and (39) are O(c^2), uniformly
in parameters for which these data are uniform. This includes every final
hold of the protocol by (18). This scalar rate can be stronger than the
O(c) trace-distance estimate (24) because both sides of each Q are controlled.

No operator equality C=PWP is assumed. No assertion identifies P A_i P
with evolution generated by P G P: P generally does not reduce G.
For completely unrestricted bounded insertions, even the exact free vacuum
with all initial energy moments zero does not control the intermediate
Q excursions in a word; section 8 records a concrete failure.

## 7. Time averages and shrinking windows under second-moment data

Let beta_t(B)=exp(itG)B exp(-itG), G=H+V, ||V||<=K. For a bounded B with
||B||<=b and a compact whole-line complex BV kernel k, define

    A_k(t)=integral_R k(s) beta_(t+s)(B)ds,
    alpha=||k||_1, q_k=|Dk|(R).                          (40)

For arbitrary B this is a strong vector integral. For the supplied CAR
class it is also a norm Bochner integral because the orbit is point-norm
continuous. The shared time-smearing parent proves by weak differentiation
on D(G) tests and Stieltjes integration by parts that

    A_k(t)D subset D, [G,A_k(t)]
                     =i integral beta_(t+s)(B) d(Dk)(s),
    ||A_k(t)||<=b alpha,
    ||[H,A_k(t)]||<=b(q_k+2K alpha).                    (41)

The adjoint uses B* and conjugate k. These are actual operator-domain and
bounded-commutator statements, not only form bounds. They do not require
B or V to preserve D. The constants are uniform in every real center t.
The weak adjoint-domain proof in the allowed parent is load-bearing here;
it includes endpoint atoms for a rectangular average.

Thus (38) applies to the averages with

    a_i=b_i alpha_i, d_i=b_i(q_i+2K alpha_i).             (42)

An unsmeared block with a separately supplied bounded [G,B_i] and D-invariance
also works, replacing b_i q_i by that commutator norm. The conversion to H
adds at most 2K||B_i|| and is uniform in its Heisenberg time center.

For scaled windows k_i,epsilon_i(s)=epsilon_i^-1 phi_i(s/epsilon_i), let
alpha_i=||phi_i||_1 and q_i=|Dphi_i|(R). Then d_i=b_i(q_i/epsilon_i+2K alpha_i).
If any a_i=0 the word vanishes. Otherwise define

    r_i=d_i/a_i=2K+q_i/(alpha_i epsilon_i),
    R_j=sum_{i<=j} r_i, R_0=0, R=R_n, a=product a_i.

The exact coefficient (38) becomes

    G_2=(a/Lambda_c^2) sum_{j=0}^n (S+R_j)(S+R-R_j)
       <=a(n+1)(S+R/2)^2/Lambda_c^2.                    (43)

Normalization adds a S^2/Lambda_c^2. This additive-commutator calculation
avoids an exponential-in-word-length product of reference-energy graph
constants. It proves a sufficient joint regime, for fixed n, fixed kernel
shapes, bounded total K, bounded b_i and uniformly bounded state S:

    c max_i epsilon_i(c)^-1 ->0.                         (44)

For a common shrinking width the displayed scalar bound is
O(c^2(1+epsilon^-1)^2), hence O((c/epsilon)^2) as epsilon->0.
At a fixed nonzero width it is O(c^2). The earlier first-moment theorem
had a sufficient optimized-reference O(c/epsilon) bound; the present power
improvement consumes actual second-moment data. It does not change the
sufficient scale separation for a general word with internal slots.
For n=1 the exact sum has only endpoint terms, 2a S(S+r_1)/Lambda_c^2;
the broader squared bound is deliberately sufficient, not a necessity claim.
A direct bounded-observable state comparison (24) also controls any one
factor, independently of its averaging width.

These sector estimates hold uniformly in all centers and final hold times
when S is uniform. Complete continuum comparison remains a different step:
under the allowed parent's compact free-orbit norm comparisons, bounded
cocycle comparison controls the unital averaged blocks on the enlarged
support window. A converging state functional on the resulting target word
family is still required. For fixed ordinary compact L2 inputs and normalized
kernels, norm continuity already gives qualitative point-window convergence
on compact centers for any epsilon(c)->0, with the explicit state premise.
It need not satisfy (44), and carries no universal rough-input rate.
Growing centers or supports require their actual growing-window moduli.

In particular, finite nonzero pulses can leave a nonstationary final state.
Its uniform graph moment and uniform sector estimates do not by themselves
compare actual and target evolution through an arbitrarily long final hold.
The preparation-without-pulses static ground argument has that additional
uniform-in-hold state conclusion; it must not be silently transferred to a
fixed nonzero driven excitation.

## 8. Controls, failed shortcuts, and exact limits of the stronger claims

### 8.1 First energy does not supply the second moment

At one fixed c the actual low one-particle band contains an infinite-dimensional
spectral subspace with energies in [m,L], for some finite L. Choose countably
many orthonormal vectors there. Let chi_k be a normalized wedge of 2k such
vectors. Distinct particle-number sectors make these chi_k orthogonal, and

    2km<=<chi_k,H_c chi_k><=2kL,
    ||H_c chi_k||^2>=(2km)^2.

With Z=sum k^-3, the normal even density
rho=Z^-1 sum k^-3 |chi_k><chi_k| has finite first energy and infinite second
moment. Mixing it with the vacuum enforces any prescribed positive first cap.
Finite one-particle bandwidth at fixed c does not bound the many-body energy.

Moreover the domain/graph identities work backwards. If a density had finite
final second moment, reverse the holds, BV pulses and ramp in (8)-(12) to
bound its initial root-second-moment by S_final+2K+B. Thus finiteness of the
second moment is preserved in both directions. The finite BV protocol is a
graph isomorphism; its special uniform bound comes from the specified vacuum
input, not regularization of arbitrary finite-first-energy states.

The first-cap high-number rate also cannot be silently upgraded. Choose an
actual normalized two-high-particle chi_c, so
2Lambda_c<=e_c:=<chi_c,H_c chi_c><=2 sqrt(2)Lambda_c. For sufficiently small c,

    rho_c=(1-M/e_c)|Omega><Omega|+(M/e_c)|chi_c><chi_c|

has first energy exactly M and

    M/(sqrt(2)Lambda_c)<=Tr rho_c N_H<=M/Lambda_c.

This is an even normal family in the actual full Fock space. Its second
moments diverge at least proportionally to M Lambda_c. It is not claimed
to be produced by a bounded-resource vacuum preparation protocol.

Conversely choose p_c=S^2/||H_c chi_c||^2 and the pure vector
sqrt(1-p_c)Omega+sqrt(p_c)chi_c. It has second moment S^2, expected high number
2p_c of order Lambda_c^-2, and distance 2 sqrt(p_c) from its normalized
high-vacuum compression, of order Lambda_c^-1. Thus these powers can be
attained in the stated general second-moment state class. This is not an
optimality claim for a fixed interaction/control family.

### 8.2 A bounded finite BV pulse need not give any higher moment

Here is a control within the abstract gapped Hamiltonian and bounded-control
hypotheses. It concerns those general hypotheses; no local CAR realization
of this rank-two control on the specific continuum chain is asserted.
On C Omega direct-sum ell^2({2,3,...}), take H Omega=0 and H e_n=mn e_n.
Let f=sum f_n e_n be the unit vector with

    f_n=C/(sqrt(n) log n),
    C=(sum_{n>=2} 1/(n log(n)^2))^-1/2,
    A=|f><Omega|+|Omega><f|, ||A||=1.

The series for ||f|| converges, while sum n^eta |f_n|^2 diverges for every
eta>0. Set V=0, so the prescribed linear ramp leaves the vacuum unchanged.
Apply the real rectangular pulse j=1_[0,T], whose whole-line variation is
2, with epsilon!=0. During the pulse psi(t)=exp[-it(H-epsilon A)]Omega.
The BV/domain theorem gives psi(t) in D(H); its endpoint second-moment
bound is ||H psi(T)||<=2|epsilon|.

Write u_0(t)=<Omega,psi(t)> and u_n(t)=<e_n,psi(t)>. Since Omega lies in
D(H-epsilon A), the path is Hilbert C1, and u_0' is continuous. Its initial
excited derivative is i epsilon f, so for every sufficiently small positive
T the excited component is nonzero and |u_0(T)|<1. The component equation
and one scalar integration by parts give exactly

    u_n(T)=(epsilon f_n/(mn))
       [u_0(T)-exp(-imnT)-integral_0^T exp(-imn(T-s))u_0'(s)ds].         (45)

The integral tends to zero as n->infinity: approximate its continuous
integrand u_0' in L1 by a finite step function; the Fourier integral of
each step tends to zero, and the L1 error bounds the remainder uniformly.
If b_T=1-|u_0(T)|>0, the bracket in (45) consequently has modulus at least
b_T/2 for all sufficiently large n. Therefore for every eta>0,

    <psi(T),H^(2+eta) psi(T)>
      >= (epsilon^2 b_T^2/4) sum_large_n (mn)^eta |f_n|^2
      =infinity.                                                       (46)

The expectation in (46) is its spectral/form moment. Finite second moment
coexists with failure of every strictly higher moment, including D(H^2).
Any later autonomous H hold preserves these moments. This disproves an
automatic higher-moment extension under the abstract bounded BV premises;
it does not preclude higher regularity for smoother controls or narrower
physical observable classes. All series and asymptotics here were checked
analytically; no numerical program was used.

### 8.3 Two tempting operator shortcuts fail

A positive form inequality does not permit noncommuting squaring. For example
X=diag(1,0) and Y=[[2,1],[1,1]] obey 0<=X<=Y, because Y-X is the positive
all-ones matrix. But Y^2-X^2=[[4,3],[3,2]] has quadratic value -2 on (2,-3).
The valid high-number square estimate instead uses the actual joint free
occupation representation.

Norm or trace convergence alone does not control energy. The allowed BV
parent's finite-rank rotation has vacuum-to-energy-E amplitude sqrt(M/E):
it tends to identity in norm while the resulting vacuum energy stays M and
its second moment grows like M E. The reverse lower-semicontinuity argument
in the BV proof, rather than norm convergence, supplies exact work.
Uniform second moments plus trace convergence do control the first energy
as in (35); they still need not make second moments converge. Taking amplitude
S/E gives trace convergence to the vacuum while the second moment stays S^2.

### 8.4 Initial moments cannot replace insertion regularity

Let chi_c be an actual high two-particle vector in D(H_c), and define the
bounded even rank-two block

    A_c=|chi_c><Omega|+|Omega><chi_c|.

It has norm one, maps D into D, and P A_c P=0. In the free vacuum, of zero
energy and zero moments of every order,

    <Omega,A_c^2 Omega>=1,
    <Omega,P A_c P A_c P Omega>=0.

Its commutator norm is ||H_c chi_c||, of order Lambda_c, so it violates the
uniform commutator resource required for an O(c^2) conclusion. This is an
abstract bounded even block diagnostic; no local CAR realization of this
rank-two operator is claimed.

The allowed time-smearing parent supplies the stronger local-family control
at precisely its stated scope: alternating ordinary-cell coefficients
(Current C24) give bounded finite-support even blocks with high-factor limit,
zero high-vacuum mean, and square equal to identity. With V=0 and a scaled
real normalized kernel, its estimate
||A_epsilon,c-B_c||<=2 epsilon sqrt(m^2+4v^2/c^2) integral |u phi(u)|du
makes the same two-factor full/corner expectations tend respectively to one
and zero when epsilon(c)/c->0. The initial vacuum still has every energy
moment zero. This is a varying locally oscillatory class, not the fixed
ordinary-input C21/C25 class. It does not prove necessity of (44) or settle
all intermediate scales.

The fixed rough ordinary-input witness is different. The allowed source's
B_0=i gamma(1_[0,1] e_1) gamma(g), with a separated nonzero smooth real g,
sends the target vacuum outside D(H_0^(1/2)). Normalized time averages approach
B_0 in norm. If their actual fixed-reference norms
||(H_0+mu)A_epsilon,0(H_0+mu)^-1||, mu>0 fixed, stayed bounded, applying
them to the vacuum and using closedness/bounded spectral cutoffs would put
B_0 Omega in D(H_0), a contradiction already at the weaker form-domain level.
Thus temporal averaging may be graph regularizing while those constants grow
as its width shrinks. This witness proves no universal growth rate.

### 8.5 Moment bounds do not supply spatial tightness or all-time comparison

For spatial escape, choose orthonormal low one-particle vectors u,z with
finite E^2 moments and let T_x be the translation commuting with E. For
x_n->infinity, the two-particle vectors
chi_n=a*(T_xn u)a*(T_xn z)Omega have the same positive first and finite second
free energy for every n. Their moving one-particle modes converge weakly to
zero. Expanding any fixed finite CAR polynomial and using the CAR relations
makes its vector-state expectation converge to the vacuum expectation;
norm density extends this to all fixed CAR elements. The densities stay at
trace distance two from the vacuum. Hence CAR convergence with uniform second
moments can lose energy through spatial escape, consistently with (27).
This example is a target free-Fock state-class control, not the specified
vacuum preparation protocol.

For the distinct long-time issue, on a two-dimensional space take

    H_n=diag(0,omega+omega/(2n)), H_0=diag(0,omega), omega>0,
    psi=(|0>+|1>)/sqrt(2), A=|0><1|+|1><0|,
    w_n=2 pi n/omega.

The Hamiltonians and their bounded-time evolutions converge, all the displayed
state second moments and observable commutators are uniformly bounded, but
at w_n the target A expectation is +1 and the n-model expectation is -1.
This abstract finite-dimensional diagnostic refutes the proposed inference
from compact-time comparison and moments to all-time comparison. It is not
a counterexample asserted for a particular fixed ordinary-cell continuum
family. The latter needs its own long-time dynamical evidence if such a
conclusion is desired.

### 8.6 Resource and domain boundaries

Equations (18), (22), (38) and (43) remain explicit for varying resources.
Uniform graph caps require the relevant square-root budget, such as 2K+B_c,
to stay bounded. The high-mode limit only needs (2K+B_c)/Lambda_c->0 under
these sufficient bounds. Profiles that are individually BV can have diverging
variation; an impulse limit is not covered uniformly merely by that label.
The parent rough-pulse control remains compatible with this statement.

No argument here uses an instantaneous driven gap, an H^2-domain initial
vector, smooth spatial cells, or bounded [H,V]. No unbounded regional energy,
extensive interaction, massless limit, gap closure, physical state selector,
or necessity/optimality of BV is established. A supplied normal density of
finite second moment is distinct from the probability law that would choose
it. Finite polynomial CAR identities alone do not verify these analytic claims.

## 9. Negative-scope check and procedural limits

The no-go-discipline skill was read because the counterexamples delimit
claims inside a positive result. This is a bounded independent proof handoff,
not a submitted no-go packet or a PR/audit operation. The following records
actual checks without claiming that a route count certifies truth.

- N1: The real attempted mechanisms are graph work, direct excitation-graph
  integration, commuting free spectral comparison, energy-window truncation,
  and two-sided word transfer. Counterexamples test separate invalid extensions
  in section 8. They are not five independent routes exhausting one broad
  no-go. No five-route packet PASS or exhaustive scientific obstruction is
  claimed; a formal negative-claim packet remains unsubmitted.
- N2: No independent wall count is asserted. The second-moment data are proved
  for the protocol and separately supplied for a general state; commutator
  data concern insertions and follow from temporal BV averaging. Neither
  condition is silently used to infer the other. Continuum state and orbit
  comparison are separate hypotheses, without an independence theorem.
- N3: The full argument is reread for hidden domain, parity, normality,
  boundedness, endpoint, and commutation assumptions. The mechanical phrase
  scan is saved as evidence; its matches are contextual source/provenance
  words or explicit premises, not an authority or PASS certificate.
- N4: The BV parent's norm-limit energy example is used only against an
  unbounded-energy passage based on norm convergence. The time-smearing
  parent's fixed rough witness is used only against uniform graph constants
  at a point window, and its alternating witness only against the stated
  varying-family short-window compression claim. No broader residual is
  assigned to those witnesses. The new state-class and matrix controls have
  their calculations in section 8 rather than an inherited audit citation.
- N5: The matrix-order diagnostic is finite-dimensional; the high-number
  calculation is joint occupation-wise and then normal-density/full-Fock;
  the word result is finite-block and scalar; local support in the alternating
  example is exactly its parent scope. No per-site regional-energy or general
  lattice-wide dynamical no-go is asserted. No scientific runner was executed,
  so no cached execution certificate is represented as existing.
- N6: There is no claim that a new axiom or unregistered primitive is required.
  This is an implication from a supplied conditional Hamiltonian/control model.
  Primitive-registry status, broad queue searches and convention ratification
  were outside the bounded source barrier, and none is used as proof evidence.
- N7: A hostile reviewer can correctly demand that arbitrary-state examples
  not be used against the prescribed vacuum protocol, or varying high-cell
  examples against fixed ordinary inputs. Smooth observables, smaller control
  budgets, spatial tightness or extra long-time estimates can strengthen the
  conclusions. Those are live extensions, not routes ruled out by this note.
  Its counterexamples refute only the specifically quantified implications
  they instantiate; no failed search is promoted to impossibility.
- N8: Matching earlier boundaries were checked within all six allowed parents.
  A global campaign/queue/no-go-ledger search was not performed because those
  sources were excluded. No claim of global novelty, exhaustion or complete
  negative-claim packet conformance is made.

## 10. Sources, verification and freeze boundary

The neutral plan/source barrier was sealed before reading scientific parent
content, at 2026-10-12T22:13:30.981388+00:00. The six supplied identities were
first checked mechanically, then every scientific parent was read in full
without truncated content. Exact immutable source copies and complete-read
coverage are in `graph_energy_independent/`.

| Allowed input | SHA-256 | Complete extent |
|---|---|---|
| BV_PULSE_WORK_INDEPENDENT.md | 0af3a48b0604b6dfd530dfc901d81e789a89ef65b89d43391ed351f6f0ac95d9 | 545 lines |
| BV_PULSE_WORK_CROSSCHECK.md | 741b3d4a73f2091768087b5cf4e3a004980632a6644eda6a19e9247164ba32b3 | 401 lines |
| ADIABATIC_PREPARATION_SYNTHESIS.md | 6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c | 888 lines |
| ADIABATIC_PREPARATION_SYNTHESIS_REVIEW.md | fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245 | 285 lines |
| TIME_SMEARED_TRANSFER_INDEPENDENT.md | 04eef4960b18d6b0e4a7f81852ddceea7fc081c855360bf613aaf9124e141984 | 696 lines |
| TIME_SMEARED_TRANSFER_CROSSCHECK.md | 46533eb1f57e866f4b3d7db23c1e41d69eac566ce16cf0eaaa489f58fccfc905 | 410 lines |

No extra canonical scientific body was needed: the actual free branches,
operator domains, ground premises and correlation conventions used here are
explicit in these read parents. Their transitive canonical source identities
are recorded there; this task does not pretend to have reaudited those bodies.
The preparation review's Local citation correction is retained: even-spin
support is in Local sections 3 and 6, especially L23-L24, not Local L10.
No fresh physical support theorem is claimed in this graph note.

Applicable AGENTS/CLAUDE, SCIENCE_WORKFLOW and skill instructions were read.
Installed physics-loop/workhorse entries and the three loaded physics-loop
references were byte-identical to cached origin/main
516cb69d8487ff04f8a48e065d3dcbe71d7dd237. No fetch was performed: read-only
Git source inspection identified instructions without changing refs or the
working tree. No scientific program, numerical/symbolic/formal runner,
installation, repository edit, PR, audit, checkpoint, other-chat message or
subdelegation occurred. Only this assigned note and its evidence directory
were written. Editable prompt files changed: none. Platform-supplied
instructions were not modified.

The forbidden graph-energy preparation/correlation root probes, their seals,
prepared-pulse robustness probe, other new candidate outcomes, checkpoint,
HANDOFF and queues remain unexposed through this proof's freeze. The full
author reread, mechanical source stability checks and final frozen hash/time
are recorded in the evidence directory. Those bookkeeping checks bind the
argument's identity; they do not prove the mathematics. The unresolved
verification limit is an independent check of this exact completed proof,
with shared-parent/model risks disclosed. No comparison outcome is predicted.


## Publication provenance and dependency scope

The installed [evidence map](../.claude/science/physics-loops/toe-energy-protocol-20261012/EVIDENCE_MAP.json)
indexes every accepted source-package member and all 211 original aliases.
The original/copy manifests, correction records, complete source diffs,
line-piece map and canonical-parent history remain losslessly archived.
The [publication map](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_EDITS.json)
records every new wrapper substitution and full publication diff. All four
accepted scientific bodies retain their exact bytes, including the two
previously accepted wording corrections. No further body edit is made.

The [source review](../.claude/science/physics-loops/toe-energy-protocol-20261012/ENERGY_PROTOCOL_SOURCE_ROOT_REVIEW.json)
and [root reconstruction](../.claude/science/physics-loops/toe-energy-protocol-20261012/ENERGY_PROTOCOL_SOURCE_ROOT_RECONSTRUCTION.json)
state the actual earlier read and mechanical coverage. The distinct
[publication acceptance](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_ROOT_ACCEPTANCE.json)
and [publication review](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_ASSEMBLY_REVIEW.txt)
must be supplied by root before guarded integration can install this note.
The [identity tool](../scripts/bv_graph_energy_protocol_identity_2026_10_13.py) checks source bytes and reconstruction
only, with zero mathematical predicates. Its cache is integration evidence,
not a proof, analytic formal check, new independent review or audit.

The canonical source dependencies are the supplied [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Concrete](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Local](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[energy transfer](ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[bounded interaction and ground](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[preparation](ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[response](EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md), and
[time averaging](TIME_AVERAGED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-12.md).
`ACCEPTED_DEPENDENCY_MAP.json` in the installed packet distinguishes their actual roles for each source body.
In particular, time averaging is used by the graph-word argument; it is not
a premise of the driven-state theorem. The separate driven-state companion uses the BV body here. Its prepared-pulse
and driven-state results are not premises of this note. That source-role statement does
not import every theorem in a cited combined note.

The finite-energy pulse core and comparison remain explicitly archived
provisional inputs; no absent canonical pulse note is silently replaced by
the different finite-energy sector-selection note. Local sections 3 and 6,
especially L23-L24, supply physical cell support; L18 fixes the field
normalization. Historical Local L10 support attributions in inherited sources
are corrected only in their already identified published copies or records.

The task used the checkout reported by root as clean at
`4ff0ff1d7868b24d7854428110512daed13530f9`, branch
`physics-loop/toe-energy-protocol-20261012`, stacked on regular PR9506.
Root reported main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`.
The source and publication-preparation workers ran no Git commands.
Exact file hashes were checked. Root execution must separately verify the
branch, exact base, clean state, parent identities and frozen source bytes. Front-matter dependency traversal
records the transitive source graph; it is not a complete proof or audit of
that graph. Existing parent status text and formal appendices confer no new
analytic verification on these arguments.

The supplied dynamics, representation, state/control/readout prescriptions,
actual gaps, support restrictions and stated convergence resources remain
hypotheses. Every counterexample retains its original actual-model or abstract
scope. No new low-block, phase-space/escape, energy-distribution/weighted-trace,
smooth-high-band or checkpoint/queue contents are included in this assembly.
The graph/native correction record is archived whole for byte preservation;
only its graph wording item 2 changes a selected body here.

At publication-preparation freeze, no scientific, numerical, symbolic or
formal program, proposed identity tool or publication driver had been run.
No checkout, checkpoint, queue, editable prompt, axiom, Git/PR or audit surface
was changed by either worker. The guarded program and new publication wrappers
require root review of their exact bytes before execution. Later execution
records report actual integration outcomes; formal retained status remains
with the independent audit path.
