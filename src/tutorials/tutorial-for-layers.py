import ezdxf

doc = ezdxf.new(setup=True)
msp = doc.modelspace()
doc.layers.add(name="MyLines", color=7, linetype="DASHED")
msp.add_line((0, 0), (10, 0), dxfattribs={"layer": "MyLines"})

doc.saveas("output/layer.dxf")
