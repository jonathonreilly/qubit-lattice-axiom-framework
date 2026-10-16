# Exposed review of the emitted sparse-compiler fixture

**Disposition: supports the claimed numerical fixture, with the stated certification and scope limits.** The complete source implements the declared q=1,L=1 target on the full ancilla-zero data input space, emits the reviewed logical formulas in the correct chronological order, and routes the saved elementary gates with full adjacent SWAPs. An independently written inspection checked every saved route and gate count, the exact determinant-omission subsequence, and all saved matrices. No inconsistency or load-bearing implementation defect was found. This is evidence about one emitted circuit; it is not a rigorous residual certificate, an efficient compiler, or a new proof of the general theorem.

The check is source-exposed and uses the same inherited model and effort. I previously read and reviewed the mathematical parent. No author compiler was imported or rerun, and no circuit propagation was independently executed. The present actual execution is an exact structural inspection of saved JSON plus floating-point reanalysis of the author's saved matrices. It is more than hash bookkeeping but less than an independent circuit simulation. Those distinctions apply to every numerical conclusion below.

## 1. Sources and exposure

The controlling fixture review is 12442 bytes, SHA256 `c9e99e725b3efd8dabbf551c315e983113129de0ed12d5f9028c207f93fe9649`; its `FREEZE.json` is SHA256 `2b62a1ba9241999824241c41f191674c3a66c0829185e5bc6ea76052fcc40582`. All 22 freeze members plus the seal were verified and captured under `fixture_source/`, including the complete source, actual source/launcher at launch, receipt, both streams, RESULT.json, all four gate lists, segments and all saved matrices. `SOURCE_MANIFEST.json` gives exact originals, captures, sizes and hashes.

The complete 17836-byte `emitted_word_fixture.py`, SHA256 `e7dc44e6493fb9d847390161e109d3fe58d5124fb1ce8e308eeec4dfd93bb7c8`, was read. Its bytes match `runs/attempt_01/source_at_launch.py`. The original and captured launchers match at SHA256 `fd9229b989b33e4a3959dc42fcbadcc016b82dc0ef56cccd6436b672cf03deb5`. Review, exposure, manifests, launcher, seal source, actual receipt and complete streams were inspected. A combined tool output initially truncated metadata; affected material was reread untruncated rather than treating that output as completed coverage.

The sparse derivation remains SHA256 `6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b`, with seal `1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9`. My unchanged prior sparse review is SHA256 `2af89ecefd2d682259e967cc96ef1f5965c37500de4d3cc9261cb39d50254a2a`, with seal `54c2e39507456f530ae87534d58ed24412b5de0bfe1669f7ba6600781ae55fe9`. Exact copies of the latter two identity/exposure records are in `prior_review/`; this is not a second copy of that packet's entire member closure.

The unchanged local-control parent is SHA256 `c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60`. Necessary parent coverage, including the previously inspected Bai–Marvian primary at SHA256 `add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8`, is reused at the identical identities. The paper was not newly downloaded or reread for this fixture. Prior root/author phase-route exposure remains known; no new root review or unrelated worker result was consulted.

## 2. Complete target and basis conventions

Independently of the compiler functions, the target specified by the review is

`z=(5+12i)/13`,
`V=z [[3/5,4i/5],[4i/5,3/5]]`,
`det V=z^2=(-119+120i)/169`.

The interior matrix has determinant `(9+16)/25=1` and is unitary; |z|=1. With q=1,L=1,M=3, the selected pairs from the prefix rule are exactly

| Total charge | Data strings | Indices |
|---|---|---|
| 1 | 0100, 1000 | 4, 8 |
| 2 | 0110, 1100 | 6, 12 |
| 3 | 0111, 1110 | 7, 14 |

There are six selected vectors and ten complementary four-bit states. The upper charge-three block is included. Each selected column changes for this V; that conclusion is specific to the fixture, not a generic support count for arbitrary V.

