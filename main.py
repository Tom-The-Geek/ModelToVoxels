import json
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <INPUT>")
    exit()

INPUT = sys.argv[1]

print("Reading: {}...".format(INPUT))

with open(INPUT) as f:
    data = json.load(f)

cubes = data["elements"]

output = []
output.append("public static VoxelShape SHAPE = Shapes.or(")

for index, cube in enumerate(cubes):
    if index == len(cubes) - 1:
        ln = "\tBlock.box({}, {}, {}, {}, {}, {}));"
        x1, y1, z1 = cube["from"]
        x2, y2, z2 = cube["to"]
        output.append(ln.format(x1, y1, z1, x2, y2, z2))
    else:
        ln = "\tBlock.box({}, {}, {}, {}, {}, {}),"
        x1, y1, z1 = cube["from"]
        x2, y2, z2 = cube["to"]
        output.append(ln.format(x1, y1, z1, x2, y2, z2))


result = "\n".join(output)

print("\n" * 4)
print(result)
