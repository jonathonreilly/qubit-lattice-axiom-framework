---
claim_id: compact_rotor_ground_correlation_comparison_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
runner: scripts/compact_rotor_ground_correlation_comparison_check_2026_09_16.py
upstream_dependencies: []
claim_scope: "05: ground-state cone comparison including the half-angle cover/parity caveat, cofinal free-box angle marginal and local electric quadratic moment limits at fixed coupling. No unrestricted thermal trace equivalence, full quantum-state uniqueness, or susceptibility monotonicity."
---

# Compact rotor ground correlation comparison

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

## Scope and provenance

05: ground-state cone comparison including the half-angle cover/parity caveat, cofinal free-box angle marginal and local electric quadratic moment limits at fixed coupling. No unrestricted thermal trace equivalence, full quantum-state uniqueness, or susceptibility monotonicity.

The complete original mathematical argument follows. Its personal reading, timing, proposal and review statements describe historical work, not a new review or current execution. Model parameters are supplied. No PR8160, PR8162 or PR8163 result is implicitly a premise. Narrow quantitative bounds and explicit witnesses do not supply a broad negative certificate or a physical phase. No five-route no-go PASS is asserted.

The supplied model and proof are redeclared here; other campaign mentions are context.

## Complete argument

# Ground-state correlation comparison on the actual compact Hamiltonian

Working bounded derivation, 2026-09-16. This adapts standard quantum
correlation-inequality machinery to integer plaquette characters on the
supplied link torus. It gives monotonicity and existence of equal-time angle
marginals in growing free boxes. It does not establish a Coulomb phase,
monotonicity of the electric susceptibility, or a unique infinite-volume
quantum ground state. All conclusions are provisional author derivations.

## 1. Scope and primary source

Consider finitely many compact angles with normalized Haar measure and

    H=(1/2) E* U E - sum_b J_b cos(b dot theta),
    E=-i gradient, U=U*>0, J_b>=0, b in Z^n.

There are finitely many interactions; U is a real positive matrix. Additive
constants in H do not affect this note. The cubic pure-gauge Hamiltonian is
the special case U=g^2 I and b equal to the oriented plaquette cycles,
J_b=g^(-2). The full-torus positive ground state is gauge invariant, hence
is the physical zero-charge ground state. A nonzero fixed charge sector,
frustrated couplings, or dynamical fermions is not covered automatically.

