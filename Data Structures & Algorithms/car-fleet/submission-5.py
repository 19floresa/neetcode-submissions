class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Setup
        n = len(position)
        cars = [ [ position[i], speed[i] ] for i in range(n) ]
        cars.sort()
        
        fleets = []
        for i in range(n-1, -1, -1):
            car = (target - cars[i][0]) / cars[i][1]
            if not fleets:
                fleets.append(car)
            else:
                car2 = fleets[-1]
                if car > car2:
                    fleets.append(car)
        return len(fleets)

        