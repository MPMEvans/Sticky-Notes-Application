# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        # Create a Post object for testing
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_has_title(self):
        # Test that a Post object has the expected title
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        # Test that a Post object has the expected content
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class PostViewTest(TestCase):
    def setUp(self):
        # Create a Post object for testing views
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_list_view(self):
        # Test the post-detail view
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')


class PostDeleteTest(TestCase):
    def setUp(self):
        # Create a Post object for testing deletion
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_delete(self):
        post = Post.objects.get(id=1)
        post.delete()
        self.assertRaises(post.DoesNotExist)


class PostEditTest(TestCase):
    def setUp(self):
        # Create a Post object for testing edits
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_edit(self):
        post = Post.objects.get(id=1)
        post.content = 'This is an edited test post.'
        self.assertEqual(post.content, 'This is an edited test post.')
