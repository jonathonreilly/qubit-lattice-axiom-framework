<!-- Original PR9794 source SHA256 16b3ec23780638e2a352ef9c5f57642d236fd9e8b669cefd427ea2e37e32dad9. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Extended particle-conditioned environment check

PASS. The transport estimate yields a genuine growing, particle-relative, high-probability flat-flux neighborhood in the declared dressed singleton coordinates. It does not select a minimizer radius or prove an undressed classical domain. The state and geometry qualifications below are essential.

## Exact transport estimate

Write the normalized singleton state as position-indexed background vectors psi_i, and set delta=<T+4>=sum_edges ||psi_i-U_ij psi_j||^2. The link signs and plaquette projections B_p=(I-P_p)/2 are commuting diagonal operators on the background Hilbert space. Thus each B_p commutes with every path transport W_i,d.

Choose a displacement d and a fixed translated nearest-neighbor path of length r=|d|_1 from i to i+d, and let

    S_d=sum_i ||B_(i+d) psi_i||^2,

where B_j denotes the plaquette with the fixed anchor convention at j. Splitting psi_i into W_i,d psi_(i+d) and its transport error, and using ||B||<=1, gives

    S_d <= 2 S_0 + 2 sum_i ||psi_i-W_i,d psi_(i+d)||^2.

The first term is S_0 after translation of the index because B commutes with W. Telescoping along the path, applying Cauchy–Schwarz to its r terms, and summing over i gives

    sum_i ||psi_i-W_i,d psi_(i+d)||^2 <= r^2 delta.

For each path step the sum over i is precisely a directional edge-gradient sum, bounded by delta; translations do not create an extra volume factor. Consequently

    S_d <= 2 S_0 + 2 r^2 delta <= 2 F+2 r^2 delta.

The proposed constants are valid, although not optimized. The result also holds for mixed states by purification or linearity.

## Growing distances and joint patch event

For the previously established near-minimal states, delta,F<=C lambda^(3/2) with constants uniform along R comparable to lambda^(-1). Therefore

    sup_(|d|_1<=L) S_d <= C lambda^(3/2)(1+L^2).

For L comparable to lambda^(-q), this tends to zero whenever 0<=q<3/4. This is a uniform bound on each displaced plaquette's bad-flux probability. It is not yet a simultaneous statement about every plaquette in that region.

For a particle-relative square D_L of plaquette anchors, all B_(i+d) commute, so the exact event projector for at least one bad plaquette is

    Q_i,L=I-product_(d in D_L)(I-B_(i+d)).

The union inequality Q_i,L<=sum_d B_(i+d) yields

    sum_i <psi_i,Q_i,L psi_i>
      <=sum_(d in D_L) S_d
      <=C lambda^(3/2)(L^2+L^4).

Thus for 0<q<3/8, L comparable to lambda^(-q), the probability of any bad plaquette in the entire relative square vanishes. Equivalently, a joint measurement of the dressed particle position and background flux has, with probability tending to one, all plaquette signs plus in that growing relative square. The leading failure bound is O(lambda^(3/2-4q)). At q=3/8 the argument gives only an order-one bound; it gives no vanishing conclusion there or beyond.

Take the square and its fixed path convention away from torus wrapping. Since q<3/4<1 and R is comparable to lambda^(-1), these choices fit for all sufficiently small lambda. The simultaneous patch statement uses the stricter q<3/8.

## Actual-state and dressing qualifications

The input energy condition is the prior one: states in the actual isolated microscopic two-wall cluster with energy within O(Jlambda^(5/2)) of its lower asymptotic minimum. Transform by the declared local SW unitary and project into the normal-form N=2 block. The actual-cluster leakage is O(lambda^3) in vector norm; a mere low energy expectation without spectral-cluster support does not supply this estimate.

The singleton projection has weight 1-O(lambda^(3/2)); the half-column part is controlled by its order-Jlambda excess. Normalize the singleton projection before using probabilities, or state the corresponding unnormalized version explicitly. Exact odd physical-Z states have no half-column component. Conditioning changes the stated orders by at most their bounded normalization factor. If half-column events are counted as failure in an unconditional statement, they add O(lambda^(3/2)).

The growing-patch event operator has norm one, independent of L and R. Therefore transfer from the projected state to the actual dressed state costs O(lambda^3), not L^2 times the leakage. This remains negligible throughout the above ranges. No replacement of the dressed event by a bare microscopic local measurement is justified by this argument; such a replacement would require separate dressing estimates.

## Claim boundary

This is stronger than the earlier trial-patch construction: it constrains the joint particle/environment statistics of every near-minimal state in the specified cluster. It establishes a high-probability conditional region with no plaquette flux defects at the stated growing scales. It does not prove a selected domain radius, a fixed classical column-sign pattern, a spatially localized particle center, an unconditional globally flat background, a bare microscopic domain observable, or an emission/scattering theory. Flat plaquette signs themselves still allow the row/column sign freedom and quantum superpositions compatible with that constraint.

## Addendum: contrast with a symmetrized actual vacuum

The proposed comparison is valid without a growing-volume vacuum spectral-gap assumption. Let N=R^2 and symmetrize an actual ground density matrix under translations and the native x/y exchange symmetry (including the accompanying spin rotation). The equivariant SW map and N=0 projection preserve these symmetries. The order-one separation from wall sectors gives projection leakage O(lambda^3), and its normalized vacuum-block energy is within O(Jlambda^3) of the coefficient-block minimum. This uses the global remainder and spectral-cluster separation, not the potentially small internal gap of K.

Since Hb=scalar+Jlambda^4 K/128 and K=-5E-4P, the flat logical-X trial gives min K<=-10N. Thus the projected symmetric state satisfies

    -5<E>-4<P> <= -10N+O(lambda^(-1)).

Using <P><=N yields <E>/(2N)>=0.6-O(lambda), since N is comparable to lambda^(-2). Symmetry makes this the expectation of each equivalent edge operator. For a plaquette and an anticommuting boundary-crossing edge, the involution inequality gives

    <P_p> <= sqrt(1-<E_edge>^2) <= 0.8+O(lambda),
    <B_p> >= 0.1-O(lambda).

The bounded dressed plaquette observable incurs only O(lambda^3) projection-transfer error. Therefore this lower bad-flux probability holds in the explicitly symmetrized actual dressed vacuum reference, whereas the heavy state's particle-relative probabilities tend uniformly to zero on the previously specified growing displacement ranges.

This demonstrates a local conditional environment contrast, not merely a statement about the particle's center-of-mass participation. It requires no clustering and no inference of independent plaquette events. “Over a growing area” should mean the uniform marginal contrast at those growing sets of relative positions (and the separately proved joint heavy flat-patch event), not a claim about an extensive number of independent vacuum defects or a probability law for a sharp domain boundary. Unsymmetrized actual ground states require an additional symmetry argument and are not covered by this comparison as stated.
