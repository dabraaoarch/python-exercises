from dataclasses import dataclass
from abc import ABC, abstractmethod
import math

class Factor(ABC):
	growth_rate: float
	growth_multiplier: int 

	def getGrowthRate(self) -> float:
		return self.multiplier * math.log(self.growth_rate)
		
		
@dataclass
class Crime(Factor):
	""" Class to represent crime growth in the simulator """
			
		

@dataclass
class Taxes(Factor):
	""" Class to represent taxes growth """



@dataclass
class Evasion(Factor):
	""" Class to represent taxes evasion growth """
		

		
@dataclass
class Police(Factor):
	""" Class to represent police force growth """
	causality: Causality
		
	def getGrowthRate(self) -> float:
		return super().getGrowthRate() - self.causality.getGrowthRate()


@dataclass
class Causality(Factor):
	""" Class to represent causality growth """
