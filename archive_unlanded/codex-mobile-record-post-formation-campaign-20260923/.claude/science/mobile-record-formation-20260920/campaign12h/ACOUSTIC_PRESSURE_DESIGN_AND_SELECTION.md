# Pressure-law freedom in immutable product-preserving exchanges

2026-09-21. Primary extension of the independently checked polynomial-flux
construction. The new identities below await a separate check. They expose
which acoustic properties the construction can supply and which it selects.

## 1. A density-dependent multiplier

Use the seven-state alphabet, rho=sum_a p_a, g_i=sum_a p_a v_(a,i),
q_i=p_(+i)+p_(-i), S_i=2rho-3q_i. For any polynomial F(rho), set the
product-current potential

    Psi_i=F(rho) S_i g_i.                                  (1)

If F has degree m, homogenize this polynomial to degree k=m+2 using
p0+sum_a p_a=1. The independently checked symmetric-tensor construction
realizes (1) exactly with fixed finite rates and a read footprint of at most
2k sites, while only swapping the two neighboring endpoint states. A fixed
positive floor is added as before. Rate size and read range depend on the
chosen polynomial. The construction is supplied, not axiom-selected.

Let J^(0) be the axis-balanced current with alpha=1 and potential S_i g_i.
Since C 1=p0 p, the exact occupied-species current is

    J_a^i=F J_a^(0),i+F' S_i g_i p0 p_a.                   (2)

This follows by differentiating the potential in the six independent
occupied probabilities before restricting any field. It remains valid for
all interior states and includes changes in the vacancy probability.

For r_j=q_j-rho/3, (2) gives

    J_(r_j)^i=F J_(r_j)^(0),i+F' S_i g_i p0 r_j.           (3)

The original quadratic rule has J_r=0 on r=0, so the entire family (1)
preserves that submanifold in the smooth exchange-only PDE. This is a
continuum invariant manifold statement, not a statement that finite
microscopic samples have exactly zero quadrupole.

## 2. Exact four-field currents on the invariant submanifold

Evaluate at q_j=rho/3 after taking all derivatives. Write

    P(rho)=rho^2 F(rho)/3,
    D(rho)=2rho F(rho)+rho^2 F'(rho)=3P'(rho).

Then

    J_rho^i=p0 D(rho) g_i,
    J_(g_j)^i=P(rho) delta_ij
       +p0[2F(rho)+rho F'(rho)]g_i g_j
       -3F(rho) delta_ij g_i^2,
    J_(r_j)^i=0.                                          (4)

The scalar pressure P is isotropic. The last term of the vector current
continues to distinguish the lattice axes at nonlinear order; choosing a
pressure law does not remove it. Linearization at g=0 gives

    delta rho_t+3p0 P'(rho) div delta g=0,
    delta g_t+P'(rho) grad delta rho=0,
    delta r_t=0,
    c_s(rho)^2=3(1-rho) P'(rho)^2.                         (5)

This is an all-density family of isotropic acoustic principal symbols,
with four zero-speed modes retained. A nonzero P' gives a nonzero pair.
The earlier quadratic construction is F=alpha. Changing F changes the
pressure and speed even though every event is still immutable exchange,
every homogeneous product remains stationary, and the same seven labels
and cubic geometry are used.

## 3. Prescribing a speed on a compact interior density interval

Fix 0<rho_-<rho_+<1. Given a continuously differentiable positive target
c_target on that interval, define

    P_target(rho)=C0+integral_(rho_*)^rho
                            c_target(s)/sqrt(3(1-s)) ds,
    F_target(rho)=3P_target(rho)/rho^2.                     (6)

For an exact differentiable potential (not yet a finite-range realization),
equation (5) gives precisely c_target. To get actual finite-range models,
approximate F_target in C^1 by polynomials F_m. One elementary construction
approximates the continuous derivative F_target' uniformly by polynomials
and integrates, choosing the integration constant to match F_target at one
point. Both function and derivative then converge uniformly. Substitution
in (5) makes c_s,m converge uniformly to c_target on the stated compact
interval. For sufficiently accurate approximation the acoustic pair remains
nonzero there. Each polynomial defines its own fixed finite-range process;
one first fixes that process before taking its hydrodynamic or fluctuation
limit. This is not a limit with interaction range growing with N.

For constant target c>0, an antiderivative is

    P_target=C0-(2c/sqrt(3)) sqrt(1-rho).

Equation (6) is only used on the specified interior interval. No bounded-rate
realization uniform to rho=0 or rho=1 is asserted. Nor is a finite polynomial
claimed to realize a square-root function exactly.

## 4. Consequence for the research decision

The acoustic mechanism is flexible: immutability and cubic geometry are
compatible with a broad set of pressure laws. That is useful constructive
progress. It also means matching a desired wave speed by choosing a local
potential is not a derivation of that speed from the framework's axioms.
The total formation clock and conditional formation odds provide additional
physical constraints; so would a quantum implementation, an independently
selected action, or data not used to choose the generator. Those constraints
must be assessed explicitly instead of treating the existence of waves as
a unique theory selection.

This calculation is not a no-go for a TOE, a claim about all invariant
measures, or a classification of all possible nonlinear continuum theories.
It gives an explicit constructive family and keeps its selection freedom
visible. The independently checked six-site cubic potential is a different
route: it improves the vector current's quadratic isotropy but generates
quadrupoles at cubic order. Neither route resolves all nonlinear effects.
