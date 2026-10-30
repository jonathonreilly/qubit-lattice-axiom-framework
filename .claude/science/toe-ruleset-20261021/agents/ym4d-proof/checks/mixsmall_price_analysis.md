# MIXSMALL author assistance: inherited-history prices and complete readers

**Status.** The supplied results do not prove uniform small mixed groups on
the actual inherited all-cut reference. They do prove a useful extension of
CHARGE's extensive filled-sector price to **all labelled original-source
derivatives at any fixed finite order**, including a sum of complete past
histories and bounded reader insertions. The extension is proved below. It
does not supply the missing local mixed field/source jet estimate. The
counterexamples below refute specific normalized-history or forward-law
claims, not the existence of a correctly charged real expansion.

This is author assistance, not independent review or a LAND/HOLD decision.
No numerics, commits, ledger changes, or existing-file edits were performed.
The bounded task uses PROCESS_LIGHT and the MIXSMALL author brief. Credit for
the large-field organization belongs to Tadeusz Balaban and its exposition
to Jonathan Dimock; no literature lemma carries proof weight here.

## 1. Sources and exact contract

Repository HEAD: `0f561ef0b2dba3b024190fc55717c5b0ca7db881`.
The following files were read completely. Source SHA-256 identities:

| File | SHA-256 |
|---|---|
| JMBRA.md | `6dd077a3383ea69b6ab04b629ee8d13be5b60958e542b1ae778eb48f90fc7c5a` |
| JMBRB.md | `6320af2da97d532fbf802f2405541de8e20f6d350b575b46462fefb4c849bb0a` |
| RENEW.md | `42b4d2a16625d4af4f6443a38ff92d63a483485816c4533292b44f867fc978a7` |
| CHARGE.md | `8c5a5ecdb95a32089f2005bf6597d4aedefa660b9b9f8c1cc7b7a01374afc1ef` |
| REALRGA.md | `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` |
| PROCESS_LIGHT.md | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| briefs_q/MIXSMALL/AUTHOR.md | `40f9355313dd29a65df1c84f34555f31ddfa7c48a68eb1acbf0906769435117b` |

Exact target: REALRGA lines 281–330, RGA14/RGA16, and H0–H6 at lines
416–479. The required quantity is the complete integrated mixed jet, with
field order p=6 and source order q=4 initially, summed over complete
supports at rate mu+2. RGA16 asks for a joint product majorant for every
selected set and a rooted sum Q<=1/4. A blanket assertion
`weight <= epsilon^(number of support blocks)` is a stronger form one
may seek, still requiring compatible type counts; it is not the literal
statement of that contract.

Throughout, an original-source derivative changes only the original
action/observable tilt. Prescribed kernels, couplings, and the fixed
selectors used in the calculations below remain fixed. Source-dependent
cuts or coordinate substitutions require their own boundary/chain-rule
terms. A source perturbation is not a retuning of every RG kernel.

## 2. A proved actual extension: filled-sector prices with every source subset

Let E be CHARGE's original filled flux tube E_delta. Fix a level j, put
`b=L^4`, `n_l=|Lambda_l|`, and let `{I_h}` be any complete disjoint history
partition through U_j, before the fixed terminal output V=U_(j+1).
Thus I_h is independent of V; current V-dependent outcomes have been
summed, as in JMBRA A2, lines 40–52. Define

    m_h = int 1_E I_h exp(-S_0) product_(l<j) K_l
                                      dU_0 ... dU_j .       (P1)

Empty products are allowed. All m_h are nonnegative and, since histories
partition and all intermediate outputs integrate through normalized
kernels,

    sum_h m_h = int 1_E exp(-S_0)dU_0
                  <= exp[-c_delta u_0 n_0],
    c_delta=(2-4delta)^2/(2N),  0<delta<1/4.                (P2)

The last inequality follows pointwise: each original 12 plaquette has
distance at least 2-4delta from I, and
`s(U)=||I-U||_HS^2/(2N)>=||I-U||_op^2/(2N)`.
This spends original action once. No renewed action or old history price
has been inserted at later levels.

