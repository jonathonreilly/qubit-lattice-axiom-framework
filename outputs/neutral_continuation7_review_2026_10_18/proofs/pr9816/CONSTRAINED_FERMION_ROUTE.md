<!-- Original PR9816 source SHA256 ffb5c584fb4a55d6aa35cd4993f718be07cce34d7ff618468f7b9009247a059b. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Constrained fermion representation and native feature test

Status: bounded-support. Trace: negative_route_pruning. Proposal allowed: false.
All numerical inputs are exposed model development, not observations. The
one-qubit cubic compass Hamiltonian, its geometry and coupling ratios remain
premises. This block does not establish physical fermions or a TOE.

## Exact rewriting of the existing Hamiltonian

Use four auxiliary Majoranas per physical site, with global Clifford
anticommutation, and impose D_i=b_i^x b_i^y b_i^z c_i=+1. Define
sigma_i^a=i b_i^a c_i. The auxiliary dimension four becomes the physical
qubit dimension two after projection. This is the standard constrained
representation of [Kitaev](https://arxiv.org/abs/cond-mat/0506438), not a new
physical degree of freedom or a new representation claimed as original.

For an oriented axis-a edge define u_ij=i b_i^a b_j^a. Direct multiplication gives

    -J_a sigma_i^a sigma_j^a = i J_a u_ij c_i c_j.

**Deferred terminal interpretation — not an active promoted theorem; packet pending.** The complete original continuation is preserved below. The coefficient identities, commutators, compression inequality and specified finite residual calculations remain active with their exact hypotheses.

> The native cubic graph has two axis-a edges at each site. Their u operators
> share one Majorana and ANTICOMMUTE. Incident edges of different axes commute.
> Thus the honeycomb model's simultaneous static-link solution does not apply.
> Every u commutes with all c_k c_l, so, with oriented neighboring edges e=(k,l),

    dot u = i[H,u] = 2 sum_(e sharing exactly one b with u) J_e u u_e c_k c_l.

Different Clifford monomials do not cancel. These are auxiliary dynamics;
P_phys u P_phys=P_phys c P_phys=0. They are not a measured gauge field.
The Hamiltonian commutes with every D_i and preserves physical projection.

For a simple xy loop of N distinct edges, traversed in order, let T be its
turn vertices. Exact multiplication yields

    product_traversal u = (-1)^(N/2 + 1_[basepoint is a turn])
                         product_(i in T) D_i sigma_i^z.

After projection this is the existing corner-Z operator, up to the displayed
phase. Changing the basepoint can change the sign: these link products are
not ordinary commuting Wilson-flux labels. For a straight n-edge path,

    i c_0 (product_path u) c_n = i^(n+1) sigma_0^a sigma_n^a.

The phase is essential; the raw ordered expression need not be Hermitian.
These identities expose the native constraint, not physical exchange statistics
or a no-go for every fermionic description. Exact Clifford controls and an
independent derivation check the signs, projection and noncommutativity.

## Capacity of a large feature

Suppose a feature is to furnish six Hermitian matrices Gamma_a satisfying
{Gamma_a,Gamma_b}=2 delta_ab I. The three commuting involutions
B_j=i Gamma_(2j-1) Gamma_(2j) have eight joint sign spaces. Multiplication
by Gamma_(2j-1) bijectively flips the jth sign alone, so all eight spaces
have equal dimension. The nonzero representation dimension is a multiple
of eight. A feature therefore needs at least three qubits in TOTAL for this
algebra; this does not require more than one qubit at any site.

There is a further physical-port constraint. Let six commuting Hermitian
involutions A_a (e.g. Pauli operators on six distinct boundary sites) compress
through an isometry V to V^dagger A_a V=alpha_a Gamma_a. Their joint spectral
projectors Pi_s yield a POVM E_s=V^dagger Pi_s V. Put
F_s=sum_a alpha_a s_a Gamma_a and A=sqrt(sum_a alpha_a^2). Then F_s<=A I,
and, for encoded dimension d,

    d sum_a alpha_a^2 = sum_s Tr(E_s F_s) <= d A.

**Deferred terminal interpretation — not an active promoted theorem; packet pending.** The complete original continuation is preserved below. The coefficient identities, commutators, compression inequality and specified finite residual calculations remain active with their exact hypotheses.

> Consequently sum alpha_a^2<=1. Equal ports satisfy |alpha|<=1/sqrt(6).
> This assumes commuting physical ports; it is not a bound on arbitrary
> noncommuting operators at shared sites. Exact unit-strength Clifford ports
> cannot be obtained this way. A unitary basis change also preserves commutators.

The bound is sharp when the dilation may be chosen: at equal saturation,
E_s=(I+sum s_a Gamma_a/sqrt(6))/64 is positive of rank four, with nonzero
eigenvalue 1/32. Factor each E_s and stack the factors into an isometry from
8 dimensions into 64*4=256 dimensions: eight physical qubits. The six sign
registers are commuting ports. Each port has exact leakage

    V^dagger A_a (I-VV^dagger) A_a V = (1-alpha_a^2) I = 5I/6.

This port leakage is not a lower bound on total Hamiltonian leakage, because
Hamiltonian terms can combine. A native low-energy code still has to be derived.

## Explicit candidate challenged against the unchanged native Hamiltonian

`neutral_feature_clifford_control.py` builds that eight-site dilation in an
open 2x2x2 cube. Lexicographic xyz site labels are 0..7. The six distinct
face ports are sites (0,7,4,3,2,5), with Pauli axes (X,X,Y,Y,Z,Z);
sites (1,6) supply the remaining physical dimensions. The explicit logical
Gamma matrices are XII,YII,ZXI,ZYI,ZZX,ZZY. Local basis rotations put each
sign-register Z into the specified physical axis. There is still exactly
one qubit at each cube site.

The code isometry and compressed ports pass below 3e-14. Then the SAME
native open-cube H=-sum ZZ-lambda sum(XX+YY), J=1, is applied to this code.
The measured quantities are h=V^dagger H V, leakage ||HV-Vh||, and the
mean energy compared with the actual eight lowest eigenvalues.

| lambda | leakage norm | code mean energy | lowest-eight mean energy |
|---|---:|---:|---:|
| 0.1 | 2.1684 | -0.3333 | -4.0250 |
| 0.5 | 2.5009 | -0.3333 | -4.6070 |
| 1 | 3.3817 | -0.3333 | -6.1963 |

**Deferred terminal interpretation — not an active promoted theorem; packet pending.** The complete original continuation is preserved below. The coefficient identities, commutators, compression inequality and specified finite residual calculations remain active with their exact hypotheses.

> These rounded entries identify the deterministic reference code. Projected
> coordinate vectors, orthonormalized in fixed order with two-pass Gram-Schmidt,
> fix each rank-four POVM factor. An earlier eigensolver-basis implementation
> also failed, but its numerical values depended on degenerate-basis choices;
> the canonical control removes that ambiguity. A different physical embedding
> is still a different candidate, not excluded by this calculation.
> This explicit candidate fails native invariance and low-energy selection.
> No penalty Hamiltonian or new interaction is added to force it to work.
> Failure of this candidate is not failure of all encodings or larger features.
> The isotropic cube's eighth/ninth levels are degenerate, so an arbitrarily
> chosen lowest-eight subspace there is not a separated native band.

## Scope and next derivation

**Deferred terminal interpretation — not an active promoted theorem; packet pending.** The complete original continuation is preserved below. The coefficient identities, commutators, compression inequality and specified finite residual calculations remain active with their exact hypotheses.

> The auxiliary rewrite and Clifford capacity calculation are exact conditional
> mathematics. The finite candidate failure is bounded support. They prune the
> static-link shortcut and this chosen encoding. They neither supply a scalar
> coupling nor undo the neutral composite poles already derived in this campaign.
> The next route must obtain a protected internal subspace and its boundary
> operators from native spectral dynamics. Anticommuting auxiliaries, a chosen
> projector, or a kinematic Clifford representation alone cannot establish
> fermionic statistics of spatially separated physical features.