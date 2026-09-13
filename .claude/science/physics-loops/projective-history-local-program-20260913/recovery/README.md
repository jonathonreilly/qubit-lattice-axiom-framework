# Initial program checker failure

The original checker used structural symbolic matrix equality P*P==P in
its program recognizer. A valid projector containing sqrt(2) produced an
unexpanded polynomial expression, so the decoder returned None and the
caller raised TypeError while unpacking it. The final checker simplifies
each entry of P*P-P exactly before comparison and adds the actual radical
program as an explicit control. No probability, algebraic law, numerical
tolerance or physical scope was changed. Original source/stdout/stderr are
preserved here; the theorem requires the mathematical idempotent identity.
