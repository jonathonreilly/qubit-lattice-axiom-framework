# Preregistration Amendment 1 -- hostile-scheduler precheck

This amendment is committed before any Block 224 runner is written or
executed.  It changes the order of discriminators, not the frozen 47-class
contact semantics or the physical carrier.

The five-physicist implementation/refuter checkpoint found a candidate that
can decide the end-to-end value of route A before the expensive local-row
compiler.  The campaign therefore runs the following Stage 0 first.

## Frozen adversarial policy

Start with two symmetric finite seam components in the clean retry state.
Each retry support has exactly one supplied Bernoulli instrument with
independent branches

```text
go   with p,
wait with 1-p,
0 < p < 1.
```

The scheduler is asynchronous and chooses one bounded support at a time.  It
is adaptive to the finite past, cannot see a future coin result, and is
strongly fair almost surely: every continuously enabled or recurrent support
is delayed only finitely almost surely and every recurrent support is chosen
infinitely often.

The frozen nonanticipating policy in every round is:

1. choose seam 1's retry support until its first `go`;
2. leave seam 1's forward support enabled but delayed;
3. choose seam 2's retry support until its first `go`;
4. advance both seams into their frozen contact class;
5. schedule conflict and rollback fairly back to the same retry state;
6. repeat.

For every `0<p<1`, each waiting time is geometric and finite almost surely.
The policy therefore delays each enabled support only finitely almost surely,
uses no future outcome, and revisits every recurrent support infinitely often.
If the contact/rollback semantics are the frozen abort-both semantics, the
five-state round quotient

```text
BOTH_RETRY -> FIRST_GO -> BOTH_GO -> CONTACT -> ROLLBACK -> BOTH_RETRY
```

is closed and contains no positive terminal.  Self-loops at `BOTH_RETRY` and
`FIRST_GO` carry the respective `wait` outcomes.

The primary must derive rather than hard-code:

- normalization of the two retry Kraus weights on the retry projector;
- almost-sure finite delay and finite mean round length for each supplied
  rational probe `p` strictly between zero and one;
- zero probability of absorption under this policy;
- the deterministic `p=1` lockstep boundary without importing it into the
  open interval;
- an explicit stronger stochastic-support assumption under which a favorable
  finite graph can escape, so the result is not promoted to a broad backoff,
  stochastic-finality or axiom no-go.

Passing Stage 0 means reproducing this scoped adversarial liveness refuter.
It classifies route A as `scoped-two-arm-hostile-fair-scheduler-liveness-
failure` and triggers the preregistered route-B pivot.  It does not assert that
the local safety table or a conditional CP instrument is impossible.  Those
become lower-priority deferred work because they cannot establish the all-
declared-fair-scheduler finality target.

## Frozen Record restriction

`LOCK` and `BG` are the inherited Record sectors, not free phase labels.  They
remain QND and may not be used as root locks, success barriers, abort barriers,
contact latches or scratch memory.  Any candidate compiler that uses them
before a fully guarded positive Record is rejected as a Record write, not
credited as a dynamic construction.

The deterministic-coalescence pivot must first test whether commutative,
idempotent component merging can avoid the scheduler-controlled retry seam
without requiring those Record sectors or a hidden winner.
