# Finite-projection mixed energy and curvature target

Status: proposed_retained
Claim type: bounded_theorem
Date: 2026-09-27
Runner: [finite_projection_mixed_curvature_2026_09_27.py](../scripts/finite_projection_mixed_curvature_2026_09_27.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The photon calculations need observable-specific sampling and extrapolation control before interpreting size trends."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Control the stated curvature functional under projection age, population, probe field and joint sampling before a physical or volume interpretation."
conditional_surface_status: "Exact finite-matrix weighted-generator identities and finite examples for supplied guides and initial distributions."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The model, guide, initial law and estimator are supplied hypotheses; no physical photon or resampling-limit theorem is asserted."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and imports

**Target.** Identify the exact-distribution benchmark of an importance-guided
continuous-time projector and its mixed local-energy average. Give an exact
susceptibility example in which both guides have the correct zero-field energy
at every projection age but have different, incorrect finite-age curvatures.
This separates observable-specific projection error from population error.

The matrix H is finite, real symmetric, and stoquastic: H(x,y)<=0 for x!=y.
The guide psi is strictly positive and p0 is a nonzero nonnegative probability
column. Time t>=0, a field-dependent family when used, and a reported average
over finitely many ages are supplied. All generator and weighting operations
in the benchmark are exact. We do not prove convergence of an empirical
population or a particular resampling method to that benchmark.

| Input | Status | Remaining bridge |
| --- | --- | --- |
| H, psi, p0 and projection ages | Supplied mathematical choices | No derivation or physical preparation asserted |
| Continuous-time rates and local-energy weights | Supplied algorithm, analyzed below | Finite implementation and population errors remain separate |
| Mixed local energy and its field curvature | Supplied estimator | A measured detector observable is not identified |
| Finite matrix evolution and rational examples | Conditional mathematics | No large-volume or physical limit follows |

The primitive registry was checked at main base
e37967e326c2bdb429bd3106d34158bd5420e9c0. No registered units, kinetic form or
pointwise realized-state primitive is needed for this finite-matrix result.
No axiom or primitive is added. No fit or observed value enters its proof.

## Proof obligations

The entrywise generator identity determines the unnormalized evolution.
Positivity makes normalization legitimate. Commuting H with its exponential
identifies the local-energy mean and logarithmic derivative. A two-state
matrix exponential then gives the mixed-energy witness. Expanding its
field-dependent counterpart to second order gives the curvature identity.
Finite time averaging preserves that identity term by term. Covariance bounds
below use only the stated marginal variances and correlation hypotheses.

For a downstream photon inference, population convergence, projection error
for curvature, probe-field remainder and physical observable identification
are unresolved obligations, not premises silently discharged by this theorem.

## Weighted generator and the two boundaries

Let D=diag(psi), chi=D^-1 p0, and define the row generator Q by

    Q(x,y) = -H(y,x) psi(y)/psi(x), x!=y,
    Q(x,x) = -sum_(y!=x) Q(x,y).

The local energy is E_L(x)=(H psi)(x)/psi(x). Comparing diagonal and
off-diagonal entries gives

    Q^T - diag(E_L) = -D H D^-1.                         (1)

The finite-state weighted forward equation therefore has solution

    f_t = D exp(-t H) chi,
    Z(t) = 1^T f_t = psi^T exp(-t H) chi.                (2)

The exponential of a finite Metzler matrix preserves the nonnegative cone;
equivalently its shifted power series has nonnegative coefficients. Its
positive diagonal term ensures f_t is nonzero when p0 is nonzero. Hence Z>0.
No irreducibility or simple ground state is needed for finite t.

For exact normalized distributions at every step, local-energy averaging is

    E_mix(t) = E_L^T f_t / Z(t)
             = psi^T H exp(-t H) chi / Z(t)
             = -d log Z(t)/dt.                         (3)

Here symmetry gives E_L^T D=psi^T H. Normalization after intermediate steps
only removes scalar factors and leaves (3) unchanged. This observation is not
a convergence theorem for systematic resampling of finitely many walkers.

The right boundary is chi=p0/psi. It equals a multiple of psi only when
p0 is proportional to psi squared. Generally (3) is a mixed expression,
not a Rayleigh quotient, and need not lie above the ground energy. An initial
random bank specifies p0 conditional on that bank; averaging over banks is a
separate operation because (3) is a ratio.

For H=[[0,-1],[-1,0]], p0=(1/2,1/2), guide (1,1) gives E_mix=-1 for all t.
Guide (1,2) instead gives

    E_mix(t) = -(9 exp(2t)+1)/(9 exp(2t)-1).

At t=log(2)/2 this is -19/17, strictly below the ground energy -1. Replacing
p0 by (1/5,4/5) changes the same-guide answer to -17/19. The difference
comes from the changed right boundary, not a numerical error estimate.

## Curvature can be wrong when the zero-field energy is exact

Let a>0 and real c,beta be supplied, and set

    H_h = [[c h,-a],[-a,-c h]],
    psi_h = (exp(beta h), exp(-beta h)),
    p0 = (1/2,1/2).

Its ground energy is -sqrt(a^2+c^2 h^2), with susceptibility
chi_ground=-E_ground''(0)=c^2/a. Write gamma=sqrt(a^2+c^2 h^2) and
C=cosh(2 beta h). Since H_h^2=gamma^2 I,

    exp(-t H_h) = cosh(gamma t) I - sinh(gamma t) H_h/gamma.

In (3), psi_h^T chi_h=1 and psi_h^T H_h chi_h=-a C. Thus

    E_mix(t,h) = -gamma (a C + gamma tanh(gamma t))
                         / (gamma + a C tanh(gamma t)). (4)

At h=0 this is -a for every t. For a direct derivative, put A=a C and
z=tanh(gamma t), and consider F(gamma,A,z)=-gamma(A+gamma z)/(gamma+A z).
At gamma=A=a,

    F_z=0, F_A=-(1-z)/(1+z), F_gamma=-2z/(1+z).

Also gamma=a+c^2 h^2/(2a)+O(h^4) and
A=a+2a beta^2 h^2+O(h^4). The possible h^2 change in z drops out because
F_z=0 there. Using (1-z)/(1+z)=exp(-2at) gives the exact derivative

    chi_mix(t) = (c^2/a)(1-exp(-2at))
                              + 4a beta^2 exp(-2at).    (5)

A common uniform guide has beta=0 and omits the second term. Both guides
still have the exact zero-field energy at every age. With a=1, c=2,
beta=1/2 and t=log(2)/2, the susceptibilities are respectively 5/2 and 2,
whereas the ground susceptibility is 4. These are finite supplied examples;
they do not estimate a cubic ring model's bias or rank its actual guides.

For any fixed positive ages t_j and nonnegative weights w_j summing to one,
the susceptibility of sum_j w_j E_mix(t_j,h) replaces exp(-2at) in (5)
by sum_j w_j exp(-2at_j)>0. This follows by differentiating a finite sum.
Changing the initial law or the ages with h requires extra derivative terms
and is outside that particular formula. The general expression (3) remains
applicable to each supplied field.

## Dated source mapping and covariance qualification

The motivating population series is PR9356 at commit
`1f2e49a0b1b9a2f84f8abc099020baf3655c1518`, inspected on September 27.
Its source is
`scripts/ring_model_12_cubed_curvature_population_series_in_both_guide_schemes_2026_09_26.py`.
Runner SHA-256: `9cf868253ee64f6d4ca2914f2afea94e53900e5848cc600029b513647a06955d`.
The source mapping is dated provenance, not a scientific input to the proof.

Its run_Ed requests Lcs=(0,). The stored current-step-weighted endpoint
energies are averaged after therm=ngen//4. For ngen=2000 and dtau=.015,
the exact-distribution benchmark of that reported functional is

    (1/1500) sum_(j=501)^2000 E_mix(.015 j),             (6)

with ages 7.515 through 30. It is not just the energy at age 30 or a log-growth
estimate. No event-cap correction, population convergence rate or numerical
bias magnitude is inferred from (6). The finite VMC bank, conditional on its
realization, supplies the initial p0. The bank seed changes with population.

The source then reports the three-field stencil

    [15 Ebar(0)-16 Ebar(H1)+Ebar(2H1)]/(9 pref N H1^2).

This is not literally the derivative in (5). Its intermediate quadratic
coefficient divides the same numerator by 12 H1^2. For an even expansion
Ebar(h)=E0-A h^2-B h^4-C h^6+..., that coefficient is
A-4 C H1^4+..., and the source uses the supplied normalization
A=3 pref N chi/4. An odd contribution L1 h+L3 h^3 instead adds
-7 L1/(6 H1)-2 L3 H1/3. Thus both symmetry and finite-probe remainder
need control for the relevant finite-bank functional. Formula (5) alone
certifies neither that stencil nor its physical normalization.

The two guide schemes reuse initial-bank and seed labels at each population,
and field runs consume their RNGs sequentially. An identical middle-field
Hamiltonian and guide therefore do not establish an identical realized
middle-field observation: earlier runs can consume different random draws.
Exact cancellation requires the same observed value, not merely its same
distribution. Zero cross-scheme covariance and its sign are not established.

More generally, for paired estimates P_i,C_i with marginal standard deviations
s_i,t_i, set X=sum_i(alpha_i P_i-gamma_i C_i). If different i are independent,
but each within-pair correlation is unrestricted, then

    sum_i (|alpha_i|s_i-|gamma_i|t_i)^2
      <= Var(X) <= sum_i (|alpha_i|s_i+|gamma_i|t_i)^2.  (7)

This is Cauchy-Schwarz on each covariance; both endpoints can be attained
with rank-one pair covariances and independent pairs. With unrestricted
covariance across all variables, the standard deviation is at most
sum_i(|alpha_i|s_i+|gamma_i|t_i), by the L2 triangle inequality. These bounds
are sensitivity statements conditional on the supplied marginal variances.
They do not reconstruct missing field/bin/bank covariance, certify the
published marginal errors, or supply a revised significance.

The source's three population settings and its assumed 1/N fit concern one
finite algorithm at fixed settings. Its own note qualifies its rough errors
and extrapolation ansatz. The exact examples above show why a stable finite
population trend alone cannot establish the ground curvature. They do not
contradict the cached outputs or prove that the observed gap has a specific
cause, sign, magnitude or large-volume limit.

## Checks and disposition

The paired runner uses only standard-library rational arithmetic. It checks
entrywise forward generators for nonuniform guides, normalized semigroup
composition, both boundary examples, second-order field expansions with an
arbitrary second-order change in tanh, finite averaging, generation indexing,
finite-probe monomials and covariance extremizers. The general identities are proved above; finite
fixtures do not prove population convergence or validate the source simulator.

Before a physical interpretation, preserve joint per-field/seed/bin data;
compare the same finite functional at matched initial laws; bound curvature's
projection-age and probe-field errors; then control population and size
extrapolation. The physical preparation, measured observable, units and
calibrated comparison remain open. This theorem supplies no photon
identification, framework closure or mass/cosmological transfer.

## Review record

This supplies the separate projector functional alongside the finite-path
analysis in the same publication. It does not replace that analysis or
identify their different boundary laws. A source-exposed independent check
reconstructed the generator, direct matrix Hessian, generation ages, finite
probe stencil and covariance sensitivity before this public composition.
Its receipt is `c57e10d3f1ca1e59065ad3ee937d4a311c4dae600990f4c1da4c74224998ff5e`.
That check found no consequential algebraic defect within the stated scope;
it is not an independent audit verdict or a population-limit proof.

No simulator output or private helper is needed to reproduce the public
runner. The source mapping records a dated program inspection. The five
scratch mutation families cover generator orientation, right boundary,
curvature guide term, probe stencil and covariance cross term. Combined
integration checks and independent audit remain landing obligations.
