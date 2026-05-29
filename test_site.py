from pathlib import Path

root = Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf-8')

assert '<title>Quick Trip to Italy: Night Mission Log</title>' in html
assert 'Quick Trip to Italy: Night Mission Log' in html
assert 'assets/chapter-1-prelude.jpg' in html
assert 'assets/chapter-1-ride-there.jpg' in html
assert 'assets/quick-trip-to-italy.jpg' in html
assert 'Three smiling people taking a neon-lit selfie outside an entertainment venue at night' in html
assert 'Three passengers smiling for a car selfie during the ride to the evening destination' in html
assert 'Two smiling diners at an Italian-style cafe table with dessert, drinks, and a shopping bag' in html
assert (root / 'assets' / 'chapter-1-prelude.jpg').exists()
assert (root / 'assets' / 'chapter-1-ride-there.jpg').exists()
assert (root / 'assets' / 'quick-trip-to-italy.jpg').exists()
assert 'Chapter 1 — Prelude' in html
assert 'Neon Contact Established' in html
assert 'Chapter 1 — Ride There' in html
assert 'Transport Unit Morale Check' in html
assert 'Chapter 2 — Dessert Intelligence' in html
assert 'Quick Trip to Italy Confirmed' in html
assert 'https://github.com/jdesgarennes/quick-trip-to-italy-briefing' in html
print('Smoke test passed')
