# ASSUMPTIONS_AND_IMPORTS — registrability-bridges-20260610

## Import ledger (what each surface supplies; role)

| surface | effective_status (origin/main) | role here | what it supplies | what it does NOT supply |
|---|---|---|---|---|
| `MINIMAL_AXIOMS_2026-06-05.md` (Record) | axiom node | foundation | durable realized-outcome registration: K/CPT orbit of realized central sector in a *supplied* readout context; finite scalar additivity I | readout context, decomposition, K/CPT structure, sector-generation rule, weighting, normalization, probability, P2/modulus, log-det, source/action, scale, observable identification |
| `tier_a_admissions.json` | audit-lane registry | target list | the two genuine admissions (AC_phi_lambda, theta) and the Record/scale reclassifications | — |
| `TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md` | unaudited (bounded_theorem) | the two blockers' source + the two lemmas | (L1) in a SUPPLIED det-class context, K/CPT kills the phase character k=0; (L2) AC_phi_lambda circulant conj maps delta->-delta, spectrum invariant | the readout context itself; exhaustiveness of the det-class; |delta|=2/9; species reading |
| `STRONG_CP_THETA_ZERO_NOTE.md` | retained_bounded | consumer of blocker (a) | bounded selected-surface theta_eff=0 on the theta-free Wilson+staggered scalar-mass surface | derivation that the action forbids CP-odd terms; derivation of positive-real mass orientation from primitives |
| `STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md` | retained_no_go | NO-GO already on the books | retained RP cannot derive "no bare theta slot" premise | — (this is about premise 1, NOT premise 2 / the mass orientation) |
| `KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` | retained_bounded | R2's named open lives here (Part D) | forced (1,2) transverse weights -> local density 2/9; local ABSS prereqs conditional on PL S^3 x R | the global Cl(3)/Z^3 -> PL S^3 x R identification (needs Perelman/Moise/van Kampen, named LIVE) |
| `ACPHILAMBDA_HW_COMPLEMENTATION_EQUIVARIANCE_SUPPORT_NOTE_2026-06-09.md` | open_gate (audited_clean) | finite support for blocker (b) | hw=1<->hw=2 complementation is C_3-equivariant bijection; symmetric circulant readouts assignment-blind; det depends on phase only via cos(3 delta); R-A/R-B/R-C rigidity | that hw=1 is physical; full-dynamics equivariance; species reading |
| `KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-09.md` | unaudited (bounded_theorem) | the |delta|=2/9 conditional chain | |delta|=2/9 conditional on R-eta (named readout identification) + carrier gate | unconditional |delta|; resolution of R-eta; the global PL bridge |
| `flavor_asymmetry_2over9_forced_weight_2026-05-31` | retained_bounded | forced-weight backing | (1,2) is the unique trace-free pair -> 2/9 | — |
| `three_generation_observable_no_proper_quotient_..._2026-05-02` | retained | R1b carrier backing (anti-rooting) | N=3 C_3 regular-rep carrier; no proper quotient | physical-species reading |
| `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` | (context) | det-class readout-atom context | tested four-cell fork: det_C readout atom is the holomorphic-polarization sibling of the (M)/det-class atom | a polarization selector |

## The shared core question (both blockers reduce to this)

Both blockers ask the SAME registrability question, phrased in two guises:

> **Q_reg.** Given ONLY the Record axiom boundary, what is the class of
> scalar readout functions registrable on a finite central-sector decomposition
> whose realized outcome is its K/CPT orbit?

- Blocker (a) needs: the physical `arg det(M_u M_d)` datum is exhausted by the
  multiplicative determinant-character class (so K/CPT evenness => phase-free).
- Blocker (b) needs: the registrable species surface is exactly the unordered
  mass multiset (so the `k -> -k` eigenvalue-label flip / `delta -> -delta` is
  not extra registrable content).

The Record axiom gives a sharp handle: in a supplied readout context, it
constrains scalar readouts by *finite scalar additivity* `I` over
pairwise-disjoint records, and the realized outcome is the *K/CPT orbit of the
central sector*. The central sector decomposition is the maximal abelian
(= central) part. Additivity plus the central (commutative, idempotent)
structure gives a finite additivity constraint over the central record labels,
together with a K/CPT (complex-conjugation) involution. This is the precise
axiom-constrained content. The question is what scalar readouts that data
permits without adding a new readout primitive.

## Counterfactual pass (for each implicit choice: what if wrong, what opens?)

