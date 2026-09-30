# A low-density occupied strip still supports the actual dark flux mode

Author analytic discriminator, not an actual Omega-residence counterexample. This is the contract's second mathematical family: test a proposed bound based ONLY on global occupied-B density, after the connected-Gram calculation left its actual source weight open. The former dark plane in KINETIC_DISCRIMINATOR7ef29cb1 had all but one B occupied. Here the SAME actual canceled rotor words admit a source-accessible dark flux mode with B density tending to zero. No new late-tail exponent or lower Omega probability is claimed. The thin-strip geometry and its legal source word are the new assertions.

## 1. Geometry, carrier and charges

Take an even cubic torus with L divisible by8 and L>=16. Let n=L^3/2, m=L/2, and use coordinates modulo L. Sites with x+y+z even are A. Let

 P={h in A: h_y+h_z=m mod L},   p=|P|=L^2/2,
 B_strip={b in B: (b_y+b_z-m) mod L is in {-3,-2,-1,0,1,2,3}},
 v_add=(1,m-4,0),   B_occ=B_strip union {v_add}.           (S1)

The seven layers are disjoint, |B_strip|=7L^2/2, and v_add is outside them. Hence

 k=|B_occ|=7L^2/2+1,
 k/n=7/L+2/L^3 ->0.                                    (S2)

Keep this B mask fixed in the displayed wave. Exactly one A site is empty. For every hole position, the total occupied matter count is M=n-1+k and the physical total charge is n. Put r=(k-1)/2=7L^2/4 negative charges among the M occupied sites and use the normalized equal-amplitude sum over all C(M,r) charge assignments. The same M,r hold at every intermediate hop. This is a physical charge sector; k is odd, as required by the one-hole Gauss parity. A formal one-hole sector with even k would be inadmissible here.

Every such charge assignment has an integer Gauss completion because its total charge equals the fixed background. Fourier decomposition of the cycle-field lattice gives the usual physical rotor fibers. At the zero phase fiber all normalized rotor hop coefficients are1. The displayed mode is a fiber vector, not a normalizable infinite-field physical state. Its use below is an exact algebraic/response discriminator at that fiber. We do not claim that this phase point alone has positive measure.

For k_x=+pi/4 or -pi/4, define

 f_(k_x)(h)=p^(-1/2) exp(i k_x h_x)(-1)^(h_z) 1_P(h),
 psi_(k_x)=f_(k_x) tensor the above normalized charge sum. (S3)

Since m is even, supported h_x is even. Periodicity is exact for L divisible by8.

## 2. Complete canceled Hamiltonian columns, not an imposed B constraint

Use the ACTUAL rotor leading operator H2=C+[F,F*] and original loss G=sum_mu j_mu*j_mu from the previously read exact one-hole argument. For a one-hole input at h, cancellation of disjoint F/F* terms leaves: the six fill-and-return paths; paths filling h from an occupied shared B then moving a charge from a neighboring A back to that same B; and the gated/empty-B correction terms whose B factors are at graph distance at most3 from h. A negative first hop in the latter terms needs an empty such B. This statement includes the terms with another A center up to distance2 and its outgoing link; it is not the assertion that F vanishes globally on this partially filled torus.

For h in P, EVERY B within nearest-neighbor distance<=3 belongs to B_strip: the coordinate y+z changes by at most3 along such a path. All those B sites are occupied. Therefore every correction requiring such an empty B vanishes on this input. The remaining complete H2 column is exactly K* K, where K maps an A hole to its six neighboring B intermediate holes, with the corresponding charge swap. There are no omitted output columns. The charge sum is preserved bijectively by each charge swap, so in this equal-charge sector K is the scalar nearest-neighbor incidence matrix. This is a conclusion about the full action on the displayed inputs, not an artificial compression to a fixed B mask.

Similarly G psi=0 because each supported hole has all six neighboring B sites occupied. Both original instruments have this loss property; a coherent mark does not create an event when its B site is occupied.

Let g=K f. At a B site with y+z=m, only the two x-neighbor A holes contribute, giving 2 cos(k_x) times the plane wave. At either adjacent transverse layer, the y and z contributions have opposite signs and cancel. All other layers receive no contribution. Applying K* again gives

 H2 psi_(k_x)=4 cos^2(k_x) psi_(k_x)=2 psi_(k_x),
 G psi_(k_x)=0.                                        (S4)

The cancellation includes outputs outside P. The extra occupied v_add is at distance at least5 from P and changes none of these columns. It was added solely to enforce physical parity.

## 3. Exact flux velocity

Orient each link A->B and set

 E_x=sum_(a,b) d_x(a,b) E_ab,
 d_x=+1,-1,0 for the periodic nearest-neighbor x direction.

The charge-averaged current can be computed by differentiating the complete physical link phases, equivalently by the literal two-hop field increments. A path moving the hole from h to a through occupied B site b changes E_x by

 Delta E_x=q_b d_x(h,b)-q_a d_x(a,b).                    (S5)

