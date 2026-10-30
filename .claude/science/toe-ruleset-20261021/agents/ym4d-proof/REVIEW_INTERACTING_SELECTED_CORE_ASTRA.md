# Independent review of the interacting selected core

**Scoped result: LAND for IC1–IC32 as stated in the frozen producer.** No
blocking mathematical defect or required source repair was found. The result
is a one-step, source-free selected-sector theorem in the explicitly supplied
Wilson / normalized paired-S4-prime model. It does not establish the original
full cut transform, nonlinear multilevel RG, four-dimensional continuum
existence, or a positive physical continuum mass gap. Both physical targets
remain **OPEN**.

The reviewed [producer](INTERACTING_SELECTED_CORE_ASTRA.md) has 790 lines and
SHA256 `b6c875ccc83eb455e12e729ccbd29851d782c63b26e978381927de1e058bfb61`.
Its author [receipt](checks/interacting_selected_core_receipt.json), SHA256
`e6920761977e1b65b824cce98cbccc02592f524bb0ac32cbefd2b3e94d374fb0`, binds the
four-file packet. All packet hashes, 21 declared input hashes and 12 protected
source hashes match. These are byte-identity checks, not proof certificates.

## Independence, scope and findings

This is same-family, fresh-context Codex review, separated from authorship.
Astra/max was requested; this worker has no independent backend attestation.
I read the complete producer and the proof inputs at the ranges recorded
below, then froze my [independent mathematical reconstruction](checks/review_interacting_selected_core_initial_findings.md),
SHA256 `ccb8c778c8a7cac72ea11259288184360252db71deb2225ea022bef886a3aeed`,
before opening the author's validation, read manifest, freeze receipt, or the
predecessor review reports. The producer's own announced conclusions and
aggregate evidence/scope descriptions were unavoidable exposure. This is not
a claim of blindness or cross-family independence.

