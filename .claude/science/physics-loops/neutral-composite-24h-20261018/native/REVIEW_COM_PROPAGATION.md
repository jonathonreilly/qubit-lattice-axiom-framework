# Final focused bulk COM review

Disposition: PASS. No material integration defect found. The claim is longitudinal dispersion of the complete fixed-order compact-sector outgoing coefficient pole near p=0; no exact microscopic pole or error-controlled momentum derivative is certified. No repository changes, formal audit or landing performed.

## Geometry and normalization

The canonical text correctly distinguishes the derived endpoint coefficient from an assumed kinetic mass. Each axial endpoint move has magnitude -1/2 in slow units; opposite-end center shifts +/-1/2 give -cos(p/2) per length link. The independent native-geometry report checks actual interval outputs and the orientation gauge. Slow transverse host moves keep the longitudinal interval unchanged, so its leading dispersion is p-independent. The short-arm contraction gives -gamma A with normalized A, hence Sigma_p=gamma² G_AA. No extra orientation or endpoint normalization factor is missing.

The Fermi-curve argument extends the independently checked strict radiation proof: on u+v=gamma the scalar hole functions are constant, while Ahat=2gamma²-4uv-2 is not. The curve is regular near gamma=1. Thus the strictly negative imaginary self-energy, nonzero boundary denominator, and compact-neighborhood continuation bounds are consistent. The separately supplied geometry and analytic reports now discharge each other's stated conditional inputs.

Dividing by gamma gives the slope f/gamma and boundary Sigma/gamma, producing alpha1 gamma^(1/3) f^(2/3) and scattering offset f(2+a_p). Consequently the alpha1/4 physical coefficient and width [-Im a_p]Jz lambda^4/4 are correct. There is no additional gamma multiplying the width. The unspecified native real order-lambda4 mass shift is correctly retained as a remainder rather than read from the NN numerical model. Its reality/locality, not a generic complex norm estimate, is needed to preserve the stated leading width; the independent analytic report makes this requirement explicit.

Fast saddle detuning remains -2gamma lambda+o(lambda), and the excluded-arm separation remains 2gamma Jz lambda². The preexisting fixed-order estimates therefore stay uniform on a sufficiently small fixed real p neighborhood with gamma bounded away from zero. Neither the text nor the report extends them to p near pi. For fixed nonzero p, the positive lambda² energy difference dominates the higher terms. The note explicitly declines to differentiate a merely real-p-uniform remainder, so it does not claim a controlled curvature, group velocity or wavepacket theorem.

The corrected transverse support statement uses at least 2ell changed spins, allowing translated pairs that share one column. That is sufficient for fixed-order suppression of deep-arm transverse motion. Finite endpoint contacts remain capable of transverse dispersion; no all-order immobility or isotropy is asserted.

## Numerical and source evidence

The runner binds the root proof, model, imported host implementation and native endpoint JSON as literal inputs. It checks the exact displayed native row coefficients, then uses an explicitly specified NN arm with diagonal f(n+2), hopping -gamma and boundary gamma² host(E). The Schur equation's first site is ell=3, so its first diagonal is 3f; the remaining banded tail is indexed consistently. The host is evaluated at the complex outgoing energy, not frozen throughout the root solve.

The numerical coefficient is measured after subtracting the band bottom and leading Airy term, and its prediction (2+a_p)/8 is specific to this NN model. It does not include the native K4 bulk shift. Increasing the cutoff by factor 1.2 is a stability control; the reported Schur residual is not a rigorous pole-position error, as the canonical text explicitly states. The imported host has a main guard, so import does not regenerate its standalone JSON.

Inspected result.json: at lambda=.003, p=0,.3,.6, the errors relative to the NN asymptotic coefficient are approximately .00012414,.00012457,.00012588, below the runner threshold; recorded cutoff differences are zero to reported floating precision, and Schur residuals lie between 4.2e-12 and 1.7e-11. This is consistent with the stated development-control role. Existing independent geometry and analytic checks were reused; no redundant full spectral replay performed.

The supplied Hamiltonian, anisotropic reference-sector construction, fixed perturbative order and near-zero momentum range remain visible premises. Finite-momentum original-source residue, state preparation, microscopic pole transfer, empirical units and cosmological identification are expressly open. Aggregate source-bound replay and publication mechanics remain root integration work.

