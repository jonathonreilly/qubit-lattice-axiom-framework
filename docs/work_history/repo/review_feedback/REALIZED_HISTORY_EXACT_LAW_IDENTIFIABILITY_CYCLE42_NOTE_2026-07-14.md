# Realized History And Exact-Law Identifiability — Cycle 42

**Date:** 2026-07-14

**Type:** authority-free exact identifiability challenge, counterfactual-
protocol separation, positive complete-corpus route, and N1–N8 scoped audit

**Authority:** none. This note does not amend an axiom, enlarge a primitive,
identify the physical law, choose a history or boundary, issue an audit
verdict, or authorize a constitutional edit. It is a local exact probe only.

Companion runner:

```text
scripts/realized_history_exact_law_identifiability_cycle42_2026_07_14.py
```

## Question

The realized-state primitive licenses pointwise evaluation at a supplied
law-admissible realized state `s_*`. It does not supply `s_*`, a state-selection
rule, or a complete history. Could that pointwise reference form nevertheless
identify the exact law `L*` and thereby remove the final constitutional
obligation?

The strongest version of the route is:

> If a complete actual record history `H` is separately supplied or uniquely
> derived, define the physical law as the unique law compatible with `H`.

If sound, this would turn law selection into empirical reconstruction and
could make the final axiom update zero words. The test must include every
legal future intervention, not only the one path that happened.

## Result Up Front

A complete actual history can identify `L*` only after a **separating
reconstruction theorem** is proved. The registered pointwise reference form
alone does not supply the history or do that reconstruction job.

Three exact controls show the gap:

1. Two deterministic laws agree on every state visited by one complete actual
   path and differ only at an unvisited but legally preparable state. The path
   is compatible with both; one intervention separates them.
2. Every finite binary transcript has positive likelihood under every
   Bernoulli parameter strictly between zero and one. Exact observed counts do
   not equal an exact probability law without a sampling-class and limiting-
   frequency theorem.
3. Two causal laws have exactly the same observational record distribution
   `P(X=Y=0)=P(X=Y=1)=1/2` but disagree under `do(X=0)`: one makes `Y=0`, the
   other leaves `Y` fair. Even an exact observational distribution is weaker
   than the complete intervention law.

The positive route is real. Within a supplied finite-order Markov class, if a
certified corpus realizes every conditioning row and exact limiting
conditional frequencies exist, those rows uniquely reconstruct the kernel.
If the legal protocol family is separating and the complete actual history
contains certified recurrence of every protocol, process tomography can in
principle identify an operational equivalence class.

But the class, legal interventions, corpus decoder, recurrence/stationarity,
pointwise or typicality bridge, and uniqueness theorem are load-bearing. They
are fields or theorems of `L*`, boundary/history conditions, or explicit
conditional premises. They are not supplied by the realized-state primitive.

The earlier shorthand “realized-state primitive closes **actuality**, not
**law identity**” is rejected if read as saying that the primitive supplies an
actual state or a complete `H`. The precise statement is: the realized-state
primitive licenses a **pointwise state reference**, not a complete history or
law identity. A separately supplied `H` still does not invert itself into a
complete counterfactual map `L*` without a separating theorem. The universal
minimum remains one exact law identity or one exact record-faithful
equivalence class, unless a genuine separating reconstruction or uniqueness
theorem is proved. No second atom is added.

## 1. Foundation And Primitive Boundary

The live foundation says that records form, are permanent, are readable by
content, and constitute physical state. Admissibility supplies one rule slot
per model but expressly does not supply dynamics, weights, or a formation
process.

The realized-state primitive permits pointwise evaluation at a
law-admissible state `s_*` supplied from outside the primitive. Its own
boundary says that it supplies no state value, state-selection rule, measure,
typicality, or genericity claim. In particular it does not say:

```text
the actual history visits every physically preparable state;
the actual corpus performs every legal intervention;
the history is generic for one stationary or ergodic law;
the candidate law class is finite-dimensional or identifiable; or
the shortest compatible rule is physical.
```

Those cannot be silently added to the word “actual.”

### Pointwise State Versus Complete History

Three different information levels must remain typed separately:

1. **Pointwise `s_*` only.** The approved primitive licenses evaluation at a
   supplied law-admissible realized state. It supplies neither `s_*` nor any
   transition, neighboring time, counterfactual response, or complete history.
2. **Separately supplied complete `H`.** A record history
   `H=(s_0,s_1,...)` is additional contingent world data, or the output of a
   separate unique-history theorem. It gives the law's answers only along the
   visited path and performed protocols unless more coverage is proved.
