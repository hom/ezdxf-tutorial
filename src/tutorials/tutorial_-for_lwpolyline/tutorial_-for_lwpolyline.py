import ezdxf

# lwpolyline 3
'''
doc = ezdxf.readfile("output/lwpolyline2.dxf")
msp = doc.modelspace()

line = msp.query("LWPOLYLINE").first

with line.points("xyseb") as points:
    del points[-2:]
    points.extend([(4, 7), (0, 7)])

doc.saveas("output/lwpolyline3.dxf")
'''

# lwpolyline 4
'''
doc = ezdxf.new("R2010")
msp = doc.modelspace()

points = [(0, 0, .1, .15), (3, 0, .2, .25), (6, 3, .3, .35), (6, 6)]
msp.add_lwpolyline(points)

doc.saveas("output/lwpolyline4.dxf")
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
'''
doc = ezdxf.new('R2010')
msp = doc.modelspace()
msp.add_lwpolyline([(0, 0, 0), (10, 0, 1), (20, 0, 0)], format='xyb')
msp.add_lwpolyline([(0, 10, 0), (10, 10, .5), (20, 10, 0)], format='xyb')
msp.add_lwpolyline([(0, 20, 0.5), (10, 20, 0)], format="xyb")
msp.add_lwpolyline([(0, 30, 2), (10, 30, 0)], format="xyb")
msp.add_lwpolyline([(0, 40, 0.5), (10, 40, 0), (20, 40, -0.5), (30, 40, 0)],
                   format="xyb")
msp.add_lwpolyline([(0, 50, 0.5), (10, 50, -0.5), (20, 50, 0)],
                   format="xyb")

doc.saveas("output/lwpolyline6.dxf")
'''

# lwpolyline 7
'''
doc = ezdxf.new('R2018', setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()
msp.add_lwpolyline([(0.3111, 0, -0.7627), (-3.7404, 0, 0.7627),
                    (-7.7919, 0, 0)],
                   format='xyb')
msp.add_linear_dim(base=[0, 12], p1=(0.3111, 0), p2=(0, 0), dimstyle="EZDXF")


msp.add_lwpolyline([(0, 10, -0.7627), (-4.0515, 10, 0.7627),
                    (-8.1030, 10, 0)],
                   format='xyb')

msp.add_line((0, 0), (0, 20))

doc.saveas("output/lwpolyline7.dxf")
'''

'''
doc = ezdxf.new('R2018', setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

msp.add_lwpolyline([(0, 0, 1), (0, 10, 1), (0, 0, 0)], close=True, format="xyb", dxfattribs={"const_width": 0.4})

doc.saveas("output/lwpolyline8.dxf")
'''

doc = ezdxf.new('R2018', setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

circle = msp.add_circle(center=(0, 0), radius=10, dxfattribs={"color": ezdxf.const.GREEN})
circle.to_spline()

doc.saveas("output/lwpolyline9.dxf")
