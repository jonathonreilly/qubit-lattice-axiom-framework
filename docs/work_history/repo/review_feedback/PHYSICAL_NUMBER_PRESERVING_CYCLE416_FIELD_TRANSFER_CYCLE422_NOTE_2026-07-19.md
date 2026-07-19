# Physical number-preserving Cycle-416 field transfer — Cycle 422

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is changed or proposed.

Companion runner:

```text
scripts/physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19.py
```

## Result up front

Cycle 422 eliminates the Cycle-417 fanout from the recurrent field route. It
constructs one **fixed nine-M2 unitary** `W` on the Cycle-416 source and
mediator M2s plus one blank reservoir and six blank directional field M2s. On
the declared one-excitation, blank-target input code,

```text
W |source>   -> |R>;
W |mediator> -> -|s_F>;
|s_F> = (1/sqrt(6)) sum_d |1_d>.
```

Equivalently, the source column maps to the reservoir column and the mediator
column maps to the negative uniform field column.

The output clears source and mediator. `W` preserves total excitation, is its
own adjoint and inverse, and implements the Cycle-418 encoding physically. For
both strict-response values,

```text
W E_in G_416(r) = G_7(r) W E_in,  r=0,1.
```

The transferred state feeds directly into the Cycle-419 two-block coin,
local exchange, and directed transport without Cycle-417 ports. The local
exchange is coherently controlled by the inherited strict-response M2. This
control is necessary: after the complete Cycle-416 code is transferred, an
unconditional exchange would emit from response-zero source branches. The
single fixed controlled update applies `G_7(0)` or `G_7(1)` inside the same
physical block without expectation feedback. There is no expectation feedback
anywhere in the transfer or propagation update.

The original Cycle-416 source-plus-mediator excitation becomes reservoir-plus-
field excitation and stays exactly balanced through propagation and inverse.
Unlike Cycle 419's copied-port comparison, no leftover mediator and duplicated
port occupations are present. This closes the excitation ledger only on the
declared code and schedule. The coordinate is **not physical energy, source,
time, or Born weight**.

## Physical code and fixed unitary

Order the Cycle-416 source/mediator computational basis as

```text
|00>, |01=mediator>, |10=source>, |11>
```

and the seven-M2 target as one reservoir qubit times six field qubits. The
complete physical space has dimension

```text
4 * 2 * 64 = 512.
```

Let `E_in` contain the two input columns

```text
|10; R=0,F=0>, |01; R=0,F=0>,
```

and let `E_418` contain

```text
|00; R=1,F=0>, -|00; R=0,s_F>.
```

The columns of `E_in` and `E_418` are mutually orthonormal. Cycle 422 defines

```text
W = I - E_in E_in^dagger - E_418 E_418^dagger
      + E_418 E_in^dagger + E_in E_418^dagger.
```

Thus `W` swaps the two code subspaces and is identity on their orthogonal
complement. It is a full physical unitary/dilation, not a non-square analysis
map. Its load-bearing action is bounded to nine M2. A primitive nearest-
neighbor synthesis of the dense gate is supplied implementation content and
remains open; the matrix unitary itself, its support, inverse, and code action
are explicit.

Every swapped state has exactly one excitation, so `W` commutes with the full
nine-M2 Hamming-number operator. The forward scientific contract is narrower
than the full unitary domain: source plus mediator must equal one and every
target M2 must start blank. The runner provides explicit **target-blank
refusal** for malformed forward preparations. Nonblank target states remain
lawful inputs to the global unitary, but are not claims of the forward
Cycle-416 transfer contract.

## Physical intertwiner and inverse

Cycle 416 uses

```text
G_416(0)=I,
G_416(1)=cos(theta) I + i sin(theta) X
```

on `(|source>,|mediator>)`. The seven-M2 exchange uses the opposite `-i`
convention between `|R>` and `|s_F>`. The negative field seed is therefore
load-bearing. With `theta=0.36272452333990834`, the runner checks forward,
inverse, and compression residuals for `r=0,1`, as well as

```text
W^dagger W = I,
W^2 = I,
[W,N_total] = 0,
W E_in = E_418.
```

After the forward map, the old source and mediator bits are exactly zero. The
adjoint returns the signed field/reservoir code to the original Cycle-416
source/mediator code. This is the exact adjoint and inverse relation on the
declared code.

Cold physical-transfer residuals are:

| control | residual |
|---|---:|
| `W^dagger W-I` | `5.659307398773803e-16` |
| `W^2-I` | `5.659307398773803e-16` |
| `[W,N_total]` | `0.0` |
| `W E_in-E_418` | `0.0` |
| maximum forward intertwiner, `r=0,1` | `9.614813431917819e-17` |
| maximum inverse intertwiner, `r=0,1` | `5.135769134355248e-16` |
| maximum compression residual | `3.4219371797089426e-16` |

## Connected bounded layout and frames

The reservoir and six field M2s form block A. The source and mediator extend
two sites from its `-x` boundary rail; the strict-response control is adjacent
to that chain. Block B is the neighboring Cycle-419 seven-M2 block, with the
two directed boundary rails adjacent. The nine-M2 `W` support is connected,
as is the response-controlled two-block installation. This is a connected
bounded layout, not an asymptotic support claim.

Source, mediator, reservoir, and response use supplied scalar frame actions;
the six field rails use the Cycle-210 direction permutation. The negative
uniform field seed is scalar. The runner checks `W`, `E_in`, and `E_418` in
all 24 proper-cubic frames and separately checks the rotated physical layout.
These are spatial frames, not physical time.

## Deletion, sign, and lawful-domain controls

Four independent controls are kept distinct:

