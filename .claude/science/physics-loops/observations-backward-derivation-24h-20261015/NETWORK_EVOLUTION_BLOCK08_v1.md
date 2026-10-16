# Which neighborhood can connect separated records?

Personal author: /root, 2026-10-16. Actual status: conditional-support.
Known Bell/game arguments are reconstructed here, not presented as new results.
The purpose is to constrain the specific changing-neighborhood hypothesis and
identify what further assumption a constructive route must actually derive.

## Observation intake and its limits

[Hensen et al.](https://arxiv.org/html/1508.05949v1) report an event-ready test
with 245 trials, 196 game wins, and a memory-allowing local-model p-value at most
0.039. Their electronics recorded outcomes within the stated space-like timing
arrangement. The reported correlation estimate S=2.42 is distinct from the
game-score value 8*(196/245-1/2)=2.4 when setting counts are unequal.

[Elkouss and Wehner](https://arxiv.org/abs/1510.07233), Figure1, give the numerical
input bound tau=1.08e-5 and win bound 3/4+tau-tau^2 for that comparison. The
calculation below reconstructs the binomial-tail number from those published
inputs. This is exposed development evidence, not a fresh independent data
analysis, a new experimental result, or a posterior probability that the
network hypothesis is false. Raw records, timing calibrations and the full
input-source characterization have not been reanalysed here.

## Causal neighborhoods, with unrestricted past memory

Let H include the entire past network, its changing edges, shared variables,
prior settings and records. Condition also on any admissible event-ready tag
selected before current inputs. Suppose during a trial that:

1. Each current input X,Y is fresh and uniform, independent of H and of the
   other input.
2. No directed physical influence path carries the current X to the other
   recorded output B, or Y to A, before those outputs are fixed.
3. The complete common causes are included in H, so conditional output laws
   factor locally. Local randomness can be included among preassigned private
   seeds independent of the fresh settings.
4. Outcomes are not subsequently relabeled or selected using current inputs.

For a deterministic realization the four local values A0,A1,B0,B1 are bits.
Winning requires A_x xor B_y = x*y. XOR all four winning equations: the left
side is zero, while the right side is one. At least one setting pair loses.
Thus conditional win probability is at most 3/4, for every H; mixing local
strategies does not change the bound. Arbitrary evolution between trials,
including changing record roles and adaptive specialization, is already allowed.
The restriction is on current-trial influence and setting independence.

If, conditional on H, X and Y are independent but each bit probability differs
from 1/2 by at most tau, every pair has probability at least (1/2-tau)^2. Hence

    P(win|H) <= q = 1-(1/2-tau)^2 = 3/4+tau-tau^2.

Without conditional factorization of the input sources this particular bound
does not follow from their two marginal biases. A separate joint-input bound
would be needed. No experiment proves independence from every conceivable
hidden common cause solely from observed marginal randomness.

For a fixed number N of admitted trials, the same conditional bound implies

    P(total wins >= k) <= sum_(j=k)^N choose(N,j) q^j (1-q)^(N-j).

One proof uses backward induction on the remaining number of trials. The
binomial upper-tail continuation value is greater after a win than a loss;
therefore its conditional expectation is maximized by taking the current
win probability q. This proves the recursion without iid devices. It is a
fixed-horizon result, not automatically an anytime-valid stopping rule.

Changing what later records mean does not alter this argument if the original
bits are preserved and the score is fixed. Actually rewriting an old output,
postselecting it, changing setting independence, or changing the relevant
causal neighborhood changes a stated premise and must have its own predictive
physical model. Calling distant events graph-neighbors may be a possible
candidate ontology; identifying that graph with observed space-time locality
then becomes a new obligation, not a completed derivation.

If a fraction lambda of trials permit current cross-setting influence, and
eligibility is selected before fresh inputs so those inputs remain fresh even
conditional on eligibility, the mean win bound becomes 3/4+lambda/4. Reaching
the ideal quantum CHSH value requires lambda>=sqrt(2)-1. This is only that
specified mixture resource bound, not a bound on every possible nonlocal
model. Input-dependent exception selection invalidates this coefficient, as
the preserved block01v1 failure already demonstrated in a related game.

For context, [Toner and Bacon](https://arxiv.org/abs/quant-ph/0304076) give a
known one-bit communication construction for singlet projective-measurement
correlations. That is evidence that explicit relational resources can matter;
it is not a local space-like mechanism or a derivation from the repo axioms.
Its four-page proof was read, but no theorem from it is needed below.

## Symmetry and no-signaling still do not select the quantum correlation

Even allowing a joint relational response does not select its numerical law.
For unit setting axes a,b and any gamma>0, set

    E_gamma(a,b)=-sgn(a.b)*|a.b|^gamma, with E_gamma=0 when a.b=0,
    P_gamma(A=r,B=s|a,b)=[1+r*s*E_gamma(a,b)]/4, r,s in {-1,+1}.

These are nonnegative normalized pair probabilities with zero local means,
no-signaling marginals, full proper-rotation covariance, exchange symmetry,
axis/outcome reversal symmetry, and perfect same-axis anticorrelation.
At gamma=1 they give the singlet pair table. At the usual four coplanar CHSH
axes the magnitude is

    |S_gamma|=4*(1/sqrt(2))^gamma=2^(2-gamma/2).

In particular 0<gamma<1 exceeds 2*sqrt(2) while retaining all the listed pair
properties. These tables are not claimed to have a consistent quantum
multisystem composition or a local hidden-variable implementation. They prove
only that the listed symmetry and marginal conditions do not determine the
desired law. Selecting gamma=1 by matching the target would be calibration,
not a derivation of the physical coupling.

## A precise additional premise that would select the linear law

Assume an operational single-system state is fully specified by a vector s
in the unit ball of R^3, and that random mixtures of preparations are represented
by the corresponding convex mixture of those vectors. For a binary analyzer
axis b, assume its mean response m_b(s) is affine in that state, covariant under
simultaneous SO(3) rotations, and reverses sign under b->-b. Finally calibrate
the aligned pure-state response m_b(b)=1.

An affine function is m_b(s)=c_b+d_b.s. Covariance makes c_b constant on unit b;
axis reversal then forces c_b=0. Rotations fixing b force d_b to be parallel to
b; covariance fixes a common coefficient d_b=k*b. Calibration gives k=1.
Therefore m_b(s)=b.s and the binary outcome probabilities are (1+/-b.s)/2.

If a supplied bipartite preparation has unbiased A and conditional B state
s=-A*a, this gives E[AB]=-a.b. Neither that bipartite preparation nor the
three-component sufficient-state/mixing premise was derived from a changing
network. This is the familiar linear operational reconstruction within a
declared state space, not a new route around its assumptions.

A possible discrimination is to compare two independently characterized
preparation histories which that proposed sufficient state identifies. For
example a half-mixture of x and z orientations has mean s=(x+z)/2. Writing
n=(x+z)/sqrt(2), r=1/sqrt(2), the mixture of n and -n with weights (1+r)/2 and
(1-r)/2 has the same mean vector. A pure-orientation response
g_gamma(a.b)=sgn(a.b)|a.b|^gamma, extended by ordinary mixture probabilities,
predicts at analyzer b=n the values 2^(-gamma/2) and 2^(-1/2), respectively.
They agree at gamma=1. Their equality is conditional on the proposed physical
preparation identification; it cannot be asserted just by naming both mean
vectors s. A real protocol must calibrate actual preparation and detector
couplings and control drift before treating a discrepancy as new physics.

The constructive research direction is therefore specific: derive when local
network history can be compressed into an operational state with this mixture
equivalence, and when context leaves additional observable memory. The present
work does not establish that current physics ignores intermediate evolution;
geometric phase, conditional states and open-system memory already describe
many such effects. A new mechanism must recover those successful relations
and explain any additional observable dependence without selecting it by hand.
