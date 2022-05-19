import ezdxf

doc = ezdxf.new('R2018')

# dxfversion
print(doc.dxfversion)

# acad_release
print(doc.acad_release)

# encoding
print(doc.encoding)

# output_encoding
print(doc.output_encoding)

# filename
print(doc.filename)

# rootdict
print(doc.rootdict)
