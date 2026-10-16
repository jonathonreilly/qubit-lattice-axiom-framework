**Focused independent check — finite-count plasma separation, revision 2**

The corrected working derivation supports the stated conditional phase/count mathematics. The first revision had a material distinction missing between raw phase increments and phase divided by a varying carrier frequency. Revision 2 repairs that distinction using fixed normalization units and retains the full initial-state and endpoint-error terms. The source locator correction is also confirmed. No remaining false displayed identity was found in the checked scope.

This is a focused mathematical/source check, not a formal audit, landing review, retained-status decision, measurement calibration or empirical scalar-theory test. Scientific authorship remains with `/root`. I read both complete working notes and used an independent implementation without importing or reading the author's new plasma runner. Its reported controls are therefore not part of this independent coverage.

The source identities are:

| Source | SHA-256 |
| --- | --- |
| `FINITE_COUNT_PLASMA_DERIVATION_v1.md` | `827562589f7386ec797237e83beb8c94464771688b732aa8d6540cb426f83d6b` |
| `FINITE_COUNT_PLASMA_DERIVATION_v2.md` | `0bcb450acf7c42251b02b18d67254f1e0797736ce58b2f6922d2845d54418d72` |
| `independent_plasma_checks_v1.py` | `f68bfc1ac1fb35a32dad47883556f9998f4c3f08495bba721641a38dbb4bd3ff` |
| `PLASMA_INDEPENDENT_RESULTS_v1.json` | `a487190d88c5ead22b423d0377f18e076460d646bdc91bb42ac54a82495da19b` |

Both source revisions are preserved byte-for-byte as `*_SNAPSHOT.md` in this directory. The worktree HEAD was `05ee32a6016c18dcab8ffd188495adc35e937bf6`; these working notes are outside that frozen commit.

**Findings and correction confirmation**

1. In v1, `p=Phi/F_d(t)` was followed by the claim that counts provide `Delta p`. Counts provide `Delta Phi`; changing normalization additionally requires initial phase. My exact counterexample is `Phi_s=Phi_r=6`, `F_s=2`, `F_r=3`: the raw increment is zero while `Delta p=-1`. In general,

       Delta p = Delta Phi/F_r + Phi_s(1/F_r - 1/F_s).

   V2 states this identity, defines the fixed-unit measured variable `q=Phi/F_ref`, and uses `B=diag(F_d/F_ref)A` when translating an originally normalized model. This resolves the observation-variable issue. It correctly warns that the first column of physical `B` need not be one. The repair does not derive the physical chirped/retarded operator.

2. The original guide locator, section 3.8, did not identify the cited discussion. The linked 2018 guide's body places the conjunction analysis in section 3.6.2.2, printed pages 64–67. V2 uses that locator. The GWE calibration and residual discussion is separately in 3.6.1.2.2–3. The guide's table of contents has a different numbering inconsistency; the body locator is the one checked.

3. The alignment result is valid with a global Lipschitz bound across each translated pair `(t,t+delta)`. Equivalently, a derivative-based sufficient condition can hold on the connecting interval hull. A separate derivative bound on two disjoint windows does not suffice: a function constant at zero on one and at one on the other has zero derivative within each window yet different means. I interpret v2's stated Lipschitz condition globally on the relevant domain, not as two unrelated local derivative bounds. This domain qualification should persist in downstream use.

**Independent mathematical checks**

For the cold, unmagnetized, collisionless fluid I solved the electron equation for velocity, used Faraday's vector equation to construct the magnetic field, and then solved Ampere's equation for the transverse wave number. This gives `J=i n_e e^2 E/(m_e omega)` in the note's negative-time-exponential convention and `k^2/(mu_0 epsilon_0 omega^2)=1-omega_p^2/omega^2`. Using positive accumulated cycles with the conjugate convention gives the stated positive carrier phase advance. With a fixed medium and prescribed ray,

    -d(delta Phi)/df = (1/c) integral (1/n - 1) dl > 0,

which is the positive excess group delay, not the same signed phase observable. The factor `e^2/(8 pi^2 epsilon_0 m_e c)` follows after converting angular frequency and radians to Hz and cycles.

I checked the remainder by rationalization rather than reusing the note's Taylor evaluation:

    1-sqrt(1-X)-X/2 = X^2/[2(1+sqrt(1-X))^2].

It is nonnegative. For `0<=X<=eta<1`, the denominator implies a bound no weaker than the displayed Taylor upper bound, since `(1+u)^2 >= 4u^3` for `u=sqrt(1-eta)` in `(0,1]`. Numerical evaluations used 75 decimal digits and the stable rationalized expression, including values near zero and cutoff. This establishes the displayed expansion within the local medium model; it supplies no physical `eta` or path-column bound.

Coherent transfer multiplies the uplink phase by `k=F_d/F_u`. Dividing the received result by fixed `F_d` gives the separate terms `K N_u/F_u^2` and `K N_d/F_d^2`. No equality of the two retarded electron columns is needed. This depends on the stated constant-carrier and coherent-transfer normalization, not on identifying an ODF stored reference with a physical carrier.

