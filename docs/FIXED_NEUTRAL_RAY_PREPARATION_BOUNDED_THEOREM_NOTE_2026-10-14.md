---
title: Fixed neutral-ray preparation by a returned nearest-neighbor circuit
claim_id: fixed_neutral_ray_preparation_bounded_theorem_note_2026-10-14
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: fixed L4 neutral ray, supplied active product input, addressed gates after drift removal, arbitrary transit and passive reference
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: one accepted finite signed preparation word and full returned-route certificate with explicit supplied controls; identity runner evaluates no mathematics
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["joint_even_matter_finite_link_interface_bounded_theorem_note_2026-10-14", "openreference_cubic_recurrent_physical_m2_matter_compiler_cycle870_bounded_theorem_note_2026-08-02", "recurrent_encode_update_decode_sandwich_cycle883_bounded_theorem_note_2026-08-03"]
runner: scripts/fixed_neutral_ray_preparation_identity_2026_10_14.py
next_trace_action: separate root review and guarded integration of this publication package, then regular PR and independent retained audit
---

Claim type: bounded_theorem

# One fixed L4 neutral matter–link ray prepared by a returned nearest-neighbor circuit

**Current source status: accepted conditional finite preparation and source assembly; this publication rendering and driver require separate root review.** The source acceptance is `NEUTRAL_PREPARATION_ROOT_ACCEPTANCE.json`, SHA-256 `6e1e1bf011dfd5cb765c8ae1430efb2aebe809443b01992edb2aac8703509fbe`. It accepts the complete unchanged proof `0e002497bfa624ceb116059e092b3d853c36a969f37e96794675de3e3f587124`, with the control-budget qualification below, after the full source-exposed review `44c9768da5256b1e5f0fb2d16d76eca731d51fe88aacdf707924a26d94847a3f` and root disposition `cf772a99d047f341fa8d82ab334e65afbd53fad7cabe48e234a8c76830214100`.

The complete 32080-byte proof follows this wrapper verbatim. Its original provisional/pending-review wording, paths, timestamps and exposure descriptions remain historical source records. The later acceptance above supplies the current disposition. This wrapper introduces no changed equation, new theorem, independent check, retained/audit verdict or native realization.

## Fixed target and supplied interface

The target uses the literal L=4 joint architecture from the joint even-matter/finite-link interface: 960 matter-face qubits and 384 link qubits at its original 1344 physical coordinates. It is the unique common +1 ray of **all 1475 signed rows**: 704 local cycles, the three specified +1 Wilson generators, 384 signed B occupation rows and 384 positive link Z rows. The B signs specify directions 1,3,5 occupied in every coarse cell. Thus N=192 and Q_x=0; the 192 links are |00>, so every electric flux and every Gauss value is zero. This fixes one ray in K rather than merely testing membership in K.

All 1344 active factors start in the supplied product |0>. The other physical factors may have arbitrary states and arbitrary passive-reference correlations. The circuit is executed on the **ordinary open box** `{0,…,63}^3`, using externally addressable one-qubit controls and distance-one two-qubit controls, an external clock and supplied drift removal. Active-only distance-one edges are absent: intermediate physical qubits are necessary and are explicitly counted. Periodic coordinates define the target; routing never treats a periodic seam as an ordinary open-box edge.

The exact unitary has the form `V = U_active tensor I_transit`, with `U_active |0> = exp(i theta) |psi_eta>` for the specified ray. Consequently, for every normalized transit/reference state sigma_TR, the complete ideal output is `|psi_eta><psi_eta| tensor sigma_TR`. Returning transit means this tensor-factor identity, not just a matching classical token list or success on blank intermediates. No ancillary clean transit is required; the 1344 active product-zero inputs remain a supplied preparation resource.

## Emitted word, complete certificate and resources

The archived package contains the actual 14017-gate signed Clifford word, all 1475 target rows, the prepared 1344-generator tableau, every target-to-basis signed product mask, route indices, per-site usage, and the complete compressed 871249-record physical word. The original physical stream is 7841241 decompressed bytes with SHA-256 `2c6cdb35e8a4ec1df3c698b66ada091046ed4c4356abea02ac184eafef24ac58`. Its gzip hash is `75f001f0783dd3e05f804b35d45adbd1c6583522afa0c47218cdcb81054abd5d`.

The mathematical certificate relates every requested signed row to a product of the actual word's images of the initial positive Z generators. The coefficient masks have rank 1344, fixing exactly one ray; a negative-identity dependency cannot be hidden by an unsigned rank. A separate source-exposed calculation reconstructed the ordered loop phases by computational-basis action, propagated the actual word in the raw phase convention, checked every signed product, and compared every physical record to a literal returned open route. Small one/two-qubit matrix controls challenged both phase conventions; the reported H-matrix residual is floating-point, while the signed words and product certificates are exact. These roles remain distinct.

