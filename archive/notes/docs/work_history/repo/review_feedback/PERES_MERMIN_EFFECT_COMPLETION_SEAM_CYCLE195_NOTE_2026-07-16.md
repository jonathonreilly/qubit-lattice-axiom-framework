# Peres–Mermin Effect-Completion Seam — Cycle 195

**Date:** 2026-07-16

**Type:** exact finite-context countermodel, shared-marginal/no-disturbance
audit, positive-state obstruction, operational Born-import reduction, and
N1–N8 scoped-negative gate

**Authority:** none. This note is not an axiom proposal, primitive,
probability postulate, exact-law adoption, preparation rule, audit verdict,
retained theorem, or owner ruling. It changes no axiom, foundation, primitive,
registry, policy, audit, queue, or retained surface. It adds only this
authority-free note and its exact companion runner.

**Companion runner:**
`scripts/peres_mermin_effect_completion_seam_cycle195_2026_07_16.py`

## Result up front

The six Cycle-189 Peres–Mermin contexts do not by themselves force a quantum
trace law, even when all of the following hold:

- every context has an exact normalized nonnegative distribution;
- every supported triple has the correct signed parity;
- both occurrences of every shared observable have the same marginal; and
- all probabilities are simple exact halves.

The runner constructs one explicit countermodel with shared expectations

```text
<IX> =  1
<XZ> = -1
<ZZ> = -1
all six other Peres–Mermin expectations = 0.
```

Each of the six context tables contains two allowed triples of weight `1/2`.
Every context normalizes and every repeated observable has one context-
independent marginal.

No positive two-qubit density operator can reproduce the tables. `IX`
anticommutes with both `ZZ` and `XZ`. A positive state with `<IX>=1` must be
supported entirely in the `IX=+1` subspace, where both anticommuting
expectations vanish. The box instead demands both to equal `-1`.

The canonical completion

```text
rho_0 = (I + IX - XZ - ZZ)/4
```

has exact eigenvalues

```text
(1-sqrt(3))/4, (1-sqrt(3))/4,
(1+sqrt(3))/4, (1+sqrt(3))/4,
```

so it is Hermitian and trace one but not positive.

The conclusion is narrow and useful:

> **Finite context consistency is not effect completeness.**

Cycle 189's trace pairing can be reduced to a smaller operational law
contract, but it is not derived from the six-context support, parity, and
shared-marginal structure. The exact law must additionally supply or derive a
normalized measure on a complete physical effect/frame repertoire with the
required coarse-graining and composition consistency.

After that completion, trace form is mathematical: the Busch/CFMR
effect-Gleason theorem for a full effect algebra, or ordinary Gleason on the
full two-qubit projective-frame domain, gives a positive trace-one
representative.

The normalized numerical law remains exact-law content. **Born trace pairing
is reduced, not derived from support.**

No axiom conclusion follows.

## 1. Frozen inputs

The runner freezes:

| source | SHA-256 |
|---|---|
| Cycle-189 runner | `a06853a529723332c774112d5aad8e53d9a91ad486de70de201cfcb8b501fe34` |
| Cycle-189 note | `97c2e98f90cef08063a3589d31555fbe76a18cbbbd3b8fb677c3b03603c54ded` |
| Cycle-20 runner | `d5cc88a558b769d1291d4c8da629b2038078d41ca9ad0e0c91542e0a34440724` |
| Cycle-20 note | `dfb44a519055f5099ff03f571271ba2e416da705976899ac877e7121551047b4` |
| Cycle-194 runner | `10cbf5029bff31dd7977f1529774f550445c6df5ec98724c3610fdd1a9fb9b25` |
| Cycle-194 note | `55ff10103b6cbf2f884897af938d36c67fbcb8982a95c8c8492ec831bb8e1ca7` |

Cycle 189 supplies the exact positive quantum process used as the control.
Cycle 20 supplies the operational effect-completion theorem. Cycle 194 keeps
the repeated-history/frequency job separate from the one-shot
representation job.

## 2. The finite Peres–Mermin scenario

Use the same six signed contexts as Cycle 189:

```text
R1: ZI, IZ, ZZ     product +I
R2: IX, XI, XX     product +I
R3: ZX, XZ, YY     product +I
C1: ZI, IX, ZX     product +I
C2: IZ, XI, XZ     product +I
C3: ZZ, XX, YY     product -I.
```

For a context with observables `A,B,C` and product sign `s`, the allowed
outcomes satisfy

```text
c = s a b.
```

Given context-independent single-observable expectations `x_A,x_B,x_C`, the
most general parity-supported joint table is

```text
p(a,b,c=sab)
  = [1 + a x_A + b x_B + ab s x_C]/4.
```

The runner inserts

```text
x_IX = 1,
x_XZ = -1,
x_ZZ = -1,
all others = 0.
```

Every resulting table is one of the following exact shapes:

```text
(0, 1/2, 1/2, 0)
```

up to outcome ordering.

The runner checks:

- six normalized tables;
- no negative weight;
- exact signed parity;
- two positive outcomes per context;
- only weights `0` and `1/2`; and
- equality of both marginals for all nine shared observables.

