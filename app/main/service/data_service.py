# coding: utf-8

"""
Service with data handlers
"""

from typing import List

from app.main.model.models import Image, Text


def websites() -> List[str]:
    """Show parsed websites
    """
    return []


def images(url: str) -> List[int]:
    """Show images from a website
    """
    pass


def text(url: str) -> str:
    """Show text extracted from a website
    """
    pass


def image(url: str, imgid: int):
    """Returns an image"""
    pass
