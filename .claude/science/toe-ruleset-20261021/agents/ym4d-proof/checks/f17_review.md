# Independent hostile review of F17

Reviewer: Codex, separate review context, 2026-10-29 (America/New_York).
This is a **same-family review: Codex reviewing Codex-authored work**. I did
not author F17. This review implements PROCESS_LIGHT.md item 3 and the
F17 author brief. Prior reviews were read to check the scope of imported
interfaces; their verdict words do not replace the arguments below.

Reviewed `F17.md`: 397 lines, SHA-256
`b2a4f0f8650ff2db736acfaa1b0f30be1d30d449ceb827e32f55186b81e82440`.
All seventeen source hashes in `checks/f17_sources.json` match the files
inspected. References below bind to these bytes. Large-source content was
located by strings and read in bounded ranges; whole-file hashing was
used only for identity, not as a scientific read.

**No binding correctness defect found in the scoped conditional
mathematics.** LAND below approves the reductions, countermodels,
normalization calculation, and limited method obstruction. It does not
approve a Yang–Mills estimate: the author's actual route verdict remains
**UNDECIDED**, and F17-SF-B, F17-WINS-B and H_int remain **OPEN**. No
scientific source change is required for this disposition.

## 1. Consumer quantifiers and the two-scale reduction

**CONFIRMED conditional.** F17:25–64, :127–174, :390–392 were checked
against W_T0:25–80, :337–389, :454–525 and REVIEW_W_T0:24–65, :164–180.

The full TS-up hypothesis supplies an all-grid power estimate, but the
finite witness uses only the two fixed physical labels t_0 and t_1.
Let A=c_-/U_+(m_0)>0. The trajectory supplies U_-(m)→infinity, while
F17-SF-B and (4) give directly

    f_(K,R)(t_m) <= C_sf/u_(K-m) + W H(u_(K-m))
                 <= C_sf/U_-(m) + W H(U_-(m)).

The second inequality uses H nonincreasing. A nonincreasing real function
with limit zero at infinity is nonnegative, so no signed-tail loophole is
present. The right side tends to zero and permits one m_1>m_0 chosen
before either limit. The constants and that choice are independent of
cutoff and volume. The nonnegative finite error R_F is inherited from
W_T0's F-B hypothesis and RLARGE's flow bracket, not proved in F17.

For the weaker (6), limsup of the LF sum plus the uniform regular bound
gives limsup f(t_1)<=A/2 on the same SEQ. MOM2-B implies uniform
integrability at each of the two fixed labels, for example by
E[X 1_(X>M)]<=E[X^2]/M. Joint convergence therefore transfers both
first moments to the same limiting state. This does not assert convergence
of second moments. ALG-B and SHARP-B are independently retained for the
common reconstructed interpretation.

If y_0-y_1>=A/2 and the marked comparator satisfies z_0-z_1<=0, then

    A/2 <= (y_0-z_0)-(y_1-z_1)
         <= |y_0-z_0|+|y_1-z_1|.

Thus the positive-part witness has margin A/2 and at least one moment
differs by A/4. These are W_T0's marked-class conclusions only. The note
does not infer an e-only identification, OWN-free characterization,
sharp-time vector, moment theorem, or mass gap from a first-moment bound.
With only (6), it correctly drops the all-grid UV conclusion; with (4)
on the full hierarchy it takes the fixed-label limits first, then m→∞.

The decay distinctions at F17:166–174 are also correct. For (5),
H(v)=C exp[-c 2^(-2p)(log v)^(2p)]: p>1/2 beats every fixed power;
p=1/2 gives exactly Cv^(-c/2); and 0<p<1/2 beats no positive power.
After adding C_sf/v, a power TS-up follows for the stated alpha ranges.
Every p>0 still suffices for the two-scale argument. The test function
1/log(2+v) correctly shows that vanishing need not have a power rate.

## 2. Weighted LF input and genuine non-necessity scope

**CONFIRMED as an exact interface and logical countermodel; no RG
achievability proved.** F17:70–138, :176–203.

The kernel normalization in PROOF's `Decision 4: the RG kernel`
(current :2340–2348) and RLARGE:49–58 makes the bare marginal exact.
A nonnegative partition independent of the numerical value of B then
gives (3) by linearity. Summing over x inside M pays the spatial count;
no localization, independence, or unproved Markov contraction is hidden
in that identity. The first-failed-cut construction gives only a finite
measurable partition, as the author expressly states. It gives neither
the regular estimate nor the weighted insertion estimate. Returned and
failed-return histories cannot be silently removed from that partition.