For the three-link matrix I solved `A^T w=(1,0,0)` by a separate rational Gauss-Jordan implementation. Row subtraction gives `det A=-(a-d)(b-c)`; the displayed weights agree with that inverse under the stated nondegeneracy conditions. The first two rows annihilate `(a,-1,0)`, confirming the explicitly restricted two-link ambiguity.

The finite-count statement follows from endpoint subtraction with constant weights. I independently accumulated increments along discontinuous rational phase paths, rather than assuming a midpoint derivative. Correlated sample covariance was computed directly from samples and agrees with `w^T C w`. Exact box-corner enumeration attains `sum |w_l| E_l`; no independence premise is needed. A cubic phase distinguishes a finite count from a midpoint derivative, and a single unmatched link-column perturbation survives the nominal cancellation.

For equal-duration alignment, translation under the integral yields `L|delta|`. I used exactly integrated piecewise-linear functions with kinks, signed offsets and shifts longer than a bin. For a bounded rate, the two interval indicators differ on a set of measure `2 min(|delta|,T)`, proving the note's weaker `2B|delta|/T` bound and the additional trivial `2B` ceiling. Affine-rate and bounded-edge examples attain the stated bounds. Changing the duration invalidates the equal-shift formula, as the note already warns.

In fixed units, applying the inverse endpoint rows gives directly

    Delta G = v_r q_r - v_s q_s
            = v_r Delta q + (v_r-v_s)q_s.

Substitution of `q_s=B_s z_s` gives the second initial-state expression and the box bound. The initial `G_s` coefficient vanishes only in the common-first-column-one class. I also tested general changing row normalizations, where this simplification does not hold. For measured phase `q+epsilon`, the estimator error is `v_r epsilon_r-v_s epsilon_s`; it cannot be bounded using only `Delta epsilon` when endpoint rows change. In the printed witness matrices a constant error `(0,1,0)` has zero increment but yields error `1/12`.

The printed zero-count witness independently solves to `(G_r,U_r,D_r)=(1/16,15/16,0)`. Its correction is exactly `1/16`. For an additional algebraic-domain check, I used a continuous matrix family with last uplink coefficient `1/(4+t)` and fixed phase vector. With initial `(0,U_0,1)`, it gives `G(t)=U_0 t/[4(3+t)]`, positive `U(t)`, and `D(t)=1`. Choosing `U_0=1` or `2` gives equal zero counts but distinct common-phase changes. These are supplied-matrix histories; they are not claimed to obey Cassini's coherent frequency-ramp dynamics.

The independent program exited 0 with 4,007 correlated mathematical checks and zero failed checks. The result JSON records family counts, witnesses and scope. These finite checks supplement the analytic reasoning above; their count is neither a theorem by itself nor a number of independent observations. The author's controls were not rerun for this report.

**Physical applicability and inherited premises**

The shared `G,U,D` functions are substantive hypotheses. Real application needs consistent local-frequency/frame definitions, common retarded ray histories, coherent transponder operation, phase unwrapping, known reference subtraction and clock normalization. Magnetic, collision, moving/nonstationary-medium, ray-splitting and higher-order effects require bounds in the residual. An unrestricted residual can absorb any failure; calling it `epsilon` does not calibrate it. Constant normalization, simultaneous endpoints, initial-phase constraints and rate bounds also require physical suppliers.

The exposed X/X product does not furnish the three distinct band combinations. Its counts and band metadata are inherited from the earlier checked block; I opened no raw product in this check. Plasma cancellation retains a unit response to common nondispersive clock, tropospheric, mechanical and trajectory terms as well as gravity. It therefore cannot by itself identify gravitational phase.

The scalar optical-potential cancellation in section 6 is inherited M1 mathematics. The M1 source retains SHA-256 `5bf05c785444a71467ae871c7e5e40f884ac67bdb976eb08b280c2d437522d56`; the count/station-time M2 note retains `7665d29d78d2ce302c445bb3f8878e50cb75d89d20bbd14cdb0c4f8d673a0bde`. Their complete arguments were checked in the earlier focused sessions; this block verifies their identities and the stated use, rather than claiming a new full review or empirical identification. No scalar action, potential, initial state, absolute scale or environmental solution is selected here.

Primary-source context was checked through [Armstrong's author review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5256086/) and the [2018 Cassini guide](https://pds.nasa.gov/data/pds4/misc/document_cassini/Cassini_Radio_Science_Users_Guide_30Sep2018.pdf). Armstrong confirms the three coherent ratios, at spacecraft-received uplink frequency, and the distinction between dispersive and nondispersive effects. The guide supports the calibration/trajectory obligations and corrected locator. No published precision is imported as a bound. Local copies hash to `378d38fe4445295fc5c55c1e436630df6291606676539a534f4a7e14d61ed01e` (HTML) and `4feb3072681da0f3026889d41864cef0c92c0beb91926278fc2d907e607c1d76` (PDF).

All writes were confined to this independent evidence directory. No author source, earlier report, campaign state, branch, commit, reserved product, formal verdict or science status was changed.
