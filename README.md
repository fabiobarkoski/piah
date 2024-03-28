# piah

[![PyPI - Version](https://img.shields.io/pypi/v/piah.svg)](https://pypi.org/project/piah)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/piah.svg)](https://pypi.org/project/piah)

-----

Piah automatically parse the data from PDF or texts based only in the dataclass that you provide and return the same dataclass fullfilled with the values.
Piah is based in the (OxyParser)[https://github.com/oxylabs/OxyParser/]

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install piah
```

## Example
```python
from piah import Piah
from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int

parser = Piah("gpt-3.5-turbo")
result = parser.parse("Hello Iam python and I have 33 years old", Person)
```

## License

`piah` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
