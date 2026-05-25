# Strict W/Z Response Packet Attempt

Outcome: exact support.

Artifact:

```text
docs/YT_STRICT_WZ_NEUTRAL_CARRIER_RESPONSE_PACKET_NOTE_2026-05-25.md
scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py
outputs/yt_strict_wz_neutral_carrier_response_packet_2026-05-25.json
```

The packet proves the denominator-side response rows on the neutral carrier
ray:

```text
dM_W/ds = (g_2/2) v'(s)
dM_Z/ds = (sqrt(g_2^2 + g_Y^2)/2) v'(s)
```

The result closes the W/Z denominator support for the source-coordinate and
FH-ratio gates.  It does not determine the top numerator coefficient, does not
derive physical-scale `g_2(v)`, and does not promote the Y_T lane.

Gate result:

```text
python3 scripts/frontier_yt_strict_wz_neutral_carrier_response_packet.py
SUMMARY: PASS=46 FAIL=0
```
