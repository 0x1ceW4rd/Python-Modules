from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if (self.contact_type == ContactType.physical
                and not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact require at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Valid contact
    try:
        valid = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 10, 5, 14, 30, 0),
            location="rea 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )
        print("Valid contact report:")
        print(f"ID: {valid.contact_id}")
        print(f"Type: {valid.contact_type.value}")
        print(f"Location: {valid.location}")
        print(f"Signal: {valid.signal_strength}/10")
        print(f"Duration: {valid.duration_minutes} minutes")
        print(f"Witnesses: {valid.witness_count}")
        print(f"Message: '{valid.message_received}'")
    except ValidationError as e:
        print("Unexpected validation errors:")
        for error in e.errors():
            print(f"  - {error['msg']}")

    print("\n" + "=" * 40 + "\n")

    # Invalid contact (telepathic with only 2 witnesses)
    try:
        invalid = AlienContact(
            contact_id="ACBAD001",
            timestamp=datetime.now(),
            location="Andromeda",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
        )
        print("Valid contact report:")
        print(f"ID: {invalid.contact_id}")
        print(f"Type: {invalid.contact_type.value}")
        print(f"Location: {invalid.location}")
        print(f"Signal: {invalid.signal_strength}/10")
        print(f"Duration: {invalid.duration_minutes} minutes")
        print(f"Witnesses: {invalid.witness_count}")
        print(f"Message: '{invalid.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(f"{error['msg']}")


if __name__ == "__main__":
    main()
