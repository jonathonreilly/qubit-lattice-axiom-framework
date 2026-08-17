---
claim_id: admissibility_dirac_kahler_spatial_dressing_invisibility_bounded_theorem_note_2026-08-17
claim_type: bounded_theorem
claim_scope: "on the certified package at both rational shear fixtures, the observable wall extends to the spatial-dressing class for a structural reason — at fixed momentum the spatial shift acts as a scalar phase that cancels under conjugation, so the momentum-diagonal blocks of all spatial translates coincide and the displayed eight-weight smeared-and-conjugated family collapses to two effective weight-sums whose descent kernel consists exactly of the zero-sum directions compressing to the zero observable — no member with nonzero quotient compression descends; the admissible-observable spaces have exact dimensions 57 over the root field and 113 real (the rank-one arithmetic n^2 - (n-1) shared with, but not equal to, the Block 119 intertwiner spaces, displayed without conflation); the time direction is certified visible (a transfer-conjugated translate has a different diagonal block), so time-smeared dressings are the live route and the counterterm conclusion is an inference, not a theorem; the original solve's rank-eight certificate was refuted in verification and is recorded as corrected; and time-smeared dressings, the naturality classification, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_sourced_quotient_execution_bounded_theorem_note_2026-08-17
runner: scripts/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_sourced_quotient_execution_bounded_theorem_note_2026-08-17
target_blocker_text: "Non-local current dressings for the observable wall; the naturality classification of the swap completion; curved OS positivity on the half-space package."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Time-smeared and transfer-conjugated dressings for the observable wall; the naturality classification of the swap completion; curved OS positivity on the half-space package."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-124 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact scalar-phase cancellation and momentum-diagonal spatial-translate equality, exact two-sum factorization of the displayed eight-weight family, exact corrected rank-two descent map with zero-sum kernel equal to the zero-compression kernel, exact 57-dimensional root-field and 113-dimensional real admissible-observable spaces, and exact transfer-sandwich visibility on the certified package at both rational shear fixtures; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Spatial-Dressing Invisibility And The Wall Extension

**Date:** 2026-08-17

**Campaign block:** 125

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.py`](../scripts/admissibility_dirac_kahler_spatial_dressing_invisibility_2026_08_17.py)

## 1. Result Up Front

[Block 124](ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md)
closed onto the following handoff next gate, anchored byte-exactly at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md:16`
and elaborated in its Next Decision:

> Non-local current dressings for the observable wall; the naturality
> classification of the swap completion; curved OS positivity on the
> half-space package.

**THE SPATIAL-DRESSING INVISIBILITY LEMMA.** Let $X$ be the inherited
spatial shift, let $P_{k,s}$ be the certified fixed-momentum projector, and
let $D_s$ be the routed density block at either rational shear fixture. On
the $k$-fiber, $X^r=e^{ip_kr}I$, and therefore

\[
 P_{k,s}X^{-r}D_sX^rP_{k,s}
 =e^{-ip_kr}e^{ip_kr}P_{k,s}D_sP_{k,s}
 =P_{k,s}D_sP_{k,s}.                            \tag{1}
\]

