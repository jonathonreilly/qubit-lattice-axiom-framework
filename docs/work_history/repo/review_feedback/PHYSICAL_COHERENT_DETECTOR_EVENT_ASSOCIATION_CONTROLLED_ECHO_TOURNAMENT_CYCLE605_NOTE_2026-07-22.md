# Physical coherent-detector / event-association / controlled-echo tournament — Cycle 605

Date: 2026-07-22
Authority: none
Audit: unset
Constitutional effect: none

## Frozen question and claim ceiling

Cycle 605 continues the accepted Cycle 602 detector and event-side campaign.  It asks whether the fixed orthogonal onsite ray `a` and transported ray `G a` can be compiled into a strict physical-M2 coherent detector; whether its output can replace Cycle 570's supplied event opportunity; and whether the contact/reference echo can be made N4-free with literal local gates.

The answer is a bounded partial closure.  There are three positive constructions:

1. the onsite A2 ray is exactly a rank-two Slater determinant, and its decoded-N2 membership predicate has an exact adjacent-Givens plus reversible-equality circuit;
2. the exact algebraic path identity `H_path; controlled-G; G^-1; A2-membership-X_path; G` prepares `(a+G a)/sqrt(2)` from `a` and erases the path on that declared input;
3. the selector-controlled onsite contact is an exact seven-M2-line phase-polynomial circuit using only one- and two-M2 gates and invokes no N4 matter state.

This does **not** close a strict physical coherent readout.  The accepted physical encoder does not yet expose the code-compatible local `W^dagger` membership word with a per-readout NN SWAP total, controlled-G is not compiled from the accepted physical factor list, and the even X/Y phase readout still requires a physical vacuum/A2 grade-changing pulse.  No arbitrary Householder or opaque two-level unitary is counted as primitive closure.

The fixed sizes are train L3, held L6, and held-out L4.  L3 uses q=1..4; L6 and held-out L4 use q=1..6.  The material law remains Cycle 590's accepted `beta=-0.3`, `g=0.37` free-plus-contact update and inverse.

## Route A — what is and is not a coherent detector

Let `P_a=|a><a|` and `P_b=|G a><G a|`.  The accepted channels are orthogonal, so the runner checks `||[P_a,P_b]||`, both sequential-copy orders, inverse, leakage, and pointer-sector norm closure.  Both sharp values can be copied nondemolitionally into two pointer M2 on the declared N2 code.

That which-channel instrument is not Cycle 602's coherent detector.  If `alpha=<a|psi>` and `beta=<G a|psi>`, separate membership statistics give the normalized sum `(|alpha|^2+|beta|^2)/2`.  The fixed Cycle 602 detector `d=(a+G a)/sqrt(2)` gives

`|<d|psi>|^2 = (|alpha|^2+|beta|^2+2 Re(alpha* beta))/2`.

The runner prints the cross term at every frozen q and requires a nonzero which-channel/coherent-detector residual.  A membership predicate is not a phase or amplitude readout.  In particular, reducing over the orthogonal matter branches deletes the pointer coherence.

### Elementary onsite predicate attempt

The six-mode A2 coefficient matrix has rank two.  A deterministic real orbital pair reconstructs it to tolerance, and an adjacent-row mesh has exactly eight number-preserving two-M2 Givens gates.  On decoded q M2, `Q^dagger` maps A2 to occupation word `110000`.  The equality copy uses five clean work M2 and one retained pointer M2:

- four negative-control X gates before and after;
- five Toffolis to compute the six-bit conjunction, one pointer CNOT, then five inverse Toffolis;
- every Toffoli is decomposed exactly into 9 one-M2 Clifford/T gates and 6 CNOTs;
- the fixed line is `q0,q1,w0,q2,w1,q3,w2,q4,w3,q5,w4,pointer`;
- route-return installs 40 SWAPs; the two Q meshes add 16 adjacent fermionic Givens.

The exact per-predicate installed count is 98 one-M2 gates, 61 logical two-M2 gates, 40 NN route-return SWAPs, 117 installed two-M2 gates after the 16 Givens are included, and serial depth/total 215.  Five work M2 return blank.  The retained pointer is explicit.  Reversing the word, exchanging T/T-dagger and Q/Q-dagger, is the full-space inverse.

This count begins after the physical code is locally decoded.  Cycle 560/590 reports 15,984 Route-B Givens on L6, or 74 per cell, and maximum route length 32, but its published receipt does not expose a literal selected-factor/local-decoder word and exact per-readout SWAP count.  Rotating only the persistent q M2 has not been proved to rotate the auxiliary dressing correctly.  Therefore the decoded predicate is not called a strict physical-M2 readout.

### Coherent preparation and phase-sensitive alternative

The path-erasure identity is constructive and uses orthogonality rather than a q selector.  Starting from blank path and `a`, apply a path Hadamard, controlled-G on path one, unconditional `G^-1`, toggle the path on A2 membership, and apply G.  On the declared input the final path is blank and matter is exactly `d`.  The inverse is the reversed word.  Deleting controlled-G or the membership eraser is visible.

