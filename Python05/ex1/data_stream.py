#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count: int = 0
        self.last_batch_stats: Dict[str, Union[int, float]] = {}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a descriptive result."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on optional criteria. Default: no filtering."""
        if criteria is None:
            return data_batch
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            **self.last_batch_stats,
        }


class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps: List[float] = []
            humidities: List[float] = []
            pressures: List[float] = []
            for item in data_batch:
                if not isinstance(item, str):
                    raise TypeError("Sensor data must be strings")
                key, value = item.split(":")
                value = float(value.strip())
                if key == "temp":
                    temps.append(value)
                elif key == "humidity":
                    humidities.append(value)
                elif key == "pressure":
                    pressures.append(value)

            self.processed_count += len(data_batch)
            avg_temp = sum(temps) / len(temps) if temps else 0.0
            self.last_batch_stats = {
                "readings": len(data_batch),
                "avg_temp": round(avg_temp, 1),
            }
            return (f"Sensor analysis: {len(data_batch)} "
                    f"readings processed, avg temp: {avg_temp}°C")
        except Exception as e:
            return f"Sensor processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high_priority":
            filtered = []
            for item in data_batch:
                try:
                    key, value = item.split(":")
                    value = float(value)
                    if (key == "temp" and value > 30) or (
                        key == "humidity" and value < 20
                    ):
                        filtered.append(item)
                except Exception:
                    continue
            return filtered
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Stream for financial transactions."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buy_total = 0.0
            sell_total = 0.0
            for item in data_batch:
                if not isinstance(item, str):
                    raise TypeError("Transaction data must be strings")
                parts = item.split(":")
                action = parts[0].strip()
                amount = float(parts[1].strip())
                if action == "buy":
                    buy_total += amount
                elif action == "sell":
                    sell_total += amount
                else:
                    raise ValueError(f"Unknown action: {action}")

            self.processed_count += len(data_batch)
            net_flow = buy_total - sell_total
            sign = "+" if net_flow >= 0 else ""
            self.last_batch_stats = {
                "operations": len(data_batch),
                "net_flow": net_flow,
            }
            return (f"Transaction analysis: {len(data_batch)} "
                    f"operations, net flow: {sign}{net_flow} units")
        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high_priority":
            filtered = []
            for item in data_batch:
                try:
                    action, amount = item.split(":")
                    amount = float(amount)
                    if amount > 200:
                        filtered.append(item)
                except Exception:
                    continue
            return filtered
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    """Stream for system events."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            event_count = len(data_batch)
            error_count = 0
            for item in data_batch:
                if not isinstance(item, str):
                    raise TypeError("Event data must be strings")
                if item == "error":
                    error_count += 1

            self.processed_count += event_count
            self.last_batch_stats = {"events": event_count,
                                     "errors": error_count}
            return (f"Event analysis: {event_count} "
                    f"events, {error_count} error detected")
        except Exception as e:
            return f"Event processing error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high_priority":
            return [item for item in data_batch if item == "error"]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    """Unified processor for any DataStream subtype."""

    def process_batch(self, stream: DataStream, batch: List[Any]) -> str:
        """Polymorphically process a batch through the given stream."""
        try:
            return stream.process_batch(batch)
        except Exception as e:
            return f"Stream processing failed: {e}"

    def filter_batch(
        self, stream: DataStream,
        batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Polymorphically filter a batch."""
        try:
            return stream.filter_data(batch, criteria)
        except Exception:
            return []

    def get_stats(self,
                  stream: DataStream
                  ) -> Dict[str, Union[str, int, float]]:
        """Retrieve statistics from a stream."""
        return stream.get_stats()


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"\nProcessing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"\nProcessing transaction batch: {trans_batch}")
    print(transaction.process_batch(trans_batch))

    event_batch = ["login", "error", "logout"]
    print(f"\nProcessing event batch: {event_batch}")
    print(event.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    batches = [
        (sensor, ["temp:23.1", "humidity:70"]),
        (transaction, ["buy:50", "sell:30", "buy:20", "sell:100"]),
        (event, ["info", "warning", "error", "error"]),
    ]

    print("Batch 1 Results:")
    for stream, batch in batches:
        result = processor.process_batch(stream, batch)
        summary = result.split("\n")[0] if "\n" in result else result
        print(f"- {stream.__class__.__name__}: {summary}")

    print("\nStream filtering active: High-priority data only")
    filtered_results = []
    for stream, batch in batches:
        filtered = processor.filter_batch(stream, batch, "high_priority")
        if filtered:
            filtered_results.append(
                f"{len(filtered)} "
                f"{stream.__class__.__name__.lower().replace('stream', '')}"
                " alerts"
            )
    print(f"Filtered results: {', '.join(filtered_results)}")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
