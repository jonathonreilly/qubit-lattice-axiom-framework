# Repo search

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and
`pr/10141` in `/Users/jonreilly/Projects/Physics`, using bounded
`git grep -n -i -E ... -- '*.md' '*.tex' | head` calls. Terms:
`gap-seed-shape`, `gap-finishline`, `gap-crux-core-max`, `SEED-FP`,
`slab.to.cube`, and word-bounded `Theorem SH`. The first substring
SH query mostly hit “theorem shows”; its capped output establishes no
absence. The refined search found `origin/main:research/mass-gap/README.md`
and `research/mass-gap/library/gap-sh-astra.md`.

**Prior coverage found; do not repeat it.** `gap-sh-astra.md`, FINISH row
722, is already a Codex gpt-6-astra cross-provider check of SH, including
parts (i)–(iii), the exponent E, the r >= 24 line, and the explicit
threshold table. Sections 3–14 give exact arguments and two corrections:
require positive integers p,q; the ratio-2 two-stage row uses the
transformed seed and K'=22.2, while 1479 is a composed rate constant.
Section 24 compares the earlier row-707 check and corrects two of its
auxiliary assertions. This directly contradicts the task's premise that
row 707 was the only prior SH check. That covered subtask is stopped.

**Further prior coverage found.** Local `gap-crux-core-check-astra.md:29–39`
(row 893) already checks SPLIT and O1(b), giving exactly S<=5/17<3/10.
Local `gap-compress-check-astra.md:40–61` (row 849) already writes the
SH-to-cube composition, with a cutoff-independent k and margin 1/5999,
on FL's original ratio L>=25 domain. It also repairs the SEED-L limsup
substitution. These are direct prior checks, not merely nearby methods.
New proof work on those covered statements is stopped. What remains
below is the ratio-24 substitution and the domain/quantifier join.

The target-specific `prior/gap-shape-link-check-astra.md` is absent.
An exact-object search of `open-registry.md` found no match for these
filenames, SEED-FP, or slab-to-cube. This is a scoped search, not an
absence theorem. The statements in `gap-chain-ce-opus.md:373–375` and
`gap-handoff-opus.md:281,358` that FL is unchecked do not account for
row 849's written composition. The general November 8 prior digest was
read in full: it concerns thirteen earlier RG targets. Its nearest mass-gap
hit is a one-step plaquette correlation, not this shape recursion.

A separate all-ref search for slab-to-cube, SEED-FP and the finishline,
shape-link and crux-core filenames, excluding FINISH/ROWS tables, completed
with no hits. A method search for thermal-sum enlargement/recursion and
Schatten monotonicity returned only main's `gap-seed-shape.md:186`
(time multiplication plus E2 spatial enlargement) and
`gap-sh-astra.md:465` (the three-direction Schatten bound). The former
is the method already reused here; the latter belongs to D-shape(f),
not an additional slab-to-cube theorem. Main's README:17,24 explicitly
records row 722 and its corrections. Snapshot copies supply no second
derivation. No search result is treated as an absence theorem.

