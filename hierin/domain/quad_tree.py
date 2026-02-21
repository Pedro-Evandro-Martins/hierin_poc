from __future__ import annotations

from typing import Generic, Optional, Self, TypeVar

T = TypeVar("T")


class Children(Generic[T]):
    __slots__ = ["tr", "tl", "bl", "br"]

    def __init__(self, parent: QuadTreeNode[T]):
        self.tr: QuadTreeNode[T] = QuadTreeNode(parent.quadtree, parent=parent)
        self.tl: QuadTreeNode[T] = QuadTreeNode(parent.quadtree, parent=parent)
        self.bl: QuadTreeNode[T] = QuadTreeNode(parent.quadtree, parent=parent)
        self.br: QuadTreeNode[T] = QuadTreeNode(parent.quadtree, parent=parent)


class QuadTreeNode(Generic[T]):
    def __init__(
        self,
        quadtree: QuadTree[T],
        value: Optional[T] = None,
        parent: Optional[QuadTreeNode[T]] = None,
    ):
        self.__value: Optional[T] = value
        self.quadtree: QuadTree[T] = quadtree
        self.children_count = 0
        self.parent: Optional[QuadTreeNode[T]] = parent
        self.children: Optional[Children[T]] = None

    def is_root(self) -> bool:
        return self.parent is None

    def is_leaf(self) -> bool:
        return self.children is None

    @property
    def value(self) -> Optional[T]:
        return self.__value

    @value.setter
    def value(self, _: T) -> None:
        raise AttributeError(
            "[ERROR] Value is read-only and cannot be set directly. Use 'set_value(value)' instead"
        )

    def set_value(self, value: T) -> None:
        self.__value = value

    @property
    def tr(self) -> QuadTreeNode[T]:
        if self.children is not None:
            return self.children.tr
        else:
            raise RuntimeError(
                "[ERROR] Node is not divided, cannot access top-right child"
            )

    @property
    def tl(self) -> QuadTreeNode[T]:
        if self.children is not None:
            return self.children.tl
        else:
            raise RuntimeError(
                "[ERROR] Node is not divided, cannot access top-left child"
            )

    @property
    def bl(self) -> QuadTreeNode[T]:
        if self.children is not None:
            return self.children.bl
        else:
            raise RuntimeError(
                "[ERROR] Node is not divided, cannot access bottom-left child"
            )

    @property
    def br(self) -> QuadTreeNode[T]:
        if self.children is not None:
            return self.children.br
        else:
            raise RuntimeError(
                "[ERROR] Node is not divided, cannot access bottom-right child"
            )

    def split(self) -> Self:
        if self.children is None:
            self.children = Children(self)
            self._backtrack_children_count(4)
            # Python GC will take care of deallocating the memory when the nodes are no longer referenced

        return self

    def insert_value(
        self,
        tr: Optional[T] = None,
        tl: Optional[T] = None,
        bl: Optional[T] = None,
        br: Optional[T] = None,
    ) -> Self:
        if self.children is None:
            raise RuntimeError(
                "[ERROR] Node is not divided, cannot insert values into children"
            )
        if tr is not None:
            self.children.tr.set_value(tr)
        if tl is not None:
            self.children.tl.set_value(tl)
        if bl is not None:
            self.children.bl.set_value(bl)
        if br is not None:
            self.children.br.set_value(br)

        return self

    def _backtrack_children_count(self, count: int) -> None:
        self.children_count += count
        if self.parent is not None:
            self.parent._backtrack_children_count(count)
        else:
            self.quadtree.set_size(self.quadtree.size + count)


class QuadTree(Generic[T]):
    def __init__(self, root_value: T):
        self.root: QuadTreeNode[T] = QuadTreeNode(self, root_value)
        self.__size: int = 1

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, _: int) -> None:
        raise AttributeError(
            "[ERROR] Size is read-only and cannot be set directly. Use 'set_size(value)' instead"
        )

    def set_size(self, value: int) -> None:
        self.__size = value
