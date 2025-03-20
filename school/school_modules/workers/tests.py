# tests.py
from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from school_modules.workers.models import Worker


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.worker = Worker.objects.create(fio="worker1", birth_date="2002-02-21")
        self.client = APIClient()

    def test_list_workers(self):
        """Test listing all workers."""
        url = reverse("worker-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("list", response.data)
        self.assertEqual(len(response.data["list"]), 1)

    def test_retrieve_user(self):
        """Test retrieving a single worker by ID."""
        url = reverse("worker-detail", kwargs={"pk": self.worker.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("worker", response.data)  # Ensure the 'user' key exists
        self.assertEqual(response.data["worker"]["fio"], "worker1")

    def test_create_worker(self):
        """Test creating a new worker."""
        url = reverse("worker-list")
        data = {"worker": {"fio": "worker2", "birth_date": "2001-01-01"}}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("worker", response.data)  # Ensure the 'user' key exists
        self.assertEqual(response.data["worker"]["fio"], "worker2")
        self.assertTrue(Worker.objects.filter(fio="worker2").exists())

    def test_update_user(self):
        """Test updating an existing worker."""
        url = reverse("worker-detail", kwargs={"pk": self.worker.id})
        updated_data = {"worker": {"fio": "worker3", "birth_date": "2003-02-21"}}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.fio, "worker3")
        self.assertEqual(self.worker.birth_date, date(2003, 2, 21))

    def test_partial_update_user(self):
        """Test partially updating an existing worker."""
        url = reverse("worker-detail", kwargs={"pk": self.worker.id})
        partial_data = {
            "worker": {
                "fio": "worker5",
            }
        }
        response = self.client.patch(url, partial_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.fio, "worker5")

    def test_delete_user(self):
        """Test deleting a worker."""
        url = reverse("worker-detail", kwargs={"pk": self.worker.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Worker.objects.filter(id=self.worker.id).exists())
