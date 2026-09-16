# Working derivation: volume-uniform low-energy response

2026-09-16 UTC. Personal exploration, provisional, not independently checked.
This is a live derivation, not a completed theorem or phase claim.

New obligation beyond prior Block24: obtain a ground-state fluctuation bound
uniform in spatial volume, then a positive LOW-ENERGY spectral-weight bound
for the same compact charged Hamiltonian. This uses a charge-neutral discrete
Gaussian trial state and a two-observable spectral uncertainty estimate.
It does not assume a photon, a free vacuum or an infrared RG remainder.

## Candidate route

On a connected periodic cubic box let Lambda=ker(D) intersect Z^E. It includes
harmonic electric loops. For positive diagonal W_E and t>0 use amplitudes
exp[-t n.W_E.n/2] on Lambda. Tensor this with conjugate onsite matter ground
states with equal occupation numbers, hence exact zero onsite charge.
Poisson summation on span(Lambda) gives

    <n.W_E.n> <= rank(Lambda)/(2t).

For each integer plaquette boundary b in Lambda, symmetry and Jensen give

    <U^b> = exp[-t b.W_E.b/2] <exp[-t n.W_E.b]>
           >= exp[-t b.W_E.b/2].

With t=alpha g^2 this bounds the pure gauge trial energy by

    a E_trial <= rank(Lambda)/(4alpha)
                +alpha/2 sum_p b_p (boundary_p.W_E.boundary_p).

The onsite matter energy cancels against its operator lower bound. Hopping
has lower bound -2 sum_links ||T_l||_nuclear for conjugate species. Thus
in the actual ground ensemble, total gauge energy has a bound C V/a
independent of g and V. Translation invariance then implies a plaquette
bound rho_j=<1-cos theta_j> <= C g^2/b_j in each orientation.

Next use F_E=g E(v), F_B=g^-1 sin(theta)(w), and the complete ground-space
trace rho0=P0/Tr(P0). Its elastic commutator trace vanishes even with ground
degeneracy. Spectral Cauchy--Schwarz then gives

    mu_E((0,lambda])+mu_B((0,lambda])
      >= |rho0([F_E,F_B])|-2 sqrt(M1_E M1_B)/lambda.

The two first moments are the exact charged/compact identities in prior
Block24, to be rederived here. For a normalized transverse sine/cosine mode
with s=2 sin(k/2), the commutator magnitude is s(1-rho_j).
A translation-invariant calculation should sharpen the magnetic first moment
by cancelling the deterministic/mean cross term; retain spatial fluctuations.
Expected bound scale is O(k+g+g^2/k), with useful O(k) control for g<<k<<1
and O(g) soft weight after optimizing k. It is not gaplessness at fixed g.

Also construct finitely supported wave packets. A useful explicit envelope is
h_R(n)=sqrt(8/(3R)) sin^2(pi n/R) on n=0,...,R, zero outside. Product envelopes
on three coordinates should give exact curl norm s_R and double-curl ratio,
so no thermodynamic plane-wave interpretation is needed for finite boxes.

## Checks still required

- Exact Poisson sign and metric/rank, including harmonic cycles.
- Charge-neutral onsite trial for the stated Wilson species and a correct
  operator hopping norm (nuclear norm, not matrix operator norm).
- Elastic ground degeneracy removal in the spectral inequality.
- Literal lattice curl convention and the compact cos-field correlations.
- Finite checks must retain hard-flux boundary commutator defects; no cutoff
  identity may be silently treated as an untruncated rotor identity.
- Infinite-volume inelastic response needs extra state/spectral control;
  finite-volume soft weight can collapse into elastic weight. Do not promote
  this bound to a photon pole, a phase theorem or a selected law.
