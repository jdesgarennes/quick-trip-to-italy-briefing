from pathlib import Path

root = Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf-8')

assert '<title>Quick Trip to Italy Operations Briefing</title>' in html
assert 'Quick Trip to Italy Operations Briefing' in html
assert 'assets/quick-trip-to-italy.jpg' in html
assert 'Two smiling diners at an Italian-style cafe table with dessert, drinks, and a shopping bag' in html
assert (root / 'assets' / 'quick-trip-to-italy.jpg').exists()
assert 'Gelato Containment Level' in html
assert 'Fork Readiness' in html
assert 'Executive Summary' in html
assert 'https://github.com/jdesgarennes/quick-trip-to-italy-briefing' in html
print('Smoke test passed')
