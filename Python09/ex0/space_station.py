from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main():
    try:
        print("Space Station Data Validation")
        print("=" * 30)

        valid = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2025-04-10T10:00:00",
        )
        print("Valid station created:")
        print(f"ID: {valid.station_id}")
        print(f"Name: {valid.name}")
        print(f"Crew: {valid.crew_size} people")
        print(f"Power: {valid.power_level}%")
        print(f"Oxygen: {valid.oxygen_level}%")
        print("Status: "
              f"{'Operational' if valid.is_operational else 'Nonoperational'}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        # Print only the first error message
        for i, _ in enumerate(e.errors()):
            print(e.errors()[i]["msg"])
    print("=" * 30)
    # Invalid example
    try:
        invalid = SpaceStation(
            station_id="ISS001",
            name="Overcrowded Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2025-04-10T10:00:00",
        )
        print("Valid station created:")
        print(f"ID: {invalid.station_id}")
        print(f"Name: {invalid.name}")
        print(f"Crew: {invalid.crew_size} people")
        print(f"Power: {invalid.power_level}%")
        print(f"Oxygen: {invalid.oxygen_level}%")
        print(f"Status: {invalid.is_operational}")
        print()
    except ValidationError as e:
        print("Expected validation error:")
        # Print only the first error message
        for i, _ in enumerate(e.errors()):
            print(e.errors()[i]["msg"])


if __name__ == "__main__":
    main()
