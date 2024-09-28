# Module 3

## Comparison: equality operator

- `==` is a binary operator with left-sided binding.

**PRIORITY:** (), \*\* , +/- (unary), \*, /, //, %, +/- (binary), <, <=, >, >=, ==, !=

## Conditional instruction (or conditional statement)

- four spaces of indentation
- if you use tabs mixed with spaces, it's important to make all indentations exactly the same
- _Python 3 does not allow the mixing of spaces and tabs for indentation._

```
if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()
```

```
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()
```

```
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
```

- if there is an else branch in the cascade, only one of all the branches is executed;
- if there is no else branch, it's possible that none of the available branches is executed.

# Loops

`while` repeats the execution as long as the condition evaluates to True

- An infinite loop, also called an endless loop, is a sequence of instructions in a program which repeat indefinitely (loop endlessly.)
  `Ctrl-C (or Ctrl-Break on some computers)`

`for loop` is designed to do more complicated tasks – it can "browse" large collections of data item by item.

- the `pass keyword` inside the loop body – it does nothing at all; it's an empty instruction

These two instructions are:

- break – exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
- continue – behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
- Note: if the control variable doesn't exist before the loop starts, it won't exist when the execution reaches the else branch.

# Computer logic

- We've used the conjunction and, which means that going for a walk depends on the simultaneous fulfilment of these two conditions. In the language of logic, such a connection of conditions is called a conjunction.
- The appearance of the word or means that the purchase depends on at least one of these conditions. In logic, such a compound is called a disjunction.
- They're called logical operators.

**PRIORITY:** (), \*\* , +/- (unary), \*, /, //, %, +/- (binary), <, <=, >, >=, ==, !=, and, or, not

## Bitwise operators

There are four operators that allow you to manipulate single bits of data. They are called bitwise operators.
Here are all of them:

- & (ampersand) ‒ bitwise conjunction;
- | (bar) ‒ bitwise disjunction;
- ~ (tilde) ‒ bitwise negation;
- ^ (caret) ‒ bitwise exclusive or (xor).

Results

- & requires exactly two 1s to provide 1 as the result;
- | requires at least one 1 to provide 1 as the result;
- ^ requires exactly one 1 to provide 1 as the result.