Equation (6) deserves a precise limitation: it is an expectation budget
after a chosen regular-sector estimate, not a newly obtained Peierls
theorem. It is a sufficient consumer interface, not a necessary
characterization of every possible decomposition; if C_sf/u is loose,
the actual LF allowance could be larger. The words “minimal two-scale
version” are sound as a reduction of the data consumed by this proof,
not as an optimality theorem. F17 explicitly calls the inputs OPEN and
does not claim that renaming the budget establishes achievability.
Equation (4) is more structured: one actual-history partition, all
histories and normalizers, a spatial sum, a common H, and a summable
sequence w independent of K,R,k. Its verification remains substantive.

The Bernoulli construction has pointwise

    0 <= B <= v^(-alpha) sum_(r>=0) 2^(-r-1) <= v^(-alpha),

while exp[-log(v+br)^2]/exp[-a(v+br)] tends to infinity for every a>0.
Its nonzero contributions are positive on the associated events, and
Y_r<=L^(4r)I_r. Hence weak event probabilities and even amplification
upper bounds do not imply that a stronger probability exponent is
necessary for a small expectation. The independent additive example
does not purport to realize the particular per-r partition bound (4);
that stronger claim is neither used nor needed. Disjoint reallocation
preserves the total weighted mass, not automatically its previous
per-r allocation.

These examples are not Yang–Mills configurations and do not incorporate
the actual geometric survival predicates. F17:196–203 preserves that
distinction. A lower amplitude bound would instead imply the stated
individual probability inequality, but still would not alone prove a
strict c_LF beta_->4 law. This matches CODEX_REVIEW_ASSEMBLY R4 and
CODEX_REVIEW_HINT2 F4 without treating a divergent upper bound as a
physical lower bound.

## 3. Strict and critical amplification estimates

**CONFIRMED conditional.** F17:207–257.

In (9), both the event/amplification decomposition and its spatial
multiplicities are missing Yang–Mills inputs. With those supplied, set
r=k-j and v=u_k. The lower flow bracket gives

    L^(4r) exp(-a u_(k-r))
      <= exp(a R_F) exp(-av) L^((4-a beta_-)r).

This proves (10), with its additive-flow factor retained. It is not an
unconditional consequence of a probability rate alone.

At a beta_-=4 the exponential factor becomes constant in r. Put
b=beta_- log L and r_0=ceil(2R_F/b). For r>=r_0,
u_(k-r)>=v+br/2. For the at most r_0 earlier terms, positivity of u gives
(1+u)^(-s)<=1. Since x↦(1+v+bx/2)^(-s) decreases,

    sum_(r>=0) (1+v+br/2)^(-s)
      <= (1+v)^(-s) + integral_0^infinity (1+v+bx/2)^(-s) dx
       = (1+v)^(-s) + 2(1+v)^(1-s)/(b(s-1)).

This verifies (12), including R_F=0, uniformly in finite depth. With
(9), the full estimate is C_0 C exp(aR_F) exp(-av) times this expression
plus r_0. It is bounded by a constant times exp(-av), hence by every
fixed inverse power. The regular term limits the combined TS-up claim
to 0<alpha<=1, exactly as written.

