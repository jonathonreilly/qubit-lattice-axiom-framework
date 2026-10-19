# Tetramer leading mobility: focused check

Disposition: PASS for the leading Ax/Ay hopping after explicitly including the disconnected two-winding cancellation below. The restricted Q8/perimeter-24 script alone is insufficient to establish native completeness. Native diagonal completeness and the positive order-ten A/B split remain inherited inputs. No repo edits or formal audit.

## Independent enumeration

I replayed the root script and independently enumerated minimal edge-XOR words between translated/oriented minimum column sets. The independent method pairs the symmetric-difference endpoints by minimum Manhattan matchings, enumerates shortest paths for each pair and every edge ordering, and classifies intermediate states by Q, perimeter and the supplied D8 functional. It does not use the root's restricted next-state function. Scratch: /tmp/neutral_tetramer_motion_reviewer.py and .json.

Within Q8/perimeter24, Ax has exactly two first neighbors, each gap v lambda^8, with v=5832 L/21233664=9L/32768. At depth two the only minimum hit is the original Ax. At depth four the only nontrivial minimum hits are translations by ±2x. Each has positive denominator-product magnitude 1/5832^3 in the integer energy units. Each path contains four negative winding amplitudes and three negative resolvents, hence hopping

 -J gamma^4/v^3 lambda^16.

The resulting Ax leading dispersion contribution is -2J gamma^4/v^3 lambda^16 cos(2qx), with Ay rotated. There is no transverse or orientation-changing contribution at this order from the all-gap-eight paths. The q-independent diagonal corrections, including lower-order self-energies, must be retained separately. The script's return amplitudes should not be mistaken for complete canonical diagonal coefficients without folded terms.

## Necessary omitted-path cancellation

Outside the restricted graph there are two-winding paths at formal order lambda^(20-4)=lambda^16. Ax can translate by ±4x by deleting one adjacent dimer and creating another; four translated Bx targets likewise share one dimer with Ax. These are genuine candidate matrix elements and cannot be excluded by the four-winding graph.

For each such target the two disjoint edge operations commute. Removing first gives an intermediate Q4 state, adding first a Q12 state. Their leading energies relative to Q8 are equal and opposite, ±J Delta lambda^4, and their product numerators agree. The two leading resolvents therefore cancel exactly. This is the elementary linked-cluster cancellation, not a claim that these paths are absent. Corrections to their denominators or vertices start at later even order, so they cannot restore an order-sixteen term. This also rules out a leading Ax→Bx off-diagonal from those two-winding paths.

The finite independent enumeration finds these candidates explicitly. Translations arbitrarily far away can also be reached by four disjoint remove/create edge operations; they have smaller inverse-denominator enhancement and/or disconnected cancellation, not additional leading mobility. Thus a finite target search by itself is not a general locality proof. At order sixteen the classification by winding count and denominator orders is the useful exhaustive argument.

## Native order counting and B denominators

Every genuine change of aligned columns at height ten requires at least ten physical transverse edge uses per elementary adjacent-column winding. A composite higher-word vertex with the same multi-edge flip costs at least the corresponding microscopic count, but has fewer small denominators than fully separated winding vertices. Replacing a leading winding by its higher even-order correction also raises the order. Consequently such vertices do not improve on the four-winding/three-gap-eight order sixteen. Excursions changing Q or leading perimeter have gaps of orders lambda^4 or lambda^6, giving less enhancement, except the two-winding case just canceled explicitly.

Treat A and B together as the retained D8 minimum space before eliminating B. The two-winding A/B candidate cancels at sixteen; the all-gap-eight four-winding computation has no A/B hit. Thus B's order-lambda^10 splitting cannot produce an earlier Ax mobility: A/B mixing starts later than sixteen, and eliminating B gives a still later correction. One must not assign an inverse lambda^10 denominator to a B state while assuming an unproved earlier coupling into it. The positive nonzero split is required for that final elimination.

The result is leading one-dimensional coefficient dispersion, not exact one-dimensional motion, zero transverse mobility to all orders, or a complete actual-H isolated-band transfer. Higher orders may generate transverse motion and A/B mixing. A publication should state the disconnected two-winding cancellation and the higher-word power count explicitly alongside the restricted graph calculation.

## SHA-256

- `/tmp/neutral_tetramer_motion.py`: `263dde46632a26b6465000309637006f98d3323284dfc96275dcea43dec79da7`
- `/tmp/neutral_tetramer_motion_reviewer.py`: `2b4451e8793188d14d1648bf2d956709132abe866e4f54d23a51e71efd86bd63`
- `/tmp/neutral_tetramer_motion_reviewer.json`: `65f24f87efd2862c2d2cfa1dcf8ea923051e122c6520caeecf1d6e15d669f7b0`
