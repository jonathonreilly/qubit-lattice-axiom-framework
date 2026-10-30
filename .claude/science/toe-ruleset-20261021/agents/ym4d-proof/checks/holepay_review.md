# HOLEPAY fresh hostile review

Review date: 2026-10-30. This review concerns the frozen **research note and
checker**, not closure of EXTCONT E15, an RG induction, an audit verdict, or
a physical existence/mass-gap claim. The frozen packet needs the narrow
corrections below before LAND. Its main positive raw-charge calculation and
its negative comparisons survive the independent checks described here.

## Findings requiring correction

1. **Make the sign and count domain of the conditional certificate explicit.**
   HOLEPAY.md:282–310,323–341 (HP12–HP14) must require integer `n>=1`,
   `c_H>0`, and nonnegative boundary/reference debit constants. In particular,
   replacing `b_partial |Bdy_F|` by `b_partial c_partial n` requires
   `b_partial>=0`; a bound on the boundary cardinality does not justify that
   substitution for negative `b_partial`. This is a mathematical hypothesis,
   not just terminology. For example, with constant `N=D=1`, `B=0`,
   `q=c_ref=0`, `|Bdy|=0`, `c_partial=1`, and `b_partial=-20`, HP12 as written
   holds, but HP13 would claim `1<=exp[-(20-10 log 2)n]`. Also HP14 divides
   by `c_H`, and the absorption `n<=2^(n-1)` uses an integer count. Stating
   these hypotheses repairs the implication; it does not establish them
   on the actual history family.

2. **Quantify the history envelope and retain its constant.**
   HOLEPAY.md:333–344 says an envelope controls the sum of history suprema
   but does not state the inequality or its constant, then gives `A=A_0`.
   A bound for one paired quotient gives that coefficient's E15 price;
   it does not give the same bound for an arbitrarily large sum of such
   quotients. Distinct history masks also have different inactive-root
   charging maps. One sufficient formulation is to apply HP1 separately
   to each complete history family and require a proved uniform
   `sum_h ||K_h||_(mu,T) <= B_hist * M_input`. The resulting summed output
   bound is `(1+C_hole) B_hist M_input` if inactive terms are retained
   (or `C_hole B_hist M_input` for the active part). Do not replace that
   premise by `sup_h ||K_h||` or silently set `B_hist=1`. A coefficient
   already summed on one fixed mask can instead receive a direct HP12
   estimate. Distinguish these uses and the per-coefficient `A_0` from any
   final history-sum constant. The author's subsequently proposed
   `B_hist` formulation resolves this issue if inserted with these scopes.

3. **Restore the scope of the cap comparison.**
   HOLEPAY.md:353–365 (HP15) inherits CHARGE C9/C13 but omits their
   source-free hypothesis and cap conditions. The reference bound requires
   `0<zeta<=1` and `4 zeta` strictly below every retained interior cut.
   The numerator is a source-free nonnegative sector/complete disjoint
   history sum with an actual original-action lower bound `q n`; it is
   not an arbitrary signed connected activity. In the note's general
   source-bearing setting the numerator can have an additional source
   bill, absent from HP15. State the source-free specialization or include
   its proved source envelope. The displayed extensive debit and the
   conclusion that this majorant fails at unbounded volume/core ratio are
   correct under that specialization. CHARGE.md:155–193,240–251 and
   MIXSMALL.md:361–387,410–417 give the exact relevant restrictions.

4. **The full-mask endpoint is an identity of supports, not of the weighted
   operator.** HOLEPAY.md:96 says full Lambda gives the identity. If
   `Lambda=Gamma`, then `R(X)=X`, but the actual operation remains
   `K_X -> w_X K_X`. The allowed choice `w_X=2`, `A=2`, `S_X=0` is already
   a counterexample to an operator identity. Specify that the saturation
   support map is the identity; the supplied weights remain.

5. **Track whether mathematics started independently of completed check
   rows.** In checks/holepay_check.py:125–133, mathematical work precedes
   the first appended check at lines 141–142, and resource guards execute
   within that interval. The exception handler at lines 249–251 uses an
   empty `checks` list to choose NOT RUN. A refusal in that interval would
   falsely report NOT RUN instead of INCOMPLETE, contrary to criteria
   lines 37–39. Set an explicit `math_started` flag after the successful
   pre-mathematics guard and before invoking the first mathematical
   routine, and use it in the refusal classification. Preserve the current
   historical receipt and its runner hash: this defect does **not** falsify
   the existing receipt, whose refusal was at the pre-mathematics guard.

The author identified the endpoint, sign/domain, and cap-scope concerns in a
message after the source was frozen and after this review had begun. They
were independently assessed above, rather than counted as independent
discoveries. The author also offered the quantified history-envelope repair
after this review raised that issue. No source fixes were made by this
reviewer.

