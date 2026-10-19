# Input-independent observation-time mixtures preserve the controlled router

New bounded operational corollary requiring a distinct check. ROOT suggested averaging the uniform time-indexed output theorem over an input-independent observation-time distribution. The derivation below establishes that channel statement, conditional on the pinned uniform-window theorem. It retains all physical outputs and does not create a stopping, capture or reset mechanism.

## Fixed spaces and premise

Use the fixed finite Hamiltonian H_phys, seed isometry E_seed, legal encoded input space L=H_program tensor H_path, and controlled unitary

    C=P0 tensor X+P1 tensor I

from the exact composition source 3a195efc and the window source 1ea1943e. Let R_rad be the finite radial space spanned by n=0,...,ell. There is ONE time-independent output isometry

    J_out: R_rad tensor L -> H_phys,out.

It sends |n> tensor |p,r> to the physical one-head position (r,n), with legal program |ppp>, both emitters vacant, mediator vacant, and all remaining head qubits vacant. Its image is a subspace of the full physical output Hilbert space. This is a fixed encoded tensor factorization, not an assertion that one head's radial and path coordinates are separate physical qubits. All states outside that image remain present in the actual output comparison.

Write V_t=exp(-itH_phys)E_seed and define the target isometry

    W_t xi=exp(-i2bt)J_out(beta_F(t) tensor Cxi).

On the same fixed interval I=[tminus,tplus], adopt the uniform-window premise

    sup_(t in I)||V_t-W_t|| <= E_window,
    E_window=min{2,e_C+e0+e_B+2d_L+2d_O}.          (1)

Its exact phase, cutoff, positive normalization and quantitative hypotheses are those of source 1ea1943e. In particular d_L<1, d_O<1 and

    ||P_(0<=n<=ell)B_packet(t)||
                  >=(1-d_L)sqrt(1-d_O^2)>0

on the whole interval. Thus beta_F(t) is a unit vector continuous in t, with a common definition independent of the logical input. All its translation, scattering and dispersive phases are retained. The same isometry estimate tensors with any passive reference. No time-dependent relabeling, decoder or choice of output factorization is allowed in (1).

The complete finite composition has a recorded distinct check. The separate uniform-window source is used at its stated provisional status; this note does not silently upgrade that status or independently re-prove its endpoint error bounds.

## Arbitrary classical timing distribution and exact ideal mixture

Let mu be any Borel probability measure on I, chosen independently of the logical input and any passive reference. It may be continuous, discrete, singular or a mixture; no density or moment assumption is required. Define the actual full-output channel

    Phi_mu(rho)=integral_I V_t rho V_t* dmu(t).     (2)

This is the ensemble channel for classically selecting an observation time with that law, evolving the same initial encoded state under the same Hamiltonian, and not retaining the selected time as an output label. It does not describe coherent control of evolution times. Because the physical device is finite, V_t is norm-continuous; all displayed matrix-valued integrals exist and (2) is completely positive and trace preserving.

Define the common radial density matrix

    sigma_mu=integral_I |beta_F(t)><beta_F(t)| dmu(t). (3)

Continuity and unit normalization give sigma_mu>=0 and Tr sigma_mu=1. It depends on the device, cutoff, window and mu, but not on rho. It need not be pure. The exact averaged target channel is

    Psi_mu(rho)
      =integral_I W_t rho W_t* dmu(t)
      =J_out[sigma_mu tensor C rho C*]J_out*.      (4)

The common scalar exp(-i2bt) cancels within each rank-one channel term. This cancellation is legitimate for the classical density-matrix mixture, not a deletion of the scalar from the fixed-phase vector theorem. Likewise (3) uses the actual time-indexed packets; no incoherent replacement by a fixed vector or fitted phase is made. The packet may spread or change phase across the interval, and its full mixed density matrix remains in the output.

For an arbitrary input rho_LR entangled with a passive reference R, the exact target is

    (Psi_mu tensor Id_R)(rho_LR)
      =(J_out tensor I_R)
       [sigma_mu tensor (C tensor I_R)rho_LR(C* tensor I_R)]
       (J_out* tensor I_R),                       (5)

with the canonical tensor ordering understood. Thus the ideal radial mixture is independent of the entire logical/reference joint state. The encoded program coherence and the path/reference coherence are preserved by the same controlled unitary. Averaging does not dephase the logical program merely because the outgoing spatial packet varies with time: that packet is common to all legal logical inputs at each time.

