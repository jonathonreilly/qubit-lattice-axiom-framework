# Independent extra Y-plane sector reduction check

The actual native reduction from 2^22 to 2^20 is correct. It retains all physical qubits and selects two additional conserved binary labels rather than projecting out a physical degree of freedom or adding a Hamiltonian term.

## Generators and completeness

Each adjacent Y-plane pair contains 18 Y factors. In the action convention (flip,phase,coefficient), a product of 18 Ys has coefficient i^18=−1 and identical flip/phase masks. The input −1 sign is therefore necessary and correct. The generators commute with H, C_center, the original Z-plane generators, the original adjacent X-plane pairs, and each other.

On the open 3^3 cube the full plane Pauli-vector span has rank eight. The chosen three Z planes, two X-plane pairs, and two Y-plane pairs are seven independent commuting generators. Equivalently, inside the old five-generator sector the two reduced Y-pair flip masks are independent. Their four-element flip group has a free action on computational bit strings, so each orbit has four distinct members. All four character sectors are nonempty and have equal dimension 2^22/4=2^20. Their direct sum is the complete old sector. This is a stronger symmetry decomposition, not an assumption that any selected character sector contains the global ground state.

## Signed orbit formula

Write a Pauli term as T=(f,z,c), acting on |r> by c(−1)^(z dot r)|r xor f>. Multiplication is

(f,z,c)(g,w,d)=(f xor g,z xor w,c d (−1)^(z dot g)),

which agrees with the helper. For two commuting involutions, the four group elements have the product characters used by the code. Choosing two pivot coordinates whose group flip patterns cover all four possibilities makes the zero-pivot section a unique representative of every orbit.

The unnormalized basis vector is U_r=sum_G character(G) G|r>. Its norm is two because the four computational supports are distinct; the common missing factor 1/2 cancels in all intertwining checks and reduced matrix elements. Different representatives have disjoint supports. Different character choices on a common orbit are orthogonal by character orthogonality.

For T commuting with both generators, choose G=(g,w,d) so cf=f xor g has zero pivot bits. The resulting reduced flip is compress(cf), the reduced phase is compress(z xor w), and the general coefficient from direct orbit amplitudes is

c d character(G) (−1)^(z dot g).

The supplied reducer instead writes its final exponent as w dot cf. This is equivalent for the ACTUAL generators: commutation gives z dot g=w dot f, and their real coefficients ±1 and involution property imply w dot g=0 modulo two. Thus w dot cf=w dot f=z dot g. The product generator also satisfies this property. The actual numerical stabilizers both have coefficient −1 and even flip/phase overlap.

This simplified formula should not be advertised for arbitrary complex Pauli involutions without a restriction: a generator with imaginary coefficient and odd w dot g would not satisfy the simplification. Either explicitly require real ±1 stabilizers with even flip/phase pairing, or use the general z dot g exponent when generalizing. Current native results are unaffected. Likewise, caller signs must be ±1; the present callers satisfy this.

## Independent checks

Inspected `/private/tmp/neutral_extra_sector.py`, the control, and its saved stabilizers. An additional independent script `/private/tmp/native-extra-sector-independent-check.py` lifts reduced vectors through BOTH reductions into explicit 16-term signed orbits of full physical 27-bit strings. Across all four extra sign choices and ten deterministic representatives each, it checks the eigenvalues of both original physical 18-Y operators and all three physical C_center pair intertwiners. All 200 exact integer-dictionary checks pass. This explicitly checks the physical Y sign and central observable rather than merely repeating the 22-bit native-bond control.

The existing 10,800 native-bond intertwining checks support the Hamiltonian map; the independent lifted tests and algebra above support signs and completeness without building a dense 2^27 matrix. No big eigenproblem was rerun and no frozen repository files were edited.

## Meaning of the low-level labels

If the chosen ground eigenvector is in extra sector (++), C_center cannot connect it to exact eigenstates in any of (+−), (−+), or (−−), since C commutes with both generators. This provides a conserved-label explanation of the low dark lines, rather than evidence that their energy differences measure a scalar excitation gap. Degenerate numerical eigenvectors may be arbitrary mixtures of the (+−) and (−+) states; a mixed basis remains dark because the entire subspace is orthogonal to (++). To assert each separate label numerically, diagonalize the commuting generators within the degenerate subspace or check their spectral projectors. No global-ground certification, absence of other low-weight modes, or bulk particle conclusion follows from these label checks.

### Follow-up correction

After the scoped review, root reports replacing the simplified final exponent by the general `z dot g` formula in `/private/tmp/neutral_extra_sector.py`; all 10,800 native intertwining controls still pass. This removes the unnecessary real-stabilizer limitation in that phase step. The proof above directly supports the corrected exponent. The earlier caution describes the version inspected, not an outstanding error in the reported corrected implementation. The planned deeper response run was not inspected or executed as part of this check.