## Independent mathematical checks

**HP1–HP3: full roots and nested masks.** For each input put
`a_X=exp(mu|X|) sup T(K_X)`. Submultiplicativity and the supplied weight
bound give an output contribution at most `A exp[-(tau-mu)S_X] a_X`.
If the output root lies in an inactive component H of size m, connectedness
of X and `X meets Lambda` force X through the external face boundary of H.
That boundary has at most `8m` active vertices. Charging the input sum to
those vertices gives `8A m exp[-(tau-mu)m] ||K||`; an active root costs A.
This independently verifies the improvement from EXTCONT's 9 to 8. The
ratio of successive terms of `m/2^m` is `(m+1)/(2m)`, proving the maximum
1/2 at m=1,2 and hence `C_hole=4A`. The calculus maximum is
`sup_(s>0) s exp(-delta s)=1/(e delta)`.

For HP2, filling Lambda-components is a monotone idempotent closure on sets
meeting Lambda. Every Omega-component lies in a Lambda-component, so
`X subset R_Omega(X) subset R_Lambda(X)`. Applying the Lambda closure and
idempotence to both inclusions proves the equality. This uses a common
graph and fixed masks. HP3 is an exact product identity for once-allocated
charges; it neither commutes integration with saturation nor creates a
fresh probability charge at every scale. These boundaries agree with
LIB1.md:218–273,357–438 and EXTCONT.md:433–500.

**HP4–HP8: the raw original-action factor.** RD R2 defines failures only
among bad-block components, including completion failures; thus each
original failed block has a cut-bad interior plaquette. RD.md:264–302
does not supply such a witness for extra chart-only failures, and the note
correctly excludes that extrapolation. The inequality
`||I-U||HS >= ||I-U||op` gives `s(U)>=epsilon^2/(2N)`. Distinct block
interiors give n distinct witnesses, hence
`Q_F>=theta c^2 u^d n/(2N)`.

An ordered rth derivative of a four-occurrence plaquette has at most `4^r`
product terms, each bounded by `h_0^r`. This includes inverse occurrences
and simultaneous link-array directions. To check the exponential jet
without executing the Bell checker, use formal positive coefficient
majorants: derivative bounds `q_r<=z(4h_0)^r` give the exponential majorant
`exp[z(exp(4h_0 t)-1)]`. Its rth exponential-generating coefficient is
`(4h_0)^r M_r(z)`, verifying HP5 independently of the runner's recurrence
and partition enumeration. This is a finite derivative bookkeeping
identity, not an assumed complex analyticity estimate.

With `z=theta u C_P n`, each degree-k term costs
`u^(k-r/2)n^k<=u^3 n^6` for `r<=6`, `k<=r`, `u,n>=1`. There are no
coarse or original-source derivatives of this particular factor. For
`kappa_abs=max(6,3/d)`, the inequalities `kappa_abs>=6` and
`d kappa_abs>=3` give `u^3 n^6<=(u^d n)^kappa_abs`. Absorbing half of the
exponential has maximum `(2 kappa_abs/(e a))^kappa_abs`, confirming the
stated `A_raw`. One collar costs at most `3^4=81` vertices, so division
of `(a/2)u_*^d` by 81 gives exactly
`tau_raw=theta c^2 u_*^d/(324N)` and HP8. The no-hole case is separately
`w=1`.

The smooth function is defined before selecting its evaluation sector;
no derivative of the bad-set indicator has been acquired. Its original
readers fit in the asserted coarse parents, but this does not convert the
coarse count into a count of all original reader blocks. Most importantly,
splitting a factor from an integrand does not split it from every connected
coefficient of the logarithm. The warnings in HOLEPAY.md:211–217 preserve
that distinction and are essential. There is no E15 proof here.

**HP9–HP11: growth, merger, and ownership.** Projection and collar commute
with unions. A singleton birth's subsequent collar radius relative to its
projected seed obeys `r_next<=1+ceil(r/L)`. Starting at r=1, r<=2 is
invariant for L>=3. Therefore each cohort occupies at most `5^4=625`
current vertices. Projection preserves face-connectedness and the collar
is face-connected, so a cohort lies wholly in one final hole component.
This proves the same bound for selected complete components, even after
mergers. The count is of birth occurrences, not independent original
plaquette credits.

