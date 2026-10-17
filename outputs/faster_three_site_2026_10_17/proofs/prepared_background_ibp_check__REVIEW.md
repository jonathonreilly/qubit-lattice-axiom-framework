# Distinct check of the actual prepared-background IBP bound

**Conditional support; no necessary numerical or mathematical correction found.** The complete target `prepared_background_ibp/PROPOSAL.md`, SHA256 `90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a`, has the correct hard-edge, lip and physical-window factors. Its bound below `.000134*T/|t|` follows at the stated existing nominal point from the full recovery derivative and the separately checked D3 estimate. This is a represented-background component bound for the infinite apparatus, not an updated complete-device error, finite storage theorem or new operating point.

The fixed-Hilbert-space interpretation is important: each old-energy window has its own fixed complementary channel projector. Those projectors need not be the same for the two windows. Their recovered vectors must be embedded in the same physical output space before summing. The target's per-window integration and subsequent triangle inequality are valid with that interpretation; no orthogonality of the two energy-window error images is used.

## 1. The actual resolvent column and its output space

Fix a parity and conserved record-X sector. The endpoint forcing fiber is the complete eight-coordinate internal space. Let the common physical output Hilbert space contain all235 finite background head positions with that fiber, together with the entire slow receiver ray with the same fiber. The three new source heads form a different range and are excluded from this background map.

On window `I_e=c_att+2j+e+[-d,d]`, e=1 or3, let P_e be its fixed selected propagating B projector and C_e its fixed complement. On the receiver ray retain C_e and on the235 finite heads retain every internal coordinate. This defines an energy-independent bounded projection within that window into the common physical output space. The two projections for e=1 and e=3 may differ, but their images are both subspaces of that same physical space.

This description gives a precise meaning to the finite-plus-closed-tail recovery L_e(E). It is not a vector in an abstract Hilbert space whose basis is silently changed with E. The tail entries are the actual physical sequences, and fixed B projectors distinguish closed and open channels on each window. The non-square-summable propagating stationary ray is excluded from L; its wave-packet contribution must be handled elsewhere.

The exact three-source Schur equations give the last-source resolvent column

    psi_2=a1 a2 Q_lip^-1 V_seed.

Restoring the emitter-free background gives, in the actual physical order,

    B_e,lip(E)=-kappa a1 a2 L_e,lip(E)Q_e,lip(E)^-1 V_seed. (1)

The minus sign is the source-to-background block-resolvent sign for the specified negative hopping. No sign or phase is inferred from a scalar response surrogate. For the norm estimate the orientation chosen for the Stone jump has no effect, but its factor `1/(2pi i)` does.

The full noncommuting Q is essential. V_seed is a fixed norm-one prepared inclusion containing both the selected old-energy input and the wrong-window prepared input. Actual output induced in selected or complementary channels remains in (1). Neither L nor Q^-1 is replaced by a selected scalar entry.

## 2. Why Hilbert-valued differentiation and Stone integration apply

The imported finite matching matrices are invertible on the closed retained windows, with the stated uniform inverse margins. The physical roots have fixed analytic branches there, no relevant threshold lies at a hard endpoint, and g and lambda are strictly positive. The ordered source inverse is therefore differentiable on each lip. These are real-window regularity statements; no actual-source complex strip is required.

For each closed slow root v, the physical tail lift is the sequence

    sqrt(j/g) v^(m+1), m>=0.

The checked bound `|v|<=2g/.162<1` is uniform on the retained window. Its differentiated sequence is

    sqrt(j/g)(m+1)v^m v'.

The square series of these derivatives converges uniformly on the compact window for each fixed positive g. The exact lift and derivative formulas give the already checked ceilings `.00068` and `.009`. Thus the lift is continuously differentiable as an operator into the fixed sequence Hilbert space; it is not differentiated merely coordinate by coordinate without norm control. The finite coordinate recovery is differentiable by its finite inverse formula. Together these facts establish the needed absolute continuity of L and of (1), with integrable derivative.

The source's full-domain inequalities are consequently legitimate inputs:

    ||L||<=L0=14000,
    ||L'||<=M_g=1.00068*(7.29e16+3.31e7/g)+30.

They cover every input in the internal forcing fiber, not only selected open incidence. The source of14000 is the disjoint OUTPUT-range square sum

    7900^2+6000^2+9000^2+3270^2=190102900<14000^2.

The derivative comes from the assembled equation `F'=-RF-j R V_o Q_slow' V_o^T F`, followed by the complete tail product rule. The coefficient j is the physical connector self-energy coefficient. The `.009` tail derivative multiplies the actual output value3270, giving the final allowance below30. This use does not import a newly proposed selected-only direct-core or converter derivative in place of the full L'.

The represented Stone formula also requires the inherited local spectral regularity of the actual source/background matching, not just a formal algebraic inverse inequality. The checked continuous physical boundary values, finite matching regularity and nonzero source inverse on these windows supply that premise. It is reused here, not replaced by a claim that any small matrix majorant proves spectral absolute continuity. Possible outside atoms remain outside this argument.

