# Preregistration

No Block 222 runner may be written or executed before this packet is
committed.

## Frozen physical alphabet

Fix one supplied normal `n` and its four Block-220 tangent ports.  The active
logical rays per bit are

```text
U
R_d                         d in D4
P_p, L_p                    p in D4
H_(p,q)                     p,q in D4
T_c                         c in D4
S, A
LOCK, BG
```

`p` is an exact parent dart, `q` is the current scan dart, `c` is the exact
return-child dart, `T` is a pointer-reversal trail site and `A` is the unique
collision anchor for one active probe.  `H` is time-multiplexed: it is an
ordinary forest head when it has no `A/T` child and the moving zipper front
when its exact `q` child is `A/T`.  That distinction is a visible bounded-star
predicate, not scheduler memory.

There are 35 transient rays per bit and two active Record rays per bit: 70
transient plus four Record rays, 74 named rays total, with a transported
rank-54 default projector `X_n`.  `U` remains the frozen Block-219 transient
pair.  `LOCK/BG` remain the frozen Block-218 code rays.  The other 34 roles per
complement parity must lie in the rank-37 post-code/post-`U` controller
sector.  No Record ray, hidden ID, epoch, coordinate, size, fixed dimer phase
or independent edge tensor factor may be introduced.

For the stabilizer `C4(n)`, the directional roles are eight copies of its
four-port regular representation: `R`, `P`, `L`, `T`, and the four orbits in
`H_(p,q)`.  `U` is the frozen ordinary scalar; `S` and `A` carry explicit
projective quarter-turn characters.  The primary must compute, rather than
embed as expected constants:

- the physical complement-parity multiplicities;
- the logical character and its residual;
- full-rank physical intertwiners in both complement parities;
- the unique canonical rotation carrying the base ordered tangent frame to
  each of the six supplied normal frames;
- all 24 proper-cubic context/port transports and complement exchange;
- orthogonality to the entire rank-52 Record code and frozen `U` pair;
- the literal `74+54=128` signature partition.

Any character deficit, nonunique frame transport, Gram singularity, relative
projective phase leak or covariance failure stops the route.

## Frozen one-probe pointer reversal

The first executable semantics are deliberately limited to an `H/R` contact.
They do not yet claim all reservation/reservation contacts.

1. Every claimed nonroot site carries its exact parent dart.  A waiting `P`
   therefore does not store a host stack or a child identity.
2. On an `H/R` contact the action is one guarded star.  It changes the actor
   `H` to `A`, binds the contacted `R` direction to the exact collision dart,
   and changes the actor's parent `P` to a zipper-front `H_(p,q)` whose `p`
   retains its own parent and whose `q` points exactly to `A`.  If the actor's
   parent is already a root, the direct-root case is decided atomically from
   the two labelled darts.
3. A zipper-front step changes the old front to `T_c` and the next parent `P`
   to a new zipper-front `H_(p,q)`.  It may move only along the exact stored
   parent dart.  Thus every old `P` child/return dart is retained explicitly.
4. At the actor root, the contact is own-root only if the root's exact
   collision-bound dart points to the same `A`.  A foreign actor root lacks
   that exact marked endpoint.  Endpoint equality never substitutes for dart
   equality on width two.
5. On own-root return, each `T_c` restores to `P_p`; `p` is the exact incoming
   return dart and `c` selects the next trail site.  The final `A` restores to
   `H_(p,q)` with `p` supplied by the incoming trail dart and `q` by the exact
   collision dart.  The root restores its launch dart from its unique child
   parent relation before reuse.
6. On foreign-root return, both probe endpoints enter the inherited guarded
   eroder.  No Record transition is enabled while `A` or a zipper-front/trail
   endpoint guards either root.

All transitions are state local.  Randomness is forbidden in safety rules.

## Stage A: carrier and exact falsifier gate

The primary must first reconstruct the Block-218 code, Block-219 `U` pair and
Block-220 rank-74 controller complement without importing the Block-220
representation helper.  It then builds the carrier above and independently
reproduces Block 221's 96/576 same-bit and 0/768 opposite-bit L4 Record census.

The pointer-reversal discriminator must be applied to every shortest false
trace and every proper-cubic, complement and width-two parallel-dart image.
Required: every foreign root contact is classified before the corresponding
commit, no own-root dart is misclassified, and every reversal restores exact
parent and collision ports.

## Stage B: complete L4 safety and concurrency gate

Only after Stage A passes may the recoded forest transition table be frozen.
Exhaust every mixed L4 word, unordered two-root placement, four launch darts,
and hostile reachable action order for same and opposite bits.  Then seed all
locally possible pairs of simultaneous anchors and zipper fronts.

Required:

- zero reachable `LOCK/BG` on every mixed start;
- exact rollback on every foreign-root or malformed contact;
- no lost parent, child, launch or collision dart;
- no state reused before its `A/T` relation is erased;
- no branch-closed fair nonterminal maximal end component;
- no scheduler-carried serialization or ownership;
- full single-root L4/L6 regression.

The first simultaneous-anchor alias, ABA reuse, lost dart, false Record or
fair nonterminal component ends this one-site route.  No retuning is allowed;
the next route is the preregistered explicit two-arm higher-block forest.

## Stage C: physical instrument and held gate

Only after Stage B survives may the frozen table be compiled into literal
pair/star partial isometries on the actual 74-ray plus rank-54 partition.
Every default block, projective phase, `K^dagger K` sum, QND Record block,
proper-cubic transport and complement map must be explicit.  The grammar and
bytes freeze before independent L8 execution.

## Decision classes

- `positive-port-aware-root-ancestry`: all three stages pass, still conditional
  on non-root reservation arbitration, event/rate/renewal and retained gates;
- `scoped-carrier-covariance-failure`;
- `scoped-root-probe-alias`;
- `scoped-simultaneous-anchor-failure`;
- `scoped-classical-safety-failure`;
- `scoped-physical-certificate-failure`;
- `inconclusive` only for a disclosed resource or timeout failure.

No negative decision is a broad no-go for higher blocks, stochastic liveness,
coherent arbitration, continuous-time laws, permanent Records or the axioms.