The complete numerator with n labelled real sources is

    R_h(z,V)=int 1_E I_h exp(-S_0+sum_i z_i O_i)
                            product_(l<=j)K_l dU_0...dU_j,
    Q_h(z,V)=R_h(z,V)/Z_(j,A)(V).                           (P3)

Here O_i are bounded original observables, `|O_i|<=M_i`; the denominator
has no original sources. For every subset B of [n], not just B=[n],

    partial_B R_h(0,V)
      =int 1_E I_h exp(-S_0) product_(i in B)O_i
                                      product_(l<=j)K_l.  (P4)

This follows by differentiating the finite fixed-domain integral. It
includes repeated directions by giving them distinct labels. For a
relative original Wilson coefficient epsilon_p, `O_i=-u_0 s(U_p)` and
`M_i=2u_0`. For an absolute coefficient direction v_i(p), the valid bound
is `M_i=2 sum_p |v_i(p)|`. Thus smeared directions retain their exact
coefficient map and original units.

For `0<zeta<=1`, `4zeta<epsilon_j`, the same all-cut cap as CHARGE C9
(lines 153–193) gives the following **shared, V-independent envelope**:

    sup_V |partial_B Q_h(0,V)|
      <= exp[d_j(zeta)n_j] m_h product_(i in B) M_i,
    d_j(zeta)=48u_j zeta^2+8N^2 log(1+4N/zeta)
                                             +16 kappa u_j/b. (P5)

To check every factor: the terminal kernel product is at most
`exp(8 kappa u_j n_(j+1))`. On the denominator's product identity cap,
there are 4n_j link cap masses, each at least
`(1+4N/zeta)^(-2N^2)`; its 6n_j plaquettes have s<=8zeta^2;
and the terminal kernel product is at least
`exp(-8 kappa u_j n_(j+1))`. Dividing leaves precisely d_j n_j.
The intermediate kernels were kept inside m_h, not estimated linkwise.

For the labelled source seminorm

    S_[n](F)=sum_(B subset [n]) r_B |partial_B F|,
    r_B=product_(i in B)r_i,

(P2)–(P5) prove the stronger, history-summed statement

    sum_h sup_V S_[n](Q_h)(0,V)
      <= exp[-c_delta u_0 n_0+d_j(zeta)n_j]
                                    product_i(1+r_i M_i). (P6)

There is no unjustified interchange of a sum and a supremum: each term
is bounded first by its own nonnegative m_h times the **same** envelope,
and only then are the m_h summed. A mere bound on
`sup_V sum_h Q_h(V)` would not prove (P6). If the selected history
contains V-dependent outcomes, this proof does not apply without a
new shared envelope or an exact preliminary sum of those outcomes.

Under CHARGE C10's explicit hypotheses (lines 197–218), namely
`u_*<=u_j<=u_0`, `u_*>=4`, `epsilon_j sqrt(u_j)>=8`, and j>=j_*,
take zeta=u_j^(-1/2). Its stated inequalities give

    sum_h sup_V S_[n](Q_h)(0,V)
      <= exp[-(c_delta/2)u_0 n_0] product_i(1+r_i M_i).  (P7)

For n=4, all 16 subsets, including all 15 nonempty source subsets, are
present. No 4! is inserted. For general finite n the formula remains true;
it is not a uniform all-order HIER estimate. On a real source neighborhood
`sum_i |z_i|M_i<=s_J`, the same derivation costs an extra exp(s_J).
No source radius is obtained by omitting that factor.

**Bounded mixed readers.** Insert F_h(z,U_0,...,U_j,V), possibly the
product of several readers and their full coefficient. Suppose its
pointwise labelled source seminorm is uniformly bounded by B_h. Leibniz
over source subsets gives

    sum_h w_h sup_V S_[n](Q_(h,F))(0,V)
      <= exp[d_j n_j] product_i(1+r_i M_i)
                                      sum_h w_h B_h m_h. (P8)

Indeed, differentiating `exp(sum z_i O_i) F_h` distributes the labels
between its two factors; summing subsets is bounded by
`product_i(1+r_i M_i) S_[n](F_h)`. If F_h is a product and the factors
have pointwise seminorm bounds b_i, then B_h<=product_i b_i by the same
Leibniz calculation. No independence of those readers is used.