For finite-dimensional input and Hilbert-valued output, the above continuity and uniform bounds make the integrals ordinary Bochner integrals. At each fixed window/lip, integration by parts gives exactly

    int_A^B exp(-itE)B(E)dE
      =-[exp(-itE)B(E)]_A^B/(it)
                       +(1/(it)) int_A^B exp(-itE)B'(E)dE.

Taking operator norms proves the target's inequality for t not zero. Both hard endpoints remain. The scalar factor `exp[-it(c_att+2j+e)]` after changing E to delta has unit modulus, but is still the actual phase in the integral; no replacement of physical old aging or common phase is involved.

## 3. Product rule, endpoints and all multiplicities

Put `r_delta=sqrt(delta^2+lambda^2)`, `a1 a2=c_a lambda^2`, `c_a=2sqrt(2)/3`, and `c=(1-Theta)s`. The nominal full inverse envelope is

    ||Q^-1||<=1/(c r_delta^3).

At the two endpoints of ONE lip and ONE window, (1) therefore contributes at most

    kappa * 2 c_a lambda^2 L0/[c(d^2+lambda^2)^(3/2)]. (2)

The coefficients kappa,a1,a2 are fixed physical parameters, so differentiating (1) yields only the two ordered factors

    B'=-kappa a1a2[L'Q^-1 V_seed+L(Q^-1 V_seed)'].

For the first term,

    int_-d^d r_delta^-3 ddelta
       =2d/[lambda^2 sqrt(d^2+lambda^2)]<=2/lambda^2,

so its integrated norm is at most `2 kappa c_a M_g/c`. For the second, the definition

    D3=a1a2 sup_(window,lip,sector)
                    int_-d^d ||(Q^-1 V_seed)'|| ddelta

gives the allowance `kappa L0 D3`. This is a supremum of separate integrals, not a sum that already paid windows or lips. The checked D3 proof differentiates the ordered inverse and includes two Neumann inverse factors in the perturbation term. It is not a derivative obtained from the value envelope or from the bare Markov cubic.

Thus ONE lip/window gives `kappa/|t|` times

    F=2 c_a lambda^2 L0/[c(d^2+lambda^2)^(3/2)]
                                  +2c_a M_g/c+L0 D3.

Stone contributes `1/(2pi)`. Adding its two lips by the triangle inequality gives `kappa F/(pi|t|)` for one physical window. Adding both physical windows gives

    ||represented background(t)||
       <=2kappa F/(pi|t|).                            (3)

This reproduces the target's formula (5), including both hard edges. No assumption that the lower ordered Q equals the upper Q adjoint is needed; each lip uses its own valid bound. Nor are errors from e=1 and e=3 assumed orthogonal.

Within each invariant parity/record-X block the bounds already apply to the complete prepared input domain. Taking the orthogonal sector direct sum gives a maximum, not a new factor. The fixed initially prepared record0 inclusion has normalized sector weights and norm one. Arbitrary passive references tensor every bounded operator with the identity and preserve the result. No dimension or extra square-root-two factor is missing.

The separate complementary-input D3_C estimate is not another summand: D3 already covers the full V_seed, including induced selected output from wrong-window input. Adding D3_C again would double count that allowance.

The absolute integral gives `4c_a kappa L0/(pi c)=8sqrt(2)kappa L0/(3pi c)` for the SAME two-window represented map. Therefore taking its minimum with (3) is legitimate. Neither expression includes the three source heads or the propagating ray.

## 4. Reconstructed arithmetic at the existing nominal point

The evaluated parameters are only

    lambda=1e-13, g=5e-8, h=4e-6, T=2e14,
    .0027<j<.003, kappa^2=3jlambda.

They lie in the checked background and nominal-source domains. In particular `2.15e-8<d=2j sin h<2.4e-8` and `d/g<.48<.5`; `0<lambda<=1e-8` and `0<g<=1e-6`. No one-site emitter's kappa restriction is transferred to this different three-site source. The background itself is emitter-free.

The existing envelope slope is

    b=46000/.0053+290/g<5.81e9,

and `a=8e-18`. Since `kappa^2<9e-16`,

    kappa^2 b<5.229e-6,
    6 kappa^2(a+bd)<7.54e-13.

Also `s=sqrt(1-3lambda/j)>.9999999999`. Hence the nominal, sharper criterion indeed gives

    Theta<5.24e-6,
    n<1.00000525, c>.9999947,
    kappa<3e-8.

The existing full derivative is sufficient:

    M_g<1.00068*(7.29e16+6.62e14)+30<7.37e16.

For the checked D3 expression (13), `A_s=2/s+6.01/s^2<8.011` and

    Z_g=2e8+17000/g=3.402e11.

Using `pi<22/7`, the leading bracket is below9.445. The three remaining terms obey

    A_s(4a/3+2b lambda/3)<.003104,
    400a lambda^2+400b lambda^3<3e-27,
    Z_g[pi lambda/(2s)+12lambda^2]<.05347.

