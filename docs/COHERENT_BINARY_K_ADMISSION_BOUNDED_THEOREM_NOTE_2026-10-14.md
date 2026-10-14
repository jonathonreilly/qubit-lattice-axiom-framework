---
title: Coherent binary K-admission with returned nearest-neighbor workspace
claim_id: coherent_binary_k_admission_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: fixed literal L4 binary projector instrument, arbitrary active input and reference, supplied clean work, addressed gates after drift removal and final flag readout
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete emitted coherent binary instrument with both outcome coherences and returned dirty transit under supplied controls; identity runner evaluates no mathematics
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["joint_even_matter_finite_link_interface_bounded_theorem_note_2026-10-14", "openreference_cubic_recurrent_physical_m2_matter_compiler_cycle870_bounded_theorem_note_2026-08-02", "recurrent_encode_update_decode_sandwich_cycle883_bounded_theorem_note_2026-08-03"]
runner: scripts/coherent_binary_k_admission_identity_2026_10_14.py
next_trace_action: separate root review and guarded integration of this publication package, then regular PR and independent retained audit
---

Claim type: bounded_theorem

# Conditional binary K-admission for the literal L4 joint code

This source assembly presents an accepted conditional compiler for the complete binary Lüders instrument of the specified L4 matter/link code. It accepts arbitrary input on the 1344 active qubits, with arbitrary passive references and dirty transit. The full emitted ordinary-open-box circuit coherently computes the constraints, copies only the binary answer, and uncomputes every finer syndrome and work register before one supplied flag readout. Both unnormalized PASS and FAIL blocks retain their internal coherence. The construction does not prepare or repair the input.

**Current status and explicit historical correction.** Root accepted the binary source at 2026-10-14T10:34:17.843934Z under `75c3a29049f6d914b67b485b6fc672a5d6c1588a7fd4fa5c54fe326562065c4d`, after complete root and separate source review. Neutral preparation had already been accepted at **2026-10-14T09:52:23.409500Z** under `6e1e1bf011dfd5cb765c8ae1430efb2aebe809443b01992edb2aac8703509fbe`, before the binary author seal at **2026-10-14T09:59:20.361761Z**. The frozen proof's assertion that neutral preparation was not accepted at its seal, and its README's pending-review sentence, are stale and false as current status. They are retained unchanged as historical erroneous source text. This wrapper and the current README expressly correct them; neither the mathematical body nor any emitted circuit is edited. Earlier provisional exposure records retain their actual dates. Imported role strings, including the old pending-review and current-read phrases, are historical quotations from author exposure `48396cb732e2a0883d3c86a5e1e489b0c95916d4454dd91f08552dc9114b2f2a` at 09:46:49Z. The accepted addendum `2ab5a79a0f03046bad7053e6f1e739b021740b53fd28a8707aa6bcc2b437c581` binds all 32 copies and requires present acceptance to be recorded separately. No neutral state-preparation theorem is imported: exact graph, signed-model and route helpers are reused, and the operator/routing identities are proved in the binary source itself.

The source assembly and its separate metadata-scope addendum were conditionally accepted under `f6b9c4a0a60c1938fd31b399aed49f759b05b2be6797cef175c0425ba0bfd613`, after complete root review `f6798ab14a5457f5130386fe288aa920de55d20a8daebf4ecf2467cbbec17a85`. This publication rendering and driver require separate root review. Conditional source acceptance is not retained/audit status, a publication-driver acceptance, or authorization for canonical execution. Suggested claim scope is `bounded_theorem`, with conditional-support status. The theorem concerns this fixed literal L4 architecture, not all volumes or native measurement dynamics.

## The exact instrument and supplied inputs

Let A be the 1344-qubit active carrier. In the accepted literal joint model, let S_i be the 704 ordered local-cycle Paulis and three specified +1 Wilson Paulis, let p_e,q_e be the two physical link bits, and let G_x be the 64 integer Gauss operators. The full carrier projector is

    P_K = product_(i=1)^707 (I+S_i)/2
          product_(e=1)^192 (I-|11><11|)_e
          product_(x=1)^64 1_{0}(G_x).

All factors commute on the full active Hilbert space. The predicate imposes no fixed B-occupation ray or fixed allowed flux value. The complete proof below gives every literal sign, link convention, coordinate and seam. For any density operator rho on active A, dirty transit T and an arbitrary external reference R, the implemented ideal output is

    |PASS><PASS| tensor (P_K tensor I_TR) rho (P_K tensor I_TR)
    + |FAIL><FAIL| tensor ((I-P_K) tensor I_TR) rho ((I-P_K) tensor I_TR).

These are unnormalized blocks, with no division by a success probability. All nonflag work returns to its clean product state even jointly with flag and reference. Conditional passive marginals can be steered by the outcome; the claim is an identity tensor factor on passive systems, not unchanged postselected marginals. The unconditional passive marginal is unchanged.

There are 2309 additional supplied clean qubits, including one flag; all other 258491 factors of the physical box `{0,...,63}^3` may be arbitrary and correlated with A and R. The controller supplies individually addressed one/two-qubit gates, their chronological order, an external clock and stopping, and drift removal. Alternatively exact compensation must produce the same net scheduled generators, but no compensator or its cost is constructed. The final computational-basis flag instrument at `(0,37,40)`, PASS for 1 and FAIL for 0, is also supplied. No finer register may leak into a bath, measurement, reset or uncontrolled archive during coherent execution. Precision of the initial clean product is an extensive supplied preparation obligation.

## Why the complete word implements the projector

