from django.test import TestCase
from .models import Car, Feature, Settings, Slide


class IndexPageTests(TestCase):
    def test_index_displays_saved_site_and_slide_data(self):
        Settings.objects.create(
            title='Test Auto',
            logo='',
            description='Saved site description',
            address='Saved address',
            phone='+79991234567',
            email='test@example.com',
        )
        Slide.objects.create(
            title='Featured car',
            image='',
            description='Featured description',
            sales='1488',
            age='10',
            clients=21334,
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Featured car')
        self.assertContains(response, 'Featured description')
        self.assertContains(response, 'data-count="1488"')
        self.assertContains(response, 'data-count="10"')
        self.assertContains(response, 'data-count="21334"')
        self.assertContains(response, 'Saved address')
        self.assertContains(response, 'tel:+79991234567')
        self.assertContains(response, 'test@example.com')

    def test_index_displays_cars_and_features_from_database(self):
        car = Car.objects.create(
            name='Database Sedan',
            category=Car.Category.SEDAN,
            price=2500000,
            year=2025,
            engine='2.0 л, 150 л.с.',
            gearbox='Автомат',
            image_url='https://example.com/car.jpg',
        )
        Feature.objects.create(
            icon='⭐',
            title='Database feature',
            description='Feature managed through the database.',
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'data-name="{car.name}"')
        self.assertContains(response, f'data-category="{car.category}"')
        self.assertContains(response, car.engine)
        self.assertContains(response, 'Database feature')
        self.assertContains(response, 'Feature managed through the database.')
        self.assertContains(response, '<option value="Database Sedan">Database Sedan</option>', html=True)
        self.assertContains(response, 'Toyota Camry')
