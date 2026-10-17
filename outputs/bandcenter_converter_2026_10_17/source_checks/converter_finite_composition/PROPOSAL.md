# Nominal converted device: finite complete-output composition

Status: authored composition of selectively checked components, requiring a distinct integration check. For the exact nominal converted apparatus below, set T=1e17 and integer M=1.5e15. The conditional infinite complete vector/isometry error is <.001514 for every t>=T. The SAME finite device chosen before delivery has complete error <.001515 for every t in[T,2T]. These are different error tolerances from the original PR9672 nominal .000320 infinite/.001320 finite result at T=3e17; this is not an across-the-board improvement.

## Sources, dependency table and authorship

Read BOTH the full final wide temporal proposal and its full selective check for this task. The output-only weight and its check, and the resource source/check, were previously read in full in this coherent sequence; all six hashes were verified again here. No truncated read is counted. The following frozen dependencies carry the stated roles:

| Dependency | Exact SHA256 | Role/status used here |
|---|---|---|
| `../bandcenter_wide_temporal/PROPOSAL.md` | `f407f29620b318e6253a0d75ec9a7a3007be89ff41786f753899d30805eee8cc` | Full nominal wider-band temporal theorem and comparator |
| `../bandcenter_wide_temporal_check/REVIEW.md` | `1182667f9f46a2fd7828558f68be95d9bc742c69bb6cf72617ced810edcc931f` | Conditional selective support for T=1e17 and infinite error<.001514 |
| `../output_lead_weight/PROPOSAL.md` | `58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf` | Output-coordinate finite-transfer inequality |
| `../output_lead_weight_check/REVIEW.md` | `1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd` | Selective support for that inequality, including M=1, full operator scope and illustrative horizon arithmetic |
| `../bandcenter_resources/PROPOSAL.md` | `96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7` | Exact graph, positive blocks, cap/compression, counts and physical scalar |
| `../bandcenter_resources_check/REVIEW.md` | `01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd` | Selective support for the resource construction |

