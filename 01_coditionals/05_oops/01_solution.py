class car:
      total_car = 0
      def __init__(self,brand,model):
            self.__brand = brand
            self.__model = model
            car.total_car += 1

      def get_brand(self):
            return self.brand + "!"      

      def full_name(self):
            return f"{self.__brand}  {self.__model}"      
       
      def fuel_type(self):
            return "diseal or fuel"
      
      @staticmethod
      def general_description():
            return "cars are means of trasport"
      

      @property
      def model(self):
            return self.__model
      
class Electrical(car):
      def __init__(self,brand,model,battery_size):
           super().__init__(brand,model)
           self.battery_size = battery_size


      def fuel_type(self):
            return "Elecrical charges"  


#my_tesla = Electrical("Tesala","model s","85kwh")


#print(isinstance(my_tesla,car))
#print(isinstance(my_tesla,Electriccar))


#print(my_tesla.full_name())      
      
# = car("Toyota","corolla")  
#print(my_car.brand)
#print(my_car.get_brand())
#print(my_car.fuel_type())

my_car = car("Tata", "safari")
#my_car.model = "city"
car("Tata","Nexon")


#print(my_car.general_discription())
print(my_car.model)



#my_new_car = car("tata","safari")
#print(my_new_car.model)



class Battery:
      def battery_info(self):
            return "this is battery"

class Engine:
      def engine_info(self):
            return "This is engine"

class ElectriccarTwo(Battery,Engine,car):
      pass

my_new_tesla = ElectriccarTwo("Tesla","Model s")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())