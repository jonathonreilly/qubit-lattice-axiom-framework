# ATTEMPT: tick and dissipative-sink physical boundary (J:derive:review-20261014-tick-and-sink-boundaries:a1)

Worker: Claude Sonnet 5.5, same family as the four source reports, no subagents, unrefereed.
Result class: PARTIAL, with one scoped new estimate (steps 8-12). No status words are claimed.

## Plain summary

A tick is a grid update rule that repeats in discrete steps. A one-handed tick drags a mirror-partner
along: the partner sits at "half a tick" of phase (quasi-energy pi). Whether the partner does anything
bad depends on three separate things, which the sources run together:

1. the partner's existence (kinematic: a counting fact about the update rule);
2. the state we put the world in (which half of the phase circle is filled);
3. the coupling and the speed of the boson that couples to it.

With a photon of speed c and a partner node of speed v, the vacuum can emit one photon plus a partner
pair only if c > v, with a rate proportional to (c^2 - v^2)/(c v). So the partner alone gives no gain.
Reverse the filled half of the phase circle and the same partner absorbs instead of emits. For the repo's
own tick (all nodes speed 1) emission and absorption are exactly equal and both are shut for c <= 1.
For the single-light-Weyl Wilson tick, emission is open for every photon speed above 1/5 while light-node
absorption is shut up to c = 1. The tick's own dynamics, the photon speed and any record sink are all
supplied; none follows from Record.

## 0. What I read (state it plainly)

- Current main `docs/MINIMAL_AXIOMS_2026-06-29.md`, all 233 lines. Relevant: Lattice (:35-41), Qubit (:43-53),
  Admissibility supplies a distribution, not dynamics (:55-73, :114-123), Record (:75-83), decoherence
  mechanisms / record production dynamics / time metric are outside the axioms (:173-190).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, all 130 lines. Approved primitives: scale_reference,
  kinetic_isotropy (c_t = c_s for the matter kinetic normalisation, :58-96), realized_state (pointwise evaluation of a
  supplied state, no state selection, :98-129).
- The four source objects at `dd7d358c6f6b0fd049b46962970397dbdc7d2e1f`; all four sha256 verified (RECOVERY_STATUS.json).
  The branch has since moved to `4b306b21e0`; the four objects are byte-identical there.
- `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md:40-75` (N1-N4, the landed gamma5 statement).
- Open PRs (read titles, bodies, file lists): #10070, #10072, #10064, #10033 (see Overlap below).

Layers kept apart throughout:
- AXIOMS SAY: records form; one record per site, permanent (:75-83); the distribution at a site is set by
  its neighbours (:55-61). Nothing about ticks, photons, Lindbladians, vacua or sinks.
- LANE SUPPLIED: a free two-band tick on Z^3, an arc vacuum, a Peierls coupling, a boson speed c.
- PROVED / CHECKED here: only the conditional statements below.

## 1. Setting and premises [ASSUMED unless marked]

P1. Sites Z^3 with M_2(C); the one-body tick U(k) = a(k) - i b(k).sigma in SU(2), C^1 (quasi-local allowed),
    nondegenerate nodes {b = 0}. The tick is a supplied comparator (AX:114-123: no dynamics is supplied).
P2. Fermionic Fock space of U (free many-body tick), arc vacuum fills quasi-energy in (-pi,0] (U = e^{-i eps}).
    The state is supplied (realized_state primitive: no selection rule, no default state).
