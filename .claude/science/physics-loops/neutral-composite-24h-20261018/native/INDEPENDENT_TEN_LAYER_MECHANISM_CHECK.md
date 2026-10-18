# Focused check: thicker-slab boundary-bound four-flux route

The proposed mechanism survives the diagonal-classification and minimal-flip checks below. This is a fixed-height, fixed finite transverse-size coefficient argument, with a subsequent large-size interpretation requiring its own control. It is not yet a proof of a native bulk particle or of its readout weight.

## Eighth-order diagonal terms

For a diagonal N=0 return, the modulo-two transverse edge graph at every longitudinal layer is Eulerian. At total order eight its nonempty parts can be:

1. A four-edge plaquette with four further repeated insertions, producing only the same plaquette polynomial.
2. A six-edge rectangle with a doubled edge, producing its adjacent-plaquette product.
3. A simple eight-cycle: perimeter of a straight three-plaquette strip, an L-shaped triomino, or a 2 by 2 plaquette square.
4. Two four-cycles, possibly in different longitudinal layers. Their product can survive in a connected energy coefficient only when their physical supports interact, which here requires overlapping column support (and appropriate longitudinal contact).

Repeated-edge words with empty modulo-two graph are scalar. This classification includes the folded corrections: they can renormalize lower support structures or cancel disconnected products. In particular two disjoint four-cycles on disjoint column sets factorize under H0 and give no connected cross energy coefficient after folds. They cannot create an independent distance-two plaquette-pair interaction at order eight.

Every structure in items 1, 2 and 4 has plaquette-anchor span at most one in either transverse coordinate, except for disconnected products whose coefficients vanish. The L-triomino and 2 by 2 square also have anchor span one in both directions. Only the straight triomino has anchor span two along one direction.

For four bad plaquettes at the corners of a thin (a,1) rectangle, with a even and a>=2, a translated invariant of anchor span at most one cannot touch both separated short ends. Its summed contribution is consequently independent of a. The straight three-plaquette invariant does distinguish a=2 from a>=4. The same holds after rotation. Thus the proposed distinguishing term is exhaustive at order eight, although numerous additional terms do alter the common thin-state energy.

This assumes transverse periods large enough to exclude short wrapping cycles and avoids rectangles whose ends interact around the torus. Area-even/appropriate plane-sector restrictions are needed to exclude the odd-area (1,1) configuration when asserting that (2,1)/(1,2) are the shortest allowed thin states.

## Coefficient and defect depth

I replayed the exact simple-loop path sum for the 1 by 3 perimeter. All 40320 orderings give -9/262144 per longitudinal layer. Its four-corner Pauli polynomial equals the product of its three constituent plaquettes. Therefore c8=9L/262144 in the term -J c8 lambda^8 sum(straight triple P).

For each of the two rows of bad plaquettes in a thin a=2 configuration, one triple window contains both bad plaquettes. Compared with separated endpoints, the number of odd-parity triple windows decreases by two per row, hence four in total. Since each odd triple costs 2J c8 lambda^8, the shortest rectangle gains -8J c8 lambda^8. This establishes v=8c8>0 with the stated sign.

At L=8, gamma8=429/262144 and v/(2gamma8)=576/858, approximately 0.671329. Thus this *leading thin-arm coefficient model* has no boundary bound state from that defect alone. Higher-order small corrections cannot change this fixed strict inequality in the weak-coupling limit, but other sectors must still be kept distinct.

## Why height ten changes the ordering

For L=10 the first background-changing native term is order ten, an adjacent-column pair flip. Any two-column jump has to flip twenty spins, and a minimal ten-insertion jump can join only adjacent columns. There is no lower-order shape-preserving or translating off-diagonal term. Four-column jumps require at least twenty insertions, and a two-column jump between nonadjacent columns requires additional transverse path length in every layer. Diagonal terms carry no momentum dispersion themselves.

The order-eight defect is therefore parametrically deeper than the order-ten thin-arm hopping. At fixed longitudinal height ten it binds a state predominantly at the a=2 endpoint. The endpoint-to-a=4 hopping amplitude in a transverse COM fiber is -2J gamma10 lambda^10 cos(q_parallel). Second-order elimination across the order-eight defect gives the leading dispersive shift

-4J gamma10^2 lambda^12 cos^2(q_parallel)/v.

Its curvature at zero momentum is positive. Uncomputed order-ten and higher diagonal terms can change the common energy and higher corrections to the denominator, but cannot remove this leading lambda^12 momentum dependence. This formula is a dispersive term, not a complete energy expansion through order twelve: missing diagonal shifts at orders ten and twelve must not be silently set to zero.

The shape-changing path through the nonthin (2,2) hub costs order lambda^6, so two order-ten hoppings give orientation mixing at order lambda^14. Its off-diagonal sign is negative (two negative hopping entries divided by a negative excitation denominator), selecting the symmetric C4 combination at zero momentum. Paths through the vacuum cost order lambda^4 and first contribute at order lambda^16, later than this hub path. There is no direct native lower-order matrix element connecting the two endpoint orientations by the physical-spin count.

The orientation splitting is order lambda^14 whereas the anisotropic diagonal dispersion is order lambda^12 q^2. Hence q much smaller than lambda is the appropriate regime in which the symmetric branch has leading isotropic curvature, with the curvature averaging the two orientation branches. Outside that regime one cannot label the same approximation an isotropic mode.

## Remaining qualifications

The conclusions rely on keeping the proper plane sector (or proving actual ground selection at each fixed transverse size), on excluding periodic aliases, and on analytic reductions to sufficient order. A leading boundary state in this coefficient problem does not by itself prove an infinite-volume isolated native pole, uniform-in-size stability or original-C visibility. The absolute excitation center needs the common diagonal renormalizations and vacuum subtraction. Those omissions do not invalidate the leading sign of the dispersive mechanism, but they prevent treating the displayed terms as the full native spectrum.
