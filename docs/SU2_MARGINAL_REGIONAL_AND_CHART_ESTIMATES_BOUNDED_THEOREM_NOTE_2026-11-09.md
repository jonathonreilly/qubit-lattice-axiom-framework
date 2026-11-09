# Regional and nonlinear chart estimates for the two-plaquette SU(2) marginal

Status: proposed_retained

This note supplies regional coercivity for the complete normalized energy,
nonlinear chart covariance, and arbitrary-exterior moment and buffered-ratio estimates for the actual
seven-edge two-plaquette marginal. The earlier compact coercivity theorem is
an explicit input. These finite two-step results do not yet establish the
marginal's full connected four-response or a physical mass gap.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "regional and nonlinear chart suppliers for the actual seven-edge marginal"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Match the marginal's compact decomposition and connected-density expansion, then prove its complete connected fourth response."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Analytic estimates for the supplied finite two-step SU(2) marginal with exact surviving factors, explicit chart/collar domains and identity-exterior compact bounds."
audit_required_before_effective_retained: true
bare_retained_allowed: false
full_existence_established: false
physical_continuum_mass_gap_established: false
```

## Exact model and regional factors

Fix odd L>=3, kappa>0, m>=3, fine torus side L^2 m and u>=1. Let J be
the seven independent positive terminal edges in two distinct elementary
plaquettes sharing exactly one edge, and O its complement. Use the actual
paired-root-leg means and terminal-root fine forest, with arbitrary allowed
internal trees, all fine non-tree links and all intermediate links retained.
The [compact marginal theorem](SU2_TWO_PLAQUETTE_MARGINAL_COERCIVITY_BOUNDED_THEOREM_NOTE_2026-11-09.md)
provides a uniform c_J>0 with E_J>=c_J sum_e[1-w(a_e)].

The exact hidden law, at zero source and terminal exterior V_O=I, is

    rho_J(da) proportional to q_u(a0) K0(a1|a0)
                                      product_(c in O) k1,c(I|a1) da.

Each kernel is exp(kappa u <output,M>)/Z(kappa u |M|), with probability
Haar Z(t)=integral exp(t w(Q))dQ. Every surviving normalizer remains; the
entire kernel disappears on J. There is one fine Wilson action and no
intermediate Wilson replacement.

A region R owns every retained hidden link whose tail lies in its terminal
cells. Select each whole surviving factor whose hidden readers meet these
links: include all mean inputs, hidden outputs and normalizer inputs,
including syntactically selected factors constant under conditioning. Write
E_R^J for their centered leading energy and C_R^J for the surviving selected
kernel labels. With exterior quotient coordinates z fixed, the exact regional
density relative to product probability Haar is

    (D_R^J(z))^(-1) exp[-u E_R^J(a,z)]
                    product_(c in C_R^J) H(kappa u |M_c(a,z)|),
    H(t)=exp(t)/Z(t).

All constants below may depend on L,kappa and stated chart/threshold choices,
but not on volume, pair position/orientation, allowed trees or the region.
No useful numerical size of these existence constants is asserted.

## Nonlinear chart estimate

Write a_e=exp(i x_e dot sigma). There are delta>0, C_H and alpha>0
such that the exact negative logarithmic Lebesgue density S, on the fixed
Cartesian cube |x_e,r|<delta, satisfies for every u>=1

    Hess S >= (u c_J/2+1/2) I,
    sup_i sum_j |(Hess S)_ij| <= u C_H.

These bounds also hold for every principal-coordinate subcube with all its
fixed hidden readers in the same small chart. Surviving terminal outputs
may range over |log V_c|_coordinate<=delta for this chart statement only.
For C^1 quotient functions f,g and their actual gradient-reader supports A,B,

    |Cov(f,g)| <= 4/(u c_J) exp[-alpha d_1(A,B)]
                        ||grad f||_L2 ||grad g||_L2.          (1)

The measure and both norms in (1) are those of the actual restricted law.
Constants have zero covariance. Holes and disconnected coordinate regions
are allowed; d_1 is ambient periodic nearest-neighbor cell distance.

The [complete chart proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-nonlinear-chart-estimates.md)
retains sum h(kappa u |M|)-sum log j(x), where h=log Z-id and
j(x)=(sin|x|/|x|)^2. It proves finite-template derivative bounds through every
fixed order, including uniform radial-normalizer derivatives on |M|>=1/2.
Its covariance argument constructs the weighted Neumann Poisson solution by
cosine H^2 approximation and uses the correct mixed vector face domain.
Cube corners and the weighted inverse domain are treated explicitly.
The [complete normalized-energy extension](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-normalized-regional-coercivity.md)
removes the original proof's u_* threshold on a smaller fixed cube: the
normalizer correction has positive semidefinite Hessian at identity, its
variation is O(delta), and the Haar Hessian retains a lower bound of 1/2.

For original sources with orbit variables omega, the exact covariance is
Cov(f,g)+E Cov_omega(F,G), with f=E_omega F and g=E_omega G. Equation (1)
bounds only the first term when f,g have the stated regularity. Global
conjugation invariance alone does not remove the second term.

## Regional coercivity for the complete normalized energy

For t=kappa u and r=|M|, define

    Phi_u(v,M)=kappa(r-<v,M>)+[log H(t)-log H(tr)]/u.

Then exactly k(v|M)=H(t) exp[-u Phi_u(v,M)], including at M=0, and
kappa(r-<v,M>)<=Phi_u(v,M)<=kappa(1-<v,M>). Let Ehat_R,u be the sum
of the selected fine Wilson energies and these complete kernel energies.
The regional law relative to product Haar is exactly proportional to
exp[-u Ehat_R,u], with no leftover radial factor.

There are epsilon_*, C, alpha_0, c_0, C_Q, rho_Q>0 such that, whenever
every exterior hidden reader of R has chord distance at most
epsilon<=epsilon_* from I, there is a jointly continuous stationary
field a*_(R,u)(z), uniformly for all u>=1, with

    |log a*_e| <= C epsilon exp[-alpha_0 d_1(owner(e),R^c)].

For every compact q on the region-owned links, without a chart restriction,

    Ehat_R,u(a* q,z)-Ehat_R,u(a*,z) >= c_0 sum_e[1-w(q_e)]. (2)

Thus a* is the unique global minimum and the unique mode of the density
relative to product Haar. On the product
cap d(q_e,I)<=rho_Q the same difference is at most C_Q sum_e d(q_e,I)^2.
Full R has a*=I and no boundary; empty R is trivial. In particular the exact
Haar-density ratio at a* q versus a* is exp[-u times the difference in (2)].
This is not a statement about the mode of the Lebesgue chart density.

The [leading-energy regional proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-regional-relative-coercivity.md)
first establishes the same relative bounds for E_R^J around its own minimum.
The complete normalized-energy extension checks every uniform input again
for Phi_u. Extending a regional field by I supplies the coercive baseline;
a weighted principal inverse and contraction give the localized stationary
field. No repair detour has to stay inside R. A compact perturbation estimate
and exact tangent-proxy cancellation give (2), including zero means, using
global Lipschitz control there and local third derivatives only near identity.
Terminal exterior remains I in this compact result.

## Arbitrary-exterior moments and complete buffered ratio

Each terminal cell owns M0=3L^8+1+4L^4 retained group links. Put
T_x=sum_(e owned by x)[1-w(a_e)], tau=c_J/2 and N_s(x) for the periodic
l-infinity cell ball. For every region Omega, arbitrary compact quotient
exterior, and radial profile 0<=theta_x<=tau, tilt its exact law by
exp[u sum_x theta_x T_x]. There are C_*<infinity and q in (0,1) with

    E_(Omega,theta) T_x <= C_*/u+C_*(2s+1)^4 q^s,
                                  whenever N_s(x) subset Omega.

Consequently, in the untilted regional law, for A subset Omega and any
N_(s_x)(x) subset Omega,

    log E exp(t u T_A) <= t C_*|A|
                  +t C_* u sum_(x in A)(2s_x+1)^4 q^(s_x),
                                                0<=t<=tau.  (3)

On the full torus the boundary remainder vanishes, and each retained link's
chord moment of every fixed order p>0 is O(u^(-p/2)). These moment bounds
assert no conditional mixing.

For a fixed chord threshold 0<delta_r<=2 and deterministic nonempty core S,
let B_S mean that every cell of S owns a link with chord at least delta_r.
Choose h so C_*(2h+1)^4 q^h<=delta_r^2/4 and set R=N_h(S). For all compact
quotient exteriors to R and sufficiently large u,

    p_S=P_R(B_S|z) <= eta(u)^|S|,
    eta(u)=exp[-tau u delta_r^2/8].

Define Z_R with the full compact regional integral, Z_bad with B_S, and
Z_good with its complement B_S^c. The latter is not an all-good chart.
For eta<=1/2, exactly L_S=log(Z_R/Z_good)=-log(1-p_S), and
0<=L_S<=2 eta^|S|. For bounded real original sources F,G independent of
terminal outputs, include their joint orbit integral exp(sF+tG). For two
distinct terminal links c,d with tangents v_c,v_d at identity,

    |D_c D_d partial_s partial_t L_S|_(0,I)
       <= 5404 kappa^2 u^2 |v_c||v_d| ||F||_infinity ||G||_infinity
                                                       eta(u)^|S|. (4)

A deleted or regionally unselected terminal kernel has zero score in this
ratio. Every surviving normalizer and every source-only orbit term remains.
In particular the conditional orbit covariance is retained, not replaced by
separate projections of F and G.

The [moment and ratio proof](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-regional-moments-and-ratios.md)
derives an explicit collar cost, cancels H(kappa u)^k and the Haar powers for
the actual surviving count k, and iterates conditionals of the same radial
profile. It then writes every cumulant and mixed chain-rule partition before
bounding (4). These are derivatives at terminal identity; no arbitrary
nonidentity compact rarity estimate is presumed.

## Evidence and next obligation

The four linked proofs are self-contained new-law adaptations of the named
repo methods, with inherited model/coercivity inputs and exact source hashes.
Luna's [repo and primary-literature record](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/marginal-regional-chart-prior-art-20261109.md)
distinguishes matching methods from unmatched hypotheses. The requested
[Fable approach consultation](../.claude/science/physics-loops/su2-gauge-aligned-response-20261108/sources/fable-marginal-regional-approach-20261109.md)
suggested the complete-kernel energy. Fresh mathematical checks and their
source coverage are recorded in the pack's review history; formal audit
remains separate from these research checks.

The next task is to match the exact marginal compact decomposition, regional
source factors and connected-density expansion. Equations (1)-(4) do not
compose overlapping buffered ratios or differentiate an exterior law for
free. The marginal's full connected fourth response, required compact
nonidentity backgrounds, further exact blocking, continuum reconstruction
and physical spectral gap remain open.
