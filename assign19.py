class Pen:
    def write(self):
        print("Pen is writing")


class Pencil:
    def write(self):
        print("Pencil is writing")


class Marker:
    def write(self):
        print("Marker is writing")


pen = Pen()
pencil = Pencil()
marker = Marker()

items = [pen, pencil, marker]

for item in items:
    item.write()