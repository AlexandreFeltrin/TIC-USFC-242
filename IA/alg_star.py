import heapq

grafo = {
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

min_distancia = min(min(distancia.values()) for distancia in grafo.values())


def a_estrela(grafo, partida, objetivo):
    open_list = []
    heapq.heappush(open_list, (0, partida)) 
    
    chegou_de = {partida: None}  
    
    g_var = {cidade: float('inf') for cidade in grafo}  
    g_var[partida] = 0  
    
    f_var = {cidade: float('inf') for cidade in grafo}  
    f_var[partida] = g_var[partida] + min_distancia  
    
    while open_list:
        f_atual, cidade_atual = heapq.heappop(open_list)
        
        if cidade_atual == objetivo:
            caminho = []
            distancia_total = 0
            while cidade_atual:
                caminho.append(cidade_atual)
                if chegou_de[cidade_atual]:
                    cidade_anterior = chegou_de[cidade_atual]
                    distancia_total += grafo[cidade_anterior][cidade_atual]
                cidade_atual = chegou_de[cidade_atual]
            return caminho[::-1], distancia_total
        
 
        for vizinho, distancia in grafo[cidade_atual].items():
            tentativa_g = g_var[cidade_atual] + distancia
            
            if tentativa_g < g_var[vizinho]:
                chegou_de[vizinho] = cidade_atual
                g_var[vizinho] = tentativa_g
                f_var[vizinho] = g_var[vizinho] + min_distancia
                heapq.heappush(open_list, (f_var[vizinho], vizinho))
    
    return None, 0  

cidadeinicial = 'Turvo'
cidadefinal = 'Tubarão'

caminho, distancia_total = a_estrela(grafo, cidadeinicial, cidadefinal)
if caminho:
    print(f"Melhor caminho de {cidadeinicial} para {cidadefinal}: {' -> '.join(caminho)}")
    print(f"Distância total percorrida: {distancia_total} km")
else:
    print(f"Não foi possível encontrar um caminho de {cidadeinicial} para {cidadefinal}.")