1. replacing `W` by identity visibly fails to transfer either input column;
2. deleting the negative sign gives a large `r=1` intertwiner residual;
3. deleting one field direction gives a visible intertwiner residual and
   destroys the scalar target;
4. target-nonblank and invalid source/mediator preparations are refused by the
   declared forward interface.

These are construction controls, not minimum-content or impossibility claims.

Cold deletion/domain values are:

| control | value |
|---|---:|
| lawful-domain refusals | `4/4` |
| cleared source/mediator leakage | `0.0` |
| `W`-deleted transfer residual | `2.0` |
| wrong-sign intertwiner residual | `1.0035904189606986` |
| one-direction-deleted residual | `0.15362399182697634` |
| adjoint return residual | `3.908194008942788e-16` |

## Direct recurrent propagation and global excitation balance

For both Cycle-399 source routes, both origins, L5, and blind held L6, the
runner executes

```text
Cycle-416 strict response and balance
  -> W into blank reservoir/field block A
  -> response-controlled Cycle-419 local exchange
  -> Cycle-419 field coin and directed boundary SWAP
  -> exact inverse schedule
  -> W^dagger back to the Cycle-416 balance code.
```

No Cycle-417 CNOT or port appears. No field or mediator expectation is used to
choose, prepare, or control a gate. Squared norms are read only after execution
for regression diagnostics.

For strict-response weight `p_r`, the number-preserving route produces the
one-edge neighboring weight

```text
p_new = p_r sin^2(2 theta) / 6.
```

The old Cycle-419 copied-port route produced

```text
p_copy = p_r sin^4(theta) / 6,
```

because it first copied only the post-Cycle-416 mediator label and then used
that copy as a new reservoir control. The exact comparison ratio is

```text
p_new / p_copy = sin^2(2 theta) / sin^4(theta)
               = 4 cot^2(theta).
```

The difference is not an empirical prediction. It is a quantitative audit of
two different declared interfaces: coherent number-preserving amplitude
transfer versus non-number-conserving basis-label fanout.

Cold held values are:

| route | direct number-preserving neighbor | Cycle-419 copied-port neighbor |
|---|---:|---:|
| unit-weight | `4.3714824837761e-07` | `1.574092565133932e-08` |
| coefficient-two | `2.2044022214991975e-06` | `7.937657671749998e-08` |

The analytic and observed ratio is `27.771444834974805` up to floating-point
roundoff. Across all eight route/size/origin cases, the maximum global
excitation residual is `4.440892098500626e-16`, maximum inverse residual is
`3.270153950081591e-18`, and maximum target-code leakage after inverse is
`7.310107194127739e-19`.

At every held case the runner checks

```text
N_source+mediator before W
  = N_reservoir+field after W
  = N_reservoir+field after propagation,
```

then applies the adjoint recurrent update and `W^dagger` to restore the exact
Cycle-416 balance state. This is global excitation balance from the original
Cycle-416 code. It is not a selected resource, energy, source, rate, or
probability law.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-416 response bit, source/mediator code, balance gate, angle, and
   preparation;
2. one blank reservoir M2, six blank field M2s, and the dense bounded `W`
   implementation;
3. the Cycle-418 negative uniform-field convention;
4. the Cycle-419 field coin, directed transport, two-block boundary, gate
   order, L5/L6 cases, and tolerances;
5. scalar register frame actions and diagnostic readout.

Derived:

1. a full 512-state unitary dilation with exact code mapping, old-register
   clearing, adjoint inverse, and total-number commutator;
2. the `r=0,1` physical Cycle-418 intertwiner and compression;
3. connected bounded layout and all-frame covariance;
4. target-blank refusal plus transfer/sign/direction deletion visibility;
5. held response-controlled one-edge propagation, global excitation balance,
   and exact return to the Cycle-416 balance code;
6. the quantitative comparison with Cycle 419's copied-port interface.

Open:

1. primitive synthesis and autonomous preparation/occurrence of the blank
   target block;
2. a full cubic recurrent field, return/reabsorption, stationary dressed-state
   selection, and static response;
3. carried matter, multiparticle FSWAP transport, contact/recoil balance,
   coupling, and calibration;
4. identification of the excitation coordinate as a physical resource,
   energy, stress, or source;
5. Records, physical time, tensor/metric response, gravity, probability, and
   realized-history law.

The source/field meaning, sign, angle, blank target, update schedule, and
response-control binding remain supplied structure. No actual Record is
formed. A generator is not called a rate, and an update count is not called
time.

## Ledger effect and science disposition

- `C_ref`: unchanged; phase, normalization, coupling, and blank-target genesis
  remain supplied.
- `C_num`: the exact excitation ledger now runs from the original Cycle-416
  source/mediator code through physical transfer and propagation, without the
  Cycle-417 fanout.
- `C_wrap`: unchanged; no update count is promoted to physical time.
- `C_int`: response-controlled exchange and directed propagation share the
  transferred code; contact, recoil, carried matter, and recurrence remain.
- `C_local`: one fixed bounded physical `W` replaces the non-square seed at the
  source/field seam, with inverse, frames, deletion, domain, and held controls.
- `C_source`: the coherent response reaches a balanced propagating field code;
  physical source selection, response calibration, static/tensor/metric action,
  and gravity remain open.

Science disposition: Cycle 422 certifies the declared number-preserving
Cycle-416-to-field transfer and one-edge recurrent propagation. It does not
certify a general field receiver, physical resource law, static response, or
gravity. There is no shared obstruction and no axiom pressure.

## Reproduction

```bash
python3 -u \
  scripts/physical_number_preserving_cycle416_field_transfer_cycle422_2026_07_19.py
```

Expected cold result: all checks pass and

```text
RESULT PHYSICAL_NUMBER_PRESERVING_CYCLE416_FIELD_TRANSFER_CERTIFIED
```
