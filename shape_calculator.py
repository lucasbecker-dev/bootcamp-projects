class Rectangle:
  def __init__(self, width, height):
    try:
      self.width = int(width)
      self.height = int(height)
    except Exception as err:
      print(err)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self, new_width):
    try:
      self.width = new_width
    except Exception as err:
      print(err)

  def set_height(self, new_height):
    try:
      self.height = new_height
    except Exception as err:
      print(err)
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    res = ""
    print(f"range(self.height): {range(self.height)}")
    for h in range(self.height):
      res += "*" * self.width + "\n"
    print(res)
    return res

  def get_amount_inside(self, rectangle):
    t_area = self.get_area()
    try:
      o_area = rectangle.get_area()
    except Exception as err:
      print(err)
    res = 0
    while (t_area >= o_area):
      res += 1
      t_area -= o_area
    return res

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"
  
  def set_side(self, side):
    try:
      self.height = int(side)
      self.width = int(side)
    except Exception as err:
      print(err)
  
  def set_height(self, new_height):
    self.set_side(new_height)
  
  def set_width(self, new_width):
    self.set_side(new_width)
