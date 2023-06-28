# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name,text):
    print(f"Greetings {name} \n")
    print(f"{text} \n")
    print(f"Goodbye {name} have a nice day")

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
