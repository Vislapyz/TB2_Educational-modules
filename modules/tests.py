from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Module
from users.models import User


class ModuleTestCase(APITestCase):
    def setUp(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            email="test@test.com",
            is_staff=False,
            is_active=True,
        )
        self.user.set_password("1234")
        self.user.save()

        response = self.client.post(
            "/users/token/", {"email": "test@test.com", "password": "1234"}
        )
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.data = {
            "number": 1,
            "name": "test module",
            "description": "test description",
        }

    def test_create_module(self):
        """Тестирование создания модуля"""
        response = self.client.post(reverse("modules:module-create"), self.data)
        pk = Module.objects.all().latest("pk").pk
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "number": 1,
                "name": "test module",
                "description": "test description",
                "owner": self.user.pk,
            },
        )

    def test_list_module(self):
        """Тестирование вывода списка модулей"""
        self.test_create_module()
        response = self.client.get(reverse("modules:module-list"))
        pk = Module.objects.all().latest("pk").pk

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json()["results"],
            [
                {
                    "id": pk,
                    "number": 1,
                    "name": "test module",
                    "description": "test description",
                    "owner": self.user.pk,
                }
            ],
        )

    def test_retrieve_module(self):
        """Отображение одного модуля по ID"""
        self.test_create_module()
        pk = Module.objects.all().latest("pk").pk
        response = self.client.get(
            f"/modules/{pk}/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "number": 1,
                "name": "test module",
                "description": "test description",
                "owner": self.user.pk,
            },
        )

    def test_update_module(self):
        """Тестирование обновления модуля"""
        self.test_create_module()
        pk = Module.objects.all().latest("pk").pk
        response = self.client.patch(f"/modules/update/{pk}/", {"name": "new name"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "id": pk,
                "number": 1,
                "name": "new name",
                "description": "test description",
                "owner": self.user.pk,
            },
        )

    def test_module_destroy(self):
        """Тестирование удаления модуля"""
        self.test_create_module()
        pk = Module.objects.all().latest("pk").pk
        response = self.client.delete(f"/modules/destroy/{pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
