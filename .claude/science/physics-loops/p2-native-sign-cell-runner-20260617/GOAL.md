# Goal

Repair the P2 Wick-rotation sign-epsilon source row so it is audit-ready on
the current framework wording.

The concrete blocker is that the existing runner checked stale C-Sc wording
and the note still treated textbook reconstruction/classification material as
load-bearing context. This block replaces those with framework-native finite
checks:

- current C-Sc/R-STONE finite transfer-to-unitary language;
- direct real-matrix construction of the Euclidean `Cl(4,0)` sign cell;
- direct real-matrix construction of the Lorentzian `Cl(3,1)` sign cell;
- rank-16 Clifford-monomial checks for both sign cells.

The intended status remains bounded-support. The branch does not audit,
retag, land to main, or promote any source row.