That one line is the structural headline. Every spatial translate has the
same momentum-diagonal block. The quotient used by
[Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
sees those diagonal blocks and is blind to the spatial phases carried by
off-diagonal momentum entries.

Write the displayed four-translate, reflection-conjugated family as

\[
 \mathcal D_s(a,b)
 =\sum_{r=0}^3 a_rX^{-r}D_sX^r
  +\sum_{r=0}^3 b_rX^{-r}\Theta D_s\Theta^{-1}X^r,
 \qquad (a,b)\in\mathbb K_s^4\oplus\mathbb K_s^4.             \tag{2}
\]

Here $\mathbb K_s$ is the exact root field at the fixture and
$\Theta$ is the inherited reflection conjugation. Put

\[
 A=\sum_{r=0}^3a_r,
 \qquad
 B=\sum_{r=0}^3b_r.                              \tag{3}
\]

Equation (1) collapses all eight weights to the two effective sums:

\[
 P_{k,s}\mathcal D_s(a,b)P_{k,s}
 =A P_{k,s}D_sP_{k,s}
  +B P_{k,s}\Theta D_s\Theta^{-1}P_{k,s}.       \tag{4}
\]

The certified two-column descent residual has rank two at both fixtures.
Consequently its pullback to the eight weights has the exact kernel

\[
 \ker\mathcal R_s
 =\left\{(a,b):\sum_ra_r=0,
                    \ \sum_rb_r=0\right\},       \tag{5}
\]

of dimension six over $\mathbb K_s$. The compression map in (4) has the
same kernel. Hence every descending member of (2) compresses to the zero
observable, and every member with nonzero quotient compression fails
descent. The observable wall therefore extends from the routed density to
the entire displayed spatial-dressing class.

This extension is not a small numerical failure. Spatial smearing cannot
alter the quotient data because the scalar phase has already cancelled
before the descent equations are tested. More translates or different
spatial weights within this one-momentum-diagonal mechanism only change the
two sums in (3).

The ambient admissible-observable spaces remain large. On each certified
eight-dimensional prequotient block, preserving the seven-dimensional null
kernel imposes seven independent root-field equations. Thus

\[
 \dim_{\mathbb K_s}\mathfrak A_s
 =8^2-(8-1)=57.                                  \tag{6}
\]

For complex coefficient matrices with real descended compression, the
seven complex kernel conditions and the one real compression condition give

\[
 \dim_{\mathbb R}\mathfrak A_s^{\rm obs}
 =2(8^2)-\{2(8-1)+1\}=113.                       \tag{7}
\]

The arithmetic $n^2-(n-1)$ is the same rank-one arithmetic that appears in
the intertwiner count of
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
The spaces are not the same: the present condition preserves one null
kernel and permits a descended scalar, while the Block 119 condition
intertwines two specified quotient maps. Section 6 gives an explicit
rank-one witness separating the two.

The time direction is different. For the inherited contractive transfer
$T_s$, define the two-sided transfer translate

\[
 \mathcal T_s(D_s)=T_s^\dagger D_sT_s.             \tag{8}
\]

At each fixture, (8) has at least one certified diagonal block unequal to
that of $D_s$. Thus transfer time is visible to the quotient even though
spatial translation is not. Time-smeared and transfer-conjugated dressings
are the live next route.
It is reasonable to infer that a successful repair may need a
time-dependent counterterm, but necessity of such a counterterm is not a
theorem here.

The catch record is part of the result. The original solve reported rank
eight for the weight-level certificate. Verification refuted that claim:
the family factors through (3), so its rank cannot exceed two. The corrected
rank is exactly two. The wall conclusion survived the refutation in the
stronger structural form (5): every extra kernel direction is a zero-sum
direction whose quotient compression is already zero.

This theorem is deliberately narrow. Time-smeared dressings, the naturality
classification of the swap completion, curved OS positivity, the completed
ADM/history transporter, joint gravity, the gravity constraint quotient
beyond the displayed carrier, Records, audit retention, axiom amendment,
obligation retirement, and TOE percentage movement remain outside it.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at the authority
snapshot inherited by Block 124:
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. No newer authority claim is
made here.

The exact stacked parent is
[Block 124](ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md)
commit `da2b9020e9f15ac55640ef87a0798a78e3c9a0d0`, content-bound through
note blob `f31c1e10219d8cd85cbd24644f0e5f4dfbba90d5`. Its observable wall comes
from
[Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md),
and its rank-one positive quotient and swap completion come from
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
No audit verdict is imported from any note.

The executed contract is:

1. the certified package at both rational shear fixtures $s=5/13$ and
   $s=3/5$, with the inherited spatial shift, reflection conjugation,
   routed density, null quotient, and positive transfer;
2. the fixed-momentum scalar action of every spatial shift and the resulting
   equality of all momentum-diagonal translated density blocks;
3. the displayed four direct and four reflection-conjugated spatial
   translates, with eight independent root-field weights;
4. exact factorization of their quotient compression and descent residual
   through the two weight-sums $(A,B)$;
5. the corrected rank-two residual, its exact six-dimensional zero-sum
   kernel, equality with the zero-compression kernel, and exclusion of every
   nonzero-compression descending member;
6. the seven-condition derivation of the admissible-observable dimensions
   $57$ over the root field and $113$ over the real observable space;
7. explicit non-conflation of those admissible-observable spaces with the
   equal-dimensional Block 119 intertwiner spaces;
8. one transfer-conjugated diagonal-block nonequality showing that time is
   visible, with time-smeared dressings left live; and
9. one narrow structural wall, plus an explicit catch record correcting the
   refuted rank-eight certificate without weakening the wall conclusion.

The assigned primary runner is the path recorded in the front matter. This
note does not invent a replay footer or a `TOTAL` line: under the supplied
note-only contract, the scientific content is the supervisor-verified
certificate stated above, including the rank-eight refutation and corrected
rank-two result. The five fixed N5 resolution lines are reproduced verbatim
in Section 9 so the runner and note have one textual contract.

The scope is the eight-dimensional fixed-momentum prequotient blocks, both
fixtures, four spatial translates in each of the direct and
reflection-conjugated families, their quotient-diagonal data, and the
displayed transfer-sandwich contrast. No time-smeared construction,
naturality classification, curved reconstruction, history transporter,
joint-gravity construction, or gravity quotient beyond the displayed
carrier follows.

## 3. The Invisibility Lemma

Choose the inherited momentum basis on the four-line spatial quotient and
write

\[
 X=\operatorname{diag}
   \bigl(e^{ip_0},e^{ip_1},e^{ip_2},e^{ip_3}\bigr),
 \qquad p_k={\pi k\over2}\pmod{2\pi}.             \tag{9}
\]

The shear fixture changes the certified density and transfer data, but not
this representation of the closed spatial shift. For any operator $Y$ and
any spatial displacement $r\in\mathbb Z_4$, its momentum entries obey

\[
 (X^{-r}YX^r)_{k\ell}
 =e^{-ip_kr}Y_{k\ell}e^{ip_\ell r}
 =e^{i(p_\ell-p_k)r}Y_{k\ell}.                  \tag{10}
\]

Setting $\ell=k$ gives the entrywise certificate

\[
 (X^{-r}YX^r)_{kk}=Y_{kk}
 \quad\text{for every }k,r.                     \tag{11}
\]

Equivalently, with $P_{k,s}$ denoting the full certified fixed-momentum
block,

\[
 P_{k,s}X^{-r}YX^rP_{k,s}=P_{k,s}YP_{k,s}.       \tag{12}
\]

Equations (10)--(12) apply separately to $Y=D_s$ and
$Y=\Theta D_s\Theta^{-1}$. They are exact identities at $s=5/13$ and
$s=3/5$; no approximate phase comparison or fixture-specific cancellation
is involved.

The mechanism is now visible entry by entry. Spatial translation can rotate
an off-diagonal momentum entry $Y_{k\ell}$ by a relative phase when
$k\ne\ell$. It cannot change a diagonal entry because the left and right
phases are mutual inverses. The inherited quotient tests the
momentum-diagonal blocks. It therefore discards exactly the entries on which
spatial translation can act nontrivially.

This is an invisibility lemma about the displayed per-momentum quotient. It
does not say that spatial translation is trivial on the full carrier, that
off-diagonal momentum coherences vanish, or that an observable resolving
several momenta or individual sites would be blind to the phase in (10).

## 4. The Family Collapse

Collect the eight weights in

\[
 w=(a_0,a_1,a_2,a_3,b_0,b_1,b_2,b_3)^{\mathsf T}
 \in\mathbb K_s^8,
\]

and define the sum map

\[
 \Sigma=
 \begin{pmatrix}
  1&1&1&1&0&0&0&0\\
  0&0&0&0&1&1&1&1
 \end{pmatrix},
 \qquad
 \Sigma w=(A,B)^{\mathsf T}.                    \tag{13}
\]

The map has rank two and

\[
 \ker\Sigma
 =\{(a,b):\mathbf1^{\mathsf T}a=0,
             \ \mathbf1^{\mathsf T}b=0\},
 \qquad \dim_{\mathbb K_s}\ker\Sigma=6.         \tag{14}
\]

Let $\mathcal C_s(w)$ be the vector of all certified quotient-compression
blocks of $\mathcal D_s(w)$, and let $\mathcal R_s(w)$ be the corresponding
vector of null-descent residuals. The invisibility lemma supplies the exact
factorizations

\[
 \mathcal C_s=C_s\Sigma,
 \qquad
 \mathcal R_s=R_s\Sigma,                         \tag{15}
\]

where the two columns of $C_s$ are the direct and
reflection-conjugated diagonal-block profiles, and the two columns of $R_s$
are their descent residual profiles. The certified entrywise reductions at
each fixture give

\[
 \operatorname{rank}C_s=2,
 \qquad
 \operatorname{rank}R_s=2.                      \tag{16}
\]

Since both maps in (16) have two-dimensional domains, each has zero kernel.
Combining (14)--(16) yields

\[
 \ker\mathcal C_s
 =\ker\mathcal R_s
 =\ker\Sigma.                                   \tag{17}
\]

This equality, not merely a rank count, is the family-collapse certificate.
There are six weight directions that disappear from the descent residual,
but exactly those same six directions disappear from the quotient
observable. They are cancellations among spatial copies of an already
identical diagonal block.

The four displacements exhaust the displayed closed spatial carrier.
Therefore adding arbitrary weights on that carrier does not enlarge the two
effective coordinates. The collapse is not a sparse-weight ansatz: it is a
factorization of the whole displayed spatial smearing class.

No conclusion follows for a dressing that mixes distinct momentum fibers,
changes the quotient map, inserts transfer time, or uses a larger carrier.
Those operations need not factor through $\Sigma$.

## 5. The Wall Extension

An operator in the displayed family descends exactly when its residual
vanishes. Equations (16)--(17) give the full chain

\[
 \begin{aligned}
 \mathcal D_s(w)\text{ descends}
 &\Longleftrightarrow \mathcal R_s(w)=0\\
 &\Longleftrightarrow \Sigma w=0\\
 &\Longleftrightarrow A=B=0\\
 &\Longleftrightarrow \mathcal C_s(w)=0.
 \end{aligned}                                   \tag{18}
\]

Thus the weight-level residual map has corrected rank two, not rank eight,
and a six-dimensional kernel. That kernel contains many nonzero weight
vectors, for example

\[
 w_0=(1,-1,0,0,0,0,0,0)^{\mathsf T}.             \tag{19}
\]

But (19) is not a repaired observable: its quotient compression is zero.
Every other vector in the kernel has the same fate. Conversely, if
$\mathcal C_s(w)\ne0$, then $(A,B)\ne(0,0)$, the injectivity of $R_s$ gives
$\mathcal R_s(w)\ne0$, and descent fails.

The precise wall extension is therefore

\[
 \boxed{\text{no member of the displayed spatially smeared and
 reflection-conjugated family with nonzero quotient compression descends}.}
                                                               \tag{20}
\]

This statement holds at both rational shear fixtures. It extends
[Block 122's](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md)
routed-density wall from one operator to every spatial smearing of that
operator and its displayed reflection conjugate on the certified carrier.

The structural mechanism is stronger than an exhaustive list of eight
failed basis weights. At fixed momentum, every translated basis candidate
already presents the same diagonal block to the quotient. The quotient has
only the two direct/conjugate columns to test, and both fail independently.
Spatial weights can cancel those columns only by cancelling the observable
itself.

Equation (20) is narrow. It is not “no non-local dressing works.” It does
not cover transfer-time smearing, two-time insertions, modifications of the
quotient map $Q$, site-resolved multi-momentum observables, or density
counterterms outside (2).

## 6. The Admissible-Observable Spaces

The wall does not say that the quotient admits no nonzero observables. It
says that the displayed spatial family misses the large linear space of
operators which preserve the null kernel.

Fix a momentum block and fixture. Let $V_{k,s}\cong\mathbb K_s^8$, let

\[
 \pi_{k,s}:V_{k,s}\longrightarrow L_{k,s}\cong\mathbb K_s
\]

be the certified rank-one quotient map, and put
$N_{k,s}=\ker\pi_{k,s}$. An endomorphism $O$ is admissible precisely when it
induces an endomorphism on $L_{k,s}$:

\[
 O(N_{k,s})\subseteq N_{k,s}
 \quad\Longleftrightarrow\quad
 \pi_{k,s}O=\lambda_O\pi_{k,s}                  \tag{21}
\]

for some scalar $\lambda_O$.

Choose $e_0$ with $\pi_{k,s}e_0=1$ and choose
$e_1,\ldots,e_7$ as a basis of $N_{k,s}$. Equation (21) is equivalent to
the seven conditions

\[
 \pi_{k,s}Oe_j=0,
 \qquad j=1,\ldots,7.                            \tag{22}
\]

They are independent: in this adapted basis, the matrix unit $E_{0j}$
changes only the $j$th condition. There is no eighth condition because
$\pi_{k,s}Oe_0$ is the freely induced quotient scalar $\lambda_O$. Hence

\[
 \dim_{\mathbb K_s}\mathfrak A_{k,s}
 =\dim_{\mathbb K_s}
   \{O:\pi_{k,s}O=\lambda_O\pi_{k,s}\}
 =64-7=57.                                       \tag{23}
\]

For the real observable space, start with the $128$ real parameters of an
$8\times8$ complex matrix. Conditions (22) are seven complex equations,
hence fourteen real conditions. Requiring the descended one-dimensional
observable $\lambda_O$ to be real adds one further real condition. Thus

\[
 \dim_{\mathbb R}\mathfrak A_{k,s}^{\rm obs}
 =128-14-1=113.                                  \tag{24}
\]

Equations (23)--(24) hold at every momentum block and at both fixtures. The
counts are exact rank-one quotient arithmetic, not a count of successful
members of the spatial family.

The number $57=8^2-(8-1)$ also occurs in
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md),
but equality of dimensions is not equality of spaces. Block 119 constrains
an operator against specified source and reflected target quotient
functionals. Equation (21) instead asks one endomorphism to preserve one
fixed null kernel.

The separation can be witnessed without conflating their coordinate
systems. Let $\jmath_{k,s}$ be the Block 119 target functional and
$\widetilde\pi_{k,s}$ its source functional. If
$\jmath_{k,s}\notin\operatorname{span}\{\pi_{k,s}\}$, choose

\[
 n\in\ker\pi_{k,s}
       \quad\text{with}\quad \jmath_{k,s}(n)\ne0,
 \qquad
 \eta\notin\operatorname{span}\{\widetilde\pi_{k,s}\},
 \qquad
 W_\star=n\otimes\eta.                           \tag{25}
\]

Then $\pi_{k,s}W_\star=0$, so $W_\star\in\mathfrak A_{k,s}$, whereas

\[
 \jmath_{k,s}W_\star=\jmath_{k,s}(n)\eta
 \notin\operatorname{span}\{\widetilde\pi_{k,s}\}.          \tag{26}
\]

Thus $W_\star$ is not a Block 119 intertwiner. In pair-adapted bases it is
a single off-diagonal matrix unit. If instead
$\jmath_{k,s}\in\operatorname{span}\{\pi_{k,s}\}$, inequality of the two
spaces forces
$\widetilde\pi_{k,s}\notin\operatorname{span}\{\pi_{k,s}\}$; then
$W_\star=I_8$ is admissible by (21), while
$\jmath_{k,s}I_8$ is not proportional to $\widetilde\pi_{k,s}$ and hence is
not an intertwiner. These two cases display the non-conflation: the
dimension formula is shared; the defining maps and resulting subspaces are
not.

## 7. The Time Direction Is Visible

The inherited transfer is positive and contractive, but it is not a
unit-modulus scalar phase on the full fixed-momentum prequotient block.
Define

\[
 D_s^{[0]}=D_s,
 \qquad
 D_s^{[1]}=T_s^\dagger D_sT_s.                  \tag{27}
\]

The certified entrywise comparison at each fixture supplies a momentum
$k_\star$ for which

\[
 \Delta_{k_\star,s}
 :=P_{k_\star,s}(D_s^{[1]}-D_s^{[0]})P_{k_\star,s}
 \ne0.                                           \tag{28}
\]

Equation (28) is the positive time-visibility certificate. The spatial
phase in (12) is accompanied by its inverse and must cancel on a diagonal
block. No corresponding scalar-phase identity forces the two positive
transfer factors in (27) to cancel, and the certified block difference says
that they do not.

A time-smeared family can therefore begin with genuinely different
diagonal-block columns,

\[
 \mathcal D_s^{\rm time}(c)
 =\sum_{t=0}^m c_t(T_s^\dagger)^tD_sT_s^t,
 \qquad
 P_{k_\star,s}D_s^{[1]}P_{k_\star,s}
 \ne P_{k_\star,s}D_s^{[0]}P_{k_\star,s}.       \tag{29}
\]

Unlike the spatial family in (3), the $t=0$ and $t=1$ columns are not
identical before the descent conditions are imposed. This is why
time-smeared and transfer-conjugated dressings are the live route after W1.

No success theorem follows. Several time columns could still become
dependent after the full descent and reflection conditions are imposed.
Nor does (28) prove that time-dependent counterterms are required. It only
supports the inference that a repair invisible to pure spatial smearing may
need transfer-time dependence. The necessity, form, and naturality of such
a counterterm remain open.

## 8. The Catch Record

The original solve treated the eight translated weights as eight
independent descent columns and reported a rank-eight certificate. That
certificate is false. Equation (15) gives the immediate rank bound

\[
 \operatorname{rank}\mathcal R_s
 =\operatorname{rank}(R_s\Sigma)
 \le\operatorname{rank}\Sigma=2.                \tag{30}
\]

Verification caught the contradiction, rejected the rank-eight report, and
forced the family to be recomputed after the phase cancellation. The
corrected certificate is

\[
 \operatorname{rank}\mathcal R_s=2,
 \qquad
 \ker\mathcal R_s=\ker\Sigma,
 \qquad
 \dim\ker\mathcal R_s=6.                        \tag{31}
\]

The correction changes the weight-space statement. There are nonzero
weights satisfying the descent equations. It does not change the
observable-space terminal, because (17) adds

\[
 \ker\mathcal R_s=\ker\mathcal C_s.             \tag{32}
\]

Every newly exposed kernel vector compresses to the zero observable. Hence
the wall conclusion survived the refutation in stronger form: it no longer
rests on eight allegedly independent failures; it rests on a structural
factorization showing that all spatial freedom is quotient-invisible.

The checker discipline deserves explicit credit. A reported full-rank
answer was not protected because it supported the desired wall. It was
tested against the algebraic symmetry, refuted, and replaced by the exact
lower-rank statement. The surviving conclusion is narrower and more
informative: nonzero weights may descend, but no nonzero quotient
observable in the displayed class does.

## 9. No-Go Discipline Gate

There is exactly one bounded observable wall. It is structural and leaves a
positive time-directed route.

- W1 — **SPATIAL-DRESSING INVISIBILITY WALL:** no spatial smearing plus
  $\Theta$ conjugation of the routed density yields a nonzero conserved
  observable on the certified quotient. At fixed momentum the spatial shift
  is a scalar phase, all translated diagonal blocks coincide, and the full
  displayed eight-weight family factors through two sums. Its descent kernel
  is exactly the zero-sum kernel which compresses to the zero observable.

W1 excludes every nonzero-compression member of (2) at both fixtures. It is
narrow to the certified per-momentum quotient, the four spatial translates
on the displayed carrier, their $\Theta$-conjugated partners, and the routed
density which generated them.

W1 does not cover time-smeared dressings, two-time insertions, or
$Q$-modification routes. Equation (28) positively certifies that transfer
time is visible, so those routes remain live. W1 is not an OS no-go and is
not a curved OS no-go.

Equivalently: spatial phases cannot change the quotient-diagonal data; the
only spatial weight combinations which satisfy descent cancel that data to
zero.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). Spatial
invisibility, family rank, ambient admissibility, and time visibility remain
separate.

