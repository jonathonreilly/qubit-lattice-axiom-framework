# Panel 6 — Lens 2 (Constructive): the record-conditioned generator, made precise

Sources: DECISION_MEMO_20260821 §3/§5; INTERPRETATION_DISCRIMINATORS note N1/N4/N6/N7; CLOSURE_AUDIT_TWO note
N1(a1)/N4/N6; RECORD_BORN_FREQUENCY_BOUNDARY + its runner. Owner addendum taken as given: the lattice may be infinite
and there may be no completed history, so the generator is the primitive and the complete history a derived limit
object. Fixtures: **8x4** (cover T=8, L_x=4, T_phys=4, physical torus 4x4) and **12x4** (T_phys=6, 6x4). Region dim
`2 L_x (T_phys−1)` = 24 / 40 at fixed codim `2 L_x` = 8. `dim H_c = L_x = 4` at both. Free shears: 8 at 8x4, 16 at 12x4.

## 0. What plays `W` and what plays "frequency" in the boundary note

That note is **not** about slice-Gram weights. **Frequency** = `f_1(w) = n_1(w)/N`, the Hamming count of a realized
binary word `w ∈ {0,1}^N` over its length (runner §1; at `N=4` the attainable set is `{0,1/4,1/2,3/4,1}`). **Weight** =
`binomial_weight(N,k,p)`, a **supplied IID model** with `p` handed in by hand (`p = 0.7`, runner §3) — no Gram, no
carrier, no shear, nothing lattice-valued. The landed negative is the **many-to-one** count map (class `k=2` holds 6 of
16 words at `N=4`): a frequency identifies neither a history nor a `p` — *counts alone do not derive Born weights*. The
note then names the open gate verbatim — "a probability model **or theorem** linking pre-record weights to long-run
record frequencies" — so the candidate generator is not blocked by it; it supplies the pre-record-weight side of that
gate, under one inherited constraint: a class map that is a pure count re-inherits the many-to-one prune verbatim.

## (a) The objects

**Region (landed, N1).** Carrier interior to the adjacent-admissible region at slice `c`: `s_t = 0`, `m > 0`, x-trivial
reflections at `c` and `c+1`, `σ = 0` on links `{c−1, c, c+1}`, everything else free in the cone. **Record trail:** the
landed record is `b166.free_shears`, the shears the region leaves free (8 at 8x4, 16 at 12x4); a trail of length `k`
assigns record *classes* to the first `k` free links in a declared order (natural: increasing `t`, then `x`). Two
declarations computation cannot make for us:

1. *Alphabet.* The landed record is defined by cell **time index**. Audit-two N1(a1) discloses the **wider record** —
   every unpinned modulus the form actually depends on: 16 symbols at 8x4, 12 at 12x4, **every one a mover**, `dim W = 0`
   at both sizes. The two readings give different trails.