This is an exact no-disturbance empirical model on the declared finite
context hypergraph.

## 3. Why it has no quantum state

Let

```text
A = IX,
B = ZZ.
```

They are Hermitian involutions and anticommute:

```text
AB + BA = 0.
```

If a positive density operator `rho` has

```text
Tr(rho A)=1,
```

then it has zero weight on the `A=-1` projector. Positivity therefore places
its support entirely in

```text
P_+ = (I+A)/2.
```

Anticommutation gives

```text
P_+ B P_+ = 0.
```

Hence every such positive state satisfies

```text
Tr(rho B)=0.
```

The finite box demands `Tr(rho B)=-1`. This is impossible. The identical
argument applies to `C=XZ`.

This support argument is stronger than the displayed zero-completion
matrix. Adding any of the six unmeasured two-qubit Pauli components cannot
repair the contradiction, because the contradiction uses only the demanded
expectations and positivity.

## 4. Positive controls

The runner rechecks both Cycle-189 preparations:

```text
|00><00|,
|++><++|.
```

Both are positive trace-one density operators. Their twelve context tables
are normalized and nonnegative. Cycle 189's pointer process remains a valid
positive quantum model.

The countermodel does not claim to reproduce Cycle 189's numerical tables.
It preserves the finite structural conditions that one might otherwise try
to use to derive those numbers:

- the same context family;
- the same parity products;
- the same shared-observable identity pattern;
- normalization;
- nonnegative probabilities; and
- context-independent shared marginals.

It then assigns different permitted weights that fail global quantum
positivity. That is the exact clause-delete control.

## 5. What completion adds

The finite Peres–Mermin hypergraph tests only six compatible frames. A
positive quantum representation couples those frames to effects and frames
that are not present in this finite set.

Two sufficient completion routes remain live.

### Full physical effect route

If the exact law supplies:

1. one normalized conditional numerical law on the complete physical effect
   algebra;
2. operational equivalence across all compatible contexts;
3. physical randomization and forgetting;
4. exclusive coarse-graining and complete-test normalization; and
5. a faithful identification with the full quantum effect interval,

then the Busch/CFMR effect-Gleason theorem gives

```text
p(E|s)=Tr(sigma_s E)
```

for one unique positive trace-one `sigma_s`.

The trace form is mathematical after completion. The existence and physical
completeness of the numerical law are not mathematical consequences of
record support.

### Full two-qubit projective-frame route

Because the generated composite is four-dimensional, a normalized
context-independent measure on every physical rank-one projective frame can
use ordinary Gleason. This route still needs:

- the full projective-frame domain;
- one value for a projector across every frame;
- normalization on every complete frame; and
- a theorem that the generated two-qubit composite and spectator
  consistency are physical.

The six Peres–Mermin frames are not the full domain.

## 6. Probability-lane compression

Cycles 20, 189, 194, and 195 now split the probability lane into exact jobs:

```text
finite process support and instruments
    -> normalized effect-complete operational law
    -> trace representation theorem
    -> repeated-history component means
    -> actual record frequencies.
```

The status is:

| job | present result | remaining work |
|---|---|---|
| finite instruments | Cycle 189 exact positive process | microscopic lattice realization |
| common instruction set | Cycle 191 H/CNOT compression | physical dispatch and gate semantics |
| numerical one-shot law | supplied by Cycle 189 | derive from selected exact law |
| trace form | Cycle 20 theorem after full effect completion | prove physical effect/frame completeness |
| finite-context insufficiency | Cycle 195 exact countermodel | blocks derivation from six contexts alone |
| frequencies | Cycle 194 component-mean theorem | derive the repeated process and component means |
| actual member | Cycle 27 classification | derive, realize, reconstruct, or supply history |

This is a smaller import than “assume Born's rule,” but it remains real:

> The eventual law must provide a normalized, effect-complete operational
> process or an equivalent full-frame structure.

Once it does, a separate trace-form postulate is unnecessary.

## 7. TOE consequence

The result helps the TOE program in two ways.

First, it prevents the finite Peres–Mermin success from being overread. Exact
contextual parity and shared record identity do not determine quantum
probabilities.

Second, it identifies a constructive target with a killer control. A proposed
microscopic process must not merely reproduce six tables. It must extend
consistently to a sufficiently complete physical tester algebra. The Cycle-195
box is a test case that any claimed quantum-effect reconstruction must reject.

This target can still emerge from a better substrate law. It need not become
axiom prose.

Still open:

- physical generation of the complete effect/tester repertoire;
- proof that operational equivalence is stable under every legal
  continuation;
- normalized numerical process content;
- the microscopic meaning of coherent superposition and phase;
- physical context-program execution;
- repeated-process component means;
- actual history;
- continuum locality and empirical closure.

## 8. Constitutional diagnosis

No axiom conclusion follows.

The countermodel argues against putting a six-context “Born” or “read twice”
sentence into Record. The missing content is not a special read event. It is
the scope and consistency of the selected exact process law across all
physical effects, mixtures, coarse-grainings, and continuations.

