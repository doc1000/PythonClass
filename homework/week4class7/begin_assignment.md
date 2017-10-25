class Dog():
   """This docstring will discuss how to interact with our Dog class.

   Our Dog class will have two attributes - a name and happiness_level.
   It's one method, wag_tail, will simulate the dog wagging it's tail
   some number of times, and increasing it's happiness level.

   Parameters:
   -----------
       name: str
       happiness_level: int
   """

   def __init__(self, name, happiness_level=5):
       self.name = name
       self.happiness_level = happiness_level
       pass

   def wag_tail(self, n):
       """Wags the dogs tail n times, and each time increase
       happiness level by 5.

       Args:
           n: int
       """
       pass

   # def name(self):
   #     return __class__.__name__


class Company():
    """
    Args: name - str holding the name of the company
    industry_type - str holding what industry the company belongs to
    num_employees - int holding the number of employees the company has
    total_revenue - float holding the total revenue of the company
    """

    def __init__(self, name, industry_type, num_employees, total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self, cost):
        self.total_revenue += cost

    def gain_employees(self, employees):
        if type(employees) == list:
            self.num_employees += len(employees)
        else:
            print('gain_employees method requires a list to be passed')

class TV():
    """
    brand - str holding the brand of the television ('Sony', 'LG', etc.)
    on_status - bool holding whether or not the television is on. This should default to False (e.g. off).
    current_channel - int holding the current channel number. If the television is off, then the current_channel should be 0. Given that on_status defaults to off, what does that mean the current_channel should default to?
    life_perc - float holding the percentage of life left in the TV. This should start out at 100% (i.e. default to 100).
    """

    def __init__(self, brand, on_status=False, current_channel = 0, life_perc =100):
        self.brand = brand
        self.on_status=on_status
        self.current_channel = current_channel
        self.life_perc = life_perc

    def hit_power(self):
        if self.on_status == True:
            self.life_perc -= 0.01
            self.current_channel = 0
        self.on_status = not self.on_status

    def change_channel(self,channel):
        if self.on_status == False:
            print('television not on')
        else:
            self.current_channel = channel
