# Quantitative complete-state output on the fixed slow-device window

Status: authored conditional composition requiring a distinct check. The sharpened inverse/derivative and subsequent direct-forcing refinement both have completed distinct checks, fully read before this source was frozen. They remain conditional on their exact inherited source premises; the composition itself still requires a distinct check. This composition now yields a complete, unconditioned, normalized-target vector-map error <.00191 for the existing finite device throughout[10^15,2*10^15]. The primary point changes neither the apparatus nor its finite horizon. A separately requested second sufficient point uses the same infinite device with a shorter receiver and earlier finite window; it is not a sweep or an optimized parameter choice. All exact physical/calibration and supplied-state premises remain conditional.

## Sources and exposure

The new load-bearing sources and checks are:

| Sibling directory | Proposal SHA256 | Check SHA256 |
|---|---|---|
| slow_lead_complete_onset_frontier | c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46 | 5f8b8a3b4aea4008c07d9d8e59b53a7c58bf4cb0deead4d7da66be84a2c4a32b |
| slow_lead_incoming_late | 59e2786a7174d06e3d95b3c6b7c8b08dd58cf8de63b9c596d5cfb6e5c3dfe6b5 | 22b0c43d6c2c8cb7e0ff506b65e6d720cdb6c7e27f9cb7467ce39a24a220044b |
| slow_lead_forced_derivative_sharp | 662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0 | 41f8ad9e18d7c1910f8a2c9b7cc70a2cb6b5a89ecbad47d52fd555b694718d4d |
| slow_lead_direct_forcing_refinement | f9fdcaa59e3b2d58805d295cb2dd63d4c7c763917ee8099b90afb2ec3c0db909 | ea62892ef0105008e9aaebf80d53bb5a6f143b86425d8d3c6ec1c417f76e1e47 |

Paths are PROPOSAL.md and corresponding _check/REVIEW.md. All four full arguments and checks were read; the new derivative source/check identities were rehashed. I authored onset frontier and incoming, and the fixed synthesis below, but not the sharpened derivative. Their independent checks are external premises, not independent checks performed by this composition. Root exposed the prospective complete-state task and rough scale; the numerical ceiling below is calculated from actual supplied constants, not imposed as a target.

Previously fully read, unchanged premises are fixed synthesis ab552c4002af8388d5e223cf81390cdcbaa74685affda5c263048cbea73cdb2a/checkc6d82eaf1e4789f6b4f6b6f5c0fe97a0201fce1dbe7e99b294995d76e516a628; actual emitter53916c906eda8cd5a1c8c6228c54002f4f74fe7986bee301d3162124d40544c0/check23c228886a96e29071beabf5e3ae1f6c9caee8544eee4e5b5ddc38f854fda707; actual recoveryf0f39510b65133d8399720c53ce2822bfe60a378ab2e50e1773a3dc8d0fe880f/check488d0a9e8871f77f40d44803ee9bfe7fda25388c66b367944eea3376f51f5195; outgoing6f9ebabb3405b124e52582c313c342889c9146e0040306d0ec7b72e8e8371b17/checkaeb147ff7d430562ff27ab7cbfc276e8066b48199ed6c9a163ee281357ecf528; scalar referencee6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e/check6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5; exact resources84b76d1ec9b1e45811b74ecd2594a0622dfb01ef69d1acadf98931c0ed3f9967/checkdd944d8803da24fdfbccfd010e2fd865196aa08ac244605303093a605fef22fe. Their exact original source/calibration, source inverses and selective installed-pair premises remain inherited; no blanket ancestral recalibration is claimed.

Uniform endpointc8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887/checkf3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0 and uniform reference5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907/check338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93 supply an optional parameterized reading of the time curve below; the numerical conclusion is only for the existing fixed device. Root additionally requested one explicit earlier/shorter finite point after the primary calculation and suggested the normalized-success refinement proved below. No scientific runner, numerical integration, parameter sweep, delegation, W/Git/PR/publication/checkpoint, model or prompt change occurred. Only this proposal is written.

## 1. Fixed physical device and complete comparator

