#A Layover Planner is a tool that helps travelers decide whether they have enough time to leave the airport and explore the city during a layover. It considers factors such as whether the flight is domestic or international, visa requirements, and how long it takes to travel between the airport and the city. Based on these details, it helps travelers figure out whether going out to explore is realistic or if it’s safer to stay at the airport until their next flight.
def layover_advice(layover_hours, international, needs_visa,
                   travel_minutes_to_city):
    """Decide whether it is worth leaving the airport during a layover."""
    if international and needs_visa:
        return "Stay in the airport: you need a visa to enter."

    # Time you must keep for check-in/security before the next flight
    buffer = 3 if international else 2
    # Time to pass immigration when you arrive from abroad
    immigration = 1.5 if international else 0
    # Round trip to the city and back
    travel_hours = travel_minutes_to_city * 2 / 60

    free_hours = layover_hours - buffer - immigration - travel_hours

    if free_hours >= 2:
        return f"Go into the city! You will have about {free_hours:.1f} hours of free time."
    elif free_hours >= 0.5:
        return f"Only {free_hours:.1f} hours free: stay near the airport."
    else:
        return "Stay in the airport: not enough time."


# (layover hours, international, needs visa, minutes to city)
trips = [
    (10, True, False, 45),
    (5, True, False, 60),
    (6, False, False, 30),
    (8, True, True, 30),
    (7, True, False, 60),
]

for layover, intl, visa, minutes in trips:
    print(f"Layover {layover}h -> {layover_advice(layover, intl, visa, minutes)}")