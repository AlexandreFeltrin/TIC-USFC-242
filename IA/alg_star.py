import heapq

grafo_vizinhos = {
    'Criciuma': {'Ararangua': 40, 'Tubarão': 50, 'Içara': 15},
    'Ararangua': {'Criciuma': 40, 'Sombrio': 30},
    'Tubarão': {'Criciuma': 50, 'Laguna': 30, 'Braço do Norte': 40},
    'Laguna': {'Tubarão': 30, 'Imbituba': 25},
    'Imbituba': {'Laguna': 25, 'Garopaba': 20},
    'Garopaba': {'Imbituba': 20, 'Paulo Lopes': 10},
    'Içara': {'Criciuma': 15, 'Morro da Fumaça': 20},
    'Morro da Fumaça': {'Içara': 20, 'Orleans': 30},
    'Sombrio': {'Ararangua': 30, 'Turvo': 25},
    'Turvo': {'Sombrio': 25, 'Meleiro': 15},
    'Braço do Norte': {'Tubarão': 40, 'Orleans': 25},
    'Orleans': {'Braço do Norte': 25, 'Morro da Fumaça': 30},
    'Paulo Lopes': {'Garopaba': 10},
    'Meleiro': {'Turvo': 15}
}

grafo_linha_reta = {
    'Criciuma': {'Criciuma': 0, 'Ararangua': 40, 'Tubarão': 50, 'Içara': 15, 'Laguna': 80, 'Imbituba': 105, 'Garopaba': 125, 'Morro da Fumaça': 35, 'Sombrio': 70, 'Turvo': 90, 'Braço do Norte': 90, 'Orleans': 75, 'Paulo Lopes': 135, 'Meleiro': 105},
    'Ararangua': {'Criciuma': 40, 'Ararangua': 0, 'Tubarão': 85, 'Içara': 50, 'Laguna': 110, 'Imbituba': 135, 'Garopaba': 155, 'Morro da Fumaça': 60, 'Sombrio': 30, 'Turvo': 50, 'Braço do Norte': 125, 'Orleans': 110, 'Paulo Lopes': 165, 'Meleiro': 65},
    'Tubarão': {'Criciuma': 50, 'Ararangua': 85, 'Tubarão': 0, 'Içara': 65, 'Laguna': 30, 'Imbituba': 55, 'Garopaba': 75, 'Morro da Fumaça': 50, 'Sombrio': 115, 'Turvo': 135, 'Braço do Norte': 40, 'Orleans': 55, 'Paulo Lopes': 85, 'Meleiro': 150},
    'Içara': {'Criciuma': 15, 'Ararangua': 50, 'Tubarão': 65, 'Içara': 0, 'Laguna': 95, 'Imbituba': 120, 'Garopaba': 140, 'Morro da Fumaça': 20, 'Sombrio': 85, 'Turvo': 105, 'Braço do Norte': 85, 'Orleans': 70, 'Paulo Lopes': 150, 'Meleiro': 120},
    'Laguna': {'Criciuma': 80, 'Ararangua': 110, 'Tubarão': 30, 'Içara': 95, 'Laguna': 0, 'Imbituba': 25, 'Garopaba': 45, 'Morro da Fumaça': 70, 'Sombrio': 145, 'Turvo': 165, 'Braço do Norte': 70, 'Orleans': 85, 'Paulo Lopes': 55, 'Meleiro': 180},
    'Imbituba': {'Criciuma': 105, 'Ararangua': 135, 'Tubarão': 55, 'Içara': 120, 'Laguna': 25, 'Imbituba': 0, 'Garopaba': 20, 'Morro da Fumaça': 95, 'Sombrio': 170, 'Turvo': 190, 'Braço do Norte': 95, 'Orleans': 110, 'Paulo Lopes': 30, 'Meleiro': 205},
    'Garopaba': {'Criciuma': 125, 'Ararangua': 155, 'Tubarão': 75, 'Içara': 140, 'Laguna': 45, 'Imbituba': 20, 'Garopaba': 0, 'Morro da Fumaça': 115, 'Sombrio': 190, 'Turvo': 210, 'Braço do Norte': 115, 'Orleans': 130, 'Paulo Lopes': 10, 'Meleiro': 225},
    'Morro da Fumaça': {'Criciuma': 35, 'Ararangua': 60, 'Tubarão': 50, 'Içara': 20, 'Laguna': 70, 'Imbituba': 95, 'Garopaba': 115, 'Morro da Fumaça': 0, 'Sombrio': 100, 'Turvo': 120, 'Braço do Norte': 65, 'Orleans': 50, 'Paulo Lopes': 130, 'Meleiro': 135},
    'Sombrio': {'Criciuma': 70, 'Ararangua': 30, 'Tubarão': 115, 'Içara': 85, 'Laguna': 145, 'Imbituba': 170, 'Garopaba': 190, 'Morro da Fumaça': 100, 'Sombrio': 0, 'Turvo': 25, 'Braço do Norte': 155, 'Orleans': 140, 'Paulo Lopes': 200, 'Meleiro': 40},
    'Turvo': {'Criciuma': 90, 'Ararangua': 50, 'Tubarão': 135, 'Içara': 105, 'Laguna': 165, 'Imbituba': 190, 'Garopaba': 210, 'Morro da Fumaça': 120, 'Sombrio': 25, 'Turvo': 0, 'Braço do Norte': 175, 'Orleans': 160, 'Paulo Lopes': 220, 'Meleiro': 15},
    'Braço do Norte': {'Criciuma': 90, 'Ararangua': 125, 'Tubarão': 40, 'Içara': 85, 'Laguna': 70, 'Imbituba': 95, 'Garopaba': 115, 'Morro da Fumaça': 65, 'Sombrio': 155, 'Turvo': 175, 'Braço do Norte': 0, 'Orleans': 25, 'Paulo Lopes': 135, 'Meleiro': 190},
    'Orleans': {'Criciuma': 75, 'Ararangua': 110, 'Tubarão': 55, 'Içara': 70, 'Laguna': 85, 'Imbituba': 110, 'Garopaba': 130, 'Morro da Fumaça': 50, 'Sombrio': 140, 'Turvo': 160, 'Braço do Norte': 25, 'Orleans': 0, 'Paulo Lopes': 150, 'Meleiro': 175},
    'Paulo Lopes': {'Criciuma': 135, 'Ararangua': 165, 'Tubarão': 85, 'Içara': 150, 'Laguna': 55, 'Imbituba': 30, 'Garopaba': 10, 'Morro da Fumaça': 130, 'Sombrio': 200, 'Turvo': 220, 'Braço do Norte': 135, 'Orleans': 150, 'Paulo Lopes': 0, 'Meleiro': 235},
    'Meleiro': {'Criciuma': 105, 'Ararangua': 65, 'Tubarão': 150, 'Içara': 120, 'Laguna': 180, 'Imbituba': 205, 'Garopaba': 225, 'Morro da Fumaça': 135, 'Sombrio': 40, 'Turvo': 15, 'Braço do Norte': 190, 'Orleans': 175, 'Paulo Lopes': 235, 'Meleiro': 0}
}

