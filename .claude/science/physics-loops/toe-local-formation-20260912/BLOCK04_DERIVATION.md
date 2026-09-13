# Finite retained battery and collisions for the native feedback generator

Author derivation, 2026-09-13. Conditional-support; small author checks completed,
independent review pending. This extends an existing complete-law construction to its
explicitly excluded occupation-feedback law. It is not a new claim that finite
batteries or finite-time collision models exist in general.

## 1. Source target and supplied premises

The current-main local-quench/finite-ladder note dated2026-09-07 proves a
complete-law finite positive battery approximation. Its collision-apparatus
companion gives a finite-time unitary collision realization. Both were read
fully after the initial selected-source review. Their complete-law results
are prior art here. The occupation-feedback and ambient-erasure notes supply
the actual native seeds, head/fuel guards, energies and the non-scalar rate.

Keep the finite ambient Hamiltonian A=sum_e q_e(h_e+Delta), legal native
code, one head, original particle number, sharp old Records, full original
free Hamiltonian, and the same initially independent sine battery of widthw.
The cap[0,C] contains the exact invariant energy support. Let d be maximum
virtual degree, gamma the common supplied rate and Lambda=d gamma.
The finite feedback law has no eligibility refusal completion. All dark
and trapped mass belongs to its actual no-jump evolution.

No hopping coefficient, bath law, physical clock, battery routing, gate set,
fresh-site preparation or irreversible outcome-selection rule is derived
from the framework axioms. The result is a controlled finite apparatus
approximation under those supplied choices.

## 2. Spectral rounding preserves the correct feedback rate

Round the whole ambient spectrum to multiples of delta>0 with a fixed tie
rule and unchanged spectral projectors. Write A_delta=f_delta(A), so

    ||A-A_delta||<=delta/2,  [A,A_delta]=0.

For an eligible directed edge e, stack BOTH physical signs of its filtered
seed in a column B_e. On its source-head block ||B_e||<=1 and
B_e^dagger B_e=E_e n_v(1-n_w), which is not generally E_e. Its full-line
energy-dressed column V_e(tau) and rounded version W_e(tau) satisfy

    ||V_e(tau)-W_e(tau)||<=delta |tau|.              (1)

Both left and right spectral exponentials cost delta|tau|/2. Stacking signs
before bounding avoids treating them as independent errors. Summing at mostd
source-head edges gives the full jump-column estimate

    ||L(tau)-L_delta(tau)||<=sqrt(Lambda)delta|tau|,
    ||L(tau)||,||L_delta(tau)||<=sqrt(Lambda).        (2)

Compress the rounded jumps by the original cap and use their actual summed
loss. Whole spectral rounding retains fuel/head blocks, original N, old
Record guards and native code. The target rounded Hamiltonian still commutes
with the measured physical Z, so the sign-summed loss has the parent's code
invariance. There is no extra fair-sign factor at bridges and no artificial
identity-rate completion.

## 3. Capped feedback comparison on the exact safe reference

Apply Block3 Section10 to the rounded columns. The required common bound
controls both the input-column error and its adjoint acting on the exact
output. From(2), at exact reference time s it is

    e(s)=sqrt(Lambda)delta sqrt(pi^2/w^2+s^2).       (3)

The sine packet has Fourier second moment pi^2/w^2, by Parseval and direct
differentiation of the energy wavefunction. The exact unconditional Fourier
marginal translates bys and starts even. It therefore has the second moment
shown in(3), even after system-battery correlations develop. Exact cap safety
lets the same full-line estimates bound the capped input and adjoint terms.

The feedback recycling and non-scalar loss differences cost at most
6sqrt(Lambda)e(s) in trace norm on the exact reference state. Duhamel then
gives, through fixed modeled timeT,

    error_cap <=6Lambda delta T sqrt(pi^2/w^2+T^2). (4)

This compares complete unconditional channels with the battery retained and
arbitrary reference entanglement on the supplied input domain. It does not
presume that the rounded/capped process has the exact source's Fourier tail.
Nor does it control every normalized rare trajectory. The source's full
time-averaged and path-conditioned diagnostics remain distinct objects.

