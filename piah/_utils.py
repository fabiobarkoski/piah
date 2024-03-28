from pathlib import Path
from typing import Union, Any, IO

from pypdf import PdfReader

StreamType = IO[Any]
StrByteType = Union[str, StreamType]
Pdf = StrByteType | Path

def _extract_text(stream: StrByteType | Path) -> str:
    reader = PdfReader(stream)
    page = reader.pages[0]
    return page.extract_text()

def _is_pdf(value: Pdf) -> bool:
    try:
        _extract_text(value)
        return True
    except FileNotFoundError:
        return False
    except OSError:
        return False

