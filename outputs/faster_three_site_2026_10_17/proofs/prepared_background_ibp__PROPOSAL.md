# Actual prepared background: a complete two-window integration-by-parts bound

Status: new conditional author derivation requiring distinct checking. For the NOMINAL Delta=0 three-source device, the checked prepared inverse derivative and existing recovery derivative suffice to improve the represented background ceiling at the already studied point. No new hardware point or complete-device performance certificate is selected.

## Exact scope and assumptions

Retain the original calibration, physical graph, shared B/source vacuum, record/parity sectors, both physical old-energy windows I_e=c_att+2j+e+[-d,d], e=1,3, and both lips. Use the nominal source

    a1=lambda/sqrt(3), a2=lambda sqrt(8/3),
    kappa^2=3jlambda, Delta=0, r_i=e_i=0,
    c_a=2sqrt(2)/3, a1a2=c_a lambda^2.

The checked nominal full ordered denominator is Q, with reference Q0 and Neumann margin Theta<1. Put

    s=sqrt(1-3lambda/j), n=1/(1-Theta), c=(1-Theta)s,
    ||Q^-1(E)||<=1/[c(delta^2+lambda^2)^(3/2)].

The unchanged full-forcing physical recovery L(E) includes every one of the 235 finite background heads and all slow closed tails. It excludes the propagating open ray and the three new source heads. On each window and lip its checked values satisfy

    ||L||<=L0=14000,
    ||L'||<=M_g=1.00068*(7.29e16+3.31e7/g)+30.

All norms act on the full internal forcing fiber. Fixed inclusions V_seed retain selected and wrong-window prepared input columns. The prepared derivative source defines

    D3=a1a2 sup_(window,lip,sector)
                   integral_-d^d ||(Q^-1 V_seed)'|| ddelta,

and supplies its explicit finite bound (12), equivalently (13), at the pinned identity below. These are per-window suprema, not sums that have already paid both windows or lips.

The actual source-to-background resolvent column is exactly

    B_lip(E)=-kappa a1a2 L_lip(E)Q_lip(E)^-1 V_seed.     (1)

This uses the full noncommuting Q in its physical order. In particular a small scalar selected denominator is not the only input to this proof.

## Hilbert-valued Stone integration and endpoint terms

On each closed retained window, the inherited physical matching/root continuation and inverse margins give differentiable lip values of L and Q^-1. Closed-tail recovery is differentiable as a square-summable sequence: its geometric lift and derivative have the previously checked operator bounds. Thus (1) is an absolutely continuous operator-valued function into the fixed finite-plus-closed-tail output Hilbert space, with an integrable derivative. Fixed sector/projector bases and positive g are essential. No actual-source complex strip or continuation beyond the retained windows is assumed.

