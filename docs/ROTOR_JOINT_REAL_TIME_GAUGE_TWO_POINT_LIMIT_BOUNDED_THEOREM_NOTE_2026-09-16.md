---
claim_id: rotor_joint_real_time_gauge_two_point_limit_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/rotor_joint_gauge_propagation_check_2026_09_16.py
upstream_dependencies: ["rotor_uniform_compact_field_soft_response_bounded_theorem_note_2026-09-16", "rotor_joint_ground_energy_oscillator_defect_bounded_theorem_note_2026-09-16", "rotor_joint_local_gauge_characteristic_limit_bounded_theorem_note_2026-09-16"]
claim_scope: "Same supplied model: local electric/magnetic two-point propagation along arbitrary joint weak-coupling/large-volume sequences, uniformly on fixed compact time intervals; no full nonlinear gauge dynamics assertion."
---

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

# Joint-limit real-time gauge two-point functions

Same supplied model: local electric/magnetic two-point propagation along arbitrary joint weak-coupling/large-volume sequences, uniformly on fixed compact time intervals; no full nonlinear gauge dynamics assertion.

The model and state are supplied conditions. The proof uses no physical identification from another source package. Historical author checks are distinguished from current source-bound execution below.

**Matter restriction:** no additional unscaled onsite charge interaction is included. Use the normalized trace over the entire finite-volume ground space. Local probes and paths are fixed; time claims are uniform only on fixed compact intervals.

## 1. Domain and result

Use ground-energy and oscillator-defect theorem's paired quadratic Wilson/compact-rotor Hamiltonian, fixed
positive homogeneous weights, exact integer Gauss law, N_+=N_-=L^3, and
the normalized full ground-space trace rho_(g,L). Set

    G_(g,L)=calH_(g,L)-E_ground,      calH=aH,
    delta_(g,L)=C(sqrt(g)+L^-1).                           (1)

Throughout this note t is dimensionless time for calH. Physical time t_phys
corresponds to t=t_phys/a. Let u,v be fixed real finite-support link smears.
On each bounded time interval,

    rho[P(u,t)P(v)]
       ->(1/2)<u,Omega_infty exp(-it Omega_infty)v>        (2)

uniformly in t as g->0 and L->infinity jointly, with no relation imposed
between those rates. The scalar product in (2) is the ordinary complex
one-particle scalar product. Both u and v are real at the initial time.

For general local rescaled fields A_j=P(u_j)+Z(v_j), with real link smears
u_j and real plaquette smears v_j, define bounded Fourier-space vector
labels

    zeta_j(k)=u_j_hat(k)-i M(k)v_j_hat(k).                 (3)

The corresponding extension is

    rho[A_1(t)A_2]
       ->(1/2)int_(BZ) zeta_1(k)^* Omega(k)
                    exp[-it Omega(k)] zeta_2(k) dk/(2pi)^3.  (4)

Convergence in (4) is again uniform on compact time intervals. This proves
the free weighted Maxwell **two-point propagation** for the stated weak-g
joint limit. It does not assert full nonlinear field dynamics, convergence
at times growing with 1/g or L, or a fixed-positive-g photon pole/phase.

## 2. Why equal-time convergence alone is insufficient

Consider two harmonic modes with number-conserving Hamiltonian

    H_Lambda=a^*a+Lambda b^*b
                  +c sqrt(Lambda)(a^*b+b^*a),   0<c<1.  (5)

Its ground state is the same product vacuum for every Lambda, and the
observed a-mode has unchanged Gaussian equal-time correlations. Its
one-particle first energy moment is also unchanged:
`<a^*0,H_Lambda a^*0>=1`. Nevertheless the one-particle matrix is

    [[1,c sqrt(Lambda)],[c sqrt(Lambda),Lambda]],

whose low eigenvalue tends to 1-c^2. The observed real-time correlation
tends to exp[-it(1-c^2)] rather than exp(-it). The small high-energy spectral
weight carries the missing first moment. The norm of
`(H_Lambda-1)a^*0` grows as c sqrt(Lambda).

Thus neither a Gaussian equal-time state nor convergence of first energy
forms supplies (2). The new proof below controls a generator residual in
vector norm, excluding this particular missing step in the actual route.
The toy example is a counterexample to that inference, not a claim about
the charged rotor's phase.

