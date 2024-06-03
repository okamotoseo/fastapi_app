import sys
import os

# Adicione o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from fastapi import FastAPI
from app.routes.previsao_demanda.endpoints import router as previsao_demanda_router
from app.routes.otimizacao_estoque.endpoints import router as otimizacao_estoque_router
from app.routes.dynamic_pricing.endpoints import router as dynamic_pricing_router
from app.routes.otimizacao_promocoes.endpoints import router as otimizacao_promocoes_router
from app.routes.analise_preditiva.endpoints import router as analise_preditiva_router
from app.routes.segmentacao_clientes.endpoints import router as segmentacao_clientes_router
from app.routes.recomendacoes_produtos.endpoints import router as recomendacoes_produtos_router
from app.routes.deteccao_fraudes.endpoints import router as deteccao_fraudes_router
from app.routes.personalizacao_marketing.endpoints import router as personalizacao_marketing_router

app = FastAPI()

app.include_router(previsao_demanda_router, prefix="/previsao_demanda", tags=["Previsão de Demanda"])
app.include_router(otimizacao_estoque_router, prefix="/otimizacao_estoque", tags=["Otimização de Estoque"])
app.include_router(dynamic_pricing_router, prefix="/dynamic_pricing", tags=["Dynamic Pricing"])
app.include_router(otimizacao_promocoes_router, prefix="/otimizacao_promocoes", tags=["Otimização de Promoções"])
app.include_router(analise_preditiva_router, prefix="/analise_preditiva", tags=["Análise Preditiva"])
app.include_router(segmentacao_clientes_router, prefix="/segmentacao_clientes", tags=["Segmentação de Clientes"])
app.include_router(recomendacoes_produtos_router, prefix="/recomendacoes_produtos", tags=["Recomendações de Produtos"])
app.include_router(deteccao_fraudes_router, prefix="/deteccao_fraudes", tags=["Detecção de Fraudes"])
app.include_router(personalizacao_marketing_router, prefix="/personalizacao_marketing", tags=["Personalização de Marketing"])

@app.get("/")
async def root():
    return {"message": "API FastAPI com estrutura modular"}