Use kappa=1e-8, g=1e-6, h=4e-6 and the same supplied .0027<j<.003. The original calibrated shared old/source system, two converters, terminated input stub and emitter remain unchanged. Retain the eighteen cable sites and24-head record gate, including old port o=(100,2,2). The slow ray begins at the DISTINCT firstslow r0=(100,3,2), then rm=(100,3+m,2). Its connector is sqrt(jg), with the positive occupations (j-sqrt(jg))n_o, (2j-sqrt(jg)-g)n_r0 and2(j-g)n_rm for m>=1. These preserve every slow one-head diagonal2j and introduce no new vacancy scalar. The common physical scalar is c_att=c_total+4(sqrt(2)-1)j. The full shared B is not replicated per head.

Let V be the isometry preparing emitter occupied, other heads blank, source vacuum and record0 from an arbitrary four-dimensional old input. Passive references are arbitrary. Write U(t)=exp(-itH_infinity)V for the COMPLETE unprojected one-head evolution. Literal K=2I+Z1Z2 and W=[(9+12i)I+(-16+12i)X1X2]/25 enter only the ideal target; no commutation with the actual source is assumed.

Define gamma=kappa^2/j, d=2j sin h, H=d/gamma, q in pi/2+[-h,h], and slow k by -2j cos q=-2g cos k. The unnormalized scalar coefficient at firstslow m=0 is the unchanged

    Fs(k)=tf(q) F(q) sqrt(dq/dk),
    tf=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F(q)=kappa E'_q zeta exp[i61q+i172k_old(q)]
                                    /[sqrt(2pi)jDref(q)],
    Dref=-2j cos q+gamma exp(iq).

Here k_old(q)=2asin(sqrt(j/J)sin(q/2)), and zeta is the one fixed calibration phase. The total carrier is61.5q+.5k+172k_old, not61k. Let beta_t(m) be the Fourier integral Fs exp(ikm-itE_s(k))/sqrt(2pi) restricted to m>=0, E_s=2j-2g cos k. Its mass parameter ps=integral|Fs|^2=p0-R includes reflection loss. Define r(t)=||beta_t|| and

    Traw(t)=exp(-it c_att)Jout[beta_t tensor exp(-itK)W],
    Tnorm(t)=Traw(t)/r(t), when r(t)>0.                 (1)

Jout embeds source vacuum, blank other head sites and record1. Tnorm is an isometry on the entire old input, not a postselected actual state. The finite actual state will be embedded into the same infinite comparison space; no silent truncation/renormalization of the target is used.

## 2. Complete spectral decomposition and quantitative curve

Use the SAME physical union I_b=c_att+b+2j+[-d,d], b=1,3 for every prepared input and both record-X sectors. The actual seed theorem gives omitted STATE amplitude epsilon_sp<.00129 for this union. Charge it ONCE. The represented state splits into full8 emitter rows, all other finite coordinates plus complete closed tails, outgoing open rays and incoming open rays. Wrong-window prepared-input columns are retained in every part.

The checked onset interface supplies, with eta<2.8e-7 the full emitter density error per window,

    E_I(t)<=exp(-gamma t)+2gamma/j+(1-p0)+2eta.          (2)

It is an IN-BAND emitter bound. The complementary full8 emitter outside rows are not replaced by a small prepared-compression mass; they remain inside the single global epsilon_sp charge. The proof compares the full8 emitter inverse on both windows to the reference extension on all B eigenvalues. Only the prepared-vacuum reference columns have the two literal b supports. The full reference scalar density has L1 distance<2gamma/j from a Lorentzian of width gamma; its return is therefore bounded by exp(-gamma t)+2gamma/j. Cutting it costs1-p0, and actual full8 density comparison costs2eta.

For the background let L_s(E) recover all235 nonemitter finite heads and every closed slow tail, excluding only the propagating ray, in record-X sector s. Its absolute norm is<L0=4e5. The distinctly checked direct-forcing derivative certificate supplies on BOTH lips and both physical windows

    sup ||L_s'(E)||<M1=2.67e17.                         (3)

This is a checked conditional quantitative input, not the unverified1e17 illustration in the onset frontier. The finite-background inverse has norm<1.17e13, its actual output-port column<5e6, and its forced equation has exact derivative

    F'=-R F-j R V_o Q_slow' V_o^T F.

