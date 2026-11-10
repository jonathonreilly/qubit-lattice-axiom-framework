# SOURCE-EXPOSED comparison of the detector packet

This comparison occurred after the independently written proof and global-state
oracle were frozen and copied by the supervisor. It is explicitly source-exposed:
the primary RESULT.md, check.py, and ASSUMPTIONS.md were read in full. It is not a
second fresh-context derivation, an audit verdict, or computational execution.
The original INDEPENDENT.md, reference_check.py, and CHECKPOINT.md are unchanged.

## Reviewed identities

Primary directory:
`/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/detector_refinement/`.

| File | SHA-256 read and reviewed |
|---|---|
| RESULT.md | `b3a9bd60ae8aaa5390add43d282771541ebcc649af11fb89dd83bcf5a42f60f8` |
| check.py | `20d2fe3b1cd4e2120b67c32270a70cc81ee7ca15c5efafdab265030cbf754501` |
| ASSUMPTIONS.md | `ccd5ca22454914ef7df72d0df108ffa924ccd86c79310176c7a519a79b02d845` |

Frozen independent sources:

- INDEPENDENT.md: `e880927d8e7faca92c0943cda0d07c8a60b384e66b484f532258c189ce3cafef`.
- reference_check.py: `c739919d543d73312efca22c0159fcf27b59fd7d5c5b15c90603e20ee58e46c9`.
- Governing axiom memo: `301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`.

The workflow/workhorse identities and restricted-input history are recorded in
the frozen checkpoint. The primary's linked route checklist and original
PRIMARY.md were not included in this source-exposed assignment and were not
reviewed here. No claim about their contents is made.

## Mathematical and implementation comparison

No load-bearing disagreement was found between these three primary sources and
the specified isolated-patch process. The following checks are source inspection
and hand reasoning, rather than reported runtime outcomes.

**All-site confinement.** The emitter examines only header-derived candidate
sites, not every point of Z3. That optimization needs a proof; it is not itself
evidence that all omitted rates vanish. On the declared domain there is exactly
one record of each header content. Any successful local parse must see these
same four records, hence reconstruct the same origin/frame as the global
`candidate_sites` helper. The enabling branches in `local_query` require the
center's decoded coordinate to be in POOL or equal FINE/COARSE. Therefore every
site omitted from that candidate set has zero rate. All candidate sites see the
whole patch because its diameter is at most 15. The occupancy test in
`emit_case` removes already present sites. This closes the all-site confinement
obligation on every reachable prefix, including all proper spatial copies.

The restriction matters: with multiple distant header sets, global `geometry`
may reject a record configuration even though one local neighborhood admits a
unique header set. Thus `candidate_sites` is not a general simulator of the
declared total local kernel on arbitrary global states. The stated isolated
prepared-prefix domain excludes that situation. No enlargement to arbitrary
initial configurations should be inferred from the finite diagnostic.

**Frame reconstruction.** Each decoded axis has integer L1 norm one. Determinant
+1 then forces three distinct signed coordinate axes, so they are orthonormal
and the dot-product inverse used by `parse` is correct. Header marker contents
fix their ordering. The code handles translations and all proper rotations;
the `preferred-frame` option is explicitly a planted defect, not normal logic.

**Exact seed and phase recognition.** The parser verifies the selector range,
all sixteen weights, every column's sum of four, and all four grouping bits.
It reconstructs the canonical seed and requires every mandatory entry. The
extras must be exactly empty, one active unit-valued race record, or that same
race record plus the prescribed fine record. Extra visible records, missing
mandatory records, a second race winner, invalid winner contents, wrong fine
contents, and premature or terminal coarse records do not match a predecessor.
These branches implement R0, R1, and R2 exactly. In phase zero an unused slot
j>=N cannot fire; in phase one no other race slot can fire under fault='none'.
The three planted-defect branches visibly target the stated obligations.

**Center-excluded support.** `local_query` removes the center record before both
parsing and fallback counting. Its returned first value means an enabling
Dirac content before applying the occupied-site mask; it is not an instruction
to rewrite an old record. `emit_case` uses the mask for formation, while querying
every present site without that mask for its support mass. This is the required
separation. Removing a seed record destroys the seed; removing the latest new
record restores its enabling prefix; removing an earlier new record leaves a
hole. The local code therefore agrees with the global deletion-table oracle.
Fallback p=(1+2l)/(2(1+k)) equals the written formula, and the uniform component
gives every used content positive mass. A present zero is handled through
`content is not None`, so zero is not accidentally confused with no event.

