"""Format-independent document model."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    """Readable content and source information for a document."""

    title: str
    source: str
    document_type: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