With ||F||<4e5, ||V_o^T F||<2060 and ||Q_slow'||<1/(1.99g), the first checked bound was ||F'||<4.68e18+1.56e7/g. The direct-forcing refinement then applies the exact inverse decomposition to the actual recovered F, preserving its smaller new-site coordinates and deletion-row action, and proves ||RF||<2.66e17. It therefore replaces the preceding derivative ceiling by ||F'||<2.66e17+1.56e7/g. The complete closed-tail lift contributes multiplier1.00068 and additive3600, yielding(3) at g=1e-6. It includes every finite/source/closed forcing direction and the slow1/g energy derivative. It neither differentiates only a selected emitter column nor assumes an actual-source complex strip.

Replace Tactual by the exact full8 Tref in -kappa L_s Tactual. This costs2kappa L0 eta on the union. Real-energy integration by parts of L_s Tref pays both hard endpoints and the product derivative; ||Tref||<=1.01/r_delta and ||Tref'||<=2/r_delta^2. Both Stone lips supply1/pi per window for the UNPROJECTED sector, with no record1 half-difference. Thus, for t>0,

    B_I(t)<=2kappa L0 eta
       +2kappa/(pi t)[2.02L0/sqrt(d^2+gamma^2)
                   +2.02M1 asinh(H)+4L0 atan(H)/gamma]. (4)

This already sums the two physical windows. Their closed ranges can differ and are not declared mutually orthogonal. Record-X ranges ARE orthogonal, and record0 preparation weights them by1/sqrt2, so the same bound controls their unprojected combination. The small sector-DIFFERENCE estimate .000410 is not used in place of this absolute complete recovery bound.

The checked late incoming reference gives the RAW ceiling, when g t>=1,

    Jref(t)=min{sqrt(ps),
        1.6sqrt(ps)exp(-1.99g t)+.7/[H sqrt(gamma t)]}.  (5)

It comes from a depth-one centered hard-band contour of the CONJUGATE scalar coefficient, paying both cutoff sides and m=0. The actual coefficients are not continued. Their checked complete-input real-band comparison has Eout<4.1e-5 in EACH record-X sector, including all wrong-window prepared inputs. Conjugation, Fourier isometry and halfline restriction give actual incoming norm<=Jref+Eout. Outgoing error separately costs Eout. Therefore the complete raw curve is

    ||U(t)-Traw(t)||
       <=epsilon_sp+E_I(t)+B_I(t)+2Eout+Jref(t),        (6)

for t>0 and g t>=1. The coefficient error is intentionally paid TWICE. The sharper qualitative asymptotic floor with only one Eout is not asserted by this quantitative curve.

For reference normalization, any certified lower bound r(t)>=r_min(t)>0 permits adding1-r_min(t) to(6). One explicit family choice is

    r_min(t)=sqrt(ps)*sqrt(1-Cout(gamma t)^2),
    Cout(sigma)=min{1,2.1exp(-.4975sigma)
                            +.8/[H sqrt(ps sigma)]},
    g t>=1,

when this r_min is positive. At the fixed late window the sharper already checked scalar statement r(t)>.9999984 suffices. Every expression preserves the scalar c_att phase, physical energy of wrong-window rows and the literal target old aging. All operator bounds survive arbitrary passive-reference tensoring.

## 3. Fixed-time enclosures: no prescribed target fitted

Let T0=1e15. For all t>=T0, use gamma T0>100/3, H<720000, asinh H<15, d>2.15e-8, pi>3.14 and atan H<pi/2. Equation(2) gives

    E_I(t)<1.661e-6.

The derivative part in(4) is bounded as follows at t=T0:

| Term | Sufficient amplitude ceiling |
|---|---:|
| 4L0 atan(H)/gamma contribution | .000480 |
| 2.02M1 asinh(H) contribution, M1=2.67e17 | .0000516 |
| Two hard-cutoff endpoint contribution | 2.4e-10 |
| Tactual-to-Tref replacement | 2.24e-9 |

The first three terms scale as T0/t. In particular a convenient safe curve is

    B_I(t)<2.24e-9+.000532(T0/t), t>0.               (7)

The late incoming source gives Jref(t)<2.2e-7 throughout t>=T0; explicitly H>580000, gamma t>100/3 and g t>=1e9 suffice. Using(6)–(7) at T0,

    complete raw error
      <.00129+.000001661+.00053200224
                                +.000082+.00000022
       =.00190588324.                                (8)

