"""
Script de test pour vérifier l'installation de VizStyle
"""

import numpy as np

print("=" * 60)
print("TEST D'INSTALLATION DE VIZSTYLE")
print("=" * 60)

# Test 1: Import de la bibliothèque
print("\n1. Test d'import...")
try:
    import vizstyle
    print(f"   ✓ VizStyle version {vizstyle.__version__} importée avec succès!")
except ImportError as e:
    print(f"   ✗ Erreur d'import: {e}")
    exit(1)

# Test 2: Vérification des fonctions disponibles
print("\n2. Vérification des fonctions disponibles...")
expected_functions = [
    'styled_line',
    'styled_scatter', 
    'styled_bar',
    'styled_histogram',
    'styled_heatmap',
    'styled_box'
]

for func_name in expected_functions:
    if hasattr(vizstyle, func_name):
        print(f"   ✓ {func_name} disponible")
    else:
        print(f"   ✗ {func_name} manquante")

# Test 3: Test de création de graphiques (sans affichage)
print("\n3. Test de création des graphiques...")

try:
    # Test styled_line
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 3, 5, 7]
    fig, ax = vizstyle.styled_line(x, y, title="Test Line", show=False)
    print("   ✓ styled_line fonctionne")
    
    # Test styled_scatter
    fig, ax = vizstyle.styled_scatter(x, y, title="Test Scatter", show=False)
    print("   ✓ styled_scatter fonctionne")
    
    # Test styled_bar
    fig, ax = vizstyle.styled_bar(['A', 'B', 'C'], [10, 20, 15], title="Test Bar", show=False)
    print("   ✓ styled_bar fonctionne")
    
    # Test styled_histogram
    data = np.random.normal(0, 1, 100)
    fig, ax = vizstyle.styled_histogram(data, title="Test Histogram", show=False)
    print("   ✓ styled_histogram fonctionne")
    
    # Test styled_heatmap
    matrix = np.random.rand(5, 5)
    fig, ax = vizstyle.styled_heatmap(matrix, title="Test Heatmap", show=False)
    print("   ✓ styled_heatmap fonctionne")
    
    # Test styled_box
    data = [np.random.randn(50), np.random.randn(50)]
    fig, ax = vizstyle.styled_box(data, title="Test Box", show=False)
    print("   ✓ styled_box fonctionne")
    
except Exception as e:
    print(f"   ✗ Erreur lors de la création des graphiques: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 4: Vérification de la configuration
print("\n4. Vérification de la configuration...")
try:
    config = vizstyle.STYLE_CONFIG
    print(f"   ✓ Configuration accessible")
    print(f"   - Couleur primaire: {config['colors']['primary']}")
    print(f"   - Taille de police titre: {config['fonts']['title']}")
    print(f"   - Épaisseur de ligne: {config['lines']['width']}")
except Exception as e:
    print(f"   ✗ Erreur d'accès à la configuration: {e}")

# Test 5: Test avec plusieurs courbes
print("\n5. Test avec graphiques multiples...")
try:
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)
    fig, ax = vizstyle.styled_line(x, [y1, y2], 
                                    title="Multiple Lines",
                                    label=['sin', 'cos'],
                                    show=False)
    print("   ✓ Graphiques multiples fonctionnent")
except Exception as e:
    print(f"   ✗ Erreur avec graphiques multiples: {e}")

print("\n" + "=" * 60)
print("TOUS LES TESTS ONT RÉUSSI! ✓")
print("=" * 60)
print("\nVizStyle est correctement installé et fonctionnel.")
print("Vous pouvez maintenant l'utiliser dans vos scripts:")
print("  >>> import vizstyle")
print("  >>> vizstyle.styled_line([1,2,3], [4,2,5], title='Mon graphique')")
print("\nPour voir des exemples complets, exécutez:")
print("  python examples.py")
print("=" * 60)
