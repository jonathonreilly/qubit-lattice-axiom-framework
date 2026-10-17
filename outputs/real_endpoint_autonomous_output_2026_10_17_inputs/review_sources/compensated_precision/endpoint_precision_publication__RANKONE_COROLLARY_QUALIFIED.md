### Structured positive-block corollary with a fixed emitter baseline

This corollary changes the supplied error-direction contract, not the graph, seed or runtime. Put t0=kappa0/J, alpha0=kappa0²/J and e_base=E0-alpha0>0. Supply on the adjacent emitter/endpoint qubits the real number-conserving positive block

    B(t)=e_base n_e+J[|chi_t><chi_t|+(1+t²)|11><11|],
    chi_t=t|10>-|01>,  t=r t0,  1-4e-6<=r<=1.

Its vacuum value is zero, its one-excitation matrix is [[e_base+Jt²,-Jt],[-Jt,J]], and its double-occupation value is e_base+J(1+t²). Thus on the entire two-qubit space it equals

    Q(-kappa_a)+(E0+Delta-kappa_a)n_e+(J-kappa_a)n_end,
    kappa_a=r kappa0, Delta=(r²-1)alpha0.

At r=1 it equals the original full local block, including the double-occupation value E0+J. The endpoint background remains exactly unchanged. For this range, |Delta|<8e-6 alpha0 and r is inside(P1), so every actual-device margin already checked above applies. No new scattering or runtime transfer is assumed.

The correlation gives a sharper fixed-target comparison. Exactly,

    Da=D0+(r²-1)alpha0(z-1), Fa/F0=rD0/Da.

Since |z-1|/sin(k)=1/cos(k/2)<1.1 on I, set eta_r=1.1|r²-1|<8.8e-6. Then

    |Fa/F0-1| <= (|r-1|+eta_r)/(1-eta_r),
    ||fa-f0|| <= 2(|r-1|+eta_r)/(1-eta_r)<.000026.

The non-strict intermediate inequality includes r=1, where its two sides vanish. Positive normalization and fixed complex phase use the same argument as(P2). Combining with actual-to-own-waveform error<.000320, both negative-tail normalization costs<1e-20 and unchanged finite transfer<.001 gives

    infinite complete operator error<.000347 for t>=4e21,
    finite complete operator error<.001347 on[4e21,8e21], M=2e23.

Unhalved trace ceilings are .000694 and .002694. The old evolution, scalar phase, all outputs and arbitrary passive references remain those in(P6)-(P7). An isometry-norm seed error again enters once.

This is a supplied fixed-baseline and structured-parameter contract. The positive baseline e_base and J remain exact; generic block scaling, baseline error and arbitrary independent matrix-entry errors are not covered. A relative t error of4e-6 is an absolute t error below1.34e-12. Supplying this direction does not establish a native mechanism that protects the baseline. The benefit is explicit quadratic correlation of emitter detuning with coupling, without retuning the baseline to the actual t.

The first structural proposal used (1-t)² in the |11> completion and incorrectly claimed full-block nominal equality. That would differ by -2kappa0 on |11>. The corrected1+t² restores the full operator identity; the original and correction record remain research provenance. Its fixed-spectrum alternative is not used in this corollary. The corrected source and this exact corollary were selectively checked in the reports identified below. These source-exposed checks are not blind review or formal audit.

Source identities: corrected structural proposal d07e86f57b1247877e8f6abcc08efceaec18ac60c03b5cacce17ff178a7575b8, correction record ee6df01851795fd3adfd4c693cd387299b5ae791271af90f757931e69db17eb2, scoped baseline review8bd60218b0200888ee7ab32fe6836ac2d1c64e4eac5f8a72fec3660b2fa46c11, integration review8e5d58e9bc9a5e6bb67cb91fb89b276d6c69c5b282e8ce11897f62691d24d65a. Root identified the full-space defect before the reviews; the correction was exposed. The baseline reviewer also reviewed the reused positive contract; the integration reviewer checked the complete appended positive section and the exact corrected corollary. Their coverage is selective and explicitly source-exposed. No fixed-spectrum or independently varying strength theorem is asserted.
