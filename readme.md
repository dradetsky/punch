punch: easy dotted dict access
==============================

a super-simple wrapper around [Munch](https://github.com/Infinidat/munch/). Just do

```python
import punch

e = dict(
    a=1,
    b=2,
    c='hello',
    g=dict(
        u=33,
        v=44
    )
)

pe = punch.it(e)
print(pe.g.u)
```
