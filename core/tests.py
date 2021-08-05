# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.test import TestCase
from core.models import TestModel

# Create your tests here.


# Test BaseModel.
class BaseModelTest(TestCase):

    def setUp(self) -> None:
        self.model_1 = TestModel.objects.create()

    # First Test for checking that django can understand logical delete with all query.
    def test_1_all_deleted(self):
        self.model_1.deleted = True
        self.model_1.save()

        self.assertNotIn(self.model_1, TestModel.objects.all())

    # Second Test for checking that django can understand logical delete with filter query.
    def test_2_filter_deleted(self):
        self.model_1.deleted = True
        self.model_1.save()

        self.assertNotIn(self.model_1, TestModel.objects.filter())

    # Third Test for checking that django can understand logical delete with get query.
    def test_3_get_deleted(self):
        self.model_1.deleted = True
        self.model_1.save()

        self.assertRaises(Exception, TestModel.objects.get, id=1)

    # Forth Test for checking archives that include logical delete.
    def test_4_archive(self):
        self.model_1.deleted = True
        self.model_1.save()

        self.assertIn(self.model_1, TestModel.objects.archive())
        self.assertNotIn(self.model_1, TestModel.objects.all())