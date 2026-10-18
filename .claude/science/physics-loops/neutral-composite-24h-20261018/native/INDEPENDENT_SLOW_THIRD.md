# Focused check: exact third-order action from the length-three axial interval

Checked the canonical kernel and supplied JSON, and independently enumerated the six orders of transferring a filled length-three column into an empty adjacent column using only longitudinal wall counting.

## Six paths and signs

Let the unchanged column be a spectator. Transfer the three spins of the other column, one layer at a time, into a neighboring empty column. In layer order 0,1,2 the six permutations have intermediate excess energies:

* (0,1,2), (2,1,0): (4,4);
* (0,2,1), (2,0,1): (4,8);
* (1,0,2), (1,2,0): (8,4).

Every XX action has amplitude -1. Every YY action also has amplitude -1 here, because each layer initially contains one occupied and one empty spin and is acted on exactly once. The product is -1 for either transverse direction. All intermediate states lie outside E8; no folded contribution occurs for these paths. Thus

K3 = -2/16-4/32 = -1/4

for each physical whole-column nearest-neighbor move. The unchanged spectator column's position does not affect these longitudinal energy denominators. This agrees for targets of separation one, three, and (2,1), and for the Y-axis counterparts.

The script's canonical third-order weights are correct: two Q intermediates give 1/(q1 q2); one P intermediate contributes the appropriate -1/(2q^2) folded weight; two P intermediates contribute zero. Its energy routine excludes spurious longitudinal connections between distinct columns and restores the external-up end bonds.

## Completeness of the length-three row

A different-column target must share exactly one original column, since a disjoint target would differ in more than six spins. The Hamming lower bound also requires the target length ell'<=3. If ell'<3, even maximal overlap leaves six changed spins, saturating the three-bond budget. Every bond would then have to flip two distinct changed sites without any auxiliary intermediate spin. But a removed layer has only the original axial-distance-two endpoints changed, and no transverse nearest-neighbor bond connects them. It requires at least two bonds with an auxiliary flip, contradicting saturation. Misaligned intervals only increase the Hamming distance. Hence shortening to ell'=1 or 2 is impossible at this order.

If ell'=3, the intervals must coincide to keep the Hamming distance at six. The changed sites are the old and new column on each of three layers. Saturation requires one direct transverse bond per layer, so the new column must be a nearest neighbor of the old one. The three edges are then unique and their six orderings exhaust all paths. A target coinciding with the spectator is not a valid two-column E8 configuration and is excluded.

All same-column-pair matrix elements vanish by the odd-order checkerboard selection rule, since an axial-distance-two pair has U=+ at every length. Different-column transitions from ell>=4 are excluded by the general support bound. Therefore the listed moves are the complete E8 K3 action from the length-three axial state, not merely examples of nonzero entries.

## Momentum and scalar normalization

At zero total transverse momentum, moving either of the two columns supplies the same relative-coordinate hop. The physical -1/4 contributions add to relative hopping -1/2. The length-three scalar combinations are

A3=(|axial X separation two,3>-|axial Y separation two,3>)/sqrt(2),
E3=(|nearest X pair,3>-|nearest Y pair,3>)/sqrt(2).

There are no cross-orientation nearest-pair targets from a single column step, so <E3|K3|A3>=-1/2. The remaining separation-three and mixed-separation targets are the odd-color frozen length-three sector, with the same relative hopping coefficient and the inherited scalar signs.

This determines the previously missing short-boundary third-order vertex. It does not by itself compute its continued fast self-energy, fourth-order virtual correction, dressed original readout, or a native pole. Those remain separate from the exact local coefficient and support result.
