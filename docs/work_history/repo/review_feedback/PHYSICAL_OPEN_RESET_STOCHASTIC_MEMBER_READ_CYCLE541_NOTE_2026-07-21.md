# Physical open-reset stochastic member-read comparator — Cycle 541 note (2026-07-21)

Authority: none
Audit: unset
runner SHA-256: 2101f9cc0dbf8fefafecd08205b4af4618bbaddf1130fe2bbb593b5abb4246a4

## Question and result boundary

Cycle 541 asks for a capacity-counted open reset/entropy export mechanism, a separately typed stochastic kernel and genesis measure, and a law-owned read that feeds the exact Cycle-531 occurrence interface without host RNG or host branch choice.

The constructive object is a finite four-trial reversible dilation. A 125-state active bath is followed by three fresh 125-state environment cells. A fixed read table assigns exactly 25 microstates to each of five members. At every trial the pointwise member and receipt feed the exact Cycle-531 binder; one append-only candidate-output slot is written; then a pointer-controlled SWAP displaces the old active microstate into the used environment cell and brings its fresh microstate into the active bath. Three fresh cells therefore support four reads including the initial active state. The lawful domain rejects a fifth forward read.

The stochastic content is separate supplied structure. For each train/held preparation, a candidate p=q categorical stochastic kernel is declared. A supplied 125-microstate genesis measure assigns q(label)/25 to each microstate in that label block, and a supplied four-cell product independence law assigns the tensor-product measure to the initial active bath plus three fresh cells. The measure, stochasticity, independence, and p=q are not inferred from the physical permutation. The law-owned read maps a realized microstate to one actual member, but its ontology is also supplied. Thus p=q remains a candidate and rejectable calibration, not Born.

## Physical compiler and environment M2

The imported Cycle-531 port/interface occupies 176 M2. Cycle 541 adds:

- 125 active-bath M2;
- three fresh/spent environment cells of 125 M2 each, totaling 375 environment M2;
- four one-hot trial-pointer M2;
- 40 append-only candidate-output M2: four filled receipts, twenty member rails, four occurrence bits, and twelve content bits.

The total is 720 M2, with 544 new M2. The fixed schedule contains 1,798 logical gates:

- 250 CNOTs emit the active-bath member and law receipt;
- the exact 62-gate Cycle-531 forward binder;
- 40 bounded output gates;
- the exact 62-gate Cycle-531 reverse binder;
- 250 CNOTs unemit member and receipt;
- 1,125 gates implement three pointer-controlled 125-rail SWAPs;
- nine CNOTs advance the four-state pointer.

Every displayed primitive acts on at most three M2. The member table and physical schedule are independent of q and identical on train and held preparations. The physical-schedule source audit rejects random, choice, sample, argmax, and multinomial calls. There is no runtime host branch choice.

The initial state is explicit: one one-hot active microstate, three one-hot fresh environment microstates, one one-hot pointer at slot zero, blank candidate output, blank member/receipt/binder scratch, and the imported binding/current/K fixtures. These constraints and the product genesis measure are supplied; autonomous constraint or mixture preparation is not derived.

## Entropy, mutual information, reset work, and erasure

For a preparation with member entropy H(q), the supplied microstate measure has entropy H(S)=H(q)+log2(25). The fixed read is deterministic, so I(S;member)=H(q). Under the supplied product genesis measure, the next fresh sample has zero mutual information with the prior member. After the controlled SWAP, the new active sample remains independent of the prior member, while the spent environment cell carries the old microstate and therefore mutual information H(q) with the candidate-output member.

This is explicit entropy export by correlation transfer and displacement. It is not erasure. The enlarged dilation is reversible and preserves total joint information. To reblank a spent cell would require disposal of H(S) information bits under the declared measure; reusing all four sample stores would require disposal of 4H(S) bits. These are information-theoretic erasure lower bounds only. Reset work, Landauer work, physical energy, and a numerical cost are not derived because no temperature, reservoir law, or irreversible reblanking dynamics is supplied.

The conditional mixing horizon is one trial only because product independence is supplied. A fully correlated lawful genesis with the same microstate in all four stores yields a constant four-member word under the same gates. That counterexample makes the boundary sharp: fresh-trial independence is a property of the genesis measure, not of the reversible reset permutation.

## Candidate output, permanence, and Record firewall

Within the four-trial capacity, earlier output slots are never touched by later forward schedules. Each slot contains a filled receipt, one actual-member label under the supplied read ontology, and conditional Cycle-531 occurrence/content. This is a finite append-only permanent medium over the declared horizon.

It is not a Record in the framework sense and not realized history. The full dilation can be inverted, the fifth event is rejected for lack of capacity, no unbounded growth or persistence/readability law is present, and no external observer-facing record criterion is discharged. Calling the four slots candidate output preserves this distinction.

