from dataclasses import dataclass, field
from heap import MaxHeap

@dataclass(order= True)
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    sort_index: int = field(init=False, repr= False)
    greed_value: int = field(init=False, repr = False)

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __post_init__(self):
        self.update_greed()

    def update_greed(self):
        self.greed_value = min(self.capacity, self.volume) * self.nutrient_factor
        self.sort_index = self.greed_value

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.beeHeap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        max_beehives = len(self.beeHeap.the_array) - 1
        self.beeHeap = MaxHeap(max_beehives)

        for hives in hive_list:
            self.beeHeap.add(hives)
    
    def add_beehive(self, hive: Beehive):
        self.beeHeap.add(hive)
    
    def harvest_best_beehive(self) -> float:
        best = self.beeHeap.get_max()
        best_emeralds = best.greed_value
        best.volume -= best.capacity
        best.update_greed()
        self.beeHeap.add(best)
        return best_emeralds
