---
claim_id: recording_every_site_including_rishons_and_edge_registers_changes_no_odds_level_prediction_and_no_record_of_one_half_tick_empties_a_support_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Under a candidate actuality law with zero premise weight (one actual configuration, distributed as its odds and moved by the exact fewest-change transport; records never condition the odds), three candidate record rules (unapproved proposals with zero premise weight) are compared: (i) bound sites excluded, as in the source branch's actuality law; (ii) every site recorded each half-tick, rishons and edge registers included; (iii) as (ii), but a record that would leave some site with an empty admissible support cannot form. Theorems: the actual configuration always lies in the odds' support, so no set of records of one half-tick leaves any site without a possibility, and the clause in (iii) never blocks a record in any formation order (runner: 0/12000 formations in random orders); a value forced by records equals the actual value; in a gauge-invariant state the record law of colour-component occupations is the same in every gauge-rotated basis. Finite diagnostics: on a U(1) quantum-link ring (4 matter + 8 rishon modes, Gauss sector dimension 7, K = 4000 histories, 10 half-ticks), matter records are bit-identical under (i), (ii) and (iii) (by construction, since the transport reads no record set), joint records are Born (max z 2.5) and every recorded pattern satisfies Gauss's law (0/44000 violations); one rishon record fixes its link partner (4000/4000); one free matter record already fixes another, otherwise open, site through Gauss's law (1777/4000), so the justification of (i) fails on matter; latest records mixing half-ticks give empty supports (6751/10000), current ones never do; with every link site recorded an emitter decays at the Wigner-Weisskopf rate whatever the half-tick (0.189 at dt 0.05 and 0.02, 2g^2/J = 0.180); a single photon through a link-site Mach-Zehnder keeps V = 1.000, arm records never coincide (g2(0) = 0, by construction of the one-photon configuration space); repeated link-number records agree (1.000) with |<a>| unchanged, and a dispersive pointer in the odds gives the decoherence (0.805 to 0.569); a recorded oscillator mediator whose coupling is calibrated from the target phase (gm = sqrt(dphi/(16 pi))) reproduces the imposed concurrence 0.1563 by construction (inner phase 0.791 rad, dphi 0.314), an imposed-phase toy check and not an independent gravity prediction. Contrast: if records conditioned the odds, matter frequencies would move 0.45 off Born, decay would be Zeno-frozen (2p lifetime ~3e16 s at a Planck half-tick, estimate), fringes would vanish (V 0.005) and the mediated concurrence would fall to 0.0075. Toy models and couplings are supplied; the hydrogen estimate compares two supplied alternatives only; no 3D lattice, no CL-1 cube tick, no non-abelian dynamics. The proposed CL-2 text and the proposed replacement of the Record axiom's wording are unapproved proposals with zero premise weight."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/recording_every_site_including_rishons_and_edge_registers_changes_no_odds_level_prediction_and_no_record_of_one_half_tick_empties_a_support_2026_10_22.py
---

# Recording every site, rishons and edge registers included, changes no odds-level prediction, and no record of one half-tick empties a support

Claim type: bounded_theorem.

Axiom text is quoted from the current [axiom memo](MINIMAL_AXIOMS_2026-06-29.md) on `main` and is not edited.
- Admissibility: "For each site, the probability distribution over the possibilities is determined by, and varies with, the neighborhood conditions." Reading note (3): "The distribution is a probability measure on the local possibility domain; "available"/"admissible" denotes its support -- on finite menus, exactly the possibilities of nonzero probability." (Dated history: when this note was written on 2026-10-22 the memo read "the nearest-neighbor conditions". The arguments here use only the support reading, so nothing below depends on the change.)
- Record: "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."

