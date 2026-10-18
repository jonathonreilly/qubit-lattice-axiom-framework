# Ten-layer bound pole in a prepared heavy-return protocol

PASS for the leading coefficient and for a refined, matched-dressing fixed-volume transfer using the structural estimates below. The older generic O_R,tau(lambda) protocol error alone is insufficient for this much smaller amplitude. No bare-preparation or emission-rate conclusion follows.

## Ground/pole mixing and normalization

Let Delta4=L/16 and c=(gamma_L/Delta4)lambda^(L-4). The vacuum first correction is +c T_bg g0: the perturbing matrix element is -gamma_L lambda^L and the vacuum-to-four-flux energy denominator is -Delta4 lambda^4. The zero-momentum even pole tends to b0=(A+B)/sqrt(2). Its flat component has the opposite sign, -c<T_bg g0,b0>g0=-c sqrt(2)R g0, as required by orthogonality to the dressed ground. This is the excited-state mixing responsible for the free-return subtraction.

Each physical edge syndrome is distinct on the admissible large torus. In b0 each of the 2R^2 shortest-edge syndromes has amplitude 1/(sqrt(2)R). If r_e(tau)=<i|exp(-i tau T_e)|i> and r_0 is the flat-background return, the leading amplitude is therefore

    c/(sqrt(2)R) sum_edges [r_e(tau)-r_0(tau)].

No extra factor of two occurs. The subtraction is essential; retaining only the excited part of the vacuum gives an incorrect nonzero amplitude at tau=0.

## Four-step coefficient

At fixed particle position i,

    (T^4)_ii=28I+2 sum_(p incident i) P_p.

The zeroth and second moments are background independent; odd return moments vanish on the even bipartite torus. Flipping an edge syndrome changes each of its four affected plaquettes from +1 to -1, giving -4 for each affected incident plaquette in the fourth moment. Each of the four plaquettes incident to i is affected by eight transverse edge syndromes, hence

    sum_edges [(T_e^4)_ii-(T_0^4)_ii]=-4*4*8=-128.

The exponential fourth-order factor is (-i)^4/4!=1/24. Consequently

 amplitude = -(8sqrt(2)/3) gamma_L/(Delta4 R)
                 *lambda^(L-4) tau^4
             +O(lambda^(L-4) tau^6/R)
             +higher-lambda terms.

The sign is correct in the phase convention with positive leading b0 and g0. Its phase alone is convention dependent; the squared weight is invariant. For the leading signed-hopping graph, counting closed walks shows only O(length) affected edge syndromes per walk and bounded hopping degree, so the summed small-tau remainder is controlled without an R^2 multiplicity. At fixed R this is also immediate from the finite matrix expansion.

## Gauge invariance and the required refined transfer

Closed return amplitudes of the signed first-order hopping are invariant under diagonal link-gauge transformations: endpoint phases cancel. This does not make an arbitrary effective-frame change invisible. Microscopic preparation and the final position/background-pole readout must be transported with the same canonical heavy and vacuum embeddings.

The old NATIVE_PROBE_LOOP_PROOF bound O_R,tau(lambda), and its O_R(lambda) difference between bare X preparation and the matched channel embedding, are larger than lambda^(L-4) for L>=10. They cannot be used to claim this resolved pole amplitude. A bare-spin protocol needs a separate high-order calculation.

A sufficient refined fixed-R argument is available:

1. Use exact analytic block identifications, or an approximate construction with errors beyond the desired amplitude order after evolution for time tau/(Jlambda). The longitudinal plane-parity sector of a single spin insertion selects the singleton/complement pair within N2 at any fixed even L; other interval lengths have different parity patterns.
2. Split the heavy effective evolution into its background-preserving part and background-changing insertions. A nonempty even set of changed background columns requires at least L-1 native insertions in a singleton hop. Thus a background-changing generator term first occurs at order lambda^(L-2) after dividing energy by Jlambda. At fixed tau its contribution to the return is O_R,tau(lambda^(L-2)), later than the claimed lambda^(L-4) amplitude.
3. The background-preserving return is diagonal in background labels. Exact plane symmetries make its value constant on the flat orbit, since initial and final particle position are the same and their symmetry phases cancel. Therefore its transition from the flat vacuum to an orthogonal pole vanishes; every such contribution inherits the vacuum/pole admixture of order lambda^(L-4).
4. The background-preserving return differs from its first-order signed-hopping value by O_R,tau(lambda). Applying that error only after the preceding cancellation gives O_R,tau(lambda^(L-3)), not the uncontrolled O(lambda) bound. Higher vacuum admixtures are also higher order. The endpoint pole differs from b0 by a vanishing power (at L=10 its relative-length tail is O(lambda^2)), so its effect on this leading amplitude is smaller as well.

These facts justify a fixed-volume, fixed-tau expansion with the displayed leading lambda^(L-4) amplitude. They must be included or explicitly invoked; a generic Duhamel estimate without the flat-orbit cancellation does not prove it. The background vacuum Hamiltonian and its slow phases are included in the background-preserving part and do not evade that cancellation.

## Limits and interpretation

Take lambda to zero at fixed admissible R and fixed sufficiently small nonzero tau, then expand the coefficient in tau. A simultaneous tau(lambda) limit requires comparing the refined higher-lambda error with lambda^(L-4)tau^4; it cannot be asserted merely because both parameters are small. The 1/R coefficient is the normalized momentum-zero pole overlap, not a volume-independent single-site emission probability.

The result concerns a conditional heavy return and a specified dressed neutral-pole readout in the prepared vacuum environment. It does not describe a relaxed heavy ground, an on-shell scattering channel, a decay rate, an unmonitored finite-time emission probability, or a universal coupling. Ground-sector selection and the pole's global-ground interpretation retain their separate fixed-size/ordered-limit qualifications.