The remaining physical obligation is not hidden: compile controlled-G from the accepted physical factor sequence and route it, then compile the code-compatible membership word.  Memberships for `d+=(a+G a)/sqrt(2)` and `d+i=(a+i G a)/sqrt(2)` expose the real and imaginary relative `a/G a` interference quadratures.  They still do not expose the complex phase of `<d|psi>` against a fixed origin.  A phase-sensitive Hadamard/Naimark readout for that absolute overlap additionally applies `U_d^dagger` followed by a vacuum/A2 X or Y grade-changing pulse, or uses a separately physical reference arm such as a fully compiled contact/free echo.  The grade-changing pulse and physical reference remain supplied, so this note does not claim an operational complex-amplitude detector.

All24 covariance and all576 frame products are tested for the scalar A2 projector/update orbit.  The proper-cubic A2 sign cancels in the projector.  The law retains bounded coarse support, but strict elementary physical support awaits the missing compiler surfaces above.

## Route B — explicit matter interrogation to candidate opportunity

The two orthogonal pointer bits feed a clean certificate through `CNOT(p0,c); CNOT(p1,c)`.  On the lawful N2 pointer code they cannot both be one, so `c=p0 XOR p1` is also their OR.  `TOFFOLI(c,binder,opportunity)` derives the Cycle 570 opportunity from an explicit detector certificate and occupied binder.  It never reads q or an update ordinal.

The runner exhausts pointer/binder truth words, marks `11` outside the declared detector code, tests missed and extra controls, reverses the composed reversible schedule, and checks Cycle 570 rollover for certified prefixes 1, 2, 4, 5, and 8.  Identity and predecessor handling remain the accepted Cycle 570 interfaces.

The pointer/binder-to-opportunity map is derived.  The physical detector/pointer input and occupied binder remain supplied.  More importantly, the opportunity is a coherent candidate branch.  It is not an actual occurrence and not a Record.  Cycle 170's actual/permanent Record obligations, Cycle 451's typed matcher, Cycle 498's endpoint refinement, Cycle 504's wrap conveyor, and Cycle 570's counter remain separate.  An update ordinal is not time, an event count is not time, and phase is not energy.

## Route C — physical controlled-contact path echo without N4

For selector `s` and occupation bits `x,y`, the controlled pair phase uses

`sxy = [s+x+y-(s XOR x)-(s XOR y)-(x XOR y)+(s XOR x XOR y)]/4`.

Seven one-M2 phase gates and ten routed CNOTs therefore implement `exp(i g sxy)` exactly.  Applying the macro to all 15 unordered direction pairs implements `exp(i g s C(n,2))` on the full local N0..N6 truth table; the executed matter fixture remains the accepted complete global N<=3 code.  No N4 fixture is introduced.

The literal local line is `selector,q0,q1,q2,q3,q4,q5`.  Every CNOT is routed to adjacency and immediately routed back.  The runner prints exact one-M2, CNOT, SWAP, serial-depth, per-cell, and held-L6 totals.  Deleting one pair phase is visible on its occupied pair.  Including every unordered pair makes the circuit proper-cubic covariant under all24 frames and all576 frame products.

This closes the contact-controlled part only.  A strict full actual/reference echo also needs a controlled physical free update.  The scalar selector equality checks are preserved by the contact circuit but not dynamically enforced, and selector genesis/direct-sum reference genesis remains supplied.

## Leakage, deletion, domain, and semantic controls

- The detector is declared only on the complete global N2 physical code with blank path, pointer, and work M2.  Its elementary circuit is a full-space unitary, but the rank-one A2 meaning outside that code is not claimed.
- The five predicate work M2 return blank; pointer/path outputs or their environment are retained until the inverse.
- Deleted controlled-G, membership eraser, pointer-certificate CNOT, binder Toffoli, rotor carry, and one contact-pair phase all have explicit residuals or malformed words.
- L3/L6 plus held-out L4 are frozen before evaluation.  all24/all576 tests do not select a frame at runtime.
- The inherited global N<=3 cutoff remains a supplied lawful domain and is not claimed locally enforced.
- No Born rule, occurrence rule, proper time, energy identification, lapse, redshift, or gravity/source response is inferred.

## N1–N8 no-go discipline

N1 — Normalized alternatives: (i) commuting which-channel copies terminating in populations; (ii) path-H/controlled-G/membership erasure terminating in coherent d preparation; (iii) `U_d^dagger` plus vacuum/A2 X/Y pulse terminating in complex-amplitude readout; (iv) detector/binder certificate terminating in a coherent candidate opportunity; (v) phase-polynomial controlled contact terminating in an N4-free contact echo component; (vi) two physical dimers terminating in an independent standard, not attempted because N4 remains outside the code; and (vii) Record-admitted events terminating in proper-time calibration, still open.  Five constructive families are actually tested.  No broad negative is sought.

