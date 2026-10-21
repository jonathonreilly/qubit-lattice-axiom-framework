# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_KINK_RESONANCE_CHECK.md`, SHA256 `353976446dc7c030381b608a99cd3afb4f9e478ccc94b369b41e3ec8e2e80d3f`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Conditional half-line kink resonance check

This checks the proposed effective half-line model and conventions, not a native-theory resonance theorem. I read the relative-coordinate and third-order probes, their third-order output, and the band construction. No source files were changed or full-H calculation rerun.

## On-shell vertex

Write dimensionless energies in Jperp units, lambda=Jperp/Jz, and H0 with nearest-neighbor hopping +2 on sites 0,1,... . The host correction is lambda[-H0^2/16+P0/4]. Because (H0^2)_00=4, its boundary diagonal cancels; its 0-to-2 matrix element is -lambda/4. Thus the host scattering wave obeys

E phi0=2 phi1-lambda phi2/4+O(lambda^2).

For the side level E=-2lambda+O(lambda^2), the zeroth-order host recurrence gives phi2=-phi0+O(lambda), and consequently phi1=-(9/8)lambda phi0+O(lambda^2). The side-to-host vector through the supplied next order is

w=-sqrt(2)lambda|1>+lambda^2[-sqrt(2)|0>+|2>/sqrt(2)].

Its on-shell amplitude is

<w,phi>=lambda^2[9sqrt(2)/8-sqrt(2)-1/sqrt(2)]phi0+O(lambda^3)
          =-(3sqrt(2)/8)lambda^2 phi0+O(lambda^3).

This uses both the host boundary correction and the third-order side vector. Omitting either can change the coefficient. Higher host terms enter this leading vertex only at higher order if the stated expansion is regular and these are the complete terms through the displayed orders. A side-level self-energy shift of order lambda^2 likewise does not alter the leading coefficient. The retained near-zero-energy structure in fact suppresses the leading real self-energy further, but that stronger statement is not needed here.

## Width convention

For the unperturbed half-line hopping-2 chain, its retarded boundary resolvent is

g00(z)=(z-sqrt(z^2-16))/8,

with the branch chosen for g~1/z and Im g<0 above the band. Hence g00(0+i0)=-i/2 and the boundary spectral density is rho0(0)=1/(2pi). The on-shell effective vertex squared is 9lambda^4/32. Its leading side self-energy has imaginary part -9lambda^4/64. Therefore

Gamma/Jperp = -2 Im(E_pole) = 9lambda^4/32 + higher orders,
Gamma = 9 Jperp^5/(32 Jz^4) + higher orders.

Here Gamma is the full resonance width / probability-decay rate with hbar=1. The imaginary part of the pole, Lorentzian half-width, and amplitude-decay rate are Gamma/2. This is a resonance after analytic continuation across the host continuum, not an exact real bound eigenvalue. The coefficient presupposes an infinite half-line absolutely continuous host near E=0 and absence of additional open channels at the same order.

## Bare source residue

For a probe vector 2|0>, its norm squared is four. The leading source-to-side resolvent numerator is determined by g01(0)=-1/2 (the boundary resolvent equation), giving

<0|g w> = lambda/sqrt(2) + O(lambda^2).

The side self-energy derivative renormalizes its residue only at higher order. Thus the resonance residue in this bare probe's Green function is 4(lambda^2/2)=2lambda^2 to leading order. This is a pole-residue/weak-resonance statement, not a separately normalized exact eigenvector weight in the infinite continuum. At higher order the residue can be complex and interfere with a continuum background.

The original physical observable can have dressed direct side components or altered low-band source vectors at the same order lambda. They can change or cancel this residue. Consequently 2lambda^2 should remain explicitly the bare site0 source result until the original O dressing is derived. The linewidth belongs to the effective Hamiltonian, whereas visibility belongs to the dressed observable and chosen state; those are distinct checks.

## Limits and unproved extensions

The supplied finite L8,10,12 K3 side columns agree with -sqrt(2)|0>+|2>/sqrt(2), side diagonal zero, to numerical precision; L6 has the expected finite-boundary modification at site2. The reported outside norms are about 1e-14. This is useful finite-order evidence, not an all-length identity or a uniform native Schrieffer-Wolff remainder bound.

A finite relative chain has discrete real levels and no intrinsic decay width. Taking the continuum limit before resolving a width O(lambda^4) is essential; a finite grid would need level spacing much smaller than this scale to approximate the lineshape. Neither fixed small-L spectra nor a finite numerical Lorentzian broadening establishes the claimed physical lifetime.

Unknown next-order native terms are smaller than the leading O(lambda^2) on-shell amplitude only if the effective expansion and its continuum limit are controlled; additional resonant channels or a nonuniform expansion could invalidate the coefficient. Symmetry or full source dressing may also change the physical readout. These caveats do not invalidate the conditional effective-model calculation. They prevent promoting it to an exact native bound state, autonomous scalar, bulk pole, observed resonance, or cosmological interaction.

## Follow-up: canonical original-observable dressing

The parent's mixed-band derivation checks algebraically. Let G be the aligned vacuum projector with unperturbed energy0 and P the energy8 two-wall projector; Vg lies entirely in P. The first ground correction is -Vg/8, while the first band isometry has ground component +GVP/8. For diagonal O preserving these energy spaces, the transition source is s1=(Og-O_P)Vg/8, equal to Vg when the one-rung flipped configurations have O_P=Og-8.

At second order the ground correction in P is +H1 Vg/64, H1=PVP. The second-order canonical band isometry into G contributes the folded term -GVP H1/64; its ordinary R_P V R_P V term gives zero against g because R_P Vg=0. The cross first-order O term vanishes because O preserves P, the ground first correction lies in P, and R_P excludes P. Canonical normalization terms confined to G or P also have no direct cross-band diagonal-O matrix element. Combining the two nonzero pieces yields

s2=(O_P-Og) H1 Vg/64.

If H1Vg has only the length-two relative configurations with O_P-Og=-16, this becomes -H1Vg/4. With Vg=2|0> and H1|0>=2|1>, the physical source is consequently 2lambda[|0>-(lambda/2)|1>+...]. This conditional support assumption should be checked directly in physical configurations, as the parent is doing; the canonical algebra by itself does not establish it.

The host1 correction cannot alter the leading resonance residue: g11(0)=0 for the hopping-2 half-line, while the leading side vector is proportional to lambda|1>. Thus <1|g w> has no O(lambda) contribution; its leading nonzero value comes at higher order. With no direct side component in s2, the physical observable retains leading resonance weight 2lambda^4 (the prior bare-source 2lambda^2 multiplied by the external lambda^2 source factor). This remains a conditional effective resonance/readout result, not a certified native continuum linewidth or exact physical state.
