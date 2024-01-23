class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_list = list(senate)
        while 1:
            current_senator = senate_list.pop(0)
            if len(senate_list) == 0:
                return "Dire" if current_senator == 'D' else 'Radiant'
            for i in range(len(senate_list)):
                if current_senator != senate_list[i]:
                    senate_list.pop(i)
                    break
                if i == len(senate_list)-1:
                    return "Dire" if current_senator == 'D' else 'Radiant'
            
            senate_list += current_senator
