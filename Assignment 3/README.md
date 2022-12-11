## Group:
Simone Lewis

## How to execute:
Ensure that the dependencies are installed 

```bash
pip install -r requirements.txt
```

After the dependencies are installed, execute the driver(s)
```
python3 assignment3.py
```
## Assignment Specification:

# Problem 1: Object-Oriented Design
This problem in not about code, but about designing templates that can be turned into code. Your task is to design several classes that can instantiate you (or a set of object relevant to you) in a particular user context of, for instance, a community ('Bouldering Club'), a business (e.g. 'Bookstore'), or a profession (e.g., 'BA Student'). Use UML-inspired diagrams to design your object template(s), box-and-pointer diagrams are sufficient.

We define an object as a collection of data and associated behaviors and use dependency relations between types of objects (i.e., classes) to model complex objects. In Python data is implemented as attributes and behavior as methods.

# Object-Oriented Analysis
Start with (object-oriented) analysis, e.g., identify the objects and tasks that characterize you and your interactions in the specific context (e.g., bouldering amateur, climb() or get_coffee() ...). Keep attributes (data types) and dependencies (composition, inheritance) in mind , you are going to need them later, e.g., an 'amateur boulder' is also a person and a person's sex may matter in a bouldering competition, but not for a BA Student's exam.

# Object-Oriented Design
Convert you OOA into a design of your object templates (classes) using UML. The result of this stage is an implementation specification in UML that can be implemented as a set of classes in Python. Use your knowledge of Python as an inspiration for your visual formalization. Remember that in Python we use method to implement behavior and attributes for data. Methods are functions attached to objects and attributes are variables similarly attacted to objects, a 'BA student', for instance, may have the attribute enrollment_year: datetime and method study(duration: int, intensity: str). Use the slides from our OOD as a reference.

# Problem 2: Object-Oriented Programming
In this problem, you have to implement your object template design from problem 1, using the class keyword. The class keyword is used to create a class. A class is like an object constructor. Use our class implementation lesson as a reference.

# Problem 3: Instantiate Class using an Entry Point Function
Instantiate your class (create an object) and show what it can do in an entry point function main(). The main() function is conventionally the entry point, where a Python program starts its execution. It enables high-level organization of the program's functionality, and typically has access to the command arguments given to the program when it was executed. Remember to use the __main__ special name for the top-level environment of the program or import your class into another driver script.