The weights w_h must include complete connected supports, rooted type
counts, regulator conversion, and any other requested cost. For example,
a **proved** bound `w_h B_h<=exp(s n_0)` turns (P7) into
`exp[-(c_delta u_0/2-s)n_0] product_i(1+r_i M_i)`.
Neither (P8) nor the word "filled" proves such a full-reader bound on an
unspecified graph. With w_h=e^((mu+2)|X_h|), X_h must include all original
sources, all past failure/absence predicates, inactive vertices, output
readers and connected hulls. Supplied small-field reader jet bounds can
be inserted here; their actual construction is still missing.

**Exact limit of this result.** Equations (P6)–(P8) control source jets,
not the full p=6 mixed norm. On the fully integrated output above, only V
remains, and the r-th terminal exponent derivative in unit coarse
directions is bounded by `4t_j n_(j+1) h_(j+1)^r`. A separately proved
finite quotient-jet bound can therefore multiply the same m_h envelope
by its explicit finite polynomial. This is a direct route for the parent
lane's real calculus, not a claimed estimate for retained earlier fields,
moving selectors, general local cores, or arbitrary holes. Those cases
have extra differentiated factors and their actual envelopes must be paid.

For a localized core with m charged original plaquettes, repeating the
above cap calculation leaves `exp[-tau m+d_j n_j]`, CHARGE C13 (lines
239–249). Its volume bill cannot be relabelled as a local reader bill.
This shows an insufficient majorant, not a lower bound on the true local
contribution. It is the exact point where the extensive result stops.

## 3. Why full readers and all source subsets cannot be discarded

JMBRA A3–A12 (lines 72–270) supplies exact algebra: multiply every factor
reading an integrated variable, integrate their product, and retain the
union of all its original readers. Unread outputs integrate to one only
in the complete normalized creator law. A fixed terminal kernel is a
factor; it is not an integrated creator. The interacting nu_A and the
inherited J_h=rho_h/b_j are not product cells merely by notation.

There are two direct tests of any attempted reduction of the reader set.

1. **Shared-reader test.** For a common y=+1 or -1 with equal masses,
   put `f_1=f_2=epsilon(1+s y)`, 0<s<1. Then
   `E f_1 f_2=epsilon^2(1+s^2)` whereas
   `(E f_1)(E f_2)=epsilon^2`. Their connected difference is
   epsilon^2 s^2 regardless of how far apart their nominal cores lie.
   This calculation, JMBRB lines 565–572, prohibits factorization before
   the shared reader and its law are included. It does not prohibit
   weighted long-reader bounds after they are included.

2. **Actual distant-source test.** At fixed real V, with a nonzero
   history numerator and a relative original coefficient epsilon_p,
   direct differentiation gives

       partial_(epsilon_p) log Q_h(0,V)
                           =-u_0 E_(h,V) s(U_0,p).       (P9)

   Z_A contributes zero because it has no original source. For JMBRA's
   two-adjacent-block size-failure history, place the two interior g marks
   and identity elsewhere; a small open cap preserves the failure list
   independently of U_1. At an arbitrarily distant plaquette p, perturb
   one previously identity link to
   `diag(exp(i theta),exp(-i theta),1,...)` with small nonzero theta.
   Then s_p=2(1-cos theta)/N>0 and all remote cuts remain good. A smaller
   open cap has positive Haar measure, and every soft kernel is strictly
   positive at fixed real V. Consequently (P9) is strictly negative.
   The construction and margins are JMBRA lines 502–528. Thus the entire
   log Q_h cannot be a function supported solely in a fixed collar of
   its failed core. It must retain a bulk/source remainder or a genuinely
   full-support representation. There is no quantitative lower bound
   here, hence no counterexample to spatial decay or a weighted expansion.

Normalization does not avoid (P9). If
`R_h(z,V)=M_h(z) Rhat_h(z,V)` with Rhat_h a normalized history density,
then for every B,

    partial_B R_h=sum_(C subset B)
                  (partial_C M_h)(partial_(B\C) Rhat_h). (P10)

The source-dependent history mass and every lower-subset term remain.
Keeping only a fourth conditional connected response would not recover
the four-source response of the original generating function. REALRGA
RGA19 (lines 529–548) adds the further outer total-cumulance terms when
the final history/field mixture is integrated.