The source starts from the 16-dimensional identity and replaces precisely these three 2-by-2 principal blocks by V. Therefore the complement is explicitly identity, not absent. It constructs J by `J[2j,j]=1`, corresponding to an appended zero fifth qubit in the stated MSB-first convention. The saved target has all 32 output rows and all 16 data input columns. The independently written inspector rebuilt the target directly from these indices and V, checked exact equality of the saved binary floating arrays for V, U, J and J U, and verified every saved array's shape, complex128 type and finite entries.

This is a full input-isometry comparator. Mathematically, a certified bound on `||CJ-JU||` would extend to arbitrary data/reference states without a reference-dimension factor. The program evaluates that matrix norm numerically; it does not prove the reported value is a rigorous upper bound. No output row is dropped, no test-state sampling replaces the matrix, and no optimized global phase is fitted.

## 3. Givens, phase orientation and chronological order

For the first target column `(a,b)^T`, the exact radius is one. The source forms

`G=[[conj(a),conj(b)],[-b,a]]`,

with its numerically computed radius retained. Direct multiplication gives `GV=diag(1,det V)`, so `V=G^*D`. The chronological order must therefore be D first and G* second. The source appends `phase + gu`, which is correct.

The phase pairs in the five-bit physical space are `(16,1)`, `(24,9)`, `(28,13)`, namely `(10000,00001)`, `(11000,01001)`, `(11100,01101)`. The first vector in each pair has ancilla zero, and its partner has ancilla one with the first old excitation removed. These are equal-charge, distance-two pairs.

The `two_level` routine selects `t0` where the first string changes 0→1 and `t1` where it changes 1→0. Thus its first string is always `|01>` in the ordered target sites `(t0,t1)`, even for the phase gates whose target order is `(ancilla site 4, old site 0)`. Passing `diag(exp(i theta),exp(-i theta))` consequently gives det V to the desired ancilla-zero vector, not its inverse. All other bit positions become the specified spectator controls.

The data Givens gates have two controls on four data sites; the fifth site is untouched by their logical definition. The phase gates have three controls on five sites. A completed phase gate preserves the entire ancilla-zero subspace. Each data Givens does likewise. Hence concatenating sectors returns the ancilla on every data input. The whole ancilla-one action need not be identity, and phase/Givens operations from different sectors need not commute there. That is allowed by the full-isometry contract and does not justify dropping ancilla-one outputs from the numerical residual.

The source's `product` reverses the list of matrix factors but retains each factor word's chronological internal order. If the factors denote A B C, its emitted word applies C, then B, then A. The subsequent `execute` multiplies each chronological gate from the left. These conventions agree throughout the conjugations, commutator and Euler products.

## 4. Logical emission and spectator control

The code emits exactly the reviewed base alphabet, forward `A=exp(i pi R/4)` and onsite `Z(phi)=exp(i phi Z)`, with phi wrapped modulo 2pi. There is no uncounted inverse primitive: A* is seven forward copies and inverse iSWAP is six.

`ex` emits `S_0^* A Z_0(theta/2)Z_1(-theta/2)A^*S_0`, replacing S factors by the paired opposite Z angles. Their individual scalar factors cancel at the logical level. `fword` emits both F and F* with the correct order and 2/6 powers. `controlled_x` emits

`E(theta/2) F^* S_1^* E((-1)^bit theta/2) S_1 F`.

Under the reviewed full-three-qubit identity this is the exchange rotation on the requested control bit and identity for the other bit. The code does not implement only the selected transition and forget other target states. Each such word has 50 letters: 40 A and 10 Z.

For U=aI+i(bX+cY+dZ), direct multiplication of `exp(i gamma X)exp(i beta Y)exp(i alpha X)` gives

`a+ib=cos(beta) exp[i(gamma+alpha)]`,
`c-id=sin(beta) exp[i(gamma-alpha)]`.

