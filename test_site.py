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
assert 'assets/chapter-3-things-progress.jpg' in html
assert 'assets/chapter-3-fremont-east.jpg' in html
assert 'assets/chapter-4-craps-winnings.jpg' in html
assert 'assets/chapter-4-things-heat-up.jpg' in html
assert 'assets/chapter-7-tiki-room.jpg' in html
assert 'assets/chapter-eat-casino-floor.jpg' in html
assert 'assets/near-final-chapter-restaurant.jpg' in html
assert 'assets/quick-trip-to-italy.jpg' in html
assert 'Three smiling people taking a neon-lit selfie outside an entertainment venue at night' in html
assert 'Three passengers smiling for a car selfie during the ride to the evening destination' in html
assert 'A smiling person in a red plaid shirt posing beside an oversized red high-heel leg prop in a bright neon souvenir area' in html
assert 'A close-up of a blue video poker machine showing cards, a pay table, and a game over message' in html
assert 'Two people smiling under bright turquoise casino lights while holding a novelty red leg-shaped drink cup' in html
assert 'A Bigfoot-style street performer dancing on a neon-lit pedestrian entertainment strip at night' in html
assert 'The Fremont East District neon sign glowing over a crowded nighttime street scene' in html
assert 'A close-up of casino chips on a craps table rail including a visible one hundred dollar chip and a green chip' in html
assert 'Three people sitting under red and pink tiki bar lighting with a large tiki face decoration behind them' in html
assert 'Three people taking a selfie in a purple and red lit tiki room with thatched decor and a large wall face behind them' in html
assert 'An ornate casino floor with rows of slot machines, patterned carpet, and glowing chandeliers overhead' in html
assert 'Three people taking a restaurant table selfie after a meal with plates, condiments, a brick wall, and framed saxophone art behind them' in html
assert 'Two smiling diners at an Italian-style cafe table with dessert, drinks, and a shopping bag' in html
assert (root / 'assets' / 'chapter-1-prelude.jpg').exists()
assert (root / 'assets' / 'chapter-1-ride-there.jpg').exists()
assert (root / 'assets' / 'chapter-2-night-progresses.jpg').exists()
assert (root / 'assets' / 'chapter-3-video-poker.jpg').exists()
assert (root / 'assets' / 'chapter-3-saga-continues.jpg').exists()
assert (root / 'assets' / 'chapter-3-things-progress.jpg').exists()
assert (root / 'assets' / 'chapter-3-fremont-east.jpg').exists()
assert (root / 'assets' / 'chapter-4-craps-winnings.jpg').exists()
assert (root / 'assets' / 'chapter-4-things-heat-up.jpg').exists()
assert (root / 'assets' / 'chapter-7-tiki-room.jpg').exists()
assert (root / 'assets' / 'chapter-eat-casino-floor.jpg').exists()
assert (root / 'assets' / 'near-final-chapter-restaurant.jpg').exists()
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
assert 'Chapter 3 — Things Progress' in html
assert 'Cryptid Contact Established' in html
assert 'Fremont East Portal Located' in html
assert 'Chapter 4 — Winnings at the Craps Table' in html
assert 'Dice Department Reports Profit' in html
assert 'Chapter 4 — Things Heat Up' in html
assert 'Tiki Tribunal Convenes' in html
assert 'Chapter 7 — The Tiki Room' in html
assert 'Thatched Roof Headquarters Activated' in html
assert 'Chapter Eat — Old School Casino Fremont' in html
assert 'Chandelier Department Opens the Vault' in html
assert 'Near Final Chapter — Dinner Debrief' in html
assert 'Plate Evidence Mostly Destroyed' in html
assert 'Chapter 4 — Dessert Intelligence' in html
assert 'Quick Trip to Italy Confirmed' in html
assert 'the night is no longer casual' in html
assert 'leg lamp is no longer a landmark' in html
assert 'if Bigfoot joins the itinerary' in html
assert 'Fremont East has been located' in html
assert 'dice have spoken' in html
assert 'volcano mode' in html
assert 'tiki room is not a location' in html
assert 'Fremont old-school casino energy has been confirmed' in html
assert 'food has been investigated thoroughly' in html
assert 'good pay table, suspicious cards' in html
assert 'https://github.com/jdesgarennes/quick-trip-to-italy-briefing' in html
print('Smoke test passed')