| Accepted resource | Value and scope |
| --- | --- |
| Required active product-zero inputs | 1344, including 56 ungated active factors |
| Additional clean transit | 0; idle hardware is still counted |
| Idle transit factors used | 21747, with arbitrary states/correlations |
| Required active plus used idle factors | 23091 |
| Physical sites actually touched | 23035: 1288 active and 21747 idle |
| Logical word | 14017 gates: H 2218, S 1626, X 641, CNOT 9532 |
| Physical word | 871249 primitives: 4485 one-qubit, 9532 CNOT, 857232 SWAP |
| Ordinary support | Arity at most two; two-qubit distance exactly one |
| Declared serial depth | 871249 slots, without a parallel-depth optimality claim |
| Largest logical route | Ordinary distance 184, using at most 185 sites |
| Largest scheduled site incidence | 1737 primitives |

Replacing SWAP by three CNOTs gives an arithmetic alternative count in the original source. That expanded word was not emitted or checked and is not the primary circuit or depth here.

## Control strength, time, precision and material limits

**Jc bounds the scheduled gate generators after drift removal. It does not bound or price a separate arbitrary drift-cancellation Hamiltonian or its apparatus.** Under the drift-off branch, the displayed control Hamiltonian applies a supplied one/two-qubit gate logarithm of norm at most Jc for a slot of duration pi/Jc. Under exact compensation, the same statement describes the net scheduled generator after cancellation; the compensator's norm, support, apparatus and cost remain separately supplied. In particular, an arbitrary `-H_drift+K_gate` need not have norm Jc or arity two.

The accepted serial gate duration is `871249 pi/Jc`; instantaneous scheduled per-site norm is at most Jc and maximum integrated scheduled norm is at most `1737 pi`. These are sufficient control resources, not a lower bound, autonomous clock, fuel ledger or physical positive-energy theorem. Product-input supply and precision, addressability, clock, switching, stopping and any later final readout remain supplied. This preparation circuit contains no final readout apparatus. The all-zero active input is initially outside K, with G_x=+3, so an always-on Gauss penalty cannot silently remain active during the proof.

For unitary primitive operator errors delta_j and a stated **joint** initialization trace error epsilon_init, the complete-output bound is `min(2, epsilon_init + 2 sum_j delta_j)`, including all idle and passive-reference factors. It requires no independent error statistics. It is not automatically an arbitrary dissipative or environment-memory noise theorem. Exact return and this error estimate do not price the mechanism that prepares the active product input or removes background drift.

The construction prepares the specific neutral eta ray. It does not implement an arbitrary CAR encoder, an arbitrary-state loader, an interacting ground-state algorithm, all-L preparation, native/autonomous dynamics, physical energy/clock/readout supply, photon identification or a continuum limit. Preparing this state through an open-box word does not convert the target model's periodic seam interactions into ordinary nearest-neighbor open-box Hamiltonian terms afterward.

## Dependencies, prior mechanisms and evidence status

The **one direct mathematical parent** is [joint interface](JOINT_EVEN_MATTER_FINITE_LINK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-10-14.md), SHA `212a94bb9cbd2a5d53a227d7d8103b7eca5cc018ec8bb5ca2c86c0ca660c8aef`, carrying complete core `34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca`. It supplies the literal graph/port order, coordinates, signed cycle/Wilson convention, B dictionary, link states and Gauss interpretation. The core and canonical note are two identities for that same mathematical parent, not two different premises. Their exact full bodies are preserved in the author archive and rechecked against live originals.

The local-uniformity branch is integration ancestry only. Its estimate, other penalty/controller/history results and the separately developed binary-admission construction are not mathematical inputs here. The package assigns no new graph edge to ancestry and executes no graph operation.

Generic stabilizer preparation, Clifford elimination, measured/feedforward corrections, returned SWAP routing and inverse circuits are existing machinery. The canonical [Cycle 870 returned routing](OPENREFERENCE_CUBIC_RECURRENT_PHYSICAL_M2_MATTER_COMPILER_CYCLE870_BOUNDED_THEOREM_NOTE_2026-08-02.md) and [Cycle 883 inverse and return](RECURRENT_ENCODE_UPDATE_DECODE_SANDWICH_CYCLE883_BOUNDED_THEOREM_NOTE_2026-08-03.md) citations provide mechanism attribution only, with their original recorded read limits; their other results and fixture counts are not imported. The original C240/C244/C870/C883 context and route-source exposure remain archived with their actual read limits. The contribution accepted here is this target's signed finite compiler, complete emitted word, full reference-return certificate and explicit resource/interface accounting, not a new general stabilizer theorem.

All three actual controls are retained. A wrong Wilson character leaves the specified sector despite neutrality. A same-cell occupied/empty swap stays in K but changes the target ray. Deleting actual reverse-SWAP record 871244 leaves an active/idle transposition despite correct central operands; a Bell transit/reference witness gives trace-norm error at least 3/2. The earlier first-block deletion is preserved only as an unexecuted candidate. The packaging `KeyError: 'procedures'`, its submitted source, observed traceback and explicitly post-hoc receipt remain intact; it was not a failed scientific run.

