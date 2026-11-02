from django.test import TestCase
from .models import Car, Contact, Feature, Settings, Slide


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

    def test_contact_post_saves_submission_once_with_selected_car(self):
        Car.objects.create(
            name='Database Sedan',
            category=Car.Category.SEDAN,
            price=2500000,
            year=2025,
            engine='2.0 л, 150 л.с.',
            gearbox='Автомат',
        )

        response = self.client.post(
            '/',
            {'name': 'Test User', 'phone': '+79991234567', 'car': 'Database Sedan'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.get()
        self.assertEqual(contact.name, 'Test User')
        self.assertEqual(contact.phone, '+79991234567')
        self.assertEqual(contact.car, 'Database Sedan')
        self.assertContains(response, 'Спасибо, Test User!')

    def test_contact_post_rejects_invalid_phone(self):
        self.client.post('/', {'name': 'Test User', 'phone': '123', 'car': ''})

        self.assertEqual(Contact.objects.count(), 0)