## 4. Finite cells and the same source packet

Take C=M delta and embed the positive ladder levels (j+1/2)delta as normalized
constant functions on[j delta,(j+1)delta). All rounded energy differences are
integer shifts. The aligned cap, rounded jumps and actual summed feedback loss
preserve the step-function subspace. So does its no-jump exponential. This
uses the real operator loss; replacing it by a degree scalar would change
the law being approximated.

Replacing only free battery energy by cell centers costs at mostdelta T in
retained trace norm, since the energy operators differ by at mostdelta/2.
Keep the ORIGINAL matter A in the free Hamiltonian. Project the original
sine packet to normalized cell averages beta_delta. Cellwise Poincare and
||beta'||=pi/w give ||(I-P_delta)beta||<=delta/w; the pure-state preparation
trace error is at most2delta/w. This input replacement is made after the
exact-safe-reference comparison, so it needs no new safety assertion.

The resulting positive finite battery feedback generator satisfies

    error_finite <=delta [2/w+T+
                     6Lambda T sqrt(pi^2/w^2+T^2)]. (5)

Its input is the system in the stated legal preparation domain with the
fixed battery attached, and its output includes that retained battery. A
bounded energy interval alone was infinite dimensional; the M-cell invariant
subspace is the actual finite-dimensional replacement. Unused qubit encoding
states can be extended inertly and trace preservingly, as in the parent.

## 5. Exact rounded energy and original mean energy

Let

    K=A_delta+E_delta,  F=A+E_delta.

Every rounded jump commutes with K; hence its GKSL dissipator preserves every
bounded function of K, including for the noncomplete feedback law. Since
A_delta is a spectral function of A, [F,K]=0. Original free matter evolution
therefore preserves the rounded energy too. There is no assumed commutation
of F with individual jumps.

For the aligned symmetric sine preparation, cell reflection preserves the
exact battery mean b+w/2 after projection and normalization. For every state
in the finite cell subspace, the embedded continuous battery mean equals
its cell-center mean. As ||F-K||=||A-A_delta||<=delta/2, exact K conservation
then implies the particularly simple modeled original-energy mean bound

    |<F>_T-<A+E_B>_(original input)|<=delta.         (6)

Both endpoints contribute at mostdelta/2. The equality of initial battery
means is essential here. For a different or unaligned packet, its actual
preparation mean error must be added. The parent has a more conservative
general endpoint certificate; equation(6) uses the present symmetric aligned
fixture, not an unexplained transfer of that certificate. This is a mean
bound, not exact conservation of the unrounded energy distribution.

## 6. Explicit finite collision extension

The parent's star-collision proof needs only a bounded jump column, not
an identity-rate instrument. Let the finite feedback jumps be J_a and
R=sum_a J_a^dagger J_a<=Lambda I on the one-head domain. Use a fresh ancilla
with basis|0>,|a> and zero label energies. Set

    B=sum_a J_a tensor |a><0|,
    V=B+B^dagger,  U_h=exp(-i sqrt(h)V).

With the ancilla initially|0>, the resulting Kraus operators are
cos(sqrt(hR)) and -i sqrt(h)J_a sinc(sqrt(hR)). The continuous value sinc(0)=1
keeps dark subspaces exactly. R is the actual feedback loss throughout.

Vacuum/nonvacuum ancilla parity removes odd powers ofsqrt(h) from the
reduced channel. Using ||V||^2=||R||<=Lambda and the exponential remainder
gives the parent's per-step dissipative error<=6h^2 Lambda^2 for hLambda<=1/4.
This construction is CPTP on all stated inputs, including reference
entanglement, and uses no postselection. Keeping and decoupling every used
ancilla is equivalent to tracing it for subsequent reduced dynamics; it
does not require resetting the same ancilla.

