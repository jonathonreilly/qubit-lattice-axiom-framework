---
claim_id: square_microscopic_spectral_certificate_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Conditional exact finite-spin Schur reduction, formal first joint-scaling coefficient and rational finite-case low-spectrum error enclosures; no uniform asymptotic or empirical validation."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/square_microscopic_spectral_certificate_2026_09_27.py
---

**Type:** bounded_theorem
**Status:** conditional-support; supplied model, unaudited.

# A microscopic square correction with finite-case spectral error certificates

For the supplied closed square law in the two-positive-record Gauss sector,
the finite-spin spectrum admits the exact Schur reduction below. Its formal
first joint-scaling correction changes both electric energy and adjacent
field hopping. Exact rational spectral counts enclose the error of the full
first-order approximate operator for six declared parameter cases.

This controls part of a mathematical comparison. It does not identify the
microscopic spin with a device parameter or improve an experimental fit.
A rotor-only higher harmonic omits the earlier-order joint electric/hopping
correction. Numerical convergence alone is replaced here by explicit
finite-case interval bounds, without claiming a uniform asymptotic theorem.

## Premises and exact target

The target is the identity between the microscopic eigenvalue count below E
and the rational tridiagonal inertia count defined below, under its explicit
positive-eliminated-block conditions, plus the stated six interval bounds.

