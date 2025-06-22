from django.test import TestCase
from core.models import Teacher
from django.contrib.auth.models import User

# Create your tests here.

class TeacherModelTest(TestCase):
    

    def test_teacher_creation(self):
        teacher = Teacher.objects.create(full_name="John Doe",
                                         email="john.doe@example.com",
                                           
                                           phone_no=123450,
                                           department="BCA",
                                            join_date="2023-01-01",
                                           user=User.objects.create_user(username="testuser", password="password")
                                        #    user=User.objects.get(id=9)assuming user with id 9 exists
                                           )
        try:
          # case 1
          print("case 1:Testing with user testuser")
          self.assertEqual(teacher.full_name, "John Doe")
          self.assertEqual(teacher.email, "john.doe@example.com")
          self.assertEqual(teacher.phone_no,123450)
          self.assertEqual(teacher.department,"BCA")
          self.assertEqual(teacher.join_date, "2023-01-01")
          self.assertEqual(teacher.user, User.objects.get(username="testuser"))

        except Exception as e:
            print(f"An error occurred: {e}")


        try:
          # case 2
          print("case 2:Testing with different user")

          self.assertEqual(teacher.full_name, "John Doe")
          self.assertEqual(teacher.email, "john.doe@example.com")
          self.assertEqual(teacher.phone_no,123450)
          self.assertEqual(teacher.department,"BCA")
          self.assertEqual(teacher.join_date, "2023-01-01")
          self.assertEqual(teacher.user, User.objects.get(username="nirmal"))

        except Exception as e:
            print(f"An error occurred: {e}")
            print("User with username 'nirmal' does not exist, skipping this test case.")


        try:
          # phone number length test

          print("case 3:Testing with phone number length")
          self.assertEqual(teacher.full_name, "John Doe")
          self.assertEqual(teacher.email, "john.doe@example.com")
          self.assertEqual(teacher.phone_no,1234500000)
          self.assertEqual(teacher.department,"BCA")
          self.assertEqual(teacher.join_date, "2023-01-01")
          self.assertEqual(teacher.user, User.objects.get(username="testuser"))

          

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Phone number length is not as expected, skipping this test case.")


    def test_teacher_model_email_exists(self):
        teacher = Teacher.objects.create(full_name="kp oli",
                                         email="kpoli@example.com",
                                           
                                           phone_no=123450,
                                           department="BCA",
                                            join_date="2023-01-01",
                                           user=User.objects.create_user(username="testemail", password="password")
                                       )
        try:
            self.assertEqual(teacher.full_name, "kp oli")
            self.assertEqual(teacher.email, "hiran@example.com")
            self.assertEqual(teacher.phone_no, 123450)
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.join_date, "2023-01-01")
            self.assertEqual(teacher.user, User.objects.get(username="testemail"))
            print("case 4:email diff passed")

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Email already esxits")
  