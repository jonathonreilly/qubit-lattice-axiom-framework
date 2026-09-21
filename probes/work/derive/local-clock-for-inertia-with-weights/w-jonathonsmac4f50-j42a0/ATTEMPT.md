# local-clock-for-inertia-with-weights, attempt 2 of 4 — yes at three records, no at four

Worker `w-jonathonsmac4f50-j42a0` (`claude-opus-5`), unit `J-derive-local-clock-for-inertia-with-weights:a2`.

**Provenance.** No prior attempt existed at claim time. Block 50 is taken as the unit states it and
is same-family campaign work; I re-derive none of it, but I **validate my machinery against its own
published figures** before using it.

## 1. What is claimed

Locality class, stated precisely: a rate may depend only on the **contents and occupancies of the
sites within distance one of the two sites of the event**, modulo the lattice symmetries that fix
the (ordered) event. Equivalently, the rate is a function of the canonical *pattern*: the target's
state, plus any other record within distance one of either site, expressed relative to the mover
and canonicalised under the order-8 stabiliser of the ordered pair.

> **THEOREM** (scope: the `3×3×3` window, `(p,q,r) = (3,1,2)`, the locality class above).
>
> **(i)** On the **three-record sector** the stationarity of `π` under inertial streaming is
> **FEASIBLE** with strictly positive local rates — at `c = 1` (332 distinct equations over 274
> patterns) and at the neutral scale `c₀ = 1/2` (334 equations). Every equation balances in exact
> rational arithmetic.
>
> **(ii)** It is **INFEASIBLE** on the three- and four-record sectors together. A **single**
> four-record configuration already obstructs it:
>
> ```
> (1,0,1):−x   (1,0,2):+z   (1,1,2):−x   (1,2,1):−x
> ```
>
> with an exact Farkas certificate: a rational `y` with `(Aᵀy)_j ≤ 0` at **all 275** patterns and
> `Σ_j (Aᵀy)_j = −36/5 < 0`.
>
> **So the unit's question decides YES at three records, and the YES does not generalize.** The
> local clock's three-record defect is *repairable*; the real obstruction lives one record higher.

Also exact, and independent of the rates: **record number and the multiset of contents are
conserved by every event** — a move relocates a record, an exchange swaps two contents — so the
total content vector ("momentum") is conserved event by event *for any choice of rates at all*.
Conservation is a property of the event set, not of the clock; the whole question is stationarity.

## 2. The steps

1. **CHECKED (`V1`) — the machinery is block 50's.** Reproduced, exactly: `70200` three-record
   configurations with a record at the origin; the local clock `1/π_x` defective in **3168** of
   them; largest defect **3**, at `(0,0,0):+y, (0,0,1):+z, (0,1,0):+y` — the block's own stated
   witness. All three match before anything new is computed.
2. **CHECKED (`V2`).** Number and content-multiset conservation over every event of every
   three-record configuration.
3. **CHECKED (`V3`).** The three-record LP at both scales: an LP proposes, and **exact rational
   arithmetic verifies** every equation, with all rates strictly positive. *(The particular rate
   interval depends on which LP vertex is returned; the run prints it and this document
   deliberately does not quote it.)*
4. **CHECKED (`V4`).** Infeasibility with the adjoined four-record configuration, and the Farkas
   certificate verified exactly. Scaling note: a strictly positive solution of a homogeneous system
   can be rescaled to `R ≥ 1`, so ruling out `R ≥ 1` rules out every strictly positive solution.

## 3. Where this stops

- **One window, one weight triple.** Everything is `3×3×3` at `(3,1,2)`. A larger window has more
  configurations *and* more patterns, and I have not checked whether the three-record feasibility
  survives on, say, `4×4×4` — where a pattern can be distinguished by data the `3×3×3` torus wraps
  together. **This is the most likely place my (i) is too generous.**
- **The infeasibility is for one particular locality class.** Widen the class — let the rate see
  distance two, say — and (ii) may dissolve. The certificate is a statement about *this* class, and
  the unit's part (c) explicitly asks to then enlarge the family with a momentum-conserving
  "nothing happens" or content-redraw event. **I did not do that enlargement**, so I have not shown
  that no local rule of any kind works; only that this one family fails at four records.
- **(b)'s closed form is not found.** The three-record solution space has dimension `274 − 216 = 58`
  at `c = 1`, so there are many solutions and I exhibit no canonical one. I looked for structure and
  did not find it; the LP vertex is arbitrary and changes between runs, which is why no rate
  interval is quoted above.
- **The four-record search is not exhaustive.** I sampled four-record configurations, found the
  system infeasible, and then shrank to a single witness. That witness is verified exactly, which
  is enough for (ii) — but I did not enumerate the four-record sector, so I cannot say how *many*
  four-record configurations obstruct, nor characterise them.

## 4. What would finish it

1. **The enlargement in (c)**: add a momentum-conserving null event (both records keep their
   contents) or a content re-draw on the momentum class, and re-run the same LP. That is the
   question the unit really wants decided and it is a small change to this script.
2. Characterise the obstructing four-record configurations — is the witness special, or is it one
   of a large family? A cheap sweep with the existing machinery.
3. Repeat (i) on a `4×4×4` window to check that three-record feasibility is not an artefact of the
   `3×3×3` wrap.
4. Another model family, particularly on the Farkas certificate: it is the one step where a sign
   error would silently turn a "no" into a "yes".

## 5. Running it

```
python3 probes/work/derive/local-clock-for-inertia-with-weights/w-jonathonsmac4f50-j42a0/check.py
```

`numpy`, `scipy` and the standard library; 10 checks. The LP **proposes** and exact `Fraction`
arithmetic **verifies**, as the unit requires — no claim rests on a floating-point solve. Runs in
about two minutes.