Candidate laws used (conditional, zero premise weight; none is adopted). CL-1 to CL-3 here are the three-law numbering of the source branches; they are not the clauses of the [candidate-law register](CANDIDATE_LAWS.md) on `main`, whose CL-1 to CL-3 aliases are other clauses (lossless influence, record removal, conservation). CL-2 here is the actuality law: one actual configuration, distributed as its odds, moved each half-tick by a support-confined fewest-change transport (here the exact LP plan of clauses (i) to (iii) of [the transport note](SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md), without its maximum-entropy step); records copy the actual occupation and never condition the odds; past records are read only through pointers ([pointer note](RECORDS_THAT_NEVER_CONDITION_THE_ODDS_GIVE_NO_ZENO_FULL_FRINGES_AND_CHSH_2_SQRT_2_WHILE_BARE_TWO_TIME_RECORDS_NEED_A_POINTER_BOUNDED_THEOREM_NOTE_2026-10-22.md)). CL-1 with CL-3's phase is the supplied unitary update of the odds; here only the supplied half-tick unitary enters.

That candidate actuality law excludes bound sites from records. The reason given was that a lock may fix no other site's possibility. The owner has suggested a different reading (reported on the source branch; a reading to test, not an adopted rule): locking one site may leave a neighbour, or another site, with one possibility, or none. This note tests three record rules as equal candidates against measurement:
- (i) bound sites excluded, as in that candidate law;
- (ii) every site recorded;
- (iii) every site recorded unless the record would leave some site with an empty support.

## Theorems (exact)

T1. Support. The transport uses only transitions along nonzero elements of the half-tick, and it carries the odds to the odds. So every actual configuration it reaches has nonzero odds. The records of one half-tick copy that configuration. Locking any subset of them therefore leaves every site at least one possibility: the actual value. "No possibility" never arises. Read as a formation rule, the clause in (iii) never blocks a record. The two readings of the owner's "or no possibility" (forbidden, or allowed but inconsistent) cannot be told apart, because neither ever applies (A1, A7).

T2. Forced values. If the records leave some site only one possibility, that value is the site's actual value (T1). It is a definite value fixed by records and the rule, but it is not a record: "Records form", whereas this value is inferred. Its readout law is the Born law of the union of recorded and forced sites (A4, A5). Whether it counts as a record has no effect on any readable distribution.

T3. Record-set independence. The odds change only by the update (CL-1 together with CL-3's phase), and the transport reads odds alone. So the actual histories, and with them the values that every rule records, do not depend on which sites are recorded. All three candidates give the same matter record law, bit for bit. The only difference between them is the readable set. This is structural: the runner's transport takes the odds and the half-tick and never a record set, so the runner prints it as a structural line (A10), not as a counted check.

T4. Gauge safety. If a state is invariant under a gauge rotation g, the Born law of the occupations in the g-rotated basis equals the law in the original basis. So records of colour components of non-abelian rishons are as safe as records of matter colour components (A8: singlet 2e-16; non-singlet control 0.58).

## Finite diagnostics

The A runs use a U(1) quantum-link ring with 4 matter sites and 8 rishons, Gauss sector (2,1,2,1) of dimension 7, w = 1, m = 0.5 and dt = 0.35. There are 10 half-ticks and 4000 histories, moved by the exact LP transport.
- Born (A2). Matter records give max z 1.71 and joint records 2.54. Recorded patterns violate Gauss's law 0 times in 44000. Once rishons are recorded, Gauss's law holds among the records themselves. That is the reading of the Gauss-law note on main, which needs link records.
- Constraint propagation (A4). One rishon record fixes its link partner (4000/4000). A matter record plus one rishon record fixes the other rishon (4000/4000). Matter records alone fix 25896 of 32000 rishon values, and every forced value equals the actual value.
- Candidate (i) fails its own reason (A9). A single record of a FREE matter site leaves some other, otherwise open, site one possibility in 1777/4000 samples, through Gauss's law. "A lock fixes no other site" would exclude matter as well, and then nothing would be readable. The bound/free test passes matter only because a Gauss cluster is not a mirror pair.
- Stale records (A6). Latest records that mix half-ticks, with some sites refreshed and the rest held from the start, give empty supports in 6751/10000 samples. Current records give none in 10000. So an empty support signals a rate rule whose latest records are not current, which is how the role-change-only and once-ever rules failed in neighbourhood-roles. The no-empty-support clause is a consequence of the law, not a separate condition.
- Contrast (A3). If records conditioned the odds, matter frequencies would move off Born by 0.47 with every site recorded and by 0.45 with matter only recorded. This is the definite-links failure.

Photons (B), every link site recorded at every step:
- B1. An emitter on a chain (g = 0.3, J = 1) decays at the fitted rate 0.189, against 2g^2/J = 0.180, for dt = 0.05 and for dt = 0.02 alike. If records conditioned the odds, the rate would be 0.0045 and 0.0018, falling as the half-tick shrinks (Zeno).
- B2. A single photon in a Mach-Zehnder of link sites gives V = 1.000. Conditioning gives V = 0.005. Each actual track carries a bare which-arm record together with full fringes. As for matter (bell-records), such records are read only through pointers under the candidate pointer clause.
- B3. Arm records never coincide (0/24000), so g2(0) = 0, as measured for single photons. This holds by construction, since a configuration holds the one photon on one site; the computed part is P(arm u) = 0.496. Definite or classically mixed links would give g2 >= 1 (definite-links).
- B4. Repeated link-number records agree at every half-tick (1.000), so counting is non-demolition, and |<a>| is unchanged (0.805). The measured decoherence comes from a dispersive pointer coupled in the odds: 0.805 drops to 0.569 at a phase of pi/2 per photon.

Mediated entanglement (C1, C1b). Calibration: the oscillator coupling is set from the target phase before the oscillator runs, gm = sqrt(dphi/(16 pi)). Completing the square in H = a^+a + gm (z_A + z_B)(a + a^+) gives, after one period 2 pi, the branch phase 2 pi gm^2 (z_A + z_B)^2, so the two-qubit phase combination is 16 pi gm^2 = dphi and the concurrence is |sin(8 pi gm^2)| = |sin(dphi/2)|. Agreement with the target is therefore imposed by the calibration; it is not an independent gravity prediction. The calibration control C1b sets gm' = 1.25 gm: the toy then gives 0.2428 = |sin(8 pi gm'^2)|, not the target. The BMV inputs (1e-14 kg, 200 um, 250 um, 2.5 s; inner phase 0.791 rad, dphi = 0.314, target 0.1563) are supplied comparison inputs. What the toy does test, inside that calibration: the mediator, recorded at each of 200 half-ticks per period, stays indefinite mid-run (P(n>0) = 0.0475), returns (overlap 1.000000) and leaves the two branch qubits with concurrence 0.1563, while with conditioning records the concurrence is 0.0075. The mediator stands for an edge register (gravity) or a link (a Coulomb gate). So, in this calibrated toy, recording the mediator every half-tick keeps the imposed-phase entanglement and conditioning records remove it.