There were two author scientific executions and one separate source-exposed reviewer execution. The root performed no scientific rerun. This assembly copies and binds those results; it executes **zero mathematical predicates** and makes no new independence claim. Historical review/source statuses are preserved, with the current source acceptance stated above. The exact source assembly was accepted under `b901fd0b1c26861a39458f8693e30c0d8b3956d92f0da4d6e20f2de7130c9d00`, after root review `fe51280207166f58b57cbc8141517b9330fe551e5e3f7c2dc5c833cf87cec6c5`. This publication rendering, driver and actual-current-parent integration gates require separate root acceptance; retained audit remains a later step.

---

## Complete accepted author proof, reproduced verbatim

The historical status and exposure statements in this body are preserved. The preceding wrapper records later source acceptance and its required drift-cost qualification. No source sentence, equation, constant, program or evidence file is rewritten.

# Literal neutral-state Clifford preparation with returned open-box routing

**Claim type: bounded_theorem. Current author status: conditional-support; exact author construction/checks completed, separate substantive review pending.** The result is a finite preparation protocol under the external control contract below. It is not retained/audit status, native generation, an arbitrary-input encoder, a ground-state preparation, or an all-volume theorem.

The complete emitted word prepares the specific neutral L4 joint ray from 1,344 supplied |0> factors. It has 14,017 logical Clifford gates and 871,249 one-/nearest-neighbor-two-qubit primitives on an ordinary open box. Its 21,747 used idle transit factors may be arbitrary and reference-entangled and are returned exactly. The attached certificate verifies all 1,475 signed requested rows, including the three specified Wilson signs, through the actual emitted logical word, then verifies every physical gate record and every returned route. The methods are standard Clifford elimination and the previously used returned-routing construction; neither generic mechanism is claimed as new.

## 1. Exact domain, supplied resources and conclusion

The physical control graph is the ordinary unit-L1 graph on `B={0,...,63}^3`, with 262,144 ordinary qubit tensor factors. It has no edge from 63 to 0. The logical target uses the accepted periodic L4 matter/link definitions, placed at their literal representative sites in this box. Periodicity defines that target's operators; it does not shorten physical control paths.

Let A be its 1,344 active factors: 960 matter-face qubits and 384 qubits for 192 links. All other factors form T. The selected initial resource is

    |0><0|_A tensor sigma_TR,    |0>_A := |0>^(tensor 1344),

where sigma_TR is any density operator on the remaining box factors and an arbitrary passive reference R, including arbitrary entanglement within T and with R. The active product input is supplied; this protocol does not create clean qubits from unknown states. No transit blank is required.

The control premise supplies individually addressed H, S, X, CNOT and SWAP gates, a selected origin/coframe and an external serial schedule. Here H=(X+Z)/sqrt(2), S=diag(1,i), CNOT maps |a,b> to |a,b xor a>, and SWAP maps |a,b> to |b,a>, in the supplied local computational basis. The Z gates used only in the controls below can be realized as S squared; they are not part of the main word ledger. Every physical two-qubit operation acts on one ordinary nearest-neighbor pair. The background drift is switched off during the word or exactly compensated. Nothing here justifies an ideal gate in the presence of an uncompensated always-on penalty. A bounded-strength realization and coherent error budget are given in section 7; they remain supplied control assumptions.

Write psi_eta for the unique ray fixed by the signed rows in section 2, with matter occupations eta_(x,a)=1 for a=1,3,5, zero for a=0,2,4, and every link |00>. Let U be the emitted logical Clifford product in chronological file order, and V its emitted physical NN product. The result is

    U |0>_A = exp(i phi) psi_eta,
    V = U_A tensor I_T,

and hence, for every sigma_TR,

    (V tensor I_R)(|0><0|_A tensor sigma_TR)(V* tensor I_R)
      = |psi_eta><psi_eta| tensor sigma_TR.                       (1)

The phase phi is immaterial to this pure ray. The second equality is a routing identity on all physical inputs, proved below; it does not identify U with the accepted global CAR encoder on arbitrary input. The preparation claim uses only the stated product input. The target belongs to the fixed +++ Wilson common space K and has all Gauss values zero. It need not be a ground state of an interacting Hamiltonian.

The emitted word and exact arithmetic certificates are finite data, not an invocation of an unimplemented global encoder. They are supplied in full, with hashes and recording receipts, inside this package.

## 2. Literal model and all signed target rows

The coarse cells are `(Z/4Z)^3`, in lexicographic order. Each has direction modes in the order

    D_0=+e_x, D_1=-e_x, D_2=+e_y, D_3=-e_y, D_4=+e_z, D_5=-e_z.

Vertex `(x,a)` has index `6(16 x_1+4 x_2+x_3)+a`. At each cell, enumerate its twelve unordered nonopposite pairs a<b lexicographically, followed by its three positive-axis stream edges `(x,2a)--(x+e_a,2a+1)`. This gives 960 graph edges/face qubits. At each mode the five incident edge indices are ordered increasingly. On those physical qubits define

    B_v = product_(e incident v) Z_e,
    A_uv = epsilon_uv X_e
           product_(f<e, f incident u) Z_f
           product_(f<e, f incident v) Z_f,
    epsilon_uv = +1 for u<v, -1 for u>v,
    n_v=(I-B_v)/2.

No seam sign is removed. For an oriented cycle with r vertices, use the signed Pauli

    S(c)=i^r A_(v0 v1) A_(v1 v2) ... A_(v_(r-1) v0).             (2)

