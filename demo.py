"""
Démonstration visuelle rapide de VizStyle
==========================================

Ce script génère 6 graphiques de démonstration en utilisant VizStyle
et les sauvegarde dans le répertoire courant.
"""

import numpy as np
import vizstyle
import matplotlib.pyplot as plt

print("=" * 60)
print("DÉMONSTRATION VIZSTYLE")
print("=" * 60)
print("\nGénération de 6 graphiques de démonstration...\n")

# Désactiver l'affichage interactif
plt.ioff()

# 1. Graphique en ligne
print("1/6 - Création du graphique en ligne...")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.exp(-x/10)

fig, ax = vizstyle.styled_line(
    x=x,
    y=[y1, y2, y3],
    title="Fonctions trigonométriques",
    xlabel="x",
    ylabel="y",
    label=['sin(x)', 'cos(x)', 'sin(x)·exp(-x/10)'],
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_01_line.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_01_line.png")

# 2. Nuage de points
print("2/6 - Création du nuage de points...")
np.random.seed(42)
x_scatter = np.random.randn(200)
y_scatter = 2 * x_scatter + np.random.randn(200) * 0.7
colors = x_scatter + y_scatter

fig, ax = vizstyle.styled_scatter(
    x=x_scatter,
    y=y_scatter,
    title="Nuage de points avec corrélation",
    xlabel="Variable X",
    ylabel="Variable Y",
    color=colors,
    size=80,
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_02_scatter.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_02_scatter.png")

# 3. Graphique en barres
print("3/6 - Création du graphique en barres...")
categories = ['Produit A', 'Produit B', 'Produit C', 'Produit D', 'Produit E']
q1 = [234, 456, 389, 512, 298]
q2 = [256, 478, 412, 495, 321]
q3 = [289, 501, 445, 534, 356]

fig, ax = vizstyle.styled_bar(
    x=categories,
    y=[q1, q2, q3],
    title="Ventes trimestrielles par produit",
    xlabel="Produits",
    ylabel="Ventes (unités)",
    labels=['T1 2024', 'T2 2024', 'T3 2024'],
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_03_bar.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_03_bar.png")

# 4. Histogramme
print("4/6 - Création de l'histogramme...")
data_bimodal = np.concatenate([
    np.random.normal(60, 8, 500),
    np.random.normal(120, 10, 500)
])

fig, ax = vizstyle.styled_histogram(
    data=data_bimodal,
    bins=40,
    title="Distribution bimodale des scores",
    xlabel="Score",
    ylabel="Densité",
    kde=True,
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_04_histogram.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_04_histogram.png")

# 5. Carte de chaleur
print("5/6 - Création de la carte de chaleur...")
n_vars = 8
data = np.random.randn(100, n_vars)
# Ajouter des corrélations
data[:, 1] = data[:, 0] * 0.8 + np.random.randn(100) * 0.2
data[:, 3] = data[:, 2] * 0.6 + np.random.randn(100) * 0.4
corr_matrix = np.corrcoef(data.T)
labels = [f'Var{i+1}' for i in range(n_vars)]

fig, ax = vizstyle.styled_heatmap(
    data=corr_matrix,
    title="Matrice de corrélation",
    xticklabels=labels,
    yticklabels=labels,
    cmap='RdBu_r',
    annot=True,
    fmt='.2f',
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_05_heatmap.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_05_heatmap.png")

# 6. Boîte à moustaches
print("6/6 - Création de la boîte à moustaches...")
groupe_A = np.random.normal(100, 15, 200)
groupe_B = np.random.normal(110, 20, 200)
groupe_C = np.random.normal(95, 12, 200)
groupe_D = np.random.normal(105, 18, 200)

fig, ax = vizstyle.styled_box(
    data=[groupe_A, groupe_B, groupe_C, groupe_D],
    labels=['Groupe A', 'Groupe B', 'Groupe C', 'Groupe D'],
    title="Comparaison des performances par groupe",
    ylabel="Score",
    show=False
)
fig.savefig('/mnt/user-data/outputs/demo_06_box.png', dpi=150, bbox_inches='tight')
plt.close(fig)
print("   ✓ Sauvegardé: demo_06_box.png")

print("\n" + "=" * 60)
print("✓ DÉMONSTRATION TERMINÉE AVEC SUCCÈS!")
print("=" * 60)
print("\n6 graphiques ont été générés avec succès:")
print("  - demo_01_line.png       (Graphique en ligne)")
print("  - demo_02_scatter.png    (Nuage de points)")
print("  - demo_03_bar.png        (Graphique en barres)")
print("  - demo_04_histogram.png  (Histogramme)")
print("  - demo_05_heatmap.png    (Carte de chaleur)")
print("  - demo_06_box.png        (Boîte à moustaches)")
print("\nTous les graphiques sont sauvegardés dans /mnt/user-data/outputs/")
print("=" * 60)