In the normalized fixed-total-charge sum every occupied-site charge has mean qbar=n/M. Thus the mean increment is qbar[d_x(h,b)-d_x(a,b)], including wrap-around links. With H_{a,h}=1 for this path, i[H,E_x]_{a,h}=-i Delta E_x H_{a,h}. The plane-wave sum gives

 <psi_(k_x), i[H2,E_x] psi_(k_x)>
             =qbar d/dk_x[4 cos^2(k_x)]
             =-4 qbar sin(2 k_x).                       (S6)

At the two chosen momenta this is respectively -4n/M and +4n/M, approaching -4 and +4 as L grows. The sign convention is tied to the stated A->B electric orientation. The nonzero current is a phase-fiber derivative; it does not contradict stationarity of the fiber eigenvector because E_x differentiates the field phase rather than acting as a bounded within-fiber matrix.

Consequently an all-state/all-fiber absorption or flux-stalling estimate that becomes coercive solely because k/n is small is false for this actual law. Neither (S4) nor(S6) says that the actual Omega source has a nonvanishing macroscopic weight in these waves. In particular, the two velocities can occur with equal source overlap and cancel the linear flux mean.

## 4. Exact ordinary-birth/source word

A legal primitive word reaches a component with this B mask and hole a=(0,m,0), with all fields in {0,+1,-1}. It needs O(L^2), rather than O(L^3), ordinary preceding births. Here are explicit pairings; they also fix all counts without a Hilbert-space enumeration.

On each (y,z) row included in B_strip, the B x parity is p_x=(1-y-z) mod2. Initially pair x=p_x+4j with x=p_x+4j+2, through their midpoint A, for j=0,...,L/4-1. On the special row (m,0), instead pair (L-1,1),(3,5),(7,9),...,(L-5,L-3). Delete the pair(L-1,1); the two unpaired sites are

 b_1=(1,m,0), b_2=(L-1,m,0).

Delete the default pair(0,2) on row(m-1,0), leaving b_3=(0,m-1,0) and d_1=(2,m-1,0). Delete the default pair(1,3) on row(m-2,0), and replace it by the cross-row pair d_1 with (3,m-2,0), through A(2,m-2,0). Delete the default pair(0,2) on row(m-3,0), and add the cross-row pair (1,m-2,0) with (0,m-3,0), through A(1,m-3,0). Finally pair (2,m-3,0) with v_add=(1,m-4,0), through A(2,m-4,0).

Every B_occ site except b_1,b_2,b_3 is paired exactly once. The A centers are distinct, and none equals a. The number of pairs is

 b_old=(k-3)/2=7L^2/4-1.                                (S7)

For each pair, perform the actual outward hop of the center's original plus charge into the first B, then the original plus birth on the second edge. This is a legal term of the ordinary leading W0 birth jF, leaves the center occupied plus, and creates one plus and one minus B. All selected edges are distinct; intermediate fields remain0,+1,-1 and Gauss is exact. These are also legal unit-amplitude spin1 steps, but the spectral assertion(S4)--(S6) is a rotor assertion, not a finite-spin conclusion.

At a, use the exact positive-grade source word

 -F_a j_(a,b_2,+) F_a,

choosing the first outward hop into b_1, the marked birth on b_2, and the last outward hop into b_3. It leaves one A hole, fills the three remaining B sites with signs plus,minus,plus, and adds one negative charge. The final negative-charge count is b_old+1=r, exactly as required. The final source field shifts are -1,+1,-1 on these three links.

At the zero phase fiber all selected ordinary leading-birth coefficients are nonnegative, and all summands of the displayed source have the same overall minus sign. Taking complete original marks cannot cancel the selected component: alternative branches outside the specified B mask are orthogonal, while branches inside it have the same sign. With f_(±pi/4)(a)=p^(-1/2), the magnitude of the complete word overlap with either normalized psi is at least

 [p C(M,r)]^(-1/2)>0.                                   (S8)

This is algebraic source accessibility by the actual maps, not a lower bound on the actual finite-time ensemble probability after all intervening Hamiltonian/loss evolutions. It does not prove a failure of connected-Gram density, weighted residence, or any Omega energy estimate.

## 5. What this prunes, and what it does not

The example rules out a scalar low-GLOBAL-B-density hypothesis as sufficient for an all-background leading-fast flux/absorption estimate. A global source-number mean of order nT does not by itself exclude the O(L^2) word(S7) at fixed T. That observation is only logical insufficiency: it is not a claim that the word is typical. Spatial connected-source weights, actual phase/spectral overlap, and complete same-grade/finite-spin evolution could still suppress its contribution strongly enough to prove the desired estimate. Those remain the source-sensitive quantities needed by CONNECTED_LEDGER(20).

No exponentially decaying field tail, late-age lower bound, probability from bare Omega, exact finite-spin dark sector, or obstruction to a volume-uniform actual energy density is inferred. The supplementary exact control, if executed, checks the literal pairing/Gauss/plane-incidence and flux sums at three declared L values. The all-L proof is the explicit construction above.
