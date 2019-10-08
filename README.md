# cli-context
This is a library which supports CLI contexts for action hierarchies.
For that, you have to use the `CliContext` class and create your own contexts.

## Usage
Install this package with pip (or manually).

In your project, create a python file which will be called as a CLI entry-point:
```python
import sys
from .my_entry_context import context as entry_ctx


if __name__ == "__main__":
    entry_ctx.run((sys.argv[0],), sys.argv[1:])
```

In `my_entry_context.py`:
```python
from cli_context import CliContext

context = CliContext(
    "This is my fancy CLI",
    sub_contexts={
        "run": run_context,
        "do": another_context,
    }
)

```