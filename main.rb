# Ruby OOP
class Worker
  def initialize(name,salary)
    @name = name
    @salary = salary
  end
  def display
    print("My name is #{@name}, my salary is #{@salary}")
  end
end
worker1 = Worker.new("Pram", 9000000)
worker1.display()