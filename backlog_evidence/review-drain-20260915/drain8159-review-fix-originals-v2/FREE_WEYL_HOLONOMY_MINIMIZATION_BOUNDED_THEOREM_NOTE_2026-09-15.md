---
claim_id: free_weyl_holonomy_minimization_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/holonomy_check_2026_09_15.py
upstream_dependencies: ["docs/POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md"]
claim_scope: "Bounded conditional free Weyl holonomy selection; supplied hypotheses and limit order retained in full proofs."
---

# Free Weyl holonomy selection

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

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14](POSITIVE_FINITE_CYCLIC_GAUGE_HISTORIES_AND_LOCAL_CHARGED_ROTOR_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-14.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK20_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK20_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Block20 route and no-go review

Provisional author review; no independent audit.

N1 — Routes. Poisson summation extracts the actual lattice leading finite-size
energy. The local conical cusp excludes node hits for every phase configuration.
For the supplied diagonal-cone arithmetic example, the positive theta product
determines the global minimum. Local C2 convergence supplies lattice stability.
Heat quadrature and literal lattice sums are distinct finite calculations.

N2 — Independence. The free finite-size minimum is conditional input for a future
gauge reduction, not a second proof of the periodic interacting spectral floor.
The explicit twist alternation is a global-boundary statement, not a new bulk wall.

N3 — Hidden premises. Constant occupied rank, untilted isolated elliptic cones,
no pockets and smooth spectator bands are explicit. Diagonal G is used only for
the exact minimizing point. The arithmetic parameters b=kappa=pi/3 and the two
volume subsequences are not generalized. The physical parent has paired opposite
charges, whose occupied energies add after conjugation.

N4 — Matching. A single Weyl cone contributes one negative energy; the four cones
give 4K, consistent with the continuum Dirac normalization after counting modes.
The general periodic kernel's singularity is negative norm, so a node hit is not
a minimum. Hessians are not obtained by absolutely differentiating its |m|^-4
Fourier series. The a_2 subtraction and |m|^-6 remainder justify local C2 control.

N5 — Rhetoric. The free one-particle gap is order 1/L and vanishes in the bulk.
The conditional g/L scale is a global gauge-coordinate oscillator. Neither is
an interacting photon/mass theorem. The asymptotic lattice minimizer is proved
exact only for sufficiently large sizes; finite tests do not supply its threshold.

N6 — Partial closure. The free finite-volume preferred twist and its curvature
are determined for the declared example, including a concrete failure of a
volume-independent global twist. Local free correlations still have a common limit.
The interacting normal-mode/matter integration and uniform error bound remain open.

N7 — Steelman. Twists may alternate while local physics converges; this is the
explicit escape from an apparent thermodynamic inconsistency. With other node
positions or non-diagonal metrics the minimizing point can change, but the
general cusp-avoidance result remains. A mass or Fermi pocket would change the
hypotheses and must be analyzed separately.

N8 — Cross-cycle echo. The finite-ring Gauss cancellation in Block19 does not
justify discarding the three-dimensional Berry connection. The existing parent
provided a single-box nonzero twist preference; this block adds a declared free
large-volume result, not a rebranding of that finite certificate. No axiom fails.

Finite evidence: theta image/Fourier overlap error6.67e-16; independent Fourier
energy cutoff error1.91e-9 at radius48. The four-cone limiting Hessian has diagonal
(0.4418297127,0.4418297127,0.1579285375). L72 finite-band scaled Hessian differs by
0.00218, and the three Casimir differences by at most0.01052. The scaled free gap
is5.1207 versus limiting pi sqrt11/2=5.20974, so finite-size error is visible and
not hidden. A central finite-difference Hessian agrees within9.02e-8.

Failure provenance: the first runner transposed an already correctly ordered
derivative array, causing a shape exception before the finite-band checks. Its
note/source/stdout/stderr are frozen in review/block20_initial_check_failure.
Removing that transpose fixes the shape without changing any tolerance or formula.

Disposition: provisional free-comparator theorem; no model/phase/axiom no-go.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK20_WEYL_HOLONOMY_CASIMIR_SELECTION

Original source identity: `BLOCK20_WEYL_HOLONOMY_CASIMIR_SELECTION.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Free Weyl holonomy selection, volume arithmetic, and the remaining dynamical step

Status: proposed analytic results for a declared free-band comparator, with author
checks; no independent audit and no interacting phase theorem. All energies below
use a=1 until section 6. The supplied paired Wilson model is the free matter part
of the positive cyclic parent on main e0ef7cf4633034a8c1e6d57f5812cc4275bf1349.
It is not the mixed four-orbital model used in Blocks11–14. A flat link background
is prescribed here, not obtained by integrating fluctuating gauge links.

#### 1. Hypotheses and Fourier coefficient

Let e(k) be the occupied-band trace of a periodic analytic finite Bloch matrix
on the three-torus. Assume constant occupied rank away from finitely many isolated
untilted simple Weyl nodes, no other Fermi surface, and separated spectator bands.
For node nu at k_nu let G_nu=V_nu^T V_nu>0. In local coordinates assume

    e(k_nu+p)=s_nu(p)-sqrt(p^T G_nu p)+a_2,nu(p)+r_3,nu(p),

where s is smooth, a_2 is homogeneous of degree two and smooth on the unit sphere,
and |partial^alpha r_3(p)|<=C_alpha |p|^(3-|alpha|). Analytic isolated linear
two-band crossings satisfy this local symbol expansion. Any tilt which changes
occupied rank, extra Fermi pockets, zero charge, or nonelliptic crossing is outside
this theorem. Different charged blocks may be summed; charges are q_nu=+/-1.

With Fourier convention ehat(R)=(2pi)^-3 integral e(k) exp(-i R.k) dk, the leading
coefficient is

    ehat(R)=sum_nu exp(-i R.k_nu) /
      [pi^2 sqrt(det G_nu) (R^T G_nu^-1 R)^2] + O(|R|^-5).          (1)

The normalization and sign follow directly from Delta_p |p|=2/|p| and
FT1/|p| (`R`)=1/(2pi^2 |R|^2), hence FT[-|p|]=1/(pi^2 |R|^4) away R=0.
Changing variables u=V p gives the stated anisotropic factor. A smooth cutoff
around each node changes the principal homogeneous transform only by a rapidly
decreasing term. For the remainder, a dyadic shell of radius r contributes at most
C_M r^5(1+r|R|)^-M; summing shells with M>5 proves the O(|R|^-5) bound. Applying
the same argument to r_3 gives O(|R|^-6). These bounds are uniform in direction.

#### 2. The finite-size energy and its node-avoidance property

For a charged block sample k=(2pi n+q phi)/L and sum its occupied energies.
Absolute convergence of the Fourier coefficients justifies the exact grid identity.
Writing theta_nu,L=L k_nu mod 2pi and e_bulk=sum_blocks ehat_block(0), one obtains

    E_L(phi)=L^3 e_bulk + L^-1 F_ThetaL(phi)+O(L^-2),               (2)
    F_Theta(phi)=sum_nu K_Gnu(q_nu phi-theta_nu),
    K_G(alpha)=1/(pi^2 sqrt(det G)) sum_(m!=0)
                 cos(m.alpha)/(m^T G^-1 m)^2.                    (3)

The error in (2) is uniform over phi. Formula (3) is absolutely convergent for
the energy, not for its twice-differentiated series. Derivatives used below come
from the local singularity decomposition or a heat representation, never from
unjustified absolute differentiation of (3). The continuum Casimir normalization
agrees with the massless torus energy in Bellucci–Saharian, equation47, after using
one Weyl occupied mode per cone and multiplying density by volume:
https://arxiv.org/html/0902.3726 . This is a normalization check, not an imported
lattice or gauge-interaction theorem.

Periodize a cutoff times -sqrt(alpha^T G alpha). Its nonzero Fourier coefficients
agree with (3) up to a rapidly decreasing sequence. Consequently K_G is smooth
off alpha=0 mod2pi, with local form -sqrt(alpha^T G alpha)+smooth. At a twist
where one or more nodes hit grid points, for every nonzero direction v,

    F(phi+t v)+F(phi-t v)-2F(phi)
      =-2|t| sum_hit |q_nu V_nu v|+O(t^2)<0.                     (4)

Thus a node-hit twist cannot minimize the free Casimir energy. This is a local
concave cusp statement; it does not assert uniqueness of the minimum. For fixed
finite lists of elliptic G_nu and charges, the phase parameters Theta range over
a compact torus. The set of all (Theta,phi) with phi minimizing F_Theta is compact.
It is disjoint from the closed node-hit set by (4); therefore their phase-distance
has a positive lower bound d_*, uniform over Theta. Uniform convergence in (2)
then excludes distances <d_*/2 from every actual finite-L minimizer for sufficiently
large L. One proves this last assertion by taking a contradicting subsequence and
passing to a limiting minimizing pair. No numerical value of d_* is claimed.

It follows that the minimum free one-particle excitation energy at an optimizing
twist is bounded above and below by positive constants times 1/L. The upper bound
uses a nearest grid point to a node; the lower bound uses d_* and ellipticity,
with spectator bands separated. It is not a nonzero bulk gap.

#### 3. Derivatives away from nodes

Retain the degree-two term a_2 in the shell expansion. Its Fourier principal part
defines a periodic function J_Theta whose local singularities are the corresponding
a_2 and which is smooth elsewhere. Polynomial parts contribute only smooth terms.
The degree-three remainder has Fourier decay |R|^-6. Since sum_m |m|^-4 is finite
in dimension three, two derivatives of its rescaled grid sum are bounded. Thus on
any closed set separated from all node-hit twists,

    L(E_L-L^3 e_bulk)=F_ThetaL + L^-1 J_ThetaL + O_C2(L^-2).        (5)

In particular the Hessian converges uniformly there. This extra argument is needed:
uniform convergence of energies alone would not control minimizing curvatures.

#### 4. An exact alternating choice in the supplied paired Wilson family

Take b=kappa=pi/3, zeta=cos(kappa)=1/2, and

    h0(k)=sin(kx) sigma1+sin(ky) sigma2
            +(2+zeta-cos(kx)-cos(ky)-cos(kz)) sigma3,
    h_plus(k)=h0(k-b ex),   h_minus(k)=h_plus(-k)^*,

with charges +1 and -1 respectively. The free ground at half filling has exactly
one occupied state per momentum per species, so its total charge is zero.
Conjugation and n->-n give the exact finite-grid identity

    E_L(phi)=2 sum_n [-|d0((2pi n+phi)/L-b ex)|].                  (6)

The four cones have G=diag(1,1,3/4). For L divisible by three, their effective
twist phases coincide after charge conjugation, and F=4K_G(phi-theta_L), where

    theta_L=(0,0,0) for L=6m;    theta_L=(pi,0,pi) for L=6m+3.    (7)

For diagonal G with entries G_i>0, use 1/x^2=integral_0^infinity t exp(-t x)dt:

    K_G(alpha)=1/(pi^2 sqrt(det G)) integral_0^infinity
       t [product_i Theta(t/G_i,alpha_i)-1] dt,
    Theta(s,alpha)=sum_n exp(-s n^2) cos(n alpha)>0.               (8)

The integral converges at both endpoints, including alpha=0 (integrand O(t^-1/2)
there). Jacobi's product, DLMF20.5.3, writes each Theta as a product of positive
factors 1+2 exp(-(2n-1)s) cos(alpha)+exp(-(4n-2)s), times alpha-independent
positive factors. Each factor is strictly increasing in cos(alpha), so Theta has
a unique minimum at alpha=pi. The positive product in (8) therefore gives a unique
global minimum of K_G at (pi,pi,pi). At that point its Hessian is diagonal and
strictly positive: each first theta derivative vanishes, each second derivative
is positive, and the heat integral converges. Sources:
https://dlmf.nist.gov/20.5.E3 and https://dlmf.nist.gov/20.2.E3 .

For the lattice model, e0(k) is even in each coordinate. Hence (6) is exactly
stationary whenever phi_x-Lb, phi_y, phi_z are each 0 or pi, away from node hits.
Equation (5), the strictly positive limiting Hessian, and the unique limiting
minimum imply strict convexity near the limiting minimum and exclusion of all
other regions for sufficiently large L in each subsequence. Thus the unique
global minimizer is EXACTLY

    phi_*=(pi,pi,pi) for L=6m;
    phi_*=(0,pi,0)   for L=6m+3,                                 (9)

for all sufficiently large L in the indicated subsequence. No explicit threshold
L is proved; small-box numerical optimization does not establish this qualifier.
The nearest node is half a momentum mesh step away in each coordinate, so

    lim L Delta_sp(L,phi_*)=pi sqrt(1+1+3/4)=pi sqrt(11)/2.        (10)

This explicit finite-size alternation prevents a single volume-independent global
twist from being inferred from free-energy minimization. It does not prevent a
local bulk state: the free occupied projectors are bounded and continuous except
at finitely many nodes, so their shifted Riemann sums converge to the same local
correlation integrals for every twist sequence. Wick's rule then handles every
fixed-support free observable. The special arithmetic choice b=kappa=pi/3 is
declared, not asserted for a generic or axiom-selected parameter.

#### 5. Meaningful companion checks

The companion runner compares (8) with the literal finite Bloch sum (6), analytic
finite-band Hessians with heat-integral Hessians, and the exact doubled energy with
the two oppositely charged blocks. It checks the gap coefficient in (10). The heat
calculation switches between Gaussian-image and Fourier theta representations and
checks their overlap. Large-volume samples test convergence; the proof of the
global minimum is the positive product plus (5), not sampled minimization.

#### 6. Conditional slow holonomy dynamics and the unresolved step

For a cubic box of side L, a harmonic connection is A_i=phi_i/L on every i-link,
and its conjugate uniform flux is E_i=n_i/L^2. Summing E dA over L^3 links gives
sum_i n_i dphi_i, while the harmonic electric quadratic form is

    H_harm=g^2/(2aL) sum_i w_i n_i^2.                            (11)

Matter charge offsets and Berry connections may shift these momenta. If one proves
an effective reduction with sufficiently small remainders to

    H_eff=(aL)^-1 [g^2/2 (-i partial+A_B)^T W_E(-i partial+A_B)
                          +F_Theta(phi)+corrections],             (12)

then a nondegenerate well has leading level spacings g/(aL) times square roots of
the eigenvalues of W_E^(1/2) Hess(F) W_E^(1/2). A smooth bounded local connection
does not alter the leading oscillator frequencies. Neither (12) nor errors uniform
in growing L are proved here. Integrating normal gauge fluctuations and matter
excitations could produce corrections on the same scale unless controlled.
Consequently g/L is a conditional global-mode scale, not a proved interacting
bulk photon, mass gap, or continuum-limit result. Block19's exact charged ring
does not supply the missing cubic reduction. No axiom update follows.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: holonomy_check_2026_09_15](../scripts/holonomy_check_2026_09_15.py); [current cache](../logs/runner-cache/holonomy_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
