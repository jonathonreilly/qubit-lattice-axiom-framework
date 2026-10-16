---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
source_science_acceptance_complete: true
canonical_parent_binding_complete: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---
# A supplied finite weak mediator for one fixed two-qubit target

Claim type: bounded_theorem.

**Primary runner:** `scripts/weak_mediator_fixed_target_2026_10_16.py`

## Conditional result and status

This source-only note packages one self-contained conditional construction for
literal old `K=2I+Z1Z2` and the full-phase target
`W=((9+12i)I+(-16+12i)X1X2)/25`. It supplies two additional qubits, a Bell
projector interaction and four positive XX/YY ports on a square. These are new
microscopic permissions. The construction does not derive them from the
original four onsite rays or the repository's bare microscopic assumptions.
It retains every old/source/reference output and gives an actual-time finite
window, explicit finite coefficients and a known finite reuse budget.

Root accepted the conditional science in ACCEPTANCE.json `ba201403`, controlled
by QUALIFICATION.md `e367c861`, reproduced as the twelfth complete body below.
Review of this wrapper, the actual Git base, canonical integration, staging,
publication and retained audit remain unset. The default primary checks source
integrity and then refuses unbound canonical use. Historical proposed/unchecked
language remains unchanged evidence of the original stage.

The complete six root bodies and five analytic reviews are preserved byte for
byte before the controlling qualification. They are all part of this root
argument, not eleven external theorem parents. The proof starts from the
displayed finite matrices; it has **zero direct mathematical parents**. Other
campaign results, including the previous onsite word and direct static edge,
are context only. No previous publication archive or negative-science packet
is imported by the machinery reuse.

## Hamiltonian, full phase and finite window

Write `theta=atan(4/3)`, `delta=theta/pi`, `Delta=2-delta`, `q=theta/T`,
`gx=sqrt(q Delta/2)`, `gy=sqrt(q)` and `r=2(gx+gy)`. The source starts in
`Phi+=(00+11)/sqrt(2)` independently of the arbitrary old/reference input,
and `J psi=psi tensor Phi+`. Install

    H = K + Delta(I-|Phi+><Phi+|) + r I + V,
    V = gx(X1 XA + X2 XB) + gy(Y1 YA - Y2 YB).

The positive blocks are the source projector term, `gx(I+X1XA)`,
`gx(I+X2XB)`, `gy(I+Y1YA)` and `gy(I-Y2YB)`. Their identity reserve is
already `rI`, not a further block. Each old vertex has added incident load r;
each source vertex has Delta+r. Both are below 2 in the specified family.
The old norm-3 K block remains separately counted: its old total is 3+r.
Runtime coefficients are static and have zero slew. Physical units require
an explicit energy unit E0 and physical duration hbar*T/E0; no rescaling of
the literal old term is used to meet the added cap.

The full comparator at `t=T+s` is

    J exp(-irt) exp(-isK) W exp(-iTK).

For installed lower rounded coefficients it uses **actual**
`rhat=2(gxhat+gyhat)` in place of r. The literal old scalar and actual source
reserve are both retained. The proposal's phrase “source triplets” is corrected
here to **orthogonal Bell complement**: V reaches Psi+ and the spin-singlet
Psi−. The already-defined projector penalizes both correctly.

The exact first and second Sylvester correctors yield the identity
`(H0+V)F-F(K+H2)=VS2-S1H2-S2H2` for `F=J+S1+S2`.
The compressed second-order operator is

    H2 = ((2pi-theta)/T) I + (2pi/T) ZZ - (theta/T) XX,
    exp(-iT H2) = W.

The full cross-spectrum gap is delta; the input band need not be globally
lowest. Frobenius inverse bounds and exact Duhamel propagation give
`R(T)=12352/sqrt(T)+132096/T` for times at most 2T. Thus the proof uses an
exact residual, not an unbounded-time assertion about a truncated expansion.

For integer m>=0 set epsilon=2^-m and T=2^(2m+32). Equality-safe lower
rounding at p=3m+39 gives each coefficient error below 2*2^-p. On the fixed
24 window the full-isometry error is below 13epsilon/32. On the larger window
`w=epsilon*T/256`, it is below 15epsilon/32, hence unhalved full joint trace
error below 15epsilon/16. Tensoring arbitrary references preserves the norm;
mixed inputs follow by purification. A full initial joint trace defect adds
once. A source-marginal error alone is insufficient with arbitrary initial
correlations; the preserved review supplies a counterexample.

The sharper structured result keeps the same supports, signs, paired port
coefficients, source projector and exact K, and only lowers the three shared
coefficients. Port errors at most `hg=epsilon/(4096 sqrt(T))` and source error
at most `hD=epsilon/8192` give isometry error below 7epsilon/16 on the larger
window. The proof prices `||H2hat-H2||<128hg/sqrt(T)+256hD/T` and the actual
corrector residual. Its norm monotonicity uses this commuting Pauli family;
its gap bound uses Deltahat>3/2. It is not a generic fault estimate. Generic
self-adjoint residual E retains a separate `(T+w)||E||` allowance. Using the
original r instead of actual rhat can give an order-one phase defect, as the
unchanged review demonstrates.

