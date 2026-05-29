from pathlib import Path

root = Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf-8')

assert '<title>Quick Trip to Italy: Night Mission Log</title>' in html
assert 'Quick Trip to Italy: Night Mission Log' in html
assert 'assets/chapter-1-prelude.jpg' in html
assert 'assets/chapter-1-ride-there.jpg' in html
assert 'assets/chapter-2-night-progresses.jpg' in html
assert 'assets/chapter-3-video-poker.jpg' in html
assert 'assets/chapter-3-saga-continues.jpg' in html
assert 'assets/quick-trip-to-italy.jpg' in html
assert 'Three smiling people taking a neon-lit selfie outside an entertainment venue at night' in html
assert 'Three passengers smiling for a car selfie during the ride to the evening destination' in html
assert 'A smiling person in a red plaid shirt posing beside an oversized red high-heel leg prop in a bright neon souvenir area' in html
assert 'A close-up of a blue video poker machine showing cards, a pay table, and a game over message' in html
assert 'Two people smiling under bright turquoise casino lights while holding a novelty red leg-shaped drink cup' in html
assert 'Two smiling diners at an Italian-style cafe table with dessert, drinks, and a shopping bag' in html
assert (root / 'assets' / 'chapter-1-prelude.jpg').exists()
assert (root / 'assets' / 'chapter-1-ride-there.jpg').exists()
assert (root / 'assets' / 'chapter-2-night-progresses.jpg').exists()
assert (root / 'assets' / 'chapter-3-video-poker.jpg').exists()
assert (root / 'assets' / 'chapter-3-saga-continues.jpg').exists()
assert (root / 'assets' / 'quick-trip-to-italy.jpg').exists()
assert 'Chapter 1 — Prelude' in html
assert 'Neon Contact Established' in html
assert 'Chapter 1 — Ride There' in html
assert 'Transport Unit Morale Check' in html
assert 'Chapter 2 — Casino Math Department' in html
assert 'Royal Flush Briefing Denied' in html
assert 'good pay table, suspicious cards' in html
assert 'Chapter 3 — The Night Progresses' in html
assert 'Souvenir District: Leg Lamp Encounter' in html
assert 'Chapter 3 — The Saga Continues' in html
assert 'Leg Lamp Acquisition Verified' in html
assert 'Chapter 4 — Dessert Intelligence' in html
assert 'Quick Trip to Italy Confirmed' in html
assert 'the night is no longer casual' in html
assert 'leg lamp is no longer a landmark' in html
assert 'good pay table, suspicious cards' in html
assert 'https://github.com/jdesgarennes/quick-trip-to-italy-briefing' in html
print('Smoke test passed')
