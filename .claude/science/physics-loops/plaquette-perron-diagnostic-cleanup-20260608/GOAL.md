# Goal

Repair the audited conditional defects in `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` without broadening the science surface.

The audit repair target was:

```text
other: correct or remove the one-plaquette reference diagnostic and tighten
admissibility language at parameter endpoints, then re-audit the same bounded
Perron-solve surface.
```

Success means the runner computes the one-plaquette reference from the Haar partition coefficient `c_(0,0)(beta)`, not from an identity-evaluation character sum, and the note/runner no longer call degenerate endpoint rho samples strictly positive.
