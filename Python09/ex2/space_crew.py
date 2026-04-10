from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)  # fixed
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(crew.rank in (Rank.captain, Rank.commander)
                   for crew in self.crew):
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(1 for crew in self.crew
                              if crew.years_experience >= 5)
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )

        if not all(crew.is_active for crew in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    # Valid mission (matches expected output)
    crew_list = [
        CrewMember(
            member_id="CREW001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=20,
            is_active=True,
        ),
        CrewMember(
            member_id="CREW002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=38,
            specialization="Navigation",
            years_experience=12,
            is_active=True,
        ),
        CrewMember(
            member_id="CREW003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=32,
            specialization="Engineering",
            years_experience=8,
            is_active=True,
        ),
    ]

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 6, 1),
        duration_days=900,
        crew=crew_list,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for crew in valid_mission.crew:
        print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")
    print("\n=========================================")

    # Invalid mission: missing commander/captain
    invalid_crew = [
        CrewMember(
            member_id="CREW004",
            name="Nobody",
            rank=Rank.cadet,
            age=25,
            specialization="Janitor",
            years_experience=1,
            is_active=True,
        )
    ]

    print("Expected validation error:")
    try:
        _ = SpaceMission(
            mission_id="M999_BAD",
            mission_name="Bad Mission",
            destination="Nowhere",
            launch_date=datetime(2025, 1, 1),
            duration_days=30,
            crew=invalid_crew,
            budget_millions=10.0,
        )
    except ValidationError as e:
        # Print only the first error message as in the example
        error_msg = str(e.errors()[0]["msg"]) if e.errors() else str(e)
        print(error_msg)


if __name__ == "__main__":
    main()
