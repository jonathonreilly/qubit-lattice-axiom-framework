# Final focused odd-rectangle source review

Disposition: PASS for the canonical maximal-center, fixed finite-array claims. The newly appended global-ground-selection argument in RECTANGLE_SOURCE_ACTIVATION_PROOF.md is explicitly pending independent review and is NOT included in this disposition. Affected-source confirmation is needed if that extension is promoted. No formal audit, landing, or repository edits performed.

## Material findings and scope

No material defect found in the canonical claim as currently scoped. The note retains the distinction between a neutral multiplicity transition in a symmetry-resolved sector and the unrestricted first excitation gap. It does not describe the rectangle transition as an established unrestricted-ground response. The pending source-proof paragraph states its own independent-check obligation; its promotion must wait for that check rather than borrowing this review's PASS.

Odd-height physical planes form a projective/noncommuting algebra with a protected two-dimensional irreducible factor and a neutral multiplicity factor. The even-height multiplicity-one darkness argument is correctly not reused. The independent algebra and native hierarchy checks establish the square maximal-center Hamiltonian, its exact physical doublet, and the nematic source. The exact even-C darkness on the square uses exchange symmetry on that four-state band, not plane neutrality alone. Other-center intermediate levels and transitions outside that band are explicitly allowed.

For the 4x6x5 rectangle, the distinct matching sizes yield a=3Jz lambda^7/361 and b=3Jz lambda^6/38. The original unnormalized C is computed through H+sC solely as a generating derivative. The source ratios 9/(2Jz) and 54/(19Jz), their difference 63/(38Jz), amplitude 189 lambda^7/13718 and weight proportional to lambda^14 agree with the exact independent coefficient check. Normalizing by sqrt(120) divides the weight by 120; no extra physical-doublet factor belongs in the per-state or doublet-averaged neutral weight.

The draft does not silently identify an effective-H derivative with the observable. Both projected Kato connections start at order lambda^2 in a fixed analytic source neighborhood; their commutator with the first nonscalar lambda^6 operator is O(lambda^8), below the retained lambda^7 amplitude. This is the decisive refinement over a mere full-unitary O(lambda) estimate. Checkerboard parity removes a lambda^7 correction to the dominant b term, supporting the displayed gap remainder O(Jz lambda^8). Reused INDEPENDENT_RECTANGLE_SOURCE.md confirms these points independently.

The square and rectangle geometry, open odd height, anisotropy and finite-dimensional limit are stated. No added physical interaction, fitted coupling, empirical identification, propagation between arrays, infinite-grid embedding, Lorentz scalar or universal matter coupling is inferred. The prior native joining test is outside this block and has not been folded into its result.

## Runner and evidence

Inspected the signed-Pauli stabilizer reduction: selected commuting generators fix the maximal center and one physical X sector, removing the protected doublet without altering the neutral transition. XX and YY phases remain distinct. The matrix builder checks term-generator commutation and exact real symmetry. Its rectangle dimension is 32768 for a 24-column coefficient Hamiltonian; it is not 120-physical-spin diagonalization. The square control is dimension 512 for the 16-column coefficient model.

The source control uses a direct matrix 4.5t(X+Y)+(54/19)Z at K=1, not a derivative of approximate eigenvalues. On the square the displayed weight ratio tests the nematic t(X-Y) diagnostic; the separate plaquette_weight field tests the even diagnostic's darkness. These two evidence roles should remain distinct, as the current note does.

Replayed source_coefficients() without running the expensive spectral control or modifying outputs. It returned t=1/16, t_log_source=9/2, K=19/128, K_log_source=54/19, amplitude=189/13718. This replay is a reproducibility check, not a replacement for the independent path derivation. Inspected frozen result.json: rectangle t/K=.01 gives gap ratio 1.000014593607198, weight ratio 1.0010225103343433, residual 5.11e-14; square t/K=.005 gives exactly stored zero plaquette weight and residual 1.57e-14. These match the canonical numerical description.

The unrelated older INDEPENDENT_RECTANGLE_RANGE.md concerns distinct perimeter coefficients and was not treated as evidence for this new rectangle activation. Untracked scratch/MPS/kink artifacts elsewhere in the shared worktree are outside this coherent review unit. Mechanical aggregate-cache, main-preservation and publication gates remain the root's integration work, not science certified by this report.

## Source SHA256

