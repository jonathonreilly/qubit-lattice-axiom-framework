# PRE-STATED

UTC: 2026-10-28 22:59:37. Independent hostile review of Finding X1 in
`REVIEW55_TENT.md`, locating string `### X1 — Root charges of composite-co-closed
sources are data.` This entry is written after reading X1 and before inspecting
its supporting theorems or the earlier refutation. No verdict is assumed.

Refutation criteria fixed in advance:

1. An admissible composite-co-closed source whose root demands violate neutrality
   or a necessary coarse-torus capacity cut, or an incorrect placement/flux
   identity or scale factor essential to the proposed cut bound.
2. A mismatch between the current response and the datum response, or an unmet
   hypothesis of LINEAR_PACKAGE Theorem 4.2/4.2′ (norm, scale, level, gauge,
   support, or uniformity). A pointwise kernel bound alone will not be treated as
   a uniform operator bound without checking its summation measure and scale.
3. A subtracted source outside Theorem COF's precise hypothesis class, including
   residual-slot, gauge, norm, or cancellation requirements.
4. A surviving valid counterexample from S10-11/COF-res to the claimed curvature
   bound. A large term in a representation is not by itself a counterexample
   without control of its complement.
5. Failure of linear superposition for the actual minimisers, constraints, and
   observable used by X1.

A false algebraic identity or an explicit counterexample warrants REFUTED for
that assertion. Missing justification or an unverified theorem hypothesis
warrants NOT-VERIFIED, without claiming a counterexample to the underlying
estimate. CONFIRMED requires a traceable argument with all relevant hypotheses.
Every substantive verdict will identify a file and locating string. Numerical
checks, if useful, will use exact integers/rationals only. Only this file will be
written; no git operations will be used.

## Review scope and decision

**X1's mathematical core is CONFIRMED as a conditional implication: the
unweighted supremum half of (CO-fun) holds on the stated composite-co-closed
source class.** The cited data theorem applies. There is an explicit bounded
coarse current, so the argument does not need a max-flow existence theorem.
The top residual can be handled without losing the stated source-norm scale.

Two qualifications are necessary before banking the wording:

- Define N as the **source-class norm**, excluding the response-dependent top
  residual term. If N denotes the entire displayed right side of COF, X1's
  particular comparison of N(S') with N(S) is **NOT-VERIFIED** as written.
  This does not obstruct the sup theorem: COF's proof (a)-(c) already gives the
  source-only sup bound.
- The result reverses S10-11's alleged **sup obstruction**. It does not establish
  the Hölder half, and therefore does not by itself prove the full statement
  whose wording is “(CO-fun) as stated.” Its downstream scope must remain
  “supremum estimate on composite-co-closed sources.”

Source under review: [REVIEW55_TENT.md](REVIEW55_TENT.md), locating string
“### X1 — Root charges of composite-co-closed sources are data.”
The dependency statements were checked in the local files named below,
including the frozen proof ranges behind LP 4.2/4.2′. Their entire underlying
proof packages were not independently re-audited. This is a review of the
claimed implication, accepting those two theorem inputs at their stated scope,
not a new certification of the Yang–Mills proof or of scientific status on main.
No git operation, source correction, status promotion, or write outside this
report was made.

All numerical work below used integers and Python Fraction. Exponential
summability is used symbolically; no decimal estimate of a strip rate or
kernel constant is imported.

## 1. The actual divergence, including the top residual

**CONFIRMED:** the top residual contributes a root divergence. The older
unqualified assertion that every residual-slot collection has D = 0 is
**REFUTED**.

Sources: [BFT_A.md](BFT_A.md), “7.1 Setting LIN” and “Transposing (b) for one
step”; [BFT_B.md](BFT_B.md), “27.1 Definitions used below,”
“34.1 Definitions used below,” and “35.2 Lemma SPLIT”;
[REVIEW55_TENT.md](REVIEW55_TENT.md), “### X-T7”.

Write s_* = s_{k-1}, s_{-1} = 0, and let I_l = ev^{(0→l)T} denote placement
on level-l roots in the fine lattice. At B_k = 0 the actual level-l linear
source is

$$
S_l=j_l+d_l^*G_l+Q_l^Ts_l-s_{l-1},\qquad 0\le l<k.
$$

Using d_l^*Q_l^T = ev^{(l→l+1)T}d_{l+1}^*, internal residual terms telescope.
There is no variable at level k to supply a cancelling -s_* term. Thus

$$
D(S)=\sum_{l<k}I_l d_l^*j_l+I_k d_k^*s_* . \tag{1}
$$

The G terms vanish because d^*d^* = 0. An explicit counterexample to the old
SPLIT assertion is s_* = one oriented coarse-bond unit current, all other
slots zero, on T ≥ 2. Its D is +1 at the head root and -1 at the tail root.
It is composite-co-closed but is not strictly (CC-0).

X1 explicitly mentions the X-T7 repair, so this is not a refutation of X1.
The construction below implements that repair with a controlled norm.

## 2. Every cut is controlled; an explicit current proves more than max-flow

**CONFIRMED**, including neutrality, periodic cuts, and winding parts.

Sources: [REVIEW55_TENT.md](REVIEW55_TENT.md), X1 “(1) **Cut bound**” and
“(2) **Gale-Hoffman**”; [LINEAR_PACKAGE.md](LINEAR_PACKAGE.md),
“1.1 Lattices, levels, torus”; [BFT_B.md](BFT_B.md),
“Coarse plain unit” and “Strict composite co-closedness (CC-0)”.

Let N_l = L^{k-l}. In level-l coordinates the level-k block indexed by X is

$$
B_l(X)=N_lX+\{0,\ldots,N_l-1\}^4
$$

with the coordinates taken periodically. Define a coarse current from the
actual outward face flux of j_l:

$$
(F_lj_l)_\mu(X)=
 \sum_{\substack{z\in B_l(X)\\
 z_\mu=N_lX_\mu+N_l-1\ {\rm mod}\ TN_l}}
 (j_l)_\mu(z).
$$

The divergence convention is incoming minus outgoing, as in BFT_A's
“28.10 Lemma BOG.” Internal bonds cancel exactly, giving

$$
d_k^*F_lj_l(X)=\sum_{z\in B_l(X)}d_l^*j_l(z),\qquad
\|F_lj_l\|_\infty\le N_l^3\|j_l\|_{\infty,\rm own}=\pi_l(j_l). \tag{2}
$$

The root placements are compatible with these nested blocks. Summing (1)
over the fine block of X, and using D(S) = I_k q, therefore gives

$$
q=d_k^*(a+s_*),\qquad
a:=\sum_{l<k}F_lj_l.
$$

Consequently choose, explicitly,

$$
b:=a+s_*,\quad
c_j:=\sum_{l<k}\pi_l(j_l),\quad
c:=c_j+\|s_*\|_\infty .
$$

Then

$$
d_k^*b=q,\qquad \|a\|_\infty\le c_j,\qquad \|b\|_\infty\le c. \tag{3}
$$

For every subset A of coarse vertices, summing d^*b over A gives its signed
boundary flux. Hence

$$
\left|\sum_{X\in A}q_X\right|
 \le \sum_{e\in\partial A}|b_e|
 \le c\,|\partial A|. \tag{4}
$$

This establishes the source-dependent cut bound and constructs a feasible
current without invoking Gale–Hoffman. In particular it proves the relevant
negative-divergence norm estimate
inf_{d^*v=q} ||v||_infinity ≤ c. A pointwise bound on q alone would not imply
this uniformly in T; the source's actual face fluxes supply the extra
information.

Edge cases and topology:

- The whole-torus cut gives sum q = 0, also directly from (1). No non-neutral
  demand is admitted.
- For T = 2, retain the distinct periodic bonds as a multigraph. Counting only
  one edge between a pair of neighbouring vertices would give the wrong cut
  capacity. Formula (2) uses the actual lattice bonds.
- For T = 1, coarse bonds are self-loops and d^*b = q = 0. The construction is
  still defined; a nonzero b can be purely winding.
- Divergence does not prescribe harmonic/winding currents. None needs to be
  eliminated: LP accepts arbitrary b as data. The construction may retain
  such currents, and (3) controls them as well.
- No bound on a path length or on the volume of A was used. The only face
  count is N_l^3, exactly the factor in pi_l. There is no hidden T loss.

This is an independent constructive derivation of X1's first two steps.
It also chooses b in a way useful for the top-residual bookkeeping below.

## 3. The datum identification and every relevant LP hypothesis

**CONFIRMED:** U(b), the plain current Q_{k-1}^T b in the top unknown slot,
has the same fine-curvature response as the source-free datum
B_k = b/kappa_{k-1}.

Sources: [BFT_A.md](BFT_A.md), “7.1 Setting LIN”;
[LINEAR_PACKAGE.md](LINEAR_PACKAGE.md), “1.3 The soft normalised kernel,”
“1.4 Norms,” “Theorem 4.2 (N2-exp” and “Theorem 4.2' (N2-exp'”;
[PROOF_session16_snapshot.md](PROOF_session16_snapshot.md),
“Theorem N2-exp (exponential locality of the linearised soft chain)” and
“m_*' := min”.

Put kappa = kappa_{k-1}. The equality is an equality of energies in the same
unknowns x_0,...,x_{k-1}:

$$
E_{\rm SC}(x;b/\kappa)
 =E_{\rm SC}(x;0)-\langle Q_{k-1}^Tb,x_{k-1}\rangle
       +\frac{\|b\|_2^2}{2\kappa}. \tag{5}
$$

Thus the minimisers, and n^2 d x_0, coincide. There is no missing factor of
L or n: b is a level-k 1-form and kappa is the coefficient of that last
quadratic term. The top residual *observable* changes when the datum changes;
the curvature observable does not.

The hypotheses match as follows.

| Issue | Check |
|---|---|
| Level | B_k is exactly the level-k datum of Setting SC; U(b) is at level k-1. |
| Norm | At m = 0, LP's data norm is the ordinary coarse sup norm. The theorem gives a kernel estimate, from which its operator bound follows below. |
| Background and linearity | Both energies are the real, abelian linearisation at the trivial background. |
| Gauge/slice | The f_0 output is gauge invariant. Theorem 4.2 is not restricted to the separate “Phys” gap slice. No condition h(B_k) = 0 is imposed on the data. |
| Mean, divergence | The data need not be co-closed or zero-mean. The co-closed, zero-mean *source* convention in LP §1.3 is not a restriction on the source-free data map. |
| Support | No compact-support or localization hypothesis on B_k occurs in 4.2. |
| Parameters | Fix L and 0 < kappa_- ≤ kappa_i ≤ kappa_+ < infinity. The statement is uniform in k ≥ 1, T, and fine offset u. |
| Rate | Choose a fixed 0 < m' < m_* (or use 4.2′ and its own constants). The frozen N2-exp statement explicitly includes m_* > 0. No measured rate is needed. |

Here is the necessary kernel-to-operator calculation. At a fixed output
plaquette orientation and fine offset u, the input index is a coarse site Z
and one of four link orientations mu. There is **no sum over fine offsets**.
For the periodized kernel,

$$
\begin{aligned}
\sup_{X,u}\sum_{Z\in\Lambda_k}\sum_{\mu=1}^4
 |K_{T,u}^{\mu}(X-Z)|
&\le 4M\sum_{W\in\mathbb Z^4}e^{-m'|W|_1}\\
&=4M\left(\frac{1+e^{-m'}}{1-e^{-m'}}\right)^4
=:C_D<\infty .
\end{aligned} \tag{6}
$$

Periodization makes the sum over Z and periodic images a single sum over
Z^4, independent of T. Uniformity in u prevents an n-dependent supremum.
Therefore

$$
\|f_0[U(b)]\|_\infty\le C_D\|b\|_\infty/\kappa. \tag{7}
$$

C_D must mean this summable-row constant, not the entrywise constant M alone.
The replacement is a constant depending only on the fixed package parameters.
A requirement that b have a uniformly bounded exponentially weighted norm
has not been smuggled in: the output being proved is unweighted.

As a separate consistency check, LP's “Theorem 3.8 (N2-lin, sup forms)” states
the f_0 estimate for every B_k in terms of sup|dB_k|; the exact inequality
sup|dB_k| ≤ 4 sup|B_k| also gives a bound of the form (7).
A constant harmonic datum is represented by x_i = L^{i-k} B_k, with zero
curvature and zero data-relative residuals, so winding does not invalidate
the data theorem.

## 4. The remainder is in COF's class, with a precise norm convention

**CONFIRMED** for the following representation of S' = S - U(b).
**NOT-VERIFIED** for X1's literal N-comparison if N includes the
response-dependent residual on COF's displayed right side.

Sources: [REVIEW55_TENT.md](REVIEW55_TENT.md), X1 “(3) **Subtract a data-type
current**” and its displayed N(S') inequality; [BFT_B.md](BFT_B.md),
“35.5 Theorem COF,” especially proof (a)-(c) and “Honest scope” item (4);
[BFT_A.md](BFT_A.md), “7.2 Norms” and “8.2 BL-2”.

Use the explicit b = a + s_* from (3), rather than an unspecified feasible
flow. A slot representation of S' is

$$
j'_{k-1}=j_{k-1}-Q_{k-1}^Ta,\qquad s'_{k-1}=0,
$$

with every G_l, every j_l for l < k-1, and every s_l for l < k-1 unchanged.
Indeed the removed top residual Q^T s_* and the subtracted plain current
Q^T a together are exactly U(b). By (1)-(3) and transposed root covariance,

$$
D(S')=I_k(q-d_k^*b)=0. \tag{8}
$$

Now every remaining residual slot is an internal, telescoping slot and has
D = 0. Every G slot has D = 0. Thus the *plain collection* in this
representation also has D = 0. COF's slot splitting and its use of the
co-closed assembled plain current are legitimate. This handles the gap in
SPLIT without assuming a non-co-closed top residual is strictly co-closed.

No further hypothesis is lost: B_k remains zero in the source problem;
m = 0 and the trivial background are unchanged; fix 0 < alpha < theta < 1;
the existing G regularity and R norms remain controlled. The P0 and Pl-c
classes impose the displayed sup/level-weight norms, not a support or a
level-wise divergence constraint. A possibly globally supported top current
is therefore permitted. When k = 1 it goes into P0; for k ≥ 2 it goes into
Pl-c.

For clarity define the source-only norm

$$
\mathcal N_{\rm src}(S):=
 \|G_0^c\|_\infty+[G_0^c]_\alpha+
 \pi_0(j_0)+\|j\|_{Pc}+\|G\|_Y+\|s\|_R, \tag{9}
$$

using COF's conventions for the G seminorm. The empty Pc norm at k = 1 is
zero. COF proof (a)-(c) gives

$$
\|f_0(S')\|_\infty\le C_0\mathcal N_{\rm src}(S'), \tag{10}
$$

with C_0 independent of k,T. This is not an unjustified deletion of a term
from the theorem statement: its “Honest scope” item (4) explicitly says that
the extra kappa_+ ||r^c_{k-1}|| term is needed only in (d), the Hölder step.

Because the h paths stay inside one block, each fine link receives an h^T
contribution from at most one block. If w is its maximum absolute kernel
entry, then

$$
\|Q^Ta\|_{\infty,\rm own}
 \le (L^{-3}+2d\,w)\|a\|_\infty,\qquad
\pi_{k-1}(Q^Ta)\le A_L\|a\|_\infty,\quad
A_L:=1+2dL^3w. \tag{11}
$$

For the actual order-averaged S4' map at d = 4, L = 3, the independent exact
contour enumeration below gives w = 10/81 and A_L = 83/3.
For general fixed L the finite one-block coefficient supplies a finite A_L.

Set gamma_k = 1 when k = 1 and gamma_k = L^theta when k ≥ 2. The top Pc
weight is L^theta, not L^{theta k}. The triangle inequality for the Pc
maximum and the decrease of the R norm give

$$
\mathcal N_{\rm src}(S')
 \le\mathcal N_{\rm src}(S)+\gamma_k A_L c_j
 \le\mathcal N_{\rm src}(S)+L^\theta A_L c. \tag{12}
$$

The choice b = a+s_* is useful: the correction to the *plain* slots is Q^T a,
not Q^T b plus an independently charged Q^T s_*.
An arbitrary max-flow output would not automatically give this same
bookkeeping.

**The ambiguity if N is the full COF right side.** Let
N_full(S) = N_src(S) + kappa_+ ||r_{k-1}(S;0)||_infinity. For the response to
U(b), the top residual evaluated at zero datum is

$$
r_{k-1}(U(b);0)=b/\kappa+r_{k-1}^{\rm data}(b/\kappa).
$$

It is not the data-relative residual alone. With C_{D,r} the row-sum
constant for LP's B_k-to-r_{k-1} kernel, the immediate justified comparison is

$$
N_{\rm full}(S')
\le N_{\rm full}(S)+\gamma_k A_L c_j
 +\frac{\kappa_+}{\kappa}(1+C_{D,r})c. \tag{13}
$$

X1 does not supply the last term if its N was meant to include the response
residual. I have not established its particular sharper inequality in that
interpretation and do not label it false without a counterexample.
Equations (9)-(12) avoid the issue and prove the claimed sup result directly.

## 5. Superposition is valid in the actual setting

**CONFIRMED.**

Sources: [BFT_A.md](BFT_A.md), “26.0”/“Composite gauge map,”
“26.2”/“Lemma FG (gauge-fixed responses),” and
“28.9 Lemma FG: PROVEN-HERE (linear algebra)”;
[REVIEW55_TENT.md](REVIEW55_TENT.md), X1 “(5) Linearity”.

The common Hessian H is the fixed quadratic-chain Hessian with top datum
zero. Its kernel is the composite gradients whose level-k root values are
constant. Root-supported neutral D annihilates that kernel. Thus S, U(b)
and S' all lie in the solvable source space. On the quotient by Ker H the
minimizer is linear in the source. Equivalently fix the same linear gauge
Gamma and use the same operator (H+Gamma^T Gamma)^{-1} for all three.

It follows exactly that

$$
f_0(S)=f_0(S')+f_0(U(b)). \tag{14}
$$

The data problem in (5) has the same Hessian on the same unknowns. Its
different top datum is a linear forcing plus a constant, so it introduces
no change of slice or of operator into (14). The explicit flux choice is
itself linear in the original source slots; even a nonlinear choice of
feasible flow would not invalidate superposition for the resulting fixed
source decomposition.

None of this asserts superposition of the nonlinear Yang–Mills equations
or of nonlinear fixed-point iterates.

## 6. Why S10-11 concluded FALSE, and why that argument does not survive

**REFUTED:** S10-11 as a proof of failure of the sup estimate.
**CONFIRMED:** the transposed funnel identity for the defect term.
**NOT-VERIFIED by this review:** either truth or falsity of the full
sup-plus-Hölder statement.

Sources: [REVIEW_BFT_B_S9_S10.md](REVIEW_BFT_B_S9_S10.md),
“S10-9 Proposition COF-res,” “S10-10,” “S10-11,” and “RS10-6 (binding)”;
[BFT_B.md](BFT_B.md), “35.7 Proposition COF-res” and
“Why this makes (CO-fun) as stated FALSE”;
[REVIEW_BFT_A_S8.md](REVIEW_BFT_A_S8.md), “S8-5 Proposition RF” and
“Why the conclusion survives, exactly and with no stand-in”.

The old reasoning was:

1. The root funnel pairing carries n^2 q times a purported order-one funnel
   value.
2. A top plain source permits q of order L^{-3} pi_{k-1}.
3. Therefore a term can be of order L^{2k-3} pi_{k-1}, so (CO-fun) is false.

The invalid inference is from a large term in a representation to a lower
bound on the **whole** response. S10-10, immediately before S10-11, already
records that the complementary terms are not controlled when D is nonzero.
In particular, the straight-push-down main term was not proved co-closed,
so the representative change used in COF's sup proof could not be applied
to it. RS10-6 explicitly requires keeping the additional
<D^root, lambda_opt> contribution or proving the missing cancellation.
S10-11 did not discharge that requirement before declaring a counterexample.

Two further evidentiary problems remain in the alleged lower bound:

- Neutrality requires at least a compensating charge. The signed response
  sees a difference of funnel values, not an isolated root value.
- The exact 17/243 ratio and -65/26244 value used in the cited S8 material
  concern a constructed test field u = (1/8)d^*delta_p. They do not by
  themselves prove the required lower bound, for every depth, on the actual
  chain response Y^p and its neutral root pairing.

X1 does not merely point out these gaps. It supplies a different uniform
upper bound on the full response. For example take a coarse bond current b
and S = U(b). Its source norm is bounded by gamma_k A_L ||b||_infinity,
uniformly in k, and (7) bounds its full curvature. If a chosen funnel term
for this family grows, the rest of that representation must cancel it.

The cancellation issue can be seen without any estimate. For the plaquette
response Y^p with Y_k = 0, duality gives

$$
\begin{aligned}
f_0[U(b)](p)
&=n^2\langle b,Q_{k-1}Y^p_{k-1}\rangle\\
&=n^2\left[
 \langle b,Q_{\rm str}^{(0→k)}Y^p_0\rangle
 -\langle d^*b,\Phi_k(Y^p_0)\rangle
 -\sum_{m<k-1}
   \langle (Q^{(m+1→k)})^Tb,r_m(Y^p)\rangle
 \right].
\end{aligned} \tag{15}
$$

This uses only residual telescoping and Q^{(0→k)} =
Q_str^{(0→k)} - d Phi_k. The funnel pairing is one summand, with its sign
fixed here by that identity. Its magnitude is not a lower bound on the
left side. LP controls the entire left side.

The algebra in COF-res identifying the transposed defect with a root/funnel
pairing remains valid. Its description as the “single extra term” with
every other contribution already bounded is not licensed. The original
review's CONFIRMED label cannot substitute for the missing lower bound.

Thus the advertised *sup refutation* must be withdrawn, conditional on the
two accepted theorem inputs. It would still be logically incorrect to
infer the full Hölder estimate from this reversal.

## 7. Independent exact diagnostics

The following are **post-derivation diagnostics**, not a claim that finite
tests prove k- or T-uniformity. The general proofs are (1)-(15).

A fresh implementation enumerated the actual 24 coordinate orders and all
81 offsets of the L = 3 block. Q^T was built from the complete root contours,
rather than from the identity Q_str^T - h^T d^* being checked. No old lane
runner or floating-point solver was used. The one-block checks include
T = 1 self-loops and T = 2 parallel periodic bonds. A depth-two example
includes nonzero internal residual sources and a non-co-closed top residual.

Observed output from the in-memory Python run:

~~~text
Exact contour enumeration: d=4, L=3; h max = 10/81 ; A_L = 83/3
One-link covariance, face-flux right inverse, and sup bound: 12 cases; T=1,2,3; all exact
k=2, T=2: internal residual cancellation and root placement exact; nonzero root charges = 3
k=2: b=a+s_top; a=v; divergence matching and strict remainder exact
Capacity: ||b||_inf = 3/7 ; c_j = 3353/55 ; c = 23636/385
All 65536 coarse-torus cuts: exact; maximum |q(A)|/|boundary A| = 29/280
Energy identity with kappa=5/3: defect = 0 ; constant = 1263/12250
~~~

The cut enumeration is exhaustive for this one 16-vertex torus demand,
not for all sources. The energy check tests the exact datum/source
identification, not a numerical estimate of an inverse Hessian. The
positive LP strip rate and uniform COF constant remain named theorem
inputs, not outcomes of these diagnostics.

For reproducibility, the complete script executed through Python standard
input is embedded here; it creates no file:

~~~python
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, permutations
d, L = 4, 3
orders = list(permutations(range(d)))
offsets = list(product(range(L), repeat=d))
root = (1,)*d
den = len(orders)*len(offsets)

def path(a, z, order):
    x = list(a)
    for mu in order:
        while x[mu] != z[mu]:
            sign = 1 if x[mu] < z[mu] else -1
            if sign < 0:
                x[mu] -= 1
            yield (tuple(x), mu), sign
            if sign > 0:
                x[mu] += 1

hcounts = defaultdict(int)
qcounts = [defaultdict(int) for _ in range(d)]
for order in orders:
    for y in offsets:
        p = list(path(root, y, order))
        for edge, sign in p:
            hcounts[edge] += sign
        for mu in range(d):
            out = qcounts[mu]
            for (z, nu), sign in p:
                out[z, nu] += sign
                zz = list(z); zz[mu] += L
                out[tuple(zz), nu] -= sign
            z = list(y)
            for _ in range(L):
                out[tuple(z), mu] += 1
                z[mu] += 1
h = {e:F(v,den) for e,v in hcounts.items() if v}
qt = [{e:F(v,den) for e,v in row.items() if v} for row in qcounts]
wmax = max(map(abs,h.values()))
A = 1 + 2*d*L**3*wmax
assert wmax == F(10,81)
assert A == F(83,3)

def add(*terms):
    out = defaultdict(F)
    for scale, data in terms:
        for key, value in data.items():
            out[key] += scale*value
    return {key:value for key,value in out.items() if value}

def transpose(v, T):
    out = defaultdict(F)
    M = L*T
    for (X, mu), value in v.items():
        for (z, nu), weight in qt[mu].items():
            key = (tuple((L*X[a]+z[a])%M for a in range(d)),nu)
            out[key] += value*weight
    return {key:value for key,value in out.items() if value}

def divergence(v, M):
    out = defaultdict(F)
    for (z,mu),value in v.items():
        head = list(z); head[mu] = (head[mu]+1)%M
        out[z] -= value
        out[tuple(head)] += value
    return {key:value for key,value in out.items() if value}

def place(f):
    return {tuple(L*z[a]+1 for a in range(d)):value for z,value in f.items()}

def flux(v, side):
    out = defaultdict(F)
    for (z,mu),value in v.items():
        if z[mu]%side == side-1:
            out[tuple(a//side for a in z),mu] += value
    return {key:value for key,value in out.items() if value}

def sup(v):
    return max(map(abs,v.values()), default=F(0))

basis_count = 0
for T in (1,2,3):
    for mu in range(d):
        v = {((0,)*d,mu):F(1)}
        j = transpose(v,T)
        assert divergence(j,L*T) == place(divergence(v,T))
        assert flux(j,L) == v
        assert L**3*sup(j) <= A*sup(v)
        basis_count += 1

T = 2
v = {((0,0,0,0),0):F(2,5)}
t = {((1,0,0,0),1):F(-3,7)}
u = {((2,1,1,1),0):F(5,11), ((0,2,2,1),3):F(-1,13)}
s = {((3,0,1,2),2):F(7,17)}
j0 = transpose(u,L*T)
j1 = add((-1,u),(1,transpose(v,T)))
S0 = add((1,j0),(1,transpose(s,L*T)))
S1 = add((1,j1),(-1,s),(1,transpose(t,T)))
D = add((1,divergence(S0,L*L*T)),(1,place(divergence(S1,L*T))))
q = divergence(add((1,v),(1,t)),T)
assert D == place(place(q))
a = add((1,flux(j0,L*L)),(1,flux(j1,L)))
b = add((1,a),(1,t))
assert a == v
assert divergence(b,T) == q
cj = L**6*sup(j0) + L**3*sup(j1)
c = cj + sup(t)
assert sup(b) <= c
j1r = add((1,j1),(-1,transpose(a,T)))
S1r = add((1,j1r),(-1,s))
assert add((1,S1r),(1,transpose(b,T))) == S1
assert add((1,divergence(S0,L*L*T)),(1,place(divergence(S1r,L*T)))) == {}
assert L**3*sup(j1r) <= L**3*sup(j1) + A*sup(a)

verts = list(product(range(T), repeat=d))
vid = {z:i for i,z in enumerate(verts)}
edges = []
for X in verts:
    for mu in range(d):
        Y = list(X); Y[mu] = (Y[mu]+1)%T
        edges.append((vid[X],vid[tuple(Y)]))
charges = [(vid[X],int(35*value)) for X,value in q.items()]
capnum = int(35*sup(b))
maxratio = F(0)
for mask in range(1<<len(verts)):
    charge = abs(sum(value for i,value in charges if (mask>>i)&1))
    cut = sum(((mask>>i)&1) != ((mask>>j)&1) for i,j in edges)
    assert charge <= capnum*cut
    if cut:
        maxratio = max(maxratio,F(charge,35*cut))

kappa = F(5,3)
def xvalue(z,mu):
    return F(sum((a+1)*z[a] for a in range(d))+2*mu-7,19)
qxs = {}
for X in verts:
    for mu in range(d):
        qxs[X,mu] = sum(weight*xvalue(tuple((L*X[a]+z[a])%(L*T) for a in range(d)),nu)
                            for (z,nu),weight in qt[mu].items())
B = {edge:value/kappa for edge,value in b.items()}
Ezero = sum(kappa*value*value/2 for value in qxs.values())
Edata = sum(kappa*(value-B.get(edge,F(0)))**2/2 for edge,value in qxs.items())
pair = sum(value*xvalue(z,mu) for (z,mu),value in transpose(b,T).items())
constant = sum(value*value for value in b.values())/(2*kappa)
energy_defect = Edata-Ezero+pair-constant
assert energy_defect == 0
print("Exact contour enumeration: d=4, L=3; h max =",wmax,"; A_L =",A)
print("One-link covariance, face-flux right inverse, and sup bound:",basis_count,"cases; T=1,2,3; all exact")
print("k=2, T=2: internal residual cancellation and root placement exact; nonzero root charges =",len(q))
print("k=2: b=a+s_top; a=v; divergence matching and strict remainder exact")
print("Capacity: ||b||_inf =",sup(b),"; c_j =",cj,"; c =",c)
print("All",1<<len(verts),"coarse-torus cuts: exact; maximum |q(A)|/|boundary A| =",maxratio)
print("Energy identity with kappa=5/3: defect =",energy_defect,"; constant =",constant)
~~~

## 8. Exact statement that can be banked

**CONFIRMED, conditional on the cited COF and LP theorem inputs.**

Fix d = 4, odd L ≥ 3, 0 < kappa_- ≤ kappa_i ≤ kappa_+ < infinity, and
0 < alpha < theta < 1. At the trivial background and m = 0, for every
integer k ≥ 1 and coarse torus side T ≥ 1, let S be a Setting LIN^cc
source with B_k = 0 in the P0, Pl-c, G and R classes. Use N_src from (9).
Then its gauge-invariant fine-curvature response satisfies

$$
\boxed{
\|f_0(S)\|_\infty
 \le C_0\bigl(\mathcal N_{\rm src}(S)+\gamma_k A_L c_j\bigr)
       +\frac{C_D}{\kappa_{k-1}}
          \bigl(c_j+\|s_{k-1}\|_\infty\bigr).
} \tag{16}
$$

Here gamma_1 = 1, gamma_k = L^theta for k ≥ 2,
c_j = sum_{l<k} pi_l(j_l), and A_L is (11), equal to 83/3 at L = 3
for the order-averaged S4' map. C_0 is the COF sup constant from proof
(a)-(c), and C_D is the row-sum constant (6). All are independent of k,T.

The level weights make the extra cost summable:

$$
c_j\le \pi_0(j_0)+\frac{\|j\|_{Pc}}{L^\theta-1},
\qquad
\|s_{k-1}\|_\infty\le L^{-\theta}\|s\|_R. \tag{17}
$$

For instance, with
C_c = max{1, (L^theta-1)^{-1}, L^{-theta}},
(16) implies

$$
\boxed{\quad
\|f_0(S)\|_\infty\le
 \left[C_0(1+L^\theta A_L C_c)+
       \frac{C_D C_c}{\kappa_-}\right]\mathcal N_{\rm src}(S).
\quad} \tag{18}
$$

This is the supremum half of (CO-fun), indeed with no response-residual
term needed on its right side. The proof is the explicit flux decomposition,
COF on the strictly co-closed remainder, LP on the data part, and
superposition. Sources and locating strings for every step are in §§1-6;
the target is [BFT_B.md](BFT_B.md), “The named open item (CO-fun), stated
precisely,” and [REVIEW55_TENT.md](REVIEW55_TENT.md), “### X1”.

For this specific estimate, TENT-Q, TENT-osc, face (b), the G_e sign,
FACEB's circular step, YH-pin, and ROOT-sup are unnecessary inputs.
This does not prove any of those separate estimates, or settle their use
outside this source class. In particular:

- The Hölder half and a full curvature-tower/norm conclusion are not banked.
- Positive spatial decay weights, nontrivial backgrounds, and the nonlinear
  problem are not covered.
- Arbitrary non-composite-co-closed sources still have the off-root
  divergence problem.
- Uniform per-level nonlinear row sizes do not supply a uniform Pl-c norm.
  The level sum c_j can grow with k. The row-summability issue identified in
  [REVIEW_BFT_B_S9_S10.md](REVIEW_BFT_B_S9_S10.md), “S10-6,” survives.
- If someone uses N for the *full* COF right side, use (13) or explicitly
  replace N by N_src. Do not silently bank X1's ambiguous comparison.

**Final verdict on X1 as a whole: CONFIRMED as the claimed conditional,
unweighted sup theorem, in the precise form (16)-(18). S10-11's purported
sup refutation is REFUTED. The full sup-plus-Hölder (CO-fun) statement
remains NOT-VERIFIED by this review.**

