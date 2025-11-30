from abc import ABC, abstractmethod
import math
import time


class MovementStrategy(ABC):
    @abstractmethod
    def calculate_offset(self, initial_offset, elapsed_time):
        pass


class VerticalOscillationStrategy(MovementStrategy):
    def __init__(self, range_val, speed):
        self._range = range_val
        self._speed = speed
        self._direction = 1
    
    def calculate_offset(self, current_offset, elapsed_time):
        new_offset = current_offset + self._speed * self._direction
        
        if abs(new_offset) >= self._range:
            self._direction *= -1
        
        return new_offset


class SineWaveStrategy(MovementStrategy):
    def __init__(self, amplitude, frequency):
        self._amplitude = amplitude
        self._frequency = frequency
        self._start_time = time.time()
    
    def calculate_offset(self, current_offset, elapsed_time):
        return int(
            self._amplitude * math.sin(2 * math.pi * self._frequency * elapsed_time)
        )


class StaticStrategy(MovementStrategy):
    def calculate_offset(self, current_offset, elapsed_time):
        return 0