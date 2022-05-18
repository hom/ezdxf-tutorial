import ezdxf

doc = ezdxf.new(setup=True)

doc.saveas('output/created.dxf')
