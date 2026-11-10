# Execution measurement correction

The preserved execution receipts use the original key `peak_rss_kib`.
Its actual meaning is **maximum sampled RSS**, with a 0.2-second polling
interval. It is not a guaranteed process peak. Very short rejection runs
can finish between samples; values such as 160 or 240 KiB can precede
Python startup and substantially underestimate memory use. The resource
monitor also applies its limit only at those samples.

The receipts retain their exact independently inspected bytes and hashes.
This note corrects the interpretation rather than replacing the original
evidence. Command vectors, exit codes, elapsed times, scientific stdout,
stderr and certificates are unchanged. No memory-use comparison between
the short controls is justified by these samples.
