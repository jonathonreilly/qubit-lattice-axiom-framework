# Referee: a law for the rotation of the coin axes, attempt 2

Attempt `w-jonathonsmac4f50-j330f`. Bond matrices and the torque identity are rebuilt here. The attempt's script is not imported.

The generator on a bond is `ψ_x† (B/(2i)) ψ_y + h.c.`, with `B = Ē·σ` when there is no link. A coin rotation `U(x) ∈ SU(2)` acts by `U (v·σ) U† = (Rv)·σ`.

## Verdicts

**Bond mismatch.** For two rational Cayley rotations and two rational frames, `U_x (Ē·σ) U_y†` differs from the rotated-frame bond by

`(1/2)[U_x (E_x·σ)(U_y† − U_x†) + (U_x − U_y)(E_y·σ) U_y†]`.

The difference has trace `29656048 i / 24115175`, while every frame bond is traceless. So the conjugated generator is not `H[E']` for any frame `E'`.

**First order.** With real angles, `U_x σ_j U_y† = σ_j + (((θ_x+θ_y)/2) × e_j)·σ + (i/2)(θ_y − θ_x)_j + O(θ²)`.

**Links.** `B = (1/2)(E_x·σ W + W E_y·σ)` satisfies `B[RE, U_x W U_y†] = U_x B U_y†`. At `W = 1` it is the averaged frame bond. For a positive diagonal stretch and flat links `W = Û_x Û_y†`, every bond equals the stretch bond conjugated by the lifts, so the walker sees only the stretch. Replacing a lift by its negative leaves the rotation unchanged and flips the link.

**Torque.** On a 3-torus with rational frames, links and states, frame torque plus the link response equals `(1/2) d⟨σ_c⟩/dt` at all 81 site-axis pairs, and every term is nonzero.

**Stationary wave.** On the 4-torus, `Σ_j i^{x_j} c_j` with coins `(1,1)`, `(1,i)` and `(1,0)` is an energy `+1` eigenstate of the identity-frame, link-free generator. Its spin is stationary. The frame torque is nonzero at 136 of 192 pairs and equals minus the link response.

**Flat dressing.** Dressing that state and frame by the same site lifts keeps energy `+1`. The total torque vanishes at all 192 pairs. On this independent frame the frame part alone is nonzero at 178 pairs.

**Plaquette.** `Σ Re tr(W_i W_j W_i† W_j†)` on the 3-torus is unchanged by a finite link gauge transformation.

## What stays open

No nearest-neighbour rule fixing the stretch factor `f(S_x, S_y)` was constructed, and the links were not given dynamics. The comparison with a torsion-free continuum connection was not made.

## Result

HIT: confirmed. Covariant SU(2) links make a local coin rotation a symmetry to all orders. Flat links leave only the stretch. On a stationary state the frame torque vanishes exactly when the link response does.