## Finite compiler, reuse and energy

Three fixed alternating sums for atan(1/5), atan(1/239), atan(1/7), signed
Machin intervals and exact rational lower endpoints supply the coefficients.
Integer quotient and isqrt operations avoid any irrational grid-equality
oracle. Uniform n=p+8 or mixed grids `pg=2m+29`, `pD=m+14`,
`n=max(pg,pD)+8` meet the stated bounds. Each scenario uses **3n summed terms
plus three first-omitted remainders**, three final rounding quotients and two
isqrt calls. Those primitive counts exclude rational internals/GCD and do
not establish a total bit-complexity optimum. Output coefficient bit bounds
are not intermediate arithmetic bounds or physical calibration guarantees.

For known finite L, the unitary hybrid argument accumulates at most L times
the one-use isometry error with the same source retained. It does not assume
that the actual source resets or remains uncorrelated. Optional interventions
are supplied unitaries on old/reference registers acting as identity on the
source; their duration, apparatus, aging and error are separate interfaces.
Taking `m=m0+ceil(log2 L)` gives final trace error below epsilon0=2^-m0
with mediator endpoint duration below `2^34 L^3 epsilon0^-2` and window-inclusive
duration below `2^35 L^3 epsilon0^-2`. This excludes physical intervention time.
The window compares actual old aging, not a stationary output. It supplies
neither permanent halt nor indefinite reuse of one fixed device.

For the intended Bell product input the exact mean is `<K>+r`; the variance is
`Var(K)+2gx^2(1+<XX>)+2gy^2(1+<YY>)`, with hats for the actual rounded model.
The full static moments are conserved. Old K energy can change during runtime;
an endpoint bound follows from the joint trace error and half-width 1 of K.
Zero prescribed drive work during the static interval does not price source
preparation, installation, calibration, timing, reset or discarded apparatus.

## Actual evidence and limits

Two author scientific programs ran once each, with no replay here. The symbolic
fixture took 0.2838803748600185 seconds and records 60 finite exact polynomial
checks, including wrong-sign and bare-denominator mutants; its complete report
is 247777 bytes at SHA256 `4369fa1d5a970bf4e01ea00cc7db000779cab1d1f26be9bcbd26e1c4bc292a7d`.
The coefficient compiler took 0.131953792180866 seconds and records 64 checks
for two predeclared m44 outputs: T=2^120, uniform p171/n179/window24 and mixed
pg117/pD58/n125/window2^68. Its 1188206-byte report is
`0b108a9605e02b8b907ea13b364875b6282fc727c368dbed862ecb5d67149564`.
The latter observed 912 summed terms, six remainders, six final quotients,
four isqrt calls, 6111 guarded integer operations and maximum guarded integer
size 20857 bits. Both had actual 60-second wall limits, exit 0 and no timeout;
neither had an OS CPU/RAM quota.

All original and captured sources, inputs, reports, actual argv/cwd/version,
complete streams and freeze inventories are recoverable from SOURCE_MANIFEST.
Large polynomial and rational report bytes are preserved and hashed, not
described as manually checked entry by entry. The analytic reviews are separate
source-exposed reconstructions using the same selected model; the reviewer
contributed the lower-rounding strategy. This packaging author wrote both
scientific programs. There is no blind/model-independent validation or physical
experiment. Analytic gap, exponential and remainder proofs remain distinct
from finite assertions; provenance checks prove no physics.

A separately implemented saved-certificate validator subsequently ran once in
0.07717579184100032 seconds, exit 0, with 429 arithmetic predicates. Its exact
receipt is `73c9f6544f7530f3e8106b6f4f1dc523098e2bf107312bae88644bf8a88358a0`
and result is `ea2b9b99c64e6e3eecadde5a9eec34a50a589afb26a0ce40f1e378d0dab3fdb5`.
It checks saved endpoint algebra, integer inequalities, loads, actual phases
and conditional budgets without rerunning the compiler, calling isqrt or
regenerating the series. Saved endpoint truth remains an analytic premise.
Its report-derived implementation shares the model and Python integer trust
base; it is not blind, physical or an independent enclosure proof. The original
failed metadata inspection and corrected schema attempt are preserved with
their actual sources and streams. Root acceptance predates this check; neither
that acceptance nor any of the twelve bodies is rewritten by the new evidence.
Bell preparation, supplied microscopic couplers, physical precision and
observation timing remain explicit obligations. Root controls all later
wrapper and publication decisions. The new draft changes no editable prompt,
physical axiom, canonical file, Git state or retained audit record.