The requested list contains all of the following rows, each interpreted as a +1 stabilizer:

* 512 triangles: at each cell, choose one signed direction on each of the x,y,z axes and traverse them in axis order;
* 192 octagons: for each corner c and omitted axis k, let a<b be the other axes and x_ij=c-i e_a-j e_b; traverse `(x00,-a),(x00,-b),(x01,+b),(x01,-a),(x11,+a),(x11,+b),(x10,-b),(x10,+a)`;
* three Wilson rows: for axis a and b=(a+1) mod 3, concatenate `(j e_a,+a),((j+1)e_a,-a),((j+1)e_a,+b)` for j=0,1,2,3, then close;
* 384 occupation rows `(-1)^(a mod 2) B_(x,a)`;
* 384 positive single-qubit Z rows on the link qubits.

All coarse coordinates in these graph definitions are reduced modulo 4. The full literal list therefore has `704+3+384+384=1475` signed rows. Keeping redundant rows matters: unsigned rank alone would not certify the chosen phases or the selected pure ray.

The physical coordinates, reduced modulo 64 and then represented in 0,...,63, are

    internal face (x,a,b): 16x+2(D_a+D_b),
    positive stream (x,axis a): 16x+8e_a,
    link p_(x,a): 16x+6e_a,
    link q_(x,a): 16x+10e_a.

Link labels are `|-1>=|01>`, `|0>=|00>`, `|+1>=|10>` with unused |11>; `E=n_p-n_q`. The actual Gauss operator is

    G_x=sum_out E - sum_in E - (sum_(a=0)^5 n_(x,a)-3).

The target B eigenvalues specify precisely three occupied directions per cell and 192 particles in total, an even number. Positive link Z fixes |00> and E=0. Therefore every G_x annihilates the prepared ray. The 704 local plus three Wilson rows select exactly the supplied +++ matter sector; no Wilson penalty or unspecified Wilson representative is substituted.

`artifacts/model.json` gives every literal edge and all 1,344 coordinates. `artifacts/target_rows.jsonl` gives all 1,475 rows with their labels and raw convention `i^p X^x Z^z`. For a Hermitian Pauli, this equals `(-1)^r i^(popcount(x&z)) X^x Z^z`, where `p=2r+popcount(x&z) mod 4`. These are actual signed rows, not only support masks.

## 3. Deterministic signed Clifford construction

The compiler works with raw Pauli triples `(p,x,z)` representing `i^p X^x Z^z`, where p is modulo 4 and x,z are finite bitsets. Products obey

    (p,x,z)(q,y,w)
      = (p+q+2 popcount(z&y) mod 4, x xor y, z xor w).             (3)

Equation (3) follows by moving the left Z factors past the right X factors. It is used for the ordered loop products in (2), including their orientation phases.

First select independent rows by exact binary elimination of `(x,z)`, retaining their original signs. Exactly 1,344 rows are selected. This binary choice is only a basis selection; the later signed certificate checks every original row, so an inconsistent redundant sign would be rejected.

For the selected commuting independent generators, perform the following deterministic reduction. Store all generator columns as row bitsets, together with both bits of the raw phase. Process selected rows in their retained order. Previous pivots have been made positive single-qubit Z rows and cleared out of all later rows. In the current nonzero row, choose the least-index supported unprocessed qubit q.

1. If the row is already a signed single Z_q, skip directly to step 3. Otherwise turn every supported local letter into X: apply H to a Z-only letter and S* to a Y letter, keeping all induced phases.
2. For that converted X row, apply CNOT(q,j) to each other supported qubit j in increasing order, clearing its X. Apply H_q, giving a signed single Z_q.
3. If that sign is negative, apply X_q. The pivot is now positive Z_q.
4. Every remaining generator commutes with Z_q, so it has no X_q component. Multiply each remaining row with Z_q component by the positive pivot to clear that component. This last operation is a generator row operation, not a physical gate and is not charged as one.

The actual conjugations in the raw convention are

| Gate | Bit/phase action |
| --- | --- |
| H_q | swap x_q,z_q; add `2 x_q z_q` to p |
| S*_q | replace z_q by z_q xor x_q; subtract x_q from p |
| X_q | add `2 z_q` to p |
| CNOT(c,t) | replace x_t by x_t xor x_c and z_c by z_c xor z_t; p unchanged in the raw all-X-then-all-Z convention |

Earlier pivots are untouched because all new gates use unprocessed qubits. Commutation and independence are preserved. The row operation in step 4 has no sign contribution: its multiplier is positive pure Z_q and the row has x_q=0. Each step removes one unprocessed qubit and one independent generator, so induction ends with all positive single-qubit Z generators. The resulting reduction Clifford D maps the selected target group onto the |0> stabilizer group. The preparation word is its inverse `U=D*`, obtained by reversing the recorded physical gates and replacing S* by S. No row operation is mistaken for an implementable gate.

The exact emitted reduction has 14,017 gates. The preparation word has

| Logical primitive | Actual count |
| --- | ---: |
| H | 2,218 |
| S | 1,626 |
| X | 641 |
| CNOT | 9,532 |
| Total | 14,017 |

