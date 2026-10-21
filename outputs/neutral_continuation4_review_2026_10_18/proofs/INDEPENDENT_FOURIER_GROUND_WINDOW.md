<!-- Owning original: PR9764; source SHA256 8f934ab11e07d998ae1d632819f05eb300881b6d60b7d46160e9e0d87e443530. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Fourier-source extension of the actual-ground finite-time comparison

Read `native/MICROSCOPIC_GROUND_WINDOW_PROOF.md` and `native/BULK_COM_SOURCE_PROOF.md`. The Fourier extension is valid with the qualifications below, assuming the already established normal-form gap, exact local remainder, and locality statements of the first proof. No new outgoing-pole transfer is implied.

## Correct observable and correlation

On the even periodic cube let p=2pi k/L, with p in a fixed real neighborhood of zero, and define

C_p=V^(-1/2) sum_(r,z) exp[ip(z+1)] Z_(r,z)Z_(r,z+2).

The midpoint convention and periodicity give C_p dagger=C_-p exactly. The positive-frequency ground correlation that creates the p-source is

F_p(t)=<C_-p(t) C_p> - <C_-p><C_p>.

Do not replace this by <C_p(t)C_p>: that generally has total momentum 2p and is a different quantity. In the interval-center basis the real vertex matrices in the separate COM derivation represent this same physical correlation; the half-integer centers only introduce a length-dependent fiber gauge. No additional physical boundary twist is required. A shift p by 2pi can change that fiber gauge while leaving C_p unchanged.

## Bounds are uniform in allowed real momenta

Every Fourier coefficient has modulus one, so ||C_p||<=sqrt(V) and the local normal-form truncation error remains C sqrt(V)lambda^41. The two-source norm products and elementary Duhamel error retain exactly the estimates in the zero-p proof. Actual-ground-density replacement costs O(lambda^17), source replacement O(lambda^29), and finite-box dynamics replacement O(lambda^13), with constants independent of the allowed p in the fixed interval.

Multiplying a local diagnostic by exp[ip(z+1)] does not alter its plane invariance or support. After localization, the operator identity P0 c_j^R(t)c_k P0=a_jk(t)P0 therefore still applies term by term. Multiplication by exp[-ip(z_j+1)]exp[ip(z_k+1)] and summation with 1/V cannot enlarge the absolute sum. Thus all densities on P0 have the same Fourier connected correlation, up to the same superpolynomial locality error. No assumption that an arbitrary actual ground density itself is translation invariant is needed. Its means must be subtracted separately; the comparison also controls them.

## Charge selection and high-energy suppression

Use the local raising component c_(j,+4), then sum with the physical Fourier weights. The first source sector is still N=4. Phase weights do not change transverse spin-flip counting, longitudinal plane parity, or the exclusion of another finite-support N=0 column configuration. On all-up, the N=4 correlation can be written

< [sum_j exp(ip(z_j+1)) c_(j,+4)] dagger(t)
   [sum_k exp(ip(z_k+1)) c_(k,+4)] >/V.

Both entries are sums of local finite-support operators; no nonlocal N=4 projector is inserted in the Lieb-Robinson argument.

For the same smooth compactly supported time window psi and T=c lambda^-4/Jz, the N>=6 contribution for omega/Jz in [7,9] remains bounded by C_r V(Jz T)^(-r). Taking r=5 gives O(lambda^8), uniformly in p. The Fourier phase on the spatial source does not change the positive spectral-measure bound used here, since C_-p is the adjoint of C_p.

## Periodic-to-infinite comparison

Allowed p=2pi k/L is essential to a clean periodic statement: phase weights agree across the torus seam. In a local coordinate lift, exp[ip(z+L)]=exp(ipz), so different periodic representatives have identical weights. Translation invariance of the all-up coefficient correlation reduces the double sum to a relative-coordinate sum with a unit-modulus phase. Local finite/infinite dynamics agree inside the light cone margin; the remaining relative-coordinate tails are bounded by their absolute Lieb-Robinson sum. Consequently the same choice of sufficiently large K_m in L approximately K_m lambda^-4 makes the discrepancy superpolynomially small, uniformly in allowed real p. The infinite response is evaluated at precisely that p, which may vary with lambda along the allowed mesh.

An arbitrary nonquantized p on a finite torus would need a different convention and seam analysis; it is unnecessary here. No uniform complex-p assertion follows from this argument: complex spatial weights have non-unit modulus and can spoil these volume estimates.

## Result and scope

For every actual microscopic ground density on the stated cube family, the window of F_p(t) equals the complete infinite compact-N=4 coefficient correlation window at the same p, plus O(lambda^8), uniformly for allowed real p in the fixed neighborhood and omega/Jz in [7,9]. The time scale is T=c lambda^-4/Jz. Thus the existing theorem does extend to an actual spatially modulated original diagnostic, not only its uniform sum.

This is the smooth windowed connected correlation defined above. Calling it a response should not silently replace it by an arbitrary causal retarded filter: multiplication by a step function changes Fourier-tail estimates and needs its own accounting. Real cosine/sine diagnostics can be assembled from C_p and C_-p without adding a Hamiltonian term, with the corresponding conjugate/cross correlations treated consistently.

The comparison retains the full coefficient correlation, including continua and fast fine structure. It neither turns a complex outgoing residue into a positive peak nor transfers an outgoing pole to H. Ground restriction, supplied microscopic Hamiltonian and readout, weak-coupling growing-volume regime, and units remain explicit. No detector calibration or cosmological state is selected by the Fourier extension.