The right side is a uniform ceiling for all t>=T0. Adding1-r(t)<1.6e-6 gives infinite COMPLETE normalized-target error<.00190748324. These bounds are consequences of the new derivative and incoming arguments; they do not reuse the old branch-to-complete square-root estimate. No numerical integral, simulation or sweep is involved in the enclosures.

## 4. Exact finite transfer and the complete finite theorem

Retain M=5,000,000,000 NEW slow sites m=0,...,M-1 with cap g n_last and every compensation occupation. The old gate output remains upstream. This is exactly H_M=P H_infinity P in the seeded one-head sector, not an absorbing boundary. Counts are unchanged:

    5,000,000,236 head qubits;
    5,000,000,241 total physical qubits;
    5,000,000,237 head edges;
    10,000,000,277 positive blocks in the unmerged decomposition.

The four original shared old/source qubits and one record are counted once; passive references are not apparatus qubits. All source/contact norm loads and supplied correlations remain unchanged.

Weight zero on all upstream sites and firstslow, then f(r_m)=m. Only internal g edges contribute to the weighted imaginary part, so the exact single-cut theorem gives, for0<=t<=2T0,

    ||embed U_M(t)-U(t)||
       <=1.2exp[-M+4gT0 sinh1]
       <1.2exp(-2e8)<1e-6.                           (9)

This is a full-state estimate retaining both record sectors, every internal coordinate and reflected return within the horizon. There is no second reverse-edge factor and no target-packet truncation.

Combining(8), normalization and(9) proves the proposed fixed-device theorem

    ||embed exp(-itH_M)V-Tnorm(t)||<.00191,
                  EVERY t in[1e15,2e15].              (10)

It is a complete UNCONDITIONED operator-norm statement on arbitrary old input and passive reference. In its target the head lies on the normalized slow output packet, record is1, source is vacuum and all other head sites are blank. No actual record outcome is discarded in(10). The exact summed ceiling .00190848324 has slack below .00191.

The ideal packet is normalized in the infinite comparison space; the finite actual state is embedded there. Equation(10) pays any mismatch of that support by the exact cut comparison, rather than silently creating a normalized finite packet with a different comparator.

## 5. Consequences and comparison of error metrics

Let epsilon=.00191. For every normalized old/reference input and any single chosen read in the window, projection onto record0 gives

    probability(record1)>1-epsilon^2
                    =.9999963519>.999996.             (11)

This follows because the normalized COMPLETE target has no record0 part. It is stronger than subtracting a branch-amplitude tolerance from a subnormalized reference norm. It does not imply the record is permanently absorbing or that earlier measurements leave the same dynamics.

The unconditioned complete quantum channel differs from the normalized ideal isometric channel by diamond norm<2epsilon=.00382. Partial trace over apparatus is contractive, so the complete old/reference output channel is within the same bound of the literal exp(-itK)W channel. The common scalar cancels only at the channel level; it remains in the vector comparison. Projecting onto record1 also gives a successful subnormalized CP-map error<.00382 against the normalized target map. For a normalized successful branch there is a sharper elementary bound. Put a=P1 U_M psi and y=Tnorm psi. Projection gives ||a-y||<epsilon, while the complete comparison gives ||a||>=sqrt(1-epsilon^2) and unitarity gives ||a||<=1. Therefore

    ||a/||a||-y|| <=||a-y||+1-||a||
                 <epsilon+1-sqrt(1-epsilon^2).

At epsilon=.00191 this is<.001912. The same statement includes entangled passive references. Conditioning remains nonlinear, so this is not a normalized-channel diamond claim.

The same device and window previously had a complete finite-vector ceiling .083 obtained from the weaker record1 estimate .003401. Equation(10) improves THAT SAME complete-state metric to .00191 by retaining quantitative oscillation in the actual local background and by the late incoming contour. The old .003401 is a subnormalized branch metric and is not numerically compared as if it were the same error definition. Receiver length, supplied time window and exact hardware are unchanged; no speed or size improvement is asserted here.

The prior infinite qualitative complete asymptotic ceiling .001332 remains separately valid. This quantitative proof pays two Eout terms and an in-band reference replacement allowance, so it is not an onset theorem for .001332. It does not show convergence of the actual error to zero or eliminate possible omitted bound/singular spectrum. The finite apparatus is not assigned an infinite-time complete guarantee.

## 6. One additional requested earlier/shorter point