The complete preparation word is `artifacts/logical_word.jsonl`, SHA-256 `a5129c29e76c1e3315d54ca9b3636077ba7272d91e99be535ded01c758c8fcc0`. File order is chronological: if its records are g_1,...,g_m, the matrix U is `g_m ... g_1`. The reduction word and every selected-row/pivot choice are also emitted. There are no logical link gates; their prescribed |00> input is retained, including when their factors serve temporarily as routing transit.

### Exact signed certificate of the actual word

The separate checker does not import the compiler or historical checker code. It reconstructs the literal graph and target rows anew using an explicit I/X/Y/Z local multiplication table with Gaussian quarter-turn phases, rather than the compiler's raw-XZ product routine. It compares every reconstructed signed row and coordinate to the emitted target/model files.

It then uses the Hermitian sign convention `(-1)^r i^(|x&z|) X^x Z^z`. Its Clifford updates include the CNOT sign

    r <- r xor [x_c z_t (x_t xor z_c xor 1)],
    x_t <- x_t xor x_c,    z_c <- z_c xor z_t,                    (4)

with the old bits on the right. H flips r on x_q z_q; S flips r on x_q z_q and toggles z_q by x_q; S* flips r on x_q(1-z_q) and toggles z_q; X flips r on z_q. These rules follow from the elementary Pauli conjugations, with (4) accounting for the change in the number of Y factors. This is a distinct phase bookkeeping implementation, not a claim of a blind or separately authored review.

The checker propagates **all 1,475 target rows backwards through the actual emitted preparation word**, using inverse gates. Every resulting row is a positive Z word. Their binary rank is 1,344. This is a finite signed certificate: positive Z words fix |0>, and full rank means they generate every single Z_q, so their common +1 space is one-dimensional. By conjugation the target rows likewise have a unique common ray and U|0> is that ray. A negative identity dependency could not pass this check.

The checker also propagates all 1,344 initial Z generators forward through that same word and emits the complete prepared tableau. For every requested target row, it multiplies the specified subset of these forward generators with exact phases and recovers the target row. `verification/target_to_prepared_basis.jsonl` contains every coefficient mask and `verification/prepared_tableau.jsonl` contains the full signed basis. This binds the exact word to the requested target, rather than only checking a separately synthesized tableau. The direct commutator census found zero noncommuting pairs among all requested rows.

## 4. Ordinary open-box nearest-neighbor compilation

Every active coordinate has even components. Consequently the active-only unit-distance graph has no edges. The protocol admits and counts intervening ordinary box factors rather than declaring a long gate nearest-neighbor.

For a logical CNOT from active site a to b, choose the monotone open Manhattan path that first changes x, then y, then z, one unit per step. This remains in 0,...,63. Write the path as `v_0=a,...,v_d=b`, where d is the ordinary L1 distance. Emit, chronologically,

    SWAP(v0,v1), ..., SWAP(v_(d-2),v_(d-1)),
    CNOT(v_(d-1),v_d),
    SWAP(v_(d-2),v_(d-1)), ..., SWAP(v0,v1).                      (5)

For d=1 the two SWAP lists are empty. Every displayed two-qubit support is an actual unit-distance pair. One-qubit logical gates are emitted at their literal active coordinates.

Let R be the forward SWAP permutation in (5). It sends the original control factor to v_(d-1), leaves the target b at v_d, and only permutes the intervening factors. Tensor-permutation conjugation gives

    R* CNOT_(v_(d-1),v_d) R = CNOT_(a,b) tensor I_(other factors). (6)

This is an operator identity on arbitrary states, not a blank-transit argument. The intervening factors may include other already-entangled active qubits and arbitrary idle/reference-entangled qubits. Reverse SWAPs restore their full states and correlations. These are ordinary qubit SWAPs; adding fermionic exchange signs would be wrong, because the encoded fermionic signs already reside in the physical target Pauli/state construction.

Concatenating (6) and the one-qubit gates proves `V=U_A tensor I_T`. The route has `2(d-1)+1=2d-1` two-qubit primitives. No gates from different blocks are parallelized in the declared schedule, so the full primitive count is also its serial depth.

### Literal stream verification

The full emitted word is `artifacts/nn_word.bin.gz`, not a route-count proxy. Its decompressed stream has 871,249 records, each exactly nine bytes in little-endian `<BII>` format: opcode, flattened site a, flattened site b. Flattening is `(64x+y)64+z`; one-site b is `0xffffffff`. Opcodes are H=1, S=2, S*=3, X=4, CNOT=5, SWAP=6, Z=7. The actual word uses H,S,X,CNOT,SWAP. The gzip omits timestamp dependence (`mtime=0`); its raw record hash binds the word independently of compression-library details. Compression changes no operation.

`artifacts/route_index.jsonl` binds each logical gate to its consecutive physical records. The checker reads every physical record, checks its site bounds and ordinary NN condition, and tracks every routing SWAP as a permutation of all 262,144 factor labels. At each central operation it checks the actual original operand labels and orientation against the logical word already certified by the signed tableau. It verifies identity of the resulting permutation after every block and at the end. It also checks that the physical stream has no missing/trailing records and computes its complete uncompressed hash.