1. **PROVED — strongest invisibility lemma and wall extension / scalar-phase
   cancellation on every fixed-momentum block / no member of the displayed
   spatially smeared and $\Theta$-conjugated family with nonzero quotient
   compression descends.** This is the strongest route and the shipped
   theorem.
2. **PROVED — family collapse / factorization of all eight weights through
   $\Sigma w=(A,B)$ / corrected rank two with a six-dimensional zero-sum
   kernel equal to the zero-compression kernel.** Nonzero kernel weights
   represent the zero quotient observable.
3. **PROVED — admissible-observable dimensions with non-conflation / seven
   independent null-kernel conditions and one real compression condition /
   exact dimensions $57$ over the root field and $113$ real.** The rank-one
   arithmetic is shared with, but the space is not equal to, the Block 119
   intertwiner space; witness (25)--(26) separates them.
4. **PROVED / POSITIVE — time-visibility certificate / the contractive
   transfer appears twice with the same sign in a transfer sandwich / one
   transfer-conjugated translate has a different momentum-diagonal block at
   each fixture.** Time-smeared dressings are a live route.
5. **CORRECTED / CHECKER CREDIT — catch record / test the alleged rank eight
   against the phase-factorization bound / refute it and replace it by the
   exact rank-two certificate.** The wall survives in the stronger
   zero-compression form.