The commuting refinement consists of signed loop/Wilson values, unsigned B occupations and physical link bits. Dependencies may make some joint spectral projectors zero; the proof does not assume all formal assignments occur. Signed controlled-Pauli extraction retains negative Pauli signs and Y phases. All 707 emitted rows and their generator-image checks are preserved. The 384 B parities are data used in Gauss arithmetic, not fixed admission signs; the 192 coherent link ANDs reject precisely unused |11>.

For each cell, the exact identity on the full four-state link carrier is `G_x=9-w_x`, where w_x is the Hamming weight of the six occupation bits plus, per axis, `1-out_p, out_q, in_p, 1-in_q`. There are eighteen bits and six complements. A five-bit reversible counter distinguishes weight 9 without aliasing. The actual Toffoli primitive is a concrete phase-exact 15-gate one/two-qubit word, not a relative-phase or supplied three-body gate. All 76931 macro Toffolis are expanded in the logical artifact.

The forward computation F has 1347 blocks. A 963-control flag ladder with 961 reusable clean scratch bits copies only the common predicate. Exact F inverse removes every fine label and temporary bit. Thus, on clean input work and flag, the complete unitary is the isometry `P_K|psi>|0_work>|1_flag> + (I-P_K)|psi>|0_work>|0_flag>`. The proof fixes relative phases as well as returned bits. Tensoring with arbitrary references and applying the single supplied flag instrument gives both complete unnormalized blocks above.

For each logical two-qubit gate, ordinary monotone x/y/z routing swaps the first endpoint to a neighbor of the second, applies the gate, and reverses all swaps. This is an exact tensor-permutation conjugation and returns arbitrary dirty transit, including its correlations. Every physical edge has ordinary L1 distance one; periodic seams are not shortcuts. The original even active coordinates alone have no ordinary NN edges. The full emitted physical word has 29489403 records, not merely an expansion recipe. Its exact token and central-operation certificate, combined with the tensor identity, justifies quantum transit return without a dense full-box simulation.

## Resources and complete error contract

| Resource | Literal emitted or supplied value |
| --- | ---: |
| Arbitrary active input qubits | 1344 |
| Additional clean qubits, including flag | 2309 |
| Logical sites, total | 3653 |
| Available dirty-transit factors | 258491 |
| Dirty-transit sites actually touched | 74450 |
| Total sites touched | 78103 |
| Logical one/two-qubit gates | 1207419 |
| Physical ordinary-NN primitives | 29489403 |
| Included physical SWAPs | 28281984 |
| Routed CNOTs | 484012 |
| Sum / maximum route distance | 14625004 / 162 |
| Maximum gate incidence at one site | 925422 |
| Total gate-site incidences | 58255399 |
| Actual serial depth | 29489403 slots |
| Supplied final flag readout | One event |

For supplied arbitrary addressed Hermitian gate generators, a logarithm of norm at most pi realizes each primitive in a slot `pi/Jc`, with `Jc>0`. Serial operation gives instantaneous scheduled per-site norm at most Jc, circuit duration `29489403*pi/Jc`, and integrated scheduled norm at a site at most `925422*pi`. **Jc prices scheduled gate generators after drift removal; it does not bound or price a separate arbitrary drift-cancellation apparatus.** Clean-input preparation and final readout times remain separate supplied terms. Hermiticity and these control norms imply no positive physical energy, autonomous fuel budget or native clock.

For joint initial trace-norm error epsilon_init, full unitary operator-norm error delta_j of physical slot j, and complete final flag-instrument diamond error epsilon_read, all without an extra factor 1/2,

    ||output_actual-output_ideal||_1
       <= epsilon_init + 2 sum_j delta_j + epsilon_read.

The comparison includes transit and arbitrary references. A uniform delta gives `58978806*delta`. An integrable self-adjoint residual drift can instead add `2 integral ||D(t)|| dt` with its actual global norm. No local or volume-uniform replacement is assumed. This is not a normalized rare-outcome bound or a guarantee for arbitrary dissipative, memory-dependent or population-only gate error specifications.

## Evidence, scope and attribution

The full 34075-byte proof is preserved at `8abf93c718c691f2140ae9df990bdf0b49f5ddd4a013277f36b04d3dac1887d3`, with all 64 author files under freeze `4b8ba76040b0d43668d1d9c9706d404a32e54ea8cde4978326571809fc68df97`. This includes complete compressed macro/logical/physical words, all three complete deletion mutants, exact certificates, all five attempt sources/streams/receipts, original reconnaissance/exposure and the failed run02. Run02 genuinely failed on an incorrect expectation about the wrong-phase mutant after the ideal Toffoli check; it did not complete the remaining suite. Its exact narrow verifier repair and successful run03 are preserved. The compiler and emitted word were unchanged.

The complete separate review `75298722578dbd860f75097631e44dca6c91929880540154d755b71564deefe7` and seal `9efe378ad083ac07c4238acb01f27e1dca08d2e13083ee4578fcc478ddeecb62` preserve all 16 review files. One six-qubit channel/phase control preceded author-source exposure; it is a generic interface discriminator, not a literal L4 simulation. The subsequent check is source-exposed and uses a distinct integer-phase argument, full macro semantics/inverse relations, all logical geometry/counts, selected logical/physical spans, and whole-stream deletion identities. It does not repeat the author's full Gauss truth vector, all expansion comparisons or 29-million-record token evolution. The remaining complete-word coverage rests on the fully reviewed author source and actual recorded execution. No blind, model-diverse or second full independent execution is claimed.

The selected fine-archive mutants separately violate within-PASS and within-FAIL coherence with full trace-norm error 1 despite correct labels. The missing last return SWAP has a passive-reference Bell discriminator with error at least 3/2. Non-ray, seam-with-flux, unused-link and Wilson controls distinguish full K from narrower predicates. These are scoped controls, not universal negative claims. All actual root review and binding records remain unchanged, including their earlier pending statuses.