This checks a sufficient full-operator certificate for (6): route-only operations are literal SWAPs, the central gate acts on the intended original factors, and all other factor labels return. It does not simulate the full-box Hilbert space. The reference extension follows from the proved tensor-factor identity; it is not inferred from a selected unentangled numerical state.

## 5. Actual resource ledger

The emitted route lengths have sum 438,148 over the 9,532 CNOT blocks. Their maximum is 184, so the largest block touches 185 sites and contains 367 two-qubit primitives. The complete histogram is preserved in `artifacts/CONSTRUCTION_RESULT.json`.

| Resource | Actual value or explicit supplied capacity |
| --- | ---: |
| Active product-input factors | 1,344 |
| Matter/link active factors | 960 / 384 |
| Additional clean transit factors required | 0 |
| Used idle transit factors, arbitrary state allowed | 21,747 |
| Active factors touched by any emitted gate | 1,288 |
| All gate-touched factors | 23,035 |
| All active inputs plus used idle factors | 23,091 |
| Available ordinary box factors | 262,144 |
| Idle box capacity | 260,800 |
| Physical H / S / X | 2,218 / 1,626 / 641 |
| Physical central CNOTs | 9,532 |
| Physical routing SWAPs | 857,232 |
| One-qubit primitives | 4,485 |
| Two-qubit primitives | 866,764 |
| Total primitives and serial depth | 871,249 |
| Maximum primitive incidence at one physical site | 1,737 |
| Maximum simultaneous interaction arity | 2 |
| Maximum two-site ordinary separation | 1 |

The 56 active factors never touched by a gate still count among the required active product inputs. Available box capacity, actually touched factors and prepared active factors are distinct counts. The detailed per-site incidence record is `verification/physical_site_usage.jsonl`; no idle transit capacity is treated as unpriced hardware or as a free blank.

SWAP is an explicitly supplied two-qubit primitive in this theorem. If it is subsequently expanded as three nearest-neighbor CNOTs, arithmetic gives 2,581,228 CNOTs and 2,585,713 total primitives. That secondary expansion was **not emitted or executed here** and is not the primary word or depth being certified.

The physical raw stream is 7,841,241 bytes; its saved gzip is 757,784 bytes. Its hashes are:

    compressed:   75f001f0783dd3e05f804b35d45adbd1c6583522afa0c47218cdcb81054abd5d
    uncompressed: 2c6cdb35e8a4ec1df3c698b66ada091046ed4c4356abea02ac184eafef24ac58

The entire evidence package is modest in size (the pre-documentation inventory was 6,630,145 bytes); the final freeze records exact member sizes and total size. No large dense matrix or unbounded enumeration is hidden behind these compressed files.

## 6. Three discriminating controls and their exact scope

### Wrong Wilson character

The checker solves the actual binary equations for a physical Z word M_W which commutes with all 704 local cycle rows and anticommutes with precisely W_0 among the three fixed Wilson rows. It uses the literal loop X supports and checks every equation, rather than assuming a sign-free topological representative. The resulting word contains 64 single-site Z gates, listed in full in `verification/signed_state_controls.json` and appended to the complete base word in `verification/wrong_wilson_logical_word.jsonl`.

Replaying this actual mutant word through the signed checker gives exactly one failed target row, `wilson:0`. All B signs, link Z signs, local cycles and all 64 Gauss values remain correct. The state is orthogonal to the target and lies outside the specified +++ K. Thus checking only local cycles, charge neutrality or unsigned rank would miss this error.

### A neutral but different occupation ray inside K

At cell (0,0,0), use the actual nonopposite mode pair u=0 (empty) and v=3 (occupied). Its literal A operator is `A_(0,3)=X_1 Z_0`. Append the two local gates Z_0 and X_1 to the emitted preparation word. The checker finds exactly the failed occupation rows `B:0,0,0:0` and `B:0,0,0:3`. Every local cycle, all three Wilson rows and all link Z rows remain positive. This transfers one occupation between two modes in the same cell, so that cell still has three particles; all Gauss values remain zero.

This mutant lies in K but is orthogonal to the requested ray. Therefore K membership alone is an insufficient preparation certificate. The complete mutant word and signed failures are preserved, not discarded as an irrelevant negative test.

### Missing final reverse SWAP

The executed routing control deletes physical record 871,244, the final reverse SWAP in the last logical CNOT block (logical index 14,012, zero-based). That record exchanges site 8320=(2,2,0), an active control, with site 8384=(2,3,0), an idle transit. Four active one-qubit gates follow and no later two-qubit operation occurs.

The checker actually replays the altered permutation and hashes the full one-record-deleted stream. It ends with the nonidentity transposition 8320<->8384. Crucially, the central-operation stream still has **zero operand mismatches**. Thus a gate-stream-only check would pass while the return obligation fails. The exact deletion descriptor plus the complete base word determines the entire mutant; its uncompressed SHA is `a98222ccd42e50998a3ae53885ab4ff7a7305fb7e88db65ebd06e9b38d36e870` and it has 871,248 records.