6. **UNTESTED-LIVE — time-smeared dressings, naturality, and curved OS /
   exploit time-visible quotient columns, classify the swap completion, and
   reconstruct the half-space package / test whether a nonzero conserved
   observable survives those stronger structures.** No result on those
   terminals is imported here.

The completed ADM/history transporter, joint gravity, and the gravity
constraint quotient beyond the displayed carrier remain downstream of row
6. W1 consumes none of those routes.

### N2 — Wall-Independence Audit

W1 is independent of Block 124's sourced-quotient wall, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md:771-798`.

[Block 124](ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md)
asked which vanishing-expected-momentum matter classes form a sourced Gauss
quotient and which of those classes transfer preserves. Its wall mechanism
was the $p_2$ convention split together with unequal even and odd transfer
rates. Its positive break was the convention-free stable balanced sector.

The present W1 begins after that quotient exists. Its object is a candidate
observable on each rank-one quotient block. Its mechanism is scalar-phase
cancellation under spatial conjugation, followed by the equality of the
descent and zero-compression kernels. It neither uses the $p_2$ branch split
nor asks whether a matter state remains balanced under transfer.

There is an honest shared carrier: both blocks use the same certified
per-momentum quotient and transfer package. That does not merge the walls. A
matter class can form a stable sourced graph while a routed density and all
of its spatial translates fail to define a nonzero observable on that graph.
Conversely, the time-visibility certificate does not alter Block 124's
balanced-sector theorem.

