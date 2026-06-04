# Route Portfolio

## R1 Parent-Source Constant Repair

Status: shipped in this branch.

Replace `v_LR = 2 e J R_int Z_lat` by the conservative finite-range
source constant `v_LR = 2 e J_* R_int D_int`.

## R2 Parent-Source Eq(8) Removal

Status: shipped in this branch.

Remove the false imaginary-time commutator identity from Step 4 and
route L2 only through separately retained gap/transfer authorities.

## R3 Full L2 Closure

Status: still open.

Would require a retained proof of `Delta_T > 0` or `Delta_x > 0` on
the canonical finite-block surface, plus independent audit of the
spatial/temporal cluster route.