The charge-ownership requirement is substantive: a later birth can reuse
ancestral readers, so HP10 cannot be removed. A nonempty cohort never
becomes empty under the specified maps; a fixed reserve Q cannot dominate
`tau sum_(j=1)^r |H_j|>=tau r` for unbounded r. Conversely CHARGE C6
allocates fractions of an extensive original volume, whose scale volumes
sum geometrically, so there is no contradiction. Each level-j block has
`L^(4j)` original-block preimages on the stated compatible tori, proving
HP11 and the failure of the proposed 625 original-footprint bound.
Strictly positive finite kernels and identity neighborhoods at later
levels provide the claimed finite-history geometry witnesses; they do
not supply a depth-uniform lower bound on an integrated coefficient.

**HP12–HP14: complete quotient jets, conditional only.** A second formal
majorant checks the inverse constants. For `z=Bn`, normalized derivatives
of either positive integral are dominated by
`A(t)=exp[z(exp(t)-1)]`. The reciprocal series is dominated coefficientwise
by `1/[1-(A(t)-1)]=1/(2-A(t))`. The quotient is therefore dominated by
`A(t)/(2-A(t))`. Multiplying the formal series gives precisely the inverse
recurrence and quotient convolution in the note. For example
`I_1=z`, `I_2=z+3z^2`, `C_1=2z`, `C_2=2z+6z^2`. Ordered Leibniz
subsequence counts give the same binomial multiplicities without commuting
fine derivatives. The constant terms, factorial conventions, all mixed
orders through ten, and the four-label binomial factor are consistent
with REALRGA RGA3/RGA4.

The degree is at most ten after the Taylor sum, so integer n>=1 gives
`P(Bn)<=n^10 P(B)<=exp[(10 log 2+log P(B))n]`. With finding 1's sign
conditions, the resulting exponent is exactly HP13. If `q_net/c_H>=tau`
and `S_X<=c_H n`, then `q_net n>=tau S_X`; thus a genuinely supplied
local coefficient satisfies E15. This checks the **implication**, not the
existence of that coefficient, positive paired representation, local
score bound, selectors, supported tails, or uniform history envelope.
HP12 can be stronger than a direct integrated E15 estimate. The note
appropriately leaves these actual hypotheses open rather than calling
them weak final lemmas.

Fixed nonnegative selectors outside the logarithm are legitimate on fixed
integration domains with dominated derivatives. A parameter-dependent
disappearing fiber is different. The note retains this distinction, all
endpoint normalizers, and the source/regulator bills. REFMATCH RM7–RM12
provides only a conditional cancellation mechanism under its actual
MATCH/RM2 assumptions; those assumptions remain open in REFMATCH section 7.
No source read establishes their missing realization for HOLEPAY.

**HP15–HP18 and fresh gaps.** Under finding 3's cap hypotheses, `6n_j`
plaquettes each cost at most `8u_j zeta^2`; `4n_j` Haar-cap factors each
cost `2N^2 log(1+4N/zeta)`; and the last kernel upper and lower bounds
cost `16 kappa u_j n_(j+1)` together. This reconstructs every coefficient
of `d_j` in HP15. With fixed local n and `d_j>0`, the displayed sufficient
inequality fails as `n_j/n` grows. This is a failure of that majorant,
not evidence that the actual quotient grows.

For the fixed-event forward gap estimate, a radius `1/t` cap around a
maximizer, with `t>=1`, lower-bounds the normalized denominator by
`e^-1 (1+4Nt)^(-2N^2)` after subtracting the maximum exponent. The gap
numerator is at most `e^(-ta)`, yielding the stated `q_gap`; the useful
product-event price uses `q_gap>=0` and fixed event boundaries. These
restrictions should remain attached to the reference to MS17–MS18.
Tilting by `H=1_E` gives probability one when the original event has
positive probability. For a coherent mean `M=WP` with positive P, the
trace identity shows W maximizes the kernel exponent, giving zero fresh
gap. Neither observation rules out a matched original-charge construction.

The LF7 boundary proof also works in a supplied full jet norm because
matching holds as functions and each surviving support meets the boundary.
Rooting there gives `2(q_T+b_T)|Bdy|`, and the jet algebra exponentiates
that bound. Combining it with LF6's `B_0=16V_w` gives exactly
`c_B^T=32V_w(q_T+b_T)/log L`; LF7's scalar estimates alone do not supply
the required jet inputs. A four-dimensional cube has `n^4` vertices and
eight disjoint external faces of `n^3` vertices, so a single supported
constant input has the exact HP17 ratio `exp(mu n^4-8b n^3)`. The
unboundedness is confined to this specified boundary-only weight. HP18
is a different input space and its transfer follows from the same root
argument; its membership and regeneration are not proved by defining it.

## Runner and execution evidence

