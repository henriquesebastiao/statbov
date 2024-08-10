from selenium.webdriver.common.by import By

from ..utils import FunctionalTestBase


class IndexFunctionalTest(FunctionalTestBase):
    def test_content_index_page(self):
        content = self.get_content(By.TAG_NAME, 'header', '/')
        words = [
            'Statbov',
            'Início',
            'Planos',
            # 'Blog',
            'Suporte',
            'Sobre nós',
            'Entrar',
            'Registrar',
        ]
        for word in words:
            self.assertIn(word, content.text)
