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
