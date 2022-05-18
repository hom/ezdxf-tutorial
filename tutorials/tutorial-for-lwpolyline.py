import ezdxf

doc = ezdxf.readfile("../output/lwpolyline2.dxf")
msp = doc.modelspace()

line = msp.query("LWPOLYLINE").first

with line.points("xyseb") as points:
    del points[-2:]
    points.extend([(4, 7), (0, 7)])

doc.saveas("../output/lwpolyline3.dxf")
