import unittest

from gadget import Gadget

class Gadget_test(object):
	my_iphone = Gadget(240,'iOS',1980,4)
	def test_array_type(self):
		self.assertEqual(240,my_iphone.weight)

	my_iphone.weight = 255

	def test_array_type(self):
		self.assertEqual(255,my_iphone.weight)

	def test_array_type(self):
		self.assertEqual('IOS',my_iphone.operating_system)

	my_iphone.operating_system = 'iOS 8.1'

	def test_array_type(self):
		self.assertEqual('iOS 8.1   ',my_iphone.operating_system)


if __name__ == '__main__':
	unittest.main()
