class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        i = 0 
        parties = {
            "R": ["Radiant", 0],
            "D": ["Dire", 0]
        }
        while True:
            char = senate[0]
            if char == 'D':
                r_count = parties['R'][1]
                if r_count > 0:
                    parties['R'][1] -= 1
                    senate = senate[1:]
                else:
                    parties['D'][1] += 1
                    senate = senate[1:] + char
            else:
                d_count = parties['D'][1]
                if d_count > 0:
                    parties['D'][1] -= 1
                    senate = senate[1:]
                else:
                    parties['R'][1] += 1
                    senate = senate[1:] + char

            if len(set(senate)) == 1:
                return parties[senate[0]][0]