The `atan2` formulas in `euler_xyx` solve exactly this convention. The Y rotation is implemented by `S_0 X S_0^*`. Three controlled X words and that additional S pair cost 152 letters, specifically 120 A and 32 Z. The numerical code checks every reconstructed SU(2) before emitting it. Its small-value branch thresholds are implementation heuristics for this floating fixture, not exact zero-decision or certified general-input algorithms.

`commutator_factors` uses the reviewed construction: choose an axis perpendicular to the SU(2) axis, take its pi rotation for B and a half-angle rotation for A, so `ABA^*B^*=U`. The zero-vector branches select the specified ±I cases. The code records a full 2-by-2 commutator residual before recursive emission. `controlled_many` partitions the spectator list and emits the four factors on the same target sites. When either control group fails, the surviving pair cancels. This is the full control-space construction, with no clean flag ancilla.

The fixture actually reaches k=2 and k=3, whose leaf counts are four and ten. It does not exercise greater-than-two logical basis distance, because `two_level` asserts one 0→1 and one 1→0 difference. That restriction is explicit and appropriate for these q=1 pairs. It is not an implementation of every part of the general compiler.

## 5. Every saved route and count

The emitted lists are complete JSON artifacts. The independent inspector consumed every record without importing the emitter. For every logical gate, it gathered the corresponding consecutive routed records, checked kinds, sites, legal angle range and role ordering, and tracked exact integer wire labels through each SWAP. At the unique adjacent A it required the ordered wire labels to equal the original ordered operands. It then required the reverse SWAP sequence and final identity wire permutation. This checks the complete route, not just adjacency or final gate counts. Every nominal and mutant route passed those exact structural checks.

For logical operands i<j the source moves i toward j using edges `(i,i+1),...,(j-2,j-1)`, applies A at `(j-1,j)`, then reverses. For i>j it moves i left and applies A at `(j+1,j)` in the original operand order. The physical gate is a full SWAP, with no occupation-dependent phase. Each route therefore implements precisely the embedded original A by permutation conjugation. Onsite rotations are unchanged. Each route uses `2(|i-j|-1)+1` gates. This reasoning depends on the parent's supplied full-SWAP interaction; replacing it by iSWAP would not preserve it.

The artifact inspection obtained:

| Word | A | Z | SWAP | Total |
|---|---:|---:|---:|---:|
| Logical | 5040 | 1344 | 0 | 6384 |
| Routed | 5040 | 1344 | 18336 | 24720 |
| Mutant logical | 1440 | 384 | 0 | 1824 |
| Mutant routed | 1440 | 384 | 2496 | 4320 |

There are `3[T(2)+T(3)]=42` controlled-SU(2) leaves, so `G0=42*152=6384`. The reported `Gbar=7G0=44688` and tighter uniform `1344+7*5040=36624` are correctly priced. The actual route has A-distance histogram `{1:1008,2:1056,3:816,4:2160}`. Its required SWAP count is exactly

`2[1056+2*816+3*2160]=18336`.

For the mutant the histogram is `{1:576,2:480,3:384}`, giving `2[480+2*384]=2496` SWAPs. Thus the saved count is not merely copied from a theoretical recurrence. The control generators for the final parallel phase layer are separate: five generators in one extra slot. They are explicitly included in the physical ledger, not silently absorbed into 24720 circuit gates.

## 6. Matrix evaluation and actual numerical observations

By source inspection, `local_left` reshapes the five qubit bits plus a final input-column axis, transposes the ordered target sites to the front, applies the local matrix to all remaining bit/column combinations, and inverts that axis permutation. This is the stated MSB tensor action on every input column. Its cache omits site labels legitimately: the small local matrix depends on kind and phi, while operand placement is supplied separately. The source separately propagates full 32-by-32 logical and routed matrices, then applies J, rather than only propagating the chosen old state or a reservoir packet.

The independent inspector did not repeat that propagation. It loaded all eleven saved arrays, reconstructed the target, recomputed the saved full-isometry residuals, and checked the stored circuit-isometry relation `routed_isometry=routed_u@J`. The results match the author's report:

| Saved-matrix quantity | Recomputed floating value |
|---|---:|
| Complete 32-by-16 operator residual | 2.9508448902312835e-13 |
| Complete Frobenius residual | 8.930355179806793e-13 |
| Largest column error | 2.9506123471984577e-13 |
| All ten unselected input columns, operator residual | 2.950835855960473e-13 |
| Ancilla-one output norm | 1.203455149051588e-14 |
| Isometry defect | 5.90018483444466e-13 |
| Full saved routed-unitary defect | 5.904525925507249e-13 |

The complete saved logical and routed matrices are bitwise equal. The source reports a floating zero for their difference and the number commutator. This is consistent with exact wire-permutation routing and exact zeros imposed by the gate representation, but a returned floating zero is not an outward-rounded mathematical certificate. The independently inspected artifact establishes that these arrays and reported numbers agree; it does not turn them into an independently propagated or rigorously enclosed circuit result.

The author source's local Euler/commutator diagnostics cover 42 and 12 calls respectively, with maxima approximately 2.557e-16 and 2.191e-16. Those diagnostics are numerical checks, not a proof that branch selection will be robust for arbitrary inputs. The complete comparator is the stronger fixture check. No tolerance was inferred after seeing the result: the retained source has its 1e-9 discriminator threshold before launch. That is still a chosen test threshold, not a certified bound on roundoff from 24720 operations.

## 7. Determinant omission is a genuine discriminator

The inspector checked that `mutant_logical_word.json` equals exactly the concatenation of the three saved Givens segments from the nominal list. All determinant segments are omitted, no Givens gate is changed, and the mutant's separately saved routes preserve the same local gate actions.

On each selected block the exact nominal target is `G^*D`, while the mutant is `G^*`. Their difference has norm

`|1-det V|=|(288-120i)/169|=312/169=24/13`.

The same direct sum on three sectors gives the same operator norm, not three times it. Its Frobenius norm is `sqrt(3)*24/13`. The complement remains identity and the ancilla can return perfectly despite the wrong target phase. The saved mutant error is `1.8461538461538018`, differing from 24/13 by about 4.441e-14. Its very small complement residual and zero ancilla leakage therefore do not mask the failure in the actual full comparator.

This demonstrates why checking only unselected states and ancilla return would be insufficient. No scalar fitting was performed. The full mutant words, matrices, residuals and exact analytic prediction remain in the packet. It is an intentional negative control, not a failed launch or an argument that the general compiler fails.

## 8. Positive generators, free evolution and laboratory illustration

The independent local Hermitian-eigendecomposition routine in the author's source uses the claimed positive generators. Analytically,

`exp[-i(pi/4)(I-R)] = exp(-i pi/4) A`,
`exp[-i(|phi|I-phi Z)] = exp(-i|phi|) Z(phi)`,
`exp[-i(pi/2)(I-SWAP)] = SWAP`.

The last identity follows from SWAP eigenvalues ±1: the generator eigenvalues are 0 and pi. It does not omit a scalar reserve. Summing all 5040 forward-A and 1344 onsite contributions yields the reported `Phi=4732.64387840259` for the actual stored angles; the independently written artifact inspector recomputed that sum. The positive-gate array is not generated in the source simply by multiplying the logical array by this scalar; local eigendecompositions supply an additional numerical test. It still shares the same tensor-placement routine, and its positivity assertions use floating eigenvalue tolerances.

The saved positive-word residual, recomputed without new propagation, is `3.6647411565014315e-12`. Logical angle wrapping is harmless because Z(phi) has period 2pi, but it can change the positive reserve convention relative to an unwrapped ancestor. The source correctly computes Phi from the actual wrapped emitted word.

The illustration sets hbar=h=1, E0=1/5 and Delta=7/10, with `Q_*=6pi`, `g=24pi`, `sigma=24pi^2`. Both slot-length requirements give one. Using the actual route count gives `tau=24721`. Only after that count is known does it choose a rational r and integer k, then `lambda=2pi k-Delta tau`. This order is noncircular: the emitted circuit does not depend on that final lambda. The five simultaneous onsite number-phase generators occupy the last slot.