## 3. Second moments from the annihilation estimate

For a real finite-volume link array f, write Q_f=Q(f) and
eta_f=||Q_f||_rho. Translation covariance positivity from gauge characteristic theorem gives

    eta_f^2<=delta sup_k ||f_hat(k)||^2.                  (6)

The exact commutator and the compact-field concentration theorem mean-defect bound imply

    c_f:=rho[Q_f,Q_f^*]
       =2 sum_p (Sf)_p(M^*f)_p rho(cos theta_p)
       =2<f,Omega f>+O(g^2||f||_2^2).                   (7)

The error constant is uniform in L, since the absolute coefficient sum
is at most ||Sf||_2||M^*f||_2<=w0||f||_2^2. Moreover

    ||Q_f^*||_rho^2=eta_f^2+c_f,
    |rho(Q_f^2)|<=eta_f sqrt(eta_f^2+c_f).               (8)

Because P(f)=(Q_f+Q_f^*)/2,

    rho(P(f)^2)=eta_f^2/2+c_f/4+(1/2)Re rho(Q_f^2).     (9)

It follows that, for any family with ||f||_2 and sup||f_hat|| bounded by a
fixed B,

    rho(P(f)^2)=(1/2)<f,Omega f>
                         +O_B(sqrt(delta)+g^2).         (10)

Take delta<=1, as is sufficient for the joint limit. Complex smears and
cross moments follow by real polarization and linearity; all electric
components commute. In particular,

    rho(P(f)^*P(h))=(1/2)<f,Omega h>
                         +O_B(sqrt(delta)+g^2)          (11)

for real and imaginary parts with the same uniform bounds. No inference
from convergence in distribution to unbounded moments has been made.

## 4. An exact electric equation and a norm residual

Define the Hermitian matter current by

    J_l=-partial_(theta_l) calH_m.                      (12)

For each link, ||J_l||<=2||T_l||_*, since differentiating a charge+/-1
Hermitian hopping changes only its phase. This is a Fock-space nuclear-norm
bound, independent of the surrounding rotor state.

Using E=-i partial_theta and the exact compact magnetic potential,

    [calH,P(u)]=i Z(Su)-i g J(W_E^(1/2)u).              (13)

The electric energy commutes with P(u), and the onsite term has no link
phase. There is no small-field approximation in (13). By the polar
identity M^*Omega=S,

    G P(u)rho^(1/2)-P(Omega u)rho^(1/2)
       =-Q(Omega u)rho^(1/2)
                         -i g J(W_E^(1/2)u)rho^(1/2).  (14)

Here vectors can be understood as Hilbert--Schmidt operators from the
finite ground space into the physical Hilbert space. Their norm is exactly
||.||_rho. Left multiplication by G is self-adjoint on this Hilbert space,
and G rho^(1/2)=0. This handles ground degeneracy without selecting a vector.

Equation (14) is a norm identity on smooth ground vectors. The first term
has norm <=w0 sqrt(delta) sup||u_hat|| by (6). The second is bounded by

    C g ||u||_1,                                       (15)

with fixed coefficients. To integrate this residual along free propagation
we still need a volume-uniform l1 estimate for the evolved smear. A bounded
Fourier symbol alone would not give that estimate.

## 5. Absolute summability of the square-root kernel

The following argument concerns Omega, not the polar multiplier M. The
latter generally has a directional discontinuity at zero and need not
have an absolutely summable kernel.

Let d_i(k)=exp(ik_i)-1 and A(k)=S(k)^*S(k). Away from k=0, A has rank two
and its kernel is spanned by W_E^(-1/2)d(k). Its two positive eigenvalues
are bounded above and below by fixed multiples of |k|^2 near zero; this
follows by comparing positive fixed weights with the ordinary curl, whose
two positive singular values have magnitude |d(k)|.

Put

    tau=tr A,       p=[tau^2-tr(A^2)]/2,
    Pi=I-zz^*/(z^*z),         z=W_E^(-1/2)d.

For k!=0 an explicit square-root formula is

    Omega(k)=[A(k)+sqrt(p(k)) Pi(k)]
                               /sqrt(tau(k)+2sqrt(p(k))).  (16)