There are zero unresolved P0/P1/P2 scientific findings. Required repairs:
none. One initial bibliographic nit is **withdrawn**, not silently deleted:
the experimental arXiv HTML author blocks omit Bałaban, but the official
versioned abstract pages for [Part 4](https://arxiv.org/abs/1609.01748v1) and
[Part 3](https://arxiv.org/abs/1609.01747v1) explicitly list all four authors.
The producer's attribution is correct. The coordinator first supplied that
counterevidence; I independently opened both exact-version metadata pages.
The original preliminary finding remains immutable in the reconstruction.

A coverage clarification also remains explicit. The initial reconstruction
correctly records a first FK read of lines 1–430, but its phrase about
“FK24 source-corollary content” was imprecise: the displayed FK24 is at
lines 457–458. I subsequently read 425–472, including its entire derivation,
after packaging exposure. The final scope includes all consumed FK2 and
FK16–FK24 steps; the first read is not restamped as a longer read.

## Mathematical reconstruction

| Claimed range | Independent assessment | Boundary preserved |
|---|---|---|
| IC1–IC4 | The pinned quotient leaves `n=(3L^4+1)T^4` free links and `Dn` scalar modes. The brick lift and paired contour words match CB, including the lifted-brick qualification at T=2. IC2 reproduces the exact unsubtracted density with `sigma^2=N/u`. | The Wilson law, normalized S4-prime kernel, torus and conventions are supplied model data. |
| IC6–IC13 | The complex original-V tube, all actual principal-compression resolvents, marked parametrix, critical point, whitening map and full determinant are controlled uniformly in T and u. | The constants depend on fixed N,L,kappa and the chosen support rate; the determinant's main budget is not small. |
| IC14–IC20 | The auxiliary interaction and connected logarithm are coefficientwise even. The first nonzero coefficient has p-independent fourth/sixth moment bounds; the remaining even tail gives the stated O(sigma^2). | All three cutoff/chart conditions are retained. u, b, C and the reference law stay fixed when z varies. |
| IC21–IC24 | Both real selected sectors have their exact prefactors. Original coarse derivatives have rooted and anchored-input bounds. The product of HS balls, its normalization and radial tensors are correct and gauge covariant. | Complex continuation is a pulled-back fixed-W integral. The cube has no asserted colour-rotation Ward identity. |
| IC25–IC32 | The exact finite-u/tree/one-loop dictionary, critical shift, Haar/dexp cancellation, full-colour determinant, tree gauge Gram and FLOW factors agree. | No extra ghost, harmonic deletion, all-depth coupling estimate or fixed-free-complement invariance is added. |

The detailed reconstruction supplies the algebra behind these assessments.
The following are the decisive checks, including points where a weaker
argument would not establish the claim.

**Fixed complex readers and connected inverse.** If `K=Kbar+E`, the scalar
row and column estimate gives `||E||_2<=gamma/4`. Every actual compression
therefore has Hermitian part at least `3gamma/4`. Distance conjugation costs
at most another `gamma/4`, giving inverse norm
`1/(lambda+gamma/2)<=2/(lambda+gamma)` and the exponential entry estimate.
This is an accretivity argument, valid about arbitrary real small-curvature
holonomies. It does not infer a product complex domain from real smoothness.

For a residual column the inside index anchors its actual Wilson/kernel
readers, so the R+4 collar includes the outside endpoint too. The complete
scalar density and periodic multiplicities occur in the row and column sums.
Marking a product support requires the column sum of its prefix and row sum
of its suffix; the resulting bounds are `p/(1-r)` and
`J n_R p/(1-r)^2`. Consecutive labels meet at the summed index. This produces
connected original-reader atoms rather than just endpoint decay. The same
marked algebra controls the nonlinear analytic series and the full trace.
The order of choices—box size, contraction radius, then curvature and coarse
tube radii—makes all smallness conditions nonempty.

The force at a complex brick lift is O(delta_*+8rho_V), and the kernel/Haar
forces vanish there by common-path invariance. The scalar majorant includes
root and substituted-factor marks. Its nonlinear derivative vanishes at
zero, so the contraction is uniform in volume. Resolvent integration gives
the principal symmetric inverse square root and `C^T K C=I`; no finite-volume
implicit-function radius or colour-diagonal approximation is used.

**The coefficient and its support cost.** At fixed physical u,
`U_z=z J_3+z^2 J_4+...`. Direct differentiation of `log E exp(-U_z)` gives

    H_2 = -E J_4 + (1/2)(E J_3^2-(E J_3)^2).

Each cubic mean vanishes. Disjoint reader supports have zero covariance,
and S=T is included. Cube conditioning lowers absolute coordinate moments;
ball conditioning lowers radial moments while preserving the independent
uniform angle. Comparison with the full product Gaussian and Holder's
inequality bound every absolute degree-four/six monomial by 3/15. No inverse
cutoff probability growing with volume enters this comparison.

To root the cubic pair, mark x in either support. The two choices cancel
the 1/2 by an upper bound; the partner can meet at any of at most |S| boxes.
The two lost support-weight units pay this factor, giving
`3 A_4+(15/2) A_3^2`. Thus the estimate is a rooted coefficient norm,
not an extensive variance divided by volume. At radius `r_z/p^3`, the
interaction is uniformly small. Every overlap collection is even under
`(z,W)->(-z,-W)`, so the two-stage connected expansion preserves parity
support by support. Cauchy's tail is
`(2/3) sigma^4 p^12/r_z^4`; the separate condition `sigma^2 p^12<=1`
then makes it O(sigma^2). Parity alone would have left p^6 in the first
coefficient, and is not the proof used here.

**Derivatives, balls and Ward identity.** A fixed q-th coarse jet costs
`q! r_V^-q`. With one input fixed, the other choices contribute at most
`(q_V |Y|)^(q-1)`; summing all inputs at a rooted box costs the stated
q-th power instead. The remaining support weight pays both. Filling boxes
yields the reduced original-block rate, not an arbitrarily prescribed rate.
For a ball, polar integration gives exactly
`a_j=z_(p,D+2j)/z_(p,D)` and normalization `z_(p,D)^n`; these are not
untruncated Wick constants. The scalar cube has `z_p^(Dn)`.

A coarse root gauge acts on each free-link algebra by its starting-block
adjoint. It preserves the internal tree and the HS balls. Phase covariance,
critical-point uniqueness and the resolvent formula establish the actual
b and C transformations. The Ward tangent is
`omega_x-Ad(V_c)omega_y`. At identity global colour invariance kills the
one-jet; differentiating the Ward identity then gives `R''(1)d=0`.
These facts provide neither spatial symmetry of the axial selection nor
volume-first marginal extraction.

**Exact action, measures and units.** FK's fixed-chart remainder is a
uniform inequality, including independent complex plus/minus means and the
scalar SU saddle constraint. Its factorization gives
`F_u=F_T+sigma^2 F_1+sigma^4 R_u-sigma^2(D nc/2)log(kappa u)`
exactly. Subtracting the critical equations gives
`b_u-b_T=-sigma^2 K_T^-1 F_1'(b_T)+O_v(sigma^4 delta_hat)`.
The tree-value increment is quadratic in this shift because the complete
tree gradient vanishes. Its scalar contractions retain the matrix mark and
both vector marks. The trace-log difference likewise retains every colour
and every mode. Together with H_u these give the connected unscaled
O(sigma^2)=O(1/u) remainder; the scaled-phase error is O(u^-2).

The real affine integral has prefactor
`h_N^n (2pi sigma^2)^(Dn/2) det(K_u)^(-1/2) Z_p`.
The vacuum terms in IC29 have the correct signs; `nc log A_0` and the E0
vacuum remain in their separately stated terms. The right logarithmic
exponential differential is
`Ad(U0^-1)(1-exp(-ad a))/(ad a)`, whose determinant equals j_N(a).
At the tree critical point the coordinate Hessian is `E^T K_intr E`, so its
half log determinant cancels the `-log j_N` once, exactly.

For the root-pinned gauge tangent and free insertion,
`|det[D_r,J]|=1`. In an orthonormal gauge/complement basis this gives
`det(D_r^*D_r)|det B|^2=1`, while the slice Hessian has determinant
`|det B|^2 det H_perp`. This proves IC31, including the sign of its gauge
Gram. The complex version is bilinear analytic transport, not a Hermitian
projector involving conjugated V. Finally `a_HS=sqrt(N)a_FLOW`,
`H_c,FLOW=N H_c,HS` and `h_FLOW=N^(D/2)h_N` give IC32 with the positive
half log of the normalizer covariance. Its N factors cancel correctly.
This uses the transported-slice identity and does not revive UL's corrected
fixed-free-complement assertion.

## Evidence, history and disposition

No numerical experiment was necessary or run. No numerical criteria, finite
sample, old checker PASS, or metadata validator is used as evidence for the
analytic uniform theorem. The inherited FK review's surviving mutation that
deletes lambda from one Weyl routine remains a recorded coverage limit; its
separate independent SU(3) calculation and the FK proof are not relabelled as
a new IC execution.

The original author packaging failure is retained verbatim in the read
manifest: an unanchored equation-label regex counted the inline `sup_(IC3)`
and returned `[1,2,3,4,3,5,...,32]`, causing an assertion failure. The later
parser matches only line-ending equation labels. No formula, acceptance
threshold, or scientific claim changed in that repair. I inspected the saved
metadata and independently compared its bindings; I did not rerun the author
metadata command or restamp its output.

[The reviewer read manifest](checks/review_interacting_selected_core_read_manifest.json)
records actual ranges, hashes, exposure order, recovered truncated reads and
literature versions. The primary comparisons are Dimock
[1212.5562v2](https://arxiv.org/html/1212.5562v2), section 3.14 and Appendix F,
and Bałaban–Feldman–Knörrer–Trubowitz
[1609.01748v1](https://arxiv.org/html/1609.01748v1), Appendix A, and
[1609.01747v1](https://arxiv.org/html/1609.01747v1), its introductory and
selected contour passages. These compare product-measure expansion, marked
field-map norms and contour boundaries. The relevant steps are rebuilt
locally; their different bosonic/scalar models supply no Yang–Mills premise.
No third-party PDF was saved.

Methodology was selected at `01589af3faf806b736c42dc2f3bd625e9edead9f`;
installed entry-point drift was read explicitly against that revision, and
applicable references were read from the same object. [PROCESS_LIGHT.md](PROCESS_LIGHT.md)
controls this research-log review. Entry HEAD was `295b508bea2c65bf548172f3190e32f7f7eaf6cf`.
The coordinator's move to `a0a3499e84e23e783a4933cce4459b249bfdaf07` added only
an unrelated REC_CONT spot-review file; the inspected input hashes remained
unchanged. Later exact checkout identity and final hashes are bound by the
[review receipt](checks/review_interacting_selected_core_receipt.json).

Proof obligations are closed at the stated selected-sector scope; model and
normalization inputs are disclosed. No framework primitive, empirical value,
new axiom, no-go claim, formal proof-assistant certificate or retained grade
is introduced. The full-complement and fixed-source/history return problems,
admissible input-class closure, spatial-symmetry and marginal-limit
identifications, nonlinear multilevel RG, continuum construction and physical
gap remain separate. Source-level preservation is confirmed; whole-PR/current-
main integration, audit compatibility pipeline, Git and publication remain
the coordinator's responsibility. This review changes only its owned report
and evidence and grants no audit authority.

VERDICT: LAND
