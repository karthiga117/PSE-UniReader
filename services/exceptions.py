"""Custom exceptions for the reader pipeline."""


class PSEReaderException(Exception):
    """Base exception for friendly document-reader errors."""


class UnsupportedFormatError(PSEReaderException):
    """Raised when a file type is not supported."""


class InvalidDocumentError(PSEReaderException):
    """Raised when a supported document cannot be parsed."""


class DocumentReadError(PSEReaderException):
    """Raised when a document could not be opened for reading."""
