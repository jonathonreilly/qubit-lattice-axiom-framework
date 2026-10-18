# Independent leading-XY composite readout check

Disposition: PASS for section3's finite leading-effective-theory one-pair formulas, reflection selection and stated interpretation. No pack edits or native full-H inference. This is not a formal audit.

## Boundary condition and normalization

The spin Hamiltonian has matrix element -1 between neighboring unlike bits, hence equals -(1/2)sum(XX+YY) and has Jordan–Wigner hopping -1. For L divisible by4 at half filling, fermion number L/2 is even and the periodic spin chain maps to antiperiodic fermions k=2pi(n+1/2)/L. There are no Fermi-level zero modes in this sequence. The occupied symmetric Fermi sea has n=1/2, g1=<c†_j c_(j+1)>=1/[L sin(pi/L)], and g2=0. These statements are specific to this state/boundary sequence, not arbitrary finite XX sectors.

The source uses L^-1/2 Fourier normalization and Pauli density 1-2n rather than number density. Each accessible particle-hole density amplitude has magnitude2/sqrt(L), giving total4m/L for m=1,2. The script's .75 spin-flip coefficient is precisely (3/8)XY because XY has flip amplitude2. No extra factor of two is missing.

## Wick projection

Next-neighbor XY includes its Jordan–Wigner intermediate-site parity string. Wick expansion about this Fermi sea cancels its bare next-neighbor bilinear against the n=1/2 contraction. The g2 contraction is zero. The two remaining g1 contractions give exactly2g1 times the sum of the adjacent XY bonds in the one-particle/one-hole projection. The leftover normal-ordered quartic term creates two particle-hole pairs from this Slater ground state. Thus

Pi_1pair C2(q)|FS>=(3/8)(1+2g1) Pi_1pair[XY_(j-1,j)+XY_(j,j+1)](q)|FS>.

This is a projected source-vector identity with respect to the specified sea, not an operator identity replacing the full composite. The elastic constant is irrelevant for the nonzero Fourier momenta; the script also explicitly centers sources.

For p=h+q, the adjacent-bond sum has matrix element4(cos p+cos h)/sqrt(L)=8cos(q/2)cos(h+q/2)/sqrt(L). At q=2pi/L the single allowed crossing has midpoint pi/2 and therefore zero composite amplitude. At q=4pi/L the two crossings have midpoints pi/2±pi/L; each composite amplitude has magnitude3(1+2g1)cos(2pi/L)sin(pi/L)/sqrt(L). Squaring and summing gives the stated18/L coefficient. Their energy difference is4t sin(2pi/L)cos(pi/L); q1's density gap is4t sin(pi/L). Fixed profile index yields composite one-pair weight O(L^-3) and density O(L^-1).

## Independent direct Slater control

Built normalized Slater determinants in the spin occupation basis at L8 and L12 from the antiperiodic occupied orbitals. Constructed the physical spin sources directly and every single particle-hole determinant, without using the root spin eigensolver or Lanczos routine. Complete one-pair projection verifies the Wick identity with maximum amplitude error9.1e-16. Composite weights are:

L8 q1:4.0e-30 (zero), q2:.4503243662879293;
L12 q1:5.3e-30 (zero), q2:.2036678522846994.

These agree with the analytic expression within9e-16. Density weights are .5,1 for L8 and1/3,2/3 for L12. The independent script and output are /private/tmp/neutral-xy-independent.py and .json. No expensive L20 replay was necessary.

## Reflection and coincident energies

Global spin complement leaves the XY Hamiltonian and C2 even while sending density odd. The ground state is a reflection eigenstate. The two source vectors therefore have opposite relative reflection parity and zero cross spectral response at every time/frequency. The independent determinant control verifies both vector parities and cross overlap below3e-17. Equal excitation energies can support orthogonal parity sectors or distinct vectors within a degenerate subspace; they do not identify equal transition vertices or one common linear bosonic readout. Conversely this distinction does not prove the even channel gapped or exclude a common low-energy continuum theory with different composite operators.

The full C2 includes quartic weight. Root's Lanczos low-node grouping is numerical support for the selected finite sizes, not a general proof that every composite spectral contribution is exhausted by the one-pair formula. q1 has zero ONE-PAIR weight, not zero total response. The text preserves this distinction and explicitly restricts the calculation to the leading periodic effective XY model. Restore original-observable amplitude lambda² and weight lambda⁴; native higher-order corrections, state selection and a physical detector mapping remain uncontrolled here. Section2's bosonization/infrared route was outside this focused section3 check and is not independently certified by this report.

