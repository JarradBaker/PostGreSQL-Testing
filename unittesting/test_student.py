import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('Jarrad', 'Baker')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Jarrad Baker')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'jarrad.baker@email.com')

    def test_apply_extension(self):
        print('test_apply_extension')
        new_end_date = self.student.apply_extension(60)

        self.assertEqual(self.student.end_date, new_end_date)


if __name__ == '__main__':
    unittest.main()