Root requested a single additional sufficient point, T1=3e14 and M1_sites=1,500,000,000 new slow sites. This changes only the finite receiver cut, not kappa,g,h, the infinite Hamiltonian, derivative certificate or target phase. It is not a parameter sweep or an optimality claim. Evaluate the actual curves(2),(4),(5) and the SAME normalization at t>=T1 rather than importing the old fixed scalar onset.

Here gamma t>10, g t>=3e8 and H>580000. Equation(7) yields B_I(t)<.001774. Since exp(-10)<.000046, equation(2) gives E_I(t)<.000047661. The raw incoming side bound is at most .7/(580000*sqrt(10))<.7/(580000*3); including the negligible bottom gives Jref(t)<4.1e-7.

For normalized outgoing concentration, use the explicit uniform-reference curve in section2. We have exp(-4.975)<.007 and ps>1-1.100044e-6, so

    Cout(gamma t)<2.1*.007+4.7e-7<.014701.

These exponential enclosures have elementary witnesses: the positive Taylor sum for exp(5) through order12 exceeds148; exp(.025)<1/(1-.025)=40/39. Thus exp(4.975)>148*39/40>1000/7, and exp(10)>148^2>1/.000046. No numerical propagation or fitted estimate is involved.

Using1-sqrt(ps)<5.6e-7 and sqrt(1-.014701^2)>.9998 gives

    1-r(t)<=1-sqrt(ps)+1-sqrt(1-Cout^2)
       <5.6e-7+.014701^2/(1+.9998)<.000110.           (12)

Both the hard-band tail and reflected reference mass remain in ps. In particular this normalization is not inherited as1.6e-6 from the later T0 window.

The complete raw error on t>=T1 is bounded by

    .00129+.000047661+.001774+.000082+.00000041
       =.003194071.

For the new finite receiver and0<=t<=2T1, its exact cut error satisfies

    D_M(T1)<1.2exp[-1.5e9+4*(1e-6)*(3e14)*sinh1]
            <1.2exp(-6e7)<1e-6.

Combining this with(12) proves the second sufficient finite point

    ||embed exp(-itH_M)V-Tnorm(t)||<.00331,
                    EVERY t in[3e14,6e14].             (13)

The summed ceiling is .003305071, with slack below .00331. Physical counts are1,500,000,236 heads,1,500,000,241 total qubits,1,500,000,237 head edges and3,000,000,277 unmerged positive blocks. All shared-source, record, seed and exact-correlated-coefficient premises are unchanged.

The same elementary complete-state consequences apply with epsilon=.00331: a single chosen read has success>1-.00331^2=.9999890439, normalized successful-vector error<.003316, and complete-channel and successful-CP-map diamond errors<.00662. These are comparisons to the same literal old operation and the correctly normalized packet at that actual time; they do not identify targets at different times.

Relative to the prior PR9676 finite complete-state ceiling .083 at T0=1e15 with5e9 new receiver sites, this second point certifies the SAME complete-vector metric below.00331 with onset and receiver count each smaller by the exact factor10/3. The physical total-qubit ratio is slightly different because of the241 shared/upstream offset. This is a comparison of sufficient mathematical certificates, not optimality or a practical speed claim. The prior .003401 branch metric is not interchangeable with this .00331 complete metric. The primary same-window theorem(10) and earlier/shorter theorem(13) are distinct finite apparatus cuts; they are not a joint assertion about one apparatus changing its length during evolution.

## Scope and next check

This is a new authored complete-state composition, pending a distinct check of its source use, both-lip/window factors, unprojected-sector aggregation, full8 emitter restriction, one omitted charge, two coefficient errors, normalization, fixed arithmetic and exact finite comparison. The sharpened inverse/derivative and direct-forcing refinement have completed separate checks; neither check alone independently certifies this new temporal composition.

All conclusions concern the exact supplied static Hamiltonian and seeded one-head sector with arbitrary passive references. Original source/calibration closure, correlated coefficient supply, initialization, installed-pair selection, native Record/readout identification and physical-time units remain premises. No tolerance theorem, repeated-monitoring protocol, stopping-time rule, autonomous reset/reuse, irreversible capture or permanent halt is derived. A single chosen read is covered; intervening measurements alter the evolution and require their own instrument contract. No Git/PR, publication or retained audit status is claimed.
