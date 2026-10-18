# Independent open-cube CSS sector check

Inspected `native/compass_sector_basis.py` and independently checked its physical bit actions on the odd 3x3x3 geometry. The stabilizer construction and affine sign reduction are correct for the stated Hamiltonian and central composite.

## Stabilizers and odd geometry

Let Z_z be the product of physical Z over the plane of constant z, and X_x the product of physical X over the plane of constant x. Each individual plane operator commutes with every native bond: a bond of another Pauli type lies within a plane and meets it in either zero or two sites; a bond normal to the plane uses its own Pauli type and commutes even at one site.

For a 3x3x3 cube, X_x and Z_z intersect in three sites and therefore anticommute. They cannot both be imposed as independent commuting stabilizers. The chosen adjacent products X_x X_(x+1), however, meet each Z plane in six sites and commute. This is exactly the needed odd-geometry distinction; the code handles it correctly.

The three disjoint Z-plane masks are independent. The two adjacent X-plane-pair masks are independent. Pure-X and pure-Z binary masks cannot cancel one another in a product except when both separately vanish, so the total commuting stabilizer rank is five. There is no product equal to minus identity. Every one of the 32 sign sectors is consequently nonempty and has dimension 2^(27−5)=2^22. The analogous 2x2x2 construction has rank three and eight sectors of dimension 32. It need not exhaust all commuting symmetries available on an even geometry to be a valid decomposition.

The central C consists of distance-two same-axis Pauli pairs. The same zero/two-intersection argument proves that each term commutes with every chosen stabilizer. In particular, endpoint separation along z does not obstruct Z-plane commutation because that pair uses Z. Thus C_center preserves each sector; this does not identify its spectrum or create a scalar mode.

## Affine/sign reduction

RREF on the X masks supplies independent generators g with their transformed character bits eta, so orbit amplitudes are (−1)^(sum eta). Setting the X-pivot bits of the representative to zero fixes exactly one point per X orbit: each pivot is toggled by one RREF generator, and distinct pivot generators do not toggle each other's pivots. Because the X masks commute with the Z masks, this gauge fixing preserves every Z-plane affine constraint.

The second RREF solves the Z-sign constraints together with this gauge. The code's offset is the solution with all free bits zero. Its columns give the homogeneous solution produced by toggling each free bit. Thus a reduced bit string j represents b(j)=offset XOR sum_j column_j.

For a term T|b>=c(−1)^(phase dot b)|b XOR flip>, commutation with the Z stabilizers ensures its flip preserves the Z constraints; commutation with the X stabilizers makes its phase constant on each X orbit. Canonicalizing the flip gives both its representative displacement and the character sign from removed X generators. The reduced phase is phase dot each affine column, and the offset contributes (−1)^(phase dot offset). These are precisely the code's reduced flip, phase, and coefficient. No missing phase from reordering Y occurs: each native −YY term has coefficient +1 in the computational X-flip/Z-phase convention, whereas −XX and −ZZ have coefficient −1.

## Independent exact control

`/private/tmp/native-sector-independent-check.py` uses the supplied basis parameters but independently applies the original physical flips and phases to explicit signed bit-string orbits. It tests all 32 odd-cube sign sectors and five deterministic random representatives in each. For each representative it verifies all five ORIGINAL stabilizer eigenvalues, all 54 native bond intertwiners, and the three central-C intertwiners. All 9,120 term checks pass exactly as integer dictionaries; no floating-point tolerance is involved and no 2^27 dense matrix is needed. This specifically exercises nonzero affine offsets, negative X characters, odd-plane intersections, and the central observable rather than relying only on the even 2x2x2 spectrum control.

## Benchmark scope

The exact reduction supports a stationary eigenbenchmark within a declared sector. The all-plus sector is not thereby known to contain a global ground state. A lowest eigenvalue found there is an upper bound on the unrestricted ground energy, unless a separate comparison or sector-equivalence proof is supplied. Other global symmetries can relate some sectors but do not justify silently identifying all of them. Nor does a sector-preserving C guarantee a sharp bulk excitation or remove finite-open-boundary effects.
