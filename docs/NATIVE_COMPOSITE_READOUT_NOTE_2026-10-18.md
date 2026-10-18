# Original readout coupling to the native neutral composite

**Status:** bounded-support.
**Primary runner:** [scripts/native_composite_readout.py](../scripts/native_composite_readout.py)

The [complete fixed-order neutral pole](NATIVE_FIXED_ORDER_COMPOSITE_NOTE_2026-10-18.md)
was derived without adding an interaction. This block derives its leading
coupling to the original longitudinal diagnostic, rather than appending a
scalar-source term. It does not identify this diagnostic with physical matter
or a detector, and it does not transfer a pole to the exact microscopic H.

Use the same supplied Hamiltonian, uniformly polarized reference, zero COM
momentum, square-scalar/even-reflection sector and fixed-order local normal
form. Define

    C = sum_r Z_r Z_(r+2ez) / sqrt(Nphysical),

and center its exactly transformed observable before truncating its connected
coefficients to the fixed order. This normalization and reference are stated
premises. C is a scalar under the transverse square group; a full cubic or
Lorentz scalar is not claimed.

## Deriving the source from H

The local transformation has (S1)_(a,v)=V_(a,v)/(8Jz) between the polarized
vacuum and a one-layer two-column excitation. A transverse edge changes the
unnormalized C by -8. Consequently

    [S1,C]_(a,v)=(C_v-C_a)(S1)_(a,v),
    q_F = -sqrt(2) lambda d + O_m(lambda^2).

The signs follow from the existing XX and YY matrix elements. The earlier
[physical-bit normalization check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_BULK_SOURCE.md)
uses225 actual sites and normalized translation orbits, not a replacement
multi-qubit site. Each fixed-order connected source has bounded support in
relative coordinates.

Direct source terms into the slow ell=2 states vanish through second order:
on each of two layers, non-neighboring flipped columns require at least two
transverse edges. Closed ell>=3 arms also cannot be reached through second
order. Thus the weaker bounds q_S,q_closed=O_m(lambda^3) suffice. Eliminating
the gapped closed arms contributes only O_m(lambda^4) to the source.

The leading native slow-to-fast vertices are

    v_A = F0 d/2 = -d2-e,     v_D=-2e.

For the complete fixed-order fast operator F_lambda, let
R=(z-F_lambda)^(-1) on its established outgoing sheet. The physical vertex,
resolvent and first source have factors Jz lambda^2, (Jz lambda)^(-1) and
lambda respectively. Their product gives an induced source of orderlambda^2.
The exact resolvent identity yields

    v_A^T R d = [z Rdd-1-((F_lambda-F0)d)^T R d]/2.

The complete fast-sector estimates give Rdd=O(1) and
Red=1/2+O(1/log(1/lambda))+O_m(lambda log^2(1/lambda)). The correction vector
(F_lambda-F0)d is O_m(lambda) with fixed support. Therefore the full effective
slow source satisfies

    q_S,eff/lambda^2 -> u0=(A+2D)/sqrt(2).

The error is logarithmic in general. Other fixed boundary components are
smaller thanlambda^2. This result uses the actual confined fast arm on the
proved lower-half-plane disk; it is not a pointwise real-energy statement.

## Coupling residue, without a supplied scalar constant

Let G_s be the regular punctured-square-host Green matrix, Sigma0=G_s,AA(-2)
and f=lambda^2/8. Eliminating that host gives endpoint source
-lambda^2 u0^T G_s A+o_m(lambda^2). The Airy pole's endpoint Riesz residue is

    P11 = f/(1+Sigma0)^2 + o_m(f).

One derivation differentiates the analytic pole energy with respect to a
frozen endpoint Sigma; its derivative is the complex Riesz entry. Equivalently,
the Bessel boundary equation has derivative (1+Sigma0)^2/f at the pole.
For every fixed endpoint i, its polevector ratio tends
1+(i-1)(1+Sigma0), so fixed-support source errors are not amplified.

Localized contour estimates bound the range-two correction by O(f^(4/3)).
The fast correction of size delta=O_m(lambda log(1/lambda)) changes the
endpoint residue by O(f delta). Its energy derivative may be as large as
delta/f, but multiplication by the endpoint residue f makes the normalization
correction O(delta). This is why a global projector-norm estimate would not
be sufficient.

The continued original-C response consequently has pole residue

    Res_C = lambda^6 [u0^T G_s(-2) A]^2 / [8(1+Sigma0)^2]
            +o_m(lambda^6)
          =(-0.03036208824-0.03638513790i)lambda^6+o_m(lambda^6).

The square is a transpose square from analytic continuation of a real
symmetric response, not an absolute-value square. This complex residue is
not a positive probability. Converting the resolvent back to physical energy
cancels its Jz lambda^2 prefactor against the pole denominator, so no extra
energy-unit factor belongs in Res_C.

The [source check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FIXED_ORDER_SOURCE.md)
and [endpoint check](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FIXED_ORDER_RESIDUE.md)
record separate derivations. The runner checks finite range-two endpoint
residues and their normalization against the analytic limit; those numerical
models supplement, and do not replace, the fixed-order proof.

## What remains

This retires the need to supply an independent source coupling inside this
specified coefficient construction. It does not derive the Hamiltonian,
reference preparation, units or identification of C with an empirical source.
The mass remains near8Jz. The exact microscopic response, real-axis line shape
and any cosmological identification remain open. In particular, confined
fast-arm fine structure cannot be erased by an unannounced energy average.
No observational value is fitted and no independent observation is tested.