3. **Separating or self-testing complete `H`.** A complete history may identify
   a law or operational equivalence class only if a theorem establishes the
   needed domain/protocol coverage, certified decoder, exact limits, and
   uniqueness against every admissible rival law.

The controls below test levels 2 and 3 as the strongest reconstruction route.
They do not reinterpret level 1 as if the primitive had already supplied `H`.

## 2. Deterministic Off-Path Separation

Take three record states `a,b,c`. Let the actual history be

```text
a -> b -> b -> b -> ... .
```

Define two deterministic one-answer laws:

```text
L_0(a)=b,  L_0(b)=b,  L_0(c)=a;
L_1(a)=b,  L_1(b)=b,  L_1(c)=c.
```

Both generate the complete displayed history from `a`. If a legal preparation
can place the system in `c`, their next readable records differ. The history
therefore fixes the law only on its visited path, not on the law's complete
domain.

Calling `c` illegal would remove the separator only by changing the legal
domain. That domain is itself part of the complete law. Calling the two
off-path answers physically equivalent requires a complete protocol-
equivalence proof. Neither move follows from the actual path.

This witness survives determinism and infinite observation time. Its issue is
counterfactual coverage, not statistical noise.

## 3. Finite Statistical Nonidentifiability

For a binary transcript with `k` ones in `n` trials, the Bernoulli likelihood
is

```text
p^k (1-p)^(n-k).
```

For every finite transcript and every `0<p<1`, this value is positive. The
exact same records are therefore compatible with `p=1/3`, `p=1/2`, `p=2/3`,
and a continuum of other exact laws. The empirical ratio `k/n` is a statistic,
not a theorem that the underlying parameter equals that rational number.

An infinite certified corpus can do more. Under a supplied IID Bernoulli law,
the strong law makes the limiting frequency equal `p` almost surely. Under a
stationary block law, the repository's component-mean theorem gives a
conditional expectation instead. Moving from either almost-sure statement to
the primitive-referenced actual history still requires pointwise scope,
typicality, or an every-history theorem.

Thus long data can identify a parameter **inside a supplied identifiable
class**. It does not derive the class, intervention semantics, or complete law
from pointwise actuality alone.

## 4. Observational Equality, Intervention Difference

Let `U` be a fair bit. Compare:

```text
Model A: X=U, Y=X;
Model B: X=U, Y=U.
```

Without intervention both models give exactly

```text
P(X=0,Y=0)=1/2,
P(X=1,Y=1)=1/2,
P(X!=Y)=0.
```

Under the legal intervention `do(X=0)`:

```text
Model A: Y=0 with probability 1;
Model B: Y remains fair.
```

The complete observational distribution—not merely one finite sample—does not
identify the intervention law. The distinction is precisely physical in this
framework because legal preparation, intervention, and later readable records
belong to the complete protocol contract.

An actual history can contain many experiments, but it contains only the
interventions actually performed. A separating universal corpus is an
additional structural property to prove, not a consequence of singular
actuality.

## 5. Exact Positive Reconstruction Route

For a binary first-order Markov law, write

```text
K = [[K_00,K_01],
     [K_10,K_11]].
```

If a certified recurrent corpus supplies exact limiting conditional
frequencies for both predecessor values, then

```text
K_ij = lim_N count(i->j)/count(i->0 or i->1)
```

uniquely determines all four entries. The companion checks this exact row-
reconstruction for a rational kernel. This is a genuine zero-edit route for a
candidate whose complete law class and every operational row are similarly
identifiable.

The route has explicit gates:

1. the exact candidate class and parameterization;
2. a complete legal protocol family that separates its members;
3. certified preparation and outcome decoders;
4. recurrence of every required conditioning event;
5. existence and scope of the limiting frequencies;
6. a proof that reconstructed representatives are equivalent under every
   future record protocol; and
7. a proof that no off-class law fits the same complete corpus.

If those are derived from the current foundation, `L*` becomes a theorem and
the axiom update is zero. If they are part of a proposed law, the
reconstruction validates that referent but does not independently select it.

## 6. Constitutional Classification

The exact roles remain:

```text
pointwise reference form s_*     approved primitive; licenses evaluation only;
supplied value of s_*             contingent input, not primitive content;
complete history H                additional contingent record-history datum,
                                  or output of a unique-history theorem;
finite observed corpus            projection of H;
legal protocol family             field of L* or derived physical category;
statistical/causal law class       field of L* or theorem target;
separating reconstruction          theorem;
typicality/pointwise upgrade        claim-specific condition;
complete extensional law identity  universal residue unless reconstructed.
```

