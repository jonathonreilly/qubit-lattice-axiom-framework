# Initial energy and band balance: released-source POST

No material mathematical disagreement was found with the sealed PRE. The
root's compact initial profile, uniform energy bounds, distributional net
drift including its endpoint term, and exact coherent band balance are
supported under the stated provisional dependencies. The additional
trace-norm rare-density statement and positive diagonal carrier also follow
from the supplied source/age estimates, as reconstructed below. No author
controls were rerun.

One minor publication wording clarification is recommended. In the frozen
derivation, lines 299–305 summarize “loss terms of order epsilon^-2” and
“either positive circulation term.” Equations (17)–(21) establish a
nonnegative gain, a nonnegative diagonal carrier with a pointwise scaled
limit, and an exact coherence-containing loss with a distributional scaled
limit. The summary should explicitly name the gain and diagonal carrier as
the positive quantities, and retain the tested integral/distributional
sense for the exact loss. The preceding equations already make these
distinctions correctly; this clarification requires no new scientific result.

## Reviewed identities and independence boundary

The independent PRE is SHA256
`785f3c87cec7db2d00f2548745b22fd68e74afa09a307081446fc80763555b3a`,
with PRE seal SHA256
`f459870253083462c9448a0f1ca2ea50beb9b954b34bdffd783fe27a08f060f8`.
All 19 members remain unchanged. The PRE was sealed at 17:31:36 UTC.

The complete released argument is
`INITIAL_ENERGY_LAYER_AND_BAND_POWER_PERSONAL_DERIVATION.md`, SHA256
`f93139735be333d46cb7b5d7d0882beaa341532df0a76d24d61676b93514d844`.
Its author seal, SHA256
`498705aaeac3f6cd542ceabe0d0042fc7f301ef6b4e6402c4b56152c8c113513`,
records 17:13:58 UTC. Its control seal, SHA256
`97be508f590b9ad739d3fe9805dd2fdcbebfeceab9d859cc105de195c646a7ec`,
records 17:18:37 UTC. Both precede PRE disclosure. Every author/control
seal member was verified, and the complete argument, script, source-pin
manifest, execution receipt and every output row were read.

The argument's source manifest also names a separate full-ensemble author
candidate whose review was pending. That candidate and its controls were
not opened here. The necessary claims are checked directly from the expressly
supplied full-ensemble independent PRE, SHA256
`3996a4a5d128545470b8636d88aef2d6b29e424eff8672bd3be125dc372258df`,
and the unchanged permitted parents already read and pinned in this PRE.
They remain provisional imports. This POST does not adopt the pending
candidate, certify its other assertions, or reclassify an imported result
as independent discovery.

## Compact initial density and scalar limits

The root uses the actual L_i=sqrt(kappa) epsilon^-1 j_i inside its source
integral, whereas the PRE used j_i with kappa epsilon^-2 outside. The two
normalizations agree. Its first-high source is sqrt(kappa) epsilon R_i,S
a4,e+O(epsilon^3); integrating its squared amplitude over ds=epsilon^2 d sigma
therefore gives an epsilon^4 density, with coefficient kappa. No selected
branch normalization or missing survival factor occurs.

The Hermitian/no-event mismatch costs O(epsilon^3) on the bounded raw L_i
source, hence O(epsilon^2) after division by sqrt(kappa) epsilon. The scalar
phase disappears in each outer product, without mixing different birth
times coherently. Strong bounded-generator convergence, source convergence
and the rank-one trace-norm inequality then establish the whole finite
initial-age triangle, including tau=0.

The low source has bounded weighted energy action and an O(epsilon^2)
coordinate error after the L_i factor. Multiplying that error by the
O(epsilon^-2) low Hamiltonian costs O(1) in energy-vector norm. Integrating
over a physical interval O(epsilon^2) makes the low N=6 mean and second
moment vanish. The other-band estimates have the same normalization as
the PRE. Thus the full scalar conclusions and variance subtraction in
root equation (6) are justified. The root does not differentiate that
convergence to assert microscopic pointwise power convergence.

The trace-class initial profile is positive and increasing. Its tail is
positive, so its trace norm is exactly its trace; the imported rotor
norm-squared bound makes that tail O((1+tau)^(-3/2)). The stated iterated
order of limits is valid. My stronger uniform matched expression, moving
lower-endpoint criterion, initial microscopic derivative and extra initial
profile refinements remain PRE additions; they are not attributed to the
root's earlier frozen text.

## Fixed-positive-time rare density and the positive carrier

This trace-norm strengthening was not a theorem statement in my sealed PRE.
The following verification was made after release. It does not require
reading or accepting the separate full-ensemble author candidate.

In the PRE's raw-j notation let y_i,e,1(t,s) be the exact Hermitian high
coordinate. On 0<=tau<=t/epsilon^2 define

```
f_i,e(t,tau)=epsilon^-2 exp(i delta tau/epsilon^2)
                         y_i,e,1(t,t-epsilon^2 tau),
```

and set it to zero beyond that interval. The exact source formula gives

```
epsilon^-4 U1,e* rho6,e(t) U1,e
             =kappa sum_i integral_0^infinity |f_i,e><f_i,e| d tau. (P1)
```

The imported source estimate makes f_i,e equal to the phase-removed exact
fast block acting on R_i,S a4,e(t-epsilon^2 tau), plus O(epsilon^2).
The squared-age integral of that remainder is O(epsilon^2) over at most
T/epsilon^2 ages. The principal term has the common tail bound
`C_T(1+R)^(-3/2)+C_T epsilon^(1/2)` above R. On each bounded age interval
it converges to f_i(t,tau)=exp(tau Z)R_i u4(t), uniformly for t in a fixed
[a,T], a>0. Extend by zero as above and use the compact comparison below
R and both tail bounds above R. This proves