The sole mathematical parent is the [joint interface](JOINT_EVEN_MATTER_FINITE_LINK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-10-14.md) canonical `c903cfd91b76fe69cf492272af00bfe014cb04f5d85f721214638aa5f977fe48`, representing core `34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca`. These are two identities for one parent. Neutral helper source reuse is explicitly mapped; its state-preparation conclusion is not imported. Cycles 240/244/279/870/883 and the earlier reconnaissance retain their stated context/attribution coverage. Generic reversible predicates, coarse pointer dilation, copy/uncompute and returned routing are existing machinery. The canonical [Cycle 870 returned routing](OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md) and [Cycle 883 inverse and return](RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md) citations provide mechanism attribution only at their original limited exposure; their other theorem conclusions and fixture counts are not imported. No exhaustive novelty claim follows from the bounded overlap screen. Intervening publication ancestry, local-uniformity, penalty/controller, finite-history and kinetic results supply no additional theorem premise.

What is established conditionally is a literal finite implementation of the full supplied projector interface, with both outcome coherences and a returned-transit word. Clean resources, controls, drift removal, clock/precision and the physical flag instrument remain supplied. No all-L admission, arbitrary-state encoding, state repair, cooling, autonomous/native measurement, physical-energy, photon/continuum or retained-grade conclusion follows. This source assembly performs only identity/extraction/closure checks, with zero mathematical predicates and no archived scientific rerun.


Review-loop integration: current parent wrapper identities are rebound in PARENT_BINDINGS.json. Historical full-note hashes inside unchanged proof bodies identify original source versions; the relied mathematical bodies remain byte-identical. Historical review records are provenance, not audit authority.
## Complete unchanged historical proof

The following accepted body is byte-identical to DERIVATION.md 8abf93c7. Its original pending-review and neutral-preparation status assertions are historical text; the explicit current-status correction above governs this presentation. No mathematical or circuit correction is applied.

# A literal coherent binary K-admission compiler on the open physical box

**Status: a conditional finite construction with an emitted complete word and exact same-author checks; separate mathematical review is still required.** The output is the binary Lüders instrument for the original L=4 joint code K, on arbitrary active input and arbitrary passive reference. The construction returns every fine syndrome and arithmetic work bit to zero before the one supplied flag readout. It does not prepare an arbitrary accepted state, select a fixed occupation ray, or provide an autonomous/native measurement law.

There are 1344 arbitrary active input qubits, **2309 additionally supplied clean qubits including the flag**, and an ordinary open physical box `{0,…,63}^3`. The remaining 258491 factors can have arbitrary states and arbitrary correlations with the active input and reference. The actual emitted circuit has **1,207,419 one/two-qubit logical gates** and **29,489,403 nearest-neighbor physical gates**, including every forward and return SWAP. This is a large, serial, externally controlled implementation, not a practical-efficiency claim.

## 1. Sources, overlap screen and actual assumptions

The mathematical model is the accepted joint derivation `joint_matter_photon_interface/DERIVATION.md`, SHA-256 `34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca`; its canonical source-bound note is `JOINT_EVEN_MATTER_FINITE_LINK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-10-14.md`, SHA `212a94bb9cbd2a5d53a227d7d8103b7eca5cc018ec8bb5ca2c86c0ca660c8aef`. Previous complete coverage is reused at unchanged identities. This task refreshed source lines 1–185, including the literal signed loops, B, link states and Gauss equations. `SOURCE_EXPOSURE.json` records every exact source and the distinction between reused coverage, refreshed passages and identity-only checks.

The earlier preparation reconnaissance `a7041d8ada95360a0c8720d1fcc3948b381787edcb2eeab1d72b024d0eebee33` explicitly identified a coherent binary compiler as a remaining route. The new bounded `rg` search and its complete raw results are in `reconnaissance/`. Those searches, the earlier scoped encoder/decoder survey, and the relevant existing sources did not reveal a completed compiler for this literal K predicate. This is a bounded overlap finding, not an exhaustive repository/open-PR or literature search.

Cycle 279 already supplies a generic coarse pointer dilation, copy/uncompute and the fine-archive counterexample. Cycle 240 supplies related measured/feedforward preparation; Cycle 244 a syndrome decoder; Cycles 870/883 supply returned routing and encode/decode/uncompute machinery. None of these general mechanisms is claimed novel here. The additional result proposed here is the literal signed predicate, its exact arithmetic and workspace, the actual emitted one/two-qubit and ordinary-NN words, and their complete-channel binding.

The provisional neutral-preparation source `0e002497bfa624ceb116059e092b3d853c36a969f37e96794675de3e3f587124` has been read by the root but is **not independently accepted** at this construction's seal. This task reuses only exact graph/coordinate/route helpers and the separate signed-letter graph reconstruction from that source package. The extraction maps give original line ranges and function hashes. No state-preparation synthesis function is imported or executed, and this theorem does not require the proposed preparation circuit to be correct. The route identity is proved again below; the literal model is independently pinned to the accepted joint source. The reused model helper also constructs occupation-ray rows after its first 707 rows; those later rows are unused here. Actual B extraction is unsigned and its occupations are input data, as checked by the non-ray controls below.

The supplied engineering assumptions are:

