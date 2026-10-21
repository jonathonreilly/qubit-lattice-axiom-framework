# Native neutral energy fluctuations and a derived scalar overlap

**Status:** exact-support for the stated Hamiltonian and statistical ensemble.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_conserved_scalar.py](../scripts/native_conserved_scalar.py)

The existing one-qubit compass Hamiltonian has a neutral collective
fluctuation channel that needs no appended interaction: its conserved energy
density. A specified scalar diagnostic derived from the same Hamiltonian has
an exactly calculable overlap with that channel. This is a different route
from the massive finite-interval composites, and its limitations are sharp:
the calculation supplies an infinite-temperature state, and its ordinary
retarded response is zero. It does not produce a vacuum scalar particle or
a cosmological force.

Conserved-observable projection bounds are established prior art, including
[Mazur's 1969 paper](https://doi.org/10.1016/0031-8914(69)90185-2).
Here the model-specific moments and overlaps are calculated directly.
No novelty claim is made for conservation laws or spectral projection.

## Exact neutral collective fluctuation

Take periodic lengths at least five, lattice spacing and hbar set to one,
V sites, and the supplied Hamiltonian

    H = -sum_(r,a) J_a sigma_r^a sigma_(r+e_a)^a.
    E_q = V^(-1/2) sum_b exp(-i q.r_b) h_b,

where r_b is the bond center and q is an allowed reciprocal momentum.
Use normalized Hilbert-Schmidt trace, corresponding to rho=I/2^V.
Every bond term commutes with the exact plane symmetries. At equal positive J_a=J,
E_q transforms as a cubic scalar density, with q transformed geometrically.

Pauli orthogonality and the unique right-angle three-spin commutators give

    m0 = <E_q^dagger E_q> = sum_a J_a^2,
    m2 = <[H,E_q]^dagger[H,E_q]>
       = 32 sum_(a<b) J_a^2 J_b^2
           [1-cos(q_a/2)cos(q_b/2)].

At isotropy, m2/m0=(8/3)J^2 |q|^2+O(|q|^4). The positive Liouvillian
spectral measure therefore obeys

    weight(|omega|>Omega)/m0 <= m2/(m0 Omega^2).

For Omega=J|q|^alpha, 0<alpha<1, essentially all fluctuation weight lies in
a shrinking frequency window as q tends to zero along larger tori. This
statement does not require an assumed limiting spectral density. It does
not distinguish elastic weight, diffusion, propagating waves or a continuum.

## Derived scalar diagnostic coupling

Use the [already derived](NATIVE_CUBIC_SCALAR_RESPONSE_NOTE_2026-10-18.md)
operator Q=sum_a[H_a,[H,H_a]]. It is a diagnostic made from the existing
Hamiltonian, not an extra term added to H. At isotropy its Pauli expansion is

    Q = -32 J^2 H + Q_four_spin,
    <Q^2>/V = 5376 J^6,
    <Q H>/<H^2> = -32 J^2.

The four-spin remainder is Hilbert-Schmidt orthogonal to H. Consequently at
least 3072 J^6 per site, or **4/7 of Q's fluctuation weight**, lies in the
conserved energy component at zero momentum. Other conserved components
could add weight; equality with the complete elastic weight is not claimed.

For a local finite-q extension, set Q_q=sum_a[H_a,[H,H_(a,q)]], using the
same bond-center phases on the inner H_a: H_(a,q)=V^(-1/2) sum_(b parallel a) exp(-i q.r_b) h_b. Thus Q_0=Q/sqrt(V). Its exact energy projection is

    g(q) = <E_q,Q_q>/m0
         = -32 sum_(a<b) J_a^2 J_b^2 cos(q_a/2)cos(q_b/2)/sum_a J_a^2.

The isotropic norm N(q)=<Q_q^dagger Q_q> is the finite polynomial

    N(q)/J^6 = 1536 + 512 sum_a cos(q_a)
      + 256 sum_(a<b) cos(q_a)cos(q_b)
      + 256 sum_(a<b) cos(q_a/2)cos(q_b/2)
      + 256 sum_cyclic cos(q_a)cos(q_b/2)cos(q_c/2).

This comes from exact local Pauli contractions, not a fit. For the spectral
projection P onto |omega|<=Omega, Cauchy-Schwarz gives

    ||P Q_q||^2/N(q) >=
      [ max(0, |g(q)| sqrt(m0/N(q))
                  - sqrt(m2/(m0 Omega^2))) ]^2.

This handles possible cancellation by the orthogonal remainder at finite q.
The limiting fraction is at least 4/7 for the shrinking windows above. Even
for Omega=A J|q|, the limiting lower bound is

    [max(0,sqrt(4/7)-sqrt(8/3)/A)]^2.

It is positive for A>sqrt(14/3). This is low-frequency fluctuation weight,
not an isolated dispersion relation or a derived speed of light.

## Original readout and the state obstacle

The original C_z=sum_r Z_r Z_(r+2e_z) has zero energy overlap at beta=0.
For the explicitly chosen Gibbs state, exact finite-volume Taylor counts give

    <C_z>/V = beta^2 J_z^2+O(beta^3),
    Cov(C_z,H)/V = -2 beta J_z^2+O(beta^2),
    g_C(beta) = -2 beta J_z^2/(sum_a J_a^2)+O(beta^2).

Thus a coupling coefficient can be derived once the state is specified;
the temperature and physical environment have not been derived. Uniform
thermodynamic remainder bounds require additional high-temperature control.
C_z is directional, whereas the sum over three axes is a different operator.

At beta=0, trace[A(t),B]=0 for every pair of operators. Therefore the ordinary
retarded response vanishes despite the nonzero fluctuation spectrum. In an
energy eigenstate, the total-energy variance vanishes, so the argument also
cannot be transplanted unchanged to a vacuum. No inverse-square static
response, physical source/detector identification or cosmological scalar is
established. These failures constrain this route without ruling out all
native scalar candidates.

## Evidence

The derivation (`outputs/neutral_continuation4_review_2026_10_18/proofs/NATIVE_ENERGY_FLUCTUATION_PROOF.md`)
and independent moment (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_ENERGY_MOMENTS.md`)
and source (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_ENERGY_SOURCE.md`)
checks retain all state premises. The independent Fourier norm check (`outputs/neutral_continuation4_review_2026_10_18/proofs/INDEPENDENT_ENERGY_QNORM.md`) verifies all 55 exact displacement coefficients. The runner enumerates exact Pauli operators
on 125- and 216-site tori without diagonalizing their Hilbert spaces, checks
anisotropic and finite-q identities, and constructs the exact norm polynomial.
A separate six-qubit open-grid Gibbs calculation checks the original-readout
Taylor coefficients. All of these are exposed model-development controls;
none is an independent observational test.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.
