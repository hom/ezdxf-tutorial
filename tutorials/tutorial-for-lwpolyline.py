import ezdxf

# lwpolyline 3
'''
doc = ezdxf.readfile("../output/lwpolyline2.dxf")
msp = doc.modelspace()

line = msp.query("LWPOLYLINE").first

with line.points("xyseb") as points:
    del points[-2:]
    points.extend([(4, 7), (0, 7)])

doc.saveas("../output/lwpolyline3.dxf")
'''

# lwpolyline 4
'''
doc = ezdxf.new("R2010")
msp = doc.modelspace()

points = [(0, 0, .1, .15), (3, 0, .2, .25), (6, 3, .3, .35), (6, 6)]
msp.add_lwpolyline(points)

doc.saveas("../output/lwpolyline4.dxf")
'''


# lwpolyline 5
'''
doc = ezdxf.new("R2010")
msp = doc.modelspace()

points = [(0, 0, 0, .05), (3, 0, .1, .2, -.5), (6, 0, .1, .05), (9, 0)]
msp.add_lwpolyline(points)

doc.saveas('lwpolyline5.dxf')
'''

# lwpolyline 6

doc = ezdxf.new('R2010')
msp = doc.modelspace()
msp.add_lwpolyline([(0, 0, 0), (10, 0, 1), (20, 0, 0)], format='xyb')
msp.add_lwpolyline([(0, 10, 0), (10, 10, .5), (20, 10, 0)], format='xyb')

doc.saveas("../output/lwpolyline6.dxf")