1. The 1344 original active factors have the exact coordinates and operator dictionary below. All factors in the open box are distinguishable qubits with the stated tensor product.
2. The specified 2309 additional factors begin in the product `|0>`. All other factors, including those used as transit, can be unknown and reference-entangled. No initial active code membership is assumed.
3. An external controller addresses each emitted one-qubit gate and each emitted two-qubit gate on an ordinary distance-one edge, with an external clock and the stated chronological order. H, S, S†, T, T†, X, Z, CNOT and SWAP are supplied one/two-qubit control unitaries. No three-qubit control is supplied.
4. Uncontrolled drift is switched off during the quoted circuit. Alternatively the net generator must equal the specified control generator through supplied exact compensation; the construction supplies no compensator or its cost. All quoted gate/time resources use the drift-off version of the contract. An always-on joint Hamiltonian or constraint penalty is not silently left active.
5. After completion, a supplied computational-basis instrument measures only the flag at `(0,37,40)`, returning the classical label PASS for 1 and FAIL for 0, and acting as identity on the other factors. No finer register is measured, discarded, reset by a bath, or exposed to an uncontrolled archive during the coherent word.

These are conditional premises, not new physical axioms or a native realization. Preparation of the clean workspace and the final flag readout are separately supplied interfaces. No prior finite-history, kinetic-limit, controller or penalty theorem is imported merely because it exists on the working branch.

## 2. The exact projector on the full active Hilbert space

Coarse cells are `x∈(Z/4Z)^3`; direction modes are `a=0,…,5` in order `(+x,−x,+y,−y,+z,−z)`. Number the 384 vertices lexicographically by cell then mode. For each cell, number its twelve unordered nonopposite pairs lexicographically, then its three positive-axis stream edges. This gives 960 matter-edge qubits. Each vertex star contains five edges. At matter edge e=(u,v),

    B_v = product_(e incident v) Z_e,
    A_uv = epsilon_uv X_e
           product_(f<e, f incident u) Z_f
           product_(f<e, f incident v) Z_f,
    epsilon_uv = +1 for u<v and -1 for u>v,
    n_v = (I-B_v)/2.

For the literal ordered path `c=(v0,…,v(r−1))`, use

    S(c) = i^r A_(v0 v1) … A_(v(r−1) v0).

There are 512 triangles, 192 octagons and the three specified length-12 Wilson paths. Their literal vertex orders are the ones printed in the accepted source: triangles in axis order with every sign choice; octagons around each omitted axis with the displayed eight-vertex sequence; Wilson axis a with next cyclic axis b and triples `(k e_a,+a),((k+1)e_a,−a),((k+1)e_a,+b)` for k=0,…,3, then closure. The new emitted `cycle_rows.jsonl` stores **all 707 signed physical Paulis**, including the three specified +1 Wilson choices. Its rows are reconstructed a second way by local I/X/Y/Z multiplication, including phases; unsigned rank alone is not used to set signs.

The original coordinates, reduced modulo 64 only when defining the fixed active sites, are

    internal face(a,b) at 16x + 2(D_a+D_b),
    positive stream face a at 16x + 8 e_a,
    link p_(x,a) at 16x + 6 e_a,
    link q_(x,a) at 16x + 10 e_a.

They are 1344 distinct sites. Every component is even, so the induced graph on the original active sites has **no ordinary distance-one edges**. The following routing uses intervening physical factors and never treats a periodic seam as an open-box shortcut.

The link basis is `|-1>=|01>`, `|0>=|00>`, `|+1>=|10>`, with unused `|11>`. On the full two-qubit carrier,

    P_e = I - |11><11|,
    E_e = n_(p_e) - n_(q_e),
    Q_x = sum_(a=0)^5 n_(x,a) - 3,
    G_x = sum_(e outgoing x) E_e - sum_(e incoming x) E_e - Q_x.

Let S_1,…,S_707 include local cycles and Wilson operators, all prescribed with eigenvalue +1. The requested projector is exactly

    P_K = [product_i (I+S_i)/2]
          [product_e (I-n_(p_e)n_(q_e))]
          [product_x 1_{ {0} }(G_x)].                         (1)

All factors commute on the full 1344-qubit Hilbert space. The accepted algebra proves this, and the present signed reconstruction also checks the 707 loops against each loop and B row. Redundant checks are retained. Formula (1) requires neither a basis choice inside K nor a fixed occupation sign. The relation `product_v B_v=I` and other constraints can make some simultaneous eigenvalue assignments absent; the compiler's Boolean formula is valid also on those absent assignments and never assumes that they occur.

For clarity, the 384 B operators and the 384 physical link Z operators form, with the 707 loops, a commuting refinement. Let its spectral projectors be Π_(s,b,l), where

    S_i eigenvalue = (-1)^s_i,
    B_v eigenvalue = (-1)^b_v,
    n_(p_e), n_(q_e) have the bits l_(p_e), l_(q_e).

They are mutually orthogonal and sum to I, with zero projectors allowed. On each nonzero projector, (1) is precisely one Boolean predicate: all s_i=0, every link bit-pair differs from 11, and every actual integer Gauss value vanishes.

## 3. Exact signed extraction and the Gauss arithmetic

### 3.1 Nondestructive fine extraction

For a signed Hermitian Pauli P, a clean target t is coupled by

    H_t ; controlled-P ; H_t.

Its exact operator is `C_P = (I+P)/2 tensor I_t + (I-P)/2 tensor X_t`. This writes `(1-P)/2` without measuring it. Write P=(-1)^r times its local I/X/Y/Z letters. The actual controlled-P is compiled by one Z_t if r=1, and for each nonidentity letter:

- X_q: CNOT(t,q).
- Z_q: H_q, CNOT(t,q), H_q.
- Y_q: S†_q, CNOT(t,q), S_q.

The local controlled factors commute, and the last line follows from `S X S†=Y`. Thus the sign is part of the controlled operation, not an ignored global phase. The raw storage convention `i^p X^x Z^z` is converted using `r=(p-popcount(x&z))/2 mod 2`.

