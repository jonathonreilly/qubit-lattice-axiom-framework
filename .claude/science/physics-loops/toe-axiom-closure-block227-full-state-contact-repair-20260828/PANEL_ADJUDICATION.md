# Block 227 Panel and Local-Rule Adjudication

## Portfolio vote

The post-result panel voted `4-1-0` for one full-state repair block before the
component-coalescence fallback.  Fixed bounded support keeps the carrier and
Kraus test finite; component coalescence risks an unbounded set-valued
incidence demand; serial scanning adds a token and termination burden.

The latest connection/time PR, #7774, supplies an exact common-clock
obstruction for one exterior-character action family.  It does not derive a
physical clock, action selection, gravity, or Record law, so it does not
shorten the present local Record route.

## Independent local-rule synthesis

Two independent passes agreed that the one-site-larger row alone is
insufficient for a contact far down a `T` wake.  They selected an oriented `L`
as the rootward visible abort certificate and the following smallest collision
joins:

```text
C0  H T T_F T -> P H T L      nearest incident contact
CQ  H L T_F T -> P H T L      clean return reaches an incident contact
CF  T T T_F T -> T T L T      seed a remote rootward certificate
M   T T L     -> T L T        move that certificate one site rootward
K1  H L T L   -> P H T L      one-T good/abort collision
K0  H L L T   -> P H T L      adjacent good/abort collision
B   H T L T   -> P H T L      inherited abort return step
A   H T L A   -> P P P S      atomic tagged arrival, reciprocal S-S
```

`T_F` is notation for an ordinary `T` with one exact incident foreign
participant in the complete input cylinder.  It is not a new onsite role.
The foreign roles and darts are consumed only by the indexed incident row;
remote foreign participants remain present.

An independent synthesis proposed omitting `K1` in favor of ordinary good
return followed by `K0`.  The five-physicist adversarial pass found the exact
boundary counterexample, so `K1` remains frozen:

```text
R H T T L A
  marker then B:  R H T L T A -> R P H T L A
  root turn:      R H L T L A
```

Without `K1`, ordinary good return reaches `R-P-H-L-L-A`; `K0` needs a
trailing `T`, so that branch is stuck.  Ordinary good return must therefore
bind one seamward lookahead and exclude `next=L`.  The same review found that
discovery must bind `next in {T,A}` and exclude `next=L`; otherwise
`P-H-T-L-T-A` cycles through discovery, marker motion, and abort return.
These are bounded visible guards, not priority or inferred absence.

The exact race diamonds motivating `CQ/K1/K0` are:

```text
R H T T_F T:  C0  joins  Q=(R H T -> R H L) then CQ
R H T T L A:  Q then K1 joins M then B at the seam boundary
R H T T L T:  Q then K1 joins M then B in the interior
R H T L T:    Q then K0 joins B
H L T^k L:    distant moves commute; k=1 uses K1; k=0 uses K0
```

The first anticipated Stage-B stress is two simultaneous remote contacts,
which may create two `L` certificates.  Adjacent and widely separated
witnesses are frozen as first tests.  They are test targets, not a
preregistered negative and not evidence against another finite local grammar.