P3. Coupling (only for steps 8-12): minimal (Peierls) substitution k -> k - eA in U, all nodes carry the same
    charge e (as in the sources' "identical charges" A1(iv)), slow transverse boson of isotropic speed c
    with L = (1/2)(A_dot^2 - c^2 (grad A)^2), hbar = 1, tick = edge = 1. First order in e. Cone regime
    omega, q much smaller than the node scale.
P4. Premises of the outside view that are NOT used: interacting vacua, non-Gaussian states, non-quasi-free sinks.

## 2. T_d (reading of F6:70-81 against landed N3) [CHECKED, exact integer arithmetic, check.py A1-A9]

- On Z_4^3: T_d^2 != 1, T_d^4 = 1, (1+T_d)/2 is not a projector (A1-A3).
- Eigenvalues are i^(m1+m2+m3), 16 each (A4). They are +-1 on 32 momenta, of which only 8 are corners (A5-A6).
  So "(-1)^hw" holds on the 8 corner momenta only; the +-1 spaces are not corner spaces.
- The object that IS an on-site involution is eps(x) = (-1)^(x+y+z): eps^2 = 1, T_d eps T_d^-1 = -eps, and
  {H_walker, eps} = 0 (A7-A9). eps pairs k with k+Q, i.e. it exchanges node hands. It is not a gamma5 in the
  sense of N3 (gamma5^2 = I, anticommutes with sigma_i on one site): consistent with K3 :134-141, no contradiction
  with the landed N1-N4.
Status: recovered and re-verified exactly; K3 already states the conclusion.

## 3. Two-band node sum rules with exact hypotheses [PROVED (standard) + CHECKED]

Hypotheses: free, translation invariant, two bands, U in SU(2), C^1, nondegenerate nodes. E := (i/2)(U - U^+) = b.sigma.
- (i) [E, U] = 0 and E has the range of U. PROVED (one line).
- (ii) E-chirality at a node equals +chi if a = +1 and -chi if a = -1 (sign of det of the Jacobian, det(-J) = -det J in 3 dimensions). PROVED.
- (iii) Sum over eps = 0 nodes of chi equals the sum over eps = pi nodes (both equal the degree W3), and the E-chirality sums to 0
  (Nielsen-Ninomiya on b.sigma). Degree equality is the standard degree-theory fact (F3 A1, comparator Bessho-Sato); I did not re-prove it.
- CHECKED exactly (Fractions, 10 values of the mass parameter mu; B1): the node sums obey (iii) for
  U_mu = (m - i d.sigma)/sqrt(m^2 + |d|^2), m = mu + sum cos k_j, d_j = sin k_j.
  For mu = -2 (B2-B4, symbolic Jacobians B5-B6): exactly one eps = 0 node (k = 0, speed 1) and seven eps = pi nodes with
  speeds {1,1,1,1/3,1/3,1/3,1/5}; net chirality +1 at eps = 0 and +1 at eps = pi; the E-chirality of the pi nodes sums to -1.
Not new (F3 A1, R1). The new content is only the exact node-speed data (B5, B7) used in steps 10-11.

## 4. Mass-term index conservation does not cover every free tick [CHECKED, counterexample]

The index lemma (F6 Lemma 2) is about a finite-dimensional unitary G-representation V of left-handed Weyl content with a G-invariant symmetric
mass form; vector-like V gives vector-like massless content. Its hypotheses are Hermitian, one spectral level, V given.
- The tick U_(mu=-2) has net chirality +1 at quasi-energy 0 (B3): the content at eps = 0 alone is not vector-like.
- The lemma is not violated: the other seven nodes (net +1 on the pi side, net -1 in E-chirality) sit at a second quasi-energy.
  The lemma then says: if V is taken to be all nodes at both levels, the E-chirality is 0 (B4). The question "is the pi slice part of the
  light V" is a state-and-coupling question (steps 8-12), not an index question.
Status: re-states K3 :164-172 with a checked example. READING for the application; the lemma itself is standard.

## 5. Static backgrounds: the branch (b) of F3's dichotomy is automatic [PROVED, CHECKED exactly (D1-D2)]

Claim. For any finite-band (or any bounded normal) unitary one-body tick U[A] in a time-independent background A, E[A] = (i/2)(U - U^+) is
Hermitian, has the range of U[A], commutes with U[A], and equals sin(eps). The arc vacuum is exactly the zero-sea of dGamma(E[A])
(eps in (-pi,0) iff E < 0). So a static background produces no pair creation and no inversion relative to E[A].
Check: exact rational Cayley unitaries (n = 3,4,5): U U^+ = 1, [E,U] = 0, E = 2H/(1+H^2); sin(2 atan h) = 2h/(1+h^2).
Scope: this changes the hypotheses under which F3 A3(b) vs K3 finding 1 apply. K3's "no exactly conserved E'" needs a dynamical boson (time-dependent
coupling); with static fixed A the conserved E[A] always exists. Under static E (or B) the pi slice responds as an E-Weyl point of opposite hand (step 3(ii)).
NEW as a stated scope boundary (the algebra is elementary).

## 6. K3 finding 1 [READING, not re-proved]

K3 :72-84 argues first order in e that a dynamical massive boson at rest forces E'_b(Z) = +2c_0 and -2c_pi simultaneously, so no exactly conserved
A2-class E' exists. I did not re-derive it. Its hypotheses (free two-band, one-body E', boson one-body conserved quantity, first order) are the
class of this attempt; interacting E' with no one-body form is outside it, and step 5 shows the dynamical hypothesis is essential.

## 7. Photon coupling and what is state-independent [ASSUMED P3; READING]