The first estimate is close enough to warrant retaining the actual arithmetic: `8.011*(2*5.81e9*1e-13/3)` is below `.003102928`, and the a term is negligible at this displayed margin. The Z_g leading estimate using22/7 is `.05346` before its tiny s and lambda-squared allowances. The prefactor satisfies `3j n^2/s<.0090001`, so the combined correction is below

    .0090001*(.003104+.05347+3e-27)<.00051.

Thus, with `c_a<.944`,

    D3<.944*(9.445+.00051)/lambda<9e13.               (4)

This uses the actual background derivative contribution in D3; it is not the bare reference value alone. It retains the nonzero calibration floor a and the nominal full inverse margin.

The three contributions to F in (3) can now be bounded separately. For the endpoint term, `d^3>(2.15e-8)^3>9.93e-24` yields

    2c_a lambda^2 L0/[c(d^2+lambda^2)^(3/2)]<27.

For the recovery derivative term,

    2c_a M_g/c<2*.944*7.37e16/.9999947<1.392e17.

For the prepared inverse derivative term, (4) gives

    L0 D3<14000*9e13=1.26e18.

Their sum is below `1.4e18`; the small endpoint allowance fits easily in the remaining slack. Finally `pi>3.14` gives

    2kappa F/(pi T)
       <6e-8*1.4e18/(3.14*2e14)
       <.000133758<.000134.                           (5)

The same fixed parameters and endpoint allowances give (5) multiplied by `T/|t|` for `|t|>=T`, in particular throughout `[T,2T]`. The earlier absolute component ceiling was `.000505` at these parameters, and `.000505/.000134>3.7`. This compares two conditional upper bounds, not measured amplitudes or an established improvement in the complete device. No new hardware point, optimization or sweep is involved.

## 5. What the result can support

The represented background is the sum of the two projected window integrals in the common physical Hilbert space. A complete-state decomposition must add the separately controlled represented source heads and traveling components, plus the ACTUAL outside-window vector once. The latter can include point spectrum. Nothing in this IBP calculation bounds it, identifies it with reference omitted mass, or justifies charging it separately in several spatial components.

For a background-only residual estimate it is conservative to allocate the full omitted vector to that residual, or apply a specified contractive physical projection to it. This does not mean that every omitted component physically occupies the background, nor does it change the two-window definition above. A full spatial synthesis should state its allocation explicitly and avoid double counting.

The `1/|t|` conclusion is for this represented portion of the actual infinite apparatus with fixed positive band and nominal source parameters. It is not a bound on all later evolution of a capped receiver: finite returns and recurrences remain possible. The cap comparison, finite observation interval and resource inventory still require their own proof. Source-local escape, incoming and outgoing profiles, physical waveform normalization, literal old K/W action and common phase are untouched dependencies of any complete-output theorem.

The result is also restricted to nominal `Delta=0` and the stated critical source ratios. Common offsets, residual detunings or generic coefficient errors are not handled by renaming delta. Varying g or lambda changes M_g,D3,c and the endpoints and requires reevaluating the whole expression. Neither the new selected-only converter derivative nor the separate mediated program-cell model is a premise here.

## Exposure, exact sources and verification limits

I authored the underlying prepared-core recovery proposal and the earlier large receiver point. Their value/derivative conclusions are reused through the distinct dwell and composition checks, not presented as newly independent proof by their author. The composition check's original pending-dwell label remains historical; the separately supplied dwell check is the explicit matching premise. I did not author this IBP proposal or the new D3 source. Root supplied the target and identified the already checked D3 dependency.

I read the complete IBP target, complete D3 source and check, complete loaded-inverse source and check, complete wide-derivative source and check, and the complete prepared-core composition review. The prepared-core full-forcing, derivative, absolute-Stone and prior IBP-interface sections were refreshed. The unchanged dwell source/check had already been read fully and were reused at their verified identities. The new calculation here reconstructs the fixed output-space embedding, product rule, endpoint and multiplicity factors, and the stated-point arithmetic; it does not recalibrate or audit all ancestors.

| Source relative to the renewal directory | SHA256 |
|---|---|
| prepared_background_ibp/PROPOSAL.md | 90d42e3699496e7694ddda630672af778a506b795865118757ab1e57da4a9c5a |
| three_site_prepared_inverse_derivative/PROPOSAL.md | 25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84 |
| three_site_prepared_inverse_derivative_check/REVIEW.md | 3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c |
| prepared_core_recovery/PROPOSAL.md | cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9 |
| prepared_core_dwell_check/REVIEW.md | 88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819 |
| prepared_core_composition_check/REVIEW.md | 52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
| slow_lead_wide_derivative/PROPOSAL.md | c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a |
| slow_lead_wide_derivative_check/REVIEW.md | c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79 |

All ten identities were verified from actual bytes. The mathematics and arithmetic above were reconstructed analytically. No numerical integration, scientific source execution, dynamics, inverse experiment or sweep occurred. Only this review was created; no original source, W, Git, PR, checkpoint, editable prompt, axiom, model setting or other deliverable changed. This is a source-exposed same-model distinct composition check with shared ancestry, not blind review, native validation or retained audit status.
