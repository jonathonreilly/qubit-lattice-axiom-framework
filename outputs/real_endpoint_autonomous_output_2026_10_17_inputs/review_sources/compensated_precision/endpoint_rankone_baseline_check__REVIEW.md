# Structured endpoint block with fixed baseline: bounded review

Scope: section 3's orientation-only block with gamma=1 and fixed emitter baseline, including its fixed-nominal full-output implication. The original source's full-qubit matching assertion is false. Replacing its |11> coefficient (1-t)^2 by (1+t^2) repairs that assertion and makes the replacement exactly equal to the previously checked compensated endpoint on the entire two-qubit space. The corrected ratio and complete .000347/.001347 implication are supported as detailed below. Final corrected-source identity is recorded in the addendum below.

## Exposure and source control

Original proposal read fully: endpoint_structural_precision/PROPOSAL.md, SHA256 c29243e8f2efd52865d591858dca38ac8a8bee352f29278de9f46b63002d8717. Root identified the |11> defect before this review; I independently reconstructed it below. This is not a blind discovery of that defect. The other proposal sections were visible but their fixed-spectrum and gamma-scaling constructions are outside the accepted scope.

The controlling canonical argument previously read in full is the note at SHA256 bc75051b87d62e65ea7953f11c2fcd320f1a9ab853c7a346f32e9314859cb1a5. The positive-contract proposal and my review are respectively 233364359dc3e79b54debf331eb75e6454f093cdbec36c36e1ba4fe17acc1381 and 40f7649071bc0eeb192a7832c64510c4185d39d31b6c27e9064a77fd5fa6a5f5. I authored the older weighted-profile proposal and reviewed several reused components, and later drafted the positive publication section. This is an independent reconstruction of the new local-block reduction and ratio bound, not an additional independent origin of the reused full-device precision theorem.

During this check the editable canonical note hash was bdd1e8ab42bf472a9f75c01e598c15857f0e383a09f06b80f8cfd59b8ab0a39e. I selectively refreshed its unchanged Q definition at lines 605–606, not its entire new appendix. This report does not certify that concurrent integration. No scientific execution, numerical spectrum, quadrature, W/Git/PR/checkpoint/prompt edit, new agent or model/effort change occurred.

## 1. Original full-qubit failure and exact repair

Canonical Q(-kappa)=kappa(n_e+n_end)-kappa(a_e* a_end+a_end* a_e) has |11> eigenvalue 2kappa. Adding its two compensations gives the complete local diagonal on |11> equal to

    2kappa+(E0-kappa)+(J-kappa)=E0+J.

The original candidate instead gives e_base+J(1-t0)^2=E0+J-2kappa0. Thus its claimed nominal full-block equality misses 2kappa0=2e-8 on |11>. Positivity and correct one-head entries do not cure a false full-qubit equality. The failure must remain recorded even though the delivered one-head sector would not visit this state.

For the corrected candidate define

    e_base=E0-alpha0>0, t0=kappa0/J, chi_t=t|10>-|01>,
    B(t)=e_base n_e+J[|chi_t><chi_t|+(1+t^2)|11><11|].

Both summands are positive for real t, real, number conserving and supported on the same adjacent qubits. The first-excitation determinant is e_base J>0 and its trace is positive. The complete block is zero on |00>, has matrix [[e_base+Jt^2,-Jt],[-Jt,J]] on (|10>,|01>), and eigenvalue e_base+J(1+t^2) on |11>. At t0 these entries are exactly the original full block, including E0+J on |11>.

Only the |chi_t> projector is rank one in the one-excitation sector; the complete local block is not rank one. Its positive fixed baseline is essential and remains supplied.

## 2. Exact reduction to the compensated contract

For t=r t0>0 set kappa_a=Jt=r kappa0 and Delta=Jt^2-alpha0=(r^2-1)alpha0. On every two-qubit state, not merely after projection,

    B(t)=Q(-kappa_a)+(E0+Delta-kappa_a)n_e
                              +(J-kappa_a)n_end.

The |11> entry on either side is E0+Delta+J. The off-diagonal element is -kappa_a, the one-head diagonals are E0+Delta and J, and the |00> entry is zero. This proves the exact full-operator identity. The remaining endpoint bond supplies the other J, so the pre-emitter background remains exactly unchanged. Old/source terms, c_new, lead, reference planes, seed and graph are unchanged as required by the positive contract.

