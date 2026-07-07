# SU(3) Link Stars: Pair Data Are Locally Rigid (Full-Rank Jacobian), the Known Global Degeneracy Is the Transpose Sheet Carrying Only the Chiral Sign, and Real-Weight Stars Are Even Across It — the SU(3) Star Reduces to Pairwise Data in the Local-Plus-Sheet Sense and the Chiral Sign Is an Exhibited Multilinear Escape (Bounded Theorem)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite identities and certificates
plus one locality-graded rigidity statement; not a terminal no-go, not a
discharge of the theta admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta is already retired from live
Tier-A by retained derivation. This note banks a historical bounded support
calculation for the theta-side local link-star campaign; it does not reopen,
modify, or re-grade the theta retirement record or
`tier_a_admissions.json`.
**Primary runner:**
[`scripts/theta_su3_link_star_pairwise_reduction_chiral_sign_escape_2026_07_02.py`](../scripts/theta_su3_link_star_pairwise_reduction_chiral_sign_escape_2026_07_02.py)
**Runner cache:**
[`logs/runner-cache/theta_su3_link_star_pairwise_reduction_chiral_sign_escape_2026_07_02.txt`](../logs/runner-cache/theta_su3_link_star_pairwise_reduction_chiral_sign_escape_2026_07_02.txt)

## Question

Earlier theta-wall work left a context question about whether the SU(2)
pairwise-reduction pattern for real class weights survives for SU(3) link
stars:

```text
(i-b''-a) SU(3) star reduction: does the even invariant ring of SU(3)
          staple tuples reduce to pairwise composite data?
          (the SU(2) trace identity does not transfer)
```

Question answered here: what is the exact local-plus-transpose-sheet
reduction structure of SU(3) link stars — which identities transfer, which
are new, what carries the beyond-pairwise content in the witness, and what
the scoped real-weight star class cannot read?

## Answer

Everything below is evaluated with **no group integration anywhere**: the
Haar average over the shared link is replaced exactly by the invariant
projector — the joint null space of the Lie-algebra action on the channel
representation — validated in the runner by its defining property
`sigma(V) Pi = Pi` and by generator-convention checks against exponentiated
representations (which caught a conjugate-representation sign error during
development; the guard is now a permanent check).

1. **Three evenness identities (exact).** The SU(3) star of real class
   weights is invariant under simultaneous dagger, under simultaneous
   entrywise conjugation (**bar** — the SU(3) outer flip tested here), and
   hence under simultaneous transpose (their composition). All three
   verified to 1e-12 at the projector level (runner B3-B5).

2. **The polarized Cayley-Hamilton reduction transfers WITH a new term.**
   For 3 x 3 matrices,

   ```text
   tr(ABC) + tr(ACB) = det-polarization(A,B,C)
                     + tr(A)tr(BC) + tr(B)tr(AC) + tr(C)tr(AB)
                     - tr(A)tr(B)tr(C)          (exact, runner C1),
   ```

   so unlike SU(2) the symmetric triple word is pairwise-reducible only up
   to the **det-polarization** — the epsilon/baryonic channel that exists
   exactly at N = 3. The star genuinely sees this channel: the epsilon
   projector channel `I(F,F,Fb)` is nonzero (0.155 at the fixed staples)
   and removing it changes the star by 0.013 (runner B6-B7). The reduction
   therefore cannot proceed channel-by-channel; it proceeds through
   evenness and rigidity:

3. **Pair data are locally rigid.** At fixed generic (A, B), the 10 x 8
   real Jacobian of the pair-data map on the third staple has full rank 8
   (smallest singular value 0.204; runner D1): **no continuous
   pair-data-preserving deformation of a staple exists.** The pair data —
   separate classes plus both-orientation composite classes, 18 real
   numbers — locally pin the triple's diagonal orbit outright.

4. **The known global degeneracy is the transpose sheet, and it carries
   only the chiral sign.** The simultaneous-transpose triple preserves all
   18 pair data exactly (3e-16; runner D2) yet is a genuinely different
   diagonal orbit: the chiral datum `d = tr(ABC) - tr(ACB)` flips sign
   (|d| > 0.1; d is a diagonal-conjugation invariant; runner D3). The
   parity table (runner C2-C3):

   ```text
   transpose: d -> -d;   dagger: d -> -conj(d);   bar: d -> conj(d)
   ```

   — every real-linear component of `d` is odd under a flip the star is
   even under. And the star takes the **same value on both sheets**
   (runner D4).

**Consequence (the (i-b''-a) answer, graded).** Locally (full-rank
Jacobian) and across the one exhibited global sheet (transpose), the SU(3)
link star is a function of separate + pairwise composite classes: the
pairwise data supplied by the real-weight gluing calculus suffice to
evaluate it in that scope. The exhibited multilinear escape in this witness
is the chiral SIGN, which the scoped real-weight star observables drop by
the evenness identities. This gives an additional bounded convergence on
residual (ii'): the phase-type insertion class must be able to read the
chiral sign `sgn`-content that the real-weight observables tested here do
not read.

Grading is explicit: the evenness identities, the CH identity, the parity
table, the sheet exhibits, and the Jacobian certificate are exact; the
statement "no OTHER global sheet exists" is NOT claimed (an earlier seeded
search found none, but that is evidence, not proof — see Non-claims).

## Source surface (named authorities)

1. **Record axiom, current clauses used** (approved axiom node
   `minimal_axioms`,
   [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md); the memo
   is under active clarification on main; the two sentences consumed here are
   quoted from the current tip):

   > "Only records are readable. A readout value is determined by record
   > content alone."

   > "A law privileges no states. Its domain is a supplied condition, and at
   > every state where the condition holds it gives exactly one answer."

   Used as licensing discipline only; record occurrence is not claimed.

2. **Theta-wall chronology labels** (context only): the star functional,
   pair-gluing composites, and frame-dichotomy language are the surrounding
   campaign objects; every identity used here is earned inline by this
   runner. No sibling wall note is consumed as a premise.

3. **Retired theta registry text**
   ([`docs/audit/data/tier_a_admissions.json`](audit/data/tier_a_admissions.json),
   gauge side): the historical residual was "localized to the
   multi-plaquette / large-gauge-winding account"; link stars are that
   account's local structure and this note answers their SU(3) reduction
   question in the graded sense above. The retired registry entry is context,
   not a proof premise.

No external comparator, measured value, fitted number, Monte Carlo, or
continuum input enters anywhere.

## Theorem statements

**T1 (machinery; runner A1-A3).** The invariant projector for each channel
(R, S, T) in {1, F, Fb}^3 — the joint null space of the Lie-algebra action
on `D_R x D_S x conj(D_T)` — is a Hermitian idempotent satisfying
`sigma(V) Pi = Pi`, with the singlet-rank table exactly matching
representation theory: nine rank-1 channels (`(1,1,1)`, `(F,Fb,1)`,
`(Fb,F,1)`, `(F,1,F)`, `(Fb,1,Fb)`, `(1,F,F)`, `(1,Fb,Fb)`, and the two
epsilon channels `(F,F,Fb)`, `(Fb,Fb,F)`), all others rank 0. Star values
are exact traces against these projectors.

**T2 (evenness; runner B1-B5).** Real-weight SU(3) stars are real,
diagonal-conjugation invariant, and even under simultaneous dagger, bar,
and transpose. (Dagger and bar are one-line change-of-variables identities
— `V -> V^dag`, `V -> conj(V)` — for the projector-defined star class
checked here; transpose is their composition.)

**T3 (invariant algebra; runner C1-C3).** The polarized Cayley-Hamilton
identity with det-polarization term; transpose-invariance of the
det-polarization; transpose-oddness of the chiral datum; the full flip
parity table. Every real-linear component of `d` is flip-odd.

**T4 (rigidity and sheets; runner D1-D4).** Full-rank pair-data Jacobian
(local rigidity); the transpose sheet preserves all 18 pair data, is a
distinct diagonal orbit (d flips sign, |d| > 0.1), and the star is constant
across it.

## Corollary (wall state)

```text
W_theta_Q_context (current decomposition):
  (i-a)     defect closure on the abelianized multi-plaquette dual
            (context label; unchanged here);
  (i-b''-a) answered in the graded sense: SU(3) stars reduce to pairwise
            composite data locally (exact Jacobian certificate) and across
            the exhibited transpose sheet (exact evenness); the epsilon
            channel contributes but its beyond-pairwise part is projected
            out by evenness. Open sliver: a PROOF that no further global
            sheet exists (evidence only).
  (i-b''-b) sector-level closed-surface statement (context label;
            unchanged here);
  (ii')     the phase-type F u F insertion — this note adds a scoped arrow:
            the insertion must read the chiral sign content that the
            real-weight star observables tested here drop.

W_theta_bar_assembly: out of scope here.
```

## Identification checkpoint (what objects these are)

Staples, stars, and the chiral datum are configurational reconstruction
objects of the gluing calculus on a witness weight class; no claim is made
that records register them or that the fixed staples model the physical
sector. The headline is a theory of what SU(3) gluing observables determine
and what they provably cannot read — not a registration claim.

## Relation to the RP-half no-go (route independence)

The retained no-go row
[`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
forecloses only "the RP half-square identity alone cannot derive a
no-bare-theta-slot exclusion." No reflection positivity appears here; the
evenness results locate the theta-capable insertion class (constructive
direction), they forbid nothing about theta.

## What moves

| Prior state | After this note |
|---|---|
| (i-b''-a) — open: does the SU(3) even ring reduce to pairwise data? | answered in the graded local-plus-sheet sense: full-rank Jacobian rigidity + transpose sheet + evenness across it |
| SU(2) trace identity does not transfer | the transferring identity found: polarized CH3 WITH the det-polarization (epsilon) term; the epsilon channel is nonzero yet evenness projects out its beyond-pairwise part |
| bar (outer) flip unexamined | new exact evenness identity: real-weight stars are bar-even; with dagger this gives transpose-evenness |
| chiral datum status in this SU(3) witness | complete flip-parity table: every real-linear component odd; the SIGN is an exhibited multilinear escape, unreadable by the scoped real-weight star class |
| (ii') motivation count | additional scoped arrow; sharpened target: the insertion must read the chiral sign |

## What remains

```text
(i-a)      defect closure (unchanged);
(i-b''-a') the global-sheet sliver: prove no pair-data-preserving sheet
           beyond transpose exists (current status: seeded-search evidence);
(i-b''-b)  sector-level closed-surface statement (unchanged);
(ii')      the phase-type insertion reading the chiral sign.
```

## Non-claims

This note does not claim:

- Strong-CP closure, theta retirement, or any change to the Tier-A registry;
- a derivation of (i-a), (i-b''-b), or (ii');
- a PROOF that the transpose sheet is the only global degeneracy (the
  seeded fixed-(A,B) constraint search found no other branch — 12/12
  converged solutions returned the original staple — but that is bounded
  evidence; the local certificate is the exact part);
- that the fixed staples or the truncated weight model the physical sector;
- that records register any object here;
- exclusion of complex/phase-weighted gluing observables (they are exactly
  the open insertion class (ii'));
- any new axiom, import, primitive, or admission.

## No-Go Discipline Gate (for the negative boundary)

**Status:** PASS as bounded scoping inside positive constructions. The
negative content is exactly: (a) real-weight SU(3) stars cannot read any
real-linear component of the chiral datum (evenness + parity table, exact);
(b) no continuous pair-data-preserving staple deformation exists at the
tested generic point (exact rank certificate).

### N1 — Alternative-route enumeration

| Route to the chiral/beyond-pairwise data | Standing here |
|---|---|
| real-class-weight star observables | EXCLUDED for every real-linear component of d in this star class (evenness x parity table, exact) |
| epsilon-channel extraction from real stars | its beyond-pairwise part is evenness-projected out (B7 + T3); only the pairwise shadow survives |
| pair composites via gluing | SUFFICIENT for star evaluation locally + across the transpose sheet |
| phase-type (complex) insertion | OPEN — residual (ii'), sharpened: must read the chiral sign |
| quadratic-order even data (e.g. modulus-squared words) | NOT SETTLED here (beyond the multilinear scope; not claimed either way) |
| a further global sheet | NOT FOUND (bounded search); proof = named sliver (i-b''-a') |
| operational primitive registration | OWNER-GOVERNANCE ROUTE, not proposed (standing direction 2 -> 0) |

### N2 — Wall-independence audit

Nothing here binds the mass side or `W_theta_bar_assembly`. The negatives
are scoped: (a) to real class weights and real-linear components of d; (b)
to the tested generic point (locality is explicit). Complex-weight
observables and quadratic-order data are expressly out of scope.

### N3 — Hidden-wall scan

The projector construction is validated by its defining property (A2), the
generator conventions by exponentiation (A1 — the guard that caught a real
sign error in development), and the rank table against representation
theory with the design-time miscount corrected by the machine (A3,
documented in the runner docstring). The Jacobian certificate states its
scope (one generic point, deterministic seed); nothing is extrapolated from
it beyond local rigidity. The 18-number pair-data inventory is enumerated
explicitly in the runner (both orientations, all three pairs).

### N4 — Residual matching

The SU(3) (i-b''-a) remainder is answered in the graded sense, with the
global-sheet sliver named (i-b''-a'). The added scoped convergence on (ii')
matches and sharpens the campaign decomposition; the Tier-A registry's
multi-plaquette localization is respected throughout.

### N5 — Rhetoric audit

No "closes/exhausted/only-route" framing. The rigidity claim is explicitly
graded (exact locally; evidence globally); the reduction is stated
local-plus-sheet, never absolutely; live paths are named.

### N6 — Partial-closure path scan

Live paths: prove (i-b''-a') by invariant-theoretic fiber analysis (the
pair-data map's global fiber structure); extend to quadratic-order even
data; build the sector-level closed-surface statement from its own loop
data; construct the phase-type insertion (ii') and verify it reads d's
sign; (i-a); the assembly side.

### N7 — Steelman

A hostile reviewer can press: (1) "Local rigidity at one seeded point is
thin." The Jacobian certificate is exact at that point and generic by
Zariski-openness of the full-rank condition, but the note claims only what
is computed; the global statement is explicitly downgraded to evidence.
(2) "The projector method is overkill for five nonzero channels." It is
also exact, integration-free, and self-validating — and its guards caught
two real design errors (a sign, a rank miscount) that quadrature noise
would have masked. (3) "The chiral-sign story repeats the earlier SU(2)
star story." That earlier case reduced by a trace identity; here the
identity fails, the epsilon channel enters, and the reduction survives by a
different mechanism (rigidity + evenness) — the convergence is the point,
not repetition. All three absorbed into scope.

### N8 — Cross-cycle echo

Cumulative wall guards plus this note's additions: do not attempt to read
any real-linear component of the chiral datum from the scoped real-weight
SU(3) gluing observables (evenness + parity, exact); do not cite the
transpose sheet as the proven-unique global degeneracy (named sliver); and
check conjugate-representation generator signs against exponentiation
before trusting any projector construction. Future cycles citing this
chain must supply (i-a), (i-b''-a'), (i-b''-b), and (ii') explicitly.

## Verification

Run:

```bash
python3 scripts/theta_su3_link_star_pairwise_reduction_chiral_sign_escape_2026_07_02.py
```

Expected close:

```text
TOTAL: PASS=17 FAIL=0
```

Sections: A machinery ground (generator conventions vs exponentiation;
`sigma(V) Pi = Pi`; nine-channel rank table); B star and evenness (real;
diagonal-conjugation invariant; dagger/bar/transpose-even; epsilon channel
nonzero, conjugate-paired, and load-bearing); C invariant algebra
(polarized CH3 with det-polarization; transpose parities; full flip table);
D rigidity and sheets (full-rank Jacobian; 18 pair data preserved by
transpose; distinct sheets via d; star equal across sheets).
