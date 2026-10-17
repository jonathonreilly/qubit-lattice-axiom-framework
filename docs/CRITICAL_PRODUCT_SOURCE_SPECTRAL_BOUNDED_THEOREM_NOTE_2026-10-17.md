# Three-site product source: installed spectral concentration and matching

**Type:** bounded_theorem
**Status:** conditional mathematical support; unaudited.

Runner: [control_output_family_2026_10_17.py](../scripts/control_output_family_2026_10_17.py).

Publication evidence boundary: the analytical argument and its named supporting proofs remain controlling. The shared runner supplies finite algebra, matrix, flux and budget corroborations only; it does not prove the continuum/contour estimates, certify all parameter families, or establish physical realization. Statements below about no new computation describe the original authoring stage; its exact source is preserved in `outputs/control_family_landing_2026_10_17/originals/CRITICAL_PRODUCT_SOURCE_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-17.md`. Historical author reviews are provenance, not independent landing authority.

Claim type: bounded_theorem. Status: conditional-support publication draft for review. The component constructions and calculations have distinct selective checks; this new synthesis requires its own integration review and confers no retained audit status.

A three-site source can replace the existing single emitter by adding two head qubits while leaving the calibrated emitter-free processor unchanged. For the supplied nominal point

    lambda=10^-11, g=5×10^-8, h=4×10^-6,
    a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda,

the actual installed product seed has outside-window STATE norm **<4.1×10^-6**, uniformly over all old inputs and passive references. The complete source matching criterion obeys **Theta3<.000523** on both physical windows, with every internal channel retained. These are spectral concentration and resolvent-conditioning results. They are not a complete output-error, runtime, storage or receiver-size improvement.

