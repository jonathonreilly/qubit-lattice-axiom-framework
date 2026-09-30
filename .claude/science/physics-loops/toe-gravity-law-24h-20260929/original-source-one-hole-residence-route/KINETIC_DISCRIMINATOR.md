# A nonzero-velocity dark one-hole fiber of the actual rotor coefficient

This is a separate analytic discriminator, not a physical preparation or an actual-source residence lower bound. It addresses the proposed mechanism that a loss-dark long-lived one-hole mode must have vanishing electric velocity. The result uses the ACTUAL cancelled H=C+[F,F*], not the false global FF* factorization. The earlier source late-tail construction is credited explicitly. No new numerical run is claimed.

## 1. Exact physical charge fiber and local words

Take the rotor leading coefficient on a periodic cubic torus with L>=8 divisible by8, N=|A|=L^3/2, m=L/2, and the sole B vacancy v=(1,0,0). Use global W1 and N_B=N-1. Gauss neutrality fixes total charge N; hence among the2N-2 occupied matter sites there are r=(N-2)/2 minus charges. For each hole/B-vacancy pattern use the normalized equal-amplitude sum over all binomial(2N-2,r) assignments. This is the same physical charge fiber used in the checked source late-tail proof, not an all-plus nonphysical state.

A spanning tree identifies physical fields as the charge-dependent integer tree flow plus independent integer cycle currents. At zero cycle angle every allowed rotor hop permutes charge assignments bijectively between the corresponding vacancy patterns, with coefficient one and the same normalization. Intermediate W0 and W2 patterns are included. No fermionic signs or proxy hopping law is introduced.

On a one-hole input h, the exact local blocks are

 P_h H P_h=P_h[F_hF_h* -sum_(c!=h,dist_1(c,h)=2)F_c*F_c]P_h,
 P_a H P_h=P_a[F_a,F_h*]P_h, a!=h,                         (1)

where the compensation gate has already canceled the distant same-hole contributions. With every B within distance three of h occupied, each negative same-hole first hop in(1) is blocked. The surviving return and shared-B move give the adjacency-square K*K on the symmetric-charge vacancy-pattern vectors, with v fixed, INCLUDING every output. A shared occupied B passes its charge to h, then receives the charge from a. Off-center terms in the full commutator cancel distant vacancy relocation. In particular the global identity H=FF* is not being asserted; C and F*F can be nonzero on these inputs.

## 2. An exact band of dark plane waves

Let k be compatible with the period, and on A set

 f_k(h)=exp(i k h_x)(-1)^(h_z)1_((h_y+h_z) mod L=m).       (2)

There are p=L^2/2 supported holes. Their x coordinate is even. Every supported hole has periodic graph distance at least m+1>=5 from v, so(1) applies to the entire input wave. Let psi_k be the normalized wave with the charge vectors of section1.

The y and z contributions of A-to-B adjacency cancel pairwise: the support condition selects equal displacements of y+z, while the z shift reverses the sign. The two x-neighbor contributions add to2cos(k) times the corresponding B wave. Applying the reverse adjacency gives4cos^2(k) f_k, with all off-plane outputs canceling. Therefore the ACTUAL leading rotor operators satisfy

 H(0)psi_k=lambda(k)psi_k,  lambda(k)=4cos^2(k),
 G psi_k=0,  G=sum_mu j_mu*j_mu,  ||psi_k||=1.             (3)

The loss is twice the number of empty B neighbors of the hole for either original instrument. Equality of loss does not identify their recycling maps. Choose k=pi/4 and -pi/4. The two waves are orthogonal because L is divisible by8 and the x sum over even sites of exp(i pi h_x/2) vanishes. Both have lambda=2. The old checked late-tail wave was k=pi/2, lambda=0. We do not present its polynomial survival lower bound again as a new theorem.

## 3. Actual electric current and charge averaging

Orient every link from A to B and let d_x(e) be its signed nearest-neighbor x displacement (+1,-1 or0), also for wrapping links. Consider the physical extensive x electric flux

 E_x=sum_e d_x(e) E_e,
 V_x=i[H,E_x].                                           (4)

H is a bounded finite-range rotor shift operator on the W1 sector; its field bandwidth is finite, so(4) extends to a bounded self-adjoint operator there. On finite-field words it is the literal commutator. It preserves Gauss. It is not an electric energy replacement; it is only a current discriminator.

For a surviving two-hop hole move h -> a through an occupied B site b, the first inward hop changes E_hb by +q_b and the second outward hop changes E_ab by -q_a. Thus its exact change of(4)'s flux is

 Delta E_x=q_b d_x(h,b)-q_a d_x(a,b).                     (5)

Each occupied charge position in the normalized Dicke vector has mean

 qbar=N/(2N-2).

Averaging the matrix element over the bijective charge assignments therefore gives

 average Delta E_x=qbar[d_x(h,b)-d_x(a,b)],               (6)

