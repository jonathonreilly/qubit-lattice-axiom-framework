# Native low-density structural and coherence discriminator

Frozen before numerical/local-word checks, 2026-09-30 approximately 03:31 UTC.
This is a discovery contract, not an assumed result, independent receipt or
axiom adoption. Only this directory is writable. Original campaign deadline
2026-09-30T22:41:00.557005+00:00 and STOP_REQUESTED remain binding.

## Exact model and source

Use the actual M2-site Hamiltonian H0, bare d_i/v_ij^(s,t), collective
Q_E1,Q_E2,Q_Tij, V3 and Wtau of current main
30a9461ee19a49b99fa6628fe942f08e504e8903,
docs/NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md.
No coefficient, occupation basis, hard-core rule or pair Gram is changed.
Tori are cubic L>=5, mu,tau>0, and a=min(tau,mu/12). The supplied quantum
state/expectation interpretation and law are not inferred from M2 alone.

Read the complete current density source, full frozen N4 threshold report
9030dd11..., independent threshold check730d47f5..., root positivity
extension5b795a11..., and its independent checkbe619cf.... The strict
fifteen-channel threshold form is provisional checked input; it is neither
a dilute-gas theorem nor a replacement for the many-particle carrier.

Closest main sources inspected: the density theorem; native RK charge
stability (a different edge carrier and law); the full moving-record
neutral-scale correlation note (classical vacancy Gibbs law, with explicit
conditional high-density imports); the supplied free-Fock occupancy note
(its pair coherence is a two-sector phase example, not this interacting law).
Targeted current-main searches for dilute/condensation/pair-coherence and
composite-boson terms found no version of the proposed all-N local pin bound.
Current open-PR metadata contains only draft9008c2f56b72 on an ice covariance
diagnostic, not this Hamiltonian. No broad historical novelty is asserted.

## Primary target: test/prove full-carrier short-pin estimates

For Egrad equal to the sum of all fifteen bare-pair nearest-center gradient
norms, seek an all-state, all-volume estimate

    V3 <=24 mu Egrad.

The proposed mechanism is explicit. In an ordered local triple
(x,x+d,x+e), d,e in the eighteen-neighbor set, d!=e, choose a literal bare
pair B_t(c) with endpoints x,x+d. The residual occupation x+e makes the
output of B_t(c+e) vanish. Since every e has l1 length two, telescope along
two nearest-center steps, apply Cauchy-Schwarz, retain the residual projector
until after the norm inequality, and count every translated path.

If valid, combine it with the ACTUAL SOS/gradient comparison to control the
diagonal number O of particles outside isolated two-vertex components of
the induced eighteen-neighbor occupation graph. Candidate bound:

    O <=72 H0/a.

O is a local diagonal observable, not a projection onto fictitious pair
bosons. Test consequences for arbitrary N, in particular a closed-sector
compression bound and the limitation of using that absolute gap at an
extensive many-body energy.

## Pair coherence and algebra, without assuming a condensate

Use R=(Q_E1,Q_E2,Q_T12/sqrt2,Q_T13/sqrt2,Q_T23/sqrt2), the actual zero-momentum
Gram normalization. For arbitrary states let rho=<N>/V and e=<H0>/V. Seek
quantitative bounds on

    C(r)=V^-1 sum_(x,A)<R_A(x+r)^dagger R_A(x)>,
    Gamma_AB(k)=<Rhat_A(k)^dagger Rhat_B(k)>,

using only the exact energy identity and Wtau, followed by the ground-state
condition e<=nu rho for Hnu=H0-nu N. Target a diverging finite coherence
distance of order nu^(-1/2), not nonzero order as r->infinity at fixed nu.

A separate operator-algebra approach will test the actual pair commutators:
their vacuum Gram is diag(1,1,S12(k)/2,S13(k)/2,S23(k)/2), Sij=1+cos ki cos kj.
Seek a state-dependent O(rho) expectation error for a fixed finite selection
of normalized Fourier components. No uniform full-Fock CCR, bosonic
replacement, condensate fraction or SO3 identification is presumed.

## Distinct harder approaches and honest terminal gaps

1. Local hard-core/SOS pins: prove or refute the all-N bounds above.
2. Pair-algebra/positive correlation matrices: establish only the coherence
   and approximate-commutator statements actually justified by them.
3. Many-body pair-channel elimination: determine precisely why the checked
   N4 threshold form does or does not fix the leading thermodynamic energy
   coefficient. Price the N-dependent resolvent and physical matching Gram;
   do not call a uniform absolute closed gap a relative many-body gap.
4. A simple occupation-basis Perron-Frobenius route: test actual sign-cycle
   invariants before importing positivity/ordering conclusions. Failure of
   that particular diagonal sign gauge is not a phase no-go or an exclusion
   of more general positivity/reflection methods.

The desired output is a real full-carrier low-density discriminator and an
exact statement of the remaining leading-energy/condensation lemma. A
candidate energy coefficient based on T0 must retain identical-pair factors
and cannot be asserted without a many-body error estimate and polarization
argument. No pulse quartic is relabeled as scattering.

## Verification/resource contract

Analytic all-N proof is primary. A single small exact local-word job may
check all306 ordered neighbor pairs, L=5 alias geometry, the translated
gradient multiplicities, hard-core commutators and any sign-cycle witness.
Each local support has at most six sites (at most64 occupation words);
enumerate sparse bit actions, not a dense torus or phase diagram. Price:
<=60 CPU seconds, <=150 MB, BLAS/OpenMP1, <=180 wall seconds. One other
graph build is active globally; this is the only compute job planned here.
New load-bearing lemmas require a focused independent check before extensive
downstream reuse. No formal review, audit, PR, commit or shared-file edit.
