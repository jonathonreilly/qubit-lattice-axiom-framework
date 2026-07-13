# Review History

## Framework-blind physicist panel (3 seats, gpt-5.6-sol max, read-only; pre-PR per handoff P4)

All three seats: UNSOUND against the pre-repair derivation claims;
algebra assessed valid by all three. Verdicts verbatim below; all
findings adopted into the note (8-edit repair pass, commit history).

### Seat 1

    UNSOUND
    
    1. The fan-out state is correct: two controlled copies of the same orthogonal pointer basis produce
       \[
       c_0|0r_0s_0\rangle+c_1|1r_1s_1\rangle .
       \]
       This does not clone an arbitrary quantum state. Conditioned on a projective outcome \(i\), the registers are in the product state \(|r_i\rangle|s_i\rangle\), so conditional independence is valid only in that branch/classical-outcome sense. Before conditioning, they are correlated parts of a GHZ-like state.
    
    2. The claimed derivation of \(|c_i|^2\) is circular. Duplication identifies an agreement projector such as
       \[
       Q_i=|r_i s_i\rangle\langle r_i s_i|,
       \]
       but does not assign it a numerical weight. Obtaining
       \(\langle\Psi|Q_i|\Psi\rangle=|c_i|^2\) already uses the Hilbert-space expectation/Born pairing. Calling this number the “agreement functional” does not derive that pairing from two witnesses. FRAME-EXT plus Gleason can constrain a previously supplied frame measure to \(\operatorname{Tr}(\rho P)\), but R-FORM still does not determine that the relevant \(\rho\) is \(|\Psi\rangle\langle\Psi|\).
    
    3. Gleason cannot be applied to the realized agreement menu. Two writes realize only the correlated pointer subspace spanned by \(|r_0s_0\rangle\) and \(|r_1s_1\rangle\), not all projections or orthogonal decompositions of \(M_4\). Gleason requires a frame function defined consistently on the entire projection lattice, including entangled bases, disagreement sectors, and unrealized contexts. It is legitimate only if the full FRAME-EXT premise is invoked. In that case, however, the essential extension is still supplied by hand; the two registers provide merely a physical \(4\)-dimensional carrier. The modest claim that the carrier/domain has been identified is defensible, but the claim that the composite-domain requirement or pairing has been physically supplied is not.
    
    4. “One write revocable, two writes lock” is only an access-relative decoherence statement. An isometry’s adjoint reverses it physically only on its image and with suitable coherent control. After two writes, undoing the first interaction while tracing over the inaccessible second register indeed leaves zero pointer-basis coherence because \(\langle s_0|s_1\rangle=0\). But the complete two-write interaction remains globally reversible. Measuring the second register in an eraser basis, followed by feed-forward and undoing the first copy, can restore the original state. Thus redundancy provides robustness against restricted local reversal, not permanence or fundamental locking.
    
    5. The qubit counterexample \(f(P_{\mathbf n})=(1+n_z^3)/2\) is valid, but it establishes only the familiar failure of Gleason in dimension two. Adding a second register raises the dimension; it does not make duplicate witnessing the physical source of quadratic weights. Any suitable dimension-raising ancilla plus the full frame-function assumption would do the same mathematical work.
### Seat 2

    UNSOUND
    
    1. The central weight claim is circular. The isometry derives the fan-out amplitudes \(c_i\), but it does not turn squared Hilbert norms into physical readout weights. Calling
    \[
    \langle\Psi|\Pi_i^{\mathrm{agree}}|\Psi\rangle=|c_i|^2
    \]
    the “agreement weight” already assumes the Born pairing. Gleason only yields \(f(P)=\mathrm{Tr}(\rho P)\); it does not identify \(\rho\) with the density operator constructed from the input vector. FRAME-EXT permits, for example, a maximally mixed or other input-dependent density operator unless an additional preparation-calibration, covariance, or eigenstate-certainty premise is supplied.
    
    2. R-FORM-b carries the pointer-basis payload. Two individually admissible writes need not copy the same system projectors. The claimed fan-out requires both interactions to be nondemolition copies of one common decomposition \(\{P_0,P_1\}\), with a preselected subsystem/register factorization. Saying both contents are tied to “the outcome” assumes precisely this shared outcome observable; neither Record nor the one-write classification selects it.
    
    3. “Conditional independence given the outcome” does no derivational work in its structural reading: conditioned branch states were stipulated to factor across fresh registers. In a probabilistic reading it is worse, because “conditioning” presupposes the joint outcome measure whose weights are under derivation. Thus it is either an explicit broadcast assumption or circular, not an emergent Born-level result.
    
    4. Two registers do not physically supply the Gleason domain. The realized agreement states occupy only the correlated two-dimensional code subspace spanned by \(\{|r_0s_0\rangle,|r_1s_1\rangle\}\). Realizing two qubit carriers does not realize, make readable, or impose frame additivity on every projector and every orthogonal decomposition of \(M_4\). With no local-observability mechanism, FRAME-EXT still supplies that full domain and its counterfactual menus by hand. The second register merely embeds the problem in dimension four; the extension premise remains load-bearing.
    
    5. Distinct sites are forced only after “read” has been redefined as creation of a new record. Record allows repeated readout of the same permanent record and does not state that reading writes another register. Permanence explains why later reads agree; it does not logically exclude them or select independent witnesses as the meaning of “read twice.”
    
    The fan-out algebra and local irreversibility once an inaccessible orthogonal copy remains are sound conditional observations. They establish redundant decoherence, not the claimed derivation of readout weights or the full frame domain.
