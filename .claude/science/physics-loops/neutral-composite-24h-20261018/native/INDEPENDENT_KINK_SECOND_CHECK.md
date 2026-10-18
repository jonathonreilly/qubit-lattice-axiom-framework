# Independent periodic two-domain-wall band and second-order readout check

Disposition: PASS for the stated finite periodic band construction and the tested L6/L8 relative-space identities. No physical scalar, width, thermodynamic or all-orders inference. No pack edits or formal audit; root retains authorship.

## Complete band and projection

Each rung is restricted to its eight even physical-parity configurations. Distinct such configurations have Hamming distance2 or4, so any nontrivial longitudinal boundary costs at least4Jz. A periodic nonconstant configuration has at least two boundaries. Total excitation8Jz therefore requires exactly two boundaries, each between the SAME pair a,b of Hamming distance2. The configuration is precisely one nonempty proper contiguous b interval in an a background. There are24 unordered distance2 pairs, L interval origins and L-1 lengths, giving24L(L-1) distinct states for the ordinary periodic L>=3 graph. The code's lookup uniqueness and enumeration are correct. An independent exhaustive enumeration of all8^6 computational states gives exactly the same720 energy8 states at L6. L8 has1344 states by the complete argument and code.

The periodic boundary convention matters: this is not the prior open aligned-band denominator formula. L2 would double-count the same longitudinal edge in the implemented ring sum and also has different ground tunneling order, so these identities should not be silently reused there.

The core builds PVP from actual rung h entries and records every one-step Q destination. Q in the code is the rectangular matrix P V Q, not a Hilbert projector; repeated paths to a Q state are correctly summed by sparse assembly. Its energy is the full diagonal longitudinal excitation relative to the aligned ground. No omitted energy8 destination remains. Thus Q diag[1/(8-E_Q)] Q.T is exactly the canonical degenerate-band second-order coefficient P V Q(8-H0)^(-1)Q V P, with no additional factor1/2. PVP need not vanish for this formula: the unperturbed P energy is scalar, so the second-order polar expression is still this one.

The ground second-order shift is -L/2:4L elementary transverse flips each have unit squared amplitude and excitation8, with no shorter off-diagonal aligned-state return for L>=3. Adding+(L/2)I in the excited block therefore forms the excitation-energy coefficient, not the absolute-band coefficient. The full512-dimensional L3 control correctly subtracts it back before comparing absolute eigenenergies. I replayed that control: first/second-order projected matrix identities pass; canonical-band operator errors divided by ratio³ are3.3096,3.2458,3.2144 at .04,.02,.01, consistent with the stated finite O(ratio³) remainder. This is numerical confirmation, not a uniform error enclosure.

## Source normalization

The source constructed here is P V |G_sym>/sqrt(L), where |G_sym> is the normalized equal superposition of the eight aligned configurations. There are4L orthogonal one-flip images per aligned vacuum in these tested volumes, giving norm squared4. Independent contraction gives4 at L6 and L8. This is a specified transverse/native source in a selected symmetric ground representative; calling it an operational source for the original diagonal composite would require the separate dressed-observable relation. The core alone does not supply that physical identification or a state-selection mechanism.

## Relative-coordinate control

Starting from source/2, independent orthogonal Krylov construction at L6 and L8 gives dimensions L/2, zero diagonal and positive offdiagonals2 except final2sqrt(2). Signs of basis vectors are a gauge convention; the chosen positive-hopping convention fixes the formulas below. In that space, with A=H1,

B_host=-A²/16+|0><0|/4.

The H2 component outside the host has rank one. Choose the normalized extra vector so that its coupling to host index1 is negative. Then H1 annihilates it, its H2 diagonal is-2, and its sole H2 host coupling is-sqrt(2) at index1 (zero-based indexing; the second chain site). The enlarged space is closed under H2 at both tested lengths. Host coefficient errors are at most3.1e-15; side-energy/coupling errors below2.9e-15; full enlarged-space closure residuals below7.3e-15. Independent output is /private/tmp/neutral-kink-independent.json.

These are finite tested matrix identities, not an independent all-L symbolic proof. The source routine includes full reorthogonalization and retains termination residuals, so its finite Krylov data are appropriately diagnosed. The side channel cannot be dropped merely because it is absent from the first-order source space. Conversely a side channel and continuum-like host do not alone establish a physical resonance width, stable scalar, or uniform large-volume effective theory.

The perturbative variables must remain explicit: in units Jz, excitation H=8I+lambda H1+lambda²H2+..., lambda=Jperp/Jz. A plotted H1+ratio H2 therefore describes the scaled excitation shift (E-E_ground-8Jz)/Jperp through the indicated order. It is not the full microscopic spectrum at arbitrary ratio. Periodic geometry, positive rung parity, source state and finite-band isolation all remain premises.

## SHA256 snapshot

- `/private/tmp/neutral_kink_core.py`: `62cc36f85bb1d6932ccc81db8a9ebe3f0171a7443adc74d2d6564c4da45e4dd8`
- `/private/tmp/neutral_kink_source.py`: `0c645274699c102ba1141d0c75ce143ef1377e696ec33b15f2cf0a20ec783722`
- `/private/tmp/neutral_kink_relative.py`: `2739238bc1053c5c917ace7f557d2aa7c325af83ce4458c5f3697b4b64a91393`
- `/private/tmp/neutral_kink_full_check.py`: `89864930aff6e0c403280cdf85f7f643f4c5c3f4c637c172fca33cef5004b2a2`
- `/private/tmp/neutral_kink_full_check.json`: `577dfd8d9bdcba313b869c32452437581772e03e454fd1987b0c7de05f4c3ef6`
- `/private/tmp/neutral-kink-independent.py`: `11a07e7f0822e7c95c79b8003bd3c9658d8cef50780dd4d57e787fe2de962f6a`
- `/private/tmp/neutral-kink-independent.json`: `c30f3c6080df73ceb1ee003697e4992e0c7e3ab38adb5d8dcdc737b468a6f306`
