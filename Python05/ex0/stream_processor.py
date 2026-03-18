#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Optional


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a raw result string."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if the data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string. Can be overridden by subclasses."""
        return result


class NumericProcessor(DataProcessor):
    """Processor for numeric lists."""

    def __init__(self) -> None:
        super().__init__()
        print("Initializing Numeric Processor...")

    def validate(self, data: Any) -> bool:
        # Use List and Union type hints as required
        if isinstance(data, list):
            numbers: List[Union[int, float]] = data
            return all(isinstance(x, (int, float)) for x in numbers)
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        count = len(data)
        total = sum(data)
        avg = total / count if count else 0.0
        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text strings."""

    def __init__(self) -> None:
        super().__init__()
        print("Initializing Text Processor...")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        char_count = len(data)
        word_count = len(data.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entries with level detection."""

    # Use Dict for level mapping (optional, to demonstrate Dict usage)
    _LEVEL_PREFIXES: Dict[str, str] = {
        "ERROR": "[ALERT] ",
        "WARNING": "[WARN] ",
        "INFO": "[INFO] "
    }

    def __init__(self) -> None:
        super().__init__()
        print("Initializing Log Processor...")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        # Extract log level if present
        level: str = "INFO"
        message: str = data
        if data.startswith("ERROR:"):
            level = "ERROR"
            message = data[len("ERROR:"):].strip()
        elif data.startswith("INFO:"):
            level = "INFO"
            message = data[len("INFO:"):].strip()
        elif data.startswith("WARNING:"):
            level = "WARNING"
            message = data[len("WARNING:"):].strip()
        return f"{level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Add severity brackets based on the detected level."""
        for level, prefix in self._LEVEL_PREFIXES.items():
            if result.startswith(level):
                return prefix + result
        return "[LOG] " + result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    # Instantiate processors
    print()
    num_proc = NumericProcessor()
    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    if num_proc.validate(data_num):
        print("Validation: Numeric data verified")
        try:
            raw = num_proc.process(data_num)
            formatted = num_proc.format_output(raw)
            print(f"Output: {formatted}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Validation failed")

    print()
    text_proc = TextProcessor()
    data_text = "Hello Nexus World"
    print(f"Processing data: {repr(data_text)}")
    if text_proc.validate(data_text):
        print("Validation: Text data verified")
        try:
            raw = text_proc.process(data_text)
            formatted = text_proc.format_output(raw)
            print(f"Output: {formatted}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Validation failed")

    print()
    log_proc = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f"Processing data: {repr(data_log)}")
    if log_proc.validate(data_log):
        print("Validation: Log entry verified")
        try:
            raw = log_proc.process(data_log)
            formatted = log_proc.format_output(raw)
            print(f"Output: {formatted}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Validation failed")

    
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    # Demo with the same processor instances
    demo_data = [
        ([1, 2, 3], num_proc),
        ("Hello World!", text_proc),
        ("INFO: System ready", log_proc),
    ]

    for i, (data, processor) in enumerate(demo_data, 1):
        try:
            raw = processor.process(data)
            formatted = processor.format_output(raw)
            print(f"Result {i}: {formatted}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()