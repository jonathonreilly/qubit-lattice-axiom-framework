# Longitudinal propagation of the native bulk composite resonance

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_com_propagation.py](../scripts/native_com_propagation.py)

The compact neutral feature in the uncut lattice has derived longitudinal
motion as well as an internal oscillation. For the complete fixed-order
compact-sector coefficient operator, its outgoing pole acquires a momentum
dispersion. No new kinetic term or interaction is supplied. Its gap remains
near 8Jz: this is not a light cosmological scalar or a full microscopic pole.

## Native endpoint motion fixes the kinetic coefficient

Use the same supplied XX/YY/ZZ Hamiltonian and weak anisotropy as the
[zero-momentum construction](NATIVE_FIXED_ORDER_COMPOSITE_NOTE_2026-10-18.md).
Fix transverse center-of-mass momentum to zero and take longitudinal total
momentum p near zero. A compact state has two flipped columns sharing an
interval of length ell; its longitudinal center is the midpoint of that
interval.

For the axial-distance-two long arm, the native second-order diagonal is
-4 and each of four endpoint moves has coefficient -1/2 in Jz lambda^2
units. Growing or shrinking opposite ends shifts the center by plus or
minus one half. Their Bloch phases therefore give

    gamma = cos(p/2),
    H_long/Jz = 8 + lambda^2[-4 I - gamma T] + lambda^4 ell/8 + ...,

where T moves the interval length by one. This coefficient is obtained
from the actual virtual paths, not from a chosen effective mass.

## The outgoing mode persists near zero momentum

Let G_AA^hole(E) be the already-derived scalar host Green function on the
square lattice with its five-site cross removed, with
A=(delta_(2,0)+delta_(-2,0)+delta_(0,2)+delta_(0,-2))/2. Native endpoint
shortening gives the boundary self-energy

    Sigma_p(E) = gamma^2 G_AA^hole(E),
    a_p = Sigma_p(-2gamma)/(gamma+Sigma_p(-2gamma)).

The host remains radiative near E=-2gamma. On its energy curve
u+v=gamma, with u=cos(kx), v=cos(ky), the form factor
Ahat=2gamma^2-4uv-2 varies while every scalar hole correction is constant.
The resulting spectral density is strictly positive. Thus Im Sigma_p<0
and the boundary denominator does not vanish.

Rescaling the Airy arm by gamma, and retaining the actual finite-order
bulk coefficients and finite contacts, gives uniformly for p in a
sufficiently small fixed real neighborhood of zero,

    E_p/Jz = 8-(4+2gamma)lambda^2
             +(alpha1/4)gamma^(1/3)lambda^(10/3) + O_m(lambda^4),
    Gamma_p/Jz = (-Im a_p)/4 lambda^4 + o_m(lambda^4).

Here alpha1 is the first positive Airy zero and Gamma_p=-2Im E_p.
The first omitted real mass coefficient depends on the native higher
matrices; it is not supplied by the numerical model below. The proof
uses the [existing Airy control](NATIVE_RANGE_TWO_AIRY_NOTE_2026-10-18.md)
and the complete outgoing construction. The fast-host saddle stays a
distance comparable to 2gamma lambda from the pole in fast units, and
excluded long arms stay separated by order 2gamma Jz lambda^2. These
controls are uniform near zero; they are not asserted near p=pi.

For any fixed small nonzero p, the leading energy increase is
2[1-cos(p/2)]Jz lambda^2. This establishes longitudinal dispersion of the
coefficient resonance. A formal curvature expansion is not used as an
error-controlled derivative theorem here. The fast confined-arm estimates
currently control a narrow outgoing strip and do not give a fixed complex-
momentum neighborhood; differentiating the remainder would require more
control. No ballistic velocity or propagation-distance bound is claimed.

## The original observable couples to the moving mode

Give the existing longitudinal observable a Fourier weight at its bond
midpoint:

    C_p = V^(-1/2) sum_(r,z) exp[ip(z+1)] Z_(r,z) Z_(r,z+2).

