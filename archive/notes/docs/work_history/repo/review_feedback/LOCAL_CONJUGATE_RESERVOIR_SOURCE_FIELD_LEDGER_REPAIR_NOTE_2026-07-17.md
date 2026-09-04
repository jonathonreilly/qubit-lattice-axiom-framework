# Local conjugate-reservoir source/field ledger repair

Date: 2026-07-17

Authority: none

Audit: unset

Constitutional effect: none

Scientific type: bounded physical-M2 source-port locality repair

This result is an operator-level excitation ledger.  It is not energy, stress,
a clock rate, a Record, or an occurrence law.  It is not a gravity source.
Mass/contact deletion is tested explicitly.  It creates no axiom pressure.

## Question and result

Can emission consume a genuinely local physical excitation, and can absorption
restore it, while the zero/one-mediator sector remains invariant without a
global occupancy service?

Yes, for a **site-local, not carried** reservoir.

Add one reservoir M2 and six directional field M2 factors at every coarse cell.
The existing Cycle-269 matter number is

\[
 N_x={1\over2}\sum_{d=1}^{6}(I-B_{x,d}),
 \qquad M_x=mN_x,
 \qquad m=-3\tan(\beta/2),\quad\beta=-0.3.
\]

On the six field M2 factors define the bounded uniform-scalar creation operator

\[
 b_{s,x}^\dagger={1\over\sqrt6}\sum_{d=1}^{6}
 \sigma^+_{x,d}\prod_{e\ne d}|0\rangle\!\langle0|_{x,e}.
\]

With reservoir lowering operator `sigma^-_r`, set

\[
 T_x=\sigma^-_{r,x}b_{s,x}^\dagger
    +\sigma^+_{r,x}b_{s,x},
 \qquad
 V_x=\exp[-i\kappa M_x\otimes T_x],
 \qquad \kappa=0.8.
\]

The operator is defined on the full local physical-M2 Hilbert space.  It does
not inspect global field occupancy.  The six directional field qubits undergo
a number-preserving onsite coin and a direction-preserving one-edge qubit
shift, both of which are full-Hilbert physical operations.

## Why the zero/one sector is now local

Let

\[
 Q_x=N_{r,x}+N_{f,x},
 \qquad N_{f,x}=\sum_d n_{f,x,d}.
\]

The local exchange obeys

\[
 [T_x,Q_x]=0,\qquad [V_x,Q_x]=0.
\]

The field coin and stream preserve total field number.  Therefore the complete
update preserves

\[
 Q_{\rm total}=\sum_x Q_x.
\]

Preparing `Q_total=1` implies zero or one mediator at every later step.  The
law does not query a global occupancy bit or call a host service before
emission.  With several prepared reservoir excitations, the same law allows
several mediators; the single-mediator restriction is a conserved-sector
initial condition rather than a global control rule.

On the complete seven-M2 reservoir/field block:

| Control | Residual/value |
|---|---:|
| exchange Hermiticity | `0.0` |
| exchange-gate unitarity | `4.004469278125907e-16` |
| `[V,Q]` | `0.0` |
| `Q=1` leakage | `0.0` |
| `Q=1` local dimension | `7` |
| 24-frame covariance | `0.0` |

## Exact conjugate source/field ledger

Define the signed onsite transfer operator

\[
 j_x=V_x^\dagger N_{f,x}V_x-N_{f,x}.
\]

Then

\[
 V_x^\dagger N_{r,x}V_x-N_{r,x}=-j_x
\]

as an exact operator identity.  The residual is

```text
3.4166566809407604e-16.
```

The transfer operator has both signs:

```text
minimum eigenvalue = -0.3548227953904791,
maximum eigenvalue =  0.35482279539047906.
```

Thus the same gate supports emission and absorption.  Starting with reservoir
excited and field vacuum gives field weight

```text
sin^2(kappa m) = 0.12589921612871377.
```

Starting with reservoir ground and the uniform scalar field excitation restores
the reservoir with weight

```text
0.1258992161287138.
```

These are norm weights inside the unitary probe.  They are not named energy,
probability of occurrence, or transition rates.

## Cellwise transported ledger

For a fixed occupied scalar matter control at every cell, the runner constructs
the complete `L=3` reservoir/field one-excitation operator on 27 reservoir
modes and 162 directional field modes.  This is a uniform `N_x=1` control, not
a one-body moving-matter history.  The candidate full schedule is

```text
matter and field onsite coins
  -> local matter-controlled reservoir/field exchange
  -> matter and directional-field streams
  -> arrival-cell ordinary contact.
```

The matter layers and contact commute with reservoir-plus-field number.  If
`J_(x,d)` is the post-coin/post-vertex outgoing directional-field projector,
then

\[
 G^\dagger Q_xG-Q_x
 =\sum_d[J_{x-e_d,d}-J_{x,d}].
\]

Measured operator residuals are:

| Control | Residual |
|---|---:|
| maximum cellwise divergence residual | `1.5167952278789587e-15` |
| maximum local source/reservoir residual | `3.4279119115275734e-16` |
| one-excitation update unitarity | `7.263701286747599e-15` |
| maximum all-24-frame covariance residual | `2.280353229183044e-15` |
| maximum translation residual | `0.0` |

