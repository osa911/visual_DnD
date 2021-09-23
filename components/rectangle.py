from utils.screen import get_coords

class DragRect():
    def __init__(self, centerPosition, size=[200, 200]):
        self.centerPosition = centerPosition
        self.size = size

    def update(self, cursor):
        # cx, cy = self.centerPosition
        # w, h = self.size
        cx1, cy1, cx2, cy2 = get_coords(self.centerPosition, self.size)
        # If the index tip is in the rectangle region
        if cx1 < cursor[0] < cx2 and cy1 < cursor[1] < cy2:
            colorR = 0, 255, 0
            self.centerPosition = cursor