## Estimate against measurement

With records conditioning the odds at a Planck half-tick, the hydrogen 2p decay rate would be suppressed by about t_P (c/a0)/(2 pi). The lifetime would then be about 3e16 s, against the measured 1.60 ns. Under (ii), and under every candidate rule compared here, the toy decay is at the Wigner-Weisskopf rate. Of the two supplied alternatives (records that never condition the odds, and records that condition them at a Planck half-tick), this estimate disfavours the second. It does not select a record law in general, and it does not distinguish record sets. The 1.60 ns lifetime, a0 and t_P are supplied comparison inputs.

## Verdict

- All three candidates tie on Born statistics, photon counting (g2, fringes, non-demolition repeatability, decay), Gauss's law in the actual configuration, and the imposed gravity-entanglement phase of the calibrated toy (C1). They tie because no candidate law here reads records (CL-1 and CL-3 act on the odds, and CL-3 on the source branch no longer has a 4-volume-per-record clause).
- (i) fails internally. Its reason excludes matter too (A9). It needs a supplied set form (|A| <= 2) and a tolerance. On a finite ring a set pair covering the whole matter ring binds every site (a finite-size artefact reported by edge-register-bound, PR #9989, which does not claim a closed-universe version). It also keeps Gauss's law and link values unreadable.
- (iii) ties with (ii) and adds an idle clause (T1, A7).
- (iv), the candidate found here (an unapproved proposal): records copy the actual configuration. The no-empty-support property and constraint propagation then follow as theorems.
- Recommended for comparison, as an unapproved proposal with zero premise weight: (ii) in that form. It deletes the bound/free condition and the edge-register placement clause's role in records.

Proposed CL-2 text for the source branch's candidate law (an unapproved proposal with zero premise weight; replacing the two sentences from "Each site that is free ..." to "... gets no record."):

> "Each site then gets a permanent record of its occupation in the actual configuration: a new site's first record comes at the half-tick after it appears, and a removed site keeps its records."

Proposed replacement of the Record axiom's wording (an unapproved proposal with zero premise weight; changing an axiom is the owner's decision alone, and nothing in this note uses this wording as a premise):