For each actual loop/Wilson block, the checker conjugates every local X and Z generator with the emitted block. It verifies

    X_t -> X_t,        Z_t -> P Z_t,
    Q_q -> Q_q X_t^[Q_q anticommutes with P].                 (2)

There are 15392 exact signed generator-image comparisons across all 707 actual blocks. The generator identity fixes the block up to a scalar phase; the displayed controlled-letter derivation fixes its stated action. Even a scalar phase of an entire extraction block would cancel in its actual inverse, but the prescribed signed syndrome is verified by the Z_t image.

For B_v, the five CNOTs from its incident matter qubits into a clean occupation register give exactly `C_(B_v)`. The target is b_v=(1-B_v)/2. No preselected η signs are applied. Each link bad bit is computed by CCX(p_e,q_e;bad_e), and equals `l_p l_q`, so precisely |11> is excluded.

### 3.2 The 18-bit identity on the full link carrier

At a cell x, the exact operator formula is

    G_x = 3 - sum_(six modes) b_v
          + sum_(three outgoing links) (l_p-l_q)
          - sum_(three incoming links) (l_p-l_q).             (3)

For each axis, introduce the four **ordinary Boolean values**

    1-l_(out,p),  l_(out,q),  l_(in,p),  1-l_(in,q).

Together with the six b_v these are 18 bits, with exactly six complements. Their Hamming weight w_x satisfies

    G_x = 9 - w_x.                                          (4)

Indeed their sum is `sum b + 6 - sum_out l_p + sum_out l_q + sum_in l_p - sum_in l_q`; subtracting it from 9 gives (3). No link-code assumption was used. In particular |11> contributes zero E and does not by itself violate Gauss; it is rejected separately by the link bad bit.

The checker constructs (3) directly, independently of a weight formula, for all 262144 raw 18-bit assignments. It checks (4) and the actual emitted arithmetic block on the full truth vector. Exactly 48620 assignments have G=0, the middle binomial coefficient. The complete direct-G histogram, predicate-bit hash and the first sign-mutant witness are retained. A removed outgoing-p complement changes the neutral assignment `111000` with all twelve link bits zero from true G=0 to wrong G=1; thus the background and orientation signs matter.

### 3.3 A reversible exact zero test

Five clean little-endian counter bits represent weight modulo 32. For a control b, increment by b using, in chronological high-to-low order,

    MCX(b,a0,a1,a2,a3; a4),
    MCX(b,a0,a1,a2; a3),
    MCX(b,a0,a1; a2),
    CCX(b,a0; a1),
    CNOT(b; a0).                                           (5)

Every update of a higher bit uses the original lower bits, so it is the usual binary carry. All gates are reversible, and the high-to-low sequence implements addition by b modulo 32 for every counter value. On a clean counter, the eighteen controlled increments produce the exact integer weight in 0,…,18, with no overflow ambiguity.

For a complemented input bit, apply X to that input before its controlled increment and X again afterwards. Even physical link bits are restored after this pair; the transformation can temporarily leave a constraint sector, which is permitted by the drift-off control contract. It never relies on preserving K at intermediate gate times.

To toggle a clean Gauss-good target iff weight=9, invert counter bits a1,a2,a4, apply MCX(a0,…,a4;good_x), and restore those three bits. Then apply the exact inverse of all eighteen increments. Counter and temporary ladder bits return to zero; all input bits return; the good target is toggled by `1_{G_x=0}`. The truth-vector check acts on the actual first-cell macro block. Every one of the 64 actual cell blocks is checked to be its exact renaming to the literal incident links and six occupations, including incoming periodic seam links. The good target is never used as a control, so the same word XORs the predicate into an arbitrary initial target bit as well.

For m>=3 controls c_0,…,c_(m−1), MCX uses m−2 clean ladder bits s_0,…,s_(m−3): compute prefix ANDs with m−2 Toffolis, toggle the target with CCX(s_(m−3),c_(m−1);target), then reverse the prefix computation. Induction gives each s_j as the AND of c_0,…,c_(j+1). The exact reverse clears it. This proves the all-input controlled-X action with no relative phases once the concrete Toffoli is checked. For m=2 it is one Toffoli; for m=1 one CNOT. The 963-control flag ladder is checked against this complete explicit sequence, not accepted solely from a gate count.

One five-bit controlled increment costs 16 Toffolis and one CNOT. One compute/compare/uncompute Gauss block costs 583 Toffolis, 36 CNOTs and 30 X gates: the complemented-input X pairs and the comparator zero-controls are included. The five counter and three increment scratch bits are reused in the later 963-control ladder after they have returned to zero.

### 3.4 Every Toffoli is a phase-exact two-qubit word

For controls a,b and target t, the emitted chronological template is

    H_t,
    CX_(b,t), T†_t, CX_(a,t), T_t,
    CX_(b,t), T†_t, CX_(a,t), T_b, T_t, H_t,
    CX_(a,b), T_a, T†_b, CX_(a,b).                           (6)

It contains six CNOTs, two H gates and seven T/T† gates. Here `T=diag(1,exp(iπ/4))`. The checker computes all eight columns of (6) exactly in `Q(ω)`, ω^4=-1, using four rational coefficients per amplitude and `1/sqrt(2)=(ω−ω^3)/2`. The result is exactly `|a,b,t> -> |a,b,t xor ab>`, with no relative or overall phase. The complete exact matrix is archived. Replacing the first T† with T gives 16 changed matrix entries, eight outside the ideal permutation; it is a consequential phase/control error, not a harmless global phase.

All 76931 macro Toffolis are replaced by (6) in the actual logical word; the verifier compares every expansion to the emitted one/two-qubit records. No Toffoli or larger controlled-X is charged as a physical three-body gate.