There is also a full-channel witness, not merely a bookkeeping rejection. Before the word put that idle factor in a Bell state with a passive reference, independently of the active |0> input. All preceding correct routes return it. If the final return gate S is omitted from the selected block, the mutant block equals S times the correct block. It swaps the active output with this idle Bell half. The later one-qubit gates act only on active sites and cannot restore the idle-reference Bell state. Its final idle-reference reduced state is `rho_a tensor I_R/2`, where rho_a is the selected active factor's pre-swap marginal. Its overlap with the original Bell projector is 1/4 rather than 1. The reduced trace-norm error is therefore at least 3/2, using the unit-norm observable twice the Bell projector minus identity. This proves failure of arbitrary-transit return for that actual deleted-gate word.

The constructor's result file also records its first-routed-block deletion **candidate** (record 10). It is not presented as an executed control. The verifier deliberately selected the final CNOT block instead, so the above full-channel witness cannot be obscured by later routing. The executed control and actual mutated-stream hash are only those in `verification/missing_reverse_swap_control.json` and the verification receipt.

## 7. Strength, time and error accounting

Take a supplied strength J_c>0. For each one-/two-qubit primitive G, choose its Hermitian spectral logarithm with eigenphases in [-pi,pi]. With slot duration `tau_c=pi/J_c`, a supplied local generator K_G satisfying `exp(-i tau_c K_G)=G` has `||K_G||<=J_c`. Apply one such term at a time. Every term has arity at most two and unit-distance support when two-site. The instantaneous per-site sum of control-term norms is at most J_c. This controls a supplied externally scheduled Hamiltonian; it does not derive that control law from the framework.

For the emitted serial word,

    T_prepare = 871249 pi/J_c.                                  (7)

A site's summed active slot durations are at most `1737 pi/J_c`, and its integrated control norm is at most 1737 pi. The total time in (7) is the entire serial schedule, not that per-site count. Gate logarithms and their scalar offsets are not identified with a positive physical energy law. Drift compensation, addressing, switching and the external stop time remain supplied; their physical mechanism is not priced as autonomous hardware by this theorem.

For implemented unitary primitives Gtilde_j with complete local operator errors `||Gtilde_j-G_j||<=delta_j`, the product telescope gives

    ||Vtilde-V|| <= sum_j delta_j.

Tensoring any passive reference preserves this operator norm. If the actual initial state is within trace norm epsilon_init of the specified active-product/transit-reference resource, then

    ||rho_out - |psi_eta><psi_eta| tensor sigma_TR||_1
       <= min(2, epsilon_init + 2 sum_(j=1)^871249 delta_j).       (8)

This is a global joint-output estimate including transit and its reference correlations. It neither assumes independent gate errors nor substitutes a per-site count for the full gate count. With exact initialization, a common sufficient error is `delta_j<=epsilon/1742498`. Under a supplied product preparation of the individual active inputs, their separate trace errors can be summed to bound epsilon_init; correlated input preparation requires the explicit joint bound instead. No unknown transit preparation error is charged because the ideal identity holds for every sigma_TR.

The actual physical |0> input is not already a neutral K state: all B_v are +1, the matter occupations vanish, and with zero links G_x=3. The gates can also leave the constraint sectors during preparation. The drift-off/exact-compensation premise is consequently material. A large always-on penalty does not validate these uncompensated gates.

## 8. Source roles, exposure and prior work

`SOURCE_MANIFEST.json` pins the exact live inputs and their unchanged archived bodies. The central model definition is the accepted joint source `34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca`; its canonical body is `212a94bb9cbd2a5d53a227d7d8103b7eca5cc018ec8bb5ca2c86c0ca660c8aef`. These supply the literal ordered A/B/cycle/Wilson/link/coordinate definitions and the interpretation of K and eta. This construction does not import the penalty recovery or local averaging theorem. Its own signed word certifies this particular target ray directly.

The source-bound reconnaissance is `a7041d8ada95360a0c8720d1fcc3948b381787edcb2eeab1d72b024d0eebee33`, read completely for this task. Its targeted repository/archive/open-PR overlap coverage is reused at the same pins, not repeated or promoted to an exhaustive novelty assertion. The closest prior sources and roles are:

| Source and exact SHA | Role here |
| --- | --- |
| Cycle 240, `fc8acdba1ea7d4552f32ed3ab72540c415696ba0c05c5187e6b9d7f74a8021ee` | Prior deterministic measurement/feedforward preparation of the square-pyramid even vacuum, including Wilson correction. Generic stabilizer preparation is already present. This note emits a different coherent fixed-neutral-ray word and its full physical routing. |
| Cycle 244, `af551c19cbf714d47c23518cf7914598bd093d1d69c9f4a8034495f6e3b96256` | Prior classical marked syndrome gather/solve/broadcast and its limits. Context/comparison only: this offline coherent compiler does not import those propagation or root-compute counts. |
| Cycle 870, `74beb1de39ea0e579b8c709fdb294602f8cb959f1283b7556eb4c62335fd2e2b` | Reuse of the returned NN routing mechanism and arbitrary-transit verification discipline for different open reference fixtures. Equations (5)–(6) reproduce its relevant mechanism with the current coordinates and actual word. No old fixture counts or periodic-code theorem are transferred. |
| Cycle 883, `f25441ace48d2b850aa6ac5b03601d4e71de4821775ee21c7dc6dc8414169fbd` | Prior inverse/return and recurrent encode-update-decode result on those open fixtures. Context for supplied first clean input and return scope; not a preparation of this periodic neutral ray. |
| Cycle-870 route code, `6ae587e6bd8769e0b6880199d7a95023649464f625211bcb0530c21634a7e3ab` | Previously read complete `manhattan_path`, `in_capacity`, `route_word` region. Mechanism exposure is disclosed. No old module was imported/executed or copied into the new programs. |