> "A record locks exactly one admissible local possibility at its own site, the site's value in the actual configuration. Through the admissibility rule this may leave other sites with one possibility; it never leaves a site with none. A removed site keeps its records."

## Anti-smuggling gate (rule (ii))

1. Measured numbers chosen: none. The BMV inputs (1e-14 kg, 200 um, 250 um, 2.5 s), the 1.60 ns lifetime, a0 and t_P appear only as test inputs and estimates; the C1 toy coupling is calibrated from the BMV inputs (C1). The rule contains no number.
2. Observed structure inserted by name: none. The rule refers only to sites, occupations, records and the actual configuration. It does not mention rishons, links or edges; it removes the role-based clause.
3. A prediction it was not built for: the emitter lifetime is independent of the half-tick, which is consistent with 1.60 ns. Repeated link-number records are non-demolition, with decoherence only from pointers. Gauss's law holds exactly among each half-tick's records. Honest caveat: these follow from "records never condition the odds" and hold under (i) too. The only content that distinguishes (ii) from (i) is the readable set, which no measurement tests. That part is UNTESTED.
4. Axiom conflict: rule (ii) records each site at every half-tick, which conflicts with the Record axiom's "A site never carries more than one record". The conflict is inherited from the candidate CL-2's one record per site per half-tick and is extended here to every site. Rule (ii) is usable only under an axiom change that the owner alone can make; this note neither makes nor assumes one.

## Smuggling review

- Supplied: the toy Hamiltonians and sizes; the couplings w, m, g, J and dt; the Mach-Zehnder layout; the probe phase; the oscillator mediator (d = 14) and its coupling gm = sqrt(dphi/(16 pi)), calibrated from the target phase; seeds; tolerance.
- Forced: T1 to T4, record-set independence, forced = actual, and the idle no-empty-support clause.
- Not derived: a 3D cube-tick version; non-abelian dynamics; the record count per cell (edge registers add about 0.13 records per cell per half-tick at s = 135, b_e = 40, per edge-register-bound, which affects nothing because no law reads counts).

## Dependencies

- Used:
  - neighbourhood-roles (PR #9970): the bound rule, the LP transport form and the quantum-link ring;
  - edge-register-bound (PR #9989): pair totals, the covering artefact, BMV numbers;
  - [the formation-law note](RECORDS_NEVER_CONDITION_THE_ODDS_FORMATION_LAW_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-10-21.md) (PR #9873);
  - bell-records, [the pointer note](RECORDS_THAT_NEVER_CONDITION_THE_ODDS_GIVE_NO_ZENO_FULL_FRINGES_AND_CHSH_2_SQRT_2_WHILE_BARE_TWO_TIME_RECORDS_NEED_A_POINTER_BOUNDED_THEOREM_NOTE_2026-10-22.md) (PR #9930): the pointer clause;
  - definite-links (g2 >= 1, definite-link failures);
  - photon-records (PR #9887).
  PRs #9970, #9989 and #9887 are not on `main` or this branch; their scopes are recorded only in the source map of `docs/RECORDS_BORN_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`. The definite-links note is not in this repository and is not in that map; its two inputs here are named, not checked.
- Consistent with: [the Gauss-law-as-support-condition note](THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md) on main.
- Contradicted: the neighbourhood-roles C1 justification for excluding bound sites (A9).

## How to run

python3 scripts/recording_every_site_including_rishons_and_edge_registers_changes_no_odds_level_prediction_and_no_record_of_one_half_tick_empties_a_support_2026_10_22.py

The runner needs numpy and scipy and declares AUDIT_TIMEOUT_SEC = 120. It runs in about 3 s at about 80 MB resident, prints about 6.4 kB and ends with TOTAL: PASS=15 FAIL=0. It exits nonzero on any failed check. A10 is printed as a structural line and not counted; C1b is the calibration control. Its cache was produced with `scripts/runner_cache.py` on this branch.