## 4. Coherent binary copying and complete erasure of finer information

The clean workspace allocation is exact:

| Register | Number of qubits | Logical indices |
| --- | ---: | --- |
| Local-cycle/Wilson bad bits | 707 | 1344–2050 |
| Occupation B parities | 384 | 2051–2434 |
| Link bad bits | 192 | 2435–2626 |
| Gauss-good bits | 64 | 2627–2690 |
| Reusable clean scratch | 961 | 2691–3651 |
| Final flag | 1 | 3652 |
| **Total additional clean qubits** | **2309** | |

Logical indices 0–1343 are the original active input. The additional sites are the first 2309 lexicographic sites of the ordinary box that are not original active coordinates. `model.json` gives every coordinate; the allocation is separately reconstructed. The flag is at `(0,37,40)`. The scratch pool's first five bits are the counter, and its next three supply increment/comparator scratch; all 961 are clean before the flag MCX.

Let F be, in order, the 707 coherent loop extractions, the 384 B-parity extractions, the 192 link-bad computations, and the 64 complete Gauss-good computations. There are 1347 forward blocks. On a joint eigenspace Π_(s,b,l),

    F |ψ> |0_work> = |ψ> |s,b,c(l),g(b,l)> |0_scratch>.

This equation is exact; it is not a measurement of the fine label. It follows from the nondestructive extraction identities and the phase-free reversible arithmetic. The full block operations are diagonal in the commuting refinement even though individual physical gates need not commute with it.

Now invert the 707 cycle/Wilson bad controls and 192 link bad controls, leaving 64 Gauss-good controls unchanged. The resulting **963 controls** are all 1 exactly when (1) holds. Their 1923-Toffoli MCX toggles the initially zero flag. Its 961 ladder bits are returned to zero. Undo the 899 control inversions. Finally apply **F†**, by the exact reverse of all 1347 forward macro blocks. H/X/Z/CNOT/CCX are self-adjoint and S exchanges with S†. Each self-adjoint CCX is again expanded by (6), so the resulting one/two-qubit uncompute is the exact operator inverse; its phase-gate list need not be the literal reverse of the first expansion. The archived block index and macro word verify every inverse block, including full signed loop uncompute.

On the clean input subspace, the complete unitary V therefore obeys

    V |ψ>_A |0_work> |0_flag>
      = P_K |ψ>_A |0_work> |1_flag>
        + (I-P_K)|ψ>_A |0_work> |0_flag>.                  (7)

To see why coarse coherence is retained, expand |ψ> over Π_(s,b,l). The flag predicate is constant on every accepted/refused fiber, but F† removes the entire fine label separately in each term. Thus different fine sectors in the same binary fiber retain their relative amplitude and phase. The operation on the active system is the sum P_K, not the list of individual fine projectors.

Tensoring (7) with the identity on any reference proves the result for arbitrary active/reference density operators by linearity, with no dimension bound on the reference. After the **single supplied flag instrument**, discarding only the returned zero work gives

    I(ρ_AR) = |PASS><PASS| tensor (P_K tensor I_R) ρ_AR (P_K tensor I_R)
            + |FAIL><FAIL| tensor ((I-P_K) tensor I_R) ρ_AR ((I-P_K) tensor I_R).  (8)

The two blocks are unnormalized. Neither the active input nor the FAIL branch has been dephased into finer eigenspaces. The clean work is a product `|0><0|` even with the flag and reference. There is no need to normalize, prepare or synthesize a state in K to define this instrument. A FAIL result preserves the entire failed subspace coherently and does not repair it.

## 5. Complete ordinary-NN word and arbitrary transit return

For a logical two-qubit gate on distinct coordinates a,b, choose the ordinary monotone path that changes x, then y, then z, with no modular wrap. Let the path be v_0=a,…,v_d=b, d the ordinary L1 distance. Apply

    SWAP(v0,v1), …, SWAP(v(d−2),v(d−1)),
    gate(v(d−1),vd),
    SWAP(v(d−2),v(d−1)), …, SWAP(v0,v1).                  (9)

There are 2d−1 two-qubit primitives. For d=1 there are no SWAPs. The path is simple and lies wholly in the open box. Routing can pass through other active qubits, clean registers, already computed syndrome bits, the flag, or dirty transit qubits; every such factor is restored by the same conjugation argument.

If R denotes the forward tensor-factor permutation, (9) is `R† gate_(v(d−1),vd) R = gate_(a,b) tensor I_other`. This is an identity of operators on the **complete tensor product**, not a statement just about basis labels or initially blank transit. Hence it holds for arbitrary transit states and arbitrary entanglement with the active input, workspace or reference. Composing the individually returned routes gives

    U_physical = V_(active,clean-work,flag) tensor I_transit. (10)

The full emitted physical file contains 29,489,403 fixed-size records, 265,404,627 decompressed bytes; its gzip file is about 6.84 MB. It is a complete gate word, not an expansion count or symbolic encoder placeholder. The verifier reads every physical record, checks bounds and ordinary distance-one edges, reconstructs every monotone path, verifies the actual central operation/operands, applies every SWAP to an exact 262144-token permutation, and checks identity on all touched positions after each routed gate and globally. It also matches every logical record to its complete macro expansion and every block to its source predicate. The tensor-permutation proof above explains why this finite token certificate suffices for **arbitrary quantum transit**; no dense full-box simulation is represented as having occurred.

In (8), one may therefore include all dirty transit T in the passive reference: the implemented channel is `I_A tensor id_(TR)`. If A was initially entangled with T or R, conditioning on PASS/FAIL can of course steer their conditional states. “Transit returned” means the exact identity factor in (10), not a false claim that conditioning leaves every passive marginal unchanged. The unconditional passive marginal is unchanged because the local binary instrument is trace preserving.

