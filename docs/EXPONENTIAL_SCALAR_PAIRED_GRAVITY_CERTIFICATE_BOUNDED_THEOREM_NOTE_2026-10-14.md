# A finite-error test for paired gravity measurements

Status: conditional support.
Claim type: bounded_theorem.
Scientific author: /root.
Primary runner: `scripts/exponential_scalar_paired_gravity_certificate_check.py`.

Two matched epochs can infer a candidate coupling without an assumed absolute
reference scale. A third epoch tests a separate consistency relation. This
unit derives finite error bounds from measured values and explicit aggregate
error envelopes, including a gate that refuses an unresolved denominator.
It does not substitute published estimates from different environments for
the required paired data.

The [supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
[local normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and [ideal force readout](EXPONENTIAL_SCALAR_CALIBRATED_GRAVITY_TURNING_BOUNDED_THEOREM_NOTE_2026-10-14.md)
are premises. The earlier two-epoch affine reconstruction is preserved in the
archive and is re-expressed here; only its finite measured-input certificate
and explicit residual error control are new extensions.

## Measured-error certificate for paired force and deflection

Scientific author: /root. This is an operational re-expression and finite-error
extension of TWO_EPOCH_DERIVATION_v1.md, not a new unique-action derivation.
All weak common-background, long-range, complete-source and calibrated-response
premises of the calibrated gravity turning block remain. The observables are
an ideal total force coefficient G and potential ratio gamma at matched epochs
of the same modeled environment/source. They are not arbitrary published G
and gamma estimates from unrelated experiments. No new real data is fit.

### Exact reconstruction without an assumed reference scale

Let q=(1-gamma)/(1+gamma), 0<q<a<1/3 and a=(1-k)(1+3k)/4.
The supplied forward functions imply

    H=G (1-3q)/(1+q)=G(2gamma-1)=P(a-q),
    P=4 Gref/(1+k)^2>0.

Thus H is affine in q. Two epochs with distinct q give

    D=H1-H2, N=q2 H1-q1 H2,
    a=N/D, P=D/(q2-q1), k=(1-2 sqrt(1-3a))/3.

The admissible parameter is 1/4<a<1/3, with all0<q_i<a and P>0.
The other quadratic k root is outside0<k<1/3. A common unknown positive
multiplicative calibration of every G rescales H and P, leaving a and k
unchanged. This does not remove time-dependent calibration, source mass
changes or uncontrolled environmental corrections. Absolute Gref still needs
an absolute measurement; nu,Hv, potential selection and state history remain.

This is algebraically equivalent to the earlier affine Y versus G_lens
relation: G_lens=G/(1+q), Y=1/(1-3q), hence H=G_lens/Y.
From H=P(a-q), q=(1-1/Y)/3, one obtains
G_lens=P[(a-1/3)Y+1/3]. The old intercept is1/(1-3a)=4/(1-3k)^2.
The new point is the following measured-input error certificate, not that
re-expression. The turning point of G alone causes no special algebraic
failure when the paired q values are distinct and adequately separated.

### Finite errors use measured inputs

Suppose actual ideal quantities obey deterministic aggregate envelopes
|G_i-Ghat_i|<=eG_i and |gamma_i-gammahat_i|<=egamma_i. These must include
measurement and forward-model errors in the same units; a reported Gaussian
standard error is not automatically such an envelope. Assume
1+gammahat_i>egamma_i>=0. Define

    qhat_i=(1-gammahat_i)/(1+gammahat_i),
    Hhat_i=Ghat_i(2gammahat_i-1),
    eq_i=2 egamma_i/[(1+gammahat_i)(1+gammahat_i-egamma_i)],
    eH_i=|2gammahat_i-1| eG_i+2|Ghat_i| egamma_i+2 eG_i egamma_i.

Exact difference identities and the product triangle inequality prove these
q/H envelopes, without independence, linearization or an assumed true input.
The cross term is required for arbitrary finite errors.

For Dhat=Hhat1-Hhat2, Nhat=qhat2 Hhat1-qhat1 Hhat2, define

    eD=eH1+eH2,
    eN=|qhat2|eH1+|Hhat1|eq2+eq2 eH1
       +|qhat1|eH2+|Hhat2|eq1+eq1 eH2.

If |Dhat|>eD, ahat=Nhat/Dhat obeys

    |a-ahat| <= ea=(eN+|ahat|eD)/(|Dhat|-eD).

Proof: subtract the two rational expressions, use the exact measured ahat
in (N-Nhat)-ahat(D-Dhat), and bound the true denominator below. No unknown
true a appears in ea. If [ahat-ea,ahat+ea] is wholly within(1/4,1/3),
monotonicity gives the exact k interval by applying k(a) to both endpoints.
The signs of D and q2-q1 must be certified consistently to infer P>0;
a sufficient test is separate strictly same-sign measured intervals using
eD and eq1+eq2. Physical field intervals require qhat_i-eq_i>0 and
qhat_i+eq_i<ahat-ea. Failure of a sufficient certificate is inconclusive,
not an exclusion or a license to divide by an interval containing zero.

### A third epoch is a separate consistency test

Choose the two calibration epochs before testing the third. The third point
must obey

    Z=(q2-q1)(H3-H1)-(H2-H1)(q3-q1)=0.

For measured differences Q21=qhat2-qhat1, Q31=qhat3-qhat1,
H21=Hhat2-Hhat1, H31=Hhat3-Hhat1, set
E_Q21=eq2+eq1,E_Q31=eq3+eq1,E_H21=eH2+eH1,E_H31=eH3+eH1. Then

    |Zhat-Z| <= eZ=|Q21|E_H31+|H31|E_Q21+E_Q21 E_H31
                       +|H21|E_Q31+|Q31|E_H21+E_H21 E_Q31.

The exact expansion of each product proves the bound even with correlated
errors. |Zhat|>eZ rejects this conditional forward relation under the claimed
envelopes; |Zhat|<=eZ is not acceptance of the complete theory. The error and
residual both scale with a common G calibration, so their comparison is
unchanged. Any positive normalization common to both may be used; dividing
by a separately uncertain reference requires its own error handling.

Current Cassini and LLR summaries do not provide this matched three-epoch
experiment. They remain exposed context, not combined data. The inverse is
conditional calibration, not first-principles parameter selection, and the
prospective relation is shared by other actions with the same coupling law.
No claim of unique action, actual initial state or TOE is made.


## Computed controls and evidence roles

The original computation has576 passed and0 failed conditions: exact original
coupling identities,9 k/calibration settings,81 declared correlated finite
error fixtures, separate third-epoch data alterations and singular-data gates.
The first two synthetic epochs calibrate; the third was designated in the
protocol before calculation. It remains same-model synthetic evidence, not
an independent observed holdout. All actual parameters and full result rows
are preserved. The general certificates follow from algebraic inequalities,
not from a finite noise grid. Four actual altered implementations respectively
produce152/424,323/253,548/28 and575/1, detecting a wrong gamma transform,
inverse sign, omitted finite cross terms and missing separation gate.

The complete result exceeds the cache helper's200000-character body cap if
printed as ordinary JSON. The canonical wrapper therefore carries the entire
unit as lossless zlib/base64 JSON, with byte length and SHA256, plus readable
counts and scope. No numerical field, failed row or case is omitted. Decode
base64, decompress zlib, verify length/hash, then parse JSON. The runner
round-trips the payload before success. The archive also contains the full
uncompressed results, original source and complete staged profile file.
Compression is packaging, not a scientific check or statistical operation.

No observed parameter, confidence region, universal coupling law, initial
state, physical history or absolute scale is derived. Constant shared
calibration cancels; arbitrary time-dependent calibration does not. The
error envelopes must cover real apparatus and forward-model errors before
any observational rejection could be claimed. No such data or error model
has been established in this campaign.

Recovery: `docs/work_history/physics/revised-scalar-paired-gravity-certificate-20261014/README.txt`.