No “history selects its law” sentence belongs in Record. It would combine an
actual datum with a counterfactual reconstruction theorem that has not been
proved. No enlargement of the realized-state primitive is justified either.

## 7. No-Go Discipline Gate

The scoped negative is only:

> The approved pointwise realized-state reference form, by itself, neither
> supplies a complete history nor extensionally identifies a complete law on
> unvisited states and unperformed legal protocols.

It is not a claim that empirical or mathematical law reconstruction is
impossible. In particular, the broad no-go “no complete history can identify a
law” is demoted and is not asserted here.

### N1 — Alternative routes

Every live route is marked rather than dismissed by reference to prior work:

| Route | Status | Exact exercise here | Result |
|---|---|---|---|
| Deterministic full-domain visitation | ATTEMPTED | Section 2 and runner B | A generic supplied `H` need not visit every legal state; the route remains positive if complete visitation is proved. |
| Infinite certified-frequency reconstruction | ATTEMPTED | Section 3 and the Cycle 21 component-mean result | It needs a supplied sampling class, existence/scope of limits, and a pointwise bridge. |
| Exact observational-distribution reconstruction | ATTEMPTED | Section 4 and runner D | An intervention-distinct pair survives exact observational equality. |
| Finite-class Markov/process tomography | ATTEMPTED | Section 5 and runner E | It succeeds conditionally with a supplied class, row coverage, exact limits, and uniqueness. |
| Universal self-testing complete-`H` corpus/full abstraction | ATTEMPTED | The hostile steelman in N7 and the cited adaptive-protocol construction | This is a live positive theorem target, not content of the realized-state primitive. |
| Direct unique derivation from the four axioms | OPEN | No complete uniqueness proof is supplied by this note | A successful proof would be a zero-edit route. |
| Unique global extension or compiler-invariant algorithmic inference | OPEN | No exact extension/compiler theorem is supplied by this note | Either could close the residue if its hypotheses and physical invariance were proved. |

No route is marked `RULED OUT BY PRIOR`; the note is authority-free and tests
the routes only to the resolution stated.

### N2 — Wall independence

Collapse the assumptions to three wall conditions:

- `W_D`: domain/state-visitation coverage;
- `W_S`: supplied sampling class plus exact limit and pointwise scope; and
- `W_P`: legal intervention/protocol coverage.

| Pair | Same object? | One implies the other? | Independent witness in this note? |
|---|---:|---:|---:|
| `W_D`, `W_S` | no | no | yes — the deterministic and Bernoulli controls vary them separately |
| `W_D`, `W_P` | no | no | yes — visiting states does not perform every intervention |
| `W_S`, `W_P` | no | no | yes — exact observational statistics leave the causal intervention pair distinct |

The collapsed wall set is `{W_D,W_S,W_P}`. Merely calling `H` complete closes
none of the three: temporal completeness is not domain, sampling, or protocol
completeness.

### N3 — Hidden-wall scan

| Trigger word or phrase | Classification | Required action |
|---|---|---|
| “registered” | approved premise boundary | State that the primitive licenses pointwise evaluation only and supplies neither `s_*` nor `H`. |
| “complete history” | explicit condition | Type `H` as separate contingent data or a theorem output; state which domain and protocols it covers. |
| “compatible” / “same law” | explicit condition | Name the legal domain and exact extensional or record-protocol equivalence relation. |
| “observed” | explicit condition | Supply a certified preparation/outcome decoder. |
| “all experiments” | explicit condition | Define the legal protocol family and prove coverage/separation. |
| “generic” | hidden condition promoted | Name a measure/typicality theorem or remove the word; no genericity is free. |
| “learned” | non-load-bearing shorthand | Replace it with reconstruction under a named theorem and resolution. |

Unresolved hidden conditions: **0**. Every trigger above is either removed or
promoted to an explicit condition.

### N4 — Residual matching

| Evidence path | Residual actually tested | Matches the scoped negative? | Use |
|---|---|---:|---|
| Section 2 / runner B (`:116-130`) | off-path deterministic identity versus complete-domain identity | yes | negative evidence at the domain-resolution seam |
| Section 3 / runner C (`:133-145`) | finite transcript versus exact statistical parameter | yes | negative evidence at finite statistical resolution |
| Section 4 / runner D (`:148-170`) | observational distribution versus complete intervention law | yes | negative evidence at protocol resolution |
| Section 5 / runner E (`:173-190`) | positive finite-class reconstruction versus primitive-alone nonidentifiability | no | **positive closure route; drop as negative evidence** |