On the exact trajectory with slope beta_-, the probabilities in (11)
are legitimate for C=1 and v>0, and cannot obey any larger exponential
rate because exp((a'-a)u)/(1+u)^s→infinity. Setting
Y_r=L^(4r)I_r realizes the expectation model with equality. Thus a
strict exponent margin is genuinely unnecessary even within that
model. It supplies finite first moments but no uniform second-moment
bound; the explicit MOM2-B warning is necessary and present. Replacing
4 by another proved amplification exponent changes the threshold, but
spatial slice dimension alone cannot justify that replacement.

## 4. Raw-counting obstruction

**CONFIRMED for the stated estimate class only.** F17:261–305.

At fixed m, u_k<=U_+(m). For r=floor(k/2), the upper flow bracket and
monotonicity of q yield

    4r log L-q(u_(k-r))
      >=4r log L-q(U_+(m)+R_F+beta_+ r log L)→infinity

when q(v)=o(v). The last argument is asymptotically linear in r, so
the q term is o(r). Fixed numbers of paid defects and fixed polynomial
prefactors in the scale/coupling variables do not change the conclusion.
For q(v)=a_eff v, the geometric lower bound (15) uses beta_+, the
correct side of the bracket. It diverges exponentially below threshold
and linearly at a_eff beta_+=4. Restricting to one fixed physical time
does not bound the finer-scale range as K→infinity.

The independent Bernoulli model realizes the failed estimate as its
actual first moment and satisfies product event bounds. A bounded
weighted observable on the same variables realizes the opposite
behavior. Consequently the probability/amplification data alone cannot
decide the desired expectation bound. This is an information obstruction,
not a lower bound for the Yang–Mills observable and not a no-go theorem
for decision 4. Larger paid clusters, variable cluster cutoffs, returned
insertions and small failed returns are expressly kept outside the
obstruction's conclusion. This is the scope required by
CODEX_REVIEW_LARGE F5, F8 and F9.

## 5. Reviewed producer interfaces

**CONFIRMED as a scoped inventory of missing inputs.** F17:307–344.
The following checks explain why the available statements cannot simply
be substituted for the weighted source theorem.

| Source inspected | Scope preserved in F17 |
|---|---|
| PROOF `Decision 4`, RLARGE §0 | The chain is positive and normalized. Its negative log contains the field-dependent sum of log normalizers. Exact marginal preservation does not estimate a bare B insertion. |
| RLARGE §1.2; REVIEW_RLARGE_V3 opening findings, Part 1 and Part 2 | RLF remains an OPEN target. The bad-only SU(2) implication uses the final minimum price and shadow costs, conditional on inputs under the correct relaxed/future-tilted laws. Collar defects, SU(N) extensions and the returned price a_ret are not granted. The reviewed future-law bridge is retained as missing. |
| LARGE55 TL/PP/MIS/COL; CODEX_REVIEW_LARGE F1–F3,F6,F9 | Positive raw propagation does not supply spatial source locality; centered mismatch tails need a geometric event bridge; unobserved forward integration does not settle source-reading histories, reference ratios, normalized returned activities or holes. No such stronger interface is promoted to PROVEN. |
| LARGE55 §§2,5–6; CODEX_REVIEW_LARGE F4,F5,F8,F9 | Fixed-cutoff counting failures do not exclude variable cutoffs or observable weights. Raw prices must pay polynomial, entropy and boundary costs before use. Small failed returns do not inherit the large-cluster charge automatically. |
| LCONV55 §F and §G; CODEX_REVIEW_LCONV R1,R8,R9 | Specified negative-curvature examples do not refute every admissible chart. The exact separation of convexity and rarity windows is unproved. One-step conditional positivity and tilted Peierls/forcing estimates remain open. |
| W_T0 §4.1 and REVIEW_W_T0 | Spatial magnetic flow needs its own transport, MOM2 and common sharp-time realization. A 4D-flow discussion or deterministic block witness supplies no automatic comparison. |

The normalization identity at F17:321–326 is exact by multiplication:
the remaining density has coefficient (1-lambda)a, and division by its
own normalizer leaves N_((1-lambda)a)(M)/N_a(M). That ratio cannot in
general be dropped. A minimized column action is a different tilt.
Likewise u^q exp(-au) cannot be bounded by a fixed multiple of exp(-au)
when q>0; allowing a_eff<a absorbs the polynomial. F17 correctly requires
the final exponent in every summability threshold.

The assessment claims neither a complete disk-wide producer search nor
an impossibility theorem for the normalized soft RG. Its UNDECIDED
achievability disposition is therefore honest. Source-weighted
integration is an ARGUED research preference, not a demonstrated
improvement in the unresolved Yang–Mills estimates.

## 6. Instanton convention and H_int

**CONFIRMED normalization and conditional arithmetic.** F17:346–392;
FLOW55:24–29; RLARGE:44–48; W_T0:437–444.

In the displayed Euclidean component convention, the Hodge dual has
the same squared norm as F. Expanding the nonnegative square gives
integral F^2>=|integral F tilde F|=32pi^2|Q|. Multiplication by
1/(4g_std^2) gives S>=8pi^2|Q|/g_std^2, with equality for the stipulated
self-dual or anti-self-dual field. Substituting u=2N/g_std^2 gives
S_inst=(4pi^2/N)u. No existence, integer-charge, lattice survival, or
probability theorem is required for this normalization identity.

If the named one-loop slope is supplied, its product with 4pi^2/N is
11N/3>4 for N>=2. For the actual lower bracket the strict condition is
instead beta_->N/pi^2. F17 does not replace the latter by mere positivity
of beta_- or derive the beta function from the arithmetic.

The attribution to the instanton authors and to Balaban and Dimock
carries no proof weight. No remembered [m] flow-persistence assertion or
external literature lemma is used in this review. The square identity
is rebuilt above.

The final outcome table preserves all three logically distinct cases:
a proved sufficient upper-bound input would discharge only that leaf;
F17-COUNT retires only its specified probability-counting method; the
actual route stays UNDECIDED. H_int, the common OS/algebra bridges, the
lower bound and MOM2-B remain open. Neither marked-class separation nor
a first-moment lemma alone proves the original non-freeness target or
a mass gap.

## Procedure

Only this review file was created. No author/source/log, audit, ledger,
axiom, commit or numerical experiment was changed or produced. No agent
or pool was launched. All scientific checks were written arguments, so
PROCESS_LIGHT's numerical pre-registration rule was not triggered.
Source hashing ran with nice 10 and BLAS/OpenMP thread limits set to one;
the preceding environment check showed load 2.28 and 52% free memory.

VERDICT: LAND
