# Physical endpoint/packet support-two lowering — Cycle 645 (2026-07-23)

Status: **candidate constructive compiler result**  
Authority: **none**  
Audit: **unset**  
Accepted: **false**  
Constitutional effect: **none**

## Result

Cycle 645 lowers every support-three reversible Boolean gate in the immutable
Cycle-640 candidate endpoint and predecessor/K16 interval packet to the
candidate physical primitive alphabet

```text
X, H, T, T-dagger, CNOT.
```

Every emitted primitive acts on at most two M2 factors.  No ancilla is added
by the lowering.  The runner checks the full coherent local matrix of every
gate instance, including every positive and negative control polarity, rather
than checking only classical truth words.  It also reruns Cycle 640's 256
endpoint rows, 4,096 packet cases, inverse/deletion tests, L3/L6/L7 interval
rows, and all24/all576 label covariance unchanged from the exact committed
shore.

This retires the support-three elementary-gate import for this interface.  It
does not yet provide a fixed nearest-neighbour coordinate placement for all
packet roles.  The endpoint remains a coherent candidate interface whose
actuality, admissibility, and law-domain ports are supplied.

## Exact lowering

A one-control toggle is CNOT, with `X` sandwiches for a zero-valued control.
A two-control toggle uses the exact 15-gate no-ancilla Toffoli identity.  A
controlled SWAP uses

```text
CNOT(right,left)
TOFFOLI(control,left;right)
CNOT(right,left).
```

Zero-valued controls are converted by a leading and trailing `X`.  For each
actual Cycle-640 gate, the runner constructs the ideal local permutation
matrix and the complete lowered quantum matrix.  The maximum residual, exact
primitive counts, inverse residual, and minimum single-primitive deletion
signal are recorded in the receipt.  Because every replacement is an exact
operator identity on the same named factors, substitution preserves the
whole endpoint/packet circuit on arbitrary coherent inputs, not just on the
enumerated basis controls.

The Toffoli identity is standard prior art and was already used by Cycle 523.
The new result is the exhaustive application and coherent-matrix audit on all
Cycle-640 endpoint and interval-packet gates, including negative controls and
Fredkin lowering.  No claim of inventing Clifford+T decomposition is made.

## Controls

- Immutable Cycle-640 source and receipt bytes are loaded from commit
  `c27f72ff8b1058d872695829c05e95da415813bc`; dirty working-tree bytes are not
  used as premises.
- All 256 endpoint truth inputs and all 4,096 packet inputs rerun.
- The original inverse, work-return, malformed-blank, duplicate-refusal,
  gate-deletion, contact-off, held L7, and all24/all576 controls rerun.
- Every actual gate block has exact forward and dagger matrices.
- Every individual primitive deletion in every block has nonzero signal.
- Separate templates cover CNOT/Toffoli control values and both Fredkin
  control values.

## Supplied structure

The result supplies rather than derives the X/H/T/T-dagger/CNOT matrices, the
standard Toffoli factorization, the Cycle-640 named role decomposition, blank
work factors, finite size family, and compile-time proper-cubic labels.  It
does not supply packet-role coordinates, blank-site genesis, a runtime frame
selector, occurrence, admissibility, a Record, or an infinite history.

## Dependency ledger

| Wall | Cycle-645 disposition |
|---|---|
| `C_ref` | Unchanged: blank roles, endpoint identity, and reference genesis remain supplied. |
| `C_num` | Exact unitary identities; no fitted number or new numerical law is introduced. |
| `C_wrap` | The support-three packet-gate import is retired. Packet counts are still not time. |
| `C_int` | Endpoint and predecessor/K16 Boolean interactions now use only support-one/two primitives; occurrence/admission are still supplied ports. |
| `C_local` | Advanced for the Cycle-640 interface; one fixed nearest-neighbour placement and congestion-free schedule remain open. |
| `C_source` | Unchanged: no physical energy, conserved source, gravity response, or resource genesis is derived. |

This result does not independently rebase the campaign lane coordinates.

## N1-N8 discipline

The exact no-ancilla Clifford+T route is marked `ATTEMPTED` and is positive.
Ancilla-assisted, measurement/reset, and native support-three variants remain
separate open routes and are not counted as failures.  Elementary support,
nearest-neighbour placement, and law-level occurrence are distinct walls.
The Cycle-640 support-three row and the Cycle-645 support-two row are matched
at the exact interface scope.  The rhetoric ledger separates element, site,
mode, block, and lattice claims.  Partial closures name the current runner and
the still-open placement/occurrence work.  The hostile steelman is the direct
Cycle-527-style state-carried physical router on actual packet roles.  Cycles
523, 527, and 640 are cited as mechanism echoes rather than independent
obstruction evidence.

The executable receipt contains the complete N1-N8 tables and exact
path/line citations.  All broad no-go, minimum-content, shared-obstruction,
and axiom-pressure claims are false.

## Scope firewall

- Exact support-two factorization is not nearest-neighbour placement.
- A supplied H/T/CNOT law is not a derived physical interaction law.
- Gate count is not elapsed time or physical energy.
- A packet rotor/count is not causal time by itself.
- A coherent candidate endpoint is not an occurrence or a Record.
- Pointer copying is not Record formation.
- all24/all576 proper-cubic covariance is not Lorentz covariance.
- No gravity/source/Born claim is made.

## Optimal next experiment

Give every Cycle-640 packet role one fixed integer coordinate in the installed
physical M2 microgrid.  Route every emitted one/two-M2 primitive through
adjacent tensor SWAP paths, return all work, color support conflicts, and rerun
L3/L6/L7 plus all24/all576.  Then compose the resulting local endpoint packet
with a seam-complete same-species A2 stream and the unchanged Cycle-610–612
acceptance harness.