It acts by sqrt(lambda) on either positive eigenvalue and vanishes on the
kernel. Thus it remains smooth when the two positive eigenvalues coincide;
no differentiation of individual eigenvectors is needed.

Near zero, tau is comparable to |k|^2 and p to |k|^4. Differentiation of
the explicit formula and of Pi gives, for derivative orders j=0,1,2,

    ||partial^j Omega(k)||<=C_j |k|^(1-j).              (17)

For example, derivatives of Pi of order j scale as |k|^-j, while sqrt(p)
has order |k|^2 and the denominator has order |k|. These estimates are
uniform in direction because the positive weights are fixed and bounded
away from zero. Away from zero the periodic symbol is smooth. The second
derivative bound is square integrable in three dimensions. Integrating by
parts outside a shrinking ball gives no distribution supported at zero:
Omega=O(|k|), its first derivative is bounded, and the boundary terms vanish
with the sphere's area. Therefore Omega belongs to H^2 of the Brillouin torus.

If K_x denotes its Fourier coefficients, Plancherel and Cauchy--Schwarz give

    sum_x ||K_x||
      <=C [sum_x(1+|x|^2)^-2]^(1/2)
           [sum_x(1+|x|^2)^2||K_x||_F^2]^(1/2)<infinity.  (18)

Any fixed finite-dimensional matrix norm may be used, changing the constant.
The absolutely convergent Fourier series equals the continuous symbol.
Hence every finite-volume kernel is exactly its periodization, and its
l1 convolution norm is bounded by a common constant K. The exponential
series in this convolution norm proves

    ||exp(-it Omega_L)u||_1<=exp(K|t|)||u||_1           (19)

uniformly in L. No finite-size cutoff is used to obtain K.

## 6. Duhamel comparison on one-field ground vectors

Set u_t=exp(-it Omega_L)u. Its Fourier supremum and l2 norm do not increase,
because the matrix exponential is unitary at each wave number. Apply (14)
to u_t and use (19). Differentiating

    exp(it G) P(u_t)rho^(1/2)

and integrating the norm of its derivative gives, for |t|<=T,

    ||exp(-itG)P(u)rho^(1/2)-P(u_t)rho^(1/2)||
        <=C_(u,T)[sqrt(delta)+g].                      (20)

All finite-volume vectors are in the operator domain, and the derivative
is continuous there; (20) is the ordinary strong Duhamel argument. It does
not invoke strong-resolvent convergence from a quadratic-form calculation.

For real u,v, stationarity of the ground trace gives

    rho[P(u,t)P(v)]
       =<P(u)rho^(1/2), exp(-itG)P(v)rho^(1/2)>.

Use (20), the uniform second-moment bound, and (11) with
h=exp(-it Omega_L)v. The result differs from
`<u,Omega_L exp(-it Omega_L)v>/2` by at most
C_(u,v,T)[sqrt(delta)+g]. The symbol in this last expression is continuous
and bounded, so its local Fourier sum tends to the integral. Derivatives
in t are uniformly bounded on compact intervals; a finite time net makes
the Riemann-sum convergence uniform there. This proves (2).

## 7. Magnetic fields by controlled approximation, not an l1 Riesz claim

For real local v, the exact definition of Q gives on ground vectors

    Z(v)rho^(1/2)
       =-i P(Mv)rho^(1/2)+i Q(Mv)rho^(1/2)
                                  +Z_perp(v)rho^(1/2).  (21)

The last two terms have norm O_v(sqrt(delta)) by Fourier covariance
positivity. The Fourier symbol f(k)=M(k)v_hat(k) is bounded and smooth off
zero, but it may be discontinuous at zero. Choose multivariate Fejer
trigonometric-polynomial approximations f_n to f. The kernels are positive
and normalized, so their Fourier suprema are uniformly bounded; they
converge in L2. The reality condition f(-k)=overline(f(k)) is preserved,
so each f_n corresponds to a real finite-support link smear.

For fixed n apply (10) to the finite-volume array with Fourier values
f(k)-f_n(k). Its l2 norm and Fourier supremum are bounded uniformly in L,n.
The quadratic form is a Riemann sum of

    [f(k)-f_n(k)]^* Omega(k) [f(k)-f_n(k)].              (22)

