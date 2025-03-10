# Module 2

## A Function

A function is able to:

**cause some effect** (e.g., send text to the terminal, create a file, draw an image, play a sound, etc.)

**evaluate a value** (e.g., the square root of a value or the length of a given text) and return it as the function's result

a function may have:

- an effect;
- a result.

`function_name(argument)`

print()

takes its arguments (it may accept more than one argument and may also accept less than one argument)

What value does the print() function return?

None.

argument is implicitly used in the following way: end="\n".

## Literals - the data in itself

**A literal is data whose values are determined by the literal itself.**

جسكی ٹاءپ ڈیٹا خود ہی بتا دے

123 is a literal, and c is not.

You would write the number like this: 11,111,111, or like this: 11.111.111, or even like this: 11 111 111.

Python doesn't accept things like these. It's prohibited. What Python does allow, though, is the use of underscores in numeric literals.

11_111_111

## Variables

how to store the results of these operations, in order to use them in other operations
special "boxes" (or "containers" as we may call them) for that purpose,
and these boxes are called variables ‒ the name itself suggests that the content
of these containers can be varied in (almost) any way.

`variables (an identifier) = "boxes" (containers)`

- a name
- a value

* the name of the variable must be composed of upper-case or lower-case letters, digits, and the character \_ - (underscore)
* the name of the variable must begin with a letter;
* the underscore character is a letter;
* upper- and lower-case letters are treated as different
* the name of the variable must not be any of Python's reserved words (the keywords)

## Keywords

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

They are called keywords or (more precisely) reserved keywords. They are reserved because you mustn't use them as names: neither for your variables, nor functions, nor any other named entities you want to create.

**A variable comes into existence as a result of assigning a value to it.**

**A remark inserted into the program, which is omitted at runtime, is called a comment.**

**NOTE:** Comments are very important. They are used not only to make your programs easier to understand, but also to disable those pieces of code that are currently not needed (e.g., when you need to test some parts of your code only, and ignore others). Good programmers describe each important piece of code, and give self-commenting names to variables, as sometimes it is simply much better to leave information in the code.

## INPUT

The input() function is able to read data entered by the user and to return the same data to the running program.

**Note**: the result of the input() function is a string. This means that you mustn't use it as an argument of any arithmetic operation, e.g., you can't use this data to square it, divide it by anything, or divide anything by it.

### Type casting (type conversions)

- the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer; if it fails, the whole program will fail too.
- the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float (the rest is the same).

### String operators

#### Concatenation

- The + (plus) sign, when applied to two strings, becomes a concatenation operator:

`string + string`

- concatenation operator is not commutative, i.e., "ab" + "ba" is not the same as "ba" + "ab".
- if you want the + sign to be a concatenator, not an adder, you must ensure that both its arguments are strings.

#### Replication

- The \* (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:

```
string * number
number * string
```
