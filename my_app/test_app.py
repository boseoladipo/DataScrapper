import mimetypes
import unittest

from app import get_image_link

RESULT = "data/test_results.txt"
FAILED = "data/test_failed_urls.txt"


class LinkTestCase(unittest.TestCase):
    def test_gets_correct_link(self):
        """
        Test get_image_link function for accuracy
        """
        with open(RESULT, "w") as result_file, open(FAILED, "w") as failed_load_file:
            get_image_link("google.com", result_file, failed_load_file)

        with open(RESULT, "r") as result:
            url = result.readline()

        self.assertEqual(url.strip(), "http://google.com/favicon.ico", "URL incorrect")

    def test_is_url_image(self):
        """
        Test that link returned by get_image_link function is a link to an image
        """
        with open(RESULT, "w") as result_file, open(FAILED, "w") as failed_load_file:
            get_image_link("google.com", result_file, failed_load_file)

        with open(RESULT, "r") as result:
            url = result.readline()

        mimetype, encoding = mimetypes.guess_type(url.strip())
        self.assertTrue(mimetype and mimetype.startswith("image"))


if __name__ == "__main__":
    unittest.main()