This integrand extends continuously at zero with value zero because
Omega(k)=O(|k|). Thus along the joint sequence,

    limsup ||P(M_L v-f_n)rho^(1/2)||^2
       <=(1/2)int [f-f_n]^* Omega [f-f_n],              (23)

and the right side tends to zero with n. For each fixed n the electric
dynamic statement applies. Unitarity of exp(-itG) controls (23) at every
time with the same error, so one may take the joint g,L limit first and
then n->infinity. The limiting one-particle unitary is also continuous in
the corresponding Omega-weighted norm. This proves magnetic/electric and
magnetic/magnetic limits, uniformly for bounded times.

Finally, (21) identifies the created vector of A=P(u)+Z(v) with that of
P(u-iMv). Sesquilinearity of the two-point function yields precisely (3)-(4),
including the sign of the imaginary electric/magnetic cross correlation.

## 8. Scope of the advance

The new input beyond the equal-time milestone is the exact electric
equation (13), which produces the controlled norm residual (14), together
with the summable Omega kernel. Magnetic recovery uses a two-stage smear
approximation; no false l1 bound for M is inserted. The second-moment
argument is explicit and is not delegated to characteristic convergence.

This note proves only the proposed two-point propagation theorem on fixed
time intervals and fixed local probes. It does not prove real-time limits
of arbitrary gauge-field exponentials or higher unbounded field products.
For the magnetic equation, products of electric fields with compact
cosine defects introduce higher-moment obligations that were bypassed here,
not discharged. The fixed-positive-g infrared phase is still open.

## No-Go Discipline Gate

N1: this is a positive supplied-model theorem. Fixed-positive-coupling infrared behavior, nonlinear gauge dynamics, growing-support limits, finite-clock realization and native law selection are open directions, not five completed exclusion attempts. No broad negative certificate is claimed.

N2: the model assumptions are stated hypotheses, not independent physical walls. The finite counterexamples refute only the particular inference specified beside them.

N3: the proof retains the normalized full ground trace, possible ground degeneracy, exact Gauss constraint, fixed coefficients, observable domain and order-of-limits quantifiers. Notes requiring free matter exclude an extra unscaled onsite charge interaction.

N4: the supplied continuous rotor/CAR carrier, Hamiltonian, homogeneous weights, Wilson parameters, time and ground ensemble are conditional inputs. Linked proofs below are the actual mathematical dependencies; historical campaign pins confer no authority or additional premise.

N5: the paired programs report finite element/site/mode/block coverage and unchanged tolerances. Uniform-volume estimates, arbitrary joint-sequence convergence and bounded-time analytical arguments are written proofs, not executed infinite-lattice simulations.

N6: conditional mathematical progress does not select the supplied model from the framework axioms or require a new axiom.

N7: alternative interacting fixed-coupling constructions and different physical carriers remain open. Neither finite check success nor the explicit toy counterexamples excludes them.

N8: original personal reviews, failed runs and 28 mutation failures are historical evidence, preserved with their original source hashes. They are not fresh independent review or an audit verdict.


## Mathematical dependencies and current evidence

Actual load-bearing proofs: [compact-field concentration theorem](ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md), [ground-energy and oscillator-defect theorem](ROTOR_JOINT_GROUND_ENERGY_OSCILLATOR_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-16.md), [gauge characteristic theorem](ROTOR_JOINT_LOCAL_GAUGE_CHARACTERISTIC_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md).

The Fourier covariance bound used in section 3 is proved in section 2 of the linked gauge characteristic theorem. Its characteristic-function conclusion is not substituted for the separate second-moment argument.

Reproduction programs: [rotor_joint_gauge_propagation_check_2026_09_16.py](../scripts/rotor_joint_gauge_propagation_check_2026_09_16.py). Each declares 120 seconds; all calculations and tolerances retain the original finite scope.

Current canonical caches: [rotor_joint_gauge_propagation_check_2026_09_16](../logs/runner-cache/rotor_joint_gauge_propagation_check_2026_09_16.txt). These links describe the required current evidence; historical outputs do not certify the new source bytes.

[Original recovery](work_history/review_loop/pr8160/README.md) and [exact manifest](work_history/review_loop/pr8160/original-manifest.json) preserve all 86 original files, including full proof development, original outputs, failed propagation runs and mutations.