Use the [supplied compensated law](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
and [local-pair square limit](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Their microscopic Hamiltonian and Gauss constraint are assumptions; this
note does not re-prove the inherited common-law limit. Fix integer spin S>=1,
K,delta>0, C=S(S+1), x=epsilon²=delta/(K C), two positive records, and the
separately supplied closed specialization kappa=0. Noninteger offset charge,
a resonator and physical preparation/readout are absent. No thermodynamic
limit or post-formation sector is included.

Orient edges (0,1),(0,3),(2,1),(2,3), with A={0,2}. For a two-occupied-site
word q, all physical fields have the form

    E=(n,q0-1-n,-q1-n,q2-1+q1+n),

with integer n and all four entries in [-S,S]. A legal outward hop lowers
its edge field by one and has amplitude sqrt(1-E_e(E_e-1)/C). Let W count
vacant A sites and P project onto W=0. The square compensation equals4P:
in P every one-hop matter output identifies its edge, so F_a*F_a is diagonal
and the compensation leaves the four unweighted path counts. At W=1 its
other-A occupancy gate vanishes; at W=2 no occupied A can hop. This remains
true at spin boundaries because the supplied diagonal compensation is retained.

## Exact reduction and global spectral indexing

In W=0,1,2 blocks the dimensionless bracket Hamiltonian is

    [4x I, sqrt(x) A*, 0;
     sqrt(x) A, I, sqrt(x) B*;
     0, sqrt(x) B, 2I].

A,B contain the negative microscopic hop sign. Put Z=BA and

    d_m=1-m(m+1)/C,
    Z|n>=2[d_(n-1)|n-1>+d_n|n>],
    A*A=4I-4n²/C,  BB*=4 diag(d_m).

Here P has n=-S,...,S and W=2 has m=-S,...,S-1. The Z formula counts the
two orders of each allowed matching. Each fully-B state has four reverse-hop
weights squared d_m, while no W=1 state reaches two different fully-B
states; this proves the diagonal BB* formula. Exterior d_(-S-1),d_S vanish.

For physical trial energy E put lambda=x²E/delta. Eliminating W=2 and W=1,
then using the resolvent identity with BB*, gives

    E(1+4x-lambda) psi = [4Kn²-delta Z*R(E)^(-1)Z]psi,
    R_m(E)=(1-lambda)(2-lambda)-4x d_m.              (1)

Indeed the initial Schur equation is
lambda=4xI-x A*[(1-lambda)I-xB*B/(2-lambda)]^(-1)A;
multiplying it by1-lambda and substituting A*A proves (1). The scalar in
(1) is not assumed to be an independently normalized Hilbert-space metric.

Require lambda<1 and (1-lambda)(2-lambda)>4x. Since0<=d_m<=1, the entire
eliminated Q block is positive. Its Schur complement, multiplied by the
positive number delta(1-lambda)/x², is

    F(E)=4Kn²-delta Z*R(E)^(-1)Z-E(1+4x-lambda)I.

Block congruence preserves inertia. Consequently the negative index of F(E)
is the number of microscopic eigenvalues strictly below E in this fixed
matter/charge sector. This is global indexing in that sector, not a bare-state
overlap label or a claim about every matter sector. F has rational coefficients
for rational K,delta,E; its diagonal and adjacent entries are

    4Kn²-4delta[d_(n-1)²/R_(n-1)+d_n²/R_n]-E(1+4x-lambda),
    -4delta d_n²/R_n.

Accepted endpoints use exact Fraction LDL pivots. A zero pivot or failed
positivity check rejects the endpoint. Counts j,j+1 at endpoints a,b certify
the indexed jth eigenvalue strictly inside(a,b). Floating computations only
propose brackets; their accuracy is not needed once exact counts accept them.

## First correction: formal coefficient with hypotheses retained

For fixed finite field support let N=Z*Z=N0+xN1+O(x²). Its exact entries give
N0 diagonal8, adjacent4; N1 diagonal-16(K/delta)n² and adjacent-8(K/delta)n(n+1).
At rotor order BB*=4I and A*(B*B)²A=4N0. With lambda=O(x²), expansion of
the Schur equation through x³ gives

    lambda=4xI-xM-x²N/2-x lambda M-x³(4N0)/4+O(x⁴),
    M=A*A.

Moving the leading scalar metric1+4x to the left gives

    H0(n,n)=4Kn²-4delta,       H0(n+1,n)=-2delta,
    H1(n,n)=8delta-8Kn²,       H1(n+1,n)=4delta+4K n(n+1).   (2)

Thus H0+xH1 is the candidate first-order operator. Equation (2) is a formal
fixed-support/low-energy coefficient calculation, not a uniform O(x²) spectral
bound as S grows. Taylor expansion at fixed n alone cannot control n of orderS.
The subsequent interval comparisons supply actual bounds only at named cases.

## Infinite-domain enclosures

For H0 on ell²(Z), diagonal confinement gives compact resolvent; the hopping
is bounded. Split at |n|<=L with L>=1. Each omitted tail has form lower bound

    t_L=4K(L+1)²-8delta.

At E<t_L its resolvent is positive and at most1/(t_L-E). The tails are
disjoint and couple to distinct boundary sites with amplitude-2delta, so

    0<=Sigma(E)<=beta(E) Pi_boundary,
    beta(E)=4delta²/(t_L-E).

The exact retained Schur matrix lies between the retained H0-E and that
matrix minus beta Pi_boundary. Positive-tail block factorization preserves
the finite negative index. If the two finite rational comparison counts
agree, that is the exact infinite-rotor count. Unequal counts are inconclusive
and fail the certificate. Nonzero comparison pivots and equal counts also
exclude an eigenvalue exactly at an accepted endpoint.

For H0+xH1 define the self-adjoint realization by its closed quadratic form
on D(n), with0<=x<1/4. Write its adjacent coefficient as

    t_n=-2delta(1-2x)+4Kx n(n+1).

Using |n(n+1)|+|n(n-1)|=2n² for integer n and the elementary off-diagonal
form estimate yields

    4K(1-4x)||n psi||²-8delta||psi||²
        <= q[psi] <= 4K||n psi||².

The shifted form norm is equivalent to the D(n) norm, making the form closed;
finite support is a core by truncation. The embedding D(n) into ell² is compact,
since sum_(|n|>L)|psi_n|² <= L^-2 ||n psi||². This proves compact resolvent for the
specified form realization; no bounded-hopping assumption is applied here.
Its tails obey the lower bound4K(1-4x)(L+1)²-8delta. The two boundary
couplings are equal, t_(-L-1)=t_L, so the same sandwich uses
beta=t_L²/[4K(1-4x)(L+1)²-8delta-E]. The coercivity constant degenerates
as x approaches1/4; that endpoint is excluded.

## Six finite-case error certificates

Use exact K=1, delta=1 or15803623/500000, and S=20,50,120. The latter ratio
31.607246 is a diagnostic parameter value; it is not an independently derived
device constant. Every required x is below1/4. Exact counts enclose the first
seven energies of the microscopic finite model, H0 and H0+xH1 with width2e-9
in K units; corresponding excitation-gap intervals have width4e-9. L20
suffices for H0 and L30 for H0+xH1. All positivity and count conditions are
checked separately for every rational endpoint.

Subtracting the intervals yields these upper bounds on the maximum absolute
microscopic-minus-approximate error over the first six excitation gaps:

| delta, K=1 | S20 | S50 | S120 |
|---|---:|---:|---:|
| 1 | 0.004987235265 | 0.000136754425 | 0.000004229203 |
| 15803623/500000 | 6.647658236470 | 0.281239142371 | 0.009192992163 |

Decimals are rounded upward from exact rational bounds emitted by the runner.
These compare the full spectrum of H0+xH1, not just first-order expectation
shifts. They are fixed-case errors, not signed residuals, universal constants,
experimental uncertainties or a theorem for every S. Exact rational arithmetic
is a checked computation, not a proof-assistant or hardware-verification claim.

## Scientific meaning, review and reproduction

This calculation prevents using an isolated rotor harmonic while omitting
larger-order field-dependent terms. It supplies finite-case error control for
the explicitly given microscopic model. The strongest remaining physical
obligation is an independently justified relation between its spin/resource,
couplings, preparation and detector and a measured system. That obligation is
not discharged by (1), (2), a calibrated spectrum or the certificates. Noninteger
offset, cavity, actual formation dynamics and their errors remain outside this
claim. No broad no-go, physical parameter prediction or TOE confirmation follows.

Selective independent checks reconstructed Gauss states and compensation,
verified (2) and the exact Schur identity, and used rational determinant-sign
recurrences instead of the author's LDL pivots. They independently checked
finiteS20 at the larger ratio, both rotor cases and all six corrected-operator
cases, plus every interval subtraction and upward rounding. All author cases
were also freshly rerun. These scopes are distinct: rerunning the same code is
not independent construction. Deliberately shifted brackets and altered hopping
coefficients failed against the frozen accepted intervals. Final publication
review and delivery gates are recorded in the branch handoff; formal audit is
still required before any authority promotion.

Run `python3 scripts/square_microscopic_spectral_certificate_2026_09_27.py`.
The primary imports all four load-bearing helpers; no helper registry policy
change is needed. The declared input list binds the note, helpers and both
parent sources. No external measurements or network are read by this runner.
Its fresh output contains all rational endpoints, exact counts and derived
error intervals. Finite numerical proposals may fail to locate a bracket;
the exact checks then fail rather than silently treating the guess as evidence.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Exact conditional Schur and spectral-count identities with six rational finite-case approximation certificates; first asymptotic coefficient remains formally scoped.
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: Control microscopic spectral corrections before comparison with additional measured physics.
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: Independently identify microscopic scale and detector coupling, with controlled offset/cavity/preparation errors, before new empirical claims.
```

## Supporting derivations

These current supplied-model proofs belong to this note; they confer no separate status.

- `.claude/science/physics-loops/measured-corrections-20260927/CORRECTED_OPERATOR_BOUNDS_DRAFT.md`
- `.claude/science/physics-loops/measured-corrections-20260927/EXACT_SCHUR_AND_CALIBRATION_DRAFT.md`
- `.claude/science/physics-loops/measured-corrections-20260927/JOINT_CORRECTION_DRAFT.md`
- `.claude/science/physics-loops/measured-corrections-20260927/SPECTRAL_CERTIFICATES_DRAFT.md`