The original calibrated j is fixed supplied data, enclosed by .0027<j<.003; the interval does not authorize retuning it independently. The [original exact-source note](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`, supplies the inherited source and calibration premises. The [wider slow-output note](WIDE_SLOW_OUTPUT_COMPLETE_STATE_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA256 `feec1a7b2d48b758c86d5bdcde4ef0043a3b51ee09fb773024fbd7fd52d5bb38`, supplies the existing background and inventory context. Its previous complete-output performance does not transfer to the new source. The `outputs/critical_source_2026_10_17/SOURCES.json` distinguishes exact new copies, existing ancestry and definition-only imports.

## Physical construction and unchanged shared source

Keep the old/source operator B shared once, with the original source-vacuum embedding iota and

    B iota=iota K, K=2I+Z1Z2,
    W=[(9+12i)I+(-16+12i)X1X2]/25.

No new head carries a separate copy of the source qubits. K need not commute with the actual head-dependent contacts elsewhere. Keep the converters, capped input, cable, record gate, slow output, physical scalar c_att and all their exact phases. The source sites have no new head-dependent old/source contacts.

The input endpoint is p=(40,63,1). Reuse the previous emitter as s2=(40,64,1), and add s1=(40,65,1), s0=(40,66,1). The supplied coordinate inventory shows both added positions vacant, with only the intended collinear occupied neighbors. Seed s0 is occupied; s1,s2 and every other head are blank, shared sources are in their supplied vacuum, and the record is computational 0. Old input and any passive reference are arbitrary.

For 0<lambda<=10^-8, replace the old two emitter blocks by six blocks:

    j(n_s2+n_p)−kappa exchange_(s2,p),
    Q_a2(s1,s2), Q_a1(s0,s1),
    (j−a2)n_s2, (2j−a1−a2)n_s1, (2j−a1)n_s0,
    Q_a(x,y)=a(n_x+n_y−exchange_xy).

The structured port block has eigenvalues 0,j−kappa,j+kappa,2j and norm 2j. The other exchanges and occupations are positive on the full qubit space. Each source head and p has one-head diagonal 2j. There is no vacancy term and no added scalar. New source incident norm sums are 3j+a2 at s2, 2j+a1+a2 at s1 and 2j+a1 at s0. The boundary incident-block load is unchanged.

Principal compression off all three source heads leaves exactly j n_p from the structured port block. This is exactly the old emitter-free endpoint compensation. Removing the entire incident block instead would change the boundary diagonal and invalidate the reuse. Thus the compressed background H_bg and its full eight-coordinate kernel G, within each parity/record-X sector, are literally unchanged. The `outputs/critical_source_2026_10_17/source_checks/two_site_actual_attachment/PROPOSAL.md` establishes the port/geometry and background identity; the `outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment/PROPOSAL.md` and its `outputs/critical_source_2026_10_17/source_checks/three_site_actual_attachment_check/REVIEW.md` verify the six-block extension.

With M retained slow receiver sites, the possible finite installation has M+238 heads, M+243 total physical qubits, M+239 head edges and 2M+281 unmerged positive blocks. Relative to the old single-emitter device this adds two heads, two edges and four blocks. References are excluded; old/source and record qubits are counted once. These are inventory formulas, not a sufficient choice of M or a finite performance certificate.

## Actual installed product-seed concentration

Let V denote that complete product preparation, Pi_e the old K-energy projection for e=1,3, and E_e=c_att+2j+e. Put d=2j sin h and I=I_1 union I_3 with I_e=[E_e−d,E_e+d]. The `outputs/critical_source_2026_10_17/source_checks/three_site_product_source/PROPOSAL.md` and its `outputs/critical_source_2026_10_17/source_checks/three_site_product_source_check/REVIEW.md` give an exact local identity for the installed apparatus:

    (H−E_e)^3 V Pi_e
       =[−a1(a1²+a2²)|s1>−a1 a2 kappa|p>] iota Pi_e.

The third application first reaches p; it does not yet apply any of p's downstream diagonal, contacts or branches. The shared B acts as e on the vacuum over the three source sites. Consequently

    mu6=||(H−E_e)^3 V Pi_e||² on its prepared range
       =a1²(a1²+a2²)²+a1²a2²kappa²
       =3lambda^6+(8/3)jlambda^5.

The squared-norm identity means the corresponding sixth spectral moment; for an unbounded operator it is a quadratic-form statement on the third-power domain. The bounded one-head apparatus satisfies that domain condition. The port-reaching term is essential and is not replaced by a lambda^6-only estimate.

The spectral theorem gives each old-energy outside amplitude at most sqrt(mu6)/d³. For arbitrary superpositions, triangle inequality and Cauchy–Schwarz across the two orthogonal INPUT projections yield

    ||E_H(I^c)V||<=min{1,sqrt(2mu6)/d³},
    0<=V*E_H(I^c)V<=min{1,2mu6/d^6}I.

There is no assumption that the omitted output ranges are orthogonal or that H commutes with K. This includes outside atoms, singular spectrum, all output coordinates, coherent initial record0 and passive references. It is an actual installed-seed estimate, not the measure of a fictitious uniform-ray source. It remains true in a device with poor emission; concentration alone proves no escape.

At the specified point, d>2.15×10^-8 and mu6<8.00000003×10^-58. The squared comparison

    2mu6<1.600000006×10^-57
       <(4.1×10^-6)²(2.15×10^-8)^6

proves the advertised outside-state ceiling. The local moment is also valid for a compatible finite downstream installation, but that does not transfer the semi-infinite background's stationary inverse bound to a finite receiver.

## Full matching with the unchanged boundary kernel

The `outputs/slow_wide_2026_10_17/source_checks/slow_lead_wide_endpoint/PROPOSAL.md`, specifically its emitter-free sections 1–2, provides on the retained band

    ||G−G0||<a0+b0|delta|,
    a0=8×10^-18, b0=46000/.0053+290/g,
    G0=m_j(D), D=(E−c_att−2j)I−B.

m_j is the physical uniform-j halfline root on EVERY channel: outgoing on the selected open channel, real signed decaying roots on closed channels. Complementary D eigenvalues have modulus at least .185. The background matching chain and roots remain regular on neighborhoods of both closed windows because H_bg is identical. The retained conditions are 0<g<=10^-6, 0<h<=4×10^-6 and d/g<=.5; a loose bound d<=2.4×10^-8 alone would not establish the old calibrated band. Later one-site emitter restrictions and temporal results are not used.

The new three-source Schur matrix is

    S=[[D,a1I,0],[a1I,D,a2I],[0,a2I,A]], A=D−kappa²G.

Define P(D)=D²−a1²I and Q=P(D)A−a2²D. For forcing (f,0,0), the exact source columns are

    psi2=a1a2 Q^-1 f,
    psi1=−a1 A Q^-1 f,
    psi0=(DA−a2²I)Q^-1 f.

Their order is retained even when G and D do not commute. Invertibility of Q implies that of S without inverting resonant D or A. The `outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse/PROPOSAL.md` and its `outputs/critical_source_2026_10_17/source_checks/three_site_loaded_inverse_check/REVIEW.md` show, with r=lambda/j,

    |q0(x)|²/lambda^6=(1+y²)^3−r(3y^6−10y^4+3y²)
                    >=(1−3r)(1+y²)^3, y=x/lambda,
    (1+y²)^3−9(y²−1/3)²=y²(y²−3)²>=0.

The complementary physical-root estimates give |P/q0|<6. The ordered perturbation Q=Q0[I−kappa²Q0^-1P(D)(G−G0)] therefore has norm bounded by

    Theta3=(j a0+kappa²b0)/sqrt(1−3r)
                             +6kappa²(a0+b0d).

If Theta3<1, the complete inverse exists on both lips with

    ||Q^-1||<=1/[(1−Theta3)sqrt(1−3r)(delta²+lambda²)^(3/2)].

The lower lip is treated in its own order; its Q is not generally the adjoint of upper Q. All internal rows and wrong-window prepared inputs remain in these bounds. Combining the new inverse with the existing complete matching supplies local seed boundary regularity on the windows, but not a temporal escape rate.

At the nominal point, kappa²<9×10^-14, b0<5.809×10^9 and sqrt(1−3r)>.99999999. The leading term is less than (.003·8×10^-18+9×10^-14·5.809×10^9)/.99999999; the complementary term is below 7.53×10^-11. Their sum is <.000523. This is conditioning, not fidelity or a success probability.

## The scalar comparison and what remains open

For the isolated same-carrier uniform-j halfline, the three-site determinant is

    D(z)=(z²−lambda²/3)(z−3jlambda m_j(z))−(8lambda²/3)z.

Replacing only the self-energy by its center value −i3lambda gives (z+i lambda)^3. The exact lattice density is instead

    rho0(delta)=8lambda^5 sqrt(1−delta²/(4j²))/(3pi|D_+(delta)|²).

The checked scalar proof establishes its total normalization and absence of hidden scalar spectral mass on lambda/j<=1/16. It controls all three source amplitudes against the reference

    e^-x(1+x+x²/3), i e^-x(x+x²)/sqrt(3),
    −e^-x sqrt(2)x²/3, x=lambda t,

with explicit weighted full-line density errors, including both reference tails and intermediary sites. This is a genuine candidate scalar comparison, not the actual installed processor's emission law. The local moment and unchanged-background inverse do not transfer its escape estimate to that processor.

A complete theorem still needs the actual outgoing and wrong-window coefficients on both physical windows/lips, all three source amplitudes and finite-core/closed-tail escape, incoming contribution, normalization and a common spatial waveform. The target must retain the physical scalar and full old aging as exp(−it c_att)J_out[g_t]exp(−itK)W with source vacuum, record1 and all passive references. One common g_t must be derived; it cannot be fitted by old input, parity, record sector or read time. New source-relative runtime and finite cut are also required. The provisional outgoing and prepared-core recovery work is not included as proved evidence here.

The new <4.1×10^-6 omitted-state allowance is smaller than the prior .00125 allowance for a DIFFERENT source. This compares only one error component. It preserves neither the old waveform nor its full .00191 error, T=10^15, M=250 million or record guarantee. No complete speed, storage, receiver-size or precision improvement follows.

## Evidence and status

The packet contains the three current argument/check pairs and the necessary two-site definition/attachment ancestry. Full mapped proofs, not their status labels, support the interfaces used above. The manifest also resolves unchanged background sources through existing repository packets without recopying them. Historical pending-review wording in frozen sources is qualified by their actual paired reviews; it is not silently rewritten.

The drafter authored the three-site scalar/moment proposal and previously checked the two-site inverse/mass interfaces and shared ancestors. The new attachment and loaded inverse are root-authored and separately checked. This publication is source-exposed synthesis, not an independent check of itself or of every ancestor. Component checks use the same selected model and disclosed shared research context; no blind or model-diverse independence is claimed.

Exact source calibration, correlated couplings, product preparation, selective installed interactions and native Hamiltonian/time/energy/Record identification remain conditions. Registered framework primitives do not themselves supply these device-specific interfaces. No permanent halt, irreversible capture, reset/reuse, native supplier, practical physical time scale, optimality or retained audit status is asserted.

Only this research NOTE.md and SOURCES.json are delivered. No scientific runner, numerical spectrum, quadrature, dynamics simulation, sweep, Git/canonical/PR action, checkpoint, editable prompt, model or physical axiom changed. Root owns distinct integration review, exact copying, canonical graph validation and any later publication.
