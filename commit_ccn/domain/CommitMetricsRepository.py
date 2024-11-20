from abc import ABC, abstractmethod
from typing import List
from domain.CommitMetrics import CommitMetrics

class CommitMetricsRepository(ABC):
    @abstractmethod
    def get_ccn_by_commit(self) -> List[CommitMetrics]:
        pass