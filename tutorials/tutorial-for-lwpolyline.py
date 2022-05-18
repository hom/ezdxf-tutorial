import ezdxf

doc = ezdxf.new('R2010')
msp = doc.modelspace()

points = [(0, 0), (3, 0), (6, 3), (6, 6)]
msp.add_lwpolyline(points)

line = msp.query("LWPOLYLINE").first
print(line[0])
if line is not None:
    line.append_points([(8, 7), (10, 7)])

doc.saveas("../output/lwpolyline.dxf")
