from unittest import TestCase
from algosi.queue import Queue


class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue() # новая очередь перед каждым тестом

    def test_poryadok(self):
        self.queue.add_value(10)
        self.queue.add_value(20)
        self.queue.add_value(30)

        self.assertEqual(self.queue.pop_value(), 10)
        self.assertEqual(self.queue.pop_value(), 20)
        self.assertEqual(self.queue.pop_value(), 30)

    def test_peek(self):
        self.queue.add_value(10)
        self.queue.add_value(20)

        self.assertEqual(self.queue.peek(), 10)
        self.assertEqual(self.queue.peek(), 10)

        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.pop_value(), 10)

    def test_len_and_bool(self):
        self.assertEqual(len(self.queue), 0)
        self.assertFalse(self.queue)

        self.queue.add_value(0)
        self.assertEqual(len(self.queue), 1)
        self.assertTrue(self.queue)

        self.queue.pop_value()
        self.assertEqual(len(self.queue), 0)
        self.assertFalse(self.queue)

    def test_empty_queue_and_index_err(self):
        self.assertRaises(IndexError, self.queue.peek)
        self.assertRaises(IndexError, self.queue.pop_value)