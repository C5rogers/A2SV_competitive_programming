class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round((celsius * 9/5) + 32, 5)
        return [kelvin, fahrenheit]