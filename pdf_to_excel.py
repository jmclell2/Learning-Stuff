#source code from pdfminer.six maintainer comment on stack overflow https://stackoverflow.com/questions/22898145/how-to-extract-text-and-text-coordinates-from-a-pdf-file/69151177#69151177

from pathlib import Path
from typing import Iterable, Any

from pdfminer.high_level import extract_pages


def show_ltitem_hierachy(o: Any, depth=0):
	"""Show location and text of LTItem and all its descendants"""
	if depth == 0:
		print('element                      x1  y1  x2  y2  text')
		print('---------------------------- --- --- --- --- -----')

	print(
		f'{get_indented_name(o, depth):<30.30s}) '
		f'{get_optional_bbox(o)} '
		f'{get_optional_text(o)} '
	)

	if isinstance(o, Iterable):
		for i in o:
			show_ltitem_hierachy(i, depth=depth + 1)


def get_indented_name(o: Any, depth: int) -> str:
	"""Indented name of LTItem"""
	return '  ' * depth + o.__class__.__name__


def get_optional_bbox(o: Any) -> str:
	"""Bounding box of LTItem if available, otherwise empty string"""
	if hasattr(o, 'bbox'):
		return ''.join(f'{i:<4.0f}' for i in o.bbox)
	return ''


def get_optional_text(o: Any) -> str:
	"""Text of LTItem if available, otherwise empty string"""
	if hasattr(o, 'get_text'):
		return o.get_text().strip()
	return ''


path = Path(r'C:\Users\jmclellan\Downloads\Roll_Number_Test.pdf').expanduser()

pages = extract_pages(path)
show_ltitem_hierachy(pages)