| # | implicit assumption in the blocker notes | counterfactual | direction it opens | bounded by no-new-axiom? |
|---|---|---|---|---|
| C1 | "multiplicative determinant-character class" is the registrable family | what if a non-multiplicative registrable readout exists (e.g. additive log-modulus only, or an additive phase counter)? | the det-class would NOT be exhaustive; the hostile guard cos(arg z) is exactly such a non-multiplicative K-invariant; need to show non-additive phase readouts are NOT registrable under Record constraints | YES — the question is which readouts satisfy Record constraints, not which we may add |
| C2 | the registrable readout factors through the *spectrum* (eigenvalues) | what if the registrable readout sees the *ordered* eigenvalue list (a frame)? | blocker (b) would fail (sign of delta becomes content); but Record gives only the K/CPT *orbit* of the central sector — labels are not central data | YES |
| C3 | additivity I is over the central (sector) decomposition | what if a multiplicative structure (det) is NOT recoverable from additivity? | det = exp(sum log eigenvalues); the phase of det = sum of eigenvalue-phases is ADDITIVE over sectors; this is the bridge from additivity to the multiplicative character | YES |
| C4 | K/CPT is complex conjugation on the central spectrum | what if K/CPT is a different involution? | the supplied readout context fixes K/CPT as the adopted conjugation; the realized outcome is its orbit; so any registrable scalar is constant on K/CPT orbits = K-invariant (EVEN). This is the evenness the hostile guard warns is not enough by itself | YES (Record-constrained) |
| C5 | the det phase `arg det(M_u M_d)` is an action-level / non-multiplicative datum that might "remain relevant" | what if the strong-CP premise's `arg det` enters only multiplicatively (as the phase of a product determinant)? | by construction `arg det(M_u M_d) = arg det M_u + arg det M_d` is the SUM of sector phase-characters = the multiplicative character evaluated on the realized sectors; so it IS in the multiplicative class — the question is whether Record *registers* that sum-phase at all, or only its K/CPT-even part | YES |
| C6 | "unordered multiset" is the registrable species surface | what if occupancy/within-sector data is registrable? | Record explicitly excludes within-sector data and occupancy rule; so only the central (sector-labelled, unordered up to K/CPT) spectrum is registrable | YES (Record exclusion list) |
| C7 | R2 (PL/ABSS global bridge) is a *separate* registrability question | what if R2 is geometric (compactification type) and NOT a Record-registrability question at all? | KEY INSIGHT: R2 is the global *geometric* identification Cl(3)/Z^3 -> PL S^3 x R, which is about MANIFOLD TOPOLOGY (Perelman/Moise/van Kampen), NOT about what Record registers. So blocker (b) has TWO sub-parts: (b-i) the unordered-multiset registrability bridge (a Record question, shares the layer with (a)); (b-ii) R2 the PL/ABSS global bridge (a pure-math topology question, does NOT share the layer). The shared-layer theorem can close (a) + (b-i) but CANNOT close (b-ii). | (b-ii) needs external math, named LIVE, NOT a new axiom — its status is "import-required external theorem", an honest bound |

## Key structural finding from the counterfactual pass

**The shared layer is the Record-registrability of a multiplicative scalar
character on the central spectrum modulo K/CPT.** Counterfactuals C3+C4+C5
converge on a concrete theorem candidate:

> **Candidate T (shared-core registrability theorem).** In a supplied readout
> context, Record constrains scalar readouts by finite additivity over the
> central-sector decomposition and realized-outcome = K/CPT orbit. Therefore
> (i) every registrable scalar readout is constant on K/CPT orbits
> (K-invariant / even); (ii) an additive `R`-valued phase functional is odd,
> with no regularity assumption; (iii) combining (i)+(ii), the registrable
> additive phase datum (the determinant phase = sum of sector phases) is
> identically zero. Hence the determinant *phase* is not registrable content;
> only `|det|`/log-modulus-type even data can survive. This simultaneously
> (a) exhausts the det-phase
> readout for strong-CP and (b-i) reduces AC_phi_lambda to the unordered
> multiset by the same mechanism (the eigenvalue-label/sign flip is the K/CPT
> conjugation, whose odd part is unregistrable).

The HOSTILE GUARD is respected precisely because the theorem does NOT claim
"K-invariance => phase-free" (false: cos(arg z) is K-invariant). It claims
"K-invariance AND sector-additivity => phase-free", and it separately argues
that NON-additive readouts like cos(arg z) are NOT Record-registrable without
adding a new readout primitive. The two premises
together are what kills the phase; additivity alone allows the odd phase-sum,
K/CPT alone allows even non-additive functions like cos, but their
INTERSECTION (additive AND even) is the phase-free modulus class.

This is the theorem to build and stress-test. It must be checked that:
1. additivity genuinely forces oddness in the sector phase data without a
   hidden regularity/linearity assumption;
2. evenness plus oddness forces zero;
3. cos(arg z) and other K-even non-additive readouts are correctly excluded as
   non-registrable because Record constrains scalar readouts by additivity, not
   arbitrary functions of the spectrum;
4. the strong-CP `arg det(M_u M_d)` is genuinely the additive sector-phase sum
   (it is, by det multiplicativity) and carries no separate non-multiplicative
   action-level datum into the *registrable* surface.

## Forbidden imports for this loop

- Baseline = approved axioms/primitives plus retained/retained_bounded surfaces
  above; axioms/primitives are premises, not sources of bounded status.
- Forbidden: any new axiom; any new primitive; any new admission; any
  probability/weighting/normalization rule; PDG/fitted/measured/lattice-MC
  values as derivation inputs; the global PL S^3 identification as a granted
  handle (it is an external-math LIVE target, usable only as a named open or
  disclosed comparator, never as a derivation step).