The temporal check explicitly carries the final bandwidth source `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2` and its check `3f721b75911630e0aec48688893c6bae84a182cafaa1012c977e9e262d6e180d`, and the corrected narrow temporal source `add82a40ddc49a7c7954ea1b087b1b1bf348e8375da072c96b2b2df1b6d2c011` and check `6df1d5809db83393bfd449442a355a6d25f5f26b31bdecf81c3a833ae67f5a23`. Those are inherited dependencies through the fully read wide argument/check, not fresh ancestral recertification. The original calibrated source and disk premises remain pinned there to canonical endpoint-note SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`.

I authored the earlier nominal converter/endpoint/narrow temporal proposals and generic hopping lemma, and authored the selective check of the DIFFERENT author's output-only weight. I did not author the wide temporal proposal or its check. Root supplied the intended composition and bounds. This is source-exposed synthesis, not another independent check, blind discovery, audit disposition or a claim that multiple reports recertify their shared ancestry. In particular the corrected direct incoming-packet comparison in the final temporal source is used; no earlier uncorrected packet-switch argument is revived.

Applicable previously read instructions/workflow are reused. No scientific execution, numerical experiment, parameter sweep, delegation, model override, W/Git/checkpoint/prompt edit or publication occurred. This is the sole deliverable.

## 1. Exact apparatus and comparison contract

Use the original supplied real positive source/filter/junction with one shared old/source fiber, literal K/W, J=.030021107107032, k0=2atan(1/4.510351185997098), C0=cos k0 and S0=sin k0. Add exactly TWO nominal exterior converters after F=40 old-J steps, with

    j=J(1-C0), tau=sqrt(j J S0), gamma_c=tau-j>0.

The new input contains n=0,...,ell with ell=20, and the adjacent emitter has the specified positive equal-diagonal block j(ne+nend)-kappa(exchange), plus j ne, with kappa=1e-8. Both emitter and input endpoint diagonals are2j. The original source/contact coefficients and filter/junction remain unchanged. No failed retuned-contact candidate or common-j drift family is used.

The new output origin n=0 is the first new-j site after its converter. For the finite device retain n=0,...,M-1 and add cap j n_(M-1). M counts NEW output sites only. The output cap makes the finite one-head Hamiltonian the exact retained compression of the infinite Hamiltonian. It changes neither any retained internal block nor the common scalar. There is precisely one cut edge of magnitude j.

The comparison band is q in pi/2+[-Delta,Delta], Delta=4e-6. This changes the comparison cutoff, not the physical Hamiltonian. Its energy margin maps inside the ORIGINAL certified k halfwidth1e-6: |E(q)-E0|<2.4e-8<2.5e-8 and |k(q)-k0|<.96e-6, where

    E(q)=2j(1-cos q), cos k(q)=C0+(1-C0)cos q.

All seven complementary channel directions, the full emitter complement, finite source/core positions and evanescent tails are retained by the temporal proof. The actual out-of-band/point-spectrum seed mass is charged by its earlier spectral proof; it is not reset to zero or replaced by the reference tail here.

The delivered embedding V_seed is the same emitter-occupied, other-head-blank and source-vacuum product preparation, tensored with arbitrary old input and any passive reference. No drive or timed control acts after delivery. Define

    Dref(q)=E(q)-2j+(kappa^2/j)exp(iq),
    rho_n(q)=-exp(2iF k(q))rho_g(k(q)),
    Fref(q)=i kappa E'(q) exp[i(ell+1)q]rho_n(q)
                         /[sqrt(2pi)j Dref(q)],
    p0=integral_band |Fref(q)|^2 dq, f=Fref/sqrt(p0).

Here rho_g is the fixed common old-source/filter/junction phase from the source theorem, not a phase fitted per old column. The full q-dependent phase is21q+172k(q)+constant. Let beta_t be the positively normalized restriction to output n>=0 of the Fourier packet with coefficient f and phase exp[iqn-itE(q)]. It is the SAME infinite target for both finite and infinite comparisons.

The target isometry Q_t has beta_t on the output, blank emitter/other clock/source registers, and exp(-itK)W on the literal old system, multiplied by exp(-it c_total) and tensored with the reference identity. The exact scalar is

    c_total=2nu+2beta_filter+4gamma_J+4gamma_c,
    gamma_J=(sqrt(2)-1)J.

No factorization of exp(-itK) from the interacting physical evolution is asserted. It is the prescribed target aging; internal interactions are kept exactly throughout both proofs.

## 2. Infinite theorem used without changing its error

The checked wide temporal argument proves, for every t>=T=1e17,

    ||U_infinity(t)V_seed-Q_t||<.001514.                    (1)

Its direct incoming-transform initial bound includes all actual spectral residual and uses the conjugate incoming comparison packet. The outgoing mismatch is charged once, giving static subtotal<.001512. Its complete localized bound, both scalar tails, phase derivative64, both cutoff sides and positive normalization cost yield the explicit total

    .001512+1.21e-6+1e-9+4e-8+1.6e-15 <.001514.

This statement is an all-old/reference operator/isometry bound with the inherited within-parity aggregation, not a scalar transmission probability. This composition uses the published component ceiling .001514, not an unannounced tighter tolerance obtained by rounding that displayed sum differently.

## 3. Finite transfer at one fixed integer M

Choose before delivery

    M=1.5e15=1500000000000000,
    T=1e17, 2T=2e17.

The checked output-only weight is zero on the entire core/input/buffers and first output site, and equals n on the new output ray. Every nonzero-gradient retained edge has magnitude j. The finite-cap identity, full internal unitaries and one-cut Duhamel comparison therefore give, for all0<=t<=2T,

    ||U_infinity(t)V_seed-E_M U_M(t)V_seed,M||
       <=1.2 exp[-M+4jT sinh1],                           (2)

where E_M embeds the finite head space by blank omitted head sites, with the same internal and reference spaces. The seed embeddings agree under E_M. This transfer estimate is independent of the momentum cutoff and preserves all actual source/point-spectrum components. It does not rely on wavepacket escape or scattering completeness.

Using j<.003 and sinh1<1.2,

    -M+4jT sinh1 < -1.5e15+1.44e15=-6e13,
    transfer <1.2 exp(-6e13)<1e-6.                         (3)

For an elementary strict witness, 6e13>21 and exp(21)>2^21=2097152>1.2e6. No enormous exponential was numerically evaluated. The original cap/indexing and the temporal output origin coincide, so no extra converter or buffer distance is inserted into(2).

## 4. Composed finite theorem and resources

For every t in[T,2T], apply the triangle inequality in the SAME infinite comparison space to(1) and(3):

    ||E_M U_M(t)V_seed,M-Q_t||
       <=||E_M U_M(t)V_seed,M-U_infinity(t)V_seed||
                            +||U_infinity(t)V_seed-Q_t||
       <1e-6+.001514=.001515.                            (4)

No output projection, capture, reset or postselection is inserted. In particular Q_t is not clipped and renormalized to M sites: any finite-support incompatibility with the infinite target is already paid by this complete vector comparison. Tensoring a passive reference preserves both terms. The corresponding unhalved trace-distance ceilings are .003028 infinite and .003030 finite. The finite conclusion is ONLY on[T,2T]; the infinite conclusion holds for every t>=T under its premises.

The checked exact resource inventory at this M is:

- M+194 head qubits and M+194 head-hopping edges.
- M+198 physical qubits, including the same four old/source qubits.
- M+223 positive blocks in the stated decomposition.

Thus the total physical count is1500000000000198. Passive references are excluded from that apparatus count. Counts and cap are the same construction used in the finite-transfer proof; no source duplication or omitted interface site is hidden. The coefficients are static, but the original large source incident loads remain and no all-site cap2 is asserted.

## 5. Comparison and success limits

| Conditional sufficient result | Onset | Output sites M | Infinite error | Finite error on[T,2T] |
|---|---:|---:|---:|---:|
| Original PR9672 nominal apparatus, published choice | 3e17 | 1.5e19 | <.000320 | <.001320 |
| This nominal converted composition, pending integration check | 1e17 | 1.5e15 | <.001514 | <.001515 |

The new onset is three times earlier and the displayed output-site choice is10000 times smaller than that published original choice, but BOTH error ceilings are larger and the architecture/reference packet differ. This is a tradeoff between sufficient certificates, not an optimum or an architecture-exclusive resource advantage. In particular the output-only-weight method can also improve finite-transfer estimates for an original uniform output lead; that separate application is not incorporated into this comparison. The converter's new group velocity is smaller, and this proof does not reinterpret time units.

No original fixed-spectrum robustness family, common-j drift, independent coefficient-error contract, native positive-block/seed supplier, physical energy/time calibration, practical scale, all-future finite halt, reset/reuse or capture theorem is added. The structural equal-diagonal emitter relation remains explicitly supplied. The finite count is still enormous. No new scientific execution or audit/retained status is claimed.

The remaining task before reliance is a distinct selective integration check of device/seed/target identity, the output-origin/cap interface, exact inherited static and temporal scope, and arithmetic(3)–(4). This authored composition is not that check.