For real p, C_-p=C_p†. A single-layer pair flip changes this observable
by -8 exp(ipz) cos(p)/sqrt(V). The actual local normal-form dressing
therefore gives the leading fast source -sqrt(2)lambda cos(p)d. Native
two-edge transitions and the outgoing fast resolvent then give the slow
source lambda^2[cos(p)/gamma]u0+o(lambda^2), where u0=(A+2D)/sqrt(2) and
D is the normalized sum of the four diagonal-neighbor sites.

The final slow-arm coupling contributes another gamma. Differentiating
the controlled Airy pole with respect to its endpoint self-energy gives
P11=f gamma/(gamma+Sigma_p)^2+o(f), f=lambda^2/8. Hence the complete
fixed-order outgoing response has residue

    Res(C_p) = lambda^6 R(p) + o_m(lambda^6),
    R(p) = gamma cos^2(p) [u0^T G^hole(-2gamma) A]^2
           / [8(gamma+Sigma_p)^2].

This is a complex Riesz residue, not a probability or positive isolated
spectral weight. Conversion to physical energy adds no extra Jz factor.
The source proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/BULK_COM_SOURCE_PROOF.md`)
checks the nontrivial cancellation of the two momentum-dependent vertices.

The coupling is analytically nonzero near zero momentum. At p=0 the
free-host identities give u0^T G^hole A=sqrt(2)g_cA/(E g00-1).
On the E=-2 energy curve, Ahat=-4uv is strictly negative on regular
interior arcs, so Im g_cA>0; the denominator is nonzero. This proves
nonvanishing without using a decimal as a premise. Numerically R(0)
is approximately -0.0303621-0.0363851i, recovering the earlier uniform
readout. No independent scalar-source constant was added.

## Actual finite-time response at nonzero momentum

The [microscopic ground-window theorem](NATIVE_MICROSCOPIC_GROUND_WINDOW_NOTE_2026-10-18.md)
also holds for the Fourier observable above. On its even periodic cubes
L proportional to lambda^-4, take allowed real p=2pi k/L and the connected
correlator <C_-p(t)C_p>. For the same smooth compact time window,

    S_T^H(p,omega) = S_T^(complete compact B40,C40)(p,omega)+O(lambda^8),
    T = c lambda^-4/Jz,  omega/Jz in [7,9].

The error is uniform over allowed real momenta: unit-modulus Fourier
phases preserve every norm, local symmetry and correlation-tail bound;
the momentum mesh makes the periodic seam exact. This compares the
original microscopic observable in every actual ground density of the
stated finite-volume family. It keeps the complete background and fine
structure, and transfers neither an outgoing pole nor a positive peak.
The extension proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/FOURIER_GROUND_WINDOW_PROOF.md`)
also distinguishes this smooth window from a causal step-function filter.

## Controls and remaining scope

The root proof (`outputs/neutral_continuation4_review_2026_10_18/proofs/BULK_COM_POLE_PROOF.md`)
and independent geometry and continuation checks separate native endpoint
coefficients from spectral assumptions. Numerical controls use a specified
nearest-neighbor Airy arm and the derived outgoing host at p=0,.3,.6,
with increasing cutoffs. They test the momentum-dependent boundary and
width formulas, not the complete higher-order native mass coefficient.
Their Schur residuals are not certified pole-error bounds.

A fixed perturbative order cannot translate a sufficiently long entire
feature transversely: even a translation sharing one column changes at
least 2ell physical spins. Finite endpoint contacts can nevertheless
produce transverse dispersion. No all-order immobility, isotropy or
Lorentz dispersion follows from this locality observation.

The result retains the supplied Hamiltonian, anisotropic regime and
reference-sector construction. The microscopic finite-time comparison
is a separate result and does not turn this outgoing pole into a full-H
pole. State preparation, physical
units, detector identification and the cosmological bridge remain open.
No observational value is fitted or used as an independent test.

## Current source and execution boundary

The complete live mathematical sources are listed in the primary's literal input closure. Historical reviewer dispositions and saved numerical results are provenance, not current evidence. The primary computes its declared finite controls in a fresh preserved temporary directory, enforces its aggregate wall-clock cap before scientific imports, and streams partial diagnostics. Frozen native coefficient tables are explicitly labeled input checks, not newly enumerated paths. Distinct primary assertion groups are counted; helper assertions are additional uncounted fail-closed checks. No audit status or physical primitive is introduced.