## 4. Explicit failure classes, with their exact scope

### F1. A normalized mandatory history is not a small activity

For a positive probability law P and any mandatory event E with
`0<p=P(E)<1`, its conditional density is `a=1_E/p` and
`int |a|dP=1`. Under any normalized Markov transport, the nonnegative
relative insertion becomes a conditional expectation and retains the
same L1 norm. This proves JMBRB B8–B9 (lines 126–148) directly by Fubini.
There is no factor exp(-q), q>0, available merely from transporting it.

This remains a mixed-reader obstruction to a **normalized** smallness
assertion. Let a local smooth reader satisfy `d<=f<=2d`, d>0. Then
`int a f dP>=d`. For example take `f=d(1+s(U_p)/2)`, which has that
range. At fixed couplings its local fixed-order jets have bounds
independent of ambient volume, so a fixed d can meet any prescribed
fixed small-reader jet bound as that volume grows.
The product has no rare-event factor p. If its mandatory event has full
support of size n, it cannot have a uniform bound epsilon^n for arbitrary
n at fixed d and 0<epsilon<1. Such positive events occur on arbitrarily
large actual filled flux tubes; complete all-bad size-failure histories
are also nonzero whenever their component exceeds the size threshold.

This refutes using the normalized mandatory-history insertion as an
ordinary small polymer. It does **not** refute the unnormalized p times
that insertion, nor (P7), nor extraction of an explicit large history
weight before an expansion. The chosen f illustrates a class of bounded
readers; it is not asserted to be an already constructed small-field
activity of the actual RG map.

### F2. Future selection can consume a fresh gap price entirely

For K(x,dy) normalized, a positive future weight H, and KH(x)>0,

    K^H(x,E)=int_E H(y)K(x,dy)/KH(x)
       <=K(x,E) sup_y H(y)/KH(x).                        (P11)

Choosing H=1_E makes the left side exactly one. Even insisting on a
strictly positive smooth H does not save a universal price: for a
nontrivial event with boundary of Haar measure zero, approximate its
indicator by smooth 0<=f_l<=1 with f_l->1_E almost everywhere, take
H_l=f_l+delta_l with delta_l->0, and use bounded convergence in numerator
and denominator. K^H_l(x,E)->1 whenever K(x,E)>0. No bounds on the jets
of these increasingly selective H_l are asserted.

Therefore JMBRB B11–B12's forward gap price cannot be copied into an
arbitrary future-conditioned history. The actual selector need not be
H=1_E: this is a counterexample to the universal inference, and isolates
the missing same-reader estimate of H/KH. CHARGE C23, lines 453–486,
keeps precisely that ratio. Uniform bounded jets/local oscillation of
actual H would be extra useful information, not a consequence of TV=1.

### F3. Actual coherent rough tubes have no uniform forward renewal price

For even compatible tori, odd L, and every N>=2, set

    g=diag(-1,-1,1,...,1),
    U_1(x)=g^(x_2+a), U_2(x)=g^b, U_3=U_4=I.

Every 12 plaquette is g. The actual paired contour sums give
`M_1=g^(X_2+a)P`, `M_2=g^(b+(L-1)/2)P`, `M_3=M_4=I`,
where `P=diag(1/L,1/L,1,...)`: the translated axial legs cancel or
contribute r_1-(L-1)/2, and the odd alternating offset sum equals one.
For M=WH, H>=I/L,

    h_M(W)-h_M(V)
      =tr[(I-W*V)* H(I-W*V)]/(2N)
      >=||V-W||_op^2/(2NL).                              (P12)

Thus the unique maximizing output has the same rough plaquette pattern,
with only the b label possibly alternating. This is an actual arithmetic
mean with a nondegenerate maximizer, not an arbitrary M=0 example.

It is not just a null-set construction. For fixed horizon R, choose
terminal tube radius delta_R small enough that 2-4delta_R exceeds every
cut, and recursively choose
`delta_j=delta_(j+1)^2/(8NL(5L-4))` as in RENEW R13. A contour contains
at most 5L-4 links. Perturbing its input tube changes its mean by at most
(5L-4)delta_j. Two trace errors in (P12) show that leaving the next tube
has gap at least delta_(j+1)^2/(4NL). A Haar 1/t cap about a maximizer
has mass at least (1+4Nt)^(-2N^2), so a union bound gives

    P(all R output tubes | U_0 in initial tube)
      >=1-sum_(j<R) |E_(j+1)| e(1+4Nt_j)^(2N^2)
                       exp[-t_j delta_(j+1)^2/(4NL)].    (P13)

