# Finite guarded two-state update involution

**Date:** 2026-10-24
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/finite_guarded_update_involution_2026_10_24.py`
**Cached output:** `logs/runner-cache/finite_guarded_update_involution_2026_10_24.txt`

## Supplied finite domain

Let X be a finite site set, with a finite nonempty alphabet at each site, and
let U be a finite indexed family of units. A unit u supplies sets S_u subset
F_u subset X, an involution T_u on configurations, and a Boolean predicate
C_u. T_u changes only S_u; its new values on S_u depend only on c restricted
to F_u. C_u also depends only on that restriction and satisfies
C_u(T_u c)=C_u(c). These are supplied hypotheses, not physical deductions.
A two-state crossing is a special case: interchange two distinct patterns on
F_u which agree outside S_u, and fix every other pattern. C_u can be the
indicator of these two patterns. The implementation below uses this binary
special case. The proof also covers any local involutions with the stated
candidacy invariance, including crossings with more than one local orbit.

Units are indexed, so equal geometries/patterns are allowed as distinct units;
self is excluded by index, never by geometric equality. The empty unit family
and empty site set are allowed (the empty product is the identity). The binary
implementation rejects a two-state unit with identical patterns, a repeated
read/write site, an out-of-domain site, S not contained in F, nonbinary or
wrong-length patterns, or a pattern difference outside S. It does not infer
physical significance from any supplied family.

Define a simple undirected conflict graph:

    u ~ w iff u != w and (S_u intersects F_w or S_w intersects F_u).
    N1(u) = neighbors of u.
    N2(u) = union_{w in N1(u)} N1(w), minus N1(u) and {u}.

Thus N2 means graph distance exactly two, not distance at most two. Define
A(c) to consist of u for which:

1. C_u(c) is true;
2. for every w in N1(u), C_w(c)=C_w(T_u c)=false;
3. for every w in N2(u), C_w(c)=false.

Let L(c) cross all members of A(c), using the active set computed from the
original configuration. The following proof establishes order independence
and L(L(c))=c; it does not assume either conclusion in defining the guards.

## Complete active-set proof

If u and v are distinct active units, v is a candidate and therefore is in
neither N1(u) nor N2(u). Consequently S_u and S_v are disjoint, neither write
set meets the other's read set, and N1(u) and N1(v) are disjoint. Locality then
gives T_u T_v=T_v T_u: each crossing sees unchanged input on its own read set,
and their output sites are disjoint. This reasoning also applies to identical
geometries: if the write set is nonempty, the duplicate indices are neighbors
and cannot both be active. Empty write involutions are identities.

**Persistence under one active crossing.** Suppose v is active in c and put
d=T_v c. First v remains active: its candidacy is invariant, its two neighbor
checks are exchanged because T_v^2=id, and each w in N2(v) has
F_w disjoint from S_v, so its candidacy is unchanged.

Now take u != v active in c. Its candidacy is unchanged since F_u is disjoint
from S_v. For w in N1(u), w != v and w cannot neighbor v (that would put v
at distance two from u). Thus F_w is disjoint from S_v. In the actual state,
C_w(d)=C_w(c)=false. In the hypothetical crossed state, commutation gives
C_w(T_u d)=C_w(T_v T_u c)=C_w(T_u c)=false. This explicitly checks both
states of u, not just the actual one.

For w in N2(u), w cannot equal v since v is a candidate and u's third guard
excludes it. If F_w is disjoint from S_v, C_w(d)=C_w(c)=false. Otherwise w
neighbors v, and v's two-state neighbor guard directly gives C_w(T_v c)=false.
Thus u's distance-two guard persists as well. Every old active unit therefore
survives one crossing of any old active unit.

**Forward inclusion.** Enumerate the finite set A(c) in any order and apply its
crossings once. Induction using persistence keeps every original active unit
active at every stage. Their pairwise commutation gives the same final d in
every order, namely L(c), and A(c) is contained in A(d).

**Converse (no new active units).** Take any z in A(d). All members of the
original set A(c) also lie in A(d). Apply those original crossings again, one
at a time. Persistence, now starting at d, keeps z active throughout (including
the case z itself is among them). Since these fixed crossings commute and are
involutions, their second product returns exactly c. Hence z belongs to A(c).
This proves A(L(c))=A(c). The second application of L crosses exactly the same
commuting involutions, so L^2(c)=c. Finiteness makes both inductions finite;
no infinite-configuration or local-finiteness argument is imported.

If every supplied T_u preserves occupation count, their composition L does
also. Two-state structure alone does not imply that extra hypothesis: the
single binary-site crossing 0 <-> 1 is an involution that changes the count.

## Finite implementation and discriminating fixtures

The primary builds N1 directly from finite read/write incidence and N2 from
two graph steps, with no spatial templates or periodic wrapping. Its canonical
integer-bit implementation is compared with a separately written tuple-state
reference evaluator on every configuration of the listed small families. This
is an author implementation cross-check, not independent scientific review.
The runner tests active-set equality and the involution separately. It checks
nonempty activity and disjoint simultaneous crossings, the empty family,
duplicate indexed units, and a count-preserving swap family.

Three deliberate weakenings have explicit small counterexamples, with bits
written in site order (site 0 first):

- Write-only graph: u flips x when y=0 and v flips y when x=0. At (0,0) the
  weakened graph has no edge, so both cross to (1,1); neither is then a
  candidate and the second step stays (1,1). The canonical graph includes
  their read dependency. This refutes this particular weakened rule.
- Omit N2: u flips x unconditionally, v flips y unconditionally, and w flips
  z when x=y=1. At (0,0,0), the weakened two-state neighbor checks allow u
  and v separately, but their joint crossing reaches (1,1,0), where w blocks
  both. The second step stays there. Canonical N2 excludes u and v together.
- Check neighbors only in the current state: u flips x unconditionally and
  w flips y when x=1. At (0,0), u crosses to (1,0); both candidates then block
  each other. The canonical hypothetical-state check blocks the first move.

These witnesses concern the specified finite families and weakenings; they
are not necessity theorems for every alternative guard. No one-sided-conflict
failure is asserted. The fixture with genuine enabled overlap uses u flipping
x when z=0, v flipping y when z=1, and w flipping z when x=y=1, together with
an independent fourth-site flip. In particular (0,0,0,0) has u and that fourth
unit active, so the suite is not an all-inactive test.

The `--inject-failure` option adds a deliberately false check and must return
nonzero; it does not modify any mathematical predicate in the default suite.
The source-pinned execution limit is 120 seconds. A cache is evidence only
for its actual frozen inputs, not a proof for all finite families.

## Historical provenance and remaining obligations

This finite extraction adapts original PR9831 commit
`e294c1dc745dad0c95b4c8688efc6f3f0be03613`, relative to
`f24d17d97d372df977476e4a69674577f31af575`. Historical source paths are
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C4f/NOTE.md`
(Step 3), `C4e/NOTE.md` under the same blocks directory (active-set converse),
and `C4f/scripts/c4f_core.py` (Layer). These historical paths are provenance,
not current proof dependencies. The proof above replaces the cross-reference
with a complete finite argument. The new runner does not import those files.

Historical `C4f/review_scripts/logs/rC_variants.log` records write-only conflict
failures 56/400, symmetric 0/400, and each of the two one-sided relations
0/400. The corresponding original review and scripts are preserved unchanged.
Those are historical finite observations, not newly reproduced results and
not proof that the symmetric relation is necessary. The new counterexamples
above neither replace nor relabel that history.

No spatial QCA construction, translation or axis covariance, metric radius,
quantum locality, glider/interface behavior, infinite configuration theorem,
or physical dynamics identification follows from this finite unit. Original
861-path recovery and deferred dispositions remain intact; broader C4f and
other campaign claims are not approved by this extraction. No novelty claim
is made. Independent proof and decisive-control review remain separate from
the bounded executable checks.