Prior full reads of C240, C244, C883 and the accepted joint proof are reused unchanged. C870 coverage remains the earlier lines 1–185 and 200–350; its route-code coverage remains 813–905. The joint neutral-ray argument at lines 122–179 was refreshed in this task; the immediately preceding exact-source review also refreshed definitions 1–123 and operator/geometry arguments 179–250. The canonical wrapper's earlier lines 1–85 coverage is reused, while the original complete joint mathematical body carries the proof premises. Hash matching does not upgrade partial read coverage.

The new compiler and checker are both authored in this source-exposed context with the target known. Their differing Pauli conventions and full-stream check provide meaningful cross-checks, but do not constitute an independent scientist/reviewer, blind derivation, physical experiment or retained audit. No external theorem or primary paper is newly imported. Standard stabilizer algebra is proved at the scope needed above, and known routing/preparation methods are attributed rather than called novel.

The selected model/effort and no-delegation brief were preserved. Pinned SCIENCE_WORKFLOW and AGENTS coverage was reused from main `583c699e859b64ff01c8bc92d1c04bdfe9994509` and instruction revision `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. The physics-loop skill supplied the bounded proof/evidence discipline; explicit task restrictions govern this source-only output and prohibit canonical/Git/checkpoint/publication changes.

## 9. Actual executions, reconstruction and remaining obligation

Two scientific programs were executed once each, with Python 3.13.5 on the recorded host. No previous suite or historical program ran.

| Run | Actual UTC interval and result | Executed source / full stdout SHA-256 |
| --- | --- | --- |
| `run01_construct` | 09:00:01.149956–09:00:01.872231 on 2026-10-14; exit 0; 0.722280 s wall time | source `6a7ab9b4db168899155d85c3c14976b46178e284d627958aae024cd2e54dcc29`; stdout `a61c13964f2f6a50e0a8baf028f56f2576bded93df34831a30d44d7e71e15723` |
| `run02_verify` | 09:04:45.342891–09:04:47.542202 on 2026-10-14; exit 0; 2.199347 s wall time | source `c96ed1380bb47278631d26c493230e38a0c939908a09fcc09ba32d907411a610`; stdout `7d335cd6af1e08fd5aaa4212589e818a0b6a4729e7f2d53fcff48719f66e70f2` |

Each run preserves the exact executed source copy, start/end times, command, Python/platform details, source hashes before/after, exit code, complete stdout and complete empty stderr. The recording wrapper is `record_run.py`, SHA `0f4de989012cdd6ba51728bdefa6ef9a63b1c3802f719ef4d710e3a4d3911696`. Full actual stdout and both recording receipts were read. There was no failed scientific execution; the failed mutant obligations are retained as actual mathematical/control findings, not erased to obtain a pass summary. A later inline sealing attempt failed before creating the freeze because it looked up `procedures` instead of the manifest's `procedures_reused`; `freeze_attempt01/` preserves its exact submitted source, full tool-observed traceback and an explicitly post-hoc receipt. It ran no mathematical predicate and changed no scientific program/output.

The full signed prepared tableau has SHA `415dce74bcc727e52ffb3ebabaf868bcb0b343df35aee5aa3919354eb09b9562`; the all-row coefficient certificate has SHA `78c7289b0db45439328778def232689940755fd36085c84b06c81f5233ee291d`; the literal requested-row file has SHA `9ec0b039546bd83c7f094678dcf4b6770f27c1cb3ef731568ace86d72a6373a4`. These hashes identify the exact data; they do not themselves prove any mathematical predicate.

Reproduction commands and binary format are in `README.md`. A new attempt must use fresh output/run directories; the programs refuse to overwrite an existing run/output directory. The final freeze inventories every source, emitted artifact, control and raw stream. No source or failed attempt is cleaned away.

The next obligation is focused separate review of the literal row generation, Clifford phase rules, signed word certificate, physical token-return argument and control/precision accounting. The author certificate supports the finite conditional result; it does not discharge externally supplied blanks, addressability, drift cancellation, controls or clock. Switching on the accepted periodic interaction afterward remains a separate supplied operation; this open-box preparation does not make its seam interactions ordinary short-range terms. It also does not provide readout, autonomous stopping, arbitrary-state encoding, interacting-ground-state preparation, native dynamics or an infinite-volume limit. No canonical source, Git state, PR, operational checkpoint, axiom or editable prompt was changed.