Ref pins, in the search order above:
`827f55721da6d44f68339805649e7ca1da598b2e`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`,
`c73ad7b177d94f89ff37b77386936e3d52b48b05`.

## Provenance and checkpoint

OpenAI Codex, gpt-6-astra, xhigh; research text for FINISH row 959,
2026-11-14. Checkout pinned at
`10bc2b314f7a0af47aea22029565f09f210bd01e`. Not an audit; grants no status.
No computer-assisted proof is used. Only this report is written.

Checkpoint: complete within the prior-work stop rule. SH, O1(b), and
FL's composition have prior cross-provider coverage. The endpoint and
domain join are recorded below. The actual uniform slab seed stays open.

## Prior statements reused

The source `gap-seed-shape.md` has SHA-256
`8b033032a09cb2acd7ee0958d9d6969b09b32b88bbc41609174865225c9c43f3`,
exactly the source hash recorded in row 722, section 25. Sections 1.4–1.5
and row 707's report were read. The source still lacks the two row-722
statement corrections. Verdicts below reuse that existing check; they
are not a second derivation of SH.

| Statement | Verdict and exact scope |
|---|---|
| SH domain and recursion | HOLDS AFTER CORRECTION: j is an integer >= 2, a and b_i are integers, and 1 <= p <= q are integers, p divides j, qa < min b_i. |
| SH (i)–(iii) | HOLDS on that domain, with the row-707 completion of the E s_k > 1 case; E = (j rmax/(rmin-1))^3. Row 722 sections 4–6 cover the full argument. The zero-seed case uses the extended gap +infinity rather than log(1/0). |
| r >= 24, (j,p,q)=(6,6,12), K=303/100, x_0=3/10 | HOLDS. Row 722 section 11 supplies a rational hand bound phi(x) <= 236 x^6 < K^5 x^6 for x>0, with equality of zero values at x=0; K x_0=909/1000<1. |
| Other threshold entries | HOLDS with their conditions: r=3,4,6 give 1/100,1/25,1/10; the two direct r=2 entries require strict s<1/K. The large-r family is covered by row 722 section 14. |
| r=2 two-stage table wording | HOLDS AFTER CORRECTION: use s'=S(a;(4a)^3), K'=22.2, x_0'=1/25. The constant 1479 bounds the composed rate; it is not the normalization K in SH(i) with the unchanged seed. Row 722 section 12 gives both the corrected statement and a counterexample to that literal reading. |

The ten row-707 corrections appear in the source's lead note. For this
chain only its scope correction, the E s_k > 1 completion, strict
endpoints, and the rounded coefficient in the r >= 24 line are relevant.
The rest concern free-energy variants, model examples, GUIDE numbers,
or strong-coupling inputs not consumed here. Row 722 section 24 also
corrects row 707's general nonnegative-power-series assertion and its
auxiliary 1.0003 bound; neither is used here.

**O1(b): HOLDS, already covered.** Local
`gap-crux-core-check-astra.md:29–39` (row 893) checks SPLIT and O1 against
`gap-crux-core-max.md:267–280`. These source passages were read. For the
same untwisted box, time, transfer operator and even vacuum,
S_ev <= 1/10 and Q_0 <= 1/20 give

    S <= (11/10)/(17/20)-1 = 5/17 < 3/10.

Thus s_0=5/17 is one fixed strict margin. The equality to 0.294 in the
brief is only a rounded approximation, not the exact value. Q_0 is the
maximum of all three flux probabilities; a single twist suffices only
with the cubic spatial symmetry stated at source line 280. This covered
subtask is stopped too; no seed estimate is inferred from its implication.

## FL steps (2)–(3): HOLDS; prior composition reused at ratio 24

Sources: `gap-finishline-opus.md:127–134` and the existing row-849
composition, `gap-compress-check-astra.md:40–61`. Fix one bare Wilson coupling
and integer lattice sizes a >= 3, b >= 24a. Suppose
S(a;b^3) <= s_0 < 3/10. Set c=303/100, r=b/a,

    v_h = (c s_0)^(6^h)/c,       E_r = (6r/(r-1))^3.

The letter c avoids confusion with the cutoff K. The sequence v_h is
non-increasing and tends to zero; the zero-seed case has v_h=0 throughout.
The positive-time, corrected SH statement applies: 12a < b, p=6 divides
j=6, and c s_0 < 909/1000 < 1.

For any k >= 0 and integer N with 2N >= 6^k b, let h be the largest
nonnegative integer with 6^h b <= 2N. Then h >= k. SH(i), followed by
the thermal-sum assertion of SH(ii), gives

    S(6^h a;(6^h b)^3) <= v_h,
    1+S(6^h a;(2N)^3) <= (1+v_h)^E_r <= (1+v_k)^E_r.

These are precisely FL step (2). Its use of the maximal h is necessary:
interpolating an arbitrarily distant cube directly from the fixed k
would not have a uniformly bounded enlargement exponent.

For step (3), N >= 6^h b/2 >= 12*6^h a. Every excited eigenvalue ratio
lies in [0,1), so its N-th power is at most its (6^h a)-th power.
Summing the nonnegative terms proves

    S(N;(2N)^3) <= (1+v_k)^E_r-1.                 (1)

These are the existing composition's steps, with r>=24 in place of L>=25.
All its inequalities keep their domains at this endpoint. This is reuse
of that checked implication, not a new independent check of its core.
It does not infer a thermal-sum bound from a gap alone.
Lemma Z' supplies only FL step (1), before this argument starts. Neither
Z' nor SEED-L is an input when the slab seed is supplied directly.

**A uniform k and strict margin, by hand.** Since r >= 24,

    E_r <= (144/23)^3 < (19/3)^3 < 256,

where 432<437 and 19^3=6859<6912=256*27. Choose k with
256 v_k <= 1/6000; it exists since v_k tends to zero. This depends
only on s_0, not r, a, b or the coupling. The same final series bound
as row 849 gives

    S(N;(2N)^3) <= exp(1/6000)-1
                  < 1/5999 < 1/5041.             (2)

The middle strict inequality follows from n!>=1, strict for n>=2.
Take the common SEED-FP margin s_*=1/5999. No run or numerical enclosure
is used. The fixed-datum implication holds at every integer N with
2N >= 6^k b.

The printed FL bound E<=244.2 is correct on its original rho>=25 domain.
It must not be imported at r=24: (144/23)^3>244.2. Use E_r itself or
the uniform upper bound 256 above. No step requires rho to be an integer
for this direct-seed version; integer a,b suffice.

## Box and first-passage domain

**SH admissibility: HOLDS for integer a>=3.** On (a;(24a)^3), all four
periods are integers >=3 and 12a<24a. SH and its rectangular transfer
input, `gap-seed-check.md:18–41`, require no evenness of a. The latter
states its trace identities for every integer time >=2 and every spatial
side >=3; its proof and its explicit domain were read. Taking a>=3
also admits a as a spatial side when axes are exchanged in SH.

**The a>=1 wording: HOLDS AFTER CORRECTION for direct SH use.**
`gap-direction-max.md:179–184` (row 931, in the requested row range)
says “integer a >= 1” and then calls it the SH seed shape. Replace
that domain by integer a>=3 when invoking SH as stated. The spectral
definition at time 1 does not supply the missing crossed-box hypothesis.
For fixed positive physical time A and a=A/a_K, a>=3 is automatic after
increasing K_0. This is a domain repair, not a counterexample to a seed.

**Account torus qualification.**
CA-I `1.1:def-lattice`, lines 403–445, defines a four-dimensional cubic
torus of physical side 2L^m, odd L, integer m>=1, spacing a_K=L^(-K),
and 2L^(m+K) sites on every axis. The outline at 6913 states the same
even-site frame; 21518–21534 supplies its torus floor ell_*(g).
A rectangular period vector (a,24a,24a,24a) is not that cubic torus,
even if all four periods are even. Making a even alone does not cure
that difference. Nor is multiplication by 24 or 6 generally a change
from 2L^m to another 2L^m with odd L.

This does **not** obstruct (1): it uses the bare Wilson theory on
integer rectangular tori, whose transfer construction is the lane input.
The account's GL8 (outline 2313–2336) itself starts with a cubic torus;
it is not silently used as a rectangular RG construction. No estimate
for an account effective density on a cube is thereby an estimate for
the seed slab. Supplying the latter is a hypothesis of this composition.

**Uniform SEED-FP conclusion: HOLDS with the following quantifiers.**
Fix the account's reference g and spacing a_K=L^(-K). For every
K>=K_0 and every beta in W_K(g), require the directly supplied slab
bound for the same bare Wilson measure, with one common s_0<3/10,
integer a>=3, integer b>=24a, and a common finite upper bound B on
the physical spatial side b a_K. Fixed physical time A and side B
with b/a>=24 are the intended stronger version. A bound only at one
bare coupling, or with physical seed sizes tending to infinity,
does not supply these hypotheses.

Choose once an integer m>=1 with

    ell=2L^m >= max(6^k B, ell_*(g)).

Such m exists and is independent of K,beta. Then N=ell/(2a_K)=L^(m+K)
is an integer, N>=3 after increasing K_0 if needed, and 2N>=6^k b.
Equation (2) proves the exact SEED-FP statement with this one ell and
s_*=1/5999, uniformly over all the required first-passage data. This
choice also lands on the account's side family and its floor. The
intermediate SH rectangles need not belong to that family. A uniform
direct seed and O1(b)'s same-box inputs are still unproved here.

The physical-size requirement is essential to this deduction. A separate
seed at each cutoff with no common physical size bound gives no fixed
ell satisfying the displayed inequality. The account/effective-weight
identification is also not optional: a seed for a different Wilson weight
at an effective coupling is not a seed for the actual bare first-passage
measure. FL already makes this distinction in section 2.3.

## Source boundary and final verdict

The index README, matching rows and neighbours in chunks 02, 06 and 20,
and obligations at 307–316 and 1131–1139 were read before the cited
outline passages. These index entries classify the transfer identity as
proved in detail, the first-passage objects as definitions, and the torus
floor as a construction requirement. CA-full's structural index does not
index definitions; its README and first-passage neighbouring rows were
consulted before locating `1.1:def-lattice` in CA-I. SA source files are
the supplied on-disk copies at 31a47c543775; that directory is not a Git
checkout, so their revision was not independently verified through Git.

Credits: Claude Fable 5.2 for SH and SPLIT/O1; Claude Opus 5.5 for FL and
the row-707 check; Codex gpt-6-astra for rows 722, 849 and 893. Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
supply the account's definitions and transfer framework. Balaban's method
is background; no unavailable Balaban paper or new RG estimate is used.
The O1 source blob at this pin and row 893's checked pin is identical:
`03e2beb5d12171951069a53f936a0510951ee727`.

The chain is a composition of the already checked O1 and corrected SH
statements, the already written FL composition, and the ratio-24/domain
substitution above. **HOLDS AFTER CORRECTION** is the verdict for its use
in the task's abbreviated form: require a>=3, integer periods, the same
bare first-passage measure, one common seed margin and a bounded physical
seed size for every required datum. Choose an integral final half-time,
and an account-compatible final cube if that family is desired. The
account's rectangular effective-density construction is not assumed.

No actual GLUE-FP or CORE estimate, order-one seed, or mass gap is proved.
No numerical test, formal verifier, audit, registry update, source edit,
commit or push was performed. This report is the sole local output.

RESULT: HOLDS AFTER CORRECTION — the direct 1:24 slab seed reaches SEED-FP with the stated integer, same-measure and uniform physical-size hypotheses; SH, O1(b) and the core FL composition already have cross-provider coverage (rows 722, 893 and 849), so duplicate proof work is stopped; no seed or mass gap is established.
