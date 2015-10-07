#!/usr/bin/env python

from simple_object import SimpleObject
import re
import sys
import os

class Parser(object):
	__vertex_regex               = r'v (-?\d+.\d+) (-?\d+.\d+) (-?\d+.\d+)'
	__vertex_regex_compiled      = None
	__object_name_regex          = r'o (.+)'
	__object_name_regex_compiled = None
	__tex_regex                  = r'vt (-?\d+.\d+) (-?\d+.\d+)'
	__tex_regex_compiled         = None
	__normals_regex							 = r'vn (-?\d+.\d+) (-?\d+.\d+) (-?\d+.\d+)'
	__normals_regex_compiled     = None
	__data                       = None
	__object_name   						 = None
	__vertexes									 = []
	__texes 										 = []
	__normals 									 = []
	__all_objects								 = []
	__output_dir								 = None
	# __object_name                = None


	def __init__(self, file_name, output_dir):
		object.__init__(self)
		self.__vertex_regex_compiled      = re.compile(self.__vertex_regex)
		self.__object_name_regex_compiled = re.compile(self.__object_name_regex)
		self.__tex_regex_compiled         = re.compile(self.__tex_regex)
		self.__normals_regex_compiled 	  = re.compile(self.__normals_regex)
		self.__output_dir									= output_dir
		with open(file_name, 'r') as file:
			self.__data = file.readlines()


	def generate_headers(self):
		for line in self.__data:
			# fetching object name
			obj_name = self.__object_name_regex_compiled.match(line)
			if obj_name is not None:
				# we fetched object data and now we have another object
				if self.__object_name is not None:
					so = SimpleObject(self.__object_name, \
														self.__vertexes, \
														self.__texes, \
														self.__normals)
					# so.write_to_file('test')
					self.__all_objects.append(so)
					# cleaning structs
					self.__object_name = None
					self.__vertexes    = []
					self.__texes       = []
					self.__normals     = []

				self.__object_name = obj_name.group(1)
			else: # obj not found, could be vertex
				v_table = self.__vertex_regex_compiled.match(line)
				if v_table is not None:
					x, y, z = v_table.group(1), v_table.group(2), v_table.group(3)
					self.__vertexes.append((x, y, z))
				else: # vertex not found, could be tex
					vt_table = self.__tex_regex_compiled.match(line)
					if vt_table is not None:
						x, y = vt_table.group(1), vt_table.group(2)
						self.__texes.append((x, y))
					else: # tex not found, could be normal
						n_table = self.__normals_regex_compiled.match(line)
						if n_table is not None:
							x, y, z = n_table.group(1), n_table.group(2), n_table.group(3)
							self.__normals.append((x, y, z))


		for obj in self.__all_objects[-5:]:
			obj.write_to_file(self.__output_dir + obj.get_object_name() 
				+ '.obj.h')


def usage():
	print("Usage: ./parser.py <obj_file> <path_to_output_dir>")
	print("\tParser will generate C headers for every object in obj_file")
	print("\tand saves files to path_to_output_dir dir.")


def main():
	if len(sys.argv) < 3:
		usage()
		sys.exit(1)

	file_name          = sys.argv[1]
	path_to_output_dir = sys.argv[2]

	if not os.path.exists(path_to_output_dir):
		os.makedirs(path_to_output_dir)

	p = Parser(file_name, path_to_output_dir)
	p.generate_headers()

if __name__ == "__main__":
	main()
