# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Independent full logical quotient check

The quotient Hamiltonian and source normalization pass independent full-logical-space intertwining controls at3x3 and3x4. These are representation tests only; they do not validate native coefficient expansions on such short transverse periods. No root files were edited.

Independent control: /private/tmp/neutral-four-column-independent.py
Results: /private/tmp/neutral-four-column-independent.json

## Dimension and normalized isometry

For a periodic nx by ny logical-spin array, products of X along every row and column generate rank nx+ny-1: the product of all rows equals the product of all columns, giving the single relation. The action on computational configurations is free. The joint-plus sector therefore has dimension

2^(nx*ny-(nx+ny-1))=2^((nx-1)(ny-1)).

The plaquette Z products obey product along every plaquette row and column equal+1. The (nx-1)(ny-1) interior plaquettes are independent, and the last row/column are their prescribed products. Conversely, two physical spin configurations with identical plaquette bits differ by a row-plus-column binary pattern, hence lie in the same subsystem-X orbit. Thus plaquette labels identify the plus-sector orbit basis completely.

I constructed W directly from every full computational spin configuration: W_(spin,label)=1/sqrt(orbit_size) when its physically computed plaquettes give that label, zero otherwise. This is a normalized uniform orbit projection, not a gauge-fixed representative without normalization. W†W=I and every full row/column X acts as+1 on W.

## Diagonal, flip masks and multiplicities

The code's pm(x,y) correctly reads an independent plaquette bit for an interior location, a parity product for a last-row/column location, and the product of all free bits at the final corner. Its XOR-fold parity calculation therefore gives the physical eigenvalue of every plaquette. The diagonal -P is exactly -sum_p P_p.

Flipping one logical spin toggles its four neighboring plaquettes. Restricting that mask to independent plaquettes gives site(x,y). An XX edge toggles the XOR of its two site masks, so canceled shared plaquettes are handled correctly. The code includes one edge in each positive coordinate direction per site, giving2 nx ny physical edges for the tested periods>=3.

Different physical edges can produce the same reduced mask. Their multiplicities must be retained; the code does so by looping through the full mask array. For3x3,18 distinct physical edges reduce to nine masks each with multiplicity two. For3x4,24 distinct physical edges reduce to eighteen masks with multiplicities one or two. These are genuine quotient coalescences, not physical-edge double counting. Deduplicating masks without adding their coefficients would be wrong.

## Full-space controls

I built the full logical Hamiltonian independently from physical spin-bit plaquettes and nearest-neighbor XX flips, then compared H_full W with W H_reduced at t/K=8/9. I also checked the full source O=sum P/sqrt(nx*ny) against its reduced diagonal representative.

3x3: full dimension512, quotient16, orbit size32;
intertwining maximum error0;
Gram error1.11e-16;
source intertwining error0;
all row/column symmetry errors0.

3x4: full dimension4096, quotient64, orbit size64;
intertwining maximum error0;
Gram, source and symmetry errors0.

These intertwining identities test the complete matrices, stronger than checking a few eigenvalues. The parent run's centered source f=(P-<P>)g/sqrt(N) therefore has the stated normalization, with norm squared Var(P)/N. Subsequent Lanczos weights are for this normalized uniform plaquette source, not for one plaquette or an additional physical source amplitude.

## Scope

The quotient fixes the plus subsystem-flip sector; it is not automatically a survey of all exact symmetry sectors or a global ground-state certificate. This control validates the specified FULL leading logical coefficient Hamiltonian inside that sector, with no four-defect truncation. It does not establish the native t/K coefficient, omitted higher-order interactions, large-grid convergence, physical observability or a scalar pole. The3x3 and3x4 controls must remain separate from the native coefficient calculations requiring transverse periods greater than four.
