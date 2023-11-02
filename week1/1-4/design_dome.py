
material="유리"
thickness=1
diameter=10

def sphere_area():
    global material
    global thickness
    global diameter
    global area
    global weight
    global mars_weight
    global mars_weight_kg
    while(1):
        print("지름: (종료시 0 입력)")
        diameter=float(input())
        if diameter==0:
            break
        print("재질: ")
        material=input()
        print("두께: ")
        thickness=float(input())
        if material == "유리":
            weight=2.4
        elif material == "알루미늄":
            weight=2.7
        elif material == "탄소강":
            weight=7.85
        area=(diameter/2)*(diameter/2)*3.14
        mars_weight=weight*(3.711/9.8)
        mars_weight_kg=mars_weight/1000
        print("재질 ==> {}, 지름 ==> {}, 두께 ==> {}, 면적 ==> {}, 무게 ==> {:.3f}kg".format(material,diameter, thickness,area, mars_weight_kg))

sphere_area()




#3.711 m/s2 (0.376g)
#9.8m/s2