## Source SHA256

- `docs/NATIVE_BULK_COM_PROPAGATION_NOTE_2026-10-18.md`: `5dc4d54d4516433c8a0292c481bc19a858011b0e785f5f8e9f47cde0dabbf97f`
- `scripts/native_com_propagation.py`: `06b5b3b70eadbcabfcaaa55ee3bc4db442ffc842f43ccbcaddfd27cf1952f488`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_COM_POLE_PROOF.md`: `f8b7f1cca9c894f693a17fe6e26d16e797b2e693560e00d28b10b1b715587454`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_com_model.py`: `ea73897401bf70c96655da8bc0473e4c29607e981c8042290d49858f57ec91bb`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py`: `c45065369d566859cd563e8108df1b00ca3737c5dfaf1c5ad582ea11c5ad40c2`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bulk_second_other.json`: `d28a431a110f0c0472c1b7ad4b2b314fc4d3a34a7f1189d837f9663758be7018`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COM_GEOMETRY.md`: `b16373203e3645a7080cee6cf8d98519a99296ca691ce9be53e4b1b2d6500510`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COM_POLE.md`: `f93257e0e44c0dce046343ab7341f077a908f56188dbe37b2a612edaddec4f4f`
- `outputs/native_com_propagation/result.json`: `b45b0f9804586b693a1f889fee66f1600bb1def539176ee9f3b4d4f8fdfc6f86`


## Affected-source final confirmation: original Fourier readout

Disposition: PASS for the added complete fixed-order outgoing source-residue claim and its explicitly supplementary NN-model controls. Read the new source proof, independent native effective-source report, independent residue/nonvanishing report, changed canonical section, runner and model helper. Existing pole qualifications remain intact.

The distance-two bond midpoint convention gives the two affected bonds per flipped spin phases exp[ip(z-1)] and exp[ip(z+1)]. Their sum supplies cos p, and the normalized same-layer pair source is exactly -sqrt(2)lambda cos p d. The native vertices are v_A=-gamma d2-e and v_D=-2e; they must not be replaced by the zero-p proportionality. The corrected identity v_A=(gamma/2)F0(p)d+(gamma²-1)e and the actual confined-fast strip limit R_ed->1/(2gamma) yield the stated lambda² cos(p)/gamma slow source. Direct slow source remains absent at second order by the same physical flip count.

The -gamma slow arm-host coupling cancels that inverse gamma. Combining its endpoint source with P11=f gamma/(gamma+Sigma_p)^2 yields the displayed coefficient gamma cos²p [u0^T G A]^2/[8(gamma+Sigma_p)^2]. The physical energy-unit prefactor cancels upon conversion of the pole denominator. For C_-p/C_p in the real interval-center fiber convention, analytic continuation gives the transpose square, not a modulus-square. The canonical note explicitly distinguishes this complex Riesz residue from a positive isolated spectral weight.

The nonzero overlap is now analytical rather than inferred from its decimal value. Hc=-2s and Hs=-2c-A-2D give u0^T G_hole A=sqrt(2)g_cA/(E g00-1). At E=-2 the Fermi curve has u,v in [0,1], so Ahat=-4uv is negative on regular arcs and Im g_cA is strictly positive. The denominator is nonzero, and continuity preserves nonvanishing in a sufficiently small p neighborhood. This also explains why strict positive spectral density of A alone would not have sufficed to prove the mixed u0-to-A overlap.

The helper's direct Schur residue is consistent: differentiating the tail resolvent gives g_tail'=-tail^T tail, hence F'=1-gamma² G_AA'+gamma² tail^T tail. Its P11=1/F' uses the correct sign and bilinear product. Multiplying by lambda^4 cos²p times the host-source amplitude squared and dividing by lambda^6 is the intended scaled residue. The host derivative is estimated by a fixed central difference step 1e-5; it is a numerical control, not a certified derivative/error bound. Cutoff and pole residual checks likewise do not supply a rigorous residue certificate. The independent analytic argument supplies the theorem.

The runner now binds BULK_COM_SOURCE_PROOF.md explicitly and records source residues on the same p/lambda grid, checking the final-lambda coefficient error. Source-bound replay remains root integration work. No new source interaction, full-H pole, pointwise real-axis limit, empirical coupling or cosmological conclusion is claimed. No further material fix found.