At a node with U ~ a - i b.sigma, Peierls coupling gives, to leading order, the cone Hamiltonian +-(J k).sigma with vertex e (J)sigma.A. At an eps = pi
node (a = -1) the excitation quasi-energy of a pair with |b| = theta_1, theta_2 is -(arcsin|b_1| + arcsin|b_2|) mod 2 pi (CHECKED L2), so a pair there
is a pair of negative excitation phase relative to the arc vacuum. The vertex matrix elements are those of the same cone (assumed; F3 R1-F2 and K3-T1
measured |M|^2 = 2 at both node types for U_g, a consistency check of the assumption, not a proof for other ticks).

## 8. Cone spectral function and emission rate [PROVED (derivation in check.py E1-E7) + CHECKED (Q1)]

For H = v sigma.p with charge e, hole in the lower band at k, particle in the upper band at k+q, transverse polarisations eps perp q:
- sum_eps |<u+(k+q)| eps.sigma |u-(k)>|^2 = 1 + (q^ . n)(q^ . n') (E3, exact spinor algebra);
- with u = r_1 + r_2, w = r_1 - r_2 (r_1 = |k|, r_2 = |k+q|): this equals (u^2 - q^2)(q^2 + w^2)/(q^2 (u^2 - w^2)) (E1), and d^3k = (2 pi r_1 r_2/q) dr_1 dr_2 (E2);
- hence S_T(omega,q) := 2 pi e^2 v^2 int d^3k/(2 pi)^3 [..] delta(omega - v(r_1+r_2)) = e^2 (omega^2 - v^2 q^2)/(6 pi v), for omega >= v q (E4-E6);
- the golden-rule rate per volume for one inverted cone into a boson of speed c is
  R = int d^3q/(2 pi)^3 S_T(c q, q)/(2 c q) = e^2 (c^2 - v^2) q_max^4/(96 pi^3 c v) = alpha (c^2 - v^2) q_max^4/(24 pi^2 c v), e^2 = 4 pi alpha (E7).
- Q1 is an independent floating-point quadrature with explicit eigenvector spinors on the ellipsoid, at three (v,q,omega): relative error <= 5e-12.
The pair threshold is omega = v|q| (triangle inequality, collinear pair); the weight vanishes there, so the c = v case is zero at this order.
L1 (floating point, 0.5%): the lattice pair threshold near each of the eight corners of U_(mu=-2) equals v|q| at |q| = 0.02 in two directions.

## 9. State dependence: gain is a statement about the filled arc [PROVED, exact (F1-F4)]

For one transition with hole-side occupation n_v and particle-side occupation n_c and boson occupation n:
dn/dt = A [ (n+1) n_c (1 - n_v) - n n_v (1 - n_c) ].
- normal sea (n_v = 1, n_c = 0): dn/dt = 0 at n = 0, stable.
- inverted (n_v = 0, n_c = 1): dn/dt = A (n+1) > 0 for all n: spontaneous plus stimulated, no stationary photon number.
- infinite-temperature fermions (1/2, 1/2): dn/dt = A/4 > 0: stimulated terms cancel, spontaneous remains.
- stationary n* = n_c (1-n_v)/(n_v - n_c).
So "inverted" is a property of (arc, quasi-energy folding), i.e. of the state. The complementary arc (0, pi] swaps which sector emits.

## 10. Node data and thresholds for two concrete ticks [CHECKED exact, G1-G7, C1-C2]

f(c,v) := (c^2 - v^2)/(c v) for c > v, else 0; rate per node = alpha q_max^4/(24 pi^2) f(c,v).
- U_g (rebuilt from the description F3:70-76; C1: U_g(k+Q) = -U_g(k) exactly, C2: speed exactly 1, isotropic, at all 8 corners):
  emission (4 pi nodes) = absorption (4 eps = 0 nodes) for every c; both vanish for c <= 1. At c = v = 1 (knife edge) the first-order process is closed.
- U_(mu=-2), arc (-pi,0]: emission weight sum_pi f; absorption = f(c,1) from the one light node.
  c <= 1/5: nothing. 1/5 < c <= 1/3: the speed-1/5 node only. 1/3 < c <= 1: add the three speed-1/3 nodes (c = 1: 64/5 total). c > 1: add the three speed-1 nodes and the light node absorbs.
  c = 1/4: 9/20; c = 1: emission 64/5, absorption 0; c -> infinity: emission/absorption -> sum_pi (1/v) / (1/v_0) = 17 (G4).
  K3-T1F measured 17.0008 for the uniform-field (q = 0, i.e. c -> infinity) limit: that is the same number, now with its finite-c deformation.
- complementary arc (0, pi]: at c = 1 emission 0 and absorption 64/5 (the pi nodes decay photons, the usual c > v decay) (G5).

## 11. Separation of the three things the task asks to separate

(a) Kinematic pi partner: PROVED (step 3) for the two-band class. It fixes node counts, hands and speeds. It carries no sign of gain.
(b) Actual gain / emission: depends on (arc, c, node speeds, vertex). PROVED/CHECKED in steps 8-10: open iff c > v of an inverted node;
    net stimulated gain = (inverted-sector weight) - (normal-sector weight). Zero for U_g; positive for U_(mu=-2) at c <= 1 before light absorption opens.
(c) Vacuum choice: PROVED (step 9). Choosing the complementary arc swaps which sector emits and which absorbs (check G5). F3's statement that an arc filling
    always leaves one inverted gapless boundary (F3 :85, :283) is not contradicted: the complementary arc inverts the eps = 0 node(s) instead. What changes is
    which node set (and which speeds) carry the emission, so for mu = -2 at c <= 1 the complementary arc has no first-order emission at all, only photon decay.
    Non-arc, interacting and non-Gaussian vacua are outside the class and are NOT excluded here.
The axioms select none of arc, c, vertex or tick (AX:114-123, realized_state: no state selection).

## 12. Reading of kinetic_isotropy [READING]

The primitive normalises c_t = c_s for matter. If the boson inherited the same normalisation (not supplied), U_g would sit exactly on the knife edge c = v and
the first-order rate would be zero; second order would then control. This is a statement about what is not supplied, not a result.

## 13. Dissipative sinks and records [READING + CHECKED toy (H1-H2)]

- AX:75-83 says records form, one per site, permanent, readable. AX:114-123 and :182-186 put update laws, decoherence and record-production
  dynamics outside the axioms. A Lindblad sink is therefore a supplied comparator. F5's Lemma D (a capacity bound) needs the extra premise H-rec:
  every jump writes one permanent record at a site. K3 :247-252 already says D is not load-bearing; I agree and add the exact toy: one filled mode under pure loss emits exactly
  one jump in total (H1), so N filled modes use N sites; a gain-containing sink with steady rate r exhausts a one-per-site register at T = 1/r (H2). Both statements hold only under H-rec.
- Alternatives outside the supplied class that are preserved, not closed: H-rec false (jumps are not records); register per event rather than per site; non-analytic
  jump symbols; non-Gaussian sinks. F5's Lemmas B, P and the Planck-conductivity result (T3') are not re-derived here.