def a_estrela(grafo_vizinhos, grafo_linha_reta, partida, objetivo):
    lista = []
    heapq.heappush(lista, (0, partida))  
    
    chegou_de = {partida: None} 
    
    g_var = {cidade: float('inf') for cidade in grafo_vizinhos}  
    g_var[partida] = 0 
    
    f_var = {cidade: float('inf') for cidade in grafo_vizinhos}  
    f_var[partida] = g_var[partida] + heuristica_linha_reta(grafo_linha_reta, partida, objetivo)
    
    while lista:
        f_atual, cidade_atual = heapq.heappop(lista)
        
        if cidade_atual == objetivo:
            caminho = []
            distancia_total = 0
            while cidade_atual:
                caminho.append(cidade_atual)
                if chegou_de[cidade_atual]:
                    cidade_anterior = chegou_de[cidade_atual]
                    distancia_total += grafo_vizinhos[cidade_anterior][cidade_atual]
                cidade_atual = chegou_de[cidade_atual]
            return caminho[::-1], distancia_total
        
        for vizinho, distancia in grafo_vizinhos[cidade_atual].items():
            g = g_var[cidade_atual] + distancia

            if g < g_var[vizinho]:
                chegou_de[vizinho] = cidade_atual
                g_var[vizinho] = g
                f_var[vizinho] = g_var[vizinho] + heuristica_linha_reta(grafo_linha_reta, vizinho, objetivo)  # Usa a heurística
                heapq.heappush(lista, (f_var[vizinho], vizinho))
    
    return None, 0  


def heuristica_linha_reta(grafo_linha_reta, cidade_atual, objetivo):
    
    return grafo_linha_reta[cidade_atual][objetivo]


cidadeinicial = 'Turvo'
cidadefinal = 'Laguna'


caminho, distancia_total = a_estrela(grafo_vizinhos, grafo_linha_reta, cidadeinicial, cidadefinal)
if caminho:
    print(f"Melhor caminho de {cidadeinicial} para {cidadefinal}: {' -> '.join(caminho)}")
    print(f"Distância total percorrida: {distancia_total} km")
else:
    print(f"Não foi possível encontrar um caminho de {cidadeinicial} para {cidadefinal}.")