N2 — Directional wall audit: physical coherent detection does not supply event actuality, selector genesis, proper time, or a locally enforced global-domain cutoff; and none of those reverse implications holds.  Event actuality does not compile controlled-G.  Selector genesis does not supply a grade pulse.  Proper-time calibration does not establish a local code decoder.  These walls remain directionally distinct.

N3 — Hidden supplies: beta, coupling, finite tori, N2/N<=3 code domains, blank path/pointer/work M2, H/T phases, noiseless controls, accepted G/G^-1, the local encoder theorem, occupied binder, root rotor, selector cat field, and reference genesis are inventoried.  The exact physical decoder routing, controlled-G, grade pulse, occurrence rule, Record admission, and calibration are not smuggled in.

N4 — Exact residual matching: the Route A surface prints commutator, order-swap, inverse, leakage, cross-term, coherent-preparation, deletion, all24, and all576 residuals.  The nonzero cross-term mismatch is matched directly to Cycle 602's coherent aggregate, not to projector noncommutation.  Route B prints exhaustive truth failures, inverse, rollover, missed, and extra controls.  Route C prints the N0..N6 truth residual and deletion signal.

N5 — Resolution rhetoric: claims are finite exact statements on L3/L6/held-out L4, a seven-M2 local contact line, and event prefixes through 8.  There is no arbitrary-size physical-readout theorem, infinite-volume claim, actual event, Record, proper time, energy, Born, or gravity claim.

N6 — Partial closure paths: extract and route the accepted local W/W-dagger decoder; compile controlled-G factor by factor or replace it with a direct d preparation; compile the vacuum/A2 X/Y pulse; derive actual occurrence and Record admission; and derive selector genesis or avoid the direct-sum echo.  No new-axiom gate is invoked.

N7 — Hostile steelman: a constructor may control every accepted physical-G factor, use the exact path-erasure identity, and compile the remaining grade pulse.  That live construction route blocks a no-go or minimum-content claim.  Likewise a local selector-production law could close the echo without N4.

N8 — Cross-cycle echo: Cycles 170 and 243 forbid promoting schedule/count to time.  Cycles 451, 498, 504, and 570 retain identity, predecessor, rollover, and Record boundaries.  Cycle 602's target is the coherent aggregate, not the sum of two channel populations.  Cycle 599's grade-changing pulse/read wall is therefore narrowed but not silently closed.

There is no shared substrate obstruction, no minimum-content conclusion, and no axiom pressure.

## Six-wall ledger and maturity

- `C_ref`: exact algebraic coherent-d preparation; physical controlled-G, code-compatible predicate, and grade pulse open.
- `C_num`: L3/L6 and held-out L4 distinguish coherent aggregate from which-channel populations; no arbitrary-size or empirical-unit theorem.
- `C_wrap`: detector/binder gates derive a coherent candidate opportunity and exact rollover; occurrence, Record, calibration, and proper time open.
- `C_int`: selector-controlled contact has an exact N4-free elementary circuit; controlled free update and branch genesis open.
- `C_local`: decoded A2 predicate and controlled contact have literal NN schedules; physical W readout routing and controlled-G remain open.
- `C_source`: no source-conditioned response, lapse, redshift, backreaction, or gravity law.

Repo-strict / TOE-strict maturity after this cycle:

- operational quantum / records: 4.84 / 4.68;
- causal time: 4.04 / 3.86;
- inertia / matter: 4.84 / 4.90;
- gravity / source: 4.10 / 3.85;
- Born / probability: 4.20 / 3.65.

The optimal next campaign is a narrow compiler extraction: surface the actual Cycle 560/563 physical factor word for one radius-one read block, control every factor with a local path field, print its literal NN route and exact gate/SWAP/depth counts, and then attach the vacuum/A2 X/Y pulse.  Only after that succeeds should the candidate opportunity be taken to an occurrence/Record campaign.

## Independent parent verification

The parent first rejected the initial interpretation of two sharp channel
pointers as the Cycle-602 coherent detector: the separate pointer populations
omit the interference cross term.  After that boundary was corrected, the
parent inspected the rank-two Slater factorization, equality circuit,
path-erasure identity, event association, controlled-contact phase polynomial,
and full N1--N8 ledger.  It then re-executed all eight scientific and note
checks without invoking the receipt-writing `main` function; all passed.

The spot reproduction returned coherent preparation residual
`5.916983715440049e-16`, which-channel/coherent weight difference
`0.003209185236062409`, relative-interference signal
`0.01004288847904733`, zero Route-B lawful truth failures, and Route-C truth
residual `7.108895957933346e-16`.  The parent accepts the algebraic coherent-d
preparation/inverse, decoded A2 predicate compiler, pointer/binder association
map, and N4-free controlled-contact circuit.  It does not accept a strict
physical coherent phase readout, a physical controlled-G, a fully routed
code-compatible `W^dagger` readout, a derived reference/grade pulse, an actual
event or Record, proper time, full controlled echo, shared obstruction, or
axiom pressure.  The frozen worker receipt and cold transcript were not
overwritten by this reproduction.