Every supplied gate preserves number and hence commutes with `F=E0 I+Delta N_tot`. Thus aggregating free evolution into `exp(-i tau F)` is mathematically legitimate; no old-H interval has been removed. The phase layer contributes `exp(-i lambda N_tot)`, and `(Delta tau+lambda)=2pi k` makes its combined number phase identity on the full five-qubit space. The remaining scalar is exactly the stated convention `gamma=exp[-i(E0 tau+Phi)]`. The final number generators' identity halves are already in lambda N and must not be counted again in Phi.

The stored endpoint array is computed from this factorized endpoint, rather than by integrating a pulse waveform. Its recomputed residual `5.44294855010996e-12` is numerical evidence for the scalar bookkeeping, not a test of a laboratory clock, integrated dynamics or calibrated perturbation model. The r/lambda inequalities are asserted numerically; this instance does not supply interval enclosures for pi, trigonometry, Delta or the cancellation in lambda.

There are 24725 control-generator uses in 24721 slots, with parallel actuation in the last slot. The nominal free-energy maximum 3.7, added incident cap `Delta+g/2`, and work upper bound `g(G+5)` are consistent with the supplied parent model. The ideal net prescribed-drive work is zero because F is conserved and controls vanish at the endpoints. This does not return a microscopic driver or establish its energy cost experimentally. The clock/actuator and coherent readiness remain external premises.

At L=1 this tests U_1(V) as a conserving circuit. It does not supply a useful small-error unchanged-reservoir implementation of V, does not prepare the required reference packet, and does not simulate the parent's perturbation or moment allowances. The previously stated initial-plus-final energy error condition under imperfect readiness and post-off endpoint timing condition remain unchanged.

## 9. Actual execution, bounded inspection and remaining obligations

The fixture retains one successful author launch. Its receipt is SHA256 `fb0fa13bec56ba4560fd7bd3a59671a0a0e4cc3f293cd3f4834f7b9d6895f145`, start 2026-10-16T15:14:50.930833Z, elapsed about 1.00345 seconds, exit zero, CPU limit 90 seconds, wall timeout 120 seconds, and one BLAS/OpenMP thread. Its actual argv does not include `-B`; it is preserved unchanged. Source/launcher at launch and both complete streams match their receipt hashes. Stdout parses to RESULT.json followed by the declared completion line; stderr is empty. No failed launch is present in this fixture packet. The earlier sparse-parent preexec failure remains part of the unchanged parent's evidence and is not rewritten as a failure or success of this run.

The present inspector ran once, with captured source and launcher, a 60-second wall timeout, exact argv and environment, full stdout/stderr and actual receipt under `runs/artifact_inspection/`. It completed in about 0.502 seconds, exit zero. It independently verified all route permutations, count relations, mutation segments and source bindings; it also recomputed residuals from saved arrays using Python 3.12.14 / NumPy 2.3.5, versus the author's Python 3.13.5 / NumPy 2.4.4. That version difference does not make it model-independent replication or independent circuit propagation. The full inspector stdout and empty stderr were read.

Remaining limits are concrete: a rigorously certified instance still needs outward-rounded or exact error bounds for the emitted word; this fixture does not implement the finite-grid certifying search; q>1 Givens elimination, larger control depth, greater-than-two logical-pair transport and general near-zero branch behavior are not exercised. No numerical replay of those cases was warranted by a discovered defect in the present fixture. The source theorem and its conditional permissions remain the basis for general claims.

Only this new review packet was written. No frozen parent, canonical source, Git state, PR, retained audit, cache, lock, prompt or axiom was changed; no other chat was messaged and no model override was used. Root owns acceptance and any subsequent publication. The present support is limited to the actual source, saved outputs and calculations described above.