The Block 122 routed-observable wall is the direct parent of W1. The present
result extends its object class; it does not recycle Block 124's
unbalanced-stability mechanism as an observable-descent argument.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.
Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| certified package | the inherited finite quotient package only |
| both rational shear fixtures | exactly $s=5/13$ and $s=3/5$ |
| observable wall extends to the spatial-dressing class | W1, the displayed family (2) only |
| structural reason | exact factorization, not numerical exhaustion |
| at fixed momentum | one inherited momentum block at a time |
| spatial shift acts as a scalar phase | $X^r=e^{ip_kr}I$ on that block |
| cancels under conjugation | the two factors in equation (1) |
| momentum-diagonal blocks | the data tested by the inherited quotient |
| all spatial translates coincide | equality (12) on the displayed carrier |
| displayed eight-weight smeared-and-conjugated family | four direct plus four $\Theta$-conjugated terms |
| collapses to two effective weight-sums | factorization through $(A,B)$ |
| descent kernel consists exactly | equality (17), not containment only |
| zero-sum directions | both four-weight sums vanish |
| compressing to the zero observable | $\ker\mathcal R_s=\ker\mathcal C_s$ |
| no member with nonzero quotient compression descends | wall statement (20) |
| admissible-observable spaces | null-kernel-preserving endomorphisms (21) |
| exact dimensions 57 over the root field and 113 real | equations (23)--(24) |
| rank-one arithmetic n^2 - (n-1) | $8^2-7=57$ only |
| shared with, but not equal to, the block 119 intertwiner spaces | witness (25)--(26) |
| displayed without conflation | equal counts do not identify subspaces |
| time direction is certified visible | nonequality (28) |
| transfer-conjugated translate has a different diagonal block | positive transfer sandwich, not spatial conjugation |
| time-smeared dressings are the live route | untested next construction |
| counterterm conclusion is an inference, not a theorem | no necessity result is claimed |
| original solve's rank-eight certificate | rejected historical claim only |
| refuted in verification | contradiction with rank bound (30) |
| recorded as corrected | exact replacement (31) |
| time-smeared dressings | untested-live observable-repair route |
| naturality classification | untested-live downstream classification |
| curved os positivity | explicit reconstruction firewall |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not completed |
| gravity constraint quotient beyond the displayed carrier | outside scope |
| records | no Records claim |
| retention | independent-audit firewall |
| axiom amendment | explicitly not justified |
| obligation retirement | TOE accounting firewall |
| toe percentage movement | TOE accounting firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting statement |
| no toe percentage moves | TOE accounting statement |
| retained-positive end-to-end theory count remains zero | audit accounting |
| actual adm/history transporter remains | standard partial-close statement |
| gravity constraint quotient remains unexecuted | constraint-scope firewall |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | five N5 keys |