Updated affected-source SHA256:

- `docs/NATIVE_BULK_COM_PROPAGATION_NOTE_2026-10-18.md`: `45e83bf6d3dbb6996055edb3feb91c87d3b75701dcab5a240861b52b55f1b0c2`
- `scripts/native_com_propagation.py`: `561b0d811b2dd31b031ccd57cbddfd40cd0b0cf9da1fd907ee9617de5c8fc4b4`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_com_model.py`: `d45b600908306c7067c99f87d0f60d885c9d5c6a327ae563ec44d6fcaf83b388`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/BULK_COM_SOURCE_PROOF.md`: `72895d6648b24785e760c3d1a29f1b9ff7b96eb7d28e7db4f8ee2658035a9e90`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COM_SOURCE.md`: `758fcec916e6d1f83d7bdc60b87b6b93c50a0ef557a298fbee10f6d5beecdecc`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COM_EFFECTIVE_SOURCE.md`: `4f5676e78085cb7295207503ca74dcb54528ce2acf399277e8a9ac68e556dd37`


## Final narrow additions: microscopic Fourier window and derivative boundary

Scientific disposition: PASS, reusing the established microscopic ground-window theorem and the completed coefficient-pole/source checks. This confirmation concerns only the two new sections; it does not repeat or strengthen the earlier mathematical premises.

The Fourier correlation is correctly <C_-p(t) C_p> connected, with C_-p=C_p dagger. For allowed real torus momenta 2pi k/L the midpoint weights match across periodic seams. Their modulus one preserves the source norms, two-source volume factors, local plane-neutrality, and absolute correlation-tail estimates. Therefore the prior actual-ground-density, dynamics and source-replacement estimates remain O(lambda^17), O(lambda^13), O(lambda^29). The smooth-window suppression of high N is V(JzT)^-5=O(lambda^8), as before. The local charge-raising decomposition is retained; no nonlocal spectral projector is inserted into the locality comparison. The finite/infinite correlation comparison also retains its absolute-sum control. No assumption that an arbitrary actual ground density is translation invariant is silently introduced.

The canonical statement correctly compares the complete smooth connected-correlation window, with its background and fine structure, for every actual ground density on the specified growing finite cubes. It transfers neither the outgoing pole nor a positive peak. The proof explicitly excludes automatic replacement of the smooth compact time window by a causal theta filter. Real-p uniformity does not supply complex-p bounds.

The derivative-boundary artifact accurately records the failed strengthening: real self-adjoint fast-arm strip estimates at depth lambda^3 cannot automatically handle a fixed complex kinetic perturbation. The isolated slow-arm form estimate is useful but does not close the complete-channel derivative argument. Hence no controlled curvature, ballistic velocity, propagation distance or full microscopic pole is inferred. The canonical limitation agrees with that artifact and preserves the valid real-p dispersion statement.

Root was advised to include the new proof/boundary artifacts in the unit's final declared proof inputs if the runner remains the source-bound carrier. This is packaging/source-binding follow-through, not a newly detected mathematical gap. No repository edits, audit or landing performed.

Affected-source hashes:

- `docs/NATIVE_BULK_COM_PROPAGATION_NOTE_2026-10-18.md`: `1c0c17aa31adca39253dd8cac17a33e0b4d1ad7ac1fbf97e6b6251aad30e85ae`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/FOURIER_GROUND_WINDOW_PROOF.md`: `2712a30e63abb62f7ce95e1c47ff0d522c488924c0972c8636df1b116dc3a031`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_FOURIER_GROUND_WINDOW.md`: `8f934ab11e07d998ae1d632819f05eb300881b6d60b7d46160e9e0d87e443530`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/COM_DERIVATIVE_BOUNDARY.md`: `5aebd5b8282b788d0257ceb299abe5b633c680cdecdbcae738da0577579c823d`

### Final source-binding fix confirmed

PASS: parsed the final runner literal AUDIT_INPUT_PATHS and verified both FOURIER_GROUND_WINDOW_PROOF.md and COM_DERIVATIVE_BOUNDARY.md are included. No new scientific changes reviewed or inferred. Source-bound replay remains root integration work.

Final runner SHA256: `a6d701ee49da5000e918c1d40d6076106afff7cdd3d33cc1cd989bb07845eaf3`.
