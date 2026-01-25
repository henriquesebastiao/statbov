from selenium.webdriver.common.by import By

from ..utils import FunctionalTestBase


class PlansFunctionalTest(FunctionalTestBase):
    def test_content_pricing_header_plans_page(self):
        content = self.get_content(By.CLASS_NAME, 'pricing-header', '/plans/')
        words = [
            'Encontre o plano perfeito para sua '
            'fazenda de maneira simples e eficaz!',
            'Nossos planos e preços são projetados para se adaptarem '
            'às demandas específicas de cada perfil de '
            'pecuarista. Explore as opções abaixo e '
            'solicite uma demonstração agora mesmo.',
        ]
        for word in words:
            self.assertIn(word, content.text)

    def test_content_card_free_plan_plans_page(self):
        content = self.get_content(By.ID, 'card-free-plan', '/plans/')
        words = [
            'Grátis',
            'R$0/mês',
            '1 usuário incluso',
            'Até 200 animais',
            '1 propriedade',
            'Registre-se grátis',
        ]
        for word in words:
            self.assertIn(word, content.text)

    def test_content_card_professional_plan_plans_page(self):
        content = self.get_content(By.ID, 'card-professional-plan', '/plans/')
        words = [
            'Profissional',
            'R$30/mês',
            '10 usuários inclusos',
            'Até 500 animais',
            '5 propriedade',
            'Começar',
        ]
        for word in words:
            self.assertIn(word, content.text)

    def test_content_card_business_plan_plans_page(self):
        content = self.get_content(By.ID, 'card-business-plan', '/plans/')
        words = [
            'Empresas',
            'R$100/mês',
            'Usuários ilimitados',
            'Animais ilimitados',
            'Propriedades ilimitadas',
            'Entrar em contato',
        ]
        for word in words:
            self.assertIn(word, content.text)

    def test_content_comparison_plans_title_plans_page(self):
        content = self.get_content(By.ID, 'comparison-plans-title', '/plans/')
        self.assertIn('Compare os planos', content.text)

    def test_content_comparison_plans_table_plans_page(self):
        content = self.get_content(By.ID, 'comparison-plans-table', '/plans/')
        words = [
            'Funcionalidade',
            'Grátis',
            'Profissional',
            'Empresas',
            'Coleta de dados on-line',
            'Acompanhamento dos registros',
            'Relatório de desempenho reprodutivo',
            'Relatório de ganho de peso',
            'Relatório de manejos',
            'Custeio de produção individual por animal',
            'Acompanhamento financeiro',
            'Tendências de preços do mercado',
            'Quantidade ilimitada de animais',
            'Número ilimitado de propriedades',
            'Número ilimitado de usuários',
        ]
        for word in words:
            self.assertIn(word, content.text)