No phrase upgrades a per-momentum spatial invisibility theorem into a no-go
for every non-local observable. Nothing turns a zero-compression weight
kernel into a nonzero descended operator, identifies the admissible space
with the Block 119 intertwiner space, proves a time-dependent counterterm
necessary, or asserts an absolute observable wall. Nothing asserts
time-smeared success, naturality, curved OS positivity, transporter
completion, joint gravity, axiom amendment, audit retention, obligation
retirement, or TOE percentage movement.

### N4 — Residual Matching

The Block 124 handoff next gate, quoted byte-exactly, is:

> Non-local current dressings for the observable wall; the naturality
> classification of the swap completion; curved OS positivity on the
> half-space package.

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 124 next gate](ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md:16` | “Non-local current dressings for the observable wall; the naturality classification of the swap completion; curved OS positivity on the half-space package.” | the spatial half of the non-local route is decided for the displayed class: it yields no nonzero descending compression; time-dependent dressings and the other two tasks remain |
| [Block 122 observable wall](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | the routed local density fails null-space descent on the certified quotient | extended from the undressed density to all four spatial translates, all spatial weights, and their displayed $\Theta$ conjugates |
| inherited structural theme | the per-momentum quotient retains only quotient-diagonal operator data | equation (10) locates spatial information off diagonal, while equations (11)--(17) prove that the quotient sees only the two unchanged diagonal profiles |

This is a partial closure of Block 124's next gate. Its non-local-dressing
clause has had the complete spatial class on the displayed carrier tested,
but time-smeared and transfer-conjugated dressings remain live. Naturality
and curved OS positivity are untouched.

The phrase “the non-local route's spatial half is decided” means only the
family (2) on the certified carrier. It does not mean that an arbitrary
multi-momentum, site-resolved, transfer-time, or $Q$-modified observable has
been classified.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the certified package at both
rational shear fixtures, fixed-momentum spatial shifts act by scalar phases
which cancel under conjugation, so every spatial translate has the same
momentum-diagonal block and the displayed eight-weight direct-plus-$\Theta$
family factors through two weight-sums; its corrected rank-two descent
kernel is exactly the zero-sum kernel compressing to the zero observable,
so no member with nonzero quotient compression descends, while transfer
time is certified visible and remains a live route.”

Forbidden upgrades include:

- “no non-local dressing works”;
- “time-dependent counterterms are required” as a theorem; and
- “the observable wall is absolute.”

The first exports W1 beyond the spatial class. The second converts the
inference after (29) into an unproved necessity statement. The third erases
the positive time-visibility certificate and the live two-time and
$Q$-modification routes.

Also forbidden are “the eight-weight descent map has rank eight,”
“nonzero kernel weights define a repaired observable,” “the
admissible-observable space is the Block 119 intertwiner space,”
“time-smeared dressings work,” “naturality is classified,” and “curved OS
positivity holds.” Equations (17), (30)--(32), and witness (25)--(26) refute
the first three; none of the remaining claims is tested here.

The five N5 resolution lines fixed for the runner are reproduced verbatim:

```text
N5: per_element: scalar-phase cancellation, diagonal-block equality, family-factorization, corrected-rank-two, zero-sum-kernel, zero-compression, admissible-space-dimension, time-visibility, and catch certificates are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: at fixed momentum every spatial shift is a scalar phase that cancels under conjugation, so all spatial translates have the same momentum-diagonal block
per_block: the displayed eight-weight smeared-and-conjugated family collapses to two effective weight-sums whose descent kernel is exactly the zero-sum subspace compressing to the zero observable; no nonzero-compression member descends
lattice_wide: checked and not executed — time-smeared and transfer-conjugated dressings for the observable wall, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient beyond the displayed carrier, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The result closes the spatial-smearing
branch of the inherited observable wall without weakening the quotient
descent condition.

| route | present status | remaining terminal |
|---|---|---|
| one direct spatial translate | diagonal block equal to the undressed block | no independent quotient column |
| all four direct translates | exact factorization through $A=\sum_ra_r$ | only one effective direct column |
| all four $\Theta$ conjugates | exact factorization through $B=\sum_rb_r$ | only one effective conjugate column |
| combined eight-weight family | exact two-sum collapse | no further spatial coordinate |
| descent residual | corrected rank two at both fixtures | no nonzero effective-sum kernel |
| weight-space kernel | exact six-dimensional zero-sum space | all members compress to zero |
| nonzero quotient compression | exact descent failure | excluded only in displayed class |
| root-field admissible space | exact dimension $57$ | construct a member outside spatial span |
| real observable space | exact dimension $113$ | impose any stronger physical conditions separately |
| Block 119 intertwiner comparison | same $n^2-(n-1)$ arithmetic, unequal spaces | no identification by dimension |
| transfer-conjugated translate | certified diagonal-block nonequality | build and test a time-smeared family |
| time-smeared dressing | untested-live | compute compression and descent ranks |
| two-time insertion | untested-live | test whether time columns survive reflection constraints |
| $Q$ modification | untested-live | change the carrier or quotient map explicitly |
| naturality classification | untested-live | classify the swap completion |
| curved OS route | not executed | prove positivity on the half-space package |
| gravity constraint quotient | displayed carrier only | execute beyond that carrier |

The scan finds no axiom-amendment route. The spatial part of Block 124's
first next-gate clause is discharged for the displayed family. The remaining
terminals are time-dependent observables, naturality, curved reconstruction,
the completed transporter, and gravity beyond the displayed carrier.

### N7 — Steelman

**Hostile steelman: the family was small.** It used only four spatial
translates and their four $\Theta$ conjugates, so a rank-two collapse says
little about genuinely non-local dressings.

Agreed about the eight displayed weights, and that is the point of the
structural result. On the four-site closed spatial carrier, those four
translations are all spatial displacements. Equation (12) makes all spatial
smearing small from the viewpoint of the per-momentum quotient: adding or
reweighting spatial translates cannot create a new diagonal block. The
claim remains narrow because an operator that mixes momenta, resolves sites,
uses transfer time, or modifies $Q$ is not in (2).

**Hostile steelman: the time route may face its own collapse.** Equation
(29) shows different diagonal blocks before the full constraints are
imposed, but it does not prove independent descending time columns.

Agreed. Time visibility is a positive route certificate, not a successful
dressing theorem. Transfer powers may become dependent after null descent,
reflection-adjointness, conservation, and naturality are imposed. That
possible time-column collapse is open and is named as the first next test.

**Hostile steelman: site-resolved multi-momentum observables could retain
the spatial phases.** The invisibility lemma may diagnose the quotient more
than the density.

Agreed. Equation (10) shows exactly where the missing information lives: in
off-diagonal momentum entries. A site-resolved or multi-momentum observable
can see those entries, but it lies outside the per-momentum quotient used
here. Whether the carrier and quotient should be enlarged to admit such
observables is a named $Q$-modification and carrier question, not a result of
this block.

These steelmen preserve narrow W1. The displayed carrier exhausts pure
spatial smearing, time may still collapse under stronger conditions, and
multi-momentum observables remain a separate carrier route.

### N8 — Cross-Cycle Echo

The immediate campaign chain separated positive quotient construction,
observable descent, sourced dynamics, and spatial dressing.

| campaign block | narrowing that leads to W1 and the live route |
|---|---|
| [Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | supplied the certified rank-one-per-sector positive quotient and swap completion; its equally sized intertwiner spaces remain distinct from (21) |
| [Block 122](ADMISSIBILITY_DIRAC_KAHLER_QUOTIENT_OBSERVABLE_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | proved that the routed density fails null-space descent and left non-local repair open |
| [Block 124](ADMISSIBILITY_DIRAC_KAHLER_SOURCED_QUOTIENT_EXECUTION_BOUNDED_THEOREM_NOTE_2026-08-17.md) | executed the stable balanced sourced quotient and named non-local current dressings as the next gate |
| Block 125 | proves pure spatial-dressing invisibility, extends the observable wall across the displayed spatial class, and certifies transfer time as visible |

The present result does not reuse failure of the undressed density as proof
that every translate fails. That extension follows from the independent
phase identity (10)--(12) and the two-column residual certificate. Nor does
the equality $\ker\mathcal R_s=\ker\mathcal C_s$ follow from rank two alone;
both injective two-column maps in (16) are required.

**No-Go Discipline verdict:** **PASS** only for narrow W1. No spatial
smearing plus $\Theta$ conjugation of the routed density yields a nonzero
conserved observable on the certified per-momentum quotient at either
fixture. The mechanism is structural scalar-phase invisibility, the
corrected weight-level rank is two, and the descent kernel is exactly the
zero-sum zero-compression kernel. **POSITIVE** for time visibility and the
live time-smeared route. **FAIL** for “no non-local dressing works,” an
absolute observable wall, a theorem requiring time-dependent counterterms,
time-smeared success, identification with the Block 119 intertwiner space,
naturality, curved OS positivity, a completed ADM/history transporter,
joint gravity, a quotient beyond the displayed carrier, axiom necessity,
audit retention, obligation retirement, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. Scalar-phase cancellation, diagonal-block
equality, the two-sum factorization, corrected rank-two kernel, admissible
space dimensions, and transfer-time nonequality are finite consequences of
the displayed quotient, shift, density, reflection, transfer, and fixtures.
No new primitive is assumed.

This is bounded route closure, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. construct time-smeared and transfer-conjugated dressings for the
   observable wall and test conservation, null descent,
   reflection-adjointness, and possible time-column collapse;
2. classify the naturality of the swap completion on whichever dressed
   package survives; and
3. execute curved OS positivity on the half-space package with that sourced,
   dressed, and classified structure.

The actual ADM/history transporter remains unexecuted beyond the displayed
half-space positive package, its contractive parity-paired transfer, the
balanced sourced Gauss graph modulo constant gauge, and the spatial-dressing
wall.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted beyond the displayed
balanced carrier.