- `docs/NATIVE_ODD_RECTANGLE_SCALAR_RESPONSE_NOTE_2026-10-18.md`: `a3e8b3424d77bb5e910a7e82a2626de06b87a861cf2b04ab8fd9fc2ada0d5ebd`
- `scripts/native_odd_rectangle_response.py`: `d2f0e23bd372a38777289703c2f1bfcb6cbb1502a3657e25e5d88bca963bce0a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/ODD_COLUMN_NEUTRAL_PROOF.md`: `edd39e7107afbbe2180f3572b8048d1f7aec82e743985f43f58afb27dce794ca`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/RECTANGLE_SOURCE_ACTIVATION_PROOF.md`: `3ff72fd6c0e269d3f6a7728045fa1eafbdfee075ad61db667fe3993f1c63192b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ODD_ALGEBRA.md`: `c9644aec4c6d5834f9c82aaf3524c0aa5ad855d4fbffc34420386ffad2253757`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ODD_NATIVE.md`: `0eea010b8b0dd43cd906f186f2e04a716ec98a11ef95978132ec111af7a53209`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_RECTANGLE_COEFFICIENT.md`: `102e721706cca806021bf561fa5e2f543e2ede8f88f657a89656d7b7c9397b1d`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_RECTANGLE_SOURCE.md`: `d58d785af3367337fd5b6e8b75556450ec06a2711a4c3a167659572e5023410d`
- `outputs/native_odd_rectangle_response/result.json`: `922ed990bdd8fd74b54e070d3fee9db4143ef383aa8b6bef6de2e3e31e972971`

## Affected-source confirmation: ground selection, static line, open rectangle

Scientific disposition: PASS for the updated periodic global-ground claim and the fully open maximal-center extension. This supersedes the earlier exclusion of the periodic global-ground paragraph. One narrow runner source-binding item was sent to root: include OPEN_RECTANGLE_PROOF.md in AUDIT_INPUT_PATHS, which still had only the two original proof files when inspected.

Read the updated canonical note, appended independent domain review, OPEN_RECTANGLE_PROOF.md, INDEPENDENT_OPEN_RECTANGLE.md, and changed runner. The periodic ground-selection proof now excludes every possible competing row-center term through lambda^8. A fixed gauge translation has unique symmetry-compatible phase B^p; real symmetry excludes pq odd, including the potentially dangerous mixed row/column process. The changed-column classification and valuation leave only column terms at order eight besides the known row mixing. Column terms agree between row centers in the lowest column branch. The negative row-mixing shift -tau_row² r²/(2b) then strictly selects |r|=4 at fixed geometry. The exact physical doublet remains protected. This discharges the prior specific gap; it does not make the neutral line the unrestricted first excitation gap.

The new static line coefficient is arithmetically correct: 2(189/13718)^2/(3/19)=11907/4952198. The lambda exponent is 14-6=8 and units are 1/Jz. The text correctly limits this to the positive contribution of that line; it is neither the total static susceptibility nor a total-susceptibility upper bound. Doublet averaging introduces no factor two.

For fully open transverse boundaries, one perfect matching replaces the periodic pair. The independent anchored edge-time integral proves the all-n inverse-wall sum: changing from times to path-edge differences has unit Jacobian and yields (2/a)^(n-1), with a=2Kc. Thus tau=t^n/(Kc)^(n-1). Two boundary and two interior rows give a=(5/2)t³/K²; two boundary and four interior columns give b=4t²/K. The resulting native coefficients 10/361 and 2/19 and original-C amplitude 315/6859 check. The earlier analytic source-connection control and parity counting apply at fixed open geometry. The canonical note confines this extension to the maximal center and expressly does not carry over the periodic global-center proof. The root open proof's tentative global-center sentence remains outside this confirmation.

Replayed only the new exact runner helper, without changing repository outputs: n=2,...,9 and c=1,2 assertions pass; returned open_row=10/361, open_column=2/19, open_source=315/6859, periodic_line_static=11907/4952198. The spectral controls remain periodic column-model controls, not numerical checks of the fully open native array. The canonical note does not mislabel them.

The result remains a fixed finite-array theorem with supplied Hamiltonian and geometry. Removing transverse wrapping still does not establish an embedding in a common surrounding lattice. No audit or landing performed.

### Final narrow-fix confirmation

PASS: verified the third literal OPEN_RECTANGLE_PROOF.md runner input and removal of the open proof global-center speculation. The open proof now expressly claims only maximal-center coefficients. All affected scientific and source-binding issues above are resolved. Source-bound replay remains root integration work. Updated source hashes follow.

- `docs/NATIVE_ODD_RECTANGLE_SCALAR_RESPONSE_NOTE_2026-10-18.md`: `0bf75d7c1a87e79827070fb6f778221fe8a751169ecddab1aa01e74e1f62c812`
- `scripts/native_odd_rectangle_response.py`: `15b59d3686673a729545a0354271c5e1730213f9c09b455e5723d6e9d13abb13`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/RECTANGLE_SOURCE_ACTIVATION_PROOF.md`: `004051a8e22357f8979b7c181bcdef294ed6a3e5f0bfba3a11df0a8fd815b3d2`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_RECTANGLE_SOURCE.md`: `61b9dcdba5406aee3ba51529c183f6f1b3e9c3e0350a85ff2b439cc6fb399bf8`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/OPEN_RECTANGLE_PROOF.md`: `af30729acd315a2457e3cd7235c36a64d311850cbd2eeb5bd02195820a406935`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_OPEN_RECTANGLE.md`: `c26af737ff956af8064f578b7ad2987c1967878e5134c2b8d195123ee13746ce`