## 6. Actual resources, control time and error scope

The emitted and separately parsed count table is:

| Primitive | Logical word | Physical NN word |
| --- | ---: | ---: |
| H | 172214 | 172214 |
| S | 2920 | 2920 |
| S† | 2920 | 2920 |
| T | 307724 | 307724 |
| T† | 230793 | 230793 |
| X | 5638 | 5638 |
| Z | 1198 | 1198 |
| CNOT | 484012 | 484012 |
| SWAP | 0 | 28281984 |
| **Total** | **1207419** | **29489403** |

The macro source has 130385 operations, including 76931 Toffolis. These are an intermediate representation only. The logical count already expands them into (6). The Gauss compute/uncompute contribution accounts for 74624 Toffolis; link checks compute/uncompute contribute 384; the flag ladder contributes 1923. The sum is 76931.

There are 484012 routed CNOTs, sum of route distances 14625004 and maximum ordinary distance 162. Consequently the actual SWAP total is `2(14625004−484012)=28281984`. All emitted physical two-qubit gates have arity two and ordinary L1 diameter one. The count includes seam routing through the open box. There are 74450 distinct dirty transit sites actually touched, 78103 total touched sites, 3653 logical active/work/flag sites, and 258491 available dirty-transit factors. The exact site-usage file gives every incidence; the maximum is 925422 gates at one site, and total gate-site incidences are 58255399. The two-qubit/one-qubit incidence identity is also `2*28765996+723407=58255399`.

The declared execution schedule is serial: one gate per slot. Its actual scheduled depth is therefore **29489403 slots**, not a claimed minimum depth or parallelized bound. Routing is sequentially returned after each logical gate. Final flag readout takes one additional supplied readout event, whose duration and physical implementation are not supplied by this unitary compiler.

A concrete conditional norm/time contract is available. If arbitrary one/two-qubit Hermitian controls with norm at most J_c can be addressed on the specified support, choose a Hermitian logarithm L_g with `exp(-iL_g)=g` and `||L_g||<=π`. During a slot of duration `τ=π/J_c`, apply `H_g=L_g/τ`. Thus every slot has control norm at most J_c, and each site's instantaneous interaction-norm sum is at most J_c because only one gate is scheduled at a time. The circuit duration is

    T_circuit = 29489403 π/J_c,
    T_total = T_clean_preparation + T_circuit + T_flag_readout.            (11)

The initial preparation and readout durations are supplied, not set to zero. The maximum integrated control-norm budget at a site is at most `925422π` in this serial logarithm implementation; this is a control action bound, not a physical ground-energy, variance or autonomous fuel statement. No assertion of positive native energy follows from unitary gates or Hermitian logarithms.

For errors, let the actual initial joint state be within trace norm ε_init of the intended arbitrary input/reference/transit state tensor the clean work/flag product. Let the physical gate in slot j differ in operator norm from its specified **full** one/two-qubit unitary by at most δ_j. Let ε_read bound the complete final flag instrument error in diamond norm on its input, including passive references, under the convention with no extra factor 1/2. A telescoping product gives `||U_actual−U_ideal||<=sum_j δ_j`; the usual two-sided density-operator expansion then gives

    ||I_actual(ρ)-I_ideal(ρ)||_1
       <= ε_init + 2 sum_(j=1)^29489403 δ_j + ε_read.                    (12)

This includes transit factors in the output comparison and is uniform over arbitrary passive references. If each δ_j<=δ, the term is `58978806 δ`. One may choose δ from a desired total tolerance after reserving explicit preparation/readout budgets. A residual uncontrolled generator D(t) can instead be charged by its actual global integrated norm through Duhamel, adding at most `2∫||D(t)||dt`; no volume-independent replacement of this global norm by an unproved local estimate is assumed. Precision preparation of the 2309-qubit product is an extensive supplied obligation. No error-correction threshold, robustness to a nonzero always-on drift, or practical timing accuracy is established.

## 7. Consequential controls and the preserved failed attempt

The controls address distinct semantic risks; they are not a collection of generic PASS counters.

**No occupation-ray filter.** Executing the actual arithmetic/predicate macro blocks on the correct commuting eigenvalue assignments accepts the neutral η=(1,3,5 occupied per cell), also accepts its same-cell occupied/empty swap generated by `A_(0,3)=X_1 Z_0`, and accepts the actual seam matter/flux transfer from the accepted joint source. In the seam case n_288 changes 0→1, n_1 changes 1→0 and the positive link at x=(3,0,0), axis x, changes flux 0→+1. Omitting that flux change yields two nonzero Gauss values and FAIL. These exact Boolean checks are a binding of the emitted arithmetic to the model; the existence of the corresponding matter rays/nonzero stream transfer is reused from the accepted joint proof, not inferred from a classical assignment alone.

**Link validity is not Gauss alone.** Changing one link from 00 to 11 leaves E=0 and all G=0 on the neutral occupations, yet the actual predicate returns FAIL. A single wrong specified Wilson sign also returns FAIL with all local cycles, link constraints and Gauss values good. The target is the complete original K.

**Within-PASS coherence.** Let ψ_0 be the accepted nonzero neutral ray with links 00, and ψ_1=A_(0,3)ψ_0. Both belong to K; they are orthogonal because B_0 differs. For `(ψ_0|0_R>+ψ_1|1_R>)/sqrt(2)`, the correct circuit returns PASS and preserves the full pure state. The actual mutant deletes the final five-CNOT uncompute of occupation bit 0 (543 physical records starting at record 28437302). The retained b_0 is then 0/1 on the two terms. Discarding that fine work produces the equal diagonal mixture while the visible flag still says PASS. The full trace-norm error on active+reference+flag is exactly 1: on the orthonormal two-ray/reference span, the difference has eigenvalues +1/2 and −1/2. This is not a half-trace-distance convention.

