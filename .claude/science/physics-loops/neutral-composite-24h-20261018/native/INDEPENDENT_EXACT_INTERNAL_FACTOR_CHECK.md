# Independent exact collective/internal rung factorization check

Disposition: PASS. Exact local coordinate identities, corrected signs and the projected second-order interaction are consistent. This is a focused algebra check, not a formal audit or a strong-coupling/bulk conclusion. No pack files were edited; root retains authorship.

Replayed the symbolic source with output redirected to /private/tmp. Independently checked the three declared Pauli pairs: each squares to identity, anticommutes within its pair, and commutes with both generators of every other pair. Their common-positive projector supplies a normalized reference vector; applying the three X generators produces eight orthonormal columns in the declared protected/internal-a/internal-b order. The exact W†hW=I_p tensor(-IZ-XI-YY-ZX) and all four W†D_aW assertions pass.

The corrected physical sign is exact: -(X0X2)(Z0Z2)=+Y0Y2=+YIY, since each XZ=-iY and two such factors give minus. The initially transcribed negative sign would change this coordinate convention and the specified vertex identities; it is correctly treated as a caught operational/algebraic transcription error, not a physical failed route.

The internal h has spectrum(-2sqrt(2),0,0,+2sqrt(2)); its polynomial ground projector h(h-2sqrt(2)I)/16 is rank one and idempotent. The source verifies Tr(p_g B_a)=0 and h B_a p_g=0 exactly for B=(ZZ,IY,YZ,XY). Thus each B_a takes the internal ground into its zero-energy subspace. Projecting TWO internal ground states annihilates every first-order native boundary vertex. This vanishing concerns the ground-projected low band, not arbitrary internal states or the full exact vertex.

Second order has denominator E0-E_virtual=-4sqrt(2) at Jperp=1. The source contraction uses Tr(p_g B_a B_b)^2, which is the product of two same-ordered local overlaps, NOT an absolute square; the protected A_a A_b factors retain the matching complex/Pauli phases. Its sum is Hermitian and exactly yields coefficients II=-sqrt(2)/2, XX=ZZ=-sqrt(2)/4. Replacing those overlap squares by absolute squares would generally lose necessary phases.

As a separate control, built the original full64-dimensional two-rung V=-sum D_a tensor D_a, embedded protected states with a normalized internal ground via W, and evaluated -P V² P/(4sqrt(2)) directly without the vertex-overlap contraction. The first-order norm is3.1e-17 and the result agrees with -(I+(XpXp+ZpZp)/2)/sqrt(2) to4.5e-16. This confirms the signs and protected-axis relabeling relative to the earlier XY expression.

The tensor coordinates are exact within the already selected positive physical Z-parity sector of each four-qubit rung. They do not enlarge the physical Hilbert space or select that sector dynamically. The protected factor is inert under the ON-RUNG h, but the full longitudinal vertices act on it nontrivially together with internal variables; it must not be mistaken for a globally decoupled protected spectator. The note explicitly keeps these couplings. Exact factorization at arbitrary coupling is an identity, whereas freezing the internal ground and the derived exchange require the same weak-longitudinal-coupling low-band assumptions as before. No new interaction, prescribed fluctuating coupling, physical scalar, equal-coupling phase or three-dimensional limit is established.

## SHA256 snapshot

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_exact_internal_factor.py`: `e330a678e8a84a40acaf8cdf4e6dd5fcb45d342487bbedc1e66d7f1d1ff362c0`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_exact_internal_factor.json`: `1013871f18b583c84b1f7a69ae7757a252af05618d140d49cc3531a6bf75573d`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/EXACT_INTERNAL_FACTOR.md`: `d44000935e5401bd84ad06bdb8f30b8e6df47a21805dd76b4260cbc0b7a261f3`
- `/private/tmp/neutral_exact_internal_factor.json`: `1013871f18b583c84b1f7a69ae7757a252af05618d140d49cc3531a6bf75573d`
- `/private/tmp/neutral-internal-independent.json`: `68d3dcff7630a7620648438161cf9a816e422d79aabaf7c34abaccd603c278e4`
