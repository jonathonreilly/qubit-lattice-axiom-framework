lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-29T06:06Z

# gap-purity-toy-first-fable (FINISH row 1697)

Worker: Claude Fable 5.2, high effort, Mac mini worker 1. Pinned commit 34d7b8d23.
Started 2026-11-28T18:06:49Z (date -u).
Status: IN PROGRESS. This file is written step by step. The last section says where the work stopped.

## 0. Plan

1. Read `library/gap-purity-crux-card.md` in full, and the Lean files it cites.
2. Part 1. Read Alpoge's note (`~/ym4d-papers/alpoge-rh/remark.pdf`) and Rubinstein's outline v1.5 in full.
   Write how the toy-setting proof works, what carries the decisive inequality, and what was invented for the hard setting.
3. Part 2 (closed folder). Choose a toy setting for (PUR-io). Prove the purity bound there by hand. Name the object and the inequality.
4. Part 3 (closed folder). Find the analogous object for the Wilson SU(2) transfer. Write its first lemma, or prove that the analogue does not exist.
5. Part 4 (Phase 2). Compare with the registry, rows 1380, 1481-1487, 1688. Row 1696's output is not read.

Labels: PROVED, CITED, ARGUED, GUESSED, UNVERIFIED.

Credit for Part 1: Levent Alpoge (the note and the original proof), Luke Sernau with colleagues at Anthropic and Claude (the shortened proof), Michael Rubinstein (the outline v1.5).

## 1. Part 1. How the Riemann hypothesis proof was found, and what carries it

Sources, both read in full between 2026-11-28T18:07Z and 18:19Z (date -u at both ends):
- [A] Levent Alpoge, "remark" (4 pages, `~/ym4d-papers/alpoge-rh/remark.pdf`). The announcement note of 2026-11-20.
- [R] Michael O. Rubinstein, "An outline of the shortened proof of the Riemann Hypothesis", v1.5, 2026-11-27 (`rh-outline-v1.5.tex`, 1,464 lines). It follows the shortened Lean proof of Luke Sernau, colleagues at Anthropic, and Claude (2026-11-25), which keeps Alpoge's central idea.

All statements in this section are CITED from [A] or [R] unless they carry another label. I checked no step of the proof. Line numbers are those of the `.tex` file.

### 1.1 The toy setting, and the two ideas in it

The toy setting is the Riemann hypothesis for curves over finite fields (function fields). There the statement is a theorem, with short proofs.

[A] p. 1 names two ideas that he held together in the toy setting.

- **Idea 1: Stepanov's method.** One builds an auxiliary function that vanishes at every rational point, to high multiplicity, and whose degree is small. A nonzero polynomial has no more zeros (with multiplicity) than its degree. So the number of rational points is bounded from above. [A] p. 2 says that he recognised the Siegel argument in an OpenAI result as "Stepanov without multiplicity".
- **Idea 2: the sign-only identity q N = M^k + R** ([A] p. 3, footnote 3). A character sum over a "path" quadric x_1 x_2 + ... + x_{k-1} x_k is summed in two orders. Summing over h first gives q times a count N, which has a definite sign. The other order gives a zero mode M^k plus a remainder R of square-root quality, "by iterating Parseval k times". The signs are opposite, so inverse roots cannot cancel. [A] calls this the "sign-only proof of Weil and Deligne".

**What carries the decisive inequality in the toy setting (my reading, ARGUED).** Two facts, one of each kind:

1. A rigidity fact. A nonzero object of a discrete kind cannot be too small or too divisible: a nonzero polynomial of degree D has at most D zeros with multiplicity.
2. A positivity fact. A count is nonnegative, so a one-sided bound is enough. An amplification parameter (the multiplicity in Stepanov, the power k in idea 2) makes the one-sided bound sharp.

The main term is never the difficulty. The whole proof is the comparison of two bounds on one object.

### 1.2 How the same structure appears in the hard setting

[R] Steps 1-10 show the same two facts in the number-field proof.