This is an excitation-number continuity equation.  No energy or stress
interpretation is inferred.  The numerical matrix test covers the fixed-control
reservoir/field update.  The operator identity extends to arbitrary local
matter-number controls because each controlled vertex commutes with `Q_x`, but
the runner does not execute matter motion, contact, and field motion together
in one joint Hilbert-space matrix.

## Physical-M2 matter support and leakage

The physical matter control uses only the six mapped `B_(x,d)` operators from
the Cycle-269 connected code.  The local reservoir and field add seven actual
M2 sites.

For `L=3,4,5` and held-out `L=6`:

| quantity | value |
|---|---:|
| matter-number support union | `18 M2` |
| reservoir plus field allocation | `7 M2` |
| complete local vertex support union | `25 M2` |
| maximum expanded `B T` term weight | `12` |
| local-check/Wilson leakage | `0` |
| matter `B` noncommutations | `0` |

The mapped matter scalar passes all `24 x 27 = 648` proper-frame and
translation tests.  The reservoir is a scalar and the uniform field transition
commutes with all 24 proper-cubic frames.

The inherited Cycle-269 matter allocation is 15 M2 per coarse cell.  The
18-M2 operator union crosses the macro-cell boundary; 25 is the bounded gate
support, not a per-cell allocation count.

## Mass, contact, deletion, and composition

`M_x=mN_x` is additive and commutes with the common-family onsite coin and the
ordinary contact

\[
 W_g=\exp[i gN_x(N_x-1)/2],\qquad g=0.37.
\]

Both commutator residuals are `0.0`; `W_g` remains exactly identity at
`N<=1`.  Coupling deletion `kappa=0` returns the identity reservoir/field
vertex with residual `0.0`, leaving

```text
analytic mass   = 0.4534056541748852,
dispersion mass = 0.4534056690336209.
```

The raw scalar rest phase is `0.15113521805829502`, exactly one third of the
mass.  The coupling therefore imports the Cycle-219 `c^-2=3` phase-to-mass
normalization.

Two independent local reservoir vertices commute exactly and their source/
field transfers add with residual `2.6622212897024595e-16`.  A normalized
spectator factor changes the operator ledger by `0.0`.  This is independent
composition.  Co-located several-body finite-angle saturation and mediator
collisions were not tested as an additive source law.

## The unimplemented carried-source extension

The added reservoir is attached to a lattice cell.  It is not yet an internal
state transported with a moving matter body.  The homogeneous local law is
well-defined if matter leaves: the reservoir stays at its cell, and later
absorption requires matter, reservoir, and field to meet under the supplied
matter-controlled vertex.

A carried repair would need one of:

1. a bounded matter-plus-reservoir stream that transports the reservoir flag
   with each matter carrier;
2. a two-species matter code in which excited and ground matter are separate
   internal sectors and the vertex converts them locally; or
3. a reviewed odd/species intertwiner for the present physical CAR code.

The current even-CAR compiler does not supply that internal/species
intertwiner.  This is an exact new compiler/dynamics import, not a global
occupancy obstruction and not a no-go claim.

## Supplied structure

1. the Cycle-269 sectorwise mapped matter code, `B` representatives, local
   constraints, and parity/Wilson sector;
2. `beta=-0.3`, the common-family mass map, and `c^-2=3` normalization;
3. one reservoir M2 and six directional field M2 per coarse cell;
4. the uniform vacuum/one-field transition convention;
5. the full-Hilbert field-coin extension outside the zero/one sector;
6. coupling `kappa=0.8`, its sign and normalization;
7. the coin–vertex–stream–contact schedule;
8. preparation in a declared total reservoir-plus-field excitation sector;
9. a site-local reservoir rather than a carried source;
10. all state preparation, clock, energy/stress/source interpretation, metric
    coupling, and empirical calibration.

The full candidate schedule in item 7 is supplied.  Only its reservoir/field
fixed-control block is executed in the `L=3` continuity matrix; whole-update
matter--reservoir--field intertwining remains open.

## Disposition

Earned:

- a full local physical-M2 conjugate reservoir/field gate;
- exact local and transported operator-level excitation ledgers;
- zero/one-mediator invariance from a conserved prepared sector, with no global
  occupancy service;
- bounded support, zero leakage, proper-cubic covariance, deletion, and
  independent composition;
- preservation of the declared matter mass/contact baseline under deletion.

Not earned:

- a carried source attached to moving matter;
- a prepared full-Fock matter compiler;
- combined matter recoil or field-work balance;
- physical energy, stress, or a selected gravitational source;
- a Cycle-213/216 source/response join;
- clock normalization, tensor geometry, or nonlinear gravity.

No shared obstruction, no broad no-go, and no axiom pressure are claimed.

## Verification

```text
python3 -m py_compile \
  scripts/local_conjugate_reservoir_source_field_ledger_repair_2026_07_17.py

python3 \
  scripts/local_conjugate_reservoir_source_field_ledger_repair_2026_07_17.py
```