## Exact tests

The runner exhausts all 125 active microstates, five binding labels, four pointer positions, and the no-edge/plus/minus current cases: 7,500 physical composition columns. It verifies the emitted member/receipt type, exact Cycle-531 midpoint, conditional occurrence/content, output write, controlled reset, pointer advance, blank terminal scratch, and enlarged-dilation inverse.

It also tests:

- all 125 four-sample basis origins through the full capacity, with prior-output non-overwrite, exact four-step member words, exact per-step inverse, whole-history inverse, and fifth-step rejection;
- five fully correlated genesis counterexamples producing constant member strings;
- p=q label marginals, product-pair mutual information, read/spent and read/new-active mutual information, and entropy identities on all train/held preparations;
- all 24 proper-cubic frames, with bath, environment, pointer, output, stochastic kernel, genesis measure, member, and receipt treated as scalars and current endpoints exchanged under orientation reversal;
- active bath, environment, member, receipt, binder, output, reset, pointer, and lawful-domain deletions;
- nearest-neighbor routing, inverse, leakage, unique labels, exact finite capacity, and preservation of the imported one-particle mass fixture 0.45340565417488515.

No enlarged reset/output mass eigenstate is claimed. The pointer advance is not physical time. No source, gravity, energy, Record, realized history, or Born law is derived by relabeling.

## Empirical and blinded rejection surface

For every train/held preparation the predeclared candidate is iid categorical p=q. The blinded rejection protocol is:

1. lock q, alpha=0.01, exclusions, a serial-independence test, and the multinomial likelihood-ratio G test before seeing ordered labels;
2. hash the ordered labels and metadata before unblinding;
3. use the asymptotic chi-square df=4 critical value G=13.276704135987622 only when every expected count is at least five;
4. reject p=q when the locked G statistic crosses the threshold, and evaluate serial independence separately.

Deterministic N=5000 near-q and maximally biased controls test acceptance/rejection wiring without host random sampling. They are synthetic controls, not empirical strings. Empirical strings remain separate: the observed corpus and blind commitment are absent. The four-trial physical apparatus is far too small for N=5000; it would require at least 1,250 separately admitted four-trial batches or a larger environment/output compiler. Consequently no empirical or Born calibration result is claimed.

## Full N1–N8 no-go discipline

N1 — route enumeration. Eight normalized routes are retained: this finite open reset dilation; Cycle 538's closed periodic bath; Cycle 536's pure coherent dilation; the separately supplied p=q stochastic kernel; an autonomous stochastic source; irreversible reusable reset; host RNG ruled out by scope; and a permanent history medium attempted only as a four-slot candidate.

N2 — wall independence. Reversible displacement is independent of stochastic genesis; the stochastic kernel is independent of p=q calibration; product independence is independent of one-step marginals; fresh capacity is independent of irreversible reuse; pointwise read is independent of probability; finite output is independent of framework Record permanence; entropy bits are independent of physical work without temperature; and empirical likelihood is independent of four-trial physical capacity.

N3 — hidden-wall scan. Supplied items include operational q, the p=q kernel, microstate weights, tensor-product independence, one-hot initial states, law-owned read ontology, blank output/scratch, fixed partition, exact Cycle-531 ports, three fresh cells, finite capacity, the L5/L6 interface, three-site Toffoli, and static routing. Missing items include autonomous stochastic preparation, a reblanking entropy sink, temperature/work law, empirical corpus, blind commitment, unbounded output, and arbitrary-horizon fresh capacity.

N4 — residual matching. Zero enlarged inverse/leakage residual diagnoses dilation reversibility only. Zero p=q marginal residual diagnoses supplied-measure arithmetic only. Zero fresh mutual information diagnoses the supplied product law only. Read/spent mutual information diagnoses correlation export only. Four-step persistence diagnoses finite output only. Fifth-step rejection diagnoses capacity only. All-24 mismatch diagnoses covariance only. Deletion sqrt(2) diagnoses load-bearing gates only. Synthetic G-test controls diagnose a rejection surface only.

N5 — rhetoric audit. Open dilation is not an autonomous stochastic source; SWAP reset is not erasure; entropy bits are not work or energy; supplied iid genesis is not derived independence; pointwise read is not stochasticity; finite output is not framework Record; four events are not realized history; p=q is not Born; synthetic controls are not empirical data; pointer advance is not physical time; and a route-specific capacity wall is not constitutional evidence.

N6 — partial closure. Retain the exact finite reset dilation, Cycle-531 composition, separately typed kernel/genesis/read, entropy and mutual-information flow, finite product consequences conditional on genesis, four-slot candidate output, fifth-step capacity rejection, covariance, inverse, deletion, routing, and empirical protocol. Leave autonomous stochastic production, reusable erasure, permanence, actual data, and Born open.

