# Focused stationary native benchmark review

Disposition: PASS for exact finite-sector reduction and explicitly numerical finite-system diagnostics. No material remaining mathematical or physical overclaim found. Not a formal audit, global-ground certificate, or landing authorization. Root retains authorship. Aggregate/cache replay remains a parent-owned integration gate while running; this reviewer did not duplicate the heavy 27-site solve.

## Scope and identities

Read the canonical NATIVE_STATIONARY_RESPONSE note, runner, stationary derivation, all nine declared Python inputs, supplied JSON results, and independent sector/response/spatial reports. The open 3x3x3 geometry, one qubit/site, supplied H=-J sum nearest compass bonds, selected invariant sector, J=1 numerics and state preparation limits are explicit.

The three Z planes and two adjacent X-plane products commute and have independent rank five, giving 32 sectors of dimension 2^22. Individual X planes anticommute with each odd-intersection Z plane; their exact simultaneous sign flip pairs all sectors and justifies the 16-representative survey. The CSS affine offset, X-character row operations, reduced flips/phases and YY sign are consistent. No Hamiltonian terms are discarded. The central composite and local energy terms preserve the chosen sectors.

Independent lightweight replay performed here: all eight 2x2x2 sector intertwining errors are exactly zero; the union spectrum agrees with the full 256-dimensional matrix to 1.60e-14. I also constructed physical Kronecker star operators at interior/face/edge/corner geometries. C_x=2e_x^2-degree(x)I/2 at J=1 has zero matrix residual in all four cases. Thus corner composite amplitudes vanish by operator definition, not a localization measurement. The final note explicitly includes this boundary definition.

Connected source moments and -<double commutator> acceleration are correctly implemented for real symmetric matrices and real vectors. Mixed polarization has factor 1/4, and spatial reconstruction uses ||v|| e0^T f(T)Q^T b_x with the correct indices. Sum_x e_x=H yields sum_x b_x=(H-<H>)g; the numerical zero sum is a conservation control, not independent convergence certification. The damped inverse moment f(lambda)=lambda/(lambda^2+eta^2) is properly distinguished from twice that quantity under the usual ground-state static-response convention. Numerical Cauchy-Schwarz observations do not independently prove positivity of L or lowest-state status.

Full-H reconstruction and direct Rayleigh residuals appropriately distinguish actual approximate eigenvectors from Lanczos nodes. The three residuals approximately 3.99e-7, 2.25e-5 and .00386 are retained, including poor resolution of the third. A floating residual is not an interval certificate, isolated eigenvalue/weight proof, or a thermodynamic pole. Form-factor participation values are explicitly transition-density summaries on this open cube; neither localization lengths nor bulk particle wavefunctions follow. Unknown exact degeneracies and unobserved low-weight states are not excluded merely by centering or four computed eigenpairs.

## Evidence and limitations

The survey JSON contains all 16 representatives, complete=true, with maximal recorded eigenpair residual 2.37e-9. The all-plus representative has the lowest found Ritz value -27.164894425063462. This is a comprehensive numerical comparison, not proof that each ARPACK run found its sector minimum or that the global lower edge is certified. The independent odd-cube signed-orbit report provides 9,120 exact term checks; this review inspected that argument rather than independently rerunning the large calculation. Independent response/spatial controls are small native graphs; the 27-site response numbers remain root numerical runs.

The runner declares all nine source dependencies, reconstructs raw NPZ eigenvectors before their consumers, uses the current interpreter and captures numerical library versions. Thus raw NPZ omission from committed inputs does not omit an external input: these are generated intermediates. Timing fields and floating values may vary across environments. No full Lanczos reorthogonalization or breakdown guard is present; the note accurately labels current quantities numerical diagnostics and disclaims node/error certification. No present output indicates breakdown. An extension to arbitrary parameters or longer recurrences would need explicit robustness handling.

Resolved review feedback: stale incomplete-survey statements were updated; the selected vector is called numerically lowest computed rather than certified ground; boundary composite and approximate-vector transition-density scope are explicit. Two residual editorial phrases were sent to root: stale 'Next: focused independent response check...' and 'ground eigenpair residual' in conservation prose. These do not change the explicitly stated numerical/no-global-ground scope, but should be cleaned before final publication.

## Snapshot hashes

HEAD: 74513a2e5a34a068f5d4c1997d34e81fcddd40ca

- `docs/NATIVE_STATIONARY_RESPONSE_NOTE_2026-10-18.md`: `e470a3639b0dba23b527abf7c8810a86ab6886338b5bf5ec7e3f60398965d30c`
- `scripts/native_stationary_response.py`: `33e1dc26932b69c708006191a9b2233acaccf08f6e1db02340c3022d38323ba2`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/STATIONARY_SECTOR_DERIVATION.md`: `7ff589797f70a4e1becea06cbd62df86b92b191858466c616333d3430362882c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_basis.py`: `903ece39673616ae809fd44e66a186325252f0c75c77618ec905e7f95f5ef529`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_control.py`: `b72e613134547ae85f404a7af941c2daf9c92ec75841056e03b415a8e7bd892f`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_solve.py`: `617a143fbd5112cee5d818512b72e9d49abd09970660a07e3a44e6f51b05c3b1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_survey.py`: `b7ce8302a6f3d85774c14277e2f35dca03910de83cf783625570d102a95d54d8`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_response.py`: `e77de6959edc08de458e4c27f6a6a27367f6ab7cd1902ab54f35d04dcc08273e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_mixed.py`: `790bc67c9db9e9515c7623b6f3d8c6dbe4b83435bf6caf08a09d4f296b0ff9d0`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_stationary_spatial.py`: `a6e5b92d87b76a9bf04437799abfb5cbc57db7e2c718da138ba359846f444875`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_visible_ritz.py`: `9c69faa5388ffc94af863f4481ef077915ed9430533826d36ccac06a7a8d82ee`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_mode_form_factors.py`: `47ed54116f08448cc1d51b48405ec7e83367ae0055cfd0230f78bc199ba78849`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SECTOR_CHECK.md`: `828ce209fb29bfae175fa6cae123b4f759807048c61df8ba3852aaaeccb7907b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_STATIONARY_RESPONSE_CHECK.md`: `8e78e83e0fb8fa8453604fe9cdaab54c9aab1ba5007f850c3c827bdb36f51c77`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SPATIAL_RESPONSE_CHECK.md`: `59cae94ad7b68f80cf6eafa53bb2f534321f7318ecf10b563dc3da7a1976ffb6`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/compass_sector_control.json`: `bee4afb303e3dc5c2d46449e1553b6c45bd1c656f7dff3c09d66817b3773eb6c`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_3x3x3_plus.json`: `63b3a76f2da9262469044cad24d25392330f6fa6c09cec115a5d2e79127cd64a`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_sector_survey.json`: `1cedc01df1e37e378d5007c810c8bc6248d2275989548d4315619d4349ea31d1`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_response.json`: `04fb349a2ee4e2a6992ede608d94f55df5a3ccfc35faf5d0a85bc555e438f980`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_mixed.json`: `be5436b16651ec60193dc8e272d77ec51946315d17c631be9cffe48dc7b22de5`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_spatial.json`: `aeacdea6dbbc76e6ad1233cc2db99fd7c819f3b96ea16256e9cf65f66317e3f4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_visible_ritz.json`: `ac92ec152262d9d3585f482678044453d6e04c8063d1fa1b7ad4fd23fb517719`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/stationary_mode_form_factors.json`: `e2ae47885c0cac381d06794467cf7b5d23b7a7dd5ee7efa215da9dad141098e3`
