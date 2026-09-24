# Transfer-phase runner mutation check

The runner was imported and its expected polynomial function was deliberately
mutated to `P5(u,z)=0`, then the symbolic expansion gate was called. It raised
`ArithmeticError: five-site trace coefficient` at the second-order trace
identity. The incorrect value did not pass. This tests that the gate depends
on the implemented second-order result rather than only on a by-construction
determinant or inverse identity.

This is a manual author mutation check at the campaign source revision; it is
not an independent review receipt.
