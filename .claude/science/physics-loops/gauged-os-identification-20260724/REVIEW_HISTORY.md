# Review history — reflected-Gram extension boundaries

## Round 0 — four Opus 4.8 max workers, graded against PLAN.md

Ground truth recorded in PLAN.md before any deliverable was read.

- **Gauged scout (CORRECT, three catches adopted).** Confirmed my
  prediction that the polar chain lifts verbatim, then found what I
  told it to hunt for: (i) the landed note's generalization clause
  does NOT repair its transfer-intertwiner theorem (T_2 is not a
  frame), with the correct statement being that the Gram at U pairs
  with the transfer at conj(U) and T_2[conj U] = T_2[U]^T; (ii)
  STATIC links are a necessary, previously unstated hypothesis, with
  an explicit RP failure at a time-dependent background; (iii) the
  proposed lift is NOT redundant with the landed SU(3)-Wilson
  two-seam note.
- **Gauged math (CORRECT).** Polar chain lifts consuming only
  h^dag = -h, m > 0, finite dimension. Flagged an honesty gap I
  adopted verbatim into Non-Claims: the gauged identification needs
  the coherent kernel in a MULTI-MODE Gaussian form where the landed
  input is ONE-MODE.
- **Full-field math (CORRECT; my prediction confirmed, then
  superseded).** PSD holds on the full barred+unbarred algebra with a
  constructive certificate — but the sharp negative is elsewhere and
  is representation-fatal: degree mixing via the equal-time contact
  term makes the Wick-determinant/exterior identification FALSE on
  the full algebra, with the quotient of dimension 4^|Lambda| being
  Hilbert-Schmidt operators on Fock rather than Fock.
- **Cl(3) investigation (CORRECT).** Separate surface; produced the
  repair landed as PR #5583.

## Round 0.5 — supervisor self-audit of the first runner draft

Two of my own gates were defective and I caught them before review:
A1r's rejector was VACUOUS (I built both matrix entries from the same
row's phase, forcing anti-Hermiticity by construction) — rebuilt so
that h[x,x+mu] carries eta(x) while h[x+mu,x] carries eta(x+mu), which
makes the x_mu-dependence genuinely break it; and A5 contained a
literal self-subtraction while B1 was coefficient bookkeeping rather
than the factorization. A5 now builds an SU(2)-fibered hop and reads
its dimension; B1 now computes -S_seam = sum Theta(u)u term by term in
an explicit anticommuting ring.

## Round 1 — lessons imported from the sibling PR landed mid-build

PR #5547 landed while this note was being written, after an
independent review-loop round (codex / GPT-5.6-Sol xhigh) returned
REJECT-as-submitted with a named salvage. Three of its findings are
defect PATTERNS, not one-offs, and I applied them here pre-emptively:

1. **Self-awarded "Status: PASS" removed** from the No-Go gate. The
   author does not award that status; the note now states the items
   were attempted and answered, and leaves the judgement to the audit
   lane.
2. **The N2 "pairwise hypothesis independence" claim retracted in
   place.** As in the sibling, the walls here are coupled (m > 0 and
   staticity both feed positivity; background class, staticity and
   kernel form are one coupled gauged wall). The note now states
   where each hypothesis enters and explicitly declines the
   independence claim, distinguishing gate independence (which the
   battery does establish) from hypothesis independence (which it
   does not).
3. **Misattributions to a landed note.** The sibling was caught
   asserting things about the corner-note that were not in it. Every
   statement here about the landed 3+1 note is now either a verbatim
   needle or explicitly marked as this note's own inference; in
   particular the claim that its unbarred restriction "was protecting
   against" the Part B obstruction is downgraded to the factual
   "avoids the obstruction, and no motive is attributed".

## Post-repair state

Runner 14/0 under the ordered label manifest (A1, A1r, A2, A3a, A3b,
A4, A5, B1, B2 + N1-N5). Battery 14 probes, each flipping exactly its
target, including the vacuous-rejector class, the seam sign, the
generator count, the fiber count, and a needle-meaning attack.

## Round 2 — cross-family adversarial lens (codex, sol xhigh)

