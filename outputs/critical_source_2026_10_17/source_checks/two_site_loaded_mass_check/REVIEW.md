# Check of the energy-weighted two-site mass interface

Disposition: supported as a conditional full-fiber inverse and prepared-seed mass interface, with no required correction. The energy weighting removes the logarithmic integration loss in this particular resolvent difference. Actual applicability to a newly installed emitter remains conditional on the same-plane boundary-kernel envelope and complete matching regularity; this review supplies neither that installation check nor a complete output/runtime theorem.

Target: `two_site_loaded_mass/PROPOSAL.md`, SHA256 `f2b34e07c37ee4a72b1a0301eb6f364431c71055a0a1a5b2ade90159dee9c39f`.

## Exposure and source coverage

I read the complete new root-authored proposal and the complete scalar source `two_site_product_source/PROPOSAL.md`, SHA256 `8892741e6a14bca4565aef77d5913a3afca43a850c202c43dc2afb8ed3d9e303`, concentrating on the exact spectral density, normalization and cubic tail used here. That scalar source's separate review was pending when this task was assigned; no completed-review status is inferred. I just checked the inverse source `33b4f11058bd8953f6ea1cc03e85fde8f884f2ac2cf2eadd22f509f0b390ca4d`, with review `b402f4203cb283cbd2e44fa39f73df77b566051fb189a4f219be1ed6b9df29b8`, and reuse its unaffected ordered algebra.

I did not author this mass interface. I have authored or checked shared source/recovery ancestors and received root's proposed energy-weighted mechanism. This is a distinct source-exposed calculation check, not blind review or original calibration recertification. The candidate unloaded endpoint pin `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3` is context for an explicitly unverified changed-attachment premise here, not a certified extension of its emitter domain.

Only this review was written. No scientific execution, numerical inverse, quadrature, parameter sweep, Git/canonical edit, publication, checkpoint, prompt, model or delegation change occurred.

## Weighted inverse on all channels

The domain implies r<10^-8/.0027<4×10^-6, so s=1−2r is positive and well inside the inverse lemma's domain. On the selected projection, |q0(δ)|≥sqrt(s)(δ²+λ²) follows from the previously checked exact polynomial. On each complement, |x|≥.185>2j, so the physical root is real and |m_j(x)|≤1/j. Hence q0(x)≥x²−2λ|x|−λ². At the smallest allowed modulus and largest λ, this is greater than 1/30, while |x|/q0(x)<6. Both rational majorants decrease with |x| on this range.

Since δ²+λ²≤(2.4×10^-8)²+(10^-8)²=6.76×10^-16, the stated selected inverse envelope is much larger than the complementary ceiling 30. Functional calculus thus proves the full ||Q0^-1|| bound. For Q0^-1D, combining the selected bound and complementary ceiling by their sum is conservative and valid; no assumption about the actual load being diagonal is involved.

Keeping a0+b0|δ| inside the energy-dependent estimate gives

    κ²[|δ|/(sqrt(s)(δ²+λ²))+6](a0+b0|δ|).

Using |δ|/(δ²+λ²)≤1/(2λ), δ²/(δ²+λ²)≤1 and κ²/(2λ)=j yields exactly Theta in the proposal. This is where taking the maximum kernel deviation before multiplication would lose information. If Theta<1, the ordered Neumann factor has the stated inverse norm and yields the full actual Q^-1 bound. The same argument applies on the lower lip in its own order; Qminus must not be identified with Qplus-adjoint.

The two-source Schur inverse is well-defined without inverting D at δ=0. Indeed for arbitrary forcing (f0,f1), Qψ1=Df1−λf0 and ψ0=(f1−Aψ1)/λ. Thus invertibility of Q implies invertibility of the whole Schur block, not only solvability for the selected forcing.

## Exact first-source difference and integration

The Schur perturbation is −κ²ΔG in its second-source diagonal. Resolvent subtraction therefore gives R−R0=R0 κ²P1ΔG P1 R. Its 00 block is precisely

    R00−R00,0=κ²R01,0 ΔG R10
             =κ²λ² Q0^-1 ΔG Q^-1.

