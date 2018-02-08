import os
import pickle

def save(objs, file_name):
	"""Save rooms in pb file
	:params objs: a list
	:params file_name: where to save the obj
	"""
	res = read_file(file_name)
	res.extend(objs)
	write_to_file(res, file_name)


def read_file(file_name):
	"""Reads objects from a file and
	returns as list
	"""
	res = []
	if os.path.exists(file_name):
		with open(file_name, 'rb') as pickle_file:
			res = pickle.load(pickle_file)
	return res


def write_to_file(objs, file_name):
	"""
	Write supplied objects to file
	:param objs: a list
	:param file_name: a str
	"""
	with open(file_name, 'a+b') as pickle_file:
		pickle.dump(objs, pickle_file)