## SHA256 snapshot

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/DERIVED_INFRARED_ROUTE.md`: `f9267a7b6c5fc8183bf563cacfc86aa0e62e1e6cb87aec633fbaaeabe9348aa8`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_xy_readout.py`: `e28e24dea0643357f05110ff3a9f01b919a01d678b82c0debb7f0761236588ee`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_xy_readout.json`: `d18e61d8579c9a9f48deb95a2269dcea997f9ffa653b8bdd3f9f9d65982e3b5c`
- `/private/tmp/neutral-xy-independent.py`: `ada31661841802dbc6f52895c3410f5c6a4a19fcf1d85286650fa1e56907374a`
- `/private/tmp/neutral-xy-independent.json`: `3f2a47a0cea0f96bfbeaf04b6794be8dedc3e339468c464bc6b2a655eda170de`

## Follow-up: two-pair coefficient and continuum matching

Disposition: PASS for the appended two-pair formula and smooth continuum coefficients, with composite products interpreted as normal-ordered continuum operators. The newly added external-theorem/LSM section is outside this requested check.

Independently reconstructed the two specified particle-hole Slater determinants and contracted the full spin composite source, without Lanczos or using the root spectral nodes. At L8 both amplitude magnitudes are .3200825214724774, total weight .20490564110435794; at L12 both are .2332531754730552, total weight .1088140877365278. They agree with the antisymmetrized vertex within5e-16. The overall minus sign differs in this determinant column-order convention exactly as allowed; squared weights agree. Control files are /private/tmp/neutral-xy-twopair-independent.py and .json.

The quartic operator is -(3/2)(:c†_(j-1)c†_j c_j c_(j+1):+h.c.). Antisymmetrizing both creation and annihilation momenta yields the product of exponential differences in the note; adding the Hermitian conjugate gives the real-part factor. The Fourier normalization supplies L^-3/2. For the two listed q1 states each factor product tends4, so each squared amplitude tends144/L³ and their sum tends288/L³. The pair energy is the sum of one right q2 crossing and one left q1 crossing, giving4t[sin(pi/L)+sin(2pi/L)cos(pi/L)]. These are distinct pair states; no coherent addition of their amplitudes should precede squaring.

The continuum cross coefficient and SIGN can be checked directly, without inferring it only from squared weights. At k_F=pi/2, retain smooth fields and use c_(j-1)†~sqrt(a)(i R†-i L†), c_j†~sqrt(a)(R†+L†), c_j~sqrt(a)(R+L), c_(j+1)~sqrt(a)(iR-iL). Their normal-ordered product is4a² R†L†RL=-4a² rho_R rho_L. Adding its conjugate and multiplying by-3/2 gives +12a² :rho_R rho_L:. Derivative and oscillating pieces have been omitted only in this smooth leading matching.

For the same-chirality coefficient, the one-pair adjacent-bond factor tends(3/8)(1+2/pi). Define local lattice energy h_j=-(t/4)[XY_(j-1,j)+XY_(j,j+1)]. Then the projected smooth composite is -(3/(2t))(1+2/pi) h_j. Since h_j approaches a*pi*v(:rho_R²:+:rho_L²:) and v=2ta, this gives -(3pi+6)a²(:rho_R²:+:rho_L²:). Combining the two parts reproduces the proposed expression with the correct relative sign. Normal ordering of the squared-density/composite products is necessary; a product of densities at the same point is otherwise undefined without a subtraction convention. The note's normal-ordered chiral-current convention should be read to include these products.

The result is a dimension-two readout matching in the leading free periodic effective theory, not a new Hamiltonian coupling, a full native interacting operator theorem, or a physical detector vertex. It is consistent with an even two-boson/stress-energy-like channel and does not turn coincident linear dispersions into a common linear odd-field readout. The full lattice C2 retains high-energy spectral weight, and this continuum expression only describes its smooth low-energy part. Original-observable amplitude still carries lambda² and weights lambda⁴; higher native dressing remains untested by this matching.

Follow-up hashes:

- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/DERIVED_INFRARED_ROUTE.md`: `3b5ae053e53074d91e129feffdb025e255144d5519b4557267f54679985342b3`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_xy_readout.py`: `3be0418e459ec56569621fad2730203333f0989aeb7d9bd71547a59bb633f366`
- `/private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_xy_readout.json`: `643d18d91599a29c0be02fca4f61a57294bc3b18f4731fec7c998c1a21644a11`
- `/private/tmp/neutral-xy-twopair-independent.py`: `68a545fe01e0f3fda6b1ca3e953bde322ea925d0a79e12047d694230baafbb1d`
- `/private/tmp/neutral-xy-twopair-independent.json`: `740102047e9cf9f2ed044250fbd3381af68a2ce67e212a7cbfd0c358971da490`
