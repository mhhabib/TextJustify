# A text alignment justification package.
[![Downloads](https://pepy.tech/badge/textjustify)](https://pepy.tech/project/textjustify) [![Downloads](https://pepy.tech/badge/textjustify/month)](https://pepy.tech/project/textjustify) [![Downloads](https://pepy.tech/badge/textjustify/week)](https://pepy.tech/project/textjustify)


The text alignment justifies package will provide you four types of alignment.

- Left (Default)
- Right
- Center
- Justify both

When you use the above three justification then maybe have a blank space and that space you can also fill the empty place with your own identifiers like `*` `#` or anything.

### Setup `TextJustify`


```bash
pip install TextJustify
```

# Usage


```python
import TextJustify

justify_text=TextJustify.justify_text(sample_text, width, align, fill)
print(justify_text)
```

Here `fill` is an optional value. If you don't pass any special symbol or identifier then it will use the default space.

```python

sample_text = "Your text that you want to justify"
width = 50 # Here 50 is an example value and it will be integer
align =  "left" # Default is "left". Rest of the alignment are "right", "center", "justify"
fill = " " # Default is a space. You can use your own like "*", "#" etc.

```