At fixed R and finite volumes this tends to one as all t_j grow.
Likewise, fresh gaps with thresholds a_j satisfying
`t_j a_j-2N^2 log(1+4Nt_j)->infinity` have total probability tending to
zero. Persistent roughness with no priced gap therefore has probability
tending to one on positive-measure input tubes. This disproves a
coupling-uniform finite-window return probability on **all real inputs**
under the unweighted forward law. It does not prove the same for an
isolated singleton with a uniformly good collar, an extracted operator,
or an original-weighted law. The original filled-sector action is exactly
what pays for this class in (P2)–(P7). Source: RENEW lines 147–300.

### F4. A small failed component need not admit the proposed completion

JMBRA lines 564–622 constructs one bad interior mark g in a block Q
and a second g on an exterior crossing link in N_1(Q). The latter
creates a plaquette wholly in N_1(Q), independent of I(Q), with distance
two from identity, while no new block interior becomes bad. Consequently
the bad component is the singleton {Q}, yet every completion has
e_flat>=2. Small perturbations preserve all strict inequalities, giving
positive original-chain measure at finite couplings and fixed real V.
This refutes deleting the completion-failed singleton on size grounds.
It supplies no lower bound precluding a charge from its rough exterior
plaquette. That charge, merger or other controlled disposition is required.

### F5. Two explicit majorants fail, without proving actual divergence

* In the direct Haar expansion `f_p=exp(-u_0 s_p)-1`, setting one
  plaquette link to g gives s_p=4/N. Therefore
  `sup|f_p|>=1-exp(-4u_0/N)` and its RGA16 contribution is at least
  `exp(mu+2)(1-exp(-4u_0/N))`, eventually greater than 1/4. The real
  seminorm contains its value term, so adding derivatives cannot repair
  this **particular** majorant. JMBRA A23a, lines 473–487.
* The unconditional seam envelope costs `2u P+4kappa u C` for P changed
  plaquettes and C changed kernels. If P+C>0 and these crude costs are
  charged against a sublinear raw price c u^delta, delta<1, their
  difference tends to minus infinity. This fails to certify smallness;
  it is not an asymptotic lower bound on the actual seam free energy.
  JMBRB B23–B24, lines 381–411.

Finally, a hard cut involving a retained variable is discontinuous across
its nontrivial boundary and hence is not C^6 there. REALRGA lines 304–312
requires an exact sum, smooth partition with boundary terms, or a legitimate
fixed-domain construction. An interior-only estimate cannot certify jets
across that boundary. This is a regularity obstruction for that chosen
atom/domain, not a no-go for the real representation.

## 5. What a viable inherited mixed-reader estimate must still prove

The weighted alternative already has a precise real use. Suppose the
**same complete integrated mixed-jet estimate** supplies core weights
a_gamma on full supports D_gamma and reader weights alpha_i on H_i.
At target rate sigma, define

    q=sup_x sum_(i:x in H_i)
                    exp[(sigma+1+eta)|H_i|]alpha_i,
    d=sup_x sum_(gamma:x in D_gamma)
                    exp[(sigma+1)|D_gamma|]a_gamma,
    q<1/2, q+d<=1/2.                                    (P14)

Assume exact coefficient factorization over complete overlap components.
Then core-containing integrated groups satisfy

    ||W_core||_sigma<=d/(1-2q),
    ||W_core,extent>=r||_sigma<=exp(-eta r)d/(1-2q).     (P15)

The derivation is the first rooted-tree estimate: multiply all core
weights by `R=(1/2-q)/d>=1` and all reader weights by exp(eta|H_i|).
The input budget becomes 1/2, so the full-output-root tree bound is
1/2. Each core-containing group gains at least R; divide by R. If d=0
every such term is zero. A group reaching distance r outside its cores
uses reader supports with total size at least r, so undoing their extra
weight gives exp(-eta r). This counts roots in tails and inactive regions.
REALRGA RGA8 supplies the needed product inequality for real jets;
JMBRA A14–A18, lines 312–382, supplies this weighted construction.

