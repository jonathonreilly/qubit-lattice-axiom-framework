# Real-axis broadened source Schur check

The proposed formula is algebraically correct for the explicitly specified real symmetric coefficient model and its leading fast source. Read `/private/tmp/neutral_corrected_fast_boundary.py` and `/private/tmp/neutral_slow_host.py`; this check does not upgrade their truncated coefficient content to the full microscopic diagnostic.

Set Jz=1, w=E-8, z=w/lambda, and e=w/lambda^2+4. The +4 compensates the slow block's common -4 diagonal; every slow host/arm function must use that same shifted energy convention. In the notation where R is the compressed resolvent of F at z and hSlow is the compressed slow resolvent at e, eliminating the slow block gives the fast physical resolvent

G_FF=R/lambda+R V [hSlow^(-1)-lambda V^T R V]^(-1) V^T R.

For j_F=-sqrt(2)lambda d, this yields exactly

G_C(E)=2lambda R_dd+2lambda^2 b^T [hSlow^(-1)-lambda V^T R V]^(-1)b,
b=V^T R d.

The factors are therefore 2lambda and 2lambda^2, with the Schur correction -lambda V^T R V. The transpose, not conjugate transpose of b, is required in the analytic expression: left and right resolvents are both R(z), not R(z) and R(z) dagger. The physical source itself is real in this basis.

With slow host h in coordinates A,D and an independent scalar arm endpoint resolvent g_s, coupling -1 to A produces

hSlow=h+h[:,A] g_s h[A,:]/(1-g_s h_AA).

The sign of the vertex is squared here. Equivalently use a Dyson solve (I-h Delta)^(-1)h; this avoids taking an inverse of a compressed matrix near an accidental zero. The specified vectors d,d2 and A,D are normalized distinct shell combinations, so the stated coordinate normalization is consistent. A general nonorthogonal coordinate frame would require its embedding/metric to be retained rather than blindly using these matrices.

Independent random finite real-symmetric fast+host+arm control `/private/tmp/neutral_realaxis_schur_control.py` compares the nested expression with the direct full physical block inverse: absolute error 2.80e-17. Its total negative imaginary part is positive, as required.

## Upper-half-plane convention and positivity

For E+i eta with eta>0, every constituent must be the actual upper-half-plane retarded resolvent of the specified self-adjoint model. Then Im R and Im h are negative semidefinite and the complete G_C obeys -Im G_C>=0. With eta=beta lambda^4, Im e=beta lambda^2 and Im z=beta lambda^3. beta must be positive. The upper-half-plane calculation must not accidentally use a lower-sheet outgoing continuation chosen for resonance searches. In particular the existing lattice quadrature's square-root branches and deformed integration paths need an explicit upper-half-plane control before treating its output as a positive spectral signal; the algebra alone does not verify numerical branch choices.

The two displayed terms need not separately define positive spectral measures. In particular the source correction contains b^T K b with complex b, so its imaginary part can have either sign. The full sum restores positivity. Quadrature, arm truncation, and cancellation errors should be checked against the total signal and against a positive finite-matrix approximation where practical.

## Full-versus-arm-deleted contrast

Deleting the slow arm mathematically means replacing hSlow by h while retaining the same fast model, source, and all other contacts. The difference of the two resulting resolvents is a useful diagnostic of interference caused by that channel. Its broadened spectral contrast may change sign: this is compatible with Fano enhancement and depletion and is not a negative probability. Each complete comparison spectrum must remain nonnegative.

Label the deletion as a counterfactual model diagnostic, not an allowed native Hamiltonian operation or an independent physical experiment. It can characterize line-shape interference within this coefficient model but cannot prove a positive isolated line, determine a unique resonance decomposition, or replace the omitted higher source terms. Smooth fast backgrounds and interference with them remain part of the full result. The width of Lorentz broadening is also an analysis choice and must not be fitted to manufacture a feature.

The formula treats only the leading source and stated coefficient blocks. At very small signals, omitted physical-source contributions can be comparable to a contrast even when they are higher order globally; no claim about the complete actual C response follows without a controlled remainder at the plotted scale.