the actual signed two-step hole displacement multiplied by qbar. Same-hole returns have zero flux change. All negative/canceled paths in(1) remain canceled in the commutator, since the canceled terms are equal operators and hence have identical field increments. This is not a diagonal-charge substitution for H: only the displayed current matrix element between specified coherent charge test vectors has been evaluated.

In the wave(2), every displacement d contributes the factor exp(-ikd_x), with the exact path multiplicity of K*K. Since the current matrix is -i Delta E_x times the Hamiltonian matrix, differentiating this finite Fourier sum gives

 <psi_k,V_x(0)psi_k>=qbar lambda'(k)=-4qbar sin(2k).       (7)

For a direct check of this derivative, the only terms connecting two supported holes with nonzero x displacement are h -> h+2e_x and h -> h-2e_x. Each has one shared-B path and averaged flux increment respectively +2qbar and -2qbar. Their expectation is -i 2qbar[exp(-2ik)-exp(2ik)]=-4qbar sin(2k). The sign follows the A-to-B flux orientation and exp(+ikh_x) convention. In particular

 |<psi_(pi/4),V_x(0)psi_(pi/4)>|
                         =4qbar=2N/(N-1)>0.             (8)

This calculation uses the signed periodic nearest-neighbor steps in(5), not a coordinate difference across the torus wrap. The uniform x one-form has nontrivial periodic holonomy. In spanning-tree coordinates E_x is a cycle derivative plus a charge-block tree-flow diagonal. A change of reference tree adds the corresponding finite-dimensional commutator; its expectation in the exact H eigenvector is zero. The direct physical increment calculation(5)-(7) is consequently gauge/reference independent.

Restricted between psi_(+pi/4) and psi_(-pi/4), the current's offdiagonal matrix element vanishes by the same finite x Fourier sum; the diagonal entries are opposite nonzero values. Thus the compressed velocity has a nonzero square on their standing-wave sum even though that sum has zero mean compressed velocity. This last assertion is about the two-dimensional test subspace, not an assertion about the unprojected actual source's V_x^2 expectation.

Equations(3),(8) disprove, on all such fibers, a proposed universal stalling inequality of the form

 |<psi,V_x psi>| <=C[<psi,Gpsi>+||(H-lambda)psi||]

for normalized psi and all spectral parameters lambda. Both terms on the right vanish on psi_(pi/4), while the left is nonzero. They do not disprove a source-sensitive averaged inequality, a finite-spin crossover, a field-weighted Dirichlet estimate or a signed work cancellation. The mode has an oscillating phase under the no-event evolution; it is not a zero-energy vector.

## 4. Actual source overlap and exact limitations

The already checked actual-source word can be reused without changing a label. Its complete construction is in original-record-source-late-tail-route/REPORT.md sections3-4: fill all B except v and three neighbors b1=(1,m,0), b2=(L-1,m,0), b3=(0,m-1,0) of a=(0,m,0), using (N-4)/2 ordinary ORIGINAL formations b_mu=j_mu F_center with distinct matched B pairs. Then use the ORIGINAL positive-source coefficient at(a,b2),

 B_mu^+=-F_a j_mu F_a:
      a -> b1, birth at(a,b2), a -> b3.                   (9)

The selected path is Gauss legal, all its fields are0,+1,-1, and its final hole is a with only v vacant on B. It has exactly r minus charges. At zero cycle angle every ordinary word coefficient is nonnegative, and the full source has one common minus sign. This holds separately for resolved marks and for the original unnormalized coherent sum. All unobserved paths remain in the operator. Since f_(+pi/4)(a)=f_(-pi/4)(a)=1, the full original word Phi0 has

 |<psi_(+pi/4),Phi0(0)>|,
 |<psi_(-pi/4),Phi0(0)>| >=[p binomial(2N-2,r)]^(-1/2).    (10)

Their overlaps are equal real numbers with this convention. Thus no nonzero mean current of the actual real zero-waiting source is inferred: the two opposite velocities cancel on this pair. A nonzero projection onto a current-carrying subspace alone would not prove a lower bound for the original unprojected source current or current square.

Each psi_k is a single-angle finite-dimensional fiber vector, not a normalizable physical rotor preparation. Equation(10) is an overlap test on the actual original finite word, not a grade-resolved postselection or a lower probability at physical times in a growing-volume microscopic sequence. The old finite-graph Sobolev argument can make the word section continuous for small positive source time, but none of that supplies a useful low-moment or volume-uniform residence estimate here. In particular the finite-angle measure, the very high source-event order, counter-propagating interference and complete finite-spin neutral corrections remain capable of paying or changing the response.

This discriminator removes a simple velocity-stalling shortcut. It does not establish failure of the actual Omega residence target, identify the exact kernel in EXACT_ONE_HOLE_REDUCTION.md with this bare rotor coefficient on physical time, or supply an alternative energy observable. No new control, empirical calibration, physical clock or foundation selection is claimed.
