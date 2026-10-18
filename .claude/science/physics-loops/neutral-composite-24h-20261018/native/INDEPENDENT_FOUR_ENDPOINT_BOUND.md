# Four-column endpoint height fiber: exact check

Disposition: PASS for the infinite-longitudinal, common-orientation, four one-wall-column K1 sector and its common-shift momentum-zero fiber. The claimed eigenvalue and flat weight follow exactly. This is not yet a finite droplet or full-native bound-state theorem.

Inspected /private/tmp/neutral_height_fiber.py and enumerated its adjacency through cutoff 3 independently of its eigensolver loop. No canonical files edited.

## Native move signs and invariance

For the native perturbation -XX on x bonds and -YY on y bonds, an x-pair flip has amplitude -1. Since YY|s_a,s_b>=-s_a s_b|-s_a,-s_b>, a y-pair flip has amplitude +s_a s_b. With a common wall orientation, the spins being flipped satisfy s_a s_b=sa*sb in the script. Equal-height upward/downward pairs consequently have y amplitude +1; height-difference-one swaps have y amplitude -1. The x amplitudes remain -1. These signs agree with the code.

On an infinite longitudinal chain, flipping a spin in a one-wall column changes its wall count by zero only adjacent to the wall, and otherwise adds two walls. A spin flip in a uniform exterior column adds two walls. No column in this sector admits a two-wall decrease. Hence a native two-column flip preserves the total four-wall energy only when both columns already carry walls and each flip moves its existing wall. A bond to an exterior column cannot contribute to K1=P_E V P_E. Thus the fixed four-column sector is invariant under full K1, subject to no transverse identifications introducing extra edges.

This argument uses infinite longitudinal chains (or the bulk limit away from physical boundaries), common wall orientation for the written signs, and uniform exterior columns. Open physical endpoints can change the wall-count bookkeeping. A finite droplet with two endpoints per column is not globally the same invariant sector once its endpoints approach; extension to that problem requires additional work. Opposite wall orientations require recalculating the YY signs.

## Exact graph and fiber normalization

Let F=(0,0,0,0). At common-shift COM momentum zero, the reachable configurations are

 X+_n=(0,0,n,n), X-_n=(n,n,0,0),
 Y+_n=(0,n,0,n), Y-_n=(n,0,n,0), n>=1,

and D+=(1,0,0,1), D-=(0,1,1,0). This exhausts the component by applying every allowed move to these states. A cutoff max height<=L therefore has exactly 4L+3 states for L>=1.

The X rays have hopping -2, the Y rays +2. F couples to the two X first sites by -2 each and the two Y first sites by +2 each. Each D node couples to each of the four ray first sites by -1, and has no other links. The factor 2 on ray links sums two distinct endpoint moves, which become the same quotient edge at COM zero. Common shift acts freely, so all orbit normalizations agree; no extra square-root orbit factor is missing. The code correctly retains duplicate COO entries before their summation.

Define normalized ray states

 b_n=[X+_n+X-_n+(-1)^n(Y+_n+Y-_n)]/2.

They form an invariant bright half-line: hopping is -2, F-b_1 coupling is -4, and the D couplings cancel because b_1 has coefficients (1,1,-1,-1)/2.

For a decaying solution write b_n amplitude A r^(n-1), |r|<1, and flat amplitude c. The recurrence and boundary equations give

 E=-2(r+r^(-1)), A=2r c, E=-8r.

Thus r=1/sqrt(3) yields E=-8/sqrt(3), and r=-1/sqrt(3) gives the upper partner +8/sqrt(3). For the lower state, b_n amplitude is 2r^n c and

 1=|c|^2[1+4r^2/(1-r^2)]=3|c|^2.

The flat weight is exactly 1/3. Each individual ray configuration at height n has magnitude |c| r^n, with the alternating Y phase above.

All four ray tails have essential spectrum [-4,4]. The remaining D-symmetric channel has endpoint coupling 2sqrt(2) to a hopping-2 ray, precisely the threshold value: its putative bound root has |r|=1 and is not square summable. The other ray combinations are free Dirichlet rays, and D+-D- is a decoupled zero eigenvector. Therefore there is no competing eigenvalue below -4 in the remaining channels. The bright lower eigenvalue is the unique lower isolated eigenvalue in this reachable fiber component, with gap 8/sqrt(3)-4 to its continuum.

This proves the K1 coefficient result, including its normalization, without using finite-cutoff eigenvalue fits. It does not compare other wall sectors, other transverse shapes, other COM momenta, finite paired-endpoint configurations, or higher-order native couplings. In particular a full native pole, ground-state claim, or physical source overlap beyond the flat coefficient requires the separate extensions noted by root.