For r in [1-4e-6,1], |r-1|<=4e-6<1e-5 and |r^2-1|<=8e-6<1e-5. Thus |Delta|<=8e-6 alpha0 falls inside that contract at every point, with the correct negative sign for Delta when r<1. The complete real spectrum, shifted mass interval, Schur/closed-tail and scalar contour bounds therefore transfer by exact operator equality and inclusion of parameter domains. No new background estimate or continuity assumption is substituted.

This conclusion fixes gamma=1 and e_base at its nominal value. Errors of the baseline or independent strength changes are not covered. There is no assertion about a supplier that naturally enforces this direction.

## 3. Exact complex ratio and sharper fixed-target difference

With x=E-E0 and z=exp(ik), substitution of the actual Delta gives

    Da=x-(r^2-1)alpha0+r^2alpha0 z
       =D0+(r^2-1)alpha0(z-1),
    Fa/F0=rD0/Da.

The numerator phases z^21 rho_g are identical and have not been discarded from either profile. On the original small positive band,

    |z-1|/sin k=1/cos(k/2)<1.1.

This follows at the stated k0 and sigma: tan(k0/2)=1/4.510351185997098<1/4.5, and the half-band extension 5e-7 leaves cos(k/2) comfortably above 1/1.1. No uncertain phase or global Lorentzian approximation is involved.

Consequently eta_r=1.1|r^2-1|<8.8e-6 and

    |Fa/F0-1|<=(|r-1|+eta_r)/(1-eta_r).

At r=1 the left side is zero; a non-strict inequality with the exact eta_r expression is the universally safe formulation if writing a single line that includes r=1. The strict numerical ceiling below remains valid at r=1. The normalized complex-profile comparison is

    ||fa-f0||<=2(|r-1|+eta_r)/(1-eta_r)
              <=2*(4e-6+8.8e-6)/(1-8.8e-6)
              <.000026.

Positive normalization costs at most the initial unnormalized coefficient difference a second time. No reciprocal loss, arbitrary phase optimization or old-column aggregation enters this common scalar-profile bound. At the exact nominal endpoint, both normalized profiles coincide.

## 4. Full-output consequence and limits

The positive contract supplies actual-to-own-waveform operator error <.000320 for all t>=T=4e21, actual and nominal negative-tail norms <1e-10, and finite error <.001320 for the fixed M=2e23 device on [T,2T]. Use the sharper .000026 profile comparison just proved instead of that contract's coarse .000171 comparison. Fourier evolution and half-line restriction are contractions; positive target normalization adds at most q_a^2+q_0^2<2e-20. Hence

    infinite fixed-nominal error<.000320+.000026+2e-20<.000347,
    finite fixed-nominal error<.001320+.000026+2e-20<.001347.

All actual exterior spectral mass, emitter/core/source/closed-tail outputs, complex phase, c_new and full elapsed old aging remain included. Arbitrary passive references are covered by the inherited operator bounds. Finite comparison uses the same embedded infinite nominal target without finite-waveform renormalization; M+116 total qubits and the finite [T,2T] window are unchanged. These are sufficient conditional dimensionless model bounds, not measured resources or permanent finite storage.

No full-device result is inferred for the fixed-spectrum candidate or gamma variation. The fixed baseline remains an energy-precision-bearing supplied datum; generic local-block errors need not obey the orientation-only contract. The original |11> error and the strict-zero-endpoint issue above must be corrected or explicitly qualified in the accepted source. No retained/audit status is assigned.

## Corrected-source finalization

Received and hashed endpoint_structural_precision/CORRECTED_V2.md: d07e86f57b1247877e8f6abcc08efceaec18ac60c03b5cacce17ff178a7575b8. Read its complete diff against the fully read V1, and read the complete author correction record endpoint_structural_precision/CORRECTIONS.md: ee6df01851795fd3adfd4c693cd387299b5ae791271af90f757931e69db17eb2. V2 implements both required section-3 corrections exactly: (1+t^2) on |11> and the non-strict symbolic ratio inequality, with explicit zero-error endpoint treatment. The one-head formulas are unchanged. No remaining correction is requested for this scoped orientation-only contract.

The verdict applies to this V2 section-3 baseline/orientation result at fixed gamma=1, not its broader scaling subsection or section-4 fixed-spectrum full-device behavior. The original failed V1 identity remains frozen and is not retrospectively accepted. This report's earlier statement that the defects must be corrected is satisfied by the pinned V2.
