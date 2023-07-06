class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, newwidth):
        self.width = newwidth

    def set_height(self, newheight):
        self.height = newheight

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal

    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            self.picture = ""
            for i in range(self.height):
                self.picture += "*" * self.width + "\n"
            return self.picture
        
    def get_amount_inside(self, shape):
        self.shape = shape
        self.amount = self.get_area() // self.shape.get_area()
        return self.amount




class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)


    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, newwidth):
        self.width = newwidth
        self.height = newwidth
    
    def set_height(self, newheight):
        self.height = newheight
        self.width = newheight
      