## Unhalved complete-output diamond bound

For any auxiliary reference and any trace-class operator X on logical input plus reference,

    V_t X V_t* - W_t X W_t*
       =(V_t-W_t)X V_t*+W_t X(V_t*-W_t*),

where identity factors on the reference are suppressed. Since both V_t and W_t are isometries, Schatten-norm submultiplicativity gives

    ||V_t X V_t* - W_t X W_t*||_1
                   <=2||V_t-W_t|| ||X||_1.        (6)

Integrating (6), using the trace-norm triangle inequality and that the SAME mu is used for every input, proves

    ||Phi_mu-Psi_mu||_diamond
                <=min{2,2E_window}.               (7)

The cap two is the universal unhalved distance ceiling for channels. Thus every normalized input, with arbitrary passive reference entanglement, obeys the same unhalved full-output trace-distance bound. If finer measurable pointwise isometry bounds e(t) are available, the same proof gives the optional refinement min{2,2 integral e(t)dmu(t)}; (7) needs only (1).

No actual mediator, emitter, program, lead or reference coordinate is discarded to obtain (7). The ideal density matrix lies in the fixed J_out image, with both emitters and mediator vacant; actual population and coherences outside that subspace are included in the trace/diamond error. Only the external classical observation-time label is omitted in defining the requested mixture (2). No physical time register is posited or erased by the theorem.

The target factorization in (4) is stronger than a logical reduced-state claim, but it applies through the fixed output isometry. One must not assert literal tensor independence of arbitrary groups of physical site qubits: the one-head radial/path encoding itself distributes amplitudes across sites. If a mathematical channel later extracts the encoded logical output, contractivity preserves (7), but no physical decoder or readout mechanism is supplied here.

## Scope of timing robustness

The bound is uniform over all input-independent mu supported on the certified interval. No knowledge of its shape is needed to retain the controlled logical operation and the error ceiling. However the full apparatus target sigma_mu generally depends on mu. This result does not provide one fixed radial density matrix that works for every unknown distribution without an additional comparison between those matrices.

Input-dependent or input-correlated timing is outside the product-target statement. A distribution conditioned on a logical label can correlate that label with the radial packet, and timing selected by measuring a coherent program can alter its coherence. Such a process is not represented by one fixed input-independent channel (2) with target (4). The independence premise also excludes a timing variable correlated with an otherwise passive reference.

A coherent superposition or coherent control of evolution times is a different model. Its amplitudes can carry cross-time interference and the phase exp(-i2bt); they cannot be derived by replacing probabilities in (2) with amplitudes. A specified time-control register and its complete dynamics/output would require their own comparison. No universal obstruction to such a separate construction is asserted.

The observation interval and a classical ensemble description do not halt the Hamiltonian. If all runs are instead allowed to evolve to a later common wall-clock time, the channel at that time is a different object unless the actual measurement, stopping or storage process is supplied. Nothing here freezes beta_F(t), captures the head, resets the device, produces a permanent Record, or establishes all-late validity. Finite-device returns remain possible outside the certified interval.

## Provenance and verification limits

Exact sources read and identity-checked for this task:

* common_product_finite_window/PROPOSAL.md — 1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b. Its uniform estimate (8), continuous positive-normalized target and fixed output injection are the scientific premise here. Its historical statements that the composition review was pending are superseded only by the separately read completed review below; the window itself is not thereby independently checked.
* common_product_finite_seed_router_check/REVIEW.md — 5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9. It supports the exact complete composition at its stated scope.
* common_product_finite_seed_router/PROPOSAL.md — 3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b. This source was authored and fully read in the preceding task; its fixed seed/output encoding and full-output conventions are reused, not independently checked here.

ROOT suggested the timing-mixture question and expected the convexity route. I derived the fixed-encoding density factorization, measurable arbitrary-probability mixture and reference-uniform trace/diamond estimate above as author work with that exposure. The decisive distinct-check obligations are the input-independent measure premise, fixed output tensor embedding, normalization/measurability, cancellation only within classical channel terms, and preservation of all physical outputs. No native supplier, timing controller, capture mechanism or old literal processor theorem is imported.

Only common_product_finite_window/TIMING_MIXTURE.md was created. No scientific executable, simulation, numerical integration, symbolic solver, sweep, canonical/W/Git/PR/checkpoint/editable-prompt/model change or delegation occurred. No retained status or independent acceptance is assigned.
