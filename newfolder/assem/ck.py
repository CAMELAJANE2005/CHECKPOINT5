Class point 3D:

   def_init_(self, x, y, z,):

          self .x = x
          self . y = y
          self .z = z  

def get_coodinates (self)

    return(self .x, self .y, self .z)

My_ point =point 3D(1, 2, 3)


print(my_point.get_coordinates())

Class Rectangle:

def_init_(self,length,width):

 self .length=length

 self  .width=width

def area(self):

    return self. length* self width 
def perimeter(self):

    return 2* (self. length+self .width)

my rectangle = rectangle(4, 3)

print(my_rectangle.area())


 Import math 


def_init_(self,center,radius):

Class circle:
     self .center = center 

     self . radius = radius
  
    def area(self):

          return math.pi *

self .radius

       def is_inside(self,point):

                 distance=

math .sqrt((point[0]-

self . center [0])**2+(point[1]

self  .center[1]**2)

       If distance <=

Self . radius:
          
                  return true 
else 
                   return false

my_circle = circle ((0, 0), 5)

Print (my_circle.area())
Print (my_circle perimeter())

Print  (my_circle.is.inisde((3,4)))


Class Bank:

            def_init_(self, balance):

                   self .balance=balance

              def deposit (self,amount):
 
                     self .balance=amount

                     return  self .balance


                def  withdraw(self, amount):

                       If amount<=
Self balance:
                            Self.balance -=
amount
                              return  self .balance
              else:
                         return “insufficient funds

My_account = bank(100)

Print (my_account.deposit (500))

Print (my_account.withdraw(2000))


