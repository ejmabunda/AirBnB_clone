#!/usr/bin/python3
"""This module supplies the base class.
"""
import uuid
from datetime import datetime


class BaseModel:
	"""
	BaseModel that defines all common attributes/methods for other classes.

	Attributes:
		id (str): Unique identifier for each instance, assigned with a UUID.
		created_at (datetime): Datetime when an instance is created.
		updated_at (datetime): Datetime when an instance is created
		and updated whenever the instance is modified.
	"""

	def __init__(self, *args, **kwargs):
		"""Initializes a new instance of BaseModel."""
		if kwargs:
			for key, value in kwargs.items():
				if key != "__class__":
					if key in ("created_at", "updated_at") and isinstance(value, str):
						value = datetime.fromisoformat(value)
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = self.created_at

	def __str__(self):
		"""
		Returns a string representation of the BaseModel instance.

		Returns:
			str: String representation of the instance in the format
			[<class name>] (<self.id>) <self.__dict__>.
		"""
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""
		Updates the public instance attribute `updated_at`
		with the current datetime.
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
		Returns a dictionary containing all keys/values of
		__dict__ of the instance.

		Returns:
			dict: Dictionary representation of the instance.
		"""
		instance_dict = self.__dict__.copy()
		instance_dict['__class__'] = self.__class__.__name__
		instance_dict['created_at'] = self.created_at.isoformat()
		instance_dict['updated_at'] = self.updated_at.isoformat()
		return instance_dict