The present evidence favours this placement:

```text
exact-law theorem condition:
    normalized effect-complete operational process

mathematical consequence:
    positive trace representation

separate repeated-law theorem:
    component means -> frequencies.
```

If a future compact law derives the first line, no new probability axiom is
needed. If every viable microscopic architecture requires an independent
numerical process field, that field belongs in the exact law contract before
it is considered for constitutional status.

## No-go-discipline status

The narrow negative is:

> Normalization, signed Peres–Mermin parity, and context-independent shared
> marginals on the six declared contexts do not imply a positive two-qubit
> trace representation.

This is fixed Peres–Mermin scope. It is not a no-go against deriving the trace
law from a fuller effect or frame domain.

## N1 — Alternative-route enumeration

Live derivation routes include:

1. full-effect Busch/CFMR completion;
2. full four-dimensional projective-frame Gleason completion;
3. a direct microscopic CP/process law;
4. local-to-global process gluing;
5. operational tomography plus a proved positive-state cone;
6. a symmetry/information reconstruction of the quantum effect algebra; and
7. a compact amplitude law whose normalization and composition derive the
   same trace pairing.

The countermodel closes none of these.

## N2 — Wall-independence audit

The walls are:

1. finite context normalization and parity;
2. shared-observable marginal consistency;
3. positivity across incompatible effects;
4. full effect/frame completeness;
5. numerical process existence;
6. repeated-history component means; and
7. actual-history membership.

Cycle 195 preserves walls 1 and 2 while violating 3. Cycle 20 addresses 3 and
4 after wall 5 is supplied. Cycle 194 addresses 6. Cycle 27 addresses 7.

## N3 — Hidden-wall scan

The positive completion theorem needs:

- one normalized numerical conditional law;
- a complete legal tester domain;
- operational equivalence as a congruence;
- physical randomization;
- physical coarse-graining;
- faithful effect or frame identification;
- generated composite structure; and
- positivity/noncontextuality across the complete domain.

None follows from the six context supports alone.

## N4 — Residual matching

The Cycle-195 box and the Cycle-189 control share:

- the same six contexts;
- the same nine observable names;
- the same signed context products;
- four parity-compatible outcome slots per context;
- normalized nonnegative tables; and
- identical marginals for both occurrences of each observable within each
  model.

They differ in the numerical law's extendability to one positive
effect-complete representation. That is the residual under test.

## N5 — Rhetoric audit

The result does not say:

- no Born derivation exists;
- contextuality is nonquantum;
- the Cycle-189 process is invalid;
- full Gleason assumptions are physically automatic;
- the current lattice law selects quantum theory; or
- a new axiom is required.

“Completion seam” means one exact missing law-domain condition.

## N6 — Partial-closure paths

The import can shrink further if:

1. the physical dispatcher plus gate law generates a tomographically complete
   tester family;
2. local composition proves all rank-one projective frames;
3. coarse-graining and randomization are physically realized;
4. record-fibre equivalence is proved for the complete tester category; and
5. the selected local process proves positivity and normalization globally.

Each item is a constructive theorem target.

## N7 — Steelman

A critic can fairly say that the countermodel is a generalized operational
box, not a proposed microscopic universe. It does not share Cycle 189's exact
weights and may fail many physically obvious tests outside the six contexts.
That is precisely the point: those outside tests are the missing completion
content. The result establishes only that the present finite context family
does not make them redundant.

The critic can also choose a direct quantum process law and never invoke an
operational Gleason reconstruction. That route remains live; it simply places
the same numerical/positive structure directly in the law.

## N8 — Cross-cycle echo

- Cycle 20 compressed frame weights to a normalized effect-complete
  operational law plus a representation theorem.
- Cycle 181 showed that late lookup is not a physical instrument.
- Cycle 189 built a positive preterminal quantum process.
- Cycle 191 compressed its contexts to one H/CNOT interpreter.
- Cycle 194 isolated repeated component means as the frequency condition.
- Cycle 195 now proves that the six finite contexts do not themselves supply
  the effect-complete one-shot law.

The next probability construction is therefore not another finite context
table. It is:

```text
one microscopic process
    -> complete physical tester/effect domain
    -> positive normalized operational law
    -> trace representation
    -> repeated component means.
```

## Frozen result

Two cold standalone runs must report:

```text
CONTEXTS 6
SHARED_OBSERVABLES 9
SUPPORT_HISTOGRAM {2: 6}
BOX_EXPECTATIONS {'IX': 1, 'IZ': 0, 'XI': 0, 'XX': 0,
                  'XZ': -1, 'YY': 0, 'ZI': 0, 'ZX': 0, 'ZZ': -1}
ZERO_COMPLETION_EIGENVALUES {
    (1-sqrt(3))/4: 2,
    (1+sqrt(3))/4: 2
}
PASS 13 FAIL 0
RESULT CYCLE195_EFFECT_COMPLETION_SEAM_GREEN
```

The final note and runner hashes are recorded after the cold runs. No
authority-bearing file is touched.
