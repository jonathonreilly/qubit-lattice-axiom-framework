---
claim_id: actual_corrector_small_time_lower_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "For the exact supplied globally normalized preparation, the actual rescaled correction error is bounded above and below by explicit positive multiples of the square root of the product of lambda and effective time on a specified small positive time interval with an explicit time-dependent lambda threshold. No actual leading coefficient, optimal growing-time window or physical covariance is established."
upstream_dependencies:
  - hstar_threshold_spectral_bounded_theorem_note_2026-10-12
  - boost_quantitative_corrector_bounded_theorem_note_2026-10-12
  - excluded_walk_boost_bracket_control_bounded_theorem_note_2026-10-11
runner: scripts/actual_corrector_small_time_lower_2026_10_12.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A small-time lower bound for the actual rescaled correction error

**Type:** bounded_theorem

2026-10-12. Bounded author derivation by `boost_kernel_dynamics`; root proposed
the mechanism and is a coauthor. All physical choices and the preparation
are exactly those in frozen B/X/Q. No prior source or evidence is changed.
The threshold source S and this full actual-error comparison have each
received a separate complete scientific reconstruction with no required
correction. Both remain conditional mathematical results; no audit verdict
or retained status is assigned.

For the actual X error `D_lambda=W_lambda-z`, this note proves, conditionally
on the exact source-specific threshold law S19, that there is an explicit
`t0>0` such that, for every fixed effective time `0<t<=t0`,

    0<liminf_(lambda->0) ||D_lambda(t)||_2/sqrt(lambda)
       <=limsup_(lambda->0) ||D_lambda(t)||_2/sqrt(lambda)<infinity.  (L1)

The norm is the full physical direct-integral L2 norm. In particular this
is the actual error, including the bounded noncommuting perturbation, the
varying residual and the complete forcing approximation. It proves sharpness
of the fixed-time square-root upper rate for this preparation on that small
positive interval. It does not assert an exact fixed-time leading coefficient,
an H1 asymptotic, a bracket-expectation lower bound or an optimal growing-time
window. Here `t` is effective time; the corresponding physical time is
`t/lambda`. The limit in L1 holds with t fixed, before any small-t limit.

## 1. Exact dependencies and constants

