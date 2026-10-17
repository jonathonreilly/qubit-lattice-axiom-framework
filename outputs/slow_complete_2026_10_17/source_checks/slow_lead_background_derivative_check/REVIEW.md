# Selective check of the full-background derivative certificate

Disposition: **supported as a conditional, coarse real-band estimate**. I find no substantive correction required in the frozen proposal `slow_lead_background_derivative/PROPOSAL.md`, SHA256 `603919c05d1ade774f478474b0d09ee781bf298918d3ebc19b37e7eac6c22020`. In particular, its complete finite-background bound `Bstar<10^95` and its fixed `g=10^-6` consequence `M1<6.06e103` follow from the stated source premises. This does **not** support `M1<=10^17`, the illustrative complete-output onset, or a new useful device runtime.

## Exposure, scope, and identity

This is a distinct check of the new full-inverse argument, not an independent recalibration of the device. I did not author this proposal. I previously authored several of its recovery, gate, uniform-endpoint and composition ancestors, and checked related attachment/kernel work. The parent supplied the intended route and the main risks before this check. These exposures preclude describing this as independent ancestral recertification.

I read the complete changed proposal, the converter composition, endpoint and widened-band arguments, and the complete onset frontier and its check. I refreshed the canonical original source/kernel/filter and predeletion passages and reused the unchanged previously read gate and recovery derivations for their exact interfaces. In particular, the argument below inspects arbitrary-forcing coverage rather than treating a previously accepted endpoint column as a full inverse. All sixteen source/check identities listed in the proposal were rehashed and match, including the canonical original note `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. Hashes establish identity only. No numerical inverse, solver, experiment, parameter search, Git action, publication or source modification was performed; this review is the sole new artifact.

The retained premises include the exact supplied original calibration and coefficients; original `M16` and filter inverse bounds; fixed geometry and real internal basis; and the stated real-band domain `.0027<j<.003`, `0<g<=10^-6`, `0<h<=4e-6`, `2j sin(h)/g<=.024`. No claim about native preparation or physical realization is added.

## Reconstruction of the load-bearing steps

**Arbitrary finite forcing in the original source.** The original `M16` inverse controls core/core blocks, and its contact/exterior propagation controls mixed blocks with nonnegative outgoing powers. Exterior/exterior blocks have the free-plus-image form, with bare bounds below250. Thus the two-site filter correction is bounded by

`2*250^2*(1/20)*2000 = 12,500,000`.

Physical port mixing costs at most a factor two on the individual physical blocks. Adding the bare term still gives a block bound strictly below `3e7`. This covers the90 original arm heads and both41-site buffers; it is not restricted to endpoint forcing. No growing closed root is used. For172 heads the block-operator estimate gives `172*3e7<5.2e9`; restricting one index to the two boundary heads gives `sqrt(172*2)*3e7<6e8`. These are bounds on8-by8 blocks, so an extra fiber-dimension multiplier is unnecessary. Complex symmetry, rather than Hermiticity, supplies the equal cross norms.

**Converter sign and noncommuting order.** Changing the old boundary diagonal from `2J` to `J+j` and its eliminated selfenergy from `-JQ` to `-J S0 Qn` changes `E-H` by exactly

`D=J-j+J S0 Qn-JQ`.

The original image coefficient is `T=S_old A`, with A on the right. The diagonal matrices commute with one another, but not generally with `S_old`. With `C=I+AD` and `r=-AD C^-1`, direct multiplication gives

`I+G_BB D = (I-Q^F S_old Q^F r) C`.

This preserves the required ordering. The old open/closed root bounds give the asserted `C^-1<112`; the converter full reflection bound is below.2. The full generalized original scattering norm below1.0001 follows from its open unitary block and both cross/closed bounds, rather than applying unitarity to closed channels. Thus the feedback inverse is below1.26 and the total inverse below142. The ordered Woodbury correction `G_OB D(I+G_BB D)^-1 G_BO` is correct and yields `<6e18`.

**Lift and full input deletion.** The free new-halfline kernel is `An[Qn^|m-n|-Qn^(m+n+2)]`, and the old-to-new lift has magnitude `(tau_c/j)Qn^(m+1)`. The bounds400 and3 consequently apply to all retained coordinates. The212-head norm is below `212*6e19<2e22`. The deleted site is input21; retaining input0 through20 with its unchanged diagonal is precisely the Dirichlet deletion in the endpoint proof. Its `Z^-1<24` is a full eight-coordinate estimate, still valid in the widened band, not an inverse of the selected scalar alone. The full-coordinate Schur/deletion identity therefore gives

`2e22+24*(2e22)^2<1e46`.

Deletion disconnects the exterior behind site21, so retaining no part of that exterior is legitimate.

**Gate load sign and the one-edge round trip.** At cable site `a=v17`, eliminating the actual gate gives `-j^2 Gg` in the matching matrix, whereas the old free load gives `+jQn`. Their difference is `Dg=-jQn-j^2Gg`, as stated. For a scalar channel write `w=Qn` and `z=Gg`. Then direct algebra gives

`rho=-w(w+jz)/(1+jwz)`.

The gate-port reflection is `r_gate=(-1-j w^-1 z)/(1+jwz)`, hence `rho=w^2 r_gate`. The round trip is therefore two powers at the last cable site and36 powers at v0. This checks the reference-plane shift independently of the norm estimates. Also `Cg^-1=I+rho` follows exactly. Invertibility uses the regular input-loaded gate and the explicit closed-channel gap; it does not follow from assuming `Dg` small.

**Full gate feedback, including closed forcing.** The terminated-source boundary kernel has image term `Qn^17 S^D An Qn^17`, so the ordered factorization in Eq.(14) follows by the same algebra as above. The upstream estimates apply to the full generalized `S^D`: selected modulus1, `CP<2`, whole norm `<2e8`. Combining these with the selected gate reflection `.0062` and the closed attenuation `60^-17` gives a sum of the four block ceilings below.0063. Taking this block sum is a valid operator-norm upper bound, without normality. In particular the large closed forcing columns are paid for; they are not silently discarded. Thus the full boundary inverse is below4.1, and

`1e46+.117*4.1*(1e46)^2<5e91`.

Restoring all24 gate heads is a full two-block Schur inverse. Its two triangular factors have norm below `1+j*(38/j)=39`; splitting off the standalone gate block gives `<39^2*5e91+38/j<1e95`. The count is `172+22+18-1+24=235` finite heads, each with eight internal coordinates, for dimension1880 in each stated sector. No part of the argument assumes that the nonnormal boundary matrix is Hermitian or normal. The fixed real structure gives the other spectral lip by conjugation. It does not require commuting the supplied K through the source.

## Derivative and scope of the conclusion

With the unchanged full endpoint-forcing recovery bound `||F||<4e5`, the identity `F'=-R M'F` and `||M'||<=1+j/(1.99g)` give the finite-coordinate derivative. The closed-root tail lift has norm contribution below.00068 and derivative contribution below.009. The latter can also be checked from `v'=v^2/[g(1-v^2)]` and the geometric-series derivative norm, with the closed gap keeping `|v|` proportional to g. The closed projectors are fixed; no projector derivative is omitted. Consequently Eq.(19) follows for the complete finite-plus-closed recovered column on both lips.

For fixed `g=10^-6`, `1+j/(1.99g)<1510`. The leading multiplier is `1.00068*1510*4e5=604,410,720`, so the stated strict bound `6.06e103` leaves room for the additive3600. Positive g and the separated real windows give local analytic root branches. The established inverse at every real point suffices for local differentiability; a uniform complex strip is neither proved nor needed for this derivative identity.

The uniform Bstar statement concerns real-band inverse values as g decreases. Its derivative bound explicitly grows as `1/g`; no uniform derivative at g=0 follows. The finite-coordinate estimate extends to spectator references by the operator norm, but does not itself prove a temporal complete-state error theorem. Inserting it in the already specified integration-by-parts interface retains that interface's cutoff terms, omitted-state charge, and separate actual-incoming requirement. It provides an explicit very coarse constant, not the desired sharper one. The reported sources of slack are upper-bound losses, not physical impossibility results.

No correction is requested within this scope. Formal retained status and any later publication/integration judgment remain separate from this selective analytical check.
