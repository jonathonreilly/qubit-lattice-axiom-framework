# Independent joint correction review

**Disposition:** the proposed first correction is correct as a fixed-support formal effective-operator expansion under the stated joint scaling. No sign, Gauss constraint, compensation or first-order Schur-normalization defect was found. This is an exploratory independent check, not a uniform low-spectrum theorem, physical prediction, publication decision or formal audit.

## Reconstruction

I read the complete four exploratory sources named below and used the already inspected unchanged common-field/local-pair premises. The check code imports no author implementation. It builds states from the four-vertex incidence matrix, enforces every Gauss equation, constructs normalized spin lowering amplitudes, and constructs compensation from the supplied sum of `(F_a*F_a - diagonal(F_a*F_a) + D_a,infinity) Q_a`, without presupposing `4P`.

In the two-positive-record sector, Gauss law is div E=q−1_A. Taking the first edge field as n gives the author's field tuple; source signs therefore agree with an outward positive-record hop lowering its edge field. In the all-A sector E=(n,−n,−n,n), so the electric term is 4Kn². Gates remove compensation in W=1 and W=2. In W=0 each one-hop matter output specifies its edge, eliminating interference in F_a*F_a, and the retained D_infinity terms give exactly 4P. This holds at spin boundaries as well: the missing boundary contribution is compensated by the supplied diagonal correction, not silently discarded.

The two orders of each two-hop matching have positive product sign. They give Z|n>=2[a_n|n−1>+b_n|n>] with a_n=1−n(n−1)/C and b_n=1−n(n+1)/C. Therefore M=4I−4n²/C, N diagonal=4(a_n²+b_n²), and N(n+1,n)=4b_n². These statements agree with independently constructed finite matrices for S=3,5,8 (maximum tested M/N errors below 9e−16; compensation exact in floating arithmetic).

## Schur coefficient and normalization

Put alpha=K/delta and 1/C=alpha x. Then M=4I−4alpha x n², N=N0+xN1+O(x²), with the stated N0,N1. At rotor order BB*=4I, so R0=A*(B*B)^2A=4N0. The inverse expansion yields

    lambda = 4xI − xM − (x²/2)N − x lambda M − (x³/4)R0 + O(x⁴)

on fixed support with lambda=O(x²). In particular the −x lambda M sign is negative. The left metric is 1+4x through first order; hence

    H1 = −delta N1/2 − delta N0 − 4H0.

This gives exactly

    H1(n,n) = 8delta − 8Kn²,
    H1(n+1,n) = 4delta + 4Kn(n+1).

The scalar leading metric entails no missing first-order noncommuting normalization term. At subsequent orders its non-scalar part must be retained. Interpreting this as a formal coefficient on the identified P space is appropriate; an energy-independent globally controlled effective Hamiltonian has not been established merely by this expansion.

## Exact additional simplification

The supervisor's subsequent Woodbury identity also checks. On W=2 the fields are (m,−1−m,−1−m,m). Every reverse-hop amplitude squared equals d_m=1−m(m+1)/C. Each W=1 state has only one legal remaining outward hop, so distinct W=2 rows have no shared precursor. Thus BB*=4 diag(d_m) exactly.

Away from the relevant elimination poles, Woodbury gives

    E(1+4x−lambda) psi = [4Kn² − delta Z* R(E)^−1 Z] psi,
    R_m(E)=(1−lambda)(2−lambda)−4x d_m,
    lambda=x² E/delta.

This follows by multiplying the original Schur equation by (1−lambda)delta/x², not by assuming that its scalar factor is an independently normalized Hilbert-space metric. Numerical matrix identities at S=3,5,8 and lambda=−0.04,0.02 agree within 8e−14. The denominators are bounded away from zero for bounded physical E and sufficiently small x because 0<=d_m<=1 for allowed integer fields. This helps but does not alone prove uniform low-eigenvalue identification or remainders.

## Numerical corroboration and scope

Fresh independent complete-state diagonalizations at S=12,24,48, K=1 give maximum errors in the first six gaps after first-order perturbation:

| delta | S12 | S24 | S48 |
|---|---:|---:|---:|
| 1 | 0.03323333 | 0.00230700 | 0.000151236 |
| 31.607246 | 19.288777 | 4.179830 | 0.347297 |