The complete runner and criteria were read statically. The two saturation
implementations, positive-root norm calculation, explicit inactive-root
mutation, cohort recursion, and recurrence-versus-partition polynomial
comparison are relevant finite regressions. Their scope is narrower than
the written proof and does not test HP12 on an actual history. The cohort
probe is expressly a set-geometry regression: its stage-one birth at
`(1,0,0,0)` is already in the first cohort's hole, so it is not an actual
RD R2 birth history. The proof of HP9 covers the permitted histories
analytically; this diagnostic must retain its non-realization scope.

The supplied receipt is **NOT RUN**, has an empty check list, and records
niceness zero at the pre-mathematics guard. Stderr independently records
`nice: setpriority: Operation not permitted`. The receipt's note, runner,
and criteria hashes match the frozen files, and stdout equals the JSON
receipt byte-for-byte. No mathematical PASS exists. No scientific runner,
numerical probe, mutation test, or resource-guard bypass was executed in
this review. Only file/source bookkeeping was executed; the independent
checks above are written mathematical derivations and static code review.
The NOT RUN condition does not contradict those written derivations and
does not by itself establish or refute E15.

## Source identity and independence limits

Worktree HEAD is `688a8ddf958e6a5ba5402d6b7fdad4d283af56df`; local
`origin/main` is `01589af3faf806b736c42dc2f3bd625e9edead9f`. Remote
freshness is not certified. The applicable methodology files compared
equal to that local main snapshot. The entire HOLEPAY note, runner,
criteria, log, source inventory and execution receipt were read. Necessary
source coverage was EXTCONT section 4; MIXSMALL sections 2,4–7; LIB1
sections 1–5; LFPRICE LF4–LF7; CHARGE sections 1–2; REALRGA sections 2–4;
RD R1–R6; REFMATCH sections 1,3.1,4,6–7; and JMBRB B-MASS/B-GAP.
Inventory hashing is not a claim that every other inventoried file was
fully reviewed. No literature citation was used as a proof premise.

Every entry of `checks/holepay_sources.json` matched its on-disk SHA-256
when checked. The science sources used have these identities:

| Source | SHA-256 |
|---|---|
| HOLEPAY.md | b64fc9c983cc01b349cfcf7b4890ef8dfba0a8d3d1b9514b8cb0e3928ebed9ee |
| checks/holepay_check.py | 71f8f97089192dbf2f4562bdf4caabf6921c66bd077a7d2307adecdcd5c6eae8 |
| checks/holepay_criteria.md | 9eaf6cb4ac6605953326cf29993a81a337ed4c38b463b7ed47fb0251771153f4 |
| HOLEPAY_LOG.md | 89fe32e3ebd3449d3563678155265dc7749f183d8101fdba778cb7287a0af9bd |
| checks/holepay_sources.json | 2b12a05892f24ef9aee05b36c724207f8a94cba6ac265e47bbabae3bd251eb19 |
| checks/holepay_result.json and holepay_stdout.txt | 0ab226a01873ff93ef55a19784eca32db6d0b25dd7848c0968e2dd1225d38754 |
| checks/holepay_stderr.txt | 1ae2ce53f6c4a3265acd385e7e4a21d827a2b5594337d0d9ae68b92a856b30dc |
| EXTCONT.md | b10015bbd6be5fac97fd636fdc79f665800fe9921651575b9d03b0167b534b6e |
| MIXSMALL.md | ead4ddd6bb50844d91459c3229d3abcc06b4ba02da772c578bc917a743f67340 |
| LIB1.md | 1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1 |
| LFPRICE.md | 4deb5cbf7573145a438abcda4aeedd14c4270cc05c3e63072abeb43561c77a53 |
| CHARGE.md | 8c5a5ecdb95a32089f2005bf6597d4aedefa660b9b9f8c1cc7b7a01374afc1ef |
| REALRGA.md | e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed |
| RD.md | a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5 |
| REFMATCH.md | a7f45d815b6c7c4ed51950e0d3cc30ea3a7cb650e0bcb8e508659d197889729c |
| JMBRB.md | 6320af2da97d532fbf802f2405541de8e20f6d350b575b46462fefb4c849bb0a |

This is a fresh, restricted-input reviewer context separate from authorship,
with **same-model-family review (Codex reviewing Codex)**. It is not a
cross-family check. Both contexts share the repository source arguments;
the independent work is the reconstructed algebra, geometry, scope tests,
and static checker inspection above. No formal proof assistant or
independently executed numerical implementation supplies additional
confirmation. No commits, source edits, audit/ledger changes, prompt edits,
or new subagents were made. Only this review file was written.

The narrow fixes above can make the research note landable without proving
the actual payment. The final affected source must return to this reviewer
with its changed identities. E15, selector regularity, integrated matching,
original-reader payment and the actual complete history estimate remain
open regardless of the research-note verdict.

VERDICT: HOLD