The source is Tadahiro Miyao, [Quantum Griffiths inequalities,
arXiv1507.05355v2](https://arxiv.org/abs/1507.05355), section5 and the
Hilbert-Schmidt cone machinery in section3 and appendixA. The downloaded
55-page PDF has SHA256
`39ad6c078d00acf512ca3209140b7f0d041eb534ec820876070852c2758ed5be`.
The rotor section, cone definitions and relevant appendix were read; this
is not a claim to have read every application in the paper. The familiar
cone method is credited to that literature. The present proof spells out
the compact covering map and handles ground states directly, so no thermal
trace identification under a half-angle change of variables is assumed.

## 2. The doubled compact carrier and its positive ground kernel

Let Psi be the unique strictly positive normalized ground wavefunction,
with energy E0. Ellipticity on the connected finite torus, bounded smooth
potential, and the strictly positive heat kernel give these properties.
For two independent link configurations set

    theta=v-u, theta'=v+u modulo2pi.

This is a2^n-to-one covering map from the (u,v) product torus to the
(theta,theta') product torus. It preserves normalized Haar measure. Its
pullback is an isometry onto a proper invariant subspace, not onto the full
product Hilbert space. The subspace is invariant under each simultaneous
shift (u_e,v_e)->(u_e+pi,v_e+pi). In Fourier variables the two frequencies
have matching parity, coordinate by coordinate.

The pullback of the doubled differential expression is

    Hhat=(1/4)(nu_u* U nu_u + nu_v* U nu_v)
                       -2 sum_b J_b cos(b dot u) cos(b dot v),
    nu_u=-i gradient_u, nu_v=-i gradient_v.

The function

    Phi(u,v)=Psi(v-u)Psi(v+u)

is a normalized strictly positive eigenfunction of Hhat with energy2E0.
On the full (u,v) torus, Hhat is again elliptic and has a unique positive
ground state. Therefore Phi is that ground state too. This observation
justifies using the enlarged torus for this ground-state argument despite
the covering restriction. It does not equate unrestricted thermal traces.

Identify L2(du dv) with Hilbert-Schmidt kernels on X=L2(du), with the
second factor conjugated. The closed cone consists of positive
semidefinite operators on X. Put T=(1/4)nu* U nu. The kinetic evolution
acts on a kernel operator Y by

    Y -> exp(-sT) Y exp(-sT).

Each interaction insertion acts as

    Y -> 2 J_b cos(b dot u) Y cos(b dot u).

Both preserve this cone. Bounded perturbation and the Trotter product show
that exp(-s Hhat) preserves it as well. Start from the rank-one constant
kernel Y=|1><1|. After multiplying exp(-s Hhat)Y by exp(2sE0) and taking
s to infinity, one obtains a strictly positive scalar multiple of Phi.
Consequently Phi belongs to the positive Hilbert-Schmidt cone. Only a
finite-volume spectral gap is used in this projection; no uniform gap is
asserted.

## 3. Nonnegative connected cosine correlations and coupling derivatives

For an integer character a write C_a=cos(a dot theta) and mu_a=<C_a>.
The doubled difference pulls back to

    Delta C_a=C_a(theta)-C_a(theta')
                         =2 sin(a dot u)sin(a dot v).

As a map on kernels this is Y->2 sin(a dot u)Y sin(a dot u), which
preserves the positive cone, for every integer a including signed cycles.
Thus for every a,b and every tau>=0, self-duality gives

    <Phi, Delta C_a exp[-tau(Hhat-2E0)] Delta C_b Phi> >=0.

The three operators preserve the covering subspace, so the left side can
also be evaluated before pullback. Expansion yields

    <Psi,C_a exp[-tau(H-E0)] C_b Psi> - mu_a mu_b >=0. (1)

All quantities are real. This is an imaginary-time connected correlation;
at tau=0 it is the usual covariance. The proof does not say that arbitrary
sine correlations or arbitrary observables have this sign.

Analytic perturbation by the bounded term -J_b C_b now gives

    partial_(J_b) mu_a
      =2 <(C_a-mu_a)Psi,(H-E0)^(-1)_perp(C_b-mu_b)Psi>
      =2 integral_0^infinity Cov_tau(C_a,C_b) d tau >=0. (2)

The integral converges in every fixed box. The possibly nonuniform
finite-box gap affects its size, not its sign. Hence increasing any of
the nonnegative cosine couplings increases every cosine character mean.
The first correlation inequality, obtained from positivity in the integer
electric basis, also gives0<=mu_a<=1. If a is outside the subgroup generated
by the interaction characters, its mean can be zero.

## 4. Electric second moments obey a different monotonicity

For a real vector f let A=f dot E. In the doubled variables,

    A(theta)^2-A(theta')^2 = -nu_(u,f) nu_(v,f).

Conjugation in the second Hilbert-Schmidt factor changes the sign of the
real momentum operator. The displayed insertion is therefore the kernel
map Y->nu_f Y nu_f, which is positive on its natural domain. To justify
this unbounded insertion, truncate nu_f in its Fourier spectral basis,
apply the cone argument there, and remove the truncation. Smoothness of
the finite-box ground kernel gives Hilbert-Schmidt convergence of the two
momentum derivatives. The cone is closed. Consequently

    Cov_tau(A^2,C_b)>=0,
    partial_(J_b)<A^2>=2 integral_0^infinity Cov_tau(A^2,C_b)d tau>=0. (3)

For the derivative, elliptic regularity and bounded analytic perturbation
give differentiability of the ground vector in the required kinetic graph
norm. Equation(3) concerns an equal-time second moment. It is not a
comparison theorem for integral <A exp[-tau(H-E0)] A>d tau. In particular,
it does not by itself compare the eta_f of BLOCK02-03.

## 5. Growing free boxes: an actual compact angle-state limit

Fix a finite-support integer link character a. Embed a smaller free cubic
box into a larger one, add the missing links first with kinetic terms only,
and then increase each new plaquette coupling from zero to g^(-2). Before
the last step the ground state factors, and the added link factors are
constant. Formula(2) proves

    mu_a(small box)<=mu_a(large box)<=1.

Therefore every fixed-support cosine character has a limit along nested
boxes exhausting the infinite lattice. Inversion symmetry makes every sine
mean zero. The character limits are positive definite and normalized because
they are limits of probability characteristic functions. They determine a
consistent family of probability measures on finite angle sets; compactness
and density of trigonometric polynomials give weak convergence of the local
angle marginals, with no subsequence choice. The directed monotonicity makes
the limit independent of the particular cofinal free-box exhaustion.

This proves a limit of equal-time commuting angle observables, without first
sending g to zero or using a time-discretization limit. It does not prove
clustering, a photon pole, a nonzero asymptotic loop order parameter, or
uniqueness among all boundary conditions or quantum ground states. Gauge
noninvariant characters vanish, so the limit retains the local gauge
symmetry.

For completeness, local kinetic moments are uniformly bounded. For a link
e, separate H=K_e+H_out+W, where W=sum of the n(e) touching plaquette
terms(1-cos F)/g^2 is nonnegative. The product of the constant link state
and an outside ground state has energy E_out+n(e)/g^2. The actual ground
therefore satisfies

    (g^2/2)<E_e^2><=n(e)/g^2,
    <E_e^2><=2n(e)/g^4<=8/g^4.                         (4)

Together with(3), this gives limits of the quadratic form <(f dot E)^2>
for every fixed-support f: it is monotone with box inclusion and bounded
by the local diagonal estimates and Cauchy-Schwarz. These moment limits
still do not identify the full noncommuting local density matrices.

## 6. What the comparison can and cannot transfer

The allowed comparison strengthens nonnegative Fourier cosine couplings
while holding the kinetic matrix fixed. A real noncompact Gaussian
reference changes the configuration carrier; a principal-angle quadratic
potential has alternating Fourier coefficients. Neither is automatically
ordered by(2). Deleting plaquettes supplies lower bounds from smaller
interaction sets, but a useful fixed-coupling phase comparator has yet to
be constructed. A perimeter estimate, even if obtained, must separately
be connected to the electric spectral target or a full physical-source
limit. The conditional susceptibility criterion in BLOCK02 remains open.

## Review and proposal status

The [claim-status contract](work_history/review_loop/pr8164/README.md) and
[premise inventory](work_history/review_loop/pr8164/README.md) apply to this author
proposal. The [negative-claim checklist](work_history/review_loop/pr8164/README.md)
records the scoped comparison restrictions and untested alternatives.
Independent review, formal registration and retained landing are pending.


## Canonical evidence boundary

[Program](../scripts/compact_rotor_ground_correlation_comparison_check_2026_09_16.py); [current stdout cache](../logs/runner-cache/compact_rotor_ground_correlation_comparison_check_2026_09_16.txt). The canonical TOTAL counts 3 completed finite control families, not each loop iteration or an analytical theorem. All original assertion expressions and tolerances are retained. No canonical capture has run during preparation. Historical outputs, failed refinements and mutations remain in the [exact recovery archive](work_history/review_loop/pr8164/README.md).
