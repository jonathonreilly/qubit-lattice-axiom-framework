# Heat-kernel D4: finite determinant identities and an open readout

**Date:** 2026-05-10; scope correction 2026-10-21
**Type:** bounded_theorem
**Status:** supplied finite-spectrum identities only; physical compression and thermodynamic bridge open.
**Primary runner:** [companion](../scripts/frontier_hierarchy_heat_kernel_d4_compression.py)

Supply u>0, L=2 or4 and the [parent spectrum](HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02.md):

```
q_n=u²(3+sin²((2n+1)pi/L)), n=0,...,L-1,
spec(D†D) contains each q_n eight times,
|det D|=product_n q_n^4, det(D†D)=|det D|².
```

This is a finite mean-field APBC model with8L modes. The mean-field
factorization, block size, dispersion and multiplicities are supplied;
no physical staggered realization or u is derived here. Positivity requires
u>0. For the finite spectrum, `zeta(s)=sum_j q_j^(-s)` is entire and
`-zeta'(0)=sum_j log q_j=log det(D†D)`. No infinite-spectrum
regularization or thermodynamic limit is needed.

At L2 all q=4u²; at L4 all q=(7/2)u². Consequently

```
|det D4| / |det D2|² = (7/8)^16,
det(D4†D4) / det(D2†D2)² = (7/8)^32.
```

The original note confused these two ratios and described16L as the mode
count despite its own8L spectrum. Distinguish the following readouts:

- Ordinary mass geometric mean `m_L=[det(D†D)]^(1/(2·8L))`
  has mass dimension1 and `m4/m2=(7/8)^(1/2)`.
- Stipulated hierarchy readout `r_L=|det D|^(1/(16L))`
  has `r4/r2=(7/8)^(1/4)`. Its mass dimension is1/2 under the
  supplied spectrum. Another dimensionful identification is needed to call
  it a mass; its dimensionless ratio alone does not supply that identification.

The latter ratio is valid conditional algebra, not a selected EWSB scale.
The arithmetic `4/2^4=1/4` neither selects the readout nor fixes a mode count.
The [bilinear-selector note](HIERARCHY_BOSONIC_BILINEAR_SELECTOR_NOTE.md)
is context for this stipulated readout, not an independently verified bridge.

The former Eq14 asserted a thermodynamic equivalence that is withdrawn.
D†D eigenvalues have mass dimension2, not Fermi-energy dimension1.
Using `rho(lambda)/V4 proportional lambda` in the literal expression
`-T integral rho(lambda)/V4 log(1+exp(-lambda/T)) d lambda`
would give T³ after lambda=Tx, not T⁴, and its extra T conflicts with the
previous `f=-log Z/V4` convention. A physical Hamiltonian energy spectrum,
spatial volume, temperature, measure and determinant-to-partition-function
identification must be supplied before a thermodynamic formula follows.
The Stefan-Boltzmann T⁴ law is contextual mathematics, not an equivalent
proof for this finite block.

A finite counting function saturates at8L, so it cannot obey an
unbounded-lambda Weyl asymptotic law. Positivity and counting modes are not
Weyl validation. No continuum heat-kernel correction to the finite ratio is
computed here. The companion differentiates the finite zeta function,
compares it with the product determinant, checks both ratios and includes
negative controls against confusing the determinant or readout powers.

Original note and runner are recoverable at
`f24d17d97d372df977476e4a69674577f31af575` at the same paths, including
old duplicate-computation PASS accounting and the withdrawn thermodynamic
argument. Existing historical logs are preserved. No physical hierarchy,
Higgs mass, endpoint selection or upstream authority is certified by these
finite calculations.