Spec: `lens_spec.md`. Output: `lens_out.txt`. The spec explicitly
directs the referee at the two gates I consider weakest (A4's reading
convention and B2's arithmetic-only gate) and at the seriousness of
correcting a landed theorem.
(dispositions appended on return)

## Round 1b — battery methodology repaired (imported from the drain)

The review-loop worker on the sibling PR produced the single most
useful methodological finding of the session:

> "the runner did not gate its own headline constants. My independent
> mutation battery: A_3's 2*sqrt(u) -> 2u still PASSED 20/0; A_3's
> numerator 13 -> 14 still PASSED; C_d's (d-1) -> (d+1) still PASSED."

My batteries mutate GATE ASSERTIONS (does the gate fail when I break
the gate?). That is the weaker test. The reviewer mutated the CLAIMED
CONSTANTS in the constructions (does any gate fail when I break the
physics?) and found several headline constants were not constrained
at all. Applied here as a second battery pass over CONSTRUCTIONS:

- seam coefficient 1/2 -> 1/3 : CAUGHT (B1 pins it)
- transfer factor -2 -> -3    : CAUGHT
- hop normalization 1/2 -> 1/3: CAUGHT (2 gates)
- mass 7/10 -> 1/10          : NOT caught, and correctly so — A4's
  claim is "static => Hermitian, time-dependent => negative
  eigenvalue" for ANY m > 0, so the mass is an instance parameter,
  not a claimed constant. Recorded rather than "fixed", because
  forcing a gate to depend on it would be fabricating sensitivity.

## Round 1c — two further imports from the drain

- **The d = 1 anchor is audited_failed on this exact leg.**
  `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`
  failed audit 2026-07-21, with the recorded rationale calling the
  coherent-kernel identification "target-equivalent" and scoping the
  d = 1 claim to "the positivity of Gamma(diag(lambda_-)) as a
  CONSTRUCTED matrix". Consequence applied here: that note is removed
  from `upstream_dependencies` and de-linked to a backticked filename
  so it seeds no citation-graph edge. Nothing load-bears on it — the
  chain convention is rebuilt natively in gate A4, and the
  coherent-kernel form and selection prescription are named as
  supplied inputs this note inherits WITHOUT using, since Part A
  bounds the lift rather than performing it.
- **Raw reviewer transcripts do not belong in loop packs.** The
  sibling's 419 KB `lens_b11_out.txt` duplicated governance docs,
  embedded a machine-local path, tripped `git diff --check`, and
  actively contaminated the next reviewer by replaying pre-repair
  findings as if current. This pack's `lens_out.txt` is therefore NOT
  committed; its dispositions are summarized here instead.

## Round 2 — cross-family lens verdict: BLOCKER. Note NOT shipped.

The referee refuted one headline claim outright and disqualified the
other. Supervisor grading: the refutations are CORRECT and are
accepted in full.

1. **BLOCKER — (A4) "static links are necessary" is FALSE.** Reflection
   symmetry requires PAIRED slices, schematically h_t = h_{-1-t}, not
   time-independence. The referee ran an exact eight-slice test with
   four DISTINCT reflection-paired hops and got a Hermitian Gram with
   spectrum {0, 0, 0.424045..., 0.424045...} — PSD. My worker's probe
   showed only that arbitrary UNPAIRED even/odd data fails, which does
   not establish necessity of staticity. Worse, the referee found my
   own A4 gate reversed source and target relative to the landed
   reading and kept a dim x dim block where the landed Gram is
   2dim x 2dim, and that under my own reading the STATIC comparator is
   itself K_static = -(490050/1382849) I_2 — so the "contrast" the gate
   advertised does not exist. The landed multislice note I gestured at
   explicitly ALLOWS U_k(x,t) and claims PSD for every admissible
   open-time lattice: it contradicts my claim rather than supporting
   it. A4 is withdrawn; the correct statement is that
   reflection-paired links are what the construction needs, with
   staticity a sufficient special case.
2. **BLOCKER — (B2) unsupported and in the wrong arena.** I called the
   open finite temporal chain part of the landed conventions
   "verbatim"; the landed theorem uses the vacuum / infinite temporal
   lattice and says explicitly that the finite open-chain Gram differs
   by boundary images. And GNS dimension is not algebra dimension: for
   a pure vacuum the cyclic map A -> A Omega yields Fock dimension;
   Hilbert-Schmidt would require a faithful mixed state. The
   4^|Lambda| claim is withdrawn.
3. **MAJOR — the Verification section advertised gates that do not
   exist.** It claimed a dense-chain-inverse frame rejector and a
   degree-mixing contact-term gate. Neither is in the runner: those
   were the WORKERS' probes, described as if they were my gates. This
   is the most serious process failure of the round and is exactly the
   defect class the drain caught in the sibling PR.
4. **MAJOR — (A3) K-real overstated.** Z[conj h] = Z[h] does not
   require conj U = U; the stated equivalence is false.
5. **MAJOR — completion rhetoric** ("determines both boundaries
   exactly", "the gauged direction lifts") contradicts the note's own
   Non-Claim that the identification is not completed.
6. **MAJOR — frontmatter omitted the multislice source** that bears
   directly on (and contradicts) A4.
7. **MINOR — A1/A2/A5 scope**: A1 says "for every background" but
   gates one seeded d=2, L=4 U(1) instance, and the Verification text
   wrongly calls those entries "symbolic"; A2 gates R^2 and the
   unitarity core, not constructed R, E, Z, B; A5's 8 != 4 does not by
   itself establish the unrestricted transfer claim.

**SURVIVES (referee's own words):** "(A3)'s core correction survives...
this is a genuine incompleteness, not a strawman" — the landed clause
does limit substitution to the frames, T_2 appears separately in the
later intertwiner, and T_2[conj h] = T_2[h]^T follows from
conj(h) = -h^T by direct block multiplication. A1/A2's algebra
survives at instance scope. Audit/vocabulary hygiene survives; no
verdict is set or predicted; no new vocabulary.

## Disposition

The note is NOT submitted for landing. Nothing here is proposed to
main. The defensible salvage — and the only part that survived
adversarial review — is a NARROW note carrying:
  (a) A1/A2 at honest instance scope (gauged anti-Hermiticity with
      the x_mu rejector; the polar-chain core over a complex
      background, consuming only h^dag = -h, m > 0, finite dim), and
  (b) A3's correction to the landed generalization clause plus the
      exact identity T_2[conj U] = T_2[U]^T, with the K-real
      equivalence dropped.
A4, A5, B1 and B2 are withdrawn. Rebuilding (a)+(b) as a narrow note
with gates that match its prose is the named next step; it is not
attempted in this session, because shipping a hasty narrowing is how
false sentences land.
