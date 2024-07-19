from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    if len(my_coordinate_list) <= 17:
        return my_coordinate_list
    else:
        px = Percentiles()
        py = Percentiles()
        pz = Percentiles()
        order_array = []
        for coord in my_coordinate_list:
            px.add_point(coord[0])
            py.add_point(coord[1])
            pz.add_point(coord[2])

        count = 0
        count_max = 1
        max_c = 0

        ratio_num = 43.75

        while count_max != 3:
            ratio_x = px.ratio(ratio_num, ratio_num)
            ratio_y = py.ratio(ratio_num, ratio_num)
            ratio_z = pz.ratio(ratio_num, ratio_num)
            for coord in my_coordinate_list:
                if coord[0] in ratio_x:
                    count += 1
                if coord[1] in ratio_y:
                    count += 1
                if coord[2] in ratio_z:
                    count += 1
                
                if count == 3:
                    max_c = coord
                    count_max = 3
                    break
                
                count = 0
            ratio_num -= 1

        median = max_c

        order_array.append(median)

        oct1 = []
        oct2 = []
        oct3 = []
        oct4 = []
        oct5 = []
        oct6 = []
        oct7 = []
        oct8 = []

            
        for point in my_coordinate_list:
            if point == median:
                continue
            if point[0] >= median[0]:
                if point[1] >= median[1]:
                    if point[2] >= median[2]:
                        oct1.append(point)
                    else:
                        oct2.append(point)
                else:
                    if point[2] >= median[2]:
                        oct3.append(point)
                    else:
                        oct4.append(point)
            else:
                if point[1] >= median[1]:
                    if point[2] >= median[2]:
                        oct5.append(point)
                    else:
                        oct6.append(point)
                else:
                    if point[2] >= median[2]:
                        oct7.append(point)
                    else:
                        oct8.append(point)
                        

        oct1order = make_ordering(oct1)
        oct2order = make_ordering(oct2)
        oct3order = make_ordering(oct3)
        oct4order = make_ordering(oct4)
        oct5order = make_ordering(oct5)
        oct6order = make_ordering(oct6)
        oct7order = make_ordering(oct7)
        oct8order = make_ordering(oct8)

        order_array.extend(oct1order)
        order_array.extend(oct2order)
        order_array.extend(oct3order)
        order_array.extend(oct4order)
        order_array.extend(oct5order)
        order_array.extend(oct6order)
        order_array.extend(oct7order)
        order_array.extend(oct8order)

        return order_array
    