**Within-FAIL coherence.** The checker solves and verifies two literal pure-Z membranes M_0,M_1 of weight 16. Each commutes with every local cycle and all B's, and flips precisely W_0 or W_1 respectively. Their masks are archived with every signed-row parity check. Thus φ_0=M_0ψ_0 and φ_1=M_1ψ_0 are orthogonal, satisfy the link/Gauss conditions, and both fail K. They differ in W_0's bad bit. Deleting exactly the W_0 uncompute block (68 logical gates, 4428 physical records starting at 28443299) leaves that fine archive. The coherent two-ray/reference FAIL state is again dephased with trace-norm error 1, even though both terms have the correct FAIL label. The other loop uncomputations commute with this fine bit, so they do not erase the defect. All corresponding mutant NN streams are fully emitted, with exact compressed and raw hashes; they are not descriptions of an unexecuted hypothetical word. Their quantum error is proved on the two-ray subspace, not claimed from a dense full-system simulation.

**Toffoli phase and Gauss orientation.** The exact 8-column phase mutant in section 3.4 is nontrivial. The missing-complement arithmetic witness in section 3.2 rejects an actually neutral local input. These discriminate phase-exact compilation and the literal background/orientation identity.

**Dirty-transit return.** The third emitted mutant deletes actual physical record 29489400, SWAP between `(0,0,0)` and `(1,0,0)`, from the last routed CNOT. The first site is cycle-work qubit 1344; the second is dirty transit. The last logical gate of arity two is CX(1344,0), followed only by Z(1344), H(1344). Deleting that last return swaps the workspace and transit tokens; the subsequent single-site gates cannot return them. More explicitly, if R=H Z on the workspace site, the final faulty unitary differs by `R_a SWAP_(a,d) R_a†` after the correct whole unitary. The correct workspace is |0>; the dirty output instead contains the fixed state `R†|0>=|−>`. If d is initially half of a Bell pair with a passive reference, its joint Bell projector probability drops from 1 to 1/4. This gives a trace-norm error at least 3/2 by that binary discriminator. Thus checking the central-operation list without the reverse routing would be insufficient. The correct complete stream checks the token identity after every route and at the end.

**Preserved failure.** `run02_verify` failed after the correct Toffoli matrix had already passed: its deliberate first-T†→T mutation was incorrectly expected to fix basis column 000. It actually mixes that column as well. The repaired checker uses the stronger appropriate discriminator—nonzero entries outside the ideal Toffoli permutation—and does not change the compiler, emitted circuit, or ideal matrix comparison. The failed executed source, stdout, traceback, receipt, and exact `VERIFIER_REPAIR.diff` are preserved. `run03_verify` then completes successfully. The failure is a wrong auxiliary expectation about the mutant, not an omitted or concealed failed ideal circuit check.

## 8. Evidence, reproduction and remaining boundary

The complete execution records are:

- `run01_compile`: actual compiler, exit 0, 12.612 seconds; complete macro, logical and NN streams emitted.
- `run02_verify`: actual original verifier, exit 1, 0.334 seconds; the mutation-expectation failure above.
- `run03_verify`: repaired verifier, exit 0, 39.523 seconds; all exact signed/arithmetic/expansion/NN checks complete.
- `run04_controls`: targeted arithmetic scope checks and full mutant stream emission, exit 0, 4.557 seconds.
- `run05_source_identity`: source/extraction/run-record integrity only, exit 0, 0.107 seconds; **zero mathematical predicates**. It refreshes source hashes and does not add scientific validation.

Each run has an exact executed-source copy, before/after source identity, the actual command and interpreter, full stdout/stderr and a receipt. No external scientific Python module was imported into these runs; the exact read/copy provenance is disclosed above. The main compiler uses raw `i^p X^x Z^z` arithmetic; the model checker uses separately expressed local I/X/Y/Z products and Hermitian signs; the Toffoli check uses exact cyclotomic amplitudes; the arithmetic check uses a full Boolean truth vector; routing uses actual records and tensor permutations. These are materially different same-author calculation routes, **not independent acceptance**, a retained audit, or a claim of blindness to the target.

The binary formats are fully specified in `FORMATS_AND_REPRODUCTION.md`. `block_index.json` maps all 2697 blocks to exact macro, logical and physical spans. The raw SHA-256 values of the complete streams are:

| Stream | Raw/decompressed SHA-256 |
| --- | --- |
| Macro JSONL | `8aefef248b5843e10d5eaff48619a081ab6a776cc5df6c785ce46bdd31b2a8eb` |
| Logical `<BHH>` | `35df68cd975821a229f10c29d84579eb685c49d6e19f1432fadec4ee7ad517ee` |
| Physical `<BII>` | `643eda284bf0838f77e694a169736cd3fe8123c41b6ef401a7e0bc6e0cd891c5` |

The proposed conclusion is therefore a complete conditional literal binary admission compiler, with no unresolved code-generation placeholder under the stated contract. Its separate proof/code review remains open. What it closes is the finite operational gap between an abstract supplied projector P_K and an explicit coherent, returned-workspace open-box circuit for that same projector. What it leaves supplied is clean-workspace preparation, all addressed controls and timing, drift switching/compensation, and the one final flag instrument. It gives no native measurement dynamics, autonomous event/Record, free prepared code state, repair after rejection, arbitrary-state encoder, all-L family, or practical resource optimum. No canonical/Git/PR/audit/checkpoint/axiom/editable-prompt file was changed by this task.
