from dataclasses import dataclass
from queue import PriorityQueue

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

@dataclass
class Message:
    event: str

messages = PriorityQueue()
wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

wipers < hazard_lights

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)