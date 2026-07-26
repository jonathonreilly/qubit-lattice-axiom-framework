# Promotion Value Gate — Cycle 709

## Prior-art sweep

Ref refreshed; searched commit `70e8153ec2`. Searched on the statement:
`"reference energy|energy origin|energy zero|energy offset|additive
constant.{0,30}hamiltonian"`, `"resolvent.*(E|energy)|H ?- ?E|mass.*(offset|
shift|origin)"`, `"A/B|A over B|ratio A"`.

Classification:

| hit | class |
|---|---|
| `SINGLE_AXIOM_HILBERT_NOTE:220` — "removes the energy origin … no observable effect because it contributes only a global phase" | **prior art this note depends on**, quoted and re-earned by row R4 |
| `FLAVOR_HW1_STAGGERED_PROJECTION:82` — "Reference-energy tuning … ATTEMPTED" | adjacent: reference energy as a knob in the flavor lane, a different operator and target. Not duplicative, and evidence the knob is recognized elsewhere |
| `KINETIC_ISOTROPY_…`, `REALIZATION_ROW_SIGMA_…` — "quasi-energy offset" | different object (per-block quasi-energy), not the field operator's mass |

**No landed note identifies `A = mu - 6 - E`, states the bridge theorem as
`mu = 6`, or records the observable/unobservable tension.**

## V1 — the claim

Inside the supplied range-1 covariant family, A2 is exactly `A = mu - 6 - E = 0`;
so the missing bridge theorem is exactly "derive that the on-site term equals
the coordination number". As posed the route cannot close, because `A` is the
field's mass gap (`min spec(L) = A`, exact) while `mu` is unobservable in the
matter dynamics (landed, and re-earned exactly).

## V2 — new at `70e8153ec2`?

Yes, per the sweep above. The parent row has carried "supply a retained
derivation of `L^{-1} = G_0`" since 2026-04-14 without that identity being
reduced to a single diagonal entry.

## V3 — load-bearing?

On the `critical` root row, `deps: []`, 773 transitive descendants. It
**restates the gap** in a form someone can attack (`mu = 6`), and it names the
one escape condition that provably closes it (X1: a stochastic conservation law
on record formation forces `mu = 6` outright, row R6). It also explains the
five-mechanism `A/B` scoreboard in one sentence: `A/B` is an energy origin, and
none of the five fixes an energy origin.

## V4 — cost

No axiom, primitive, dimensionless import, or convention. The operator family
is carried from its landed classification, whose own text says those hypotheses
are supplied — tagged `[supplied]` in every ledger row that uses it and flagged
in the title. The `1/sqrt(A)` range is the standard continuum reading, cited
and not computed.

## V5 — thin?

Defences: exact rational operator algebra and exact torus spectra throughout;
a route no-go with four named escape conditions, one of which is proved to be
sufficient; and a reduction of a two-year-old operator-identity gap to one
arithmetic identity.

**Risks I would flag myself:** (1) the whole reduction lives inside a supplied
operator family — if a reviewer rejects that family, N1/N2/N5 do not apply, and
the title says so; (2) reading A2 on the resolvent `G(E)` generalizes the row's
own `G_0 = H^{-1}` — done to exhibit the freedom, and it reduces to the row's
statement at `E=0`; (3) the finite-volume corollary R8 is regulator-specific and
is labelled as such after the same objection was upheld on cycle 708;
(4) "unobservable" is scoped to the matter dynamics, since A2 itself is what
would promote `mu`.

## Step 11 — inference audit

**Clean.** Ledger complete, eight rows, every hypothesis tagged. Three defects
were caught by the author during this cycle and are recorded in the note: an
`isinstance(..., Fraction)` type test standing in for a reality check (R4); a
continuum "iff" asserted while testing only the four values that avoided its
counterexamples (R7 — the same domain-narrowing defect as cycle 707's
`hill[:1]`, now exhibited rather than hidden); and an equivalence tested on two
hand-picked vectors that satisfied it trivially (R8, replaced by exhaustive
enumeration). Running the audit also exposed one linter false positive (the
`zip(xs, xs[1:])` idiom), fixed on the methodology branch.

## Verdict

Proceed to cluster-cap evaluation. 8 PASS / 0 FAIL, cold-run at `344e2a600c`,
PIN MATCH `f2a6e6b7…`.
