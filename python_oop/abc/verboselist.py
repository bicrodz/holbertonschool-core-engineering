#!/usr/bin/env python3
"""Module that defines a VerboseList class that extends the list class."""


class VerboseList(list):
    """List that prints a message when items are added or removed."""

    def append(self, item):
        """Add an item to the list and print a message.

        Args:
            item: the item to add.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list with items and print a message.

        Args:
            items: an iterable with the items to add.
        """
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a message and remove an item from the list.

        Args:
            item: the item to remove.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a message and remove the item at the given index.

        Args:
            index: the position of the item (the last one by default).

        Returns:
            The item that was removed.
        """
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
