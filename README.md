[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/08twE9R9)
# string_search
Empirical comparison of string search methods.

## Usage
```
usage: string_search.py [-h] --text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE
                        --pattern_size PATTERN_SIZE [--rounds ROUNDS]
                        --out_file OUT_FILE [--width WIDTH]
                        [--height HEIGHT]

optional arguments:
  -h, --help            show this help message and exit
  --text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE
                        Text size parameters (start stop step)
  --pattern_size PATTERN_SIZE
                        Pattern size
  --rounds ROUNDS       Number of rounds to run each algorithm (default: 10)
  --out_file OUT_FILE   File to save plot to
  --width WIDTH         Width of plot in inches (default: 8)
  --height HEIGHT       Height of plot in inches (default: 5)
```

## Examles
```
python src/string_search.py \
    --text_range 100 10000 100 \
    --pattern_size 100 \
    --rounds 1 \
    --out_file doc/naive_search.png
```
<center><img src="/doc/naive_search.png" width="600"/></center>