**Dynamics and derived responses.** The event graph is acyclic because each
event adds one permanent record. Sorting by record count in
`terminal_distribution` is a valid topological ordering. The probability
update mass*rate/total is the finite competing-clock rule already hand-derived
under independent exponential clocks. The written equal rates, independence,
preparation and activation rule remain explicit conditional inputs. The source
does not turn them into consequences of the four axioms. The mean completion
time 1/N+2 and almost-sure termination agree with the three-stage event table.

**Actual tomography inputs.** The current `main` computes four responses by
calling `terminal_distribution` on each emitted q=1 tomography case and summing
terminal masses whose actual coarse content equals one. It passes those values
to `finite_diagonal_checks`. That function computes scalar=(r0+r1)/2,
z=(r0-r1)/2, x=r2-scalar, y=r3-scalar and determinant scalar^2-x^2-y^2-z^2.
These are the correct Hermitian Pauli-coordinate inversion and determinant.
The responses are not replaced there with a prescribed target vector. For the
legal program in the proof, the independently derived vector is (1,1,0,0),
so the coordinates are (1,-1,-1,0) and the determinant is -1. These are hand
expectations here, not a claim that the current process was executed by me.

The primary's diagonal-effect/pair enumeration is arithmetic on legal weight
columns, not 225 additional native-parser runs. Its scope string says exact
finite arithmetic. The all-program hand construction justifies the realization
of those menus; the diagnostic bank alone is not exhaustive native execution
over every such realization or every one of the 35^4 programs.

**Four-outcome scope clarification recommended.** At the reviewed RESULT.md
hash `b3a9bd60ae8aaa5390add43d282771541ebcc649af11fb89dd83bcf5a42f60f8`, the layout and
indices i=0,...,3 define a four-outcome program family, but the cross-program
refinement sentence in section 4 does not repeat the bound. It should say
"within the four-outcome program family" or "when the refinement fits at most
four outcomes." This is an explicitness repair, not a counterexample to the
bounded family proof. Every one of the 25 individual effects and every one of
the 225 summable ordered pairs fits in the stated architecture (at most three
nonzero outcomes for a pair and its remainder). Arbitrary quarter-grid POVMs
need not fit: four copies of P0/4 and four copies of P1/4 form an eight-outcome
diagonal POVM summing to I. The availability of its individual effects does not
prove this detector implements that entire eight-outcome fine measurement.
The same four-outcome restriction applies to refinement wording in the frozen
independent note; that original artifact has not been silently rewritten.

## Physical scope and the classical label

The scalar records vI are literal codewords in the supplied possibility algebra.
They are not asserted to be mutually orthogonal density matrices of a quantum
qubit. The source and ledger state that boundary clearly. The readout returns
an integer from a recorded scalar content, and absence remains distinct from
recorded zero. Extending this readout by a constant value on unused matrices is
a supplied decoder, not a derivation of quantum measurement capacity.

The coarse writer physically adds its own record while retaining the race and
fine records. Equality of two coarse response functions therefore does not
establish equality of their full records, apparatus states, histories or future
record-sensitive uses. The primary explicitly keeps that distinction. Its q=2
comparison preserves ordinary within-device event additivity and refutes only
the proposed cross-device nominal-label identification. Its generalized w
argument explicitly assumes w(0)=0 and positive w(k); under those premises the
spectator cross-multiplication is valid and leaves w(4) free. The original
independent derivation additionally showed how w(0)=0 follows if all padded
four-slot merges are required. These statements use different explicit starting
premises and do not conflict. Outcome responses alone do not determine clocks.

The four-selector corollary needs the following physical boundary, now explicit
in RESULT.md and ASSUMPTIONS.md and supplied here as a supplement to the frozen
independent note: this detector reads the record s itself. It therefore has
classical preparation-label side information. A genuine qubit in one of four
nonorthogonal states accompanied by an accessible classical label can also be
distinguished using that label. Nothing in the trace-dimension argument refutes
that scenario or quantum mechanics.

