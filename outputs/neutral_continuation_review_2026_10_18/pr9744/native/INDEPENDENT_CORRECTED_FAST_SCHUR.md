# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused check: corrected-fast Schur bounds and source limit

The derivation in `/private/tmp/neutral_corrected_fast_schur_root.md` is algebraically and asymptotically consistent, conditional on the separately reviewed corrected-arm strip lemma. I checked that the lemma supplies exactly the bounds used here; no positive-definite lower bound on the whole 2x2 imaginary part is needed.

## Schur factorization

Let the contact-resummed host Green matrix be [[G,c],[c,b]], and write the host-arm coupling as W with rows w=(-2,-lambda/4), u=(-lambda,0). Then

W^T Gh W=G w w^T+E,
E=c(wu^T+uw^T)+b uu^T=O(lambda).

With bounded arm g, define gtilde=(I-gE)^-1 g. This identity is valid without assuming g invertible. It is symmetric because it also equals g(I-Eg)^-1. It differs from g by O(lambda). For real w, the corrected-arm lower bound on Im(w* g w) transfers to alpha=w^T gtilde w, giving Im alpha>=c0/2 and hence |alpha| bounded away from zero for small lambda.

The rank-one resolvent formula yields exactly

Raa=gtilde+G*gtilde*w*w^T*gtilde/(1-G alpha).

As |G| grows logarithmically, |1-G alpha|>=|G alpha|-1 grows uniformly. Thus Raa=O(1), Raa w=O(1/log), and w^T Raa w=O(1/log). All these statements are analytic bilinear identities on the outgoing continuation; they do not invoke positivity of that continued full resolvent.

Writing e1=-w/2-(lambda/8)e2 gives Raa e1=O(1/log)+O(lambda), while its scalar contraction is O(1/log)+O(lambda^2). Cross terms of order lambda/log are absorbed into the displayed O(1/log) term.

## Slow self-energy

For vA=(-d2,-e1), vD=(0,-2e1), elimination of the host produces

rA=-e1-cw-bu,
rD=-2e1.

The leading -e1 and -cw terms cancel because c tends to 1/2 and w tends to -2e1. Consequently rA=O(lambda log). The exact resulting matrix is

M_AA=b+rA^T Raa rA,
M_AD=rA^T Raa rD,
M_DD=rD^T Raa rD.

The proposed estimates follow: M_AA=O(lambda), since its extra term is O(lambda^2 log^2)=o(lambda); M_AD=O(lambda), using the improved Raa e1 bound rather than only Raa=O(1); and M_DD=O(1/log). Thus lambda M=O(lambda/log) in slow units.

The outgoing slow-host correction can be written (I-G_s lambda M)^-1 G_s, avoiding an unnecessary invertibility assumption on G_s. Its difference from G_s is O(lambda/log), uniformly and analytically on the fixed lower disk supplied by the exact partial pole.

## Original leading source

For a host d source, set t=Raa(Gw+cu). The same rank-one identity makes t uniformly bounded. The slow amplitudes are exactly

V_A^T R d=-c+rA^T t,
V_D^T R d=-2e1^T t.

The first tends to -1/2 with error O(lambda log). For the second, the leading term is G alpha/(1-G alpha), which equals -1+O(1/log); the e2 remainder and u term are smaller. Therefore it is -1+O(1/log)+O(lambda log).

Multiplying by the stipulated leading readout coefficient -sqrt(2) gives the normalized slow source limit (1,2)/sqrt(2), with the stated unequal convergence rates. This is a continued-resolvent source amplitude. It must not be silently interpreted as a positive resonance spectral weight, and it does not control omitted terms of the full dressed microscopic readout.

## Pole comparison

The previously checked uniform discrete-Airy impedance has derivative of order 1/f_s at the exact partial-model pole, with nonzero limiting coefficient. Hence an analytic endpoint self-energy change O(lambda/log) shifts that pole by O(f_s lambda/log)=O(lambda^3/log) in slow units, or O(Jz lambda^5/log) physically. A Rouche contour around the exact partial pole, contained in a disk of depth/radius proportional to f_s, preserves the strip and the unique nearby pole for small lambda. The initial disk is selected from the already established partial pole, not from an assumed coupled width.

This step requires uniform bounds on a slightly larger disk so Cauchy estimates and the small contour comparison apply. The root statement explicitly includes those strip and branch conditions. No numerical trend in the accompanying finite-lambda pole data is needed for this argument.

## Remaining scope

The corrected-arm lemma remains an external input to this focused check and is under its own independent review. Subject to that input, there is no new Schur or source-limit gap. The result treats the explicit coupled coefficient model with the specified fast K2 block; native slow K4 bulk terms, additional boundary vertices, higher coefficients, the actual SW remainder, and the full dressed source remain separate. It is not a pointwise real-axis convergence theorem or a full-native resonance claim.