The [complete milestone packet](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/433f641f24296b6d8e786930bb1327f434015162/.claude/science/physics-loops/toe-boost-threshold-sharpness-20261012/) preserves the complete original note, source map,
byte-identical dependencies, author controls and separate review. Its
EVIDENCE_MAP.json provides recovery paths. The in-branch dependencies are
the [threshold theorem](HSTAR_THRESHOLD_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[quantitative corrector](BOOST_QUANTITATIVE_CORRECTOR_BOUNDED_THEOREM_NOTE_2026-10-12.md)
and original [boost theorem](EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md).
The exact frozen source identities are:

| Source | SHA-256 | Use |
|---|---|---|
| `ROOT_ACTUAL_CORRECTOR_LOWER_LEAD.md` | `763128a12903469a45069f11ce8ee8687ab60ec4711fad8d299f0be8ad931b1d` | Proposal tested here, not a premise |
| Q: `BOOST_HSTAR_QUANTITATIVE_CORRECTOR_PROBE.md` | `4b1d5a8395d1d5c79d798ef17950f7c1ce4c1e0781e2f9ec610223bc1eb69820` | Q2–Q24 physical corrector, residual and forcing bounds |
| Q selective review | `6ccba5be389898bd97ce12e53bf767dd002a3e6f282afb3cb4e010f49d86ca2d` | Completed source-bound check; no required correction |
| S: `HSTAR_THRESHOLD_SPECTRAL_PROBE.md` | `6856c6ff02c50b2357fbda4f2c0dbc2833362965df7ef2efddb3e925b463f6da` | S19–S20 free threshold law; separate complete source review recorded in the milestone packet |
| X: `BOOST_CURRENT_EXPECTATION_PROBE.md` | `a7161d796001df4af243263acbd03e731d75d0eab2d93795f4b5960eff5acb68` | Exact preparation, global normalizers, X9/X18/X20 |
| B: `EXCLUDED_WALK_BOOST_CURRENT_PROBE.md` | `903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923` | Original supplied operators and B25–B30 preparation |
| K: `BOOST_KERNEL_EFFECTIVE_DYNAMICS_PROBE.md` | `1c314fc05a26ca27e0828a70ca8132a2bad269b60c127ea37a53e11e95e087c9` | Indirect dependency through Q11, not a source of the new lower bound |

Q and its 211-line review were reread completely for this task. S was read
and authored completely at its unchanged 445-line identity in the preceding
task; its threshold-to-primitive proof and initial-source identification were
reread here. Necessary original X2–X22 and B25–B30 arguments were reread.
Complete prior physical-kernel/source reads are reused only at their recorded
unchanged identities. The source map distinguishes direct and inherited
reading coverage. A publication or review label is not a mathematical premise.
No new nontrivial spectral theorem is imported here: S contains the spectral
calculus and source-measure argument. The new manipulations below follow
from bounded-operator ODEs and continuous Hilbert-valued integrals.

Use normalized full relative-torus measure `dmu=dq/(2pi)^3` and Lebesgue
`dkappa`. Let `epsilon=|sin q|`, `n=sin q/epsilon`, and `c` be the constant
unit singlet. Write `h0=2epsilon n` in the orthonormal triplet frame
`T_j=sigma_(1,j)c`. Set, exactly as in Q2–Q3,

    c0=(2pi)^(-3/2),       m=integral f(x)dx>0,
    I0=integral dmu/(4epsilon^2),     1/12<=I0<=pi sqrt(3)/8,
    S0=203m/4,            M=8c0 S0=406c0 m,
    c_x=pi/4,
    c_e=sqrt(pi/2)+pi sqrt(6)/4,
    K_R=2c_x+c_e.                                            (L2)

The envelope is the exact positive B25/X3 packet, with `||F||_2=1`,
`|kappa|<=65/512<1/4`, and `0<m<1`. Work on the enclosing ball
`Omega={|kappa|<=1/4}`. All sections vanish outside the fixed packet support.
The physical Hilbert space is
`Hcal=L2(Omega,dkappa; ran P in the antisymmetric relative sector)`, where
`P=I-|c><c|` uses one full-torus mean in each kappa fiber.
All generators below preserve this support. Extending sections by zero
therefore gives the same norm in the full direct integral.

The exact scalar limiting source is

    a(t,kappa)=F(kappa)/Z0 integral f(x)w(kappa,x)exp[-it e(kappa,x)]dx,
    e=|x+kappa/2|+|x-kappa/2|,
    w=[1+(x+kappa/2).(x-kappa/2)
              /(|x+kappa/2||x-kappa/2|)]/4,
    1/4<=w<=1/2,        1/2<=Z0<=1/sqrt(2).

Put

    c_init=c0 ||a(0)||_2/(sqrt(2pi) I0)>0,
    C_init=c0^2 ||a(0)||_2^2 C_J,                            (L3)

where `C_J` is the explicit finite constant in S19. For a self-contained
specification of that inherited constant, use the following S10–S19 values
(the subscript S distinguishes these from the slow generator A):

    a_*=1/(4pi^2),     A_S=a_*(4/3)^(3/2),
    B_S0=A_S/6,        B_S1=A_S/24,
    C_F=8a_*/3+6B_S0+4B_S1+4/3,
    delta_S=min(1/4,I0/(2C_F)),        e0=sqrt(delta_S),
    K_F=2I0 C_F+C_F^2 delta_S+pi^2 A_S^2,
    C_rho=4B_S0/I0^2+4a_*K_F/I0^4,    c_th=a_*/I0^2,
    C_J=8C_rho e0+8c_th/e0+4(6-1/I0)/e0^2.

Here `6I0>1` follows by strict Cauchy–Schwarz from
`integral (2epsilon)^2 dmu=6` and the nonconstant function 2epsilon.
These positive finite constants are used without any fresh spectral
inference. S19 states, for all positive lambda and all real t,

    | ||J_H(t)r(0)||_2^2-c_init^2 |t|lambda |
        <=C_init lambda^2,
    J_H(t)=integral_0^t exp[-i(t-s)H_*/lambda]ds,
    r(0,kappa)=-c0 a(0,kappa)Qh0.                           (L4)

This follows by factoring the kappa scalar out of the H_* primitive,
which is independent of kappa. No threshold estimate for a general residual
is assumed. Positivity is quantitative: `||a(0)||_2>=m/(4Z0)`, so

    c_init>=2c0 m/[pi sqrt(3pi)]>0.                         (L5)

This uses the exact nonnegative preparation and the upper bound for I0,
not a numerical cone integral or a direction delta in kappa.

## 2. The actual equation and the physical residual class

In the whole physical Hilbert space, let

    H_*=H(0),      B(kappa)=sum_j kappa_j V_j,
    Pi=F_tr+|zeta><zeta|,   Q=I-Pi,
    zeta=n/(2epsilon sqrt(I0)),
    A=Pi B Pi restricted to ker H_*,
    G_lambda=H(lambda kappa)/lambda=H_*/lambda+B+E_lambda,
    V_lambda=B+E_lambda,       U_G(t)=exp(-itG_lambda).

X9 and X18 give `iW'=G_lambda W-g_lambda` and `iz'=Az-Pi g`, with
`W(0)=z(0)=0`, `Pi z=z`, and `g=c0h0a`. Subtracting these exact equations
and using `G_lambda z-Az=Q Bz+E_lambda z` gives

    iD_lambda'=G_lambda D_lambda+r+e_lambda,  D_lambda(0)=0,
    r=Q(Bz-g),             e_lambda=E_lambda z+g-g_lambda.  (L6)

In particular the sign of the actual source is positive in the error
ODE, so its Duhamel solution has the prefactor `-i`. No homogeneous tail
is appended. The globally normalized exact source remains
`g_lambda=c0 h(lambda kappa)a_lambda/n_lambda`, with the initial global
`n_lambda` and global `Z_lambda` in X5–X6. They are not fiber normalizers.

For `0<lambda<=1/16`, Q18 and Q24 give, on `0<=s<=t<=1`,

    ||V_lambda||<=1,
    ||e_lambda(s)||_2<=M lambda(1+t).                       (L7)

For completeness, the second bound retains both mechanisms:
`||E_lambda||<=lambda/32`, `||z(s)||_2<=Mt`, and
`||g_lambda-g||_2<=M lambda^2(1+t)`. Their sum is at most the right side
of L7 on the stated lambda range. A possible singlet component of e_lambda
is estimated in Hcal and is not assigned the longitudinal corrector bound.

On a physical odd triplet field define the scalar weight norm

    ||u||_W^2=integral_Omega [ess sup_q epsilon(q)|u(kappa,q)|]^2 dkappa.

This notation only requires measurable fields with the displayed finite
norm. No assertion of strong measurability into a nonseparable L-infinity
space is needed. The embedding in the separable physical Hilbert space is

    ||u||_2<=2sqrt(I0)||u||_W.                              (L8)

For a longitudinal physical `f=beta n` in ran Q, beta is even and

    integral beta/(2epsilon)dmu=0                           (L9)

at almost every kappa. This is one global relative mean, equivalently
orthogonality to zeta. Q4 proves this for the complementary projection
of every triplet. Its transverse projection is zero. The weighted bound
makes this integral absolutely convergent.

The operators B preserve triplets; z and g are triplets. Thus both r and
`r'=Q(Bz'-g')` satisfy L9. The derivatives keep the same parity and global
constraint because B and Q are independent of time. Q12's first row gives

    ||r(0)||_W<=R_init:=3M,
    sup_(0<=s<=1)||r'(s)||_W<=R_dot:=6M.                   (L10)

These are Q12 at T=0 and T=1 respectively. `R_dot` denotes the time
residual bound, not Q12's separate kappa-derivative constant.

All time derivatives here are genuine Hilbert derivatives. The fixed-support
source integral has bounded `e<=7/4`; differentiation under the integral
therefore makes g continuously differentiable in Hcal. The bounded operator
A on the kernel yields `z'= -iAz+iPi g`, with continuous Hilbert derivative.
Consequently r is C1 in Hcal and r' is continuous there. For fixed lambda,
G_lambda is a bounded self-adjoint direct-integral operator on Omega;
its norm may depend on lambda, but its group is unitary. These facts justify
the ODEs, time differentiation and integrals without q derivatives of zeta,
without a full inverse of H_*, and without weighted-space differentiability.

## 3. A time-adapted free primitive bound for the weighted class

Let f be any fixed longitudinal section satisfying L9 and `R=||f||_W<infinity`.
For `0<delta<=1`, form the physical singlet

    m_delta(kappa)=integral [beta/(2epsilon)]1_(epsilon>=delta)dmu,
    x_delta=([beta/(2epsilon)]1_(epsilon>=delta)-m_delta)c.

It is even and has zero full-torus mean. Q5–Q7, obtained by folding all eight
sine cells, give

    f-H_*x_delta=beta n 1_(epsilon<delta)+2epsilon n m_delta,
    ||x_delta||_2<=c_x R/sqrt(delta),
    ||f-H_*x_delta||_2<=c_e R sqrt(delta).                  (L11)

To identify the required input precisely, the pointwise constants in Q7
are `ess sup epsilon|beta|`; applying their bounds in L2_kappa gives L11.
For fixed delta, the corrector is also a bounded linear Hilbert map on the
longitudinal subspace: multiply by the cutoff divided by 2epsilon, then
subtract the scalar mean. Its norm is at most `1/(2delta)`. Thus it creates
a measurable physical Hilbert section; no weighted Bochner construction
is hidden in the notation.

For fixed length s and fixed x_delta, direct integration gives exactly

    J_H(s)f=-i lambda[x_delta-U_H(s)x_delta]
                  +J_H(s)(f-H_*x_delta),
    U_H(s)=exp(-isH_*/lambda).                              (L12)

Both endpoints occur. One check is
`d_s{-i lambda[x-U_H(s)x]}=U_H(s)H_*x`, with zero initial value.
If `s>=lambda`, choose `delta=lambda/s` only after applying this identity.
Unitarity and L11 yield

    ||J_H(s)f||_2
      <=2lambda c_x R/sqrt(delta)+s c_e R sqrt(delta)
      =K_R R sqrt(lambda s).

For `0<=s<=lambda`, use L8 and `s<=sqrt(lambda s)`. The same bound follows
because
`2sqrt(I0)<=sqrt(pi sqrt(3)/2)<=pi sqrt(6)/4<=K_R`;
the middle inequality follows from `4sqrt(3)<3pi`. At s=0 it is exact.
Thus, for all s>=0 and every lambda>0,

    ||J_H(s)f||_2<=K_R ||f||_W sqrt(lambda s).              (L13)

The cutoff is held constant throughout each calculation of a primitive.
Its later choice depends on the final length s. No derivative of
`delta=lambda/s` enters any identity. L13 may be applied at different
lengths inside a norm integral without differentiating those correctors.
It is a weighted-class estimate, not an estimate on the complementary
Hilbert unit ball, and does not assume a density formula for general f.

## 4. Noncommuting comparison on the primitive

Define `J_G(s)=integral_0^s U_G(s-u)du`. For any fixed f in Hcal,

    J_G(s)f-J_H(s)f
       =-i integral_0^s U_G(s-u)V_lambda J_H(u)f du.        (L14)

There are two direct checks. The primitives satisfy
`i(J_G f)'=G_lambda J_G f+i f` and
`i(J_H f)'=(H_*/lambda)J_H f+i f`.
Their difference therefore has zero initial value and source
`V_lambda J_H f`, giving L14 with the shown sign and operator order.
Alternatively insert the ordered Duhamel identity for `U_G-U_H` into
`J_G-J_H`, and interchange the continuous triangular integrals. The inner
integral is precisely J_H. Neither route moves V_lambda past J_H or H_*.

With L7 and L13, for f in the weighted class,

    ||[J_G(s)-J_H(s)]f||_2
        <=(2/3)K_R ||f||_W sqrt(lambda) s^(3/2),
    ||J_G(s)f||_2
        <=K_R ||f||_W sqrt(lambda s)(1+2s/3).              (L15)

Only J_H's input requires the weighted longitudinal class. After applying
V_lambda the section may leave that class; unitarity of U_G in the whole
physical space is sufficient. These are direct-integral operator and vector
estimates, not an average of unsupported pointwise asymptotics.

## 5. The actual time-varying residual and complete forcing error

Because r is C1 in Hcal, `r(s)-r(0)=integral_0^s r'(v)dv` there. Integrating
over the finite triangle gives the exact identity

    integral_0^t U_G(t-s)[r(s)-r(0)]ds
        =integral_0^t J_G(t-v)r'(v)dv.                    (L16)

For fixed lambda the integrand `U_G(t-s)r'(v)` is a continuous
Hilbert-valued function on that triangle and has bounded norm. Riemann
sums on the triangle converge in Hilbert norm and may be grouped in either
order; equivalently this is Bochner Fubini. No differentiation of an
operator-valued spectral projection or of the time-adapted cutoff is used.
At each v, r'(v) satisfies exactly the hypotheses of L15. Minkowski and
L10 therefore give

    ||integral_0^t J_G(t-v)r'(v)dv||_2
       <=K_R R_dot sqrt(lambda)
                      [(2/3)t^(3/2)+(4/15)t^(5/2)].

The second coefficient is `(2/3)(2/5)`, not `(2/3)^2`. Separately,
`||integral_0^t U_G(t-s)e_lambda(s)ds||_2<=M lambda t(1+t)`.

The exact solution of L6 is `D_lambda=-i integral U_G(r+e_lambda)`.
Subtracting its time-frozen free leading term, and applying L15 to r(0),
proves, for every `0<lambda<=1/16` and `0<=t<=1`,

    ||D_lambda(t)+iJ_H(t)r(0)||_2
       <=sqrt(lambda)[A_L t^(3/2)+B_L t^(5/2)]
                            +M lambda t(1+t),
    A_L=(2/3)K_R(R_init+R_dot)=6K_R M,
    B_L=(4/15)K_R R_dot=(8/5)K_R M.                       (L17)

This is a comparison of the exact solutions with their complete sources.
The perturbation and source variation are smaller than the free scale by
one power of small effective time. The lambda forcing error vanishes after
division by sqrt(lambda) at each fixed time. No limit has yet been exchanged.

## 6. A nonempty actual lower-bound interval

Set

    t0=min(1,c_init/[2(A_L+B_L)]).

All constants are finite and positive. By L5 and `M=406c0m`, even the
following completely specified interval is contained in (0,t0]:

    0<t<=t_bar:=5/[15428 pi sqrt(3pi) K_R]<1.              (L18)

Indeed `A_L+B_L=(38/5)K_R M`, and substitution of L5 gives `t0>=t_bar`.
The small size of this conservative bound is not a claim about the largest
possible interval.

Apply L4 and both triangle inequalities to L17. For every fixed
`0<t<=t0`, first take lambda to zero. The result is

    sqrt(t)[c_init-A_L t-B_L t^2]
       <=liminf ||D_lambda(t)||_2/sqrt(lambda)
       <=limsup ||D_lambda(t)||_2/sqrt(lambda)
       <=sqrt(t)[c_init+A_L t+B_L t^2].                   (L19)

Since `A_L t+B_L t^2<=(A_L+B_L)t<=c_init/2`, the lower bound is at least
`c_init sqrt(t)/2`, and the upper bound is at most
`3c_init sqrt(t)/2`. This proves L1 without supposing that the actual
ratio has a limit. Q25 is a separate compatible upper estimate; it is
not needed to infer this upper half once L17 and S19 have been established.

There is also an explicit finite-lambda statement. Define, for `0<t<=t0`,

    lambda_*(t)=min(1/16,
                    15c_init^2 t/(64C_init),
                    c_init^2/[64M^2 t(1+t)^2]).

For `0<lambda<=lambda_*(t)`, L4 places the free norm divided by
sqrt(lambda) between `(7/8)c_init sqrt(t)` and
`(9/8)c_init sqrt(t)`: its squared deviation is at most
`(15/64)c_init^2 t`, and `sqrt(79)<9`. The perturbation plus variation in
L17 is at most `(1/2)c_init sqrt(t)`, and its remaining forcing error after
that division is at most `(1/8)c_init sqrt(t)`. Hence

    (1/4)c_init sqrt(lambda t)
       <=||D_lambda(t)||_2
       <=(7/4)c_init sqrt(lambda t),
       0<t<=t0,  0<lambda<=lambda_*(t).                  (L20)

Both the positive interval and the threshold for lambda are explicit.
The lambda threshold depends on t; this is not a lower estimate uniform
down to t=0 at fixed lambda. In particular the theorem does not interchange
the small-lambda and small-time limits. It concerns exactly the rescaled
comparison error in L6, at physical time t/lambda.

## 7. Preserved failures and verification boundary

The lead's mechanism survives, subject to the stated S dependency. The
following limitations and failed shortcuts remain part of the result.

- Directly bounding `U_G-U_H` in operator norm yields an O(t^2) source
  error at fixed t. It cannot transfer the square-root-lambda lower law.
  L14 compares primitives instead and retains their proved small norm.
- Dropping the time-varying source is unjustified. Its contribution in L16
  is controlled at order `sqrt(lambda)t^(3/2)`, rather than discarded.
- Dropping e_lambda would discard the exact generator remainder and source
  normalization, form-factor and clock errors. L7 and L17 retain them in
  the full physical Hilbert space, including possible singlet parts.
- A full inverse of the initial residual is not L2: its required singlet
  coefficient is proportional to `1-1/(4I0 epsilon^2)`. Approximate range
  vectors are essential. No gap of H_* or q derivative of zeta is assumed.
- Mean subtraction in L11, both endpoints in L12, the sign and operator
  order in L14, and the full r' in L16 are necessary. The helper's explicit
  defect controls distinguish these from the correct identities.
- A fixed finite momentum fixture has a nonzero complementary gap and a
  different lambda-first primitive law. Finite checks validate
  bounded-operator algebra only; S's continuum threshold proof supplies
  the lower asymptotic. No finite mesh or fitted power establishes L1.
- The triangle estimates allow fixed-time coefficients on both sides of
  c_init sqrt(t). They do not determine the actual coefficient, an H1
  lower asymptotic, a bracket-mean lower bound, or any growing-time optimum.

The evidence packet records a distinct direct-Pauli and augmented-exponential
reconstruction of the new identities, analytic constant checks, full execution
logs, intended defect failures and the current recovery checkpoint. These
author checks are distinct from the separate complete reconstruction. The
review report is `c4b93e4fdec0e68dc0357509ed6bb0ba6b2dc0b3376e6f407cde4d972b26968d`;
its reconstruction, independent controls, later reproduction and all preserved
failures are in the milestone packet. Root is a coauthor, not the independent
reviewer. The [finite primary](../scripts/actual_corrector_small_time_lower_2026_10_12.py)
retains every original control calculation. PUBLICATION_EDITS.json and
PRIMARY_COMPOSITION.json reconstruct both full notes and both complete
primaries exactly; DELIVERY_CHECKS.md states the publication verification
scope. The result remains a conditional supplied-model theorem. No Lean
certificate, retained status, applied audit verdict, editable-prompt change
or physical-axiom change is claimed.
