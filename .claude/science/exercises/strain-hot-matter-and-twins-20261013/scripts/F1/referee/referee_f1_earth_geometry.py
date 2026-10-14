"""Independent spherical-astronomy check of F2's GW170817 Earth chords."""

from datetime import datetime, timezone
import math

event = datetime(2017, 8, 17, 12, 41, 4, 400000, tzinfo=timezone.utc)
ra_deg = 197.4488
dec_deg = -23.3839
earth_radius_km = 6371.0


def julian_date(value):
    return value.timestamp() / 86400.0 + 2440587.5


def altitude_and_chord(latitude_deg, longitude_east_deg):
    jd = julian_date(event)
    delta = jd - 2451545.0
    gmst = (280.46061837 + 360.98564736629 * delta
            + 0.000387933 * (delta / 36525.0) ** 2
            - (delta / 36525.0) ** 3 / 38710000.0) % 360.0
    hour_angle = math.radians((gmst + longitude_east_deg - ra_deg) % 360.0)
    lat = math.radians(latitude_deg)
    dec = math.radians(dec_deg)
    altitude = math.asin(
        math.sin(lat) * math.sin(dec)
        + math.cos(lat) * math.cos(dec) * math.cos(hour_angle)
    )
    altitude_deg = math.degrees(altitude)
    chord_km = max(0.0, -2.0 * earth_radius_km * math.sin(altitude))
    closest_approach_km = earth_radius_km * math.cos(altitude)
    return altitude_deg, chord_km, closest_approach_km


sites = {
    "H1": (46.4551, -119.4079),
    "L1": (30.5629, -90.7742),
    "V1": (43.6314, 10.5045),
}

for name, coordinates in sites.items():
    altitude, chord, closest = altitude_and_chord(*coordinates)
    print(f"{name} altitude_deg={altitude:+.3f} chord_km={chord:.1f} closest_km={closest:.1f}")