```
sup_(a<=t<=T) ||f_i,e(t,.)-f_i(t,.)||_L2(d tau) ->0.       (P2)
```

The norm sums are uniformly bounded. Applying the root's rank-one inequality
(8) to (P1) proves the fixed-positive-time trace-norm rare-density limit
to Sigma(t) defined by its equation (4). This is the needed extension of
the scalar proof; scalar mass convergence alone would not establish it.

The frozen-age Sylvester identity is valid in trace class. Z is bounded,
the rank-one integrand is trace-norm integrable, and its upper endpoint
tends to zero. Thus differentiation in age and integration give

```
Z Sigma+Sigma Z*=-kappa sum_i |R_i u4><R_i u4|.
```

Taking its trace, using Z+Z*=-kappa Gamma1, cancels the common kappa and
gives Tr(Gamma1 Sigma)=72 S4 and Tr(P_bright Sigma)=36 S4. The normalization
and the resulting impulse lower bound 36 delta are correct. This frozen-age
identity is not used in place of the finite-spin physical-time balance.

Let Ghat_e=U1,e* Gamma6,e U1,e, zero extended to the common rotor coordinate
space. It is positive with a common operator bound. The canonical rotation
is I+O(epsilon), and the finite-spin original loss converges strongly to
Gamma1, so Ghat_e converges strongly to Gamma1. For a trace-class density
Sigma and a uniformly bounded strongly convergent operator, the expectation
converges by finite-rank approximation. Combined with (P1)–(P2), this proves

```
epsilon^2 D_e(t)=kappa delta Tr[Ghat_e
                  (epsilon^-4 U1,e* rho6,e U1,e)]
               ->kappa delta Tr(Gamma1 Sigma)
                =72 kappa delta S4(t).                    (P3)
```

In particular the root's fixed-positive-time carrier claim is supported.
Its positivity follows from the trace of two positive operators, not from
positivity of an anticommutator.

For clarity, writing the exact loss in Hermitian bands gives a diagonal
term plus the real interband terms involving H1 Gamma_(1,r) rho_(r,1).
The diagonal term differs from D_e by at most O_T(1): H1 differs from
delta epsilon^-4 I by O(epsilon^-2), the high population is O(epsilon^4),
and the rate prefactor is O(epsilon^-2). This makes their scaled difference
vanish. No corresponding pointwise estimate for the interband term is
assumed. The exact loss is therefore not replaced by D_e. Equations
(19)–(20) of the root have precisely the uniform-gain/distributional-loss
scope reconstructed in the PRE.

## Net drift and endpoint bookkeeping

The exact full drift and exact first-high gain-minus-loss identity agree
with PRE equations (14) and (19)–(20). The time-independent Hermitian
Hamiltonian commutes with its band observable, and every second birth
lands in the zero-energy terminal sector. The root retains all
anticommutator coherences.

The source/age and remaining-band estimates indeed give bounded full and
first-high means on the complete [0,T], including zero. They supply L1
convergence when combined with the positive-time limits. Integration by
parts then gives the positive endpoint coefficient
delta Tr Sigma(0)=kappa delta I(0). Its sign is correct: the microscopic
initial mean lacks the positive first-high contribution present in the
right-hand limiting mean. The same reasoning for the first-high mean,
initially zero, assigns the entire boundary contribution to that band.

The root's weighted C1 justification is sufficient: a fixed extra electric
weight controls u4' in the smooth-source class, the two cross terms in the
trace-class age derivative have an integrable common bound, and weighted
low source vectors remain in the needed Hamiltonian domains. Alternatively
the distributional formulation already works without that classical
derivative. The text correctly excludes total-variation, weak signed-measure
and pointwise-power conclusions. Its bath/work and physical-selection
limitations are consistent with the exact system-energy identity.

## Existing controls and verification limits

The frozen script SHA256 is
`b86de88159b5593cb16c749edf2966499670a838a562b4de2857a9a2bf956d65`.
It is a separate trace-one three-state classical cascade plus a two-band
anticommutator example. It contains no actual cube builder, canonical
large-spin evolution or finite-fiber Green calculation. The source's
mention of possible Green calculations is not evidence that one was
executed in this packet.

The cascade's rates are nonnegative at every recorded sample. Its exact
population solution has the correct rare-state energy and variance
normalization. The script records 25 initial-profile rows, 15 physical-flow
rows and five distribution-test rows. The test function (1-t/T)^2 has the
stated Laplace integral. The separate fast-age quadrature agrees with
the scalar closed form to about 1.6e-14. The omitted-impulse expression is
an explicitly evaluated wrong limiting formula separated by the known
impulse; it is not presented as a modified microscopic simulation. The
loss-sign example gives -0.16619037896906005, consistent with
1-sqrt(1+0.6^2), while Gamma is positive.

The complete result and stdout have identical SHA256
`2bf3bc82e37e1d5e2a9886ad362c48ff9332dc1c682d64113191eb55c56d4bfe`.
The execution receipt records exit 0 and separately captured empty stderr.
These are existing author controls, not independent reproduction or proof
of the cube's trace-norm, uniform-time or spin-limit assertions. All recorded
rows and the complete code were inspected; no rerun was needed.

Disposition: supported conditional released candidate, with the narrow
summary-wording clarification above. PRE and its evidence remain intact.
The trace-norm and carrier checks here are explicitly POST work; stronger
matched/initial-derivative claims retain their PRE attribution. No publication,
retained/audit state, other active checker packet or prior seal was changed.
