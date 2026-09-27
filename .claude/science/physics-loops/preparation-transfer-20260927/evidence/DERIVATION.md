# Conditional preparation-to-observation chain

Assume three states0,1,2 with nonnegative, time-independent downward rates k10,k21,k20 and no upward jumps. The populations obey

    du2/dt = -(k21+k20)u2,
    du1/dt = -k10 u1 + k21 u2,
    du0/dt = k10 u1 + k20 u2.

This is an imported classical Markov generator, also the population sector of the canonical Lindblad equation with jump operators sqrt(kij)|j><i| under a diagonal free Hamiltonian. No native framework derivation of this law or its rates is claimed. Columns of the population generator sum to zero, and off-diagonal rates are nonnegative, preserving normalized nonnegative initial populations.

Put lambda=k21+k20 and

    F(t) = [exp(-k10*t)-exp(-lambda*t)]/(lambda-k10),

with continuous limit t exp(-k10*t) at equality. Direct integration gives u2(t)=u2(0)exp(-lambda*t) and u1(t)=u1(0)exp(-k10*t)+k21 u2(0)F(t). This formula and its continuous limit determine all three populations through u0=1-u1-u2. It includes vanishing rates without dividing by a physical transition rate.

For the nominal calibration preparation |2>, the predicted population vector is

    [1-exp(-lambda*t)-k21*F(t), k21*F(t), exp(-lambda*t)].

For target preparation with equal populations in1 and2, linearity of the generator yields

    Pexc(t) = u1(t)+u2(t)
            = [exp(-k10*t)+exp(-lambda*t)+k21*F(t)]/2.

Neither a frequency nor a coherence-decay coefficient enters this quantity. A coherent equal superposition and an incoherent equal mixture produce the same Pexc. For any final unitary U that leaves|0> separate and mixes only states1,2, U commutes with projector Pexc=|1><1|+|2><2|. Cyclicity of the trace proves Tr(Pexc U rho U†)=Tr(Pexc rho). Thus final within12 pulse-angle error alone does not alter the proposed sum. Loss, leakage or relaxation during the pulse and inaccurate initial populations are additional physical effects outside this identity.

Readout is supplied as an affine calibration: measured two-dimensional I/Q vector y equals p0*c0+p1*c1+p2*c2 with p0+p1+p2=1, where c0,c1,c2 are the three recorded reference centroids. If D=[c1-c0,c2-c0] is invertible, then (p1,p2)=D^-1(y-c0), and p0=1-p1-p2. This inversion establishes an observation convention; it does not prove the reference pulses prepared pure states. Noise and model error can produce estimates outside the probability simplex. Those observations are retained without clipping.

The empirical construction fixes rates from the separate |2> calibration, then predicts the entire target Pexc array before reading target amplitudes. Source-semantic reference masks, time units, state convention, exact acquisition identities and fit bounds are frozen. Equality of the recorded fields/readout settings is not proof of rate stability across the10h42m02s gap. No target offsets, population rescaling, initial-state fitting or rate refitting is used. All starts and the later sequential-only ablation remain in the record.

This exact conditional construction explains what was predicted and why. The observed residual is a test of the supplied rate/preparation/readout transfer, not a proof of those assumptions, a coherence test, a unique model selection or a TOE confirmation.
