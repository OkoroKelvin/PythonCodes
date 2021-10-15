class Two_Sum:
    def solution(_list: list, number: int):
        _map: dict = {}
        for index, element in enumerate(_list):
            remainder = number - element
            if remainder in map:
                return [_map[remainder], index]
            else:
                _map.update({element: index})
        return [-1, -1]

