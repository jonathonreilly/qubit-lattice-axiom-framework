# Preserved integration corrections

The first integration execution stopped because Python min attempted to order
independent positive symbolic variables in the error-bound guard. Replacing that
with separate nonnegativity comparisons permits the symbolic identity check.
The second execution returned43passing and1failing control: the derivative of
(1+q)/(1+q*q) at q=1 was mistakenly expected to be zero. It is -1/2; the
control now verifies the actual symbolic derivative at both q=0 and q=1.
No theorem changed in either integration correction. Raw stdout/stderr and
execution receipts for both attempts remain here.

The first cache-envelope attempt also rejected directory identity drift when a
Python bytecode directory appeared under scripts. Source bytes and input hashes
were unchanged in its diagnostic. The rerun sets PYTHONDONTWRITEBYTECODE=1,
without weakening the identity guard. No scientific conclusion follows from that
operational failure. The earlier genuine missing s*F2 sensitivity term is
explained and corrected in the source note; its exploratory originals remain
in the campaign checkpoint.
