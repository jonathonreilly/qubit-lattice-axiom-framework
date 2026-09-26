# Referee: no-local-interaction-keeps-excluded-records-books a2

Worker `w-macbookpro90c72-j37c1` (`grok-4.6`). Author `w-macbookpro9927a-j84a4` (`claude-opus-5-5`). The attempt's script is not imported.

## Verdict

Confirmed no-go. No finite-range interaction with a local placement keeps the total energy current of two excluded records, on `Z^2` or on `Z^3`.

## What was checked

- **The resolvent identity.** On a fresh rank-2 fiber, with a double shell, `[g, T(z)] = (h0 − z)[F2, R(z)](h0 − z)` at two generic energies. On the shell the sandwich is `iη` times the mixed remainder.
- **Push-through.** `T = A W (1 + Q0 W)^{-1} A*`, `(1 + F1 R0)(1 − F1 R) = 1`, and the two determinants multiply to 1.
- **Sylvester.** `det(1 + W(Q − c Γ)) = det(1 + W Q) det(1 − c B* M B)` identically in `c`. Transparency makes the second factor 1, so the boundary values of `Δ` agree.
- **The placement.** `[h,[h,f]] = 4(|h|² f − (h·f)h)`, and it vanishes when `f` is parallel to `h`. The two-record double commutator splits into the two one-body pieces.
- **The shell witness.** `g = sin K cos 2q`. At the Pythagorean point the shell derivatives are `−2002/7225` in the plane and in space, and the wedge with the band gradient is nonzero.
- **The cones.** At `tan K0 = (5/6, 18/5)` and `(5/6, 18/5, 1/2)` the tilts are `139761000/606502321` and `2653455542/8714332815`, both below 1.
- **The line.** Both two-point shells carry one value of `g`.

The passage from these identities to `Δ = 1`, and the contradiction with the removed on-site states, uses the named theorems I1–I8. Those theorems are not re-proved.
