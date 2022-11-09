from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        training = 0
        best_exp = max(experience)+1
        best_eng = sum(energy) + 1
        if initialEnergy >= best_eng and initialExperience >= best_exp:
            return 0
        if (initialExperience >= best_exp):
            training = best_eng - initialEnergy
            return training

        if (initialExperience < best_exp):
            sum = initialExperience
            i = 0
            for exp in experience:
                if sum <= exp:
                    training += exp - sum + 1
                    sum += exp - sum + 1 + exp
                else:
                    sum += exp
            if initialEnergy < best_eng:
                training += best_eng - initialEnergy
            return training