N7 — steelman. Construct a local autonomous source model that prepares the Cycle-541 product genesis measure from a declared nonequilibrium resource without a host sampler; name every M2 receiving exported correlations; either implement reusable reblanking with temperature/work assumptions or retain a bounded capacity statement; and scale fresh cells plus readable append-only output to a predeclared blinded corpus. Lock p=q and serial-independence tests before unblinding and compare actual strings against Cycle 541 iid, Cycle 538 periodic, Cycle 536 coherent, and Cycle 534 carrier hypotheses. Preserve all-24 covariance, enlarged inverse accounting, deletion controls, and the candidate-output/Record distinction.

N8 — cross-cycle echo. The result preserves Cycle 243's event-before-Record boundary; Cycles 259/262/266 coherent occurrence candidates; Cycle 500 coherent cylinders; Cycle 505 binding without member; Cycle 508's p=q and actual-member tournament; Cycle 531's exact conditional binder; Cycle 534's deterministic carrier; Cycle 536's reduced-diagonal dilation; and Cycle 538's deterministic recurrent bath.

This is a route-specific conditional construction. It is not a shared obstruction, minimum-content theorem, or source of axiom pressure. No axiom pressure is claimed.

## Supplied / derived / open

Supplied:

- exact Cycle-531 and upstream operational interfaces;
- candidate p=q categorical stochastic kernel;
- 125-microstate genesis weights and four-store product independence;
- law-owned pointwise actual-member read;
- initial active/environment state, pointer, blank output, blank scratch, and lawful-domain constraints;
- cubic field action, static routing chart, and three-site Toffoli.

Derived:

- a fixed 720-M2 reversible open dilation with three finite controlled resets;
- exact Cycle-531 occurrence and four non-overwriting candidate-output writes;
- p=q marginals and one-trial mixing conditional on the supplied product measure;
- explicit entropy and mutual-information flow into spent cells;
- exact finite capacity, correlated-genesis counterexample, inverse, leakage, deletions, all-24 covariance, and likelihood controls.

Open:

- derivation or autonomous physical preparation of the kernel and product genesis measure;
- empirical acceptance/rejection of p=q and any Born law;
- reusable irreversible reset, entropy sink, temperature, reset work, and physical energy;
- fresh independence or mixing beyond four trials;
- permanent framework Record, readable realized history, and unbounded medium growth;
- empirical corpus, blind commitment, serial test result, and physical N=5000 resource realization;
- autonomous constraints, two-site Toffoli compilation, source, gravity, and physical time.

The six-wall ledger does not move constitutionally. C_local gains a bounded finite open-dilation comparator; C_source is sharpened into explicit kernel/genesis/read/resource imports; C_ref, C_num, C_wrap, C_int, C_local, and C_source all remain open for an autonomous stochastic realized-history law.

## Executed result

Final execution: PASS=9, FAIL=0. The timed test body took 91.64628054096829 seconds after imports, maximum RSS was 687,341,568 bytes, and reported process swaps were zero.

The 7,500 exhaustive physical columns included 6,000 member/binding mismatches and had zero member/occurrence/reset/output, exact Cycle-531 midpoint, enlarged inverse, or terminal-scratch failures. The 9,000 proper-cubic columns had zero mismatches. All 125 four-sample basis-origin sequences preserved earlier output slots, rejected the fifth trial, and inverted exactly; the five deliberately correlated genesis fixtures produced (0,0,0,0) through (4,4,4,4) as predeclared.

Across the four train/held kernels, p=q marginal residual was exactly zero because it is built into the supplied genesis measure. Member entropies were 2.090392217285188, 1.931323441749171, 1.689366190049587, and 2.0489443060842025 bits. Corresponding full microstate entropies were 6.734248407059913, 6.575179631523896, 6.333222379824312, and 6.692800495858927 bits. Fresh member-pair and prior-member/new-active mutual informations were zero to floating residual below 1.1e-14 bits, while prior-member/spent-cell mutual information equaled member entropy to floating tolerance.

All four N=5000 near-q synthetic controls remained below the locked G-test threshold; all four maximally biased controls exceeded it. The smallest expected count was 14.408129126639441, so the declared asymptotic expected-count guard passed. No empirical corpus was evaluated.

The routed representative had 1,798 logical gates, 1,534,037 adjacent routing swaps, and 9,206,020 nearest-neighbor primitives. Its schedule digest was `227e26c16e7eec03e88ee368c368c6683c2723bb937432e336b578d24117c3e6`. Thirteen targeted deletion witnesses each changed the basis output by residual sqrt(2), and every malformed active/environment/output domain probe was rejected.
