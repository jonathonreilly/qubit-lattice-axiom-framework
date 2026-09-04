# Hypercharge Quark/Lepton Naming and SM Readout Convention

**Type:** meta
**Claim type:** meta
**Status authority:** not applicable. This note records naming, conventional
readout, and chain context only; it is not a theorem or audit-status proposal.

## Purpose

[HYPERCHARGE_IDENTIFICATION_NOTE.md](HYPERCHARGE_IDENTIFICATION_NOTE.md)
proves only the name-free structural (2,3)+(2,1) decomposition, the
+1:(-3) traceless ratio, and the conditional normalized (+1/3,-1) two-block
algebra. This meta note contains every subsequent particle name, Standard
Model readout table, and convention-chain statement.

Nothing here selects a physical species from representation content. A field
or copy with the same representation class has the same algebraic carrier
before a separate physical bridge is supplied.

## Conventional particle naming

After the structural theorem is complete, Standard Model terminology attaches
the following names:

| Structural block | Multiplicity | Normalized Y | Conventional SM name |
|---|---:|---:|---|
| (2,3) = C^2 tensor Sym^2(C^2) | 6 | +1/3 | left-handed quark doublet Q_L |
| (2,1) = C^2 tensor Anti^2(C^2) | 2 | -1 | left-handed lepton doublet L_L |

The labels quark, lepton, Q_L, and L_L are naming/readout conventions. They
perform no work in constructing the projectors, proving their ranks, imposing
tracelessness, or deriving the +1:(-3) ratio.

## Convention chain

The conventional readout uses four logically distinct links:

| Link | Content | Authority and status |
|---|---|---|
| L1 | +1:(-3) on Sym^2 and Anti^2 | structural ratio theorem; theorem-grade input on its own audited scope |
| L2 | structural SU(3) fundamental/trivial classes, followed by Q_L/L_L naming | representation theorem for the classes; particle names are meta convention only |
| L3 | alpha=1/3, equivalently Y(L_L)=-1 in the displayed coordinate | bounded normalization bridge if independently retained; otherwise an explicit supplied convention |
| L4 | Q=T_3+Y/2 at Y_H=+1 and the lower-component vev convention | GMN vev-annihilator support note on its own audit row; the physical component names remain conventional |

The theorem note does not assemble L2-L4 into a physical identification.
This table is the sole home of that convention chain.

## Hypercharge readout table

At the conventional scale alpha=1/3:

| Conventional multiplet | Structural class | Y |
|---|---|---:|
| Q_L | (2,3) | +1/3 |
| L_L | (2,1) | -1 |

This is a post-theorem readout of the normalized algebra, not a derivation of
the physical fermion-sector map.

## Electric-charge readout table

With T_3=sigma_3/2 and the conventional L4 readout Q=T_3+Y/2:

| Particle label | T_3 | Y | Q |
|---|---:|---:|---:|
| u_L, three colors | +1/2 | +1/3 | +2/3 |
| d_L, three colors | -1/2 | +1/3 | -1/3 |
| nu_L | +1/2 | -1 | 0 |
| e_L | -1/2 | -1 | -1 |

The opposite supplied vev direction swaps the component labels. Thus the
component assignment is a convention attached to the readout pattern, not a
new theorem about the structural blocks.

## Conventional consistency displays

On the named left-handed surface:

- Tr(Y)=6(1/3)+2(-1)=0.
- The mixed SU(2)^2-U(1) trace vanishes because
  3(1/3)+1(-1)=0.
- Tr(Y^3) does not vanish on this left-handed surface alone. Full anomaly
  cancellation requires the separately supplied right-handed sector.
- The finite squared trace is 8/3 after alpha=1/3, but this is not a
  grand-unified normalization result or a mixing-angle prediction.

These are downstream checks after the naming and normalization conventions.
They are not evidence for the name-free theorem.

## Historical governance context

The earlier source surface mixed exact commutant algebra with SM naming and
readout tables. Independent review correctly identified that the algebra does
not derive a physical carrier-to-species map. The current split responds by:

1. leaving only projectors, representation classes, the traceless ratio, and
   the supplied normalized two-block spectrum in the bounded theorem;
2. moving Q_L/L_L, u_L/d_L/nu_L/e_L, GMN/EWSB readout, and all conventional
   charge tables here; and
3. keeping every physical naming or normalization bridge on its own audit
   boundary.

## Boundary

This meta note supplies no:

- physical species selector or generation assignment;
- framework-derived hypercharge normalization;
- Higgs dynamics or electroweak-symmetry-breaking derivation;
- anomaly-complete spectrum;
- compact U(1) charge lattice;
- grand-unified embedding or weak-angle prediction;
- retained-status proposal, audit verdict, or effective-status change.

The only theorem-grade content remains in the separate name-free source note
and its exact runner.