The reference off-diagonal block is −λQ0^-1 because its factors commute under functional calculus. The actual R10 is −λQ^-1 by the ordered forcing identity. No actual G is commuted through D or Q, and replacing the left reference block by an actual adjoint would not be the same identity.

Multiplying the two full inverse envelopes gives the printed denominator (1−Theta)s(δ²+λ²)². Compression onto prepared columns and taking the operator imaginary part are contractions. The exact majorant integrals are

    integral_R λ²/(δ²+λ²)² dδ=π/(2λ),
    integral_R λ²|δ|/(δ²+λ²)² dδ=1.

The Stone diagonal density factor is 1/π. Consequently the integrated error on each physical window is at most

    [j a0+κ²b0/π]/[(1−Theta)s].

Both numerator constants follow directly, and the real-line extension is applied only to a nonnegative bound, not to the physical spectral measure or matching kernel. There is no logarithm of d/λ in this estimate. This does not imply that all other output-column integrals or temporal bounds lack logarithms.

## Genuine reference and prepared operator aggregation

The scalar source has actual density

    2λ³ sqrt(1−δ²/(4j²))
      /[π((1−2r)δ^4+2(1+r)λ²δ²+λ^4)].

Its exact denominator is nonzero inside the band and at its edges, and the exterior bound x²−2λ|x|−λ² excludes exterior poles on the present much smaller r domain. The explicit algebraic resolvent and its asymptotic normalization give unit seed mass with no missing scalar spectral component. The density is bounded by 2λ³/[πs(δ²+λ²)²], so integrating the inverse-fourth-power majorant outside d gives 4λ³/(3πs d³). Thus the particular scalar premise used in this mass interface is independently reconstructed here; its separate escape and other comparison claims are outside this review.

The reference full fiber is a direct sum of these genuine scalar problems, shifted by the B eigenvalues. On the prepared source-vacuum range only old energies 1 and 3 occur. Their continuum supports are disjoint because their center separation is 2 and their halfwidth is 2j<.006. On the common union of width-d windows, the prepared reference measure is therefore exactly p0 times identity, with the same p0 for both old energies. The real opposite-window resolvents nevertheless remain in the full subtraction and are not discarded because their densities vanish.

Each actual physical window incurs at most eta_mass in operator measure norm before prepared compression. The two windows therefore cost 2eta_mass. This conservative sum needs no orthogonality of actual error or omitted output ranges. Parities form invariant orthogonal blocks, and the initial record0 decomposes into orthogonal record-X sectors with squared weights summing to one; neither adds another factor. Thus the actual prepared union measure is at least (p0−2eta_mass)I. Exact total seed normalization bounds its complement by the displayed minimum with 1, including every actual outside spectral type. The norm of the omitted embedding is the square root of that positive-operator bound. Passive references preserve it.

## Regularity and applicability qualifications

The actual seed density conclusion requires genuine continuous resolvent boundary values on neighborhoods of the full closed windows, not merely a formal expression or estimates away from a finite collection of unknown poles. Given the stated nonzero complete downstream matching, threshold avoidance and the proved invertible two-source Schur block, the seed boundary resolvent is continuous there. The local spectral theorem then gives the claimed absolutely continuous seed measure. No conclusion about outside atoms, an actual complex strip or decay rate is added.

Crucially, this review does not verify that the old unloaded G envelope applies at the new source coupling. The pre-emitter kernel can be independent of the later coupling while its boundary port, retained diagonal, compensation, scalar convention or reference-plane partition still changes. Those must be checked on the installed geometry. The source explicitly preserves this obligation and does not inherit the old one-site emitter's κ limit, mass or runtime by name.

The result is therefore a useful conditional energy-weighted mass interface, retaining full complements and wrong-window inputs. Actual outgoing coefficients, both source-site temporal amplitudes, all core and tail rows, literal common W/aging, normalization, finite transfer and resource claims remain separate obligations. No real gap was found in the stated algebra or its conditional mass aggregation.