| Toy setting | Number-field proof ([R]) |
|---|---|
| One-sided bound is enough (a count is >= 0) | Landau's lemma: only the upper bound R(y) <= y^(-1/2+eps) is needed ([R] Section 1, lines 129-161). Zeros of the twists enter with the opposite sign ([R] Section 3, lines 240-314). |
| A nonzero polynomial has at most deg zeros | Chebyshev's principle: a nonzero integer that many primes divide, and that is not too large, bounds a prime sum from above ([R] Section 5, lines 373-405). For algebraic numbers the product formula replaces "a nonzero integer is at least 1" ([R] lines 676-684). |
| Forced vanishing at rational points | Forced divisibility by the inert primes: derivatives of functions with complex multiplication are divisible by p^floor(ap/(p^2-1)) at each inert p ([R] Section 6, lines 490-545). The cause is structural: supersingular reduction, formal group of height two. Split primes do not divide ([R] lines 526-528). |
| Multiplicity | A chain of m theta lifts. Each lift adds the inert-prime divisibility once more ([R] Section 10, lines 954-960). [A] p. 1: multiplicity "is hard to find over the integers, corresponding to something like differentiating whole numbers". The chain length is m of order sqrt(X); [A] credits this suggestion to Claude. |
| Degree of the auxiliary function | Size, in a Gaussian (Bargmann-Fock) norm where |z^j|^2 = j!. In this norm size and twice the divisibility agree in the term j log j, and the period (Chowla-Selberg) matches the constant L'/L(1,chi_d) - gamma ([R] Section 7, lines 567-640). |

### 1.3 What had to be invented to find the analogue

These are the inventions that [A] and [R] name. I list them because Part 3 needs the same list for (PUR-io).

1. **A native form of the amplifier.** Multiplicity does not exist over the integers. The analogue is not a copy; it is a different object (a chain of theta lifts between unitary groups) that does the same work "in a natively automorphic manner" ([A] p. 1; timeline items 4, 8). The gain is linear in m. The cost (control of denominators) is quadratic in m. The balance at m of order sqrt(x) gives the exponent 1/2 ([R] lines 960, 998, 1199).
2. **A source of forced structure.** The inert primes divide CM derivatives for a structural reason. No estimate gives this. ([R] Section 6; [A] timeline item 2.)
3. **A norm in which the two sides agree to leading order.** Without it, a single derivative shows only one half of its size as divisibility ([R] lines 569, 901-906: "Why a single number fails": the cofactor is about half of the logarithm).
4. **One main term, never evaluated, bounded from both sides.** The proof does not make the cofactor small. Theorems A and B give an upper bound and Theorem C gives a lower bound relative to the same enormous quantity h. Then h cancels ([R] Section 9, lines 908-951; A.5, lines 1411-1418). [R] line 951: the product formula alone "does not produce the term Dh: that is the arithmetic content of Theorem C".
5. **Many vectors, not one number.** A Gram determinant of a family that fills all but a proportion 4/b^2 of a D-dimensional space. Hadamard gives the upper bound. The product formula gives the lower bound ([R] Section 8).
6. **A seesaw that makes the object computable.** Lifts out of an indefinite group have no finite formula. The seesaw identity replaces them by finite class sums on definite lattices ([R] Section 11, lines 1048-1055).
7. **A reduction that removes circularity.** The bound is proved for every auxiliary prime d, with no information on zeros. Only afterwards is d chosen, by a zero-density estimate, so that the twists have no zero in one box ([R] lines 314, 319-370). The order of the choices matters.

### 1.4 The lessons I take to (PUR-io) (ARGUED; each is a test, not a method)

- **(S1) Find the rigidity fact first.** The toy proof is short because one discrete fact does the work. A toy for (PUR-io) must show which discrete or structural fact gives purity, and it must be a fact that the abelian twin does not have.
- **(S2) One-sided, by positivity.** Purity is at most 1 always. Only the lower bound 457/625 is needed, and the transfer operator is positive.
- **(S3) The main term must cancel, not be estimated.** Purity is tr(P0 T^(2u)) / tr(P0 T^u)^2. The bulk free energy is the same above and below. A method that bounds numerator and denominator separately must be exact in an extensive quantity (Proposition NO-A in Section 3 makes this precise).
- **(S4) The analogue of the amplifier is not a copy.** If the toy mechanism has no native form at the couplings of the crux card, then the toy does not transport, however clean it is. Part 3 tests this.
- **(S5) Order of choices.** (PUR-io) leaves two free choices: the side l (any multiple of 1024) and the infinite set of cutoffs. A proof may fix them last, as [R] fixes d last.
