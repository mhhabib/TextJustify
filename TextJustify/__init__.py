import re
import textwrap


def justify_text(_text, w, align="left", fill=" "):
    wrapper = textwrap.TextWrapper(width=w)
    dedented_text = textwrap.dedent(text=_text)
    txt = wrapper.fill(text=dedented_text)

    def justify_both(get_text, _width):
        prev_txt = get_text
        while((l := _width-len(get_text)) > 0):
            get_text = re.sub(r"(\s+)", r"\1 ", get_text, count=l)
            if(get_text == prev_txt):
                break
        return get_text.rjust(_width)

    _justify_res = ""
    if align == 'left':
        for l in txt.splitlines():
            _justify_res += l.ljust(w, fill)+"\n"
    elif align == 'right':
        for l in txt.splitlines():
            _justify_res += l.rjust(w, fill)+"\n"
    elif align == 'center':
        for l in txt.splitlines():
            _justify_res += l.center(w, fill)+"\n"
    elif align == 'justify':
        for l in txt.splitlines():
            _justify_res += justify_both(l, w)+"\n"

    return _justify_res
