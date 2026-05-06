from dataclasses import dataclass
from model.flights import Flight


@dataclass

class Arco:
    o1:Flight
    o2:Flight
    peso: float