The precise conditional result is that the **entire declared label-accessible
input/output interface** cannot be compressed into density operators on C2 and
one fixed POVM with no further side information. For the legal fixed program
n_i(s)=4 delta_is, the exact response is delta_is. Positivity and unit trace
give rho_s<=I, so 1=tr(rho_s E_s)<=tr(E_s), and four outcomes require d>=4.
This representation bound is valid for arbitrary mixed states and arbitrary
POVM effects. It neither identifies the 43-site apparatus with a single qubit
nor establishes an intrinsic lattice obstruction. It shows that the physical
input boundary, allowable access to preparation information, and any restricted
quantum interface must be independently supplied or derived. Merely naming the
one-site possibility algebra M2(C) does not supply those operational restrictions.

## Provenance and remaining verification

One concrete provenance limitation remains in the emitter: it reads
`Path(__file__)` to obtain source_sha256 after generating the cases. If that file
is concurrently changed, the header can name different bytes from the source
loaded at process start. The self-hash alone is therefore not an execution
attestation. Execute an immutable/frozen source copy and retain its identity;
matching external pre/post source hashes also check the ordinary concurrent-edit
risk. This is separate from the mathematical parser agreement above. It is not
evidence that such a mismatch occurred in the supervisor's runs.

## Exposed comparison with actual supervisor-run evidence

After the source review, the supervisor supplied the actual output directory.
I read baseline.reference.stdout, baseline.stdout, primary_execution.json,
reference_execution.json, and all six controls' reference stdout/stderr. This
was evidence inspection, not a rerun; the original checker remained unchanged.

Evidence identities under the primary directory's `outputs/`:

| Artifact | SHA-256 |
|---|---|
| baseline.json | `933c10c852cdc27ff1868d717a541236601e27bbe3f4cc5b55d8b62b08bc7be0` |
| baseline.reference.stdout | `8fb1ca06afcb2512933a85267ce51497e7033965a0dad0fb25d95f60b8db8bd3` |
| baseline.stdout | `beef8ce70e9edd4fcf576ccc04faf0bd67c6f3095efe9bd49d4077cca34d6daf` |
| primary_execution.json | `25d2fd4cb1cdb14f0b3d8c34f17bd04c97f4b13303e7e4d3c14f060f9cdbedc5` |
| reference_execution.json | `928766e81bdf45a69b07c77fa8d33a8db0e1bf2d5c58b641394480f3df2dc5fa` |

The external execution receipt and checker output name the reviewed primary
hash `20d2fe3b...f754501` and original checker hash `c739919d...58e46c9` (full
hashes above). The baseline certificate's separately checked file hash matches
the digest reported by the oracle. The baseline reference run exited zero and
reported 178 cases, 3268 reachable states, 87880 support entries, minimum mass
1/18, complete declared coverage, and 89 cases for each q. These totals satisfy
the independent hand identity support_entries=27*nodes-2*cases, since each
case has 1+3N states and 25+81N present-record support entries.

The oracle reports q=1 direct/refined coarse probabilities 1/2 and 1/2, and
q=2 values 1/2 and 1/3. The primary's actual terminal output gives tomography
coarse responses (1,1,0,0); its reported inversion is (1,-1,-1,0), determinant
-1. These agree with the independently derived conditional mathematics and
the inspected response-to-tomography data path. Both outputs report the same
25-effect/225-pair finite arithmetic.

All three actual defect-option primary runs exited zero and emitted certificates;
their oracle rejections were semantic disagreements rather than producer crashes.
The six recorded reference failures all exited one with empty stderr:

| Control | Reported failure |
|---|---|
| reopen-race | case[0].nodes[1]: event mismatch |
| wrong-group | case[0].nodes[5]: event mismatch |
| preferred-frame | case[2].nodes[0]: event mismatch |
| tamper-missing-state | case[0]: omitted reachable states |
| tamper-support-zero | case[0].nodes[0]: support mass mismatch at (0,0,0) |
| tamper-source-pin | external source hash mismatch |

These outcomes demonstrate teeth against the named controls and agree with the
inspected code branches and integrity checks. I did not independently regenerate
the control artifacts, reexecute a numeric check, or compare every control JSON
byte against its parent; the execution receipts and failure streams are the
evidence inspected here. No finite set of mutations establishes checker
completeness, and the baseline remains diagnostic coverage rather than all
35^4 programs. Neither these receipts nor the source self-hash supplies a
cryptographic start-of-process attestation. The sources were observed unchanged
at the beginning and end of the reviewed source read.

No primary/governing source edit, commit, push, axiom change, or audit action was
performed by this worker. The source-exposed comparison and evidence inspection
do not retroactively change the original restricted-input derivation's status.
