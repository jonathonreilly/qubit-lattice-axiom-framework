# Focused original-source correction at L6

Disposition: PASS for the derivative coefficient, canonical-connection order count, and leading amplitude conditional on the stated aligned-column/four-defect source graph. No full native replay or complete effective-operator certification is claimed.

I independently implemented an exact Fraction subset recurrence for the minimum-order two-column process. At a proper flipped subset S, the energy cost for H+sC is 4Jz*w1(S)-4s*w2(S), where w1 counts open nearest-neighbor cuts and w2 counts open distance-two cuts. The denominator in the resolvent is the negative of this cost. Combining all L negative transverse vertices with L-1 negative denominators leaves the effective hopping -t(s), with t(s)>0 near zero. Decreasing the excitation cost with positive s increases t, so the bare observable term is -t'(0)T, not +t'T.

At Jz=1 and unit transverse coupling, exact recurrence gives t=1/2^(L-1) and t'/t=3(L-2)/2 for each L5..12. In particular L6 gives t=1/32, t'=3/16, hence t'=6t/Jz after restoring units. These finite exact checks do not assert an all-L proof of the closed form. Controls: neutral-column-source-derivative.py/json.

## Combining the two source contributions

Write H_eff=-K4 sum P -tT+..., C_eff=c4 sum P -t'T+..., where the previously checked open-column coefficient is c4=-3(L+13)Jx²Jy²/(128Jz^4). At L6, K4=20 Jx²Jy²/(128Jz³), so c4/K4=-57/(20Jz).

An elementary pair-column flip creates four plaquette defects. It costs Delta=8K4 and changes sum P by -8. The first-order ground admixture is +t/Delta times the corresponding defect state. Combining the ground and excited-state admixtures in the off-diagonal C matrix element gives

    (t/Delta)(C_def-C_vac) = -c4*t/K4 = +(57/20)t/Jz.

The direct off-diagonal observable contributes -t'=-6t/Jz. Their sum is therefore -(63/20)t/Jz per elementary 2×1 or1×2 rectangle, in the same hopping/source sign convention. Omitting the direct derivative would give both the wrong amplitude and the wrong spectral weight. A common phase change of the defect basis changes the total amplitude sign, but not this relative interference or its squared magnitude.

## Canonical connection

For a smooth real canonical isometry W(s), set A=W†d_sW. Then d_s H_eff=C_eff+[H_eff,A], so C_eff=d_s H_eff-[H_eff,A]. The commutator is not generally zero. Here the unperturbed aligned projector is s-independent. Matrix elements of A between different aligned configurations require at least L transverse operations across the two virtual tails: any changed column must have all L physical spins changed, and one operation touches at most one site in that column. Lower-order diagonal elements vanish because a real anti-Hermitian matrix has zero diagonal. Thus A has no entries below orderL in this real canonical gauge. Lower H_eff orders are scalar until the order-four plaquette term. The connection commutator consequently cannot affect the L6 observable coefficient (its first possible non-scalar contribution has order at least L+4). Differentiation is therefore valid through the order used here. This reasoning is gauge/order-specific, not an exact identity C_eff=d_sH_eff at all orders.

At L6 the displayed transition amplitude is orderlambda^6 and its weight orderlambda^12. Sixth-order diagonal observable terms multiplied by the orderlambda² ground admixture enter only at orderlambda^8 in the amplitude; they do not alter this leading coefficient. Same-order Hamiltonian terms can still change the eigenvectors and star-source spectral weights, so the complete relevant sixth-order defect operator remains essential.

## Weight convention and limits

Multiply (63/20)^2*(t/Jz)^2 by the spectral weight of the TWO-END source with norm squared2. If a normalized symmetric endpoint source is used instead, an additional factor2 is required. For example, the zero-offset conditional star weights4/9 already include norm²2; they must not receive another factor2. They also must not be reused at the L6 nonzero K6 offset without recomputing the star eigenvector/residue.

This checks a leading source amplitude for the supplied existing longitudinal observable in a conditional effective model. It does not certify the truncated star as the complete native theory, prove native bound-state stability, fix a physical preparation/coupling, or establish a scalar. No repository files were edited and no formal audit was performed.

## SHA-256 identities

- `/private/tmp/neutral-column-source-derivative.py`: `7945a9f097695681032f9420e8d572a0862f4fbe496b509d39503cfd0508dac1`

- `/private/tmp/neutral-column-source-derivative.json`: `c3b9a39a8313973a17242dd60e63161cdf8988f37890828e9022c075f79d10a1`

- `/private/tmp/neutral-column-readout-check.md`: `6bf59c48dc5bfb616f727d820e654b226b0b6d8627fca5710c1650e063f536d5`

- `/private/tmp/neutral-column-star-check.md`: `902bd1f66095db8536d83e59c9bc0dac064cf7aa1926fa909f072da58e947e1e`
