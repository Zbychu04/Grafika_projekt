import os.path

class SimpleObject(object):
	__IFNDEF                 = '#ifndef '
	__MACRO_POSTFIX          = '_TEX_H'
	__DEFINE                 = '#define '
	__ENDIF                  = r'#endif \\'
	__VERTEX_TABLE_POSTFIX   = 'Vertices[] = {\n'
	__VERTEX_COUNTER_POSTFIX = 'VertexCount = '
	__TEX_TABLE_POSTFIX      = 'TexCoord[] = {\n'
	__NORMALS_TABLE_POSTFIX  = 'Normals[] = {\n'
	__CLOSE                  = '};\n\n'
	__FLOAT_PREFIX           = 'float '
	__INT_PREFIX             = 'int '
	__SEMICOLON              = ';\n'
	__NEW_LINE               = '\n'
	__object_name            = None
	__v                      = None
	__vt                     = None
	__vn                     = None
	__header_prefix          = None


	def __init__(self, object_name, v, vt, vn):
		object.__init__(self)
		self.__object_name = object_name
		self.__v           = v
		self.__vt          = vt
		self.__vn          = vn


	def get_object_name(self):
		return self.__object_name


	def __get_vertices(self):
		return self.__v


	def __get_ts(self):
		return self.__vt


	def __get_normals(self):
		return self.__vn


	def __generate_payload(self):
		data = self.__NEW_LINE  + self.__NEW_LINE
		data += self.__INT_PREFIX + self.get_object_name() + self.__VERTEX_COUNTER_POSTFIX + \
				str(len(self.__get_vertices())) + self.__SEMICOLON + \
			self.__FLOAT_PREFIX + self.get_object_name() + self.__VERTEX_TABLE_POSTFIX
		for line in [''.join([str(x) + ', ' + str(y) + ', ' + str(z) + '\n']) for (x, y, z) in self.__get_vertices()]:
			data += "\t" + line

		data += self.__CLOSE

		data += self.__FLOAT_PREFIX + self.get_object_name() + self.__TEX_TABLE_POSTFIX
		for line in [''.join([str(x) + ', ' + str(y) + '\n']) for (x, y) in self.__get_ts()]:
			data += '\t' + line

		data += self.__CLOSE

		data += self.__FLOAT_PREFIX + self.get_object_name() + self.__NORMALS_TABLE_POSTFIX
		for line in [''.join([str(x) + ', ' + str(y) + ', ' + str(z) + '\n']) for (x, y, z) in self.__get_normals()]:
			data += "\t" + line

		data += self.__CLOSE

		data += self.__NEW_LINE

		return data


	def write_to_file(self, file_name):
		data = \
			self.__IFNDEF +  self.__object_name.upper() + self.__MACRO_POSTFIX + self.__NEW_LINE + \
			self.__DEFINE + self.__object_name.upper() + self.__MACRO_POSTFIX

		data += self.__generate_payload()

		data += self.__ENDIF + self.get_object_name()
		with open(file_name, 'w') as file:
			file.write(data)

	def write_payload(self, file_name):
		if not os.path.isfile(file_name):
			self.write_to_file(file_name)
		else:
			lines = []
			with open(file_name, 'r') as file:
				lines = file.readlines()
				lines.insert(len(lines) - 1, self.__generate_payload())
			with open(file_name, 'w') as file:
				file.writelines(lines)


if __name__ == "__main__":
	v = [ (1.000000, -0.126453, -1.000000),
				(-1.000000, 0.076591, -1.000000),
				(0.725267, 0.126453, -0.725267) ]

	vt = [ (0.181535, 0.250000),
				 (0.060512, 0.250000),
				 (0.399721, 0.537545),
				 (0.311947, 0.537545) ]

	vn = [
				(0.000000, -1.000000, 0.000000),
				(0.000000, 1.000000, 0.000000),
				(0.000000, 1.000000, 0.000000) ]

	so = SimpleObject('name', v, vt, vn)
	so.write_to_file('test')
	so.write_payload('test1')