At delta=1 the error/x² progresses 808.77,830.52,836.62; at the larger ratio it progresses 469.87,1506.22,1923.10. The finest eigen-residuals are about 3.8e−9 and 1.5e−10 respectively. These corroborate the coefficient and are not certified asymptotic constants. The author correction script computes first-order expectation shifts, appropriately, rather than asserting that exact diagonalization of H0+xH1 proves the expansion.

An independent scalar rotor-series reconstruction gives lambda coefficients at x²,x³,x⁴ of −4(1+c), 8(1+c), and 8(1+c)(5c−1), with c=cos(phi). Consequently the physical rotor x² coefficient contains +20delta cos(2phi), alongside scalar and first-harmonic terms. That rotor-only harmonic does not replace the earlier-order joint field-dependent correction.

Open proof obligations remain uniform control for low spectral states, boundary/high-field exclusion or localization, and an error estimate strong enough to justify expansion of the relevant eigenvalues and eigenvectors. Fixed-n Taylor coefficients do not control n of order S. The exact tridiagonal energy equation is a promising additional tool; it is not itself those missing estimates. No noninteger offset, cavity, open formation dynamics or microscopic parameter inference was checked here. Setting kappa=0 remains an external specialization. The approximate device-like ratio is a diagnostic input, and x is not calibrated from independent data. Nothing here establishes improvement on experimental holdouts or licenses fitting them.

## Evidence and identities

Fresh evidence: `independent_joint_check.py`, `independent_joint_check.json`, `independent_woodbury_check.py`, `independent_woodbury_check.json`. No author files were modified. Exact SHA-256 reviewed identities follow; the same inventory is in `independent_checked_hashes.json`.

- `.claude/science/physics-loops/measured-corrections-20260927/JOINT_CORRECTION_DRAFT.md`: `21124422fb44ca73b0b5200b648dd93fcdc22b8815ad9ccfbe247510a36aeaaf`
- `.claude/science/physics-loops/measured-corrections-20260927/finite_spin_square.py`: `de5fe61d3f05899961f38af803c5365d09bc4d52b5bb3538f16ef65a6b0b163f`
- `.claude/science/physics-loops/measured-corrections-20260927/joint_correction_check.py`: `640c3fb1d91c6edb781a907d9f9739c88b01fa1f82000294a288838a0cbbf211`
- `.claude/science/physics-loops/measured-corrections-20260927/rotor_fiber_probe.py`: `05d7f1636b0d96f2eb511ed5744e9e37a9e8441197414b7f92003a514a6addd7`
- `docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`: `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a`
- `docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md`: `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b`

## Bounded calibration-tangent follow-up

Read the three subsequently supplied scripts below. Independent central differences of the tridiagonal H0+xH1 eigenvalues, instead of the author's Hellmann–Feynman implementation, verify the two-input derivative subtraction at K=1, delta=31.607246. The constraint is J_low dp=−c_low; therefore the residual derivative is c+J dp, not c alone. Central-difference step 1e−4 gives dp≈(−2.86311017,154.40849118) and the higher-gap coefficients per x

    +0.94659537, +4.05746189, +10.95440650, +24.77605123.

Steps 3e−5 and 1e−5 preserve those positive signs, with the expected eventual finite-difference cancellation. Evidence is in independent_tangent_check.py/json. This confirms the reversal from the raw negative shifts after holding the two toy low gaps fixed. At fixed spin, x=delta/(K C) also changes during recalibration, but dp=O(x) makes its induced dx=O(x²); it does not alter this first-order tangent.

The exact_schur_square.py diagonal/off-diagonal expressions agree with the independently checked energy equation. The nonlinear control script fits only two baseline-model gaps and has the described toy scope. I have not independently rerun its nonlinear fits or certified that its root brackets exhaust a prescribed low spectrum; their numerical outputs are not additional independent evidence in this report. For this declared ratio the independent tangent is enough to disallow the inference that negative uncalibrated shifts necessarily improve the experimental residual. It does not determine signs after the actual four-coordinate cavity/offset calibration, nor test measured lines.

Follow-up source SHA-256 identities (the original draft hash above is unchanged):

- `calibration_tangent_probe.py`: `24b74362bffc396d70558d7198ff42269255bfcfb2ac25acf502b4c0ecaae455`
- `nonlinear_calibration_control.py`: `38efa7fdd72ae629855823ee281fbf7f00ff24f24f78477f805bf1930e61e539`
- `exact_schur_square.py`: `297919235617649a71304b477a3776e1e1316f23a487a76e034b3459e7603067`
