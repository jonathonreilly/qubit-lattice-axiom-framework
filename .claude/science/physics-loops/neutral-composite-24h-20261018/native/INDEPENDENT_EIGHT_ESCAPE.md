# Full neutral eight-wall escape channels: adversarial check

Disposition: BLOCK the proposed full-sector threshold reduction. The one-wall endpoint results remain valid in their stated sector, but the full finite-support neutral N=8 sector has transverse scattering channels below the paired-square energy. No canonical or shared files edited.

## Explicit lower channel

Take four flipped spins at the same longitudinal layer z0, at four widely separated transverse sites, against the uniform reference. Each occupied column has a single-site interval and hence two broken z bonds. The total is exactly N=8. The layer mask at z0 has four flips and every other layer mask is empty, so every layer has even parity.

A transverse native bond joining an occupied site to an empty site at z0 swaps the flip. Its matrix element is -1 for XX. For YY it is also -1, since the two spins are opposite and the native coefficient is -YY. The move preserves N=8 and layer parity. When the four particles are separated, K1 is therefore the sum of four independent nearest-neighbor square-lattice hopping operators, each with hopping -1 and bottom -4.

This gives a Weyl sequence at energy -16 in K1 units: place four slowly varying near-zero-momentum wavepackets in disjoint large transverse boxes, with box separations larger than their diameters. Symmetrize or use the corresponding occupation basis. Keep the same longitudinal layer. Collision/contact amplitudes vanish as the boxes separate; the individual hopping residuals tend to zero as their widths grow. Moves in layers z0+/-1 can preserve wall count only when two occupied columns are transverse neighbors, which is excluded on this support. A move in a wholly empty layer adds walls and is projected out. Thus there is no omitted off-subspace coupling of finite size in this Weyl construction. It proves inf spec_ess K1 <= -16, already far below -16/sqrt(3) approximately -9.2376.

If one fixes total transverse momentum zero, choose four near-zero momenta with zero sum, or formulate the same separated-packet construction in the relative-coordinate fiber. Common longitudinal translation can likewise be fibered without changing this leading channel. There is no layer-parity obstruction: the total four-particle configuration is neutral even though an individual isolated particle is not.

A second way to see the missed family is two far-longitudinally-separated layers with two flips each. Each layer is neutral and has N=4. Its two transverse particles have scattering bottom -8. Their combined N=8 channel again reaches -16. This example directly fits a 4+4 wall-count partition but neither four-wall cluster is a four-column one-wall interface.

## Classification gap

Finite support does imply at most four occupied columns when the total wall count is eight. It does NOT imply that every four-wall escape cluster has four distinct columns. A finite two-column droplet has two walls per column and is compatible with even layer parity. Repeated intervals and short intervals therefore create additional wall-count-preserving moves: a flip can remove two walls in one column while adding two in another. The earlier one-wall-sector invariance proof deliberately excluded this mechanism, because a one-wall column cannot lose two walls.

Longitudinal wall-count partitions alone do not classify transverse escape, nor the internal spectrum of each repeated-column cluster. Consequently the suggested bounds for four-interface graphs cannot establish the full N=8 threshold. This is an actual missing lower channel, not merely an absent estimate.

## Mixed-orientation gauge: valid narrower observation

For four distinct columns each carrying one wall in an isolated interface, write the orientation signs as sigma_i. Relative to common orientation, YY edge amplitudes acquire sigma_i sigma_j; XX amplitudes do not. A diagonal height gauge product_i zeta_i^(h_i), zeta_i=+/-1, changes both raise/lower and swap edge amplitudes by zeta_i zeta_j. Thus the desired gauge exists precisely when the prescribed bond-sign cocycle has trivial product on every graph cycle.

Any induced four-site nearest-neighbor square-grid graph is a forest or a square. Forests have no obstruction. On the square the cocycle flux is product_i sigma_i, so an even number of reversed orientations makes it trivial. In the N=8 setting with exactly four distinct occupied columns and a cluster flipping all four, the masks immediately before and after the interface lie within those four columns. Even layer parity makes the number initially reversed even, which supplies the required orientation parity. Without that restricted four-column argument, merely noting that the two masks are even would not by itself establish the parity of their intersection with an arbitrarily selected four-column cluster.