Only the first three controls support the scoped negative, each at its named
resolution. The Markov result is retained solely as a steelman and partial
closure path.

### N5 — Rhetoric audit

| Resolution | Tested? | Licensed statement |
|---|---:|---|
| pointwise state `s_*` | yes | It contains no transition or counterfactual law. |
| one finite history/corpus | yes | It does not exactly identify unrestricted statistical or counterfactual structure. |
| infinite single deterministic path | yes | Off-path control survives unless full-domain coverage is proved. |
| exact observational distribution | yes | Intervention control survives unless protocol separation is proved. |
| separating complete-`H` corpus over all legal protocols | **NOT TESTED / OPEN** | It could identify a law or operational class under a reconstruction theorem. |
| all law space / universal histories | **NOT TESTED / OPEN** | No universal nonidentifiability result is licensed. |

The result is therefore primitive-alone, pointwise-reference-only
nonidentification. It is not underdetermination under every possible infinite
corpus, a ban on induction, or a theorem that Nature has stochastic hidden
data.

### N6 — Partial-closure paths

| Path | Status | What it closes |
|---|---|---|
| Approved realized-state primitive | approved premise | Pointwise evaluation at a supplied `s_*` only; it closes neither `H` nor law identity. |
| Deterministic full-domain `H` | open conditional | The domain seam, if every legal state is certified as visited. |
| Markov/process tomography | positive conditional | A supplied finite operational class with certified row/protocol coverage and exact limits. |
| Universal self-testing complete `H` | live theorem target | Potentially the full reconstruction route, if it separates all admissible rivals. |
| Direct unique derivation from the axioms | live zero-edit route | Exact `L*` without a new constitutional atom. |
| Supplied exact law or equivalence-class referent | constitutional placement route, not derivation | The identity residue if the theorem routes fail. |

These paths mean the present controls do not justify a new Record clause or an
enlargement of the primitive.

### N7 — Strongest steelman

**Hostile steelman:** one separately supplied, self-testing complete `H`
recurs through every finite legal protocol; certified preparation and outcome
decoders recover exact limiting statistics; a full-abstraction theorem shows
that those statistics uniquely determine one complete record-process law and
that every apparent off-path extension is record-protocol equivalent. The
strongest current support is the component-frequency route in
`CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md:49-106`
and the adaptive protocol/full-abstraction route in
`ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md:426-626`.
Both are authority-free theorem work, not imported authority.

**Outcome:** this steelman defeats the broad claim that no history can
identify a law. Accordingly, the **broad no-go is demoted**. What survives is
only the **pointwise-reference-only** result: the approved primitive itself
does not supply `H`, protocol separation, or a reconstruction theorem.

### N8 — Cross-cycle echo

| Prior wall | Retired? | Mechanism carried forward | Applicable residue here |
|---|---|---|---|
| Actuality semantics — `STOCHASTIC_RECORD_HISTORY_ACTUALITY_SEMANTICS_CYCLE27_NOTE_2026-07-14.md:20-46` | bare actuality clause retired | realized-state primitive plus separately typed contingent history | The primitive supplies no `H` and no law identity. |
| Certified frequency — `CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md:49-106` | partial | component-mean frequency theorem | Exact-law use still needs pointwise scope, class, and coverage. |
| Adaptive full abstraction — `ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md:426-626` | partial | finite-protocol transport and operational equivalence | A complete physical protocol category and separating corpus remain to be proved. |
| Cycle 42 controls | no | off-path and observational/intervention separators | Domain/protocol residual survives for primitive-alone identification. |

None of these prior mechanisms makes a complete `H` part of the realized-state
primitive. They instead specify what a separately supplied history would have
to satisfy.

**Gate result: PASS for the narrow pointwise-reference-only claim after the
broad universal nonidentifiability claim is demoted.**

## Bottom Line

The world supplies what happened. A physical law must also say what would
happen under every legal alternative preparation and intervention. Those are
the same object only after a separating reconstruction theorem.

No such theorem is presently available for the complete framework, so neither
the pointwise realized-state reference nor an unseparated supplied `H`
replaces the missing exact-law referent. A separating complete-`H` theorem
remains a live zero-edit route. The minimum constitutional count remains
unchanged at this resolution and no live edit is authorized.

## Verification

```bash
python3 scripts/realized_history_exact_law_identifiability_cycle42_2026_07_14.py
```

The runner checks the displayed finite exact controls and source boundaries.
It does not prove a universal statistical-identification theorem or select a
physical law.