The represented background map is the two-window Stone integral of the jump of (1), with factor 1/(2pi i). For any t!=0, integration by parts on each lip separately gives

    || integral_A^B exp(-itE) B_lip(E) dE ||
      <= [||B_lip(A)||+||B_lip(B)||
                            +integral_A^B ||B_lip'(E)||dE]/|t|. (2)

The hard-cutoff endpoint values do not vanish and are paid explicitly. The physical E includes c_att and the old-energy center; their exponential factors have unit modulus, not a redefined phase or omitted aging. No assumption that the lower ordered Q is the adjoint of the upper Q is used.

At delta=+-d the two endpoint terms per lip are bounded by

    2kappa a1a2 L0/[c(d^2+lambda^2)^(3/2)].             (3)

Differentiating only the exact product in (1) gives

    B_lip'=-kappa a1a2[L' Q^-1 V_seed
                                      +L(Q^-1 V_seed)'].

No norm inequality is differentiated. The first derivative term integrates to at most

    kappa a1a2 M_g/c * integral_-d^d (delta^2+lambda^2)^(-3/2)
                          <=2kappa c_a M_g/c.           (4)

The second is at most kappa L0 D3. The full Q^-1 envelope and the full prepared D3 already include wrong-window input and any induced selected output. A separate complementary D3_C must not be added again.

Paying BOTH lips changes 1/(2pi) into 1/pi, and paying BOTH physical windows gives the final represented background bound

    B_IBP(t) = 2kappa/(pi|t|) * {
       2c_a lambda^2 L0/[c(d^2+lambda^2)^(3/2)]
                           +2c_a M_g/c+L0 D3 }.         (5)

Old-energy error images are not assumed orthogonal. Parity and conserved record-X sectors do combine orthogonally by maximum, retaining the normalized initial record0 weights. Passive reference extension preserves all operator bounds. There is no extra internal-dimension multiplier.

One may combine (5) with the checked absolute Stone estimate:

    ||represented background(t)||
      <=min{8sqrt(2)kappa L0/(3pi c), B_IBP(t)}.        (6)

The source heads and traveling directions are not part of (6). If bounding the untruncated background alone, adding a separately justified actual outside amplitude is safe. In a complete spatial synthesis, instead charge that actual outside vector ONCE globally. Nothing in (2)–(6) excludes outside atoms or replaces the actual seed-moment obligation. The scalar reference omitted mass is not relevant to this actual background integration.

## Existing nominal point: the old recovery derivative suffices

Evaluate only the already studied nominal point

    lambda=1e-13, g=5e-8, h=4e-6,
    T=2e14, .0027<j<.003.

These are the original device and band, not a parameter sweep or a retuned calibration. The emitter-free envelope has a=8e-18 and b<5.81e9, with 2.15e-8<d<2.4e-8. The sharper NOMINAL criterion gives

    Theta=(j a+kappa^2 b)/s+6kappa^2(a+bd)<5.24e-6,
    s>.9999999999, n<1.00000525, c>.9999947,
    kappa<3e-8, M_g<7.37e16.                           (7)

For example kappa^2 b<5.229e-6 and the complementary term is <7.54e-13. These nominal margins do not import the weaker perturbed/common-offset criterion.

The newly checked D3 expression can be bounded without numerical integration. With A_s=2/s+6.01/s^2<8.011 and Z_g=2e8+17000/g=3.402e11, its dimensionless bracket in equation (13) obeys:

    n*6.01*pi/(2s^2)<9.445,
    A_s(4a/3+2b lambda/3)<.003104,
    400a lambda^2+400b lambda^3<3e-27,
    Z_g(pi lambda/(2s)+12lambda^2)<.05347,
    (3j n^2/s)*(the last three terms)<.00051.

Here pi<22/7 suffices and c_a<.944. Therefore

    D3 < .944*(9.445+.00051)/lambda <9e13.             (8)

The coarse ceiling retains the small derivative of the actual background; it is not the bare Markov cubic derivative alone.

In the braces of (5), the three contributions satisfy

    boundary contribution <27,
    recovery derivative contribution <1.392e17,
    prepared inverse derivative contribution <1.26e18.

The boundary estimate uses d^3>(2.15e-8)^3>9.93e-24 and retains both physical hard edges. Their sum is <1.4e18. Using pi>3.14 now gives, for |t|>=T,

    B_IBP(t)<[6e-8/(3.14*2e14)]*(1.4e18)*(T/|t|)
             <.000134*(T/|t|).                        (9)

In particular the represented background is <.000134 throughout [T,2T], compared with the previous conservative absolute ceiling .000505 at this same point. This is more than a factor 3.7 reduction of that component's certified bound, not a measured improvement or a new device. The old checked M_g is already sufficient; a sharper full L' is unnecessary for this component improvement.

The derivative contribution L0 D3 dominates this particular bound. Its leading resonance scale is of order L0/lambda, so improving only M_g would not remove the principal remaining term. Equation (5) supplies a structural envelope for other parameters, but none are selected or evaluated here. When g,lambda or the margin vary, all corresponding M_g,D3,c and boundary terms must be recomputed; a fixed-g asymptotic slogan is not a parameter certificate.

## What this does and does not change

The result concerns the actual INFINITE apparatus's represented finite-plus-closed-tail background. It yields a 1/|t| component bound for this fixed positive-band problem; it is not an all-late-time finite-storage theorem. Finite caps can reflect and recur. A complete finite theorem still needs the separately checked three-source local contribution, both actual traveling coefficients and their scalar halfline/normalization bounds, one actual outside state and the exact finite-cut comparison over a stated time interval.

At the existing nominal point those other calculations are not modified by this derivation, but replacing a row in a published complete budget requires a distinct coherent integration check. No new complete error ceiling or runtime is asserted here. The bound does not apply to common offsets or residual source perturbations by relabeling delta: the D3 source is nominal and Delta=0. Supplied physical/calibration/preparation and native-interaction premises remain unchanged; no permanent halt, arbitrary noise tolerance or native supplier is established.

## Exact sources and exposure

- `three_site_prepared_inverse_derivative/PROPOSAL.md`: `25052bad1d500f52d4e4f4d3913f0bf8a0a57d69801688b7109a549ac3756d84`.
- `three_site_prepared_inverse_derivative_check/REVIEW.md`: `3a76d76895c01dcbd7cf7e5b566f7146ae683ddc4568352df06c19224e59aa1c`.
- `prepared_core_recovery/PROPOSAL.md`: `cce29994b7141df161ca12f377765fdaf760f7e64fc56043bbf370e2cd437ea9`.
- `prepared_core_dwell_check/REVIEW.md`: `88274b8b49e583bdb9b5f933f7406b1a96a6ca79049e57b83e8030c834d16819`.
- `prepared_core_composition_check/REVIEW.md`: `52edba6061be49eef40b5c06754a7425b5f7f62671f175cc72a093d4a60de65c`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
- `three_site_loaded_inverse_check/REVIEW.md`: `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`.
- `slow_lead_wide_derivative/PROPOSAL.md`: `c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a`.
- `slow_lead_wide_derivative_check/REVIEW.md`: `c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79`.

I checked but did not author the new D3 source. I previously checked parts of prepared-core recovery and have authored attachment/traveling/reference ancestors. The checked derivative/value passages of prepared_core_recovery were refreshed; the complete D3 source and necessary physical derivative/order premises were read in the immediately preceding check. Root requested this bounded synthesis and an honest evaluation of the existing point, not an improvement as an acceptance requirement. This is new author composition with shared ancestry, requiring a distinct check of endpoint terms, Hilbert-valued differentiation, window/lip factors and arithmetic. No numerical integration, dynamics, sweep, scientific runner, solver, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was written.
