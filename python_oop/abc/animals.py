#!/usr/bin/env python3
"""Module that defines an abstract Animal class and two subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that represents an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