The height gauge can change common-translation character by product_i zeta_i. Hence it can shift the COM momentum by pi; equivalence of the union over all k is safe, while equivalence at the same k requires checking this character. The orientation gauge does not remove the repeated-wall/transverse channel above.

## Permitted conclusion

Retain the exact square one-wall endpoint band and its restricted-channel thresholds. Do not call the paired-square coefficient an isolated bound state below the essential spectrum of the full neutral finite-support N=8 operator on the basis of this classification. The explicit lower continuum does not by itself exclude an embedded eigenstate or a resonance, but either would require a new decoupling or radiation analysis. No global no-go for all endpoint physics is asserted.

## Extension: the paired-end energy itself lies in an escape continuum

PASS for this stronger essential-spectrum statement in the layer-neutral sector. Inspected /tmp/neutral_collision_path.py and its JSON. Its 28 moves each preserve N=8, use a transverse nearest-neighbor bond, preserve layer parity, and carry the correct nonzero native amplitude. The first eight moves shrink the flat 2x2 length-five prism to four single-site columns. The remaining swaps move them transversely. Small correction: the displayed final configuration still has the neighboring pair (6,0,0),(6,1,0), so that particular endpoint is not yet four mutually separated defects. Move the latter further in the positive y direction to separate it; further outward swaps can achieve arbitrary separation while preserving N=8. This does not affect the existence of the collision path.

For four separated transverse wavepackets the free dispersion is

 e=-2 sum_(i=1)^4 [cos(k_ix)+cos(k_iy)].

Choose k1=(theta,theta), k2=(-theta,-theta), k3=(theta,-theta), k4=(-theta,theta), with cos(theta)=1/sqrt(3). Their total momentum is zero and e=-16/sqrt(3). Smooth cutoffs of width M have hopping residual O(1/M). Placing their centers at pairwise distances much larger than M eliminates all short-range collision/growth contacts, including the channels that could extend neighboring singleton columns longitudinally. Taking the supports to infinity gives weak convergence to zero and hence a Weyl sequence at exactly the paired-end energy. This proves membership in the full layer-neutral N=8 essential spectrum, rather than merely a bound on its infimum. An exact zero-total-momentum fiber construction uses these carrier momenta in relative coordinates and cuts off only relative positions; it must not be described as an exact momentum eigenstate of four individually localized absolute-coordinate packets.

The finite path establishes graph connectivity, not a nonzero spectral-density matrix element at that energy. Signs and interfering paths can cancel a particular bright channel's on-shell radiation amplitude. Thus the argument does not determine a resonance width or rule out a symmetry/interference-protected embedded eigenstate.

## Global plane-X/Y symmetry projection

The infinite finite-support sector around one fixed polarized reference is not itself closed under whole-plane X/Y flips; they change infinitely many spins. A literal invariant-vector projection there is therefore not defined without enlarging the representation. Keep the direct infinite-volume theorem explicitly layer-neutral unless such an enlarged-space construction is stated.

There is a valid finite-torus implementation. Take all three periods even, with the torus much larger than the packet widths/separations. The X and Y plane generators commute because their intersections contain an even longitudinal number of spins. They preserve wall count and layer parity. Average the wavepacket over their joint +1 character. Nontrivial background-changing plane products carry its finite-defect support into disjoint background sectors, provided the torus is large enough; the same separation applies to the finite-range residual support. Hence normalized orbit averaging does not enlarge the residual norm. The only products stabilizing the reference configuration are diagonal relations, including the all-X/all-Y product proportional to global Z. For all-even periods its constant phase is +1, and the even number of flips makes its action +1 on this packet. Thus the + projection is nonzero rather than canceled by a stabilizer character.

This establishes symmetry-neutral finite-volume quasimodes with the same vanishing residual as the volumes grow, using disjoint background orbits. It is not automatically an essential-spectrum assertion in the single-reference infinite-volume Hilbert space. To make a globally plane-neutral infinite-volume statement, explicitly specify the orbit/direct-sum or limiting representation; otherwise the finite-torus neutral quasimode result and the infinite layer-neutral essential-spectrum result should be reported separately. No radiation claim follows from either projection.