The unproved antecedent is not a marginal source/event bound. It is
RGA14 for every complete selected overlap group on the actual reference,
including all differentiated densities, normalization, selectors and
regulator multiplicities. Actual local original charges must be allocated
disjointly; inherited rho_h cannot be priced by b_j while its compensating
J_h is left uncontrolled. Tail weights and their original-reader incidence
must be evaluated. After that, the remaining gas budget must meet RGA16
(for example Q_sf+d/(1-2q)<=1/4 at sigma=mu+2).

CHARGE's lifetime sum and fixed-terminal accumulation are also different:
`sup_j sum_r ||C_(j+r-1)...C_j A_j||` does not by itself bound
`sup_k sum_(j<=k) ||C_(k-1)...C_j A_j||`. A common summable age envelope
a_r proves both by reindexing; an unnormalized creation price alone is
not a homogeneous operator contraction. See CHARGE lines 488–536.

## 6. Disposition for the parent lane

| Contract part | What this report establishes | Surviving obligation |
|---|---|---|
| H0 | Actual unnormalized history accounting and shared-envelope source identities; exact full-reader integration carries. | A uniformly local admissible representation and complete complements. |
| H1 | Fixed original-source derivatives, every labelled subset, and fixed-domain regularity conditions remain explicit. | Full p=6 mixed jets for retained variables and all masks/charts. |
| H2 | One-use CHARGE reserve and filled-sector history-summed source prices (P6)–(P8). | Local mixed regulator/jet prices on the actual inherited reference, especially thin/isolated histories. |
| H3 | Weighted-reader conclusion (P15) is a valid conditional real interface. | Actual alpha_i, a_gamma and their full rooted sums; local normalizer and prefactor budgets. |
| H4 | No extracted output estimate is supplied here. | Actual Loc, relevant recursions and irrelevant output bounds. |
| H5 | Explicit classes prevent using automatic forward smoothing or repricing normalized mass. | Extracted coherent continuation or common creation/accumulation envelope; all completion failures. |
| H6 | All finite labelled source subsets and history-mass derivatives are retained. | Outer cumulance estimates, all-order hierarchy, matching and consumer modules. |

Suggested carry-over refinements: CHARGE C5–C12 CARRIES at its extensive
real scope, now with the proved finite source-subset extension above;
JMBRA A3–A12 CARRIES as exact algebra, A14–A18 as real norm-algebra
implications with actual mixed input OPEN; JMBRA A19–A23b CARRIES at
its precise survival/support scope; JMBRB B-GAP/B-GEOM CARRIES only for
fresh forward events and the smooth-input branch, B-MASS CARRIES;
RENEW's coherent family CARRIES at finite horizon and fixed-volume
weak-coupling limit. No row is promoted to an all-history estimate.

## 7. Negative-claim scope check

N1: Tested mechanisms are normalized transport/conditioning, exact
coherent forward propagation, and the two explicit majorants. Adapted
local references, original remaining-credit bounds, weighted tails and
extracted continuation remain live; there are not five exhausted families
and no negative-packet PASS is claimed. N2: No independence or wall count
is asserted; a single successful mixed reference construction could pay
several listed costs. N3: Fixed source-independent selectors, finite
horizon, complete supports, actual charge fractions and CHARGE's coupling/
cut assumptions are explicit above. N4: Every witness attacks its own
named normalized law, support claim, completion rule or majorant; none is
substituted for the unnormalized R_h/Z_A estimate. N5: The claims range
from one event to finite filled towers, with no continuum/spectral or
all-route conclusion. N6: The live repairs are mathematical constructions,
not new physical axioms. N7: The strongest contrary route is to retain
original history mass, construct a local paired reference cancelling
C13's extensive debit, then price the complete mixed jets and extract
the coherent remainder; nothing above excludes it. N8: The consumed
JMBRA/JMBRB/RENEW/CHARGE notes already preserve these distinctions. The
search scope here is those exact sources and REALRGA, not an exhaustive
repo or literature search. This report is an author-support result and
does not certify a negative-claim landing packet.