### Seat 3

    UNSOUND
    
    1. The fan-out state and conditional product form are valid kinematics. The claimed weight is not derived. Writing
       \[
       \langle\Psi|E_i|\Psi\rangle=|c_i|^2
       \]
       already selects the Hilbert-space quadratic/Born functional. Record content and finite additivity do not identify that expression with readout weight. FRAME-EXT plus Gleason yields \(f(P)=\mathrm{Tr}(\rho P)\), but does not establish \(\rho=|\Psi\rangle\langle\Psi|\). That requires an additional preparation-to-frame calibration, covariance, or eigenstate-certainty premise.
    
    2. Agreement in one pointer basis supplies only diagonal numbers and is blind to relative phase. It therefore cannot produce sesquilinear structure without values in superposition contexts. Those values enter through FRAME-EXT’s full projection-lattice premise and Gleason, not through the second witness.
    
    3. “R-READ requires no registration” is an overclaim. The two formation registers are registrations, and their contents supply labels in individual runs—not statistical weights. Operationally identifying coincidence frequency with \(f(E_i)\) requires an ensemble-counting/readout rule or another register. Permanence makes repeated label-reading redundant; it does not make probability extraction registration-free.
    
    4. Two qubits instantiate \(M_4\), but the fixed copy interaction realizes only a pointer context and its coarse-grainings, not every product and entangled orthogonal decomposition of \(M_4\). Consequently, FRAME-EXT still supplies the domain needed by Gleason “by hand.” The gap is narrowed only to having a dimension-\(\ge3\) carrier, not to physically realizing the required menus. Saying Gleason applies “on the realized menu” is false unless “realized menu” already means the entire projection lattice.
    
    5. The \(M_2\) loophole function is a good control: it correctly shows that qubit complement-additivity alone permits non-density assignments. But it also demonstrates that adding a register helps only when full \(M_4\) frame additivity is assumed. One-write reversibility and two-write local decoherence test redundancy, not permanence or Born weighting; the two-write map remains globally reversible on its image. Corrupted-witness controls need quantitative bounds for nonorthogonality and correlated errors.
    
    6. The \(r=1/2\) versus \(r=1\) fork is not yet falsifiable. With no formation-frequency rule and no independent operational definitions of \(w\) and \(r\), the formula merely translates two stipulated counting conventions. “Per coordinate” is also representation-dependent unless coordinates correspond to independently controllable physical alternatives.
    
    7. The strongest additional control would be randomized \(M_4\) tomography on identically prepared two-record systems, including phase-sensitive entangled contexts, with frequencies defined independently of the proposed pairing. A noncontextual bound across those menus would strengthen the claim; inability to perform them without creating or erasing further records would expose that the asserted composite domain was never physically supplied.
## Supervisor repair map

1. R-FORM-b: shared-decomposition requirement made named clause content.
2. R-READ-c verdict demoted: decomposes to FRAME-EXT + Gleason + PREP-FRAME (panel-forced new name); nothing closed.
3. Theorem part 2 relabeled consistency identity + conditional relocation claim.
4. Theorem part 3: carrier-only narrowing (panel wording adopted).
5. Permanence framing access-relative; strict permanence stays axiom-supplied.
6. P3: 'requires no registration' -> 'adds no registrable content of its own' + PREP-FRAME placement.
7. P0: falsifiable-discriminator wording softened to two-point fork, identification contextual.
8. Panel section records verdicts; successor control (randomized two-record tomography) banked.

Runner: worker-drafted from supervisor spec; two supervisor-spec errors
corrected by the worker with supervisor line-review concurrence (overlapping
content rays remain isometric — they exit the discrimination clause, not
trace preservation; outcome-0 agreement provably cannot deviate, deviation
exhibited on the corrupted outcome-1 component). TOTAL: PASS=81 FAIL=0.
