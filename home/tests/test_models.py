from django.test import TestCase
from home.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_str_method(self):
        """Test Category model default name"""
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        self.category_obj = Category.objects.create(name='django', slug='django')
        self.data1 = Product.objects.create(category=self.category_obj, product_name='django beginners',
                                            product_text='LoremIpsum', is_active=True)

    def test_products_model_entry(self):
        """Test Product model data insertion/types/field attributes"""
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')