## 14. FIRST UNRESOLVED STEP

The emission/absorption rates (steps 8-10) are cone-level, first-order, free, two-band, with an assumed Peierls vertex (premise P3) and an assumed
isotropic boson of speed c. Unresolved, in this order:
1. the vertex of an actual tick away from the cone (and for multi-band ticks): only U_g's vertex has been measured by the sources (|M|^2 = 2);
2. what fixes c (and q_max) in the framework: nothing supplied;
3. the lattice-scale coefficient (the q_max^4 factor is a cone cutoff, not computed on the lattice);
4. interacting vacua and a multiband proof of node-speed data;
5. F5 Lemma P/C and the Planck-conductivity result were not re-checked.

## 15. New versus recovered

Recovered, not new: T_d facts (K3), node sum rules and the identity E = sin H_F (F3 A1), index lemma (F6), K3 finding 1 (not re-proved), the factor 17 (K3-T1F), Lemma D and its non-load-bearing status (K3).
New (same-family, unrefereed, scoped to P1-P3): the exact cone spectral function and the finite-c threshold/rate, the c = v knife edge for U_g, the arc-reversal swap, the static-background conservation boundary, and the node-speed data of the mu = -2 tick.

## 16. Overlap and kill pass

- Open PRs #10070, #10072 (family-class tick FREEZE; pi partners are same-hand doublers; every no-Fermi-surface filling has an inverted boundary; doubler map gives complement vacuum and zero vacuum polarisation for S-even probes) overlap steps 3 and 11 in content for a different tick; #10072 lists "decay rates" as not covered, which steps 8-10 supply for the two-band class. #10064 and #10033 are adjacent (slab, glide). None is landed. My search of landed docs was by filename and grep, not exhaustive.
- Kill: (i) the pair continuum could be wider than the cone: only the leading cone is used, stated. (ii) The photon could be massive: not covered (a massive boson at rest is always on shell, K3 :118-119). (iii) c could be position dependent: not covered. (iv) A different gauge vertex would change the weight, not the threshold c > v (threshold is kinematic). (v) The sign of E-chirality at pi nodes is irrelevant to rates.
- Not a proof for interacting dynamics; not a statement about stability of nature.
