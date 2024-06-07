import matplotlib.pyplot as plt

brands = ["Pantene", "Ox", "Seda", "Tresseme", "Salon Line", "L'oreal", "Braé", "Kerastase", "Monday Haircare", "Clear", "Lolla Rio", "OGX", "Balai", "Bed Head", "Amend", "Alfaparf", "Inoar", "Bio Extratus", "Skala", "Truss", "Forever Liss", "Haskell"] 

followers = [565000, 155000, 471000, 186000, 3900000, 429000, 1200000, 2500000, 145000, 69000, 1100000, 42000, 63000, 44000, 518000, 284000, 981000, 1600000, 1900000, 1700000, 3200000, 1000000] 

# Preços ajustados 
prices_per_ml = [0.087, 0.172, 0.03, 0.035, 0.065, 0.104, 0.128, 0.62, 0.128, 0.08, 0.105, 0.15, 0.105, 0.30, 0.14, 0.38, 0.118, 0.096, 0.073, 0.302, 0.106, 0.13] 

# Criação do gráfico scatter plot 
plt.figure(figsize=(12, 8)) 
plt.scatter(followers, prices_per_ml, color='blue') 

# Adicionando nomes das marcas nos pontos 
for i, brand in enumerate(brands): 
    plt.text(followers[i], prices_per_ml[i], brand, fontsize=9, ha='right')

# Títulos e labels 
plt.title('Posicionamento de Marcas: Popularidade (seguidores no Instagram) vs. Preço por ml') 
plt.xlabel('Popularidade (número de seguidores no Instagram)') 
plt.ylabel('Preço por ml (R$)') 
plt.xscale('log')  # Escala logarítmica para popularidade para melhor visualização 
plt.grid(True) 

# Mostrar gráfico 
plt.show()