2. *Class map.* `b = νσ/(1−σ²)` is continuous, so a **finite** partition is an input, not a derivation. Candidates: the
   `Z₂` sign classes (`σ` vs `−σ`; Block 164's `I1`, `P(flip) = J P J`, `J = diag(I,−I)`), or `σ ∈ {0, 1/5, 2/5, 3/5}`.

**Admissible next record** `A(t)`: a class value for the next free link keeping the carrier in the region cone
(`s_t = 0`, `m > 0`, x-triviality at `c`/`c+1`, the three pins, `|σ| < 1`). **Slice-Gram weight (N6's construction):**
`H_c = span(S)/ker P_c`, induced inner product `G = m·diag(D(c,·))`; state `ω(A) = tr(GA)/tr(G)`; induced distribution
`p(x) = D(c,x)/Σ_y D(c,y)`, measured `[1/4,1/4,1/4,1/4]` exact on the tested carrier. The only landed candidate is
therefore `W(class) := tr(G Π_class)/tr(G)`, with `Π_class` the compression of the class projector to `H_c`.

## (b) Well-definedness

`W(t) > 0` iff `Π_t` overlaps the support of `G`. Landed constraints: `G` has **rank `L_x` of `2 L_x`** (4/8 at both;
N4 T4a — "the `L_x`-fold kernel is the constraint signature"), so a class inside `ker P_c` gets `W = 0` and every
continuation gives `0/0` — **the ratio is ill-defined exactly on the kernel**; `m > 0` is required (at `m < 0`,
`B = m·diag(D)` is negative definite and the region fails); `D(c,x) > 0` entrywise is needed, measured on one carrier.
**The blocking fact at this scope:** `D(c,·)` is built from the cells of links `c−1` and `c`, **both pinned, and
contains no `b` at all** (N4); the region Gram carries **no shear symbol**, and `∂P/∂b ≡ 0` identically (N6). So `W` is
**independent of the trail** and `P(a|t)` is a fixed product measure — which is exactly why memo §5 calls half-support
scope "the built-in control — it collides trivially": at that scope no two distinct weight profiles exist.
**Hence the generator must be built at full-quotient scope**, where N6's correction bites: "the same free shears are
**LIVE** in the full quotient action `Q` on the same region at `s_t = 0`", measured at both sizes. That means naming a
new object `G_Q` — a Gram on the slice-`c` block built from `Q`, not from the half-support pairing `P`. Landed hazard:
`herm(Q) = m·quotient(H)` **contains no connection at all**, and `herm(Q)^{-1}` is entrywise the connection-off
covariance (audit-two N4), so a `herm(Q)`-based weight is connection-blind — the shim class at measure level. A
record-sensitive weight must draw on `Q`'s non-Hermitian part, which is not PSD. **That dichotomy — positive-but-blind
versus sensitive-but-not-PSD — is the first thing to test, and it is the construction's real risk.**

## (c) Consistency, stated as the Kolmogorov-extension conditions (no completed future)

The chain rule is **empty** for the ratio form: `W(t·a·b)/W(t)` telescopes whenever denominators are nonzero. The real
content is that the finite-window family extends to a process on a half-infinite record index without ever quantifying
over a finished history. Index set `S`: record slots ordered by time, **no terminal slot**; `Ω = A^S`, `A` the finite
class alphabet; cylinder sets are exactly finite trails; the generator defines the finite-window laws
`μ_F(t) = W(t)/W(∅)` directly. The identities to verify:

- **(K1) forward normalization / marginal consistency.** For every admissible trail `t` and next slot `s`:
  `Σ_{a ∈ A(t)} W(t·a) = W(t)`, i.e. `π_F μ_{F∪{s}} = μ_F`. Since `tr(GΠ)` is additive over orthogonal decompositions,
  K1 is a **theorem** iff the class map is a resolution of the identity inside `Π_t`, and **fails** if classes are
  cone-membership inequalities on `σ` — a cone is not a subspace and cone slices do not decompose a trace. Load-bearing.
- **(K2) permutation consistency.** `W(t·a·b) = W(t·b·a)` for `a`, `b` in distinct slots — needed because the record
  links carry **no intrinsic total order** (each time slice holds `L_x` links, so the x-order is an enumeration choice).
- **(K3) support.** `W(t) > 0` for every admissible finite trail (per (b), no trail may land in `ker P_c`), so every
  conditional in the tower is defined.

**What these buy, precisely.** With `A` finite and a fixed slot order, K1 + K3 alone give the process by
**Ionescu-Tulcea**: probability kernels `P(·|t)` extend to a unique measure on `Ω` with **no consistency requirement
beyond each conditional summing to one, no compactness argument, and no reference to a completed future** — built
forward one slot at a time, exactly as the generator is. K2 upgrades this to independence of the enumeration, the
genuine Kolmogorov condition; with `A` finite, `Ω` is compact and Kolmogorov's theorem applies with no regularity
side-conditions. **The complete history is then the derived object** — a `μ`-a.e. point of `Ω`, never an input.
Frequencies are derived too, as limits of window frequencies, needing a shift-invariance/ergodicity input which
**nothing here supplies**: the boundary note's prune ("convergence is a model-level statement") reappears at the far
end, and it is the census/bridge, not K1-K3, that must address it.
**Making a finite fixture speak about infinite time:** a numerical pass at window length ≤ 8/16 proves nothing about
arbitrary windows; the check that does is **symbolic** — verify K1 and K2 as **algebraic identities in the free
symbols** (`b`'s, `m`, `n_*`, `u_*`; exact rationals, no nsimplify), so they are window-length-independent and lift by
induction on trail length. Two guards from landed precedent: run at **both** `T_phys = 4` and 6 (the `T_phys = 4` wrap
accidents — `E` live at 8x4, dead at 12x4; the retracted T5b3 — show a single-size identity can be an artifact), and
confirm the identity's *form* is `T_phys`-stable. Only `T_phys`-stable identities are evidence for a limit object.

**One landed obstruction survives K1-K3.** Audit-two N4 measures no Hankel and no Toeplitz structure in the single-`O`
sub-blocks, 16 of 16 False — "the block is a **Gram** and **not a moment sequence**, so **no transfer operator can be
read off it even where it is PSD**", the region pin **costing time-translation invariance**. A consistent `P` is
therefore **not** a Markov law with a stationary kernel: fine for Tulcea (kernels may be slot-dependent), fatal for
reading the generator as a transfer operator.

## (c′) Where the antiperiodic wrap enters, and what replaces it on an open carrier

The wrap is load-bearing. `Q` is the **descent** of a cover object through the **antiperiodic** time identification
(cover 8x4 → physical 4x4), and audit-two N4 measures that descent **per differential** rather than assuming it:
`i(Hd + d†H)` descends for the committed `d₁` and Block 169's `d₂`, a generic third member **does not descend**. So `G`,
`D(c,·)` and every inertia triple here are quotient objects, several wrap-sensitive: `E` is live at `T_phys = 4` and
**dead at `T_phys ≥ 6`**, the linear margin term is a wrap accident, T5b3 was retracted for the same reason.
On an open or half-infinite carrier there is **no antiperiodic identification at all**: the cover is the
theory, the descent step disappears, and its role passes to a **boundary condition at the initial slice** plus a limit
along increasing `T` at fixed record trail. Consequences: everything certified only at `T_phys = 4` is void there, so
only 12x4-stable statements survive; and the region normal form `P|region = m·diag(D(c,·)) ⊕ 0` — what makes `W` a
weight at all — must be re-derived on an open boundary first. `E`-deadness at `T_phys ≥ 6` cuts in favour: at the sizes
that matter there is no wrap-borne content left to lose.

## (d) Record-permanence compatibility

Permanence — an appended entry never rewrites an earlier one — is exactly **projector nesting plus cone monotonicity**:
`Π_{t·a} Π_t = Π_{t·a}` (an exact matrix identity) and `A(t·a) ⊆ A(t)` (appending a record adds a pin; pinning only
removes freedom). Since the recording rule **is** the disconnection rule (N1: `H_q[c+1,c]` is a form in the shears of
link `c` alone, at every slice and size), conditioning on more record can only zero more transport. Falsifiable
consequence: **record-sensitivity of `W` is non-increasing in trail length and exactly zero at full length** — on a
finite carrier non-triviality lives strictly at partial trails, while on a half-infinite carrier the trail is never
complete and the sensitivity never has to reach zero. Test: `max_a |∂W(t·a)/∂b|` over free `b` per trail length, exact
rationals, checked monotone.

## (e) Transport sensitivity (the anti-shim standard)

Two dials, not to be conflated. **(1) In-region record dials** — the free shears `b`: test `∂W/∂b` exactly. Already
decided negatively at half-support scope (`∂P/∂b ≡ 0` identically); **open** at full-quotient scope, where the shears
are live in `Q`. **(2) Connection dials** `s_t`, `s_x` — moving these **leaves the region** (`s_t = 0` defines it), so
the honest test is the derivative at `s_t = 0` plus a connection-off recomputation (`s_t = s_x = 0`) compared as exact
rationals; identical ⇒ shim class, by lane precedent (the sign-quenched measure is positive *because* it is the
transport-deleted theory). Note also `m·κ₂ = 57/160` constant across four masses and three shears: `κ₂` is
**shear-blind by force** since `D(c,·)` has no `b`, so a margin-based or `herm(Q)`-based `W` fails the anti-shim
standard **by theorem**, without a run.

## (f) What the census and R1-R3 add

**The census** (memo §5) tests **injectivity** of `weight profile → record-frequency profile` at full-quotient scope,
exact rationals. K1-K3 make `P` a law and make the infinite-time process exist; they say nothing about frequencies. Zero
collisions ⇒ the frequency profile determines the weight profile ⇒ theorem *candidate*; one collision ⇒ axiom. Two
riders: half-support scope is the **control** and must collide trivially (per (b)) or the census is miswired; and
finite-fixture injectivity is not the limit statement — no sampling process is supplied, which is why memo §5 says
*candidate*. **R1-R3** is the only test evaluating the causal-time lane's **frequency** object and this lane's
**weight** object on the **same carrier**; elsewhere they are analogues compared by name. Not decidable from these
notes — the harness spec is staged, and its merge-acceptance criteria carry the anti-shim standard.

| item | decidable at 8x4 / 12x4 by finite exact-rational computation? |
|---|---|
| (a) objects | **No** — two declarations first (alphabet; class map). Everything below is finite once they are fixed. |
| (b) `W > 0` / ratio | **Yes** — support of `G` (rank 4 of 8, landed), `Π_t` overlap, `D(c,x) > 0` carrier census. Half-support triviality is **already landed** (`D(c,·)` carries no `b`) — no run needed. |
| (c) K1, K2, K3 | **Yes**, to be run **symbolically** (identity in the free symbols) at both `T_phys` so it lifts to unbounded windows. Markov/homogeneity likewise, by equality tests on `P(a\|t)` grouped by `(last class, slot)` — expect failure, per the no-transfer-operator result. |
| (c′) wrap, (d) permanence, (e) transport | Wrap: **yes** for the diagnostic (which quantities carry `T_phys = 4`), **no** for the open-carrier construction (new derivation, not a check). Permanence: **yes** — `Π_{t·a}Π_t = Π_{t·a}` plus monotone decay of `max_a \|∂W/∂b\|`. Transport: **yes at full-quotient scope**, already decided negatively at half-support scope. |
| (f) census / R1-R3 | Census **yes** as specified — delivers a candidate, not the limit theorem. R1-R3 **no** from these notes: spec staged. |