Every J_a commutes with K, hence [K tensor I,V]=0. Each collision conserves
the rounded energy distribution exactly. To include the original free F,
write D=F-K, ||D||<=delta/2. Its generator X=-i ad_F obeys

    ||[X,Diss]||_diamond<=4delta Lambda,

since the K part commutes with the dissipator. Positive-time Duhamel gives
Lie-splitting cost<=2delta Lambda h^2. Telescopingn collision/free steps,
h=T/n, yields

    error_collision <=(6Lambda^2+2delta Lambda)T^2/n,
    n>=4Lambda T.                                  (7)

No extensive ||A|| enters this error bound. A supplied pulse of modeled
durationh has interaction norm<=sqrt(Lambda/h). At bounded available strength,
the actual required pulse time changes; modeledT is not a derived physical
runtime. Fresh pure labels, pulse controls, clocks and spatial gate synthesis
remain explicit resources. A finite number of fresh ancillas does not give
an indefinitely reusable irreversible bath.

## 7. Concrete inherited cube resource choice

Keep the original feedback cube: gamma=J_*=Delta=1, d=3, sine[48,49],
cap[0,97], horizonT=1. Thus Lambda=3 andw=1. Since sqrt(pi^2+1)<10/3,
the bracket in(5) is less than63. Choose delta=1/1280. Then

    M=97*1280=124160 positive levels, requiring17qubits;
    storage=12native+12fuel+8head+17battery=49qubits;
    error_finite<63/1280.

Feedback has no refusal flag. At most24 oriented cube edges and two signs
give48 nonvacuum collision labels. Vacuum plus these fit in6fresh qubits
per collision. In(7),

    6Lambda^2+2delta Lambda=54+3/640,
    n=5401 gives error_collision<1/100,
    total storage and retained labels=49+6*5401=32455qubits.

The combined retained-channel trace-norm bound against the original supplied
continuous-battery feedback law is therefore

    error_total<63/1280+1/100=379/6400<0.06.        (8)

The original mean-energy bound(6) remains delta for the finite collision
model because both collisions and free steps conserve K exactly. The counts
are an analytic resource certificate, not a simulation of32455qubits and
not a claim that all the apparatus can be placed or controlled locally.

## 8. Required finite discriminator and interpretation

Check the rational resource arithmetic and a genuine native feedback
collision with [F,J]!=0, actual non-scalar R, all signs, battery retained,
and a zero-rate cap boundary. Compare its explicit star unitary plus
original free step with the complete GKSL evolution on a small finite state.
Such state-specific errors support the proof; they are not measured diamond
norms or evidence of sustained transport on the cube.

The completed check constructs a native square directly from physical Pauli
bit actions. It uses a cycle-code input and a separate input with an actual
old edge Record, deleting the irrational hopping sqrt(2)/3. Each fixture has
96system/battery dimensions and an explicit288-dimensional collision unitary.
Its actual original-free jump commutator norm is sqrt(2)/3, while rounded
energy commutation holds to matrix precision. The initial hazard is1/3;
the top battery cell is a genuine zero-rate boundary without a refusal jump.

At h=.04,.02,.01, the original-free one-step trace-norm errors are approximately
3.51154e-4,8.83373e-5,2.21532e-5, showing the predicted local h² scaling.
Using rounded matter energy in place of original free A produces much larger
errors, approximately .0264023,.0132670,.00665004. The two chosen legal-code
fixtures have the same effective selected-dimer dynamics and consequently
the same error values; they are not two independent proofs. The old-Record
fixture separately verifies its physical preservation conditions.

All100 predicates pass, including exact rational resource arithmetic and
the native matrix comparisons. Maximum equality residual is1.78e-15;
the runner reports~0.10seconds and79.75MiB peak RSS. The large finite
apparatus is not simulated. See BLOCK04_CHECKS.json and CHECK_NOTES.md.

This extends the apparatus approximation to the already specified feedback
law. It does not improve the source's unfavorable reach/transport census,
derive a formation law, or renew the consumed native edges. The next campaign
decision should assess those physical residuals and the native matter/gauge
frontier, not count the apparatus lemmas as independent TOE closures.
