def get_coords(position, size):
    x, y = position
    w, h = size
    x1 = x - w // 2
    y1 = y - h // 2
    x2 = x + w // 2
    y2 = y + w // 2
    return x1, y1, x2, y2
