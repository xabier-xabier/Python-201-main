# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name,text):
    print(greet(greeting, name))
    print(f"{text} \n")
    print(f"Goodbye {name} have a nice day")

greeting="Greetings!"
name="Pedro Fernandez"
letter="""No man is an island,

Entire of itself,

Every man is a piece of the continent,

A part of the main.

If a clod be washed away by the sea,

Europe is the less.

As well as if a promontory were.

As well as if a manor of thy friend’s

Or of thine own were:

Any man’s death diminishes me,

Because I am involved in mankind,

And therefore never send to know for whom the bell tolls;

It tolls for thee."""

write_letter(name